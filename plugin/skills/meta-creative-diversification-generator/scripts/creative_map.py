#!/usr/bin/env python3
"""Creative map: audit the creative mix of a Meta ad account (stdlib only).

Deterministic analysis script shipped inside the creative-diversification-generator
skill and run by the Ad Superpowers ScriptExecutor. It is invoked as
``python3 creative_map.py --input <file.json>`` (the executor may add
``--format``), its stdout is parsed as JSON, and success = (returncode == 0).

Exit 0 with a JSON result; exit 2 with ``{"errors": [...], "allowed_values": {...}}``
on stdout for caller errors (invalid input or arguments) so the model sees why.
Every result carries a ``warnings`` array: the model can relay a warning, it
cannot relay silence.

Input contract (the caller joins creatives and insights onto each ad):

    {
      "mode": "xray",                      # xray | analyze | plan | compare
      "model": "ecommerce",                # or "leadgen" (sets the KPI action)
      "as_of": "YYYY-MM-DD",               # window end; required for freshness
      "account_name": "...",               # optional, display only
      "ads": [
        {
          "id": "123",
          "name": "Spring launch [cs:M1-EMO-CRT-w1]",   # optional; a tag becomes labels
          "effective_status": "ACTIVE",
          "created_time": "2026-10-06T09:00:00+0000",
          "adset_id": "456",
          "creative": {"image_hash": "...", "video_id": "...",
                       "body": "...", "title": "..."},
          "insights": {
            "spend": "100.0", "impressions": "10000",
            "actions": [{"action_type": "purchase", "value": "5",
                         "incrementality": "2"}],
            "action_values": [{"action_type": "purchase", "value": "500",
                               "incrementality": "200"}]
          },
          "labels": {"motivator": "M1", "angle": "EMO", "execution": "CRT"}
        }
      ],
      "labels_by_creative": {"c1a2b3c4": "M1-EMO-CRT"},   # analyze/plan; keys from xray
      "taxonomy": {"motivators": [...], "angles": [...],     # plan only
                   "cells": [["M3", "EMO"], ...]},          # optional ranked cells
      "before": {"ads": [...]}, "after": {"ads": [...]},    # compare only; each window may
                                                            # carry account_totals and as_of
      "wave": 2, "launch_date": "YYYY-MM-DD", "days": 14,   # compare, optional
      "read_back": {"wave": 2, "launch_date": "...",        # compare, set by the server feed
                    "launch_source": "delivery", "days": 14},
      "daily_budget": 100, "target_cpa": 35, "test_share": 0.2  # plan only
    }

Incremental figures need ``action_attribution_windows=incrementality`` in the
insights request; when the key is absent the script reports
``incrementality_available: false`` and nulls (never a misleading 0). Label codes
are opaque placeholders supplied by the caller; the script never invents them.

xray also returns a ``creatives`` inventory (one row per distinct creative, by
spend, with a stable ``key``) so the caller can label creatives once and pass
``labels_by_creative`` instead of labelling every ad. Label precedence per ad:
explicit ``labels`` > ``labels_by_creative`` > a ``[cs:...]`` tag in the ad name.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from datetime import date
from typing import Any

MODES = ("xray", "analyze", "plan", "compare")

_WS_RE = re.compile(r"\s+")
# Creative-strategy tag in an ad name: [cs:<motivator>-<angle>-<execution>-w<wave>].
_TAG_RE = re.compile(r"\[cs:(M\d{1,2})-([A-Z]{3})-([A-Z]{2,3})-w(\d{1,3})\]")
LABEL_KEYS = ("motivator", "angle", "execution")

# The inventory lists creatives until this share of resolved spend is covered,
# capped so the output stays small even for very large accounts.
INVENTORY_SPEND_COVERAGE = 0.95
INVENTORY_MAX_ROWS = 60
ADSET_MAX_ROWS = 30
COPY_EXCERPT_CHARS = 100
# The formats an ad set can miss: a media kind, not an aspect ratio.
AD_FORMATS = ("image", "video")

# Reading floors for a comparison: below them one more result moves the index by
# 20% or more, so the script says "too early" instead of ahead/behind.
INTEGRITY_TOLERANCE = 0.005  # 0.5% of account spend: rounding, not missing ads
INVENTORY_AD_IDS = 3
SHARPEN_COVERAGE = 0.80  # ad ids per inventory row, enough to fetch a preview

MIN_IMPRESSIONS_TO_READ = 2000
MIN_RESULTS_TO_READ = 5
INDEX_AHEAD = 1.15
INDEX_BEHIND = 0.85
# A read-back of one or two days holds too few results for any cell to read.
READ_BACK_TOO_YOUNG_DAYS = 2

_RANKING_FIELDS = (
    ("quality", "quality_ranking"),
    ("engagement", "engagement_rate_ranking"),
    ("conversion", "conversion_rate_ranking"),
)


class ToolInputError(Exception):
    """A caller-input error that maps to the exit-2 envelope."""


class _EnvelopeArgumentParser(argparse.ArgumentParser):
    """argparse that reports errors as the stdout envelope + exit 2, not stderr."""

    def error(self, message: str) -> Any:  # noqa: D401 - argparse hook
        fail([f"Argument error: {message}"], {"mode": list(MODES)})


def fail(errors: list[str], allowed: dict[str, Any]) -> None:
    """Print a caller-error envelope on stdout and exit 2 (not billed)."""
    print(json.dumps({"errors": errors, "allowed_values": allowed}, ensure_ascii=False))
    raise SystemExit(2)


def compute_run_id(data: dict) -> str:
    """Deterministic, input-derived id so the same audit always carries the same tag."""
    canonical = json.dumps(data, sort_keys=True, ensure_ascii=False, default=str)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return "r-" + digest[:8]


def as_float(value: Any, default: float = 0.0) -> float:
    """Coerce Meta's string numerics safely; non-finite (NaN/Infinity) -> default."""
    if value is None:
        return default
    try:
        result = float(value)
    except (TypeError, ValueError):
        return default
    return result if math.isfinite(result) else default


def normalize_copy(text: Any) -> str:
    """Lowercase, trim and collapse whitespace so trivially different copy matches."""
    if not isinstance(text, str):
        return ""
    return _WS_RE.sub(" ", text.strip().lower())


def _collect_media_keys(creative: dict, keys: set[str]) -> None:
    """Gather image/video identities from a creative and its nested specs."""
    if not isinstance(creative, dict):
        return
    for key in ("image_hash", "video_id"):
        val = creative.get(key)
        if val:
            keys.add(f"{key}:{val}")
    oss = creative.get("object_story_spec")
    if isinstance(oss, dict):
        for sub in ("link_data", "video_data"):
            node = oss.get(sub)
            if isinstance(node, dict):
                _collect_media_keys(node, keys)
        link_data = oss.get("link_data")
        if isinstance(link_data, dict):
            for child in link_data.get("child_attachments") or []:
                if isinstance(child, dict):
                    _collect_media_keys(child, keys)
    afs = creative.get("asset_feed_spec")
    if isinstance(afs, dict):
        for img in afs.get("images") or []:
            if isinstance(img, dict) and img.get("hash"):
                keys.add(f"image_hash:{img['hash']}")
        for vid in afs.get("videos") or []:
            if isinstance(vid, dict) and vid.get("video_id"):
                keys.add(f"video_id:{vid['video_id']}")


# Copy fields that are shown to the viewer. 'name' (the creative's internal name)
# is deliberately excluded: it would split two otherwise identical creatives.
_COPY_FIELDS = ("body", "title", "message", "description")


def _collect_copy(creative: dict, pairs: list[str]) -> None:
    """Gather viewer-facing copy as 'field=normalized' so body/title keep identity."""
    if not isinstance(creative, dict):
        return
    for key in _COPY_FIELDS:
        if creative.get(key):
            pairs.append(f"{key}={normalize_copy(creative[key])}")
    oss = creative.get("object_story_spec")
    if isinstance(oss, dict):
        for sub in ("link_data", "video_data"):
            node = oss.get(sub)
            if isinstance(node, dict):
                _collect_copy(node, pairs)
        link_data = oss.get("link_data")
        if isinstance(link_data, dict):
            for child in link_data.get("child_attachments") or []:
                if isinstance(child, dict):
                    _collect_copy(child, pairs)
    afs = creative.get("asset_feed_spec")
    if isinstance(afs, dict):
        for field in ("bodies", "titles", "descriptions"):
            for item in afs.get(field) or []:
                if isinstance(item, dict) and item.get("text"):
                    pairs.append(f"{field}={normalize_copy(item['text'])}")


def fingerprint(ad: dict) -> str | None:
    """A creative fingerprint: media identities plus field-tagged copy.

    Returns None when neither a media key nor any copy can be derived, so the
    ad's spend is reported as unresolved rather than silently merged.
    """
    creative = ad.get("creative") if isinstance(ad, dict) else None
    if not isinstance(creative, dict):
        return None
    media: set[str] = set()
    pairs: list[str] = []
    _collect_media_keys(creative, media)
    _collect_copy(creative, pairs)
    copy_sig = " | ".join(sorted(p for p in pairs if p))
    media_sig = " ".join(sorted(media))
    if not media_sig and not copy_sig:
        return None
    return f"media[{media_sig}]copy[{copy_sig}]"


def creative_key(fp: str) -> str:
    """Short, stable id for a distinct creative (same fingerprint -> same key)."""
    return "c" + hashlib.sha256(fp.encode("utf-8")).hexdigest()[:7]


def media_kind(creative: Any) -> str:
    """Coarse media type from the creative fields: no ratio, no judgment."""
    if not isinstance(creative, dict):
        return "none"
    oss = creative.get("object_story_spec")
    link_data = oss.get("link_data") if isinstance(oss, dict) else None
    if isinstance(link_data, dict) and link_data.get("child_attachments"):
        return "carousel"
    afs = creative.get("asset_feed_spec")
    if isinstance(afs, dict):
        if len(afs.get("images") or []) + len(afs.get("videos") or []) > 1:
            return "flexible"
    media: set[str] = set()
    _collect_media_keys(creative, media)
    if any(k.startswith("video_id:") for k in media):
        return "video"
    if media:
        return "image"
    return "none"


def ad_formats(creative: Any) -> set[str]:
    """The image and video formats an ad shows.

    Not the media keys: a video's required thumbnail ``image_hash`` inside
    ``video_data`` would make every video ad look like an image as well.
    """
    kind = media_kind(creative)
    if kind in AD_FORMATS:
        return {kind}
    found: set[str] = set()
    if kind == "carousel":
        for child in creative["object_story_spec"]["link_data"]["child_attachments"] or []:
            if isinstance(child, dict) and child.get("video_id"):
                found.add("video")
            elif isinstance(child, dict) and child.get("image_hash"):
                found.add("image")
    elif kind == "flexible":
        afs = creative["asset_feed_spec"]
        if any(isinstance(i, dict) and i.get("hash") for i in afs.get("images") or []):
            found.add("image")
        if any(isinstance(v, dict) and v.get("video_id") for v in afs.get("videos") or []):
            found.add("video")
    return found


def _creative_id(creative: Any) -> str | None:
    """Meta's creative id when the read included it (needed for a creative-level preview)."""
    if isinstance(creative, dict) and creative.get("id") is not None:
        return str(creative["id"])
    return None


def copy_excerpt(creative: Any) -> str:
    """The first viewer-facing copy line, whitespace-collapsed and truncated."""
    pairs: list[str] = []
    if isinstance(creative, dict):
        nodes = [creative]
        oss = creative.get("object_story_spec")
        if isinstance(oss, dict):
            nodes += [oss.get(k) for k in ("link_data", "video_data") if isinstance(oss.get(k), dict)]
        for node in nodes:
            for key in _COPY_FIELDS:
                if isinstance(node.get(key), str) and node[key].strip():
                    pairs.append(node[key])
        afs = creative.get("asset_feed_spec")
        if isinstance(afs, dict):
            for field in ("bodies", "titles"):
                for item in afs.get(field) or []:
                    if isinstance(item, dict) and isinstance(item.get("text"), str):
                        pairs.append(item["text"])
    if not pairs:
        return ""
    text = _WS_RE.sub(" ", pairs[0].strip())
    return text if len(text) <= COPY_EXCERPT_CHARS else text[: COPY_EXCERPT_CHARS - 3] + "..."


def _action_value(insights: Any, action_type: str) -> float | None:
    """Sum of one action_type's 'value' in insights.actions, or None when absent."""
    if not isinstance(insights, dict):
        return None
    found = False
    total = 0.0
    for entry in insights.get("actions") or []:
        if isinstance(entry, dict) and entry.get("action_type") == action_type:
            found = True
            total += as_float(entry.get("value"))
    return total if found else None


def ad_spend(ad: dict) -> float:
    insights = ad.get("insights") if isinstance(ad, dict) else None
    if isinstance(insights, dict):
        return as_float(insights.get("spend"))
    return 0.0


def read_ads(container: dict, warnings: list[str], label: str = "ads") -> list[dict]:
    """Extract the ad list, failing closed on a wrong-typed ``ads`` key."""
    raw = container.get("ads")
    if raw is None:
        return []
    if not isinstance(raw, list):
        raise ToolInputError(f"'{label}' must be a list of ad objects.")
    ads = [a for a in raw if isinstance(a, dict)]
    if len(ads) != len(raw):
        warnings.append(f"{len(raw) - len(ads)} non-object entries in '{label}' were ignored.")
    # One ad counts once in every mode: a repeated id would double its spend and results.
    unique: list[dict] = []
    seen_ids: set[Any] = set()
    for ad in ads:
        ad_id = ad.get("id")
        if ad_id is not None:
            if ad_id in seen_ids:
                continue
            seen_ids.add(ad_id)
        unique.append(ad)
    if len(unique) != len(ads):
        warnings.append(f"{len(ads) - len(unique)} duplicate ad id(s) ignored.")
    return unique


def group_creatives(
    ads: list[dict], warnings: list[str]
) -> tuple[dict[str, dict], float, int]:
    """Group ads into distinct creatives by fingerprint; dedupe repeated ad ids.

    Returns (groups, unresolved_spend, processed_ad_count) where processed counts
    the unique ads (duplicates removed), resolved and unresolved alike.
    """
    groups: dict[str, dict] = {}
    unresolved = 0.0
    seen_ids: set[str] = set()
    duplicates = 0
    processed = 0
    for ad in ads:
        ad_id = ad.get("id")
        if ad_id is not None:
            if ad_id in seen_ids:
                duplicates += 1
                continue
            seen_ids.add(ad_id)
        processed += 1
        fp = fingerprint(ad)
        spend = ad_spend(ad)
        if fp is None:
            unresolved += spend
            continue
        g = groups.setdefault(
            fp, {"spend": 0.0, "ad_ids": [], "created": [], "creative": ad.get("creative"),
                 "impressions": 0.0, "video_views": 0.0, "with_view": False,
                 "top_spend": -1.0, "rankings": {}, "ad_spends": [], "tag": None}
        )
        insights = ad.get("insights") if isinstance(ad.get("insights"), dict) else {}
        g["impressions"] += as_float(insights.get("impressions"))
        views = _action_value(insights, "video_view")
        if views is not None:
            g["video_views"] += views
            g["with_view"] = True
        if spend > g["top_spend"]:
            # Meta's relevance rankings are per ad; show those of the stack's biggest ad.
            g["top_spend"] = spend
            g["rankings"] = {
                short: insights[field]
                for short, field in _RANKING_FIELDS
                if isinstance(insights.get(field), str) and insights[field]
            }
        g["spend"] += spend
        g["ad_ids"].append(ad_id)
        if ad_id is not None:
            g["ad_spends"].append((spend, str(ad_id)))
        tag = parse_tag(ad_name(ad))
        if g["tag"] is None and tag:
            g["tag"] = "{motivator}-{angle}-{execution}-w{wave}".format(**tag)
        created = ad.get("created_time")
        if created:
            g["created"].append(created)
    if duplicates:
        warnings.append(f"{duplicates} duplicate ad id(s) ignored.")
    return groups, unresolved, processed


def effective_count(shares: list[float]) -> float:
    """Inverse Herfindahl: 1 / sum(share^2). The 'spread as evenly as N' number."""
    sq = sum(s * s for s in shares)
    return 1.0 / sq if sq > 0 else 0.0


def parse_day(value: Any) -> date | None:
    """Parse the date part of an ISO timestamp ('YYYY-MM-DD...'); day granularity only."""
    if not isinstance(value, str) or len(value) < 10:
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


def kpi_action_type(data: dict) -> str:
    """The conversion action type for this business model (overridable)."""
    if data.get("kpi_action"):
        return str(data["kpi_action"])
    return "lead" if data.get("model") == "leadgen" else "purchase"


def _sum_action(ads: list[dict], container: str, action_type: str) -> tuple[float, float, bool]:
    """Sum value and incrementality for one action_type across ads' actions/action_values."""
    total_value = 0.0
    total_incr = 0.0
    has_incr = False
    for ad in ads:
        insights = ad.get("insights")
        if not isinstance(insights, dict):
            continue
        for entry in insights.get(container) or []:
            if isinstance(entry, dict) and entry.get("action_type") == action_type:
                total_value += as_float(entry.get("value"))
                if "incrementality" in entry:
                    has_incr = True
                    total_incr += as_float(entry.get("incrementality"))
    return total_value, total_incr, has_incr


def incremental_block(
    data: dict, ads: list[dict], total_spend: float, warnings: list[str]
) -> dict[str, Any]:
    """Meta's own incremental model (action_attribution_windows=incrementality).

    Summed per-ad incrementality fell short of the account row in our
    measurements (90 against 92). When account_totals carries the account's
    spend and its actions or action values, the KPI line uses that row and its
    spend; otherwise it sums the ads. Never account numerators over ad spend.
    """
    kpi = kpi_action_type(data)
    totals = data.get("account_totals")
    if (
        isinstance(totals, dict)
        and totals.get("spend") is not None
        and (isinstance(totals.get("actions"), list) or isinstance(totals.get("action_values"), list))
    ):
        basis, rows = "account", [{"insights": totals}]
        total_spend = as_float(totals.get("spend"))
    else:
        basis, rows = "ads", ads
    conv, iconv, has_i1 = _sum_action(rows, "actions", kpi)
    rev, irev, has_i2 = _sum_action(rows, "action_values", kpi)
    available = has_i1 or has_i2
    block: dict[str, Any] = {
        "kpi_action": kpi,
        "basis": basis,
        # The spend this block divides by: the account's on the account basis.
        "spend": round(total_spend, 2),
        "conversions": round(conv, 2),
        "revenue": round(rev, 2),
        "incrementality_available": available,
    }
    if total_spend > 0:
        block["roas"] = round(rev / total_spend, 2)
    # CPA for e-commerce, CPL for lead gen: spend per KPI action.
    block["cost_per_result"] = round(total_spend / conv, 2) if conv > 0 else None
    # Each incremental figure needs its own key: lead gen has no action_values at all,
    # so a missing revenue incrementality is "not available", never 0.
    block["incremental_conversions"] = round(iconv, 2) if has_i1 else None
    block["incremental_revenue"] = round(irev, 2) if has_i2 else None
    block["iroas"] = round(irev / total_spend, 2) if has_i2 and total_spend > 0 else None
    block["incremental_cost_per_result"] = (
        round(total_spend / iconv, 2) if has_i1 and iconv > 0 else None
    )
    if conv == 0 and rev == 0:
        # Nothing to attribute: asking for incrementality would mislead.
        warnings.append(f"No '{kpi}' conversions found; check kpi_action / model.")
    elif not available:
        warnings.append(
            "No incrementality in the input; request "
            "action_attribution_windows=incrementality to show Meta's incremental model."
        )
    return block


def freshness_block(
    groups: dict[str, dict], resolved_spend: float, as_of: Any, warnings: list[str]
) -> dict[str, Any]:
    """Age of the freshest creative that still carries >=10% of resolved spend.

    The reference date is the caller's ``as_of`` only; it is never derived from
    the data (that would make every newest creative look fresh by construction).
    """
    asof_day = parse_day(as_of)
    if asof_day is None:
        warnings.append("as_of missing or unparseable; freshness not computed.")
        return {"as_of": None, "newest_high_spend_age_days": None, "has_fresh_high_spend_21d": False}

    ages: list[int] = []
    future = False
    if resolved_spend > 0:
        for g in groups.values():
            if g["spend"] / resolved_spend < 0.10:
                continue
            created = [d for d in (parse_day(c) for c in g["created"]) if d is not None]
            if not created:
                continue
            # A creative is as old as its FIRST launch, not the newest ad in the stack.
            age = (asof_day - min(created)).days
            if age < 0:
                future = True
                continue
            ages.append(age)
    if future:
        warnings.append("Some creatives have a created_time after as_of; ignored for freshness.")
    return {
        "as_of": asof_day.isoformat(),
        "newest_high_spend_age_days": min(ages) if ages else None,
        "has_fresh_high_spend_21d": any(age <= 21 for age in ages),
    }


def hook_rate_block(ads: list[dict], warnings: list[str]) -> dict[str, Any]:
    """3-second plays / impressions over video ads; uses actions[video_view]."""
    views = 0.0
    impressions = 0.0
    video_ads = 0
    with_view = 0
    for ad in ads:
        creative = ad.get("creative")
        media: set[str] = set()
        if isinstance(creative, dict):
            _collect_media_keys(creative, media)
        if not any(k.startswith("video_id:") for k in media):
            continue
        video_ads += 1
        insights = ad.get("insights")
        if not isinstance(insights, dict):
            continue
        impressions += as_float(insights.get("impressions"))
        ad_has_view = False
        for entry in insights.get("actions") or []:
            if isinstance(entry, dict) and entry.get("action_type") == "video_view":
                views += as_float(entry.get("value"))
                ad_has_view = True
        if ad_has_view:
            with_view += 1
    rate = round(views / impressions, 4) if impressions > 0 and with_view > 0 else None
    if video_ads and not with_view:
        warnings.append("Video ads present but no video_view actions; hook rate unavailable.")
    return {"rate": rate, "video_ads": video_ads, "with_video_view": with_view}


def _labels_from_value(value: Any) -> dict[str, str]:
    """Labels from a dict or a compact 'M1-EMO-CRT' string; empty parts are dropped."""
    if isinstance(value, str):
        # A short form like "M1-EMO" is allowed: missing parts stay unset.
        value = dict(zip(LABEL_KEYS, value.split("-"), strict=False))
    if not isinstance(value, dict):
        return {}
    out: dict[str, str] = {}
    for key in LABEL_KEYS:
        val = value.get(key)
        if isinstance(val, str) and val.strip():
            out[key] = val.strip()
    return out


def parse_tag(name: Any) -> dict[str, str]:
    """Labels from a '[cs:M2-PRB-DEM-w1]' tag in an ad name, or {} when absent."""
    if not isinstance(name, str):
        return {}
    match = _TAG_RE.search(name)
    if not match:
        return {}
    return dict(zip(LABEL_KEYS + ("wave",), match.groups(), strict=True))


def ad_name(ad: dict) -> Any:
    """The ad's name, else the name on its insights row: an ad the creative read missed keeps its tag."""
    name = ad.get("name")
    if isinstance(name, str) and name:
        return name
    insights = ad.get("insights")
    return insights.get("ad_name") if isinstance(insights, dict) else None


def _has_motivator(labels: dict[str, str]) -> bool:
    # "M0" is the code for "cannot tell": it counts as unlabelled everywhere.
    return bool(labels.get("motivator")) and labels["motivator"] != "M0"


def resolve_labels(data: dict, ads: list[dict]) -> tuple[list[tuple[dict, dict[str, str]]], dict[str, int]]:
    """Each ad with its labels: explicit labels > labels_by_creative > name tag.

    labels_by_creative holds what the user confirmed in this audit, so it beats a
    tag written at launch; a tag still labels every creative the audit left open.
    """
    by_creative = data.get("labels_by_creative")
    if by_creative is None:
        by_creative = {}
    if not isinstance(by_creative, dict):
        raise ToolInputError("'labels_by_creative' must map creative keys to label codes.")
    resolved: list[tuple[dict, dict[str, str]]] = []
    sources = {"ad": 0, "tag": 0, "creative": 0, "none": 0}
    for ad in ads:
        labels, source = _labels_from_value(ad.get("labels")), "ad"
        if not _has_motivator(labels) and by_creative:
            fp = fingerprint(ad)
            if fp is not None:
                labels, source = _labels_from_value(by_creative.get(creative_key(fp))), "creative"
        if not _has_motivator(labels):
            labels, source = parse_tag(ad_name(ad)), "tag"
        if not _has_motivator(labels):
            labels, source = {}, "none"
        sources[source] += 1
        resolved.append((ad, labels))
    return resolved, sources


def xray(data: dict, ads: list[dict], warnings: list[str]) -> dict[str, Any]:
    groups, unresolved, processed = group_creatives(ads, warnings)
    resolved_spend = sum(g["spend"] for g in groups.values())
    total_spend = resolved_spend + unresolved
    shares = (
        sorted((g["spend"] / resolved_spend for g in groups.values()), reverse=True)
        if resolved_spend > 0
        else []
    )
    if unresolved > 0:
        warnings.append(
            f"{round(unresolved, 2)} spend is unresolved (ads without a creative fingerprint)."
        )
    if resolved_spend == 0:
        warnings.append("No resolved spend in the window; concentration measures are null.")
    hook = hook_rate_block(ads, warnings)
    inventory = inventory_block(groups, resolved_spend)
    media_spend: dict[str, float] = {}
    for g in groups.values():
        kind = media_kind(g["creative"])
        media_spend[kind] = media_spend.get(kind, 0.0) + g["spend"]
    if unresolved > 0:
        media_spend["unresolved"] = unresolved
    return {
        "total_ads": processed,
        "distinct_creatives": len(groups),
        "effective_creatives": round(effective_count(shares), 1) if shares else None,
        "top3_spend_share_pct": round(sum(shares[:3]) * 100, 1) if shares else None,
        # What the top 3 would hold under a perfectly even split: the ruler line.
        "even_split_top3_pct": round(min(3, len(groups)) / len(groups) * 100, 1) if shares else None,
        "total_spend": round(total_spend, 2),
        "unresolved_spend": round(unresolved, 2),
        "duplicate_stacks": sum(1 for g in groups.values() if len(g["ad_ids"]) > 1),
        "media_mix_pct": _mix_pct(media_spend, total_spend),
        "integrity": integrity_block(data, total_spend, warnings),
        "hook_rate": hook["rate"],
        "hook_rate_basis": {"video_ads": hook["video_ads"], "with_video_view": hook["with_video_view"]},
        "freshness": freshness_block(groups, resolved_spend, data.get("as_of"), warnings),
        "incremental": incremental_block(data, ads, total_spend, warnings),
        **inventory,
        **adset_block(ads, total_spend, warnings),
    }


def integrity_block(data: dict, ads_spend: float, warnings: list[str]) -> dict[str, Any] | None:
    """Compare the ads' spend with the account total for the same window, when supplied.

    A gap means ads are missing from the read (a status filter, a page cut short);
    every measure would then describe only part of the account.
    """
    totals = data.get("account_totals")
    if not isinstance(totals, dict) or totals.get("spend") is None:
        return None
    account_spend = as_float(totals.get("spend"))
    gap = round(account_spend - ads_spend, 2)
    tolerance = max(0.01, INTEGRITY_TOLERANCE * account_spend)
    matches = abs(gap) <= tolerance
    if not matches:
        warnings.append(
            f"The ads' spend ({round(ads_spend, 2)}) differs from the account total "
            f"({round(account_spend, 2)}) by {gap}; ads are missing from the read."
        )
    return {
        "account_spend": round(account_spend, 2),
        "ads_spend": round(ads_spend, 2),
        "gap": gap,
        "gap_pct": round(gap / account_spend * 100, 2) if account_spend > 0 else None,
        "matches": matches,
    }


def inventory_block(groups: dict[str, dict], resolved_spend: float) -> dict[str, Any]:
    """One row per distinct creative, by spend, until the coverage share or row cap."""
    ordered = sorted(groups.items(), key=lambda kv: (-kv[1]["spend"], creative_key(kv[0])))
    rows: list[dict[str, Any]] = []
    covered = 0.0
    for fp, g in ordered:
        if len(rows) >= INVENTORY_MAX_ROWS:
            break
        if rows and resolved_spend > 0 and covered / resolved_spend >= INVENTORY_SPEND_COVERAGE:
            break
        created = [d for d in (parse_day(c) for c in g["created"]) if d is not None]
        media = media_kind(g["creative"])
        hook = None
        if media in ("video", "flexible") and g["with_view"] and g["impressions"] > 0:
            hook = round(g["video_views"] / g["impressions"], 4)
        rows.append({
            "key": creative_key(fp),
            "spend": round(g["spend"], 2),
            "share_pct": round(g["spend"] / resolved_spend * 100, 1) if resolved_spend > 0 else 0.0,
            "ads": len(g["ad_ids"]),
            "media": media,
            "first_launch": min(created).isoformat() if created else None,
            "impressions": int(g["impressions"]),
            "hook_rate": hook,
            "hook_band": None,
            "rankings": g["rankings"],
            # Where to look: the biggest ads (for a preview) and any launch tag.
            "ad_ids": [i for _s, i in sorted(g["ad_spends"], key=lambda t: (-t[0], t[1]))][:INVENTORY_AD_IDS],
            "creative_id": _creative_id(g["creative"]),
            "tag": g["tag"],
            "copy": copy_excerpt(g["creative"]),
        })
        covered += g["spend"]
    _assign_hook_bands(rows)
    omitted = ordered[len(rows):]
    return {
        "creatives": rows,
        "creatives_omitted": len(omitted),
        "omitted_spend": round(sum(g["spend"] for _, g in omitted), 2),
    }


def adset_block(ads: list[dict], total_spend: float, warnings: list[str]) -> dict[str, Any]:
    """Spend, media kinds and missing formats per ad set, by spend, until the coverage share or row cap.

    Shares are of total spend: an ad without a readable creative still belongs to
    its set (the insights row carries ``adset_id`` when the ad node is missing).
    """
    sets: dict[str, dict] = {}
    unknown = 0
    for ad in ads:
        insights = ad.get("insights") if isinstance(ad.get("insights"), dict) else {}
        set_id = ad.get("adset_id") or insights.get("adset_id")
        if not set_id:
            unknown += 1
            set_id = "unknown"
        s = sets.setdefault(str(set_id), {"spend": 0.0, "ads": 0, "media": {}, "formats": set()})
        spend = ad_spend(ad)
        s["spend"] += spend
        s["ads"] += 1
        if fingerprint(ad) is None:
            kind = "unresolved"
        else:
            kind = media_kind(ad.get("creative"))
            s["formats"] |= ad_formats(ad.get("creative"))
        s["media"][kind] = s["media"].get(kind, 0.0) + spend
    if unknown:
        warnings.append(f"{unknown} ad(s) without an adset_id are grouped as 'unknown'.")
    ordered = sorted(sets.items(), key=lambda kv: (-kv[1]["spend"], kv[0]))
    rows: list[dict[str, Any]] = []
    covered = 0.0
    for set_id, s in ordered:
        if len(rows) >= ADSET_MAX_ROWS:
            break
        if rows and total_spend > 0 and covered / total_spend >= INVENTORY_SPEND_COVERAGE:
            break
        # Without one ad whose media kind the script can read, the set's formats are
        # unknown, not missing (an unread ad, or a copy-only boosted post).
        known = bool(s["formats"])
        rows.append({
            "adset_id": set_id,
            "spend": round(s["spend"], 2),
            "share_pct": round(s["spend"] / total_spend * 100, 1) if total_spend > 0 else 0.0,
            "ads": s["ads"],
            "media_mix_pct": _mix_pct(s["media"], s["spend"]),
            "has_image": "image" in s["formats"] if known else None,
            "has_video": "video" in s["formats"] if known else None,
            "missing": [f for f in AD_FORMATS if f not in s["formats"]] if known else None,
        })
        covered += s["spend"]
    omitted = ordered[len(rows):]
    return {
        "adsets": rows,
        "adsets_omitted": len(omitted),
        "adsets_omitted_spend": round(sum(s["spend"] for _, s in omitted), 2),
    }


def _mix_pct(spend_by: dict[str, float], total: float) -> dict[str, float]:
    """Spend share per key in percent, biggest first (ties by key), for snapshot lines."""
    if total <= 0:
        return {}
    ordered = sorted(spend_by.items(), key=lambda kv: (-kv[1], kv[0]))
    return {k: round(v / total * 100, 1) for k, v in ordered}


def _assign_hook_bands(rows: list[dict[str, Any]]) -> None:
    """Mark the bottom and top quarter of hook rates within this account's listed videos.

    Only creatives past the impression floor take part, and only when at least four
    do; a quarter of fewer is not a distribution. Ties break on the creative key.
    """
    eligible = [
        r for r in rows
        if r["hook_rate"] is not None and r["impressions"] >= MIN_IMPRESSIONS_TO_READ
    ]
    if len(eligible) < 4:
        return
    eligible.sort(key=lambda r: (r["hook_rate"], r["key"]))
    k = len(eligible) // 4
    for r in eligible:
        r["hook_band"] = "middle"
    for r in eligible[:k]:
        r["hook_band"] = "bottom_quarter"
    for r in eligible[-k:]:
        r["hook_band"] = "top_quarter"


def _read(index: float | None, impressions: float, results: float) -> str:
    """Ahead/behind/level against the layer, or too_early below the reading floors."""
    if index is None or impressions < MIN_IMPRESSIONS_TO_READ or results < MIN_RESULTS_TO_READ:
        return "too_early"
    if index >= INDEX_AHEAD:
        return "ahead"
    if index <= INDEX_BEHIND:
        return "behind"
    return "level"


def _quadrant(read: str, spend: float, even_spend: float) -> str:
    """The cell's read crossed with its spend against an even split over the cells.

    Classified on exact spend, like the read on the exact ratio (isclose: equal
    cells sum to a float a hair above their own spend); level and too_early
    carry no quadrant and pass the read through.
    """
    if read not in ("ahead", "behind"):
        return read
    large = spend >= even_spend or math.isclose(spend, even_spend)
    return f"{read}_{'large' if large else 'small'}_share"


def sharpen_block(resolved: list[tuple[dict, dict[str, str]]]) -> dict[str, Any]:
    """The fewest creatives that carry 80% of the spend whose execution was not seen."""
    unseen: dict[str, float] = {}
    for ad, labels in resolved:
        execution = labels.get("execution")
        if execution and execution != "NV":
            continue
        fp = fingerprint(ad)
        if fp is None:
            continue  # unresolved spend has no creative to preview
        key = creative_key(fp)
        unseen[key] = unseen.get(key, 0.0) + ad_spend(ad)
    total = sum(unseen.values())
    keys: list[str] = []
    covered = 0.0
    for key, spend in sorted(unseen.items(), key=lambda kv: (-kv[1], kv[0])):
        if total <= 0 or covered / total >= SHARPEN_COVERAGE:
            break
        keys.append(key)
        covered += spend
    return {
        "keys": keys,
        "unseen_spend": round(total, 2),
        "covers_pct": round(covered / total * 100, 1) if total > 0 else None,
    }


def analyze(data: dict, ads: list[dict]) -> dict[str, Any]:
    """Label-based measures. Labels arrive as opaque placeholder codes in the input."""
    total_spend = sum(ad_spend(a) for a in ads)
    kpi = kpi_action_type(data)
    m0_spend = 0.0
    # Per cell and per motivator layer: [spend, impressions, results].
    cells: dict[tuple[str, str], list[float]] = {}
    layers: dict[str, list[float]] = {}
    concepts: dict[tuple[str, str, str], float] = {}
    exec_spend: dict[str, float] = {}
    resolved, sources = resolve_labels(data, ads)
    for ad, labels in resolved:
        motivator = labels.get("motivator", "")
        angle = labels.get("angle", "")
        spend = ad_spend(ad)
        # Only a missing/empty motivator is "unlabeled"; the code itself is opaque.
        if not motivator:
            m0_spend += spend
            continue
        insights = ad.get("insights") if isinstance(ad.get("insights"), dict) else {}
        stats = (spend, as_float(insights.get("impressions")), _action_value(insights, kpi) or 0.0)
        for bucket in (cells.setdefault((motivator, angle), [0.0, 0.0, 0.0]),
                       layers.setdefault(motivator, [0.0, 0.0, 0.0])):
            for i, value in enumerate(stats):
                bucket[i] += value
        key = (motivator, angle, labels.get("execution", ""))
        concepts[key] = concepts.get(key, 0.0) + spend
        execution = labels.get("execution") or "NV"
        exec_spend[execution] = exec_spend.get(execution, 0.0) + spend

    labeled_spend = sum(c[0] for c in cells.values())
    seen_spend = sum(v for k, v in exec_spend.items() if k != "NV")
    motivator_spend = {m: layer[0] for m, layer in layers.items()}
    if m0_spend > 0:
        motivator_spend["M0"] = m0_spend
    msg_shares = sorted((c[0] / labeled_spend for c in cells.values()), reverse=True) if labeled_spend else []
    con_shares = sorted((v / labeled_spend for v in concepts.values()), reverse=True) if labeled_spend else []
    # What each cell would hold if the labelled spend were split evenly over the cells.
    even_spend = labeled_spend / len(cells) if cells else 0.0
    grid = []
    for (m, a), (spend, impressions, results) in sorted(cells.items()):
        rate = results / impressions * 1000 if impressions > 0 else None
        _layer_spend, layer_impr, layer_results = layers[m]
        layer_rate = layer_results / layer_impr * 1000 if layer_impr > 0 else None
        index = rate / layer_rate if rate is not None and layer_rate else None
        read = _read(index, impressions, results)
        grid.append({
            "motivator": m, "angle": a, "spend": round(spend, 2),
            "share_pct": round(spend / total_spend * 100, 1) if total_spend > 0 else 0.0,
            "impressions": int(impressions),
            "results": round(results, 2),
            "results_per_1000": round(rate, 2) if rate is not None else None,
            "cost_per_result": round(spend / results, 2) if results > 0 else None,
            "index_vs_layer": round(index, 2) if index is not None else None,
            # Classify on the exact ratio; only the displayed index is rounded.
            "read": read,
            "quadrant": _quadrant(read, spend, even_spend),
        })
    return {
        "distinct_messages": len(cells),
        "distinct_concepts": len(concepts),
        "effective_messages": round(effective_count(msg_shares), 1) if msg_shares else None,
        "effective_concepts": round(effective_count(con_shares), 1) if con_shares else None,
        "m0_share_pct": round(m0_spend / total_spend * 100, 1) if total_spend > 0 else 0.0,
        "label_sources": sources,
        # Motivators over all spend (M0 included); executions over labelled spend.
        "motivator_mix_pct": _mix_pct(motivator_spend, total_spend),
        "execution_mix_pct": _mix_pct(exec_spend, labeled_spend),
        # Below 60% the execution axis describes a minority: show formats instead.
        "execution_seen_pct": round(seen_spend / labeled_spend * 100, 1) if labeled_spend > 0 else None,
        "sharpen": sharpen_block(resolved),
        "angles_used": sorted({a for (_m, a) in cells if a}),
        # The quadrant's split line, on the same all-spend basis as grid[].share_pct.
        "even_cell_share_pct": round(even_spend / total_spend * 100, 1) if cells and total_spend > 0 else None,
        "grid": grid,
    }


def plan(data: dict, ads: list[dict], warnings: list[str]) -> dict[str, Any]:
    """Size the next batch from the test budget and list the empty taxonomy cells."""
    daily_budget = as_float(data.get("daily_budget"))
    target_cpa = as_float(data.get("target_cpa"))
    test_share = as_float(data.get("test_share"), 0.20)
    # Divide by 2*target_cpa: a cell needs roughly twice its target CPA in spend
    # before its result is readable, so capacity is test budget / that threshold.
    if target_cpa > 0:
        test_capacity = max(0, int(math.floor(daily_budget * 7 * test_share / (2 * target_cpa))))
    else:
        test_capacity = 0
        warnings.append("target_cpa missing or invalid; test capacity cannot be sized.")

    taxonomy = data.get("taxonomy") if isinstance(data.get("taxonomy"), dict) else {}
    for key in ("motivators", "angles", "cells"):
        if taxonomy.get(key) is not None and not isinstance(taxonomy[key], list):
            raise ToolInputError(f"'taxonomy.{key}' must be a list.")
    motivators = [m for m in (taxonomy.get("motivators") or []) if isinstance(m, str)]
    angles = [a for a in (taxonomy.get("angles") or []) if isinstance(a, str)]
    # An explicit, ranked cell list (the caller's gap ranking) replaces the grid order.
    ranked = [
        (c[0], c[1]) for c in (taxonomy.get("cells") or [])
        if isinstance(c, list) and len(c) == 2 and all(isinstance(x, str) for x in c)
    ]
    candidates = ranked or [(m, a) for m in motivators for a in angles]
    if not candidates:
        warnings.append("taxonomy.cells or taxonomy.motivators/angles missing; no empty cells to rank.")

    resolved, _sources = resolve_labels(data, ads)
    observed = {
        (labels["motivator"], labels.get("angle", ""))
        for _ad, labels in resolved
        if labels.get("motivator")
    }
    # Input order IS the priority order (not alphabetical); duplicates are dropped.
    empty: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for cell in candidates:
        if cell in observed or cell in seen:
            continue
        seen.add(cell)
        empty.append({"motivator": cell[0], "angle": cell[1]})
    return {
        "test_capacity": test_capacity,
        "test_share": test_share,
        "empty_cells": empty,
        "first_empty_cells": empty[:test_capacity],
    }


def _delta(before: Any, after: Any) -> dict[str, Any]:
    numbers = isinstance(after, (int, float)) and isinstance(before, (int, float))
    return {"before": before, "after": after, "delta": round(after - before, 2) if numbers else None}


def _positive_int(data: dict, key: str) -> int | None:
    value = data.get(key)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ToolInputError(f"'{key}' must be a whole number of 1 or more.")
    return value


def tag_wave(ad: dict) -> int | None:
    tag = parse_tag(ad_name(ad))
    return int(tag["wave"]) if tag else None


def wave_block(
    data: dict, label_data: dict, before_ads: list[dict], after_ads: list[dict], warnings: list[str]
) -> tuple[dict[str, Any], set[tuple[str, str]]]:
    """The wave being read back, and the cells its ads sit in after their labels resolve.

    The server's read_back (it found the launch) beats the caller's keys; without
    either, the wave is the highest tag in the after window. w0 is not a wave.
    """
    read_back = data.get("read_back") if isinstance(data.get("read_back"), dict) else {}
    n = _positive_int(read_back, "wave") or _positive_int(data, "wave")
    if n is None:
        waves = [w for w in (tag_wave(ad) for ad in after_ads) if w]
        n = max(waves) if waves else None
    days = _positive_int(read_back, "days") or _positive_int(data, "days")
    if days is not None and days <= READ_BACK_TOO_YOUNG_DAYS:
        warnings.append(f"The wave has {days} day(s) of data: too young to read; expect too_early cells.")
    tagged = [ad for ad in after_ads if n and tag_wave(ad) == n]
    # The feed only lists ads with delivery, so a wave ad in the before window ran before the launch.
    early = sum(1 for ad in before_ads if n and tag_wave(ad) == n)
    if early:
        warnings.append(
            f"before: {early} ad(s) of wave {n} already ran; the launch date may be later than the "
            "wave's first delivery."
        )
    resolved, _sources = resolve_labels(label_data, tagged)
    cells = {(lab["motivator"], lab.get("angle", "")) for _ad, lab in resolved if lab.get("motivator")}
    after_spend = sum(ad_spend(ad) for ad in after_ads)
    launch_date = read_back.get("launch_date") or data.get("launch_date")
    wave = {
        "n": n,
        "launch_date": launch_date,
        "source": read_back.get("launch_source") or ("user" if data.get("launch_date") else None),
        "days": days,
        "ads_tagged": len(tagged),
        "spend_share_after_pct": (
            round(sum(ad_spend(ad) for ad in tagged) / after_spend * 100, 1) if after_spend > 0 else None
        ),
    }
    return wave, cells


_CELL_FIELDS = ("spend", "share_pct", "impressions", "results", "index_vs_layer", "read")


def read_back_cells(
    before_grid: list[dict], after_grid: list[dict], wave_cells: set[tuple[str, str]]
) -> list[dict[str, Any]]:
    """Every cell of either window, side by side, with the change in its index against the layer.

    The change is the difference of the shown indexes, and only where both windows
    can be read: not too_early, and a layer of two or more cells (a cell alone in
    its layer indexes 1.0 against itself).
    """
    rows = [{(r["motivator"], r["angle"]): r for r in grid} for grid in (before_grid, after_grid)]
    layer_cells: list[dict[str, int]] = [{}, {}]
    for window, sizes in zip(rows, layer_cells, strict=True):
        for motivator, _angle in window:
            sizes[motivator] = sizes.get(motivator, 0) + 1
    out = []
    for key in sorted(rows[0].keys() | rows[1].keys()):
        before, after = rows[0].get(key), rows[1].get(key)
        readable = all(
            row is not None and row["read"] != "too_early" and sizes[key[0]] > 1
            for row, sizes in zip((before, after), layer_cells, strict=True)
        )
        out.append({
            "motivator": key[0],
            "angle": key[1],
            "wave_cell": key in wave_cells,
            "before": {f: before[f] for f in _CELL_FIELDS} if before else None,
            "after": {f: after[f] for f in _CELL_FIELDS} if after else None,
            "index_change": (
                round(after["index_vs_layer"] - before["index_vs_layer"], 2)
                if readable and before and after else None
            ),
        })
    return out


def compare(data: dict, warnings: list[str]) -> dict[str, Any]:
    """Read-back: the headline metrics and every (motivator, angle) cell before and since a wave."""
    before = data.get("before") if isinstance(data.get("before"), dict) else None
    after = data.get("after") if isinstance(data.get("after"), dict) else None
    if before is None or after is None:
        warnings.append("compare needs both 'before' and 'after' snapshots with an 'ads' list.")
    # Each window is labelled with the run's labels, model and KPI action.
    shared = {k: data[k] for k in ("model", "kpi_action", "labels_by_creative") if k in data}
    windows: dict[str, tuple[dict, dict, list[dict]]] = {}
    for key, snapshot in (("before", before or {}), ("after", after or {})):
        ads = read_ads(snapshot, warnings, f"{key}.ads")
        own: list[str] = []
        x = xray(snapshot, ads, own)
        a = analyze({**snapshot, **shared}, ads)
        if a["m0_share_pct"] > 0:
            own.append(f"{a['m0_share_pct']}% of spend has no label and sits in no cell.")
        warnings.extend(f"{key}: {w}" for w in own)
        windows[key] = (x, a, ads)
    (bx, ba, b_ads), (ax, aa, a_ads) = windows["before"], windows["after"]
    out: dict[str, Any] = {
        key: _delta(bx.get(key), ax.get(key))
        for key in ("effective_creatives", "top3_spend_share_pct", "distinct_creatives", "total_spend")
    }
    wave, wave_cells = wave_block(data, {**(after or {}), **shared}, b_ads, a_ads, warnings)
    out["wave"] = wave
    out["effective_messages"] = _delta(ba["effective_messages"], aa["effective_messages"])
    out["integrity"] = {"before": bx["integrity"], "after": ax["integrity"]}
    out["cells"] = read_back_cells(ba["grid"], aa["grid"], wave_cells)
    return out


def main(argv: list[str] | None = None) -> int:
    parser = _EnvelopeArgumentParser(description="Audit the creative mix of a Meta ad account")
    parser.add_argument("--input", "-i", required=True, help="Input JSON file")
    parser.add_argument("--mode", "-m", choices=MODES, help="Analysis mode (overrides input.mode)")
    parser.add_argument("--format", choices=["json"], default="json", help="Output format")
    args = parser.parse_args(argv)

    try:
        with open(args.input, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        fail([f"Could not read --input as JSON: {exc}"], {"mode": list(MODES)})

    if not isinstance(data, dict):
        fail(["Input must be a JSON object."], {"mode": list(MODES)})

    mode = args.mode or data.get("mode") or "xray"
    if mode not in MODES:
        fail([f"Unknown mode: {mode!r}"], {"mode": list(MODES)})

    warnings: list[str] = []
    try:
        result: dict[str, Any] = {"mode": mode, "run_id": compute_run_id(data)}
        if mode == "xray":
            result["xray"] = xray(data, read_ads(data, warnings), warnings)
        elif mode == "analyze":
            ads = read_ads(data, warnings)
            result["xray"] = xray(data, ads, warnings)
            result["analyze"] = analyze(data, ads)
        elif mode == "plan":
            result["plan"] = plan(data, read_ads(data, warnings), warnings)
        elif mode == "compare":
            result["compare"] = compare(data, warnings)
        result["warnings"] = warnings
    except ToolInputError as exc:
        fail([str(exc)], {"mode": list(MODES)})

    # allow_nan=False turns any residual non-finite value into a caught error
    # rather than emitting nonstandard JSON a strict client would reject.
    try:
        payload = json.dumps(result, ensure_ascii=False, allow_nan=False)
    except ValueError:
        fail(["Internal error: non-finite number in result."], {"mode": list(MODES)})
    print(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())

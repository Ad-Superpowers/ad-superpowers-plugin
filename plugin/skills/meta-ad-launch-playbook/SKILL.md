---
name: meta-ad-launch-playbook
description: "This skill should be used when the user wants to launch a Meta campaign end to end, create a batch of Meta ads, turn a folder of creatives into ads, go \"from creatives to live ads\", \"set up a campaign, ad set and ads\", or \"make ads with a different ratio per placement\". It is the single guided runbook from zero to live ads using the Ad Superpowers MCP write tools (meta_create, meta_create_ad), and it routes to the specialist skills for depth. Do NOT use for: getting a file into Meta / image_hash / hosting (use media-upload-guide), choosing a bid strategy in depth (use bid-strategy-selector), CBO vs ABO theory (use campaign-structure-advisor), writing the copy (use ad-copy-generator), creative testing matrices (use creative-diversification-generator), catalog / DPA strategy (use catalog-optimizer)."
---
# Meta Ad Launch Playbook

The end-to-end runbook for going from "I have some creatives" to live (paused) ads with the Ad Superpowers MCP tools. It owns the **orchestration** — the order of operations and the decisions that trip people up — and hands the deep mechanics to the specialist skills. Follow it top to bottom.

## The journey at a glance

```
[0] Page & Instagram        → confirm the client profile resolves a Page (+ IG)
        │
[1] Campaign                → meta_create(entity_type="campaign")     (budget: CBO or ABO)
        │
[2] Ad set                  → meta_create(entity_type="adset")        (+ creative-mode decision)
        │
[3] Creatives → ads         → meta_create_ad(...) per ad              (sequential batch)
        │
[4] Verify                  → meta_query / meta_get_creatives
```

Everything is created **PAUSED** by default. Nothing spends until you flip it to ACTIVE in review.

## §0 Before you start: Page & Instagram

Every ad needs a Facebook Page, and Instagram placements need an Instagram account. You usually do **not** pass these by hand — `meta_create_ad` resolves them from the client profile:

- **Auto-resolution.** If the client has a `facebook_page_id` (and optionally `instagram_user_id`) stored, `meta_create_ad` uses them, provided exactly one client profile links this ad account. Without such a profile it uses the account's only promotable Page, and asks for `page_id` when the account has several. You only pass `page_id` / `instagram_user_id` to override.
- **Set them once** with `clients_update` if they are missing, so every future ad just works.
- **Facebook-only ads.** `facebook_only=true` only means no Instagram identity is sent (page-only creative); it does not keep the ad off Instagram. Meta can attach the Page's linked Instagram account itself, asynchronously after the write; once the ad runs, it can then deliver on Instagram placements the ad set allows. To keep an ad off Instagram, set the ad set's placements: `targeting.publisher_platforms=["facebook"]`. Do not also pass an Instagram id: that conflicts. In the result, `instagram_identity.id=null` means "not sent", not "no Instagram".
- **Error `1815199`** ("ad account has no access to this Instagram account") means the stored IG account is not linked to this ad account. Fix the link in Business settings or correct `instagram_user_id`. For a stored or passed Instagram id this is surfaced as a real error rather than a silent page-only fallback; only an Instagram identity the tool resolved on its own still falls back to a page-only creative.

Discover what is available:

```python
meta_query(account_id="act_...", entity_type="promotepages")   # Pages this account can advertise
```

## §1 Create the campaign

```python
meta_create(
    account_id="act_...",
    entity_type="campaign",
    name="Spring Launch",
    objective="OUTCOME_TRAFFIC",      # or OUTCOME_SALES / _LEADS / _ENGAGEMENT / _AWARENESS / _APP_PROMOTION
    special_ad_categories=[],         # required by Meta; [] when no special ad category applies
    daily_budget=2000,                # cents (€20.00/day). CBO (the default) needs daily_budget OR lifetime_budget; for ABO see below.
    status="PAUSED",
)
```

Three things to internalize:

- **Always pass `special_ad_categories`.** Without it Meta rejects the campaign with "(#100) The parameter special_ad_categories is required". Pass `[]` when no special ad category applies; the tool accepts `CREDIT`, `EMPLOYMENT`, `HOUSING` and `SOCIAL_ISSUES_ELECTIONS_POLITICS`, not `"NONE"`.
- **Pick the budget mode: CBO (the default) or ABO.** A campaign budget (`daily_budget` or `lifetime_budget`, in cents) means CBO (Campaign Budget Optimization, which Meta now calls Advantage+ campaign budget): the budget lives on the campaign and the ad sets share it. For per-ad-set budgets (ABO), pass `budget_mode="ABO"` with no campaign budget and give each ad set its own budget in §2. Decide now: the tools set ABO only when the campaign is created (`meta_update` has no `budget_mode`), and Meta does not support turning ad set budget sharing on mid-flight (Marketing API, "Ad set budget sharing").
- **`bid_strategy` defaults to `LOWEST_COST_WITHOUT_CAP`.** You normally omit it. This is also why your ad sets do **not** need a `bid_amount` (see §2). Only set a different strategy if you have a real reason:
  - `LOWEST_COST_WITH_BID_CAP` or `COST_CAP` → require a `bid_amount` (set on the ad set).
  - `LOWEST_COST_WITH_MIN_ROAS` (ROAS goal in Ads Manager) → on the ad set pass `bid_strategy="LOWEST_COST_WITH_MIN_ROAS"`, a `roas_floor` (the target ROAS as a multiplier), `optimization_goal="VALUE"` and a `promoted_object` with the pixel and conversion event (for example `{"pixel_id": "<id>", "custom_event_type": "PURCHASE"}`); `bid_amount` is not used. Under CBO the ad sets inherit the campaign's bid strategy, so also create the campaign with `bid_strategy="LOWEST_COST_WITH_MIN_ROAS"` (or use `budget_mode="ABO"`). Sources: Meta Business Help Center, "About ROAS goal", and the Marketing API "Advantage campaign budget" guide.
  - MIN_ROAS is not open to every account. Meta refused it on a test account with: "Ad accounts owned by a new business can use minimum ROAS for ad delivery after several weeks of following our policies. If you don't want to wait, verify your business." For a new or unverified business, plan for that wait or for business verification.
  - For the "which strategy and what number" decision, `use bid-strategy-selector`. For CBO vs ABO and budget-split theory, `use campaign-structure-advisor`.

## §2 Create the ad set

```python
meta_create(
    account_id="act_...",
    entity_type="adset",
    campaign_id="<from step 1>",
    name="NL · 25-45 · interests",
    targeting={"geo_locations": {"countries": ["NL"]}, "age_min": 25, "age_max": 45},
    optimization_goal="LINK_CLICKS",   # must fit the campaign objective
    dsa_beneficiary="<who benefits>",  # EU targeting: Meta requires both DSA fields
    dsa_payor="<who pays>",
    status="PAUSED",
)
```

- **EU targeting needs the DSA fields.** Meta requires `dsa_payor` and `dsa_beneficiary` on ad sets that target the EU and associated territories (Marketing API, "Ad Set").
- **No budget here under CBO.** The ad set inherits the campaign budget; passing one is rejected. Under ABO it is the reverse: give each ad set its own `daily_budget` or `lifetime_budget` (cents).
- **No `bid_amount` needed** with the default `LOWEST_COST_WITHOUT_CAP`. Only supply `bid_amount` if you deliberately chose a cap strategy in §1.
- `advantage_audience` defaults to `0`: Meta delivers to your exact targeting, and the response notes that `advantage_audience=1` lets Meta broaden delivery. If Meta rejects the ad set because the objective requires Advantage+ audience (one of the causes the error hint lists), retry with `advantage_audience=1`.

### The creative-mode decision (do this before §3)

This is the choice that quietly breaks launches. Pick one:

| You want… | Ad set setup | How you build the ad in §3 |
|-----------|--------------|----------------------------|
| **One creative concept, the right ratio per placement** | **Standard ad set** (leave `is_dynamic_creative` off) | `placement_assets` on `meta_create_ad` |
| **Meta to auto-optimize across multiple text/creative variants** | **Dynamic Creative ad set**: `meta_create(entity_type="adset", ..., is_dynamic_creative=true)` | `body_variants` (and/or asset combos) on `meta_create_ad` |

Two things people get wrong:

- **`placement_assets` is NOT Dynamic Creative.** It builds an `asset_feed_spec` with placement `asset_customization_rules`, but that is just placement customization and runs on a **standard** ad set. Using `placement_assets` does not require — and should not be confused with — Dynamic Creative.
- **`body_variants` requires a Dynamic Creative ad set.** If you pass two or more `body_variants` to an ad on a standard ad set, `meta_create_ad` checks the ad set first and stops with an error ("body_variants needs a Dynamic Creative ad set") before it creates anything. So decide here: if you want multiple text variants, create the ad set with `is_dynamic_creative=true`; if you just want one message shown well across placements, stay standard and use `placement_assets`. Meta's Help Center says that since June 2024 dynamic creative may be unavailable for new sales or app promotion ad sets in Ads Manager ("About dynamic creative in Meta Ads Manager"); if Meta rejects `is_dynamic_creative=true`, create separate ads instead.

## §3 Creatives → ads

This is where the playbook earns its keep: **orchestration**. The file-handling mechanics (how to upload, URL vs hash, filename→ratio matching, the full placement list) live in `media-upload-guide` — `use media-upload-guide` for those and do not re-derive them here.

### Group, then build

```
1. Group your creatives by CONCEPT (a concept = one message/offer, in its various ratios).
2. One ad per concept.
3. Within a concept, bundle the aspect ratios via placement_assets (one ad serves the
   right ratio per placement, and keeps a single engagement post across placements).
4. Split into separate ads when:
     - the copy differs per ratio (placement_assets shares one body/headline), or
     - you are mixing image and video (meta_create_ad takes one media type per ad), or
     - it is a genuinely different creative concept (that is a new ad).
```

A single concept with multiple ratios → one ad:

```python
meta_create_ad(
    account_id="act_...",
    adset_id="<from step 2>",
    headline="Spring launch",
    body="One message, shown well everywhere.",
    link_url="https://example.com",
    image_hash="<1x1 hash>",          # primary / catch-all fallback (1:1 fits most placements)
    placement_assets=[
        {"image_hash": "<9x16 hash>",
         "placements": ["instagram_stories", "facebook_stories", "instagram_reels"]},
        {"image_hash": "<4x5 hash>",
         "placements": ["instagram_feed", "facebook_feed"]},
    ],
    status="PAUSED",
)
```

Other creative types, same `meta_create_ad` call:
- **Single image / single video** — pass one of `image_url` / `image_hash` / `video_url` / `video_id` (exactly one).
- **Carousel** — pass `slides=[{image_hash, name, link}, ...]` (2–10 cards).
- **Per-placement carousel variants** — `placement_assets` entries of the shape `{slides, placements}`.

For local Meta JPEG/PNG up to 20 MB (20,000,000 bytes), follow `media-upload-guide`:
`assets_stage` → client HTTP PUT → `meta_upload_image(stage_id=...)` →
`image_hash` → the existing `meta_create_ad(image_hash=...)`. The workspace must
have current upload access to that account and the client must have file/HTTP
access. Reuse an existing
account-library hash when possible. Do not add media arguments to campaigns.
A new staged image normally costs two successful calls; 50 cost 100 before
ad creation and checks. On unknown upload outcomes stop and inspect, not restage.

### Batch writes and pacing

There is **no bulk-create tool** — a batch is several `meta_create_ad` calls. You do not need to pace them yourself:

- The server mirrors Meta's documented rate model (a write scores 3 points against a read's 1, per "Marketing API Rate Limiting"; **uploads count as writes**) and has an error-613 circuit breaker plus backoff on Meta's own usage headers. Follow provider backoff, staging capacity hints and ordinary workspace plan limits. The removal of a historical hourly cap does not mean unlimited calls or uploads.
- Run the calls **sequentially** rather than as an unbounded parallel fan-out: sequential calls give clean per-ad results and let the server react to Meta's signals between calls.
- If a write is throttled, the error says so — back off, then resume where you left off; wait guidance is included where Meta provides it.
- If one ad in a batch hits a **Meta API** error, the others still succeed — that call returns a structured error result rather than aborting the run, so you can retry just the failures. Bad **inputs** are different: invalid media combinations, missing placements, a malformed carousel, or a `facebook_only` + Instagram conflict raise a validation error before the API call, so check each call's inputs before firing the batch.

## §4 Verify + honest limits

Read back what you created:

```python
meta_query(account_id="act_...", entity_type="ads", fields=["id","name","status","adset_id"])
# inspect the creative copy + placements (creative_id comes from the meta_create_ad response)
meta_get_creatives(account_id="act_...", scope="single", creative_id="<creative_id>")
```

Common stumbles and the fix:
- "Bid amount required" on the ad set → you (or an inherited strategy) chose a cap strategy without a `bid_amount`. With the default `LOWEST_COST_WITHOUT_CAP` this should not happen; if it does, omit the strategy or supply `bid_amount`.
- Instagram error `1815199` → see §0.
- "body_variants needs a Dynamic Creative ad set" → the ad set is standard. Put the ad in an ad set created with `is_dynamic_creative=true`, or drop `body_variants` and pass a single `body` (see §2).
- Mixed image + video rejected → split into separate ads.

**Honest limits (today):**
- **Catalog / Advantage+ catalog ads:** `meta_create_ad(product_set_id=...)` creates a media-less catalog ad, but only in an ad set that binds a product set in `promoted_object.product_set_id` (the tool checks this before it creates anything). This release ships no catalog tool, so catalog data itself is not reachable through MCP; `use catalog-optimizer` for the strategy.
- **No bulk-create tool** — batch = sequential `meta_create_ad` calls (see §3).

## Complementary skills

- `use media-upload-guide` — get files into Meta (URL vs hash, hosting, filename→ratio, the full placement list).
- `use bid-strategy-selector` — pick the bid strategy and the number when you override the default.
- `use campaign-structure-advisor` — CBO vs ABO, budget splits, account structure.
- `use ad-copy-generator` / `use video-script-writer` — produce the copy/script before you build.
- `use creative-diversification-generator` — plan the creative matrix (concepts × angles) feeding §3.
- `use catalog-optimizer` — catalog / DPA strategy.

## Account integrity reminder

Every `meta_create_ad` and every upload is a write. The server backs off on Meta's throttle signals. Follow explicit retry hints and the upload guide's bounded window; workspace quotas still apply. If a write is throttled, the error says so; back off and resume. Everything ships PAUSED so you can review before any spend.

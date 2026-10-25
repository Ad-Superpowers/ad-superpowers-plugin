---
name: meta-creative-diversification-generator
description: "Creative strategy for Meta ads: audit the creative mix of an ad account, map ads by motivator, angle and execution, rank the biggest gaps and plan the next batch with briefs. This skill should be used when the user asks for a \"creative audit\", \"creative strategy\", \"creative diversification\", \"what ads should we make next\", \"why does Meta spend everything on one ad\", a creative map or matrix, new creative briefs based on what is running, or to \"brainstorm ad concepts\". Do NOT use for: ad copy writing only (use ad-copy-generator), video scripts only (use video-script-writer), fatigue on one ad set (use creative-fatigue-analyzer), launching ads (use ad-launch-playbook)."
---
# Creative Strategy for Meta

Audit what an ad account really runs, see where the spend sits, find the messages it is missing, and
plan the next batch as briefs. Every number comes from the `creative_map.py` script; this skill reads,
labels and explains. It never writes to the ad account.

## Core principle

**Diversify concepts, not cosmetic variations.** Meta's guidance: "When multiple ads look or feel
alike, these are seen as variations of the same creative, meaning learnings and delivery optimizations
are shared at the creative level". It recommends ads that are "truly different in look, feel,
storyline, and message" and ads that "speak to different audience motivations or use cases" (Meta for
Business, "Demystifying Creative Diversification", 16 Dec 2025). It gives no number of creatives.

Andromeda is the retrieval stage of Meta's ads system: it narrows tens of millions of candidate ads to
a few thousand before the ranking stage (Engineering at Meta, "Meta Andromeda: Supercharging Advantage+
automation with the next-gen personalized ads retrieval engine", 2 Dec 2024).

## References

Load them with `skill(action="get", skill_id="meta-creative-diversification-generator",
include_references=True)` when you need the detail:

| File | What it holds |
|---|---|
| `creative-system.md` | The four axes, codes, starter sets, the distinction rule, evidence codes, tag grammar, rename sheet |
| `measurement.md` | Every formula the script uses, the X-ray picture, comparisons, gap ranking, test capacity, data rules |
| `evidence-and-compliance.md` | Evidence cards, the never-say list, the EU claims register |
| `demo-dataset.json` | A fictional account with precomputed results, for the demo |

## Modes

| Mode | When | Output |
|---|---|---|
| **Audit** | An account with spend in the window | The report below: X-ray, map, the three biggest opportunities; the next batch and briefs when asked |
| **Plan** | A client without history (new account, new product) | Motivators from customer evidence, a first wave sized by the test budget, briefs |
| **Next batch** | A map exists (snapshot, tags or an earlier run) | The next wave's cells and briefs |
| **Read-back** | A wave ran with tags in its ad names, or the user knows its launch date | Each cell before and since the launch, below |
| **Demo** | No `meta_*` tools are visible | The fictional demo account, clearly labelled, then how to connect Meta |

## Cost in tool calls

Say the cost before you start. A single-account audit goes ahead after you state it; ask first only for
branches above about 10 calls or across several accounts.

| Step | Calls |
|---|---|
| Load this skill | 1 |
| Client profile, if the organisation uses one (`clients`) | 0-1 |
| X-ray run (the server reads the ads and insights) | 1 |
| Analyze run with labels | 1 |
| Plan run, when the user wants the next batch | 0-1 |
| Full images for the sharpening set (image ads only), if needed | 0-2 |
| **Typical audit** | **3-7** |
| Read-back after a wave (the server reads both windows) | 1 |

The demo makes no Meta calls. For an image ad, `meta_get_creatives(account_id, scope="single",
creative_id=<creative_id>, include_images=True)` shows the full image (evidence I). For a video, a cover
image is not evidence: ask the user for frames or a description (evidence P or U, 0 calls).

## Running the x-ray

Let the server feed the script: it reads the account total for the window, then every ad that had
delivery in that window, whatever its status now, with its creative and its ad-level insights (spend,
impressions, actions, action values, Meta's relevance rankings and the incrementality attribution
setting), joins everything per ad and runs `creative_map.py`. You pass the account, the window and the
mode; you never copy ad data into the call. A run costs one tool call, and the result adds a `source`
block with the window, the number of ads read and `creatives_missing`. An account with more than 2,000
ads with delivery in the window, or a read Meta cuts short, is refused with an error instead of a partial
X-ray: use a shorter window. A refused or failed run returns no account data and is not counted.

```
skill(action="run",
      skill_id="meta-creative-diversification-generator",
      script_name="creative_map.py",
      input_source={"account_id": "act_<id>", "date_preset": "last_30d"},
      input_data={"mode": "xray", "model": "ecommerce"})
```

- `model` is `"ecommerce"` (KPI `purchase`) or `"leadgen"` (KPI `lead`); set `kpi_action` when the
  account optimises for another action.
- Leave `output_format` at its default: the script returns JSON only.
- `date_preset` is one of `last_7d`, `last_14d`, `last_28d`, `last_30d` or `last_90d`.
- Check `xray.integrity` first. `matches: false` means the ad-level read does not add up to the account
  total (`gap` is the account total minus the ads' spend; either sign means they do not reconcile); say
  so before any other number, because every ad-based measure then describes only part of the account (the
  KPI line still uses the account row when `incremental.basis` is `"account"`). Ads whose creative could not be read count as unresolved
  spend (`source.creatives_missing`).

**Small sets and the demo** may pass the ads directly instead of `input_source`, never both: with
`input_source` the server rejects `ads`, `account_totals` and `as_of` in `input_data`. Keep the input small:
copying ad data into a call is slow and error-prone above a couple of dozen ads. The shape, which is also
what the server builds:

```
{"mode": "xray", "model": "ecommerce", "as_of": "2026-10-09",
 "account_totals": {"spend": "7520.00"},
 "ads": [{"id": "...", "name": "... [cs:M2-PRB-DEM-w1]", "effective_status": "ACTIVE",
          "created_time": "2026-09-02T09:00:00+0000", "adset_id": "...",
          "creative": {"video_id": "...", "body": "...", "title": "..."},
          "insights": {"spend": "980.00", "impressions": "120000",
                       "actions": [{"action_type": "purchase", "value": "30", "incrementality": "13"},
                                   {"action_type": "video_view", "value": "21600"}],
                       "action_values": [{"action_type": "purchase", "value": "2700.00",
                                          "incrementality": "1170.00"}],
                       "engagement_rate_ranking": "AVERAGE"}}]}
```

`creative` and `insights` sit on the same ad object. `account_totals` may also carry the account row's
`actions` and `action_values` from the same request; the KPI line then uses Meta's account row and its
spend (`incremental.basis: "account"`, what the server supplies) instead of the ads' sum (`"ads"`). In
our measurements the summed per-ad incremental counts were below the account row. Without
`incrementality` keys the script reports
incremental figures as unavailable (null), never as 0; without `as_of` it skips freshness. Read the
`warnings` array and pass every warning on.

**Then label and map.** The X-ray result lists distinct creatives in `creatives`, each with a stable
`key`, its biggest `ad_ids`, its `creative_id` when known, and any launch `tag`. Label those rows (see
Audit, step 3) and run the same call with
`input_data={"mode": "analyze", "model": "ecommerce", "labels_by_creative": {"c48676e1": "M1-RES-PRD", ...}}`.
Labels apply in this order: labels on the ad itself, then `labels_by_creative` (what the user confirmed
in this audit), then a tag in the ad name. So a confirmed label corrects an old tag, and tagged rows need
no new label unless the user corrects them.
For the next batch, run `"mode": "plan"` with `labels_by_creative`, `daily_budget`, `target_cpa`, an
optional `test_share` (default 0.2) and `taxonomy.cells`: the candidate cells as
`[["M1", "PRB"], ["M3", "EMO"], ...]`, in your gap-ranking order.
Each fed run reads the account again, so run the X-ray, analyze and plan on the same day and name the
`run_id` each number comes from.

## Audit workflow

1. **Scope.** Confirm the account, the window (default last 30 days), the business model and the KPI.
   State the call cost. If the organisation uses client profiles, read the client's `## Creative`
   section: the goal, the last audits, the `LABELS` line and the `CODES` line.
2. **X-ray.** Run it and give the quick read:
   - one line: "Top 3 took {top3_spend_share_pct}%; an even split would give them
     {even_split_top3_pct}%", plus effective and distinct creatives and duplicate stacks;
   - freshness, hook rate, the media mix and the KPI line, with incremental figures named as Meta's
     model;
   - the ad sets with 10% or more of the spend that miss a format (`adsets`, `missing`);
   - the integrity result, unresolved spend and every warning.
   Describe or draw the picture in `measurement.md` when the host can render it.
3. **Label.** Work from the `creatives` rows, biggest spend first:
   - labels on the snapshot's `LABELS` line were confirmed in an earlier audit: pass them on in
     `labels_by_creative`, mark them as carried over with the snapshot date, and do not propose them
     again. Their motivators keep the names on the `CODES` line. A carried label beats a tag in the ad
     name, so ask where a row's `tag` now says otherwise;
   - motivators from customer evidence the user supplies; propose, then confirm (U);
   - angles from the copy (C);
   - executions only from seen visuals (P, I), a tag (N) or the user (U); otherwise `NV`.
   Show the proposed labels as a table with evidence codes and get the user's confirmation. The list
   stops at 95% of the resolved spend or 60 creatives (`creatives_omitted`, `omitted_spend`): that tail stays unlabelled unless
   tagged or carried on the `LABELS` line, and counts as M0. Say so.
4. **Map.** Run analyze. Show effective messages, the M0 share with its split (`m0_breakdown_pct`: on the
   list but unlabelled, below the list, creative not read), label sources, and the grid (motivators
   as rows, angles as columns; each filled cell with its share of spend, its `read` and its `quadrant`).
   - If `execution_seen_pct` is 60 or more, also show effective concepts and the execution mix.
   - If it is below 60, show the media mix instead of executions, and ask for visuals of the creatives in
     `sharpen.keys` (the fewest creatives that carry 80% of the unseen spend).
5. **Opportunities.** The three biggest, by the gap ranking in `measurement.md`, each phrased as
   "opportunity supported by <data>".
6. **Next batch**, when the user asks for it or accepts the offer in the report. Run plan with the
   ranked cells. `test_capacity` is a budget heuristic: how many new cells one week of test budget can
   fund at about twice the target CPA each. Whether a cell can be read is decided later, by the reading
   floors. Brief the cells in `first_empty_cells`.
7. **Briefs**, when a plan ran. One per chosen cell (format below). Copy goes to
   meta-ad-copy-generator, scripts to meta-video-script-writer; launching, with the tag in the ad name,
   goes through meta-ad-launch-playbook: paused, confirmed per batch.
8. **Remember.** Offer the snapshot, with its `LABELS` and `CODES` lines, and give the handoff block at
   decision points.

## The report

After the map run (Audit, step 4), give the audit as one report with these sections, in this order, on
every host. The names fix the meaning; write them in the user's language. Keep every section: when its
data is missing, say what is missing (for example the labels) instead of leaving it out.

1. **Header.** Account id, window (dates and `date_preset`), business model, KPI action, and the KPI line
   from `incremental`, with its `basis`.
2. **Integrity.** `matches`, `gap`, unresolved spend and `creatives_missing`. When `matches` is false, say
   here which of the numbers below describe only part of the account.
3. **X-ray.** The picture from `measurement.md` where the host can draw it, then these tiles: the top-3
   share against the even split, effective and distinct creatives, duplicate stacks, freshness, hook rate
   (video-only ads; say how many ads that mix images and video it leaves out,
   `mixed_media_ads_left_out`) and the media mix, then the ad sets that miss a format (`adsets`).
4. **Grid.** Motivators as rows, angles as columns; each filled cell with its share of spend, `read`,
   `quadrant`, results, cost per result and `index_vs_layer`. Under it: effective messages, the M0 share with
   its split (`m0_breakdown_pct`) and `label_sources`, plus effective concepts and the execution mix when
   `execution_seen_pct` is 60 or more.
5. **Per angle.** For each angle in use, its creatives biggest first: labels, share of spend and the first
   copy line (`copy`); then the unlabelled creatives, apart.
6. **Three opportunities.** In gap-ranking order, each as "opportunity supported by <data>".
7. **Next batch and briefs.** Only after a plan run the user asked for (the demo shows its stored plan).
   Otherwise one line that offers it and names its cost (1 call).
8. **Warnings.** The script's `warnings` as returned, then your own notes, kept apart.
9. **Sources.** The `run_id` of every run, the window, what was read (ads, creatives missing), the
   evidence codes behind the labels, and "Nothing was changed in the ad account."

**Codes with names.** Show a code with its plain name the first time it appears in a section: "M1 wants
weekends back from garden work", "PRB Problem and fix". A motivator's name is the customer wording the
user confirmed; a later audit takes it from the snapshot's `CODES` line. A motivator without a `CODES`
entry (an older snapshot, or a tag in an ad name) has no name on file: show the code alone, say that its
name is missing, and ask the user; never make one up. Angles and executions use the starter-set names unless the user renamed them:
- Angles: EMO Emotional appeal · FEA Product features · PRB Problem and fix · RES Result · PRF Proof ·
  CMP Comparison · DBT Doubt answered · HOW How it works · VAL Value and offer · STO Story.
- Executions: CRT Person to camera · DEM Hands-on demo · PRD Product shot · SCN Scene · TXT Text-led ·
  ANI Animation · NV Not verified.

**Where it renders.** Where the host renders HTML pages, the report is one page in this order. Elsewhere,
use the same order in markdown: tables for the grid and the lists, and the X-ray as the one line from
`measurement.md`.

## Read-back after a wave

Once a wave has run for a week or more, read it back in one call:

```
skill(action="run",
      skill_id="meta-creative-diversification-generator",
      script_name="creative_map.py",
      input_source={"account_id": "act_<id>", "date_preset": "last_90d"},
      input_data={"mode": "compare", "model": "ecommerce", "labels_by_creative": {"c48676e1": "M1-RES-PRD"}})
```

- The server finds the wave from the tags in the ad names (the highest wave, or `wave`), takes its first
  day with impressions as the launch, and reads as many days before the launch as since. `date_preset`
  is how far back it looks for that first day. Without tags, or to correct the launch, pass `launch_date`
  (`"YYYY-MM-DD"`); `days` shortens both windows. The formulas are in `measurement.md`.
- The windows read back are `source.before` and `source.after`. In this run `source.since` and
  `source.until` are where the launch was searched, not a window to report.
- Pass the labels of the last audit (the snapshot's `LABELS` line) as `labels_by_creative`, so both
  windows use the same labels.
- Show per cell the share of spend, results, `index_vs_layer` and `read` before and after, and
  `index_change` where it is not null, with the wave cells marked. Then the headline changes, the wave's
  share of the spend (`compare.wave`) and both integrity results, and every warning.
- Where a window reads `too_early`, say "too early to read"; never read a change from a null. A new cell
  moves the index of the other cells in its layer: say so before comparing them.
- A launched cell becomes judged only on an after window that can be read.

## Plan mode: a client without history

- Ask for customer evidence: reviews, sales-call notes, search terms, survey answers. Draft two to five
  motivators from it, in customer words, all marked proposed.
- Pick angles from the starter set in `creative-system.md` that the evidence supports.
- Size the first wave with a plan run without `input_source` (the server refuses an account without
  delivery): `input_data={"mode": "plan", "daily_budget": ..., "target_cpa": ..., "taxonomy": {"cells":
  [...]}}`. No ads are needed; `test_capacity` and `first_empty_cells` come back from the script.
- Write briefs. Costs 1-2 calls (the plan run, plus the client profile if you read it).

## Cell brief

```
CELL M2-PRB-DEM · wave 1 · status: proposed
Motivator (M2): <the reason, in customer words> [evidence: U]
Angle (PRB): <the argument, one line>
Execution (DEM): <what the viewer sees>
Format: V916, plus IMG for feeds
First line: <the opening line, no invented numbers or superlatives>
Visual: <one sentence>
Proof needed: <what must be true, or what the client must supply>
Claims check: <rows from the EU claims register, or "none">
Tag: [cs:M2-PRB-DEM-w1]
Supported by: <data, e.g. "M2-PRB reads ahead of its layer (index 1.20, 30 results)">
```

Length limits and placement details (Stories, Reels, Threads) are checked when the copy and scripts are
written: meta-ad-copy-generator and meta-video-script-writer carry them.

## Statuses

proposed → chosen → client (can / cannot / can differently) → planned → launched (tag found) → judged.
Never "approved".

## Memory: three anchors

The skill does not run on its own: each step is a run the user starts. What carries over:

1. **Tags in ad names.** They live in the account and survive every chat, host and colleague. The
   script reads them back.
2. **A snapshot in the client profile**: opt-in, in the client's `attention_points` field (10,000
   characters, shared with the onboarding digest and other skills), under its own `## Creative` heading,
   at most 2,500 characters: one goal line, one `LABELS` line, one `CODES` line and the last three
   audits. Write it only
   after an explicit yes. Read the field with `clients(action="get", client="<slug or id>")`, replace
   only the `## Creative` section, keep everything else as it was, and write the whole field back with
   `clients_update(action="update", client="<same slug or id>", attention_points=...)`. Keep the whole
   field at or under 6,000 characters: past that the write still succeeds, but the response carries a
   `warning`; tell the user and offer to summarize older sections. No per-ad or per-day data, no ad
   copy, no personal data: the one per-creative line is `LABELS`.

   ```
   ## Creative (asp-creative/1)
   GOAL 2026-10-09: eff >= 8 · vertical video in every ad set · open M3 row · iROAS >= 1.3
   LABELS c8a1b21f M1-RES-PRD · c34511bc M1-EMO-SCN · cea2ff93 M2-CMP-PRD · cd7abe90 M1-HOW-DEM · c218a6f6 M1-VAL-PRD · c445ac20 M1-PRF-TXT · cc4fab3b M1-STO-CRT · cf7a3983 M1-EMO-PRD
   CODES M1 wants weekends back from garden work · M2 tired of cords, hoses and petrol fumes · M3 buying a gift for a keen gardener
   @2026-10-09 30d ecom r-cf7ededa
   KPI spend 7520 · rev 22860 · ROAS 3.04 · iROAS 1.13 · purch 198 · CPA 37.98
   ADS 16 · distinct 14 · eff 5.9 · top3 63.8% · newest >=10% spend 37d
   MEDIA IMG 47.6 · VID 45.7 · CAR 5.7 · unresolved 0.9 (% spend) · vertical unknown
   EXEC PRD 48.7 · DEM 22.8 · SCN 20.7 · TXT 4.1 · CRT 3.6 (% labelled spend)
   MOTIV M1 72.6 · M2 23.5 · M3 0 · M0 3.9 · ANGLES 9/10
   AHEAD M1.RES 1.31x · M2.PRB 1.20x · GAP M3 no cell · NEXT wave 2, 5 cells
   ```

   The numbers are copied from the script's output, never recomputed: `incremental` (KPI spend is
   `incremental.spend`), the X-ray fields,
   `media_mix_pct`, `motivator_mix_pct`, `execution_mix_pct`, `grid[].index_vs_layer`. A motivator with
   no cell is written as 0. `ANGLES` is the number of codes in `angles_used` over the size of the angle
   set you used; `NEXT` is the number of cells in `first_empty_cells`. The goal line is the user's.

   Lead-gen KPI line: `KPI spend 4100 · leads 205 · CPL 20.0 · iLeads 131 · iCPL 31.3 · qualified 62
   (CRM, supplied 2026-11-05)`.

   `LABELS` holds the labels in force after the latest audit, carried and newly confirmed, biggest spend
   first, at most 30 creatives: the creative `key` from the X-ray (a short hash of the creative's media
   and copy, not a Meta id) and its code. Leave out M0 and anything still proposed, and write the line
   anew with each snapshot; if the section would pass 2,500 characters, drop entries from the smallest
   spend up. The next audit passes it on as `labels_by_creative`: a creative below the listed rows is
   still labelled, a key whose creative had no delivery in the window matches nothing, and a creative
   with new copy or media has a new key and is labelled again.

   `CODES` names every confirmed motivator the section mentions (on `LABELS`, in `MOTIV`, in the goal or
   as a gap) in the customer wording the user confirmed, at most 40 characters per name; angles and
   executions keep their starter-set names and are not listed. Without it a new chat knows M1 but not
   what M1 means. When `LABELS` loses entries to the size limit, a motivator the section no longer
   mentions also leaves `CODES`.
3. **The handoff block**, to continue in a new chat. Ids, codes and short labels only: no copy, no
   personal data, no demographic labels. Without a client profile, add the `LABELS` and `CODES` lines
   when the user wants the labels kept.

   ```
   asp_handoff · creative-strategy · run r-xxxxxxxx · act_<id> · 2026-09-10..2026-10-09
   cells: M1-PRB proposed · M3-EMO chosen · M2-RES client:can-differently
   open: previews for 3 NV creatives · confirm M3 wording
   ```

## Demo

When no `meta_*` tools are visible, show the demo instead of an empty audit:
- load the references and present `demo-dataset.json` as the report above: its `expected` block holds the
  X-ray, map and plan that `creative_map.py` computed for the fictional "Fernhill Garden Tools" account,
  so the stored plan fills the next-batch section;
- say in the first line that the account is fictional, and never present demo numbers as the user's;
- tell the story the numbers carry: the top 3 hold most of the spend, no creative launched in the last
  three weeks carries 10% of it, two cells read ahead of their layer, and one evidenced motivator has
  no ad yet;
- end with how to connect Meta in the Ad Superpowers dashboard, then run a real audit.

## Rules

- **No ad-account writes.** This skill never creates, edits or pauses anything in the ad account,
  whatever the write mode. Its only write is the opt-in snapshot in the client profile, after an explicit
  yes.
- **No invented numbers.** Every number comes from the script, Meta, or the user (with source and date).
  Do no arithmetic of your own on them: no sums, differences or new shares. Counting the entries of a
  list the output returns is fine (`ANGLES`, `NEXT`), and a chart may plot the rows' `share_pct` as a
  running total, labelled only with numbers from the output. When the report needs a number the output
  does not hold, say it is not available. To say what sits in M0 (catalogue ads, offers, traffic), name
  those creatives with their own `share_pct` from the X-ray (a share of resolved spend, while the M0
  share is of total spend), without a subtotal.
- **Wording.** "Opportunity supported by <data>". No promised results, no verdict words; see the
  never-say list in `evidence-and-compliance.md`.
- **Claims.** Run each brief past the EU claims register (not legal advice).
- **Special Ad Categories.** Casting: vary, do not steer. Never report delivery by demographic.
- **Scope.** Recruitment and political ads are out of scope.
- **Privacy.** Client-facing pages and files are private; never suggest share links.

Credit: the idea of a layered creative map was inspired by the Cascade approach of Peter Quadrel (Odylic
Media). The axes, codes, rules and wording here are our own, built on Meta's public guidance.

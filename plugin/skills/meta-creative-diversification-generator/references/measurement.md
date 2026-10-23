# Measurement

Every number in an audit comes from `creative_map.py`. The model reads, labels and explains; it does
not compute. Each result carries a `run_id` derived from the input, so the same data always gives the
same id. Quote the `warnings` array: the user can act on a warning, not on silence.

## X-ray: no labels needed

"Resolved spend" is the spend of ads with a fingerprint; "total spend" adds the unresolved rest.

| Measure | Rule | Output field |
|---|---|---|
| Integrity | When the input carries `account_totals.spend`: account total minus the ads' total spend (`gap`; either sign means they do not reconcile); `matches` within 0.5% of the account total | `integrity` |
| Distinct creatives | Ads grouped by fingerprint: media identities (image hashes and video ids, also inside carousels and asset feeds) plus the viewer-facing copy, lowercased and whitespace-collapsed, tagged by field so a body never matches a title | `distinct_creatives` |
| Duplicate stacks | Distinct creatives that run as more than one ad | `duplicate_stacks` |
| Unresolved spend | Spend of ads with neither media nor copy to fingerprint. Reported apart, never merged into a creative | `unresolved_spend` |
| Effective creatives | 1 / sum of (share squared), shares of resolved spend per distinct creative: "spend is spread as evenly as over N equally funded creatives" | `effective_creatives` |
| Top-3 share | Percentage of resolved spend held by the three biggest distinct creatives | `top3_spend_share_pct` |
| Even split for the top 3 | min(3, distinct) / distinct x 100: what the top 3 would hold if spend were even | `even_split_top3_pct` |
| Freshness | Age in days at `as_of` of the newest creative that still carries at least 10% of resolved spend. A creative is as old as its first launch. Needs `as_of`; the script never uses the clock | `freshness` |
| Hook rate | 3-second video plays (`actions[video_view]`) / impressions of all video ads; null when no video ad reports the action | `hook_rate` |
| KPI | Conversions, revenue, ROAS and cost per result (CPA or CPL) for the KPI action (`purchase` or `lead`): from the account row when `account_totals` carries `spend` plus an `actions` or `action_values` list (`basis: "account"`, divided by that spend), else summed over the ads (`basis: "ads"`). `spend` in the block is the spend it divides by. The grid's results stay ad-based and need not add up to an account-based KPI line | `incremental` |
| Incremental | Meta's incremental attribution: the `incrementality` value for the KPI action, on the same basis; iROAS = incremental revenue / spend. Each figure is null when its own key is absent (lead gen has no incremental revenue) | `incremental` |
| Media mix | Percentage of total spend per media kind (image, video, carousel, flexible, none), unresolved spend apart | `media_mix_pct` |
| Formats per ad set | Ads grouped by `adset_id` (the insights row's when the ad itself was not read; `unknown`, with a warning, when neither has one), biggest spend first, until 95% of total spend is covered, capped at 30 rows (`adsets_omitted`, `adsets_omitted_spend`). Per set: spend, share of total spend, the media kind mix, and `missing`: image or video when no ad in the set shows it. A video's thumbnail is not an image; a carousel counts by its cards, a flexible ad by its assets. `has_image`, `has_video` and `missing` are null when no ad in the set shows a media kind the script can read (an ad whose creative was not read, a post with copy only). This is the media kind, not the aspect ratio: vertical or square is not in the data | `adsets` |

**The inventory.** The X-ray also lists distinct creatives by spend in `creatives`, until 95% of the
resolved spend is covered, capped at 60 rows; `creatives_omitted` and `omitted_spend` give the rest.
Each row has a stable `key`, spend and share, ad count, media kind, first launch, impressions, hook rate,
Meta's relevance rankings of its biggest ad, up to three `ad_ids` (biggest first), the `creative_id`
when the read included it, any launch `tag`, and the first copy line. Label creatives from these rows,
then pass `labels_by_creative` (key to codes) to `analyze`.

**Hook band.** Among the listed video and flexible creatives with a hook rate and at least 2,000
impressions, and only when there are four or more, the script marks the lowest and the highest quarter
(`hook_band`: `bottom_quarter`, `top_quarter`, otherwise `middle`). A quarter is the count divided by
four, rounded down; ties break on the creative key. That is a comparison inside this account, not a
benchmark.

## The X-ray picture

- A cumulative curve over distinct creatives ranked by spend, a dotted line for an even spread, a marker
  at the effective-creatives value, and the top 3 annotated.
- Caption: "An even spread is a ruler, not a target."
- In plain markdown, one line: "Top 3 took {top3_spend_share_pct}%; an even split would give them
  {even_split_top3_pct}%."
- The test of a good picture: someone who is not an analyst reads it correctly in ten seconds.

## Map: labels needed

Labels apply in this order: labels on the ad itself, then `labels_by_creative`, then a `[cs:...]` tag in
the ad name (or, for an ad whose creative was not read, in the name on its insights row). `M0` and a
missing motivator both count as unlabelled.

| Measure | Rule | Output field |
|---|---|---|
| Effective messages | 1 / sum of (share squared) over (motivator, angle) cells of labelled spend | `effective_messages` |
| Effective concepts | The same over (motivator, angle, execution). Show it only when `execution_seen_pct` is 60 or more | `effective_concepts` |
| Seen executions | Percentage of labelled spend whose execution is set and not `NV` | `execution_seen_pct` |
| Sharpening set | The fewest creatives, biggest unseen spend first, that carry 80% of the spend without a seen execution | `sharpen` |
| M0 share | Percentage of spend with no motivator | `m0_share_pct` |
| Label sources | Ads labelled by their own labels, a creative label, a tag, or not at all | `label_sources` |
| Motivator and execution mix | Percentage per motivator over all spend (M0 included), and per execution over labelled spend (`NV` when no execution label) | `motivator_mix_pct`, `execution_mix_pct` |
| Angles in use | The angle codes that have at least one labelled cell | `angles_used` |
| Cell result rate | KPI results per 1,000 impressions, and cost per result | `grid[].results_per_1000`, `grid[].cost_per_result` |
| Index vs layer | The cell's result rate / the result rate of its motivator layer (all cells of that motivator), shown to two decimals | `grid[].index_vs_layer` |
| Read | On the exact ratio: `ahead` at 1.15 or more, `behind` at 0.85 or less, `level` between; `too_early` below 2,000 impressions or 5 results in the cell | `grid[].read` |
| Quadrant | The cell's read crossed with its spend against an even split of the labelled spend over the cells (`even_cell_share_pct`, on the same basis as `share_pct`): `ahead_small_share`, `ahead_large_share`, `behind_large_share`, `behind_small_share`. `level` and `too_early` pass the read through. Classified on exact spend; a cell at exactly the even split counts as large | `grid[].quadrant` |

Why effective creatives is usually higher than effective concepts: a headline swap on the same image is a
new fingerprint, not a new idea (`creative-system.md`, the distinction rule).

Why the reading floors: with fewer than 5 results, one result more or less changes the cell's rate by
20% or more. Always show the result count next to an index, and say "too early to read" rather than
guessing.

## KPIs per business model

| Model | KPIs |
|---|---|
| E-commerce (`model: "ecommerce"`, KPI `purchase`) | spend, revenue, ROAS, iROAS, purchases, CPA |
| Lead gen (`model: "leadgen"`, KPI `lead`) | spend, leads, CPL, incremental leads, incremental CPL; qualified leads only when the user pastes CRM counts, with source and date |

Set `kpi_action` in the input when the account optimises for a different action.

## Comparisons, from strongest to weakest

1. **Inside the account.** A creative against this account's own distribution: "hook rate in the bottom
   quarter of this account's videos", "a cell at 0.7x its layer".
2. **Meta's own comparison per ad.** Ad relevance diagnostics: quality, engagement rate and conversion
   rate ranking, each "compared to ads competing for the same audience" (Meta Business Help Center,
   "About ad relevance diagnostics"). Shown as returned.
3. **Practice benchmarks.** Only as context on a source card, never as a target or a pass mark.
4. **Bands across accounts.** Not in this version.

## Creative advice where the data carries it

Phrase each item as "opportunity supported by <data>", never as a promised result.

| The data shows | The opportunity |
|---|---|
| Hook band `bottom_quarter`, and an engagement ranking below average | Rework the opening |
| A cell that reads `ahead` of its layer | Extend the row: same message, a new execution, or a new angle for that motivator |
| A static with an engagement ranking below average | Check it against the billboard test: one idea, product visible, few words, readable on a phone at arm's length |
| High M0 share | Label or sharpen before planning: the map is blind there |
| `has_fresh_high_spend_21d` is false | Plan the next wave: no creative launched in the last three weeks carries 10% of spend |
| A cell with `quadrant` `ahead_small_share` | Give that message room: it reads ahead of its layer on less than an even share of the spend |
| A cell with `quadrant` `behind_large_share` | Check the spend split: more than an even share sits on a message that reads behind its layer |

Hold (how long people keep watching) is not in this version. Meta returns ThruPlays and plays to 25%
up to 100% on the same read, but not the video's length, which takes another read per video. A ThruPlay
is a play to the end or to 15 seconds, so without the length a hold share mostly compares video lengths.
Never report a metric under one second.

## Gap ranking for the next batch

Rank open opportunities in this order, and give the reason with each:

1. **Extend a row that reads ahead**: a motivator layer with a cell that reads `ahead`; state its result count.
   A cell with `quadrant` `ahead_small_share` comes first: it reads ahead on less than an even share.
2. **A confirmed motivator without any cell.**
3. **A missing media format in a high-spend ad set**: an `adsets` row with 10% or more of the spend
   whose `missing` lists a format (for example a set without video). The script sees the media kind, not
   the aspect ratio: name a missing vertical format only when the user knows the ad sets' formats.
4. **An empty angle that customer words support.**
5. **Maintenance**: iterations of running concepts, listed apart from new concepts.

Inside one rank, the spend at stake decides first, then the effort to produce. Pass the candidate cells
to `plan` as `taxonomy.cells` in this order; the script drops the cells that already exist and keeps
yours in order.

## Test capacity

`floor(daily budget x 7 x test share / (2 x target CPA))`, with a test share of 20% unless the user sets
another. A budget heuristic: how many new cells one week of test budget can fund at about twice the
target CPA (or CPL) each. Whether a cell is readable is decided later by the reading floors, not by this
number. The script returns it as `test_capacity` and the cells to brief as `first_empty_cells`.

## Read-back after a wave

`"mode": "compare"` reads a wave back: every (motivator, angle) cell before and since its launch, over
two windows of the same length. With `input_source` the server reads both windows. Without it, pass
`before` and `after`, each an object with `ads` and optionally `account_totals` and `as_of`.

| Measure | Rule | Output field |
|---|---|---|
| Wave | The highest wave in a `[cs:...-w<n>]` tag (w0 is not a wave), or `wave` when set | `compare.wave.n` |
| Launch | The first day with impressions of the wave's ads (`source: "delivery"`), or the user's `launch_date` (`"user"`). Never the creation date: ads are launched paused | `compare.wave.launch_date`, `compare.wave.source` |
| Windows | N = the smallest of `days` (default: the days since the launch), the days since the launch, and 90. Before is the N days up to the launch; after is the launch day and the N - 1 days after it | `compare.wave.days`, `source.before`, `source.after` |
| Cells | Each cell of either window with its spend, share of spend, impressions, results, `index_vs_layer` and `read` in that window; null where no labelled ad of that window sits in the cell | `cells[].before`, `cells[].after` |
| Index change | After minus before of the shown `index_vs_layer`. Null when a window reads `too_early`, the cell is missing from a window, or its motivator layer has one cell in a window (a cell alone indexes 1.0 against itself) | `cells[].index_change` |
| Wave cell | The cells the wave's ads sit in once their labels resolve, so a confirmed label beats the tag | `cells[].wave_cell` |
| Wave share | The wave's ads in the after window and their share of its spend | `compare.wave.ads_tagged`, `compare.wave.spend_share_after_pct` |
| Headline | Effective creatives, top-3 share, distinct creatives, total spend and effective messages: before, after and the change | `compare.effective_creatives` ... `compare.effective_messages` |
| Integrity | The X-ray's integrity check, per window | `compare.integrity.before`, `compare.integrity.after` |

How to read it:

- A new cell changes its motivator layer's result rate, so the other cells of that layer move in index
  even when nothing about them changed. Read a sibling's `index_change` next to the wave cell, never alone.
- The wave cell usually has no `before`: it was empty. Its read is the after window against its layer.
- The reading floors apply per window. A wave with one or two days of data is too young to read, and the
  script says so.
- A warning about one window starts with its name (`before:`, `after:`), including the share of spend
  without a label. An ad the creative read missed keeps its tag through the name on its insights row.
- Wave ads in the before window mean the launch date is later than their first delivery (a
  `launch_date` set too late); the script warns.

The server refuses, with a hint, when no tagged ad had delivery in the `date_preset` window (pass
`launch_date`), when the wave already delivered on that window's first day (a longer `date_preset` or
`launch_date`), or when the launch date is after the last day with data.

## Data rules

- Read ads in every delivery status: `ACTIVE`, `PAUSED`, `ADSET_PAUSED`, `CAMPAIGN_PAUSED`, `ARCHIVED`,
  `WITH_ISSUES`, `DISAPPROVED`, `PENDING_REVIEW`, `IN_PROCESS`, and deleted ads where Meta still returns
  them. An ACTIVE-only read misses the spend of every ad paused during the window; a deleted ad that
  spent but is not returned shows up as an integrity gap.
- Hook rate uses `actions[video_view]`. `video_play_actions` counts many more plays than 3-second views
  and is not a hook rate. `video_continuous_2_sec_watched_actions` came back empty in our tests; do not
  promise it.
- Meta leaves a metric out instead of returning 0. A missing action means 0 for that ad. A missing
  `incrementality` key means "not available", and the script reports null, never 0.
- In our tests `incrementality` on `actions` was a rounded whole number per ad, while on `action_values`
  it kept decimals. Never count "ads with an incremental effect" from non-zero counts. Summed over the
  ads, the rounded counts fell short of the account row (90 against 92 on one account, 35 against 38 on
  another), so the server-fed run takes the KPI line from the account row.
- With `input_source` the server supplies `ads`, `account_totals` and `as_of` (for `compare`: `before`,
  `after` and `read_back`). When you pass ads directly,
  include `account_totals.spend` for the same window so the integrity check can run, and the account row's
  `actions` and `action_values` from that request for the KPI line. A gap means the read
  does not reconcile with the account; it is not unresolved spend. Report it before any comparison.

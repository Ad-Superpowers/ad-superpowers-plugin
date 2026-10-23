# Creative system

The creative map has four axes. Meta's public guidance names the raw material: ads that "speak to
different audience motivations or use cases", ads that are "truly different in look, feel, storyline,
and message", and ads that are "truly distinct in their visuals, messaging, and formats" (Meta for
Business, "Demystifying Creative Diversification", 16 Dec 2025). Meta publishes no taxonomy. The four
axes, the codes and the starter sets below are this skill's own working system, built on that guidance.
Rename or extend them per client; keep the code shapes so tags and the script still read them.

## The four axes

| Axis | The question it answers | Codes | Evidence that may set it |
|---|---|---|---|
| Motivator | Why does this buyer act? A reason or use case, in the buyer's words | `M1`-`M9` per account; `M0` = cannot tell | C, U, N |
| Angle | How does the ad make its case? (the message) | three capital letters, starter set below | C, U, N |
| Execution | How does it look, feel and unfold? | starter set below; `NV` = not verified | P, I, N, U (never C alone) |
| Format | Which media and shape? | `IMG`, `VID`, `V916`, `CAR`, `FLX`, `CAT` | A |

A **message** is a (motivator, angle) pair. A **concept** is a (motivator, angle, execution) triple.
The script measures both (see `measurement.md`).

## Motivators

- Write a motivator as a reason in customer words: "wants weekends back from garden work", not an age
  or gender band. Never encode a demographic or a protected trait in a motivator.
- Draw them from evidence the user supplies: reviews, sales-call notes, search terms, survey answers,
  CRM notes. Mark each as proposed until the user confirms it (evidence U).
- Start with the reasons you can evidence; add one only when new evidence arrives.
- `M0` marks spend whose motivator cannot be told from copy and visuals. The M0 share is a finding, not
  a failure: it shows where the map is blind.
- Plan mode (a client without history): draft motivators from the offer and the customer evidence the
  user pastes; all of them start as proposed.

## Angles: starter set

Meta's own two examples of different messages are "emotional appeal" and "product features" (same Meta
for Business post). The other eight are this skill's working set of common advertising arguments.

| Code | Angle | The ad's argument | Example first line (fictional) |
|---|---|---|---|
| `EMO` | Emotional appeal | How it feels to have or use it: relief, pride, belonging | "Sunday mornings, finally yours." |
| `FEA` | Product features | What it has or does, concretely | "Two batteries, swap in a second." |
| `PRB` | Problem and fix | Names one pain, shows the way out | "Tangled hose again? Not with this reel." |
| `RES` | Result | The after-state the buyer ends up in | "A lawn you do not have to think about." |
| `PRF` | Proof | Real reviews, ratings, certification, press | "Rated by real buyers: read the reviews." |
| `CMP` | Comparison | Against the old way or a category alternative, fair and verifiable | "Same cut as petrol, without the fumes." |
| `DBT` | Doubt answered | Removes one hesitation: price, effort, risk, fit | "Not sure it fits? Free returns for 30 days." |
| `HOW` | How it works | The mechanism or the steps | "Clip, twist, mow: here is the whole setup." |
| `VAL` | Value and offer | Price, bundle, guarantee, trial | "Starter kit with spare blades included." |
| `STO` | Story | Who makes it and why: origin, craft | "Built in a two-person workshop since 2011." |

Check every `PRF`, `CMP` and `VAL` cell against `evidence-and-compliance.md` before it becomes a brief.

## Executions: starter set

Meta's guidance asks for ads that differ in "look, feel, storyline". The execution axis records that.

| Code | Execution | What you see |
|---|---|---|
| `CRT` | Person to camera | Someone talks to the viewer: creator, staff, founder or a real customer |
| `DEM` | Hands-on demo | The product being used on screen |
| `PRD` | Product shot | Packshot, still life or 3D, no person |
| `SCN` | Scene | People in a situation, no direct address |
| `TXT` | Text-led | Typographic card, review card, screenshot, meme format |
| `ANI` | Animation | Motion graphics, illustration, explainer |
| `NV` | Not verified | The visual was not seen: never guess an execution from copy |

An actor or an AI-generated person is never presented as a customer (`evidence-and-compliance.md`).

## Formats

Formats come from the API; no judgment is needed.

| Code | Format | Script `media` value |
|---|---|---|
| `IMG` | Single image | `image` |
| `VID` | Video, ratio unknown or not vertical | `video` |
| `V916` | Vertical video, 9:16 (only when the video's dimensions are known) | `video` |
| `CAR` | Carousel | `carousel` |
| `FLX` | Flexible asset feed with several media | `flexible` |
| `CAT` | Catalog or dynamic ad: not comparable with the other cells | `none` (no media found; confirm from the ad set's product set) |

Meta recommends 9:16 vertical video for Reels and Stories placements (Meta Business Help Center, "Best
practices for aspect ratios"; Meta for Business, "Reels ads"). The script cannot see a video's ratio from
the creative fields alone; until the dimensions are supplied, report vertical video as unknown.

## The distinction rule

Meta separates creative iteration from creative diversification: "Creative iteration might produce two
ads with identical visuals, but different text CTAs", and "When multiple ads look or feel alike, these
are seen as variations of the same creative" (Meta for Business, "Demystifying Creative
Diversification", 16 Dec 2025). This skill's rule on top of that:

| Two ads differ only in | They are | X-ray | Map |
|---|---|---|---|
| Nothing (same media, same copy) | A duplicate | one distinct creative, a duplicate stack | same concept |
| Crop, colour, headline wording, or a new hook line over the same footage | Variations of one concept | usually separate distinct creatives (a new image file or new copy gives a new fingerprint; a call-to-action button change alone does not) | same concept |
| Execution (look, feel, storyline); same motivator and angle | A new execution of the same message | separate | +1 concept, same message |
| Angle or motivator | A new message | separate | +1 message |

So the X-ray counts distinct assets and the map counts distinct ideas. A headline swap raises the first,
never the second. Iterations still have a place: they test elements inside a concept. List them as
maintenance, apart from new concepts.

## Evidence codes and confidence

Every label carries one evidence code per axis and a confidence (high, medium, low):

| Code | Meaning |
|---|---|
| A | Read from the API (formats, dates, spend) |
| C | Inferred from the ad's copy |
| N | Read from a `[cs:...]` tag in the ad name |
| U | Confirmed by the user |
| P | A preview, frames or the playing video was seen |
| I | The full image was viewed |

Rules:
- Never set an execution from copy alone: without P, I, N or U the execution is `NV`.
- A video's cover image or thumbnail is not evidence of its execution, and neither is a table thumbnail.
  For an image ad, viewing the full image counts as I.
- **Media fallback.** When `execution_seen_pct` (the share of labelled spend with a seen execution) is
  below 60, show formats (`media_mix_pct`) instead of executions and concepts, and say so. A map built on
  a minority of the spend describes the minority.
- **Sharpening.** `sharpen.keys` lists the fewest creatives that carry 80% of the unseen spend. Ask for
  visuals of just those: the full image for an image ad, frames or a description from the user for a
  video.

## Tag grammar

A tag at the end of the ad name records the cell an ad was made for:

```
<ad name> [cs:M2-PRB-DEM-w1]
           |   |   |   |  wave number
           |   |   |   execution code (2-3 capitals)
           |   |   angle code (3 capitals)
           |   motivator code (M + 1-2 digits)
           namespace
```

- The script reads exactly this pattern: `\[cs:(M\d{1,2})-([A-Z]{3})-([A-Z]{2,3})-w(\d{1,3})\]`.
  A tagged ad gets its labels from the tag (evidence N) unless the ad carries its own labels or the user
  confirmed a different label for its creative in this audit (`labels_by_creative`). A tag with `M0`
  counts as unlabelled. The X-ray shows each creative's tag in `creatives[].tag`.
- Tags are written when the ad is created, through `meta_create_ad` (one call per ad), using the
  meta-ad-launch-playbook: paused, confirmed per batch. This skill does not write.
- Wave `w0` marks ads that existed before the first planned wave.
- Never put a name, a customer detail or a demographic word in a tag.

## Rename sheet

For ads that already run, offer a rename sheet after the user has chosen the map. The user applies it
in Ads Manager (bulk edit), so it costs 0 tool calls:

| ad id | current name | new name |
|---|---|---|
| demo-1042 | Spring promo v3 | Spring promo v3 [cs:M1-EMO-CRT-w0] |
| demo-1057 | Reel hose fix | Reel hose fix [cs:M2-PRB-DEM-w0] |

Only rename ads whose labels have evidence beyond C; leave `NV` executions untagged until seen.

---
name: meta-attribution-window-advisor
description: "This skill should be used when the user asks to \"choose an attribution window\", \"compare click vs view-through attribution\", \"set up incremental attribution\", or mentions \"Meta attribution settings\", \"iOS 14 attribution\", or \"attribution window configuration\". Do NOT use for: cross-platform attribution reconciliation (use cross-platform-attribution-reconciler), CAPI setup (use capi-implementation-guide), EMQ optimization (use emq-optimizer)."
---
# Attribution Window Advisor

Advisor for choosing the optimal Meta Ads attribution configuration based on product, buying cycle, and goals.

> **2026 attribution changes (checked 2026-10-10):**
> - Since 12 January 2026 the Ads Insights API no longer returns the 7-day view (`7d_view`) and 28-day view (`28d_view`) windows. 1-day click, 7-day click, 28-day click, 1-day engaged view and 1-day view stay. Breakdowns of unique-count fields (such as `unique_actions`) and hourly breakdowns now reach back 13 months, frequency breakdowns 6 months; totals stay available for 37 months. Source: Meta for Developers blog, "Ads Insights API Metric Availability Updates", 16 Oct 2025
> - From March 2026 Meta is rolling out a narrower click-through for website and in-store conversions: it counts only link clicks. Shares, saves and other non-link clicks move to engage-through, the new name for engaged-view, and an engaged view of a video ad now needs 5 seconds of play instead of 10. Billing does not change. Source: Meta for Business, "Simplifying Ad Measurement for a Social-First World", 3 Mar 2026, https://www.facebook.com/business/news/click-attribution
> - Results from before and after these changes are not like for like: say so when you compare periods.

## Attribution Basics

### What Is Attribution?

Attribution determines which ads receive credit for conversions and how long after interaction a conversion is still attributed.

```
Attribution Types:
├── Click-Through: Conversion after a link click on the ad
├── View-Through: Conversion after seeing an ad (no click)
└── Engage-Through: Conversion after a non-link click or a 5+ sec video play
```

### Available Windows (Current)

| Window Type | Options | Counts conversions after |
|-------------|---------|---------|
| **Click-Through** | 1-day, 7-day | A link click on the ad |
| **View-Through** | 1-day, None | An impression of the ad |
| **Engage-Through** (formerly engaged-view) | 1-day | A non-link click (like, share, save), or a video play of 5 seconds (97% of a video shorter than 5 seconds) |

You choose these per ad set, under the standard attribution model. Meta's setup steps pair engage-through with view-through "None" or "1-day". The Meta help pages below state no default for new ad sets, so read the setting from the ad set itself. Some accounts may still use the earlier click-through and engage-through definitions while Meta rolls out the new ones, and engage-through is not available for Facebook in-stream video ads that cannot be skipped.
Sources (checked 2026-10-10): Meta Business Help Center, "About attribution models and attribution settings"; "Set up engage-through in Meta Ads Manager"

**Not available as an ad set setting:**
- 28-day click (the Ads Insights API still reports it)
- 28-day view (the API stopped returning it on 12 January 2026)
- 7-day view (the API stopped returning it on 12 January 2026)

## Attribution Window Selection

Rules of thumb, not Meta figures: check them against the account's own history. This covers the price bands in
the decision tree and the recommendation matrix.

### Decision Tree

```
WHAT IS YOUR PRODUCT/SERVICE?
│
├─► Impulse Purchases (<€50, quick decision)
│   └─► 1-day click, 1-day view
│   └─► Examples: Fast fashion, accessories, digital products
│
├─► Standard E-commerce (€50-200)
│   └─► 7-day click, 1-day view (our default)
│   └─► Examples: Clothing, electronics, home goods
│
├─► Considered Purchases (€200+, research phase)
│   └─► 7-day click, 1-day view
│   └─► Examples: Furniture, luxury items, tech
│
├─► Lead Generation (B2B/Services)
│   └─► 7-day click, 1-day view
│   └─► Long sales cycle: 7-day click (the longest click window)
│
└─► High-Ticket / Long Sales Cycle
    └─► 7-day click, 1-day view
    └─► Supplement with external attribution tools
```

### Recommendation Matrix

| Scenario | Click Window | View Window | Rationale |
|----------|--------------|-------------|-----------|
| **Default (most cases)** | 7-day | 1-day | Balanced data collection |
| **Impulse/Flash sales** | 1-day | 1-day | Short decision cycle |
| **Brand awareness** | 7-day | 1-day | Capture delayed action |
| **Retargeting** | 7-day | 1-day | Users already familiar |
| **Strict ROAS targets** | 7-day | None | Minimize inflated metrics |
| **High-consideration B2B** | 7-day | 1-day | Research-heavy buying |

## Click-Through vs View-Through

### Understanding the Difference

```
CLICK-THROUGH ATTRIBUTION:
├── User clicks a link in the ad
├── User converts within window
├── Conversion credited to ad
└── Stronger causation signal

VIEW-THROUGH ATTRIBUTION:
├── User sees ad (no click)
├── User converts within window (different path)
├── Conversion credited to ad
└── Measures awareness/influence

ENGAGE-THROUGH (formerly engaged-view):
├── User clicks the ad but not a link (like, share, save),
│   or plays a video ad for 5+ seconds (97% if it is shorter)
├── User converts within 1 day
├── Works with view-through set to None or 1-day; with view-through on,
│   the Results column adds click and view conversions only
└── Middle ground between click and view
```

Source (checked 2026-10-10): Meta Business Help Center, "Set up engage-through in Meta Ads Manager" (Meta's example: 5 click-through, 15 view-through and
3 engage-through conversions show as 20 results).

### When to Use View-Through

```
ENABLE VIEW-THROUGH (1-day) WHEN:
├── Brand awareness is important
├── Want to measure full ad impact
├── Video ads prominent in mix
├── Upper-funnel campaigns
└── Budget for incremental reach

DISABLE VIEW-THROUGH (None) WHEN:
├── Strict ROAS accountability
├── Comparison with other channels
├── Minimizing attribution overlap
├── Focus on direct response only
└── Incremental measurement priority
```

### View-Through Impact

```
View-Through Effect on Metrics:
├── ROAS: the same or higher with VT enabled (measure the difference in the account)
├── Conversions: the same or more reported
└── CPA: Appears lower (more conversions attributed)

Note:
- VT conversions are NOT fake
- They measure brand influence
- But they are less "incremental"
- Always compare apples-to-apples
```

## ATT Attribution Constraints

### Current State (Since iOS 14.5)

```
App Tracking Transparency (ATT) — standard since 2021:
├── Apps must ask permission before tracking people across
│   other companies' apps and websites (iOS 14.5, April 2021)
├── Limited conversion visibility for opted-out users
├── SKAdNetwork app results arrive with delays of at least 24 hours
├── Aggregated Event Measurement (AEM) for web and app events
│   from iOS 14 and later devices
└── Meta uses statistical modeling where conversion data is
    missing or partial

Practical Impact:
├── Reported conversions differ from your own orders:
│   measure the gap in the account, do not assume a size
├── Website and app activity custom audiences may shrink
└── Compare trends over time rather than absolute counts
```

Sources (checked 2026-10-10): Apple Newsroom, "iOS 14.5 delivers Unlock iPhone with Apple Watch, more diverse Siri
voice options, and new privacy controls", 26 Apr 2021,
https://www.apple.com/newsroom/2021/04/ios-14-5-offers-unlock-iphone-with-apple-watch-diverse-siri-voices-and-more/;
Meta Business Help Center, "About Meta Ads Manager reporting for Apple's SKAdNetwork"; "Understand how results are sometimes calculated
differently"; "Reach people using iOS 14.5 or later with
Meta ads"

### Aggregated Event Measurement (AEM)

```
What AEM Does (Meta's description):
├── Measures web and app events from people on iOS 14 and later
├── Removes identifiers
├── Adds differential privacy (noise)
└── Aggregates the data across users

Current setup for web events:
├── No 8-event priority list per domain any more
├── No value sets needed for value optimization
├── No AEM steps: events are processed automatically
└── Domain verification no longer needed for event configuration
```

Source (checked 2026-10-10, the page carries no date for this change): Meta Business Help Center, "About Meta's
Aggregated Event Measurement"

### iOS Attribution Strategy

```
RECOMMENDED SETUP:

1. Event Configuration:
   ├── Focus on high-value events (Purchase)
   ├── CAPI implementation essential
   ├── AEM needs no setup for web events
   └── No manual event ranking needed

2. Attribution Expectations:
   ├── Expect a gap with your own orders: measure it, do not assume a size
   ├── Use modeled conversions
   ├── Supplement with post-purchase surveys
   └── Cross-reference with platform data

3. Optimization Approach:
   ├── Trust Meta's modeled data
   ├── Focus on trends, not absolute numbers
   ├── Compare period-over-period
   └── Use multiple measurement sources
```

## Incremental Attribution

### What Is Incremental Attribution?

```
Traditional Attribution:
├── Counts all conversions after ad exposure
├── Including conversions that would have happened anyway
└── Can cause overclaiming

Incremental Attribution:
├── Counts only conversions Meta's model judges CAUSED BY the ad
├── Leaves out conversions expected to happen anyway
├── A machine learning model, not an experiment
│   (for an experiment, use Conversion Lift)
└── An estimate of the ad's causal effect
```

### Meta's Incremental Attribution Setting

```
How to Enable (Meta Ads Manager, at the ad set level):
1. Objective: Sales, Engagement or Leads
2. Conversion location: Website, or Website and app
3. Conversion goal: maximize number or value of conversions
4. Show more options → Attribution model → Incremental

Constraints:
├── No bid controls with incremental attribution
├── The model cannot be changed after publishing
│   (create a new campaign to switch)
└── Columns → Compare attribution models → Incremental shows
    modeled results for any campaign (not before 1 April 2025)

Impact:
├── Reported conversions LOWER (only incremental)
├── ROAS and cost per result count incremental conversions only
└── Delivery optimizes for incremental conversions
```

Sources (checked 2026-10-10): Meta Business Help Center, "About incremental attribution"; "How to use incremental attribution in Meta Ads Manager"; "How to view results for incremental attribution in Meta
Ads Manager"

### When to Use Incremental Attribution

```
USE INCREMENTAL WHEN:
├── High retargeting spend
├── Strong organic conversion base
├── Want delivery and reporting on incremental conversions
├── Budget optimization priority
└── Advanced measurement maturity

STICK TO STANDARD WHEN:
├── Low conversion volume
├── New accounts/campaigns
├── Primarily prospecting
├── Need learning phase data
└── Simple measurement needs
```

## Attribution Comparison Framework

### Meta vs Google Attribution

```
COMPARISON NOTES:
├── Different attribution models
├── Different tracking methods
├── Overlap in conversions
└── Don't add together!

Meta Attribution:
├── People-based (logged-in users)
├── Cross-device by default
├── View-through and engage-through can be included
└── Click: 1 or 7 days, view: 1 day (set per ad set)

Google Ads:
├── Cookie/click-based
├── Data-driven is the default for most conversion actions
├── View-through reported for Display Network and video ads
└── Last click is the other model listed; first click, linear,
    time decay and position-based are no longer supported

RECONCILIATION:
├── Expect overlap: measure it against your own orders
├── Use holistic measurement (MMM)
├── Post-purchase surveys for truth
└── Don't optimize for one at expense of other
```

### Multi-Touch Attribution Considerations

```
META'S APPROACH:
├── Standard: conversions within the ad set's click, view
│   or engage-through window
├── Incremental: only conversions Meta models as caused by the ad
├── Custom attribution: share your own attribution data with
│   Meta, and delivery optimizes toward it
└── Meta's cross-publisher attribution tool (Facebook Attribution)
    was retired on 25 August 2021

FOR MULTI-TOUCH:
├── Use third-party tools (Triple Whale, Northbeam)
├── Implement Marketing Mix Modeling
├── Post-purchase surveys
└── Platform-agnostic measurement
```

Sources (checked 2026-10-10): Google Ads Help, "About attribution models",
https://support.google.com/google-ads/answer/6259715; Google Ads Help, "About view-through conversions",
https://support.google.com/google-ads/answer/16542520; Meta Business Help Center, "About attribution models and
attribution settings"; "Retiring Facebook Attribution"

## Attribution Configuration Guide

### Setup Checklist

```
BEFORE CONFIGURING:

□ Define conversion events
  └── What actions matter most?

□ Understand buying cycle
  └── How long from awareness to purchase?

□ Set measurement goals
  └── Volume vs. incrementality?

□ Establish baselines
  └── Current performance benchmarks

CONFIGURATION:

□ Ad set level settings
  └── Ads Manager → Ad set → Conversion → Show more options
      → Attribution model and attribution settings

□ Consistent across campaigns
  └── Use same windows for comparison

□ Document choices
  └── Why this configuration?
```

### Attribution Settings by Campaign Type

| Campaign Type | Recommended Window | View-Through | Notes |
|--------------|-------------------|--------------|-------|
| **Prospecting** | 7-day click | 1-day | Capture delayed conversions |
| **Retargeting** | 7-day click | 1-day or None | Consider incrementality |
| **Brand Awareness** | 7-day click | 1-day | Measure full impact |
| **Advantage+ Catalog Ads** | 7-day click | 1-day | Standard e-commerce |
| **Lead Gen** | 7-day click | 1-day | Research-heavy decision |
| **App Install** | 7-day click | Not on iOS 14+ campaigns | iOS 14+ installs report 1-day or 7-day click (AEM), or through SKAdNetwork |

Rules of thumb, not Meta figures: check them against the account's own history. The App Install row follows Meta's
note on iOS 14 and later app install campaigns (Meta Business Help Center, "About attribution models and attribution
settings", checked 2026-10-10).

## Attribution Analysis

Rules of thumb, not Meta figures: check them against the account's own history. This covers the lift and
view-through bands below.

### Comparing Attribution Windows

```
HOW TO ANALYZE IMPACT:

1. Run comparison (Ads Manager → Columns → Compare attribution settings):
   ├── Show 1-day click and 7-day click side by side
   ├── Same period, no change to the ad set setting
   └── Compare conversion difference

2. Calculate "extended window lift":
   ├── (7-day conversions - 1-day conversions) / 1-day conversions
   └── Shows delayed conversion rate

3. Interpret:
   ├── >50% lift: Long consideration, use 7-day
   ├── 20-50% lift: Normal, 7-day appropriate
   └── <20% lift: Quick decisions, 1-day sufficient
```

### View-Through Impact Analysis

```
MEASURING VT CONTRIBUTION:

1. Compare columns (Compare attribution settings):
   ├── 1-day view next to the click-through columns
   ├── Same period: no need to switch view-through off
   └── Measure conversion difference

2. Calculate VT percentage:
   ├── (VT conversions) / (Total conversions)
   └── Shows VT contribution to reported results

3. Evaluate:
   ├── >30% VT: Significant brand influence
   ├── 10-30% VT: Normal awareness contribution
   └── <10% VT: Minimal impact, consider disabling
```

## Troubleshooting Attribution

### Common Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| Conversion delay | Sales missing, appear later | Recheck the period later; SKAdNetwork app results arrive at least 24 hours late |
| Over-attribution | More conversions than orders | Check deduplication, VT impact |
| Under-attribution | Fewer conversions than expected | Check pixel/CAPI, attribution window |
| Inconsistent data | Different numbers in reports | Verify date ranges, attribution settings |
| GA4 mismatch | Meta shows more conversions | Different models, VT inclusion |

### Attribution Audit Template

```markdown
# Attribution Audit

## Current Configuration
- Click window: [1-day / 7-day]
- View window: [None / 1-day]
- Engage-through: [None / 1-day]
- Incremental: [Yes / No]

## Conversion Analysis
- Reported conversions: [X]
- Platform transactions: [Y]
- Difference: [Z]%

## Attribution Window Analysis
| Window | Conversions | % of Total |
|--------|-------------|------------|
| 1-day click | [X] | [X]% |
| 2-7 day click | [Y] | [Y]% |
| 1-day view | [Z] | [Z]% |
| 1-day engage-through | [W] | [W]% |

## Recommendations
1. [Recommendation based on analysis]
2. [Additional recommendation]

## Action Items
□ [Action 1]
□ [Action 2]
```

## MCP: Analyze Attribution Impact

```python
# Which attribution setting does each ad set use? (attribution_spec: event type and window per ad set)
meta_query(account_id="act_XXXXX", entity_type="adsets", fields=["id","name","attribution_spec"])

# Results per ad set, each under its own attribution setting
meta_get_insights(account_id="act_XXXXX", level="adset", fields=["spend","actions","cost_per_action_type","website_purchase_roas"], date_preset="last_30d")
```

`meta_get_insights` has no attribution-window parameter, so it cannot split results into click, view or
engage-through. Since 10 June 2025 the Insights API reports each ad set under its own attribution setting, as Ads
Manager does (Marketing API, "Limits and Best Practices", checked
2026-10-10). For a click versus view split, use Compare attribution settings in Ads Manager. The tool returns one
page of rows; fetch the next with `meta_query(account_id, "ads", pagination_url=<paging.next>)`.

## Best Practices

```
DO:
├── Keep attribution consistent across campaigns
├── Document your attribution choices
├── Compare trends, not absolute numbers
├── Use multiple measurement sources
├── Accept some measurement uncertainty

DON'T:
├── Change attribution mid-campaign
├── Compare campaigns with different windows
├── Obsess over exact conversion counts
├── Ignore iOS measurement limitations
├── Add Meta + Google conversions together
```

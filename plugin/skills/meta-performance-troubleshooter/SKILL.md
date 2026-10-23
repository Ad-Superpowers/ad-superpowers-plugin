---
name: meta-performance-troubleshooter
description: "This skill should be used when the user asks to \"troubleshoot campaign performance\", \"diagnose delivery issues\", \"fix high CPA\", or mentions \"underperforming Meta ads\", \"Ad Relevance Diagnostics\", or \"kill vs scale decision\". Do NOT use for: learning phase issues (use learning-phase-tracker), bid strategy changes (use bid-strategy-selector), creative fatigue specifically (use creative-fatigue-analyzer)."
---
# Performance Troubleshooter

Diagnostic framework for identifying and resolving Meta Ads performance problems.

## Quick Diagnostic

```
WHAT IS THE PRIMARY SYMPTOM?
│
├─► No or low delivery
│   └─► Go to [Delivery Issues]
│
├─► High CPA / Low ROAS
│   └─► Go to [Efficiency Problems]
│
├─► Low CTR
│   └─► Go to [Engagement Issues]
│
├─► High CPM
│   └─► Go to [Auction Competition]
│
├─► Performance declining over time
│   └─► Go to [Performance Decay]
│
└─► Conversions not tracked
    └─► Go to [Tracking Issues]
```

## Diagnostic Framework

### Step 1: Check Fundamentals

```
FUNDAMENTALS CHECKLIST:
□ Pixel firing? (meta_query(account_id, "adspixels") shows last_fired_time; event diagnostics are in Events Manager)
□ CAPI active? (Server events visible?)
□ Event Match Quality? (meta_query(account_id, "dataset_quality", entity_id=<pixel_id>): composite_score per web event)
□ Attribution window correct? (Match buying cycle)
□ Budget sufficient? (Enough for about 50 results a week per ad set: daily budget of about 50 x CPA / 7)
□ Audience size adequate? (Rule of thumb, not a Meta figure: 1M+ for prospecting)
□ Creative variety? (Count distinct concepts, not ad objects: Meta treats look-alike ads as variations of the same creative)
```

The 50 is Meta's learning phase figure: an ad set usually exits learning after about 50 results in the week after
its last significant edit, and a budget too low for that keeps it learning limited (Meta Business Help Center,
"About the learning phase", and "About learning limited", checked 2026-10-10). Meta scores EMQ out of 10 for
website events sent through the Conversions API ("About event match quality").

### Step 2: Ad Relevance Diagnostics

Meta's 3 ranking metrics at ad level:

| Metric | Meaning | Below Average = |
|--------|---------|-----------------|
| **Quality Ranking** | Perceived quality vs competitors | Improve creative/landing page |
| **Engagement Rate Ranking** | Expected engagement vs competitors | Better hooks, more compelling creative |
| **Conversion Rate Ranking** | Expected CVR vs competitors | Landing page issues, audience mismatch |

Meta does not show these rankings for ads with fewer than 500 impressions, and they are not inputs into the
auction (Meta Business Help Center, "About ad relevance diagnostics", checked 2026-10-10).

### Step 3: Identify Root Cause

Use diagnostic matrix below per symptom.

## Delivery Issues

Rules of thumb, not Meta figures: check them against the account's own history.

### Symptom: No or Very Low Impressions

```
DIAGNOSE: Why no delivery?
│
├─► Ad Account Issues
│   ├── Account restricted/disabled?
│   ├── Payment method issue?
│   └── Policy violation?
│
├─► Campaign Settings
│   ├── Budget too low?
│   ├── Bid/Cost cap too restrictive?
│   ├── Schedule issues? (Ads not active?)
│   └── Campaign paused?
│
├─► Audience Issues
│   ├── Audience too small? (<50K)
│   ├── Too many exclusions?
│   ├── Geo targeting too narrow?
│   └── Overlap with other campaigns?
│
├─► Ad Issues
│   ├── Ads rejected/in review?
│   ├── Low Quality Ranking?
│   └── Policy flags?
│
└─► Competition Issues
    ├── Auction outbid?
    └── CPM spike in market?
```

### Solutions Matrix: Delivery

| Issue | Diagnose Via | Solution |
|-------|--------------|----------|
| Budget too low | Results per week vs about 50 (Meta's learning phase figure) | Raise the budget or combine ad sets |
| Bid cap too low | "Learning limited" tooltip names a low bid or cost control | Raise the cap (rule of thumb: 20-30%) or switch to LOWEST_COST_WITHOUT_CAP |
| Audience too small | Audience size estimate | Broader targeting, remove restrictions |
| Ads rejected | Ad status | Fix policy issues, appeal if incorrect |
| Low quality | Quality Ranking | Improve creative, landing page |
| Outbid by competitors | Rising CPM, spend below budget | Increase bid or switch strategy |
| Auction overlap (own ad sets) | Overlapping audiences across your ad sets | Combine similar ad sets or turn off overlapping ones |

When two or more of your ads enter the same auction, Meta lets only the one with the highest total value
compete, so your ads do not bid against each other; overlap can stop an ad set from spending its budget or leaving learning
(Meta Business Help Center, "Understand auction overlap",
checked 2026-10-10).

## Efficiency Problems

### Symptom: High CPA / Low ROAS

```
DIAGNOSE: Why high CPA?
│
├─► Funnel Analysis
│   ├── CPM normal, CTR low → Creative issue
│   ├── CPM normal, CTR normal, CVR low → Landing page issue
│   ├── CPM high, CTR normal → Audience/competition issue
│   └── All metrics degraded → Multiple issues
│
├─► Funnel Metrics Checklist (benchmarks: rules of thumb, not Meta figures; compare with the account's history)
│   ├── CPM: €[X] (Benchmark: €15-25)
│   ├── CTR: [X]% (Benchmark: 1-2%)
│   ├── CPC: €[X] (Benchmark: €0.50-1.00)
│   ├── LP → ATC: [X]% (Benchmark: 15%)
│   ├── ATC → Purchase: [X]% (Benchmark: 30-50%)
│   └── Overall CVR: [X]% (Benchmark: 2-5%)
│
└─► Identify Bottleneck
    └─► Focus optimization effort there
```

### Solutions Matrix: Efficiency

| Bottleneck | Symptom | Solution |
|------------|---------|----------|
| Creative | Low CTR | Test new hooks, formats, angles |
| Targeting | High CPM, normal CTR | Broader audience, less competition |
| Landing Page | High CTR, low CVR | UX audit, speed test, trust elements |
| Offer | Good traffic, no sales | Price, value prop, urgency |
| Tracking | Conversions missing | Fix Pixel/CAPI, check deduplication |
| Attribution | Sales in GA but not Meta | Attribution window, cross-device |

### Funnel Optimization Priority

```
PRIORITY ORDER:
1. Fix tracking first (no data = optimizing blind)
2. Landing page
3. Creative
4. Targeting (let AI help)
5. Bid strategy (fine-tuning)
```

## Engagement Issues

### Symptom: Low CTR

```
CTR BENCHMARK (rules of thumb, not Meta figures: check them against the account's own history):
├── Poor: <0.8%
├── Average: 0.8-1.5%
├── Good: 1.5-2.5%
└── Excellent: >2.5%

LOW CTR CAUSES:
│
├─► Creative Issues
│   ├── Weak hook (first 3 sec video)
│   ├── Unclear value proposition
│   ├── Poor visual quality
│   ├── Wrong format for placement
│   └── Creative fatigue
│
├─► Targeting Issues
│   ├── Irrelevant audience
│   ├── Audience too broad
│   └── Message-audience mismatch
│
└─► Ad Copy Issues
    ├── Weak headline
    ├── No clear CTA
    └── Benefits unclear
```

### Solutions: Low CTR

```
CREATIVE FIXES:
├── Test several new hook variations
├── A/B test headlines
├── Try different formats (video vs static)
├── Update visuals/thumbnails
└── Add motion/animation

TARGETING FIXES:
├── Narrow to higher-intent segments
├── Test different interest combinations
├── Create lookalikes from purchasers
└── Exclude low-engagement segments

COPY FIXES:
├── Lead with benefit, not feature
├── Add social proof
├── Create urgency
└── Clearer, action-oriented CTA
```

## Auction Competition

### Symptom: High CPM

```
CPM BENCHMARK (rules of thumb, not Meta figures: check them against the account's own history):
├── Low: <€10
├── Average: €15-25
├── High: €25-40
└── Very High: >€40

HIGH CPM CAUSES:
│
├─► Market Factors
│   ├── Peak season (Q4, Black Friday)
│   ├── Industry competition spike
│   └── Major events/elections
│
├─► Targeting Factors
│   ├── Very competitive audience
│   ├── Small audience (premium pricing)
│   └── Overlapping with own campaigns
│
└─► Quality Factors
    ├── Below-average ad relevance diagnostics
    ├── Poor engagement history
    └── New ad account (no history)
```

Ad quality and estimated action rates are part of the auction's total value, next to the bid, so a more relevant
ad could win against higher bids (Meta Business Help Center, "About ad auctions", checked 2026-10-10). The old relevance score was
replaced by ad relevance diagnostics.

### Solutions: High CPM

```
IMMEDIATE ACTIONS:
├── Expand audience
├── Remove restrictive targeting
├── Test different placements (including Threads)
├── Check audience overlap with Meta's overlap tool in Ads Manager (the MCP audienceoverlap route returned a Meta error in our tests; see audience-overlap-detector)

STRATEGIC ACTIONS:
├── Improve ad quality (better auction position)
├── Test off-peak timing
├── Build lookalikes from best customers
└── Diversify to less competitive channels

SEASONAL STRATEGY:
├── Pre-peak: Lock in audiences, test creatives
├── Peak: Accept higher CPM, focus on ROAS
└── Post-peak: Capitalize on lower competition
```

## Performance Decay

### Symptom: Metrics Declining Over Time

```
DECAY DIAGNOSIS (thresholds are rules of thumb, not Meta figures: check them against the account's own history):
│
├─► Creative Fatigue
│   ├── Symptoms: Rising frequency, falling CTR
│   ├── Threshold: Frequency >3-4
│   └── Solution: Fresh creative rotation
│
├─► Audience Saturation
│   ├── Symptoms: Shrinking reach, high frequency
│   ├── Threshold: Reached >70% of audience
│   └── Solution: Expand targeting, new audiences
│
├─► Seasonal Effects
│   ├── Symptoms: Industry-wide decline
│   └── Solution: Adjust expectations, test new offers
│
├─► Competitor Activity
│   ├── Symptoms: CPM up, CTR down
│   └── Solution: Differentiate, refresh positioning
│
└─► Algorithm Changes
    ├── Symptoms: Sudden performance shift
    └── Solution: Adapt to new best practices
```

### Creative Fatigue Detection

```
META'S OWN SIGNAL:
□ Delivery column shows "Creative limited" or "Creative fatigue"

FATIGUE INDICATORS (rules of thumb, not Meta figures: check them against the account's own history):
□ CTR dropping week-over-week
□ Frequency >4 in past 7 days
□ Same creative running >14-21 days
□ Engagement Rate Ranking declining
□ CPM increasing without market shift

REFRESH CADENCE (rules of thumb, not Meta figures: check them against the account's own history):
├── High-spend campaigns: Every 7-14 days
├── Medium-spend: Every 14-21 days
├── Low-spend: Every 21-30 days
└── Evergreen/testimonials: Can run longer
```

Meta shows "Creative limited" when an ad's cost per result is above that of ads you ran in the past but less than
twice as much, and "Creative fatigue" at twice as much or more. Meta offers this only for ad sets with one creative,
and not for Advantage+ catalog ads, dynamic creative or Advantage+ app campaigns (Meta Business Help Center, "About
creative fatigue recommendations in Meta Ads Manager",
checked 2026-10-10). Check the status in Ads Manager.

## Tracking Issues

### Symptom: Conversions Not Tracked

```
TRACKING DIAGNOSTIC:
│
├─► Pixel Issues
│   ├── Pixel not installed correctly
│   ├── Pixel blocked by ad blockers
│   ├── Event not firing on conversion
│   └── Wrong pixel ID
│
├─► CAPI Issues
│   ├── CAPI not configured
│   ├── Events not deduplicating
│   ├── Low Event Match Quality
│   └── Token expired
│
├─► Attribution Issues
│   ├── Wrong attribution window
│   ├── Cross-device not tracked
│   ├── Long purchase cycle
│   └── iOS privacy impact
│
└─► Technical Issues
    ├── Thank you page not loading
    ├── Redirect issues
    └── Tag manager conflicts
```

### Tracking Fix Checklist

```
QUICK FIXES:
□ Test Pixel with Meta Ads Data Advisor (formerly Meta Pixel Helper; a Chrome extension)
□ Check Events Manager for recent events (meta_query(account_id, "adspixels") only gives last_fired_time)
□ Skip domain verification and AEM event ranking: Meta no longer requires either for web event setup
□ Confirm event parameters (value, currency)
□ Check for duplicate events

CAPI VERIFICATION (check these in Events Manager):
□ Server events visible in Events Manager?
□ Deduplication working? (Same event from 2 sources)
□ Event Match Quality 6.0 or higher where possible? (Meta's recommendation, "Verifying Your Setup", Conversions API docs)
□ Customer parameters hashed correctly?

ATTRIBUTION CHECK:
□ Attribution window matches buying cycle
□ GA4 comparison (same trends?)
□ Post-purchase survey attribution
```

Meta's Aggregated Event Measurement page says web events need no AEM setup any more, the 8-event prioritization
is gone, and domain verification is no longer required for event configuration, though a business may still need
it for other reasons (Meta Business Help Center, "About Meta's Aggregated Event Measurement", checked 2026-10-10). Meta renamed the Pixel Helper
extension to Meta Ads Data Advisor (Meta for Developers, "Meta Ads Data Advisor", checked 2026-10-10).

## Kill vs Scale Decision

Rules of thumb, not Meta figures: check them against the account's own history.

### Decision Framework

```
SCALE SIGNALS (Increase Budget):
├── ROAS >target for 5+ days
├── CPA <target and stable
├── CTR above benchmark
├── Frequency <3
├── Room to grow in audience
└── Consistent daily performance

OPTIMIZE SIGNALS (Test & Tweak):
├── ROAS within 20% of target
├── CPA fluctuating but manageable
├── Some ads performing, others not
├── Creative starting to fatigue
└── Potential with adjustments

KILL SIGNALS (Pause/Stop):
├── ROAS <1x (losing money)
├── CPA >2x target for 7+ days
├── CTR <0.5% consistent
├── No improvements despite tests
├── Insufficient budget for learning
└── Audience exhausted
```

### Kill Decision Checklist

```
BEFORE KILLING, VERIFY:
□ Tracking is accurate (not a tracking issue)
□ Attribution window appropriate
□ Gave sufficient time (7+ days minimum)
□ Tested multiple creatives
□ Budget was adequate
□ Not during anomaly period (holiday, etc.)

IF ALL VERIFIED, THEN:
├── Killing = correct decision
├── Document learnings
├── Archive for reference
└── Reallocate budget to winners
```

## MCP: Pull Performance Data for Diagnosis

```python
# Get campaign-level performance metrics
meta_get_insights(account_id="act_XXXXX", level="campaign", date_preset="last_7d", fields=["spend","impressions","clicks","ctr","cpm","cpc","actions","cost_per_action_type","frequency"])

# Get ad-level breakdown to isolate creative issues
meta_get_insights(account_id="act_XXXXX", level="ad", date_preset="last_7d", fields=["spend","impressions","clicks","ctr","frequency","actions","quality_ranking","engagement_rate_ranking","conversion_rate_ranking"])

# meta_get_insights returns one page of rows: while a response has paging.next, fetch the next page
meta_query(account_id="act_XXXXX", entity_type="ads", pagination_url="<paging.next>")
```

## Troubleshooting Output Template

```markdown
# Campaign Troubleshooting Report

## Campaign Overview
- Campaign: [name]
- Objective: [objective]
- Daily Budget: €[X]
- Running since: [date]
- Current Status: [status]

## Symptom Analysis
**Primary symptom:** [description]
**Duration:** [since when]
**Severity:** [Low/Medium/High/Critical]

## Diagnostic Results

### Fundamentals Check
- [x] Pixel: [OK/Issue]
- [x] CAPI: [OK/Issue]
- [x] EMQ: [score]
- [x] Budget: [OK/Issue]
- [x] Audience: [OK/Issue]

### Key Metrics
| Metric | Current | Benchmark | Status |
|--------|---------|-----------|--------|
| CPM | €[X] | [from this account's history] | [OK/High/Low] |
| CTR | [X]% | [from this account's history] | [OK/High/Low] |
| CPC | €[X] | [from this account's history] | [OK/High/Low] |
| CVR | [X]% | [from this account's history] | [OK/High/Low] |
| CPA | €[X] | €[target] | [OK/High] |
| ROAS | [X]x | [target]x | [OK/Low] |

### Root Cause Identified
[Description of root cause]

## Recommended Actions

### Immediate (This Week)
1. [Action 1]
2. [Action 2]

### Short-term (2-4 Weeks)
1. [Action 1]
2. [Action 2]

### Monitor
- [Metric 1]: Watch for [threshold]
- [Metric 2]: Watch for [threshold]

## Prognosis
[Metrics to re-check after the actions, with today's values as the baseline. Estimate an outcome only from this account's own data, with the assumptions stated; otherwise write "not estimated".]
```

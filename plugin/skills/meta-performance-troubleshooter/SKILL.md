---
name: performance-troubleshooter
description: |
  This skill should be used when the user asks to "troubleshoot campaign performance",
  "diagnose delivery issues", "fix high CPA", or mentions "underperforming Meta ads",
  "Ad Relevance Diagnostics", or "kill vs scale decision". Do NOT use for: learning phase
  issues (use learning-phase-tracker), bid strategy changes (use bid-strategy-selector),
  creative fatigue specifically (use creative-fatigue-analyzer).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "meta"
  phase: "fase-1-foundation"
compatibility: "Requires AdSuperpowers MCP server with Meta Ads connection"
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
□ Pixel firing correctly? (⚠️ UI-only — no API for pixel diagnostics; check Events Manager)
□ CAPI active? (Server events visible?)
□ Event Match Quality? (⚠️ UI-only — EMQ score not available via API; check Events Manager)
□ Attribution window correct? (Match buying cycle)
□ Budget sufficient? (Min €50/day for learning)
□ Audience size adequate? (Min 1M+ for prospecting)
□ Creative variety? (Min 3-5 ads per ad set)
```

### Step 2: Ad Relevance Diagnostics

Meta's 3 ranking metrics at ad level:

| Metric | Meaning | Below Average = |
|--------|---------|-----------------|
| **Quality Ranking** | Perceived quality vs competitors | Improve creative/landing page |
| **Engagement Rate Ranking** | Expected engagement vs competitors | Better hooks, more compelling creative |
| **Conversion Rate Ranking** | Expected CVR vs competitors | Landing page issues, audience mismatch |

### Step 3: Identify Root Cause

Use diagnostic matrix below per symptom.

## Delivery Issues

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
| Budget too low | Spend vs budget | Increase to €50+/day |
| Bid cap too low | Delivery insights | Increase 20-30% or switch to Lowest Cost |
| Audience too small | Audience size estimate | Broader targeting, remove restrictions |
| Ads rejected | Ad status | Fix policy issues, appeal if incorrect |
| Low quality | Quality Ranking | Improve creative, landing page |
| Outbid | Auction overlap | Increase bid or switch strategy |

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
├─► Funnel Metrics Checklist
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
2. Landing page (often 2-3x lift possible)
3. Creative (highest ongoing impact)
4. Targeting (let AI help)
5. Bid strategy (fine-tuning)

ROI PER FIX:
├── Tracking: 50-200% improvement possible
├── Landing page: 20-100% CVR lift
├── Creative: 20-50% CTR lift
├── Targeting: 10-30% efficiency gain
└── Bid strategy: 5-15% fine-tuning
```

## Engagement Issues

### Symptom: Low CTR

```
CTR BENCHMARK:
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
├── Test 5+ new hook variations
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
CPM BENCHMARK:
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
    ├── Low relevance score
    ├── Poor engagement history
    └── New ad account (no history)
```

### Solutions: High CPM

```
IMMEDIATE ACTIONS:
├── Expand audience (larger = cheaper)
├── Remove restrictive targeting
├── Test different placements (including Threads — new March 2026, lower CPM early stage)
├── Check audience overlap tool

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
DECAY DIAGNOSIS:
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
FATIGUE INDICATORS:
□ CTR dropping week-over-week
□ Frequency >4 in past 7 days
□ Same creative running >14-21 days
□ Engagement Rate Ranking declining
□ CPM increasing without market shift

REFRESH CADENCE:
├── High-spend campaigns: Every 7-14 days
├── Medium-spend: Every 14-21 days
├── Low-spend: Every 21-30 days
└── Evergreen/testimonials: Can run longer
```

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
□ Test Pixel with Meta Pixel Helper (⚠️ UI-only — browser extension)
□ Check Events Manager for recent events (⚠️ UI-only — event diagnostics not in API)
□ Verify domain is verified
□ Confirm event parameters (value, currency)
□ Check for duplicate events

CAPI VERIFICATION (⚠️ all UI-only — Events Manager required):
□ Server events visible in Events Manager?
□ Deduplication working? (Same event from 2 sources)
□ Event Match Quality >7?
□ Customer parameters hashed correctly?

ATTRIBUTION CHECK:
□ Attribution window matches buying cycle
□ GA4 comparison (same trends?)
□ Post-purchase survey attribution
```

## Kill vs Scale Decision

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
| CPM | €[X] | €15-25 | [OK/High/Low] |
| CTR | [X]% | 1-2% | [OK/High/Low] |
| CPC | €[X] | €0.50-1 | [OK/High/Low] |
| CVR | [X]% | 2-5% | [OK/High/Low] |
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
[Expected outcome if recommendations followed]
```

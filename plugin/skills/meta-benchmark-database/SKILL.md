---
name: meta-benchmark-database
description: "This skill should be used when the user asks to \"compare my metrics to benchmarks\", \"find industry averages\", \"set campaign targets\", or mentions \"Meta Ads benchmarks\", \"CPM by industry\", or \"average CTR for my vertical\". Do NOT use for: performance diagnostics (use performance-troubleshooter), account audits (use account-auditor), scaling decisions (use scaling-calculator)."
---
# Benchmark Database

## Overview

This skill gives rule-of-thumb ranges for Meta Ads metrics by industry, funnel stage and ad format, so you can place an account's metrics in rough context. Compare with the account's own history first; use these ranges when that history is thin.

## Benchmark Disclaimer

```
IMPORTANT CONTEXT

Rules of thumb, not Meta figures: check them against the account's own history.
├── The Poor/Average/Good/Excellent bands are our working ranges,
│   not figures from Meta or from a named benchmark report
├── Primarily focused on Western markets
├── Attribution: Meta reports results by each ad set's attribution
│   setting, so compare figures read at the same setting. Since
│   12 January 2026 the Insights API no longer returns 7-day view
│   or 28-day view results
└── Subject to seasonal fluctuations

Benchmarks are GUIDELINES, not absolute truths:
├── Your specific niche may differ significantly
├── Product pricing strongly influences metrics
├── Audience quality determines a lot
└── Always compare with your own historical data
```

Attribution sources: "Limits and Best Practices", Meta Marketing API docs (beginning 10 June 2025, API results follow each ad set's attribution setting, as Ads Manager does); "Ads Insights API Metric Availability Updates", Meta for Developers, 16 Oct 2025 (7-day view and 28-day view windows no longer returned from 12 January 2026).

## Benchmarks by Industry

Rules of thumb, not Meta figures: check them against the account's own history.

### E-commerce

```
E-COMMERCE BENCHMARKS
=====================

Metric          │ Poor    │ Average │ Good    │ Excellent
────────────────┼─────────┼─────────┼─────────┼──────────
CTR (All)       │ <1.0%   │ 1.0-2.0%│ 2.0-3.0%│ >3.0%
CTR (Link)      │ at or below CTR (All), which counts link clicks too; compare with the account's history
CPC             │ >$1.50  │ $0.80-1.50│ $0.40-0.80│ <$0.40
CPM             │ >$18    │ $10-18  │ $5-10   │ <$5
CPA (Purchase)  │ >$50    │ $25-50  │ $15-25  │ <$15
ROAS            │ <1.5x   │ 1.5-2.5x│ 2.5-4x  │ >4x
Add to Cart Rate│ <3%     │ 3-6%    │ 6-10%   │ >10%
Conversion Rate │ <1%     │ 1-2%    │ 2-4%    │ >4%

SUBCATEGORIES:
├── Fashion: CPA $20-40, ROAS 2.5-4x
├── Beauty: CPA $15-30, ROAS 3-5x
├── Electronics: CPA $30-60, ROAS 2-3x
├── Home & Garden: CPA $25-45, ROAS 2.5-4x
└── Food & Beverage: CPA $10-25, ROAS 3-6x
```

### SaaS / Software

```
SAAS BENCHMARKS
===============

Metric          │ Poor    │ Average │ Good    │ Excellent
────────────────┼─────────┼─────────┼─────────┼──────────
CTR             │ <0.4%   │ 0.4-0.8%│ 0.8-1.5%│ >1.5%
CPC             │ >$3.00  │ $1.50-3 │ $0.80-1.50│ <$0.80
CPM             │ >$20    │ $12-20  │ $6-12   │ <$6
CPL (Lead)      │ >$80    │ $40-80  │ $20-40  │ <$20
CPA (Trial)     │ >$150   │ $80-150 │ $40-80  │ <$40
CPA (Paid)      │ >$300   │ $150-300│ $80-150 │ <$80
Trial to Paid   │ <5%     │ 5-15%   │ 15-25%  │ >25%

NOTES:
├── B2B SaaS: Higher CPA acceptable (LTV!)
├── Freemium: Focus on trial signups
└── Enterprise: CPA can be $500+ (high LTV)
```

### Lead Generation / Services

```
LEAD GEN BENCHMARKS
===================

Metric          │ Poor    │ Average │ Good    │ Excellent
────────────────┼─────────┼─────────┼─────────┼──────────
CTR             │ <0.5%   │ 0.5-1%  │ 1-2%    │ >2%
CPC             │ >$2.50  │ $1-2.50 │ $0.50-1 │ <$0.50
CPM             │ >$18    │ $10-18  │ $5-10   │ <$5
CPL             │ >$50    │ $20-50  │ $10-20  │ <$10
Form Fill Rate  │ <10%    │ 10-20%  │ 20-35%  │ >35%
Lead Quality    │ <5% SQL │ 5-15%   │ 15-30%  │ >30%

INDUSTRY SPECIFIC:
├── Real Estate: CPL $30-80
├── Finance/Insurance: CPL $40-100
├── Legal: CPL $50-150
├── Healthcare: CPL $25-60
├── Education: CPL $15-40
└── B2B Services: CPL $50-200
```

### Local Business

```
LOCAL BUSINESS BENCHMARKS
=========================

Metric          │ Poor    │ Average │ Good    │ Excellent
────────────────┼─────────┼─────────┼─────────┼──────────
CTR             │ <0.6%   │ 0.6-1.2%│ 1.2-2%  │ >2%
CPC             │ >$1.50  │ $0.70-1.50│$0.30-0.70│ <$0.30
CPM             │ >$12    │ $6-12   │ $3-6    │ <$3
Cost per Call   │ >$20    │ $10-20  │ $5-10   │ <$5
Cost per Direction│>$8    │ $4-8    │ $2-4    │ <$2

NOTES:
├── Radius targeting: Tight radius = higher CPM
├── Store visits: no cost per store visit to compare (Meta folded
│   the store traffic objective into its six simplified objectives)
└── Calls: Most trackable local metric
```

Store traffic source: "About the store traffic objective in Meta Ads Manager", Meta Business Help Center.

## Benchmarks by Funnel Stage

Rules of thumb, not Meta figures: check them against the account's own history.

### TOFU (Top of Funnel)

```
TOFU BENCHMARKS - AWARENESS
===========================

Objective: Awareness (reach, brand awareness); video views sit
under both Awareness and Engagement

Metric          │ Poor    │ Average │ Good    │ Excellent
────────────────┼─────────┼─────────┼─────────┼──────────
CPM             │ >$10    │ $5-10   │ $3-5    │ <$3
Reach (per $)   │ <100    │ 100-200 │ 200-350 │ >350
Frequency/week  │ >4      │ 2.5-4   │ 1.5-2.5 │ 1-1.5
ThruPlay Rate   │ compare with the account's own video ads
Cost/ThruPlay   │ >$0.10  │ $0.05-0.10│$0.02-0.05│<$0.02
3-sec View Rate │ compare with the account's own video ads

ThruPlay and Cost/ThruPlay: Ads Manager only (not available
through meta_get_insights). 3-sec view rate through the tool:
the video_view action type in actions, divided by impressions.
```

### MOFU (Middle of Funnel)

```
MOFU BENCHMARKS - CONSIDERATION
===============================

Objective: Traffic / Engagement / Leads

Metric          │ Poor    │ Average │ Good    │ Excellent
────────────────┼─────────┼─────────┼─────────┼──────────
CTR             │ <0.8%   │ 0.8-1.5%│ 1.5-2.5%│ >2.5%
CPC             │ >$1.50  │ $0.80-1.50│$0.40-0.80│<$0.40
Landing Page View Rate│<60%│60-75%  │ 75-85%  │ >85%
Bounce Rate     │ >70%    │ 50-70%  │ 30-50%  │ <30%
Time on Site    │ <30s    │ 30-60s  │ 60-120s │ >120s
Content Eng.    │ <2%     │ 2-5%    │ 5-10%   │ >10%
Email Signup    │ <1%     │ 1-3%    │ 3-6%    │ >6%
```

### BOFU (Bottom of Funnel)

```
BOFU BENCHMARKS - CONVERSION
============================

Objective: Sales (website conversions or catalog)

Metric          │ Poor    │ Average │ Good    │ Excellent
────────────────┼─────────┼─────────┼─────────┼──────────
CTR             │ <1%     │ 1-2%    │ 2-3.5%  │ >3.5%
CPC             │ >$1.20  │ $0.60-1.20│$0.30-0.60│<$0.30
Conv. Rate      │ <2%     │ 2-4%    │ 4-8%    │ >8%
CPA             │ varies by industry (see above)
ROAS            │ varies by industry (see above)
Cart Abandon    │ >80%    │ 70-80%  │ 60-70%  │ <60%
Checkout Comp.  │ <30%    │ 30-50%  │ 50-70%  │ >70%
```

Objective names follow Meta's six objectives (Awareness, Traffic, Engagement, Leads, App promotion, Sales), as the Facebook Ads Guide lists them ("Awareness Image Ad Specs on Facebook Feed", https://www.facebook.com/business/ads-guide/update/image/facebook-feed). The older objectives were deprecated with Marketing API v17.0 ("Bidding overview"). Video views are available under both Awareness and Engagement ("Facebook ad campaign objectives and goals", Meta for Business, https://www.facebook.com/business/ads/ad-objectives).

## Benchmarks by Ad Format

Rules of thumb, not Meta figures: check them against the account's own history.

### Static Image Ads

```
STATIC IMAGE BENCHMARKS
=======================

Metric          │ Poor    │ Average │ Good    │ Excellent
────────────────┼─────────┼─────────┼─────────┼──────────
CTR             │ <0.8%   │ 0.8-1.5%│ 1.5-2.5%│ >2.5%
Engagement Rate │ <1%     │ 1-2%    │ 2-4%    │ >4%
Save Rate       │ <0.1%   │ 0.1-0.5%│ 0.5-1%  │ >1%
Share Rate      │ <0.05%  │ 0.05-0.2%│0.2-0.5% │ >0.5%
```

### Video Ads

```
VIDEO AD BENCHMARKS
===================

Metric          │ Poor    │ Average │ Good    │ Excellent
────────────────┼─────────┼─────────┼─────────┼──────────
3-sec View Rate │ compare with the account's own video ads
ThruPlay Rate   │ compare with the account's own video ads
Avg Watch Time  │ compare with the account's own video ads of similar length
Video Complete  │ compare with the account's own video ads of similar length
CTR (post-view) │ <0.5%   │ 0.5-1%  │ 1-2%    │ >2%
Cost/ThruPlay   │ >$0.12  │ $0.06-0.12│$0.03-0.06│<$0.03

ThruPlay and Cost/ThruPlay: Ads Manager only (not available
through meta_get_insights). Through the tool, 3-sec views are
the video_view action type in actions, and
video_avg_time_watched_actions plus video_p25_watched_actions
to video_p100_watched_actions give watch time and drop-off.
```

### Carousel Ads

```
CAROUSEL AD BENCHMARKS
======================

Metric          │ Poor    │ Average │ Good    │ Excellent
────────────────┼─────────┼─────────┼─────────┼──────────
CTR             │ <1%     │ 1-1.8%  │ 1.8-3%  │ >3%
Cards Viewed    │ <2      │ 2-3     │ 3-4     │ >4
Swipe Rate      │ <30%    │ 30-50%  │ 50-70%  │ >70%
Exit Card       │ Card 1-2│ Card 3-4│ Card 5+ │ Last card
```

### Collection/Instant Experience

```
COLLECTION AD BENCHMARKS
========================

Metric          │ Poor    │ Average │ Good    │ Excellent
────────────────┼─────────┼─────────┼─────────┼──────────
Click to Open   │ <3%     │ 3-6%    │ 6-10%   │ >10%
Time in IE      │ <15s    │ 15-30s  │ 30-60s  │ >60s
Outbound CTR    │ <2%     │ 2-5%    │ 5-10%   │ >10%
Product Views   │ <3      │ 3-6     │ 6-10    │ >10
```

## Seasonal Adjustment Factors

Rules of thumb, not Meta figures: check them against the account's own history.

```
SEASONAL VARIATIONS
====================

MONTH           │ CPM Factor │ CPA Factor │ Notes
────────────────┼────────────┼────────────┼───────────────
January         │   0.85     │   0.90     │ Low competition
February        │   0.90     │   0.95     │ Valentine's spike
March           │   0.95     │   1.00     │ Baseline
April           │   0.95     │   1.00     │ Baseline
May             │   1.00     │   1.00     │ Baseline
June            │   0.95     │   0.98     │ Summer start
July            │   0.90     │   0.95     │ Summer lull
August          │   0.88     │   0.92     │ Summer lull
September       │   1.00     │   1.00     │ Back to school
October         │   1.10     │   1.05     │ Q4 start
November        │   1.35     │   1.20     │ Black Friday
December        │   1.40     │   1.25     │ Holiday peak

Usage: Benchmark x Factor = Seasonally Adjusted Benchmark
With a year of account history, use the account's own
month-to-month CPM and CPA changes instead of these factors.
```

## Benchmark Comparison Template

### When user asks to evaluate metrics:

```
METRIC EVALUATION - [ACCOUNT]
============================

YOUR METRICS vs BENCHMARKS

Metric      │ Your Value  │ Benchmark │ Difference │ Status
────────────┼─────────────┼───────────┼────────────┼────────
CTR         │   [X]%      │   [Y]%    │  [+/-Z%]   │ [green/yellow/red]
CPC         │   $[X]      │   $[Y]    │  [+/-Z%]   │ [green/yellow/red]
CPM         │   $[X]      │   $[Y]    │  [+/-Z%]   │ [green/yellow/red]
CPA         │   $[X]      │   $[Y]    │  [+/-Z%]   │ [green/yellow/red]
ROAS        │   [X]x      │   [Y]x    │  [+/-Z%]   │ [green/yellow/red]
Conv Rate   │   [X]%      │   [Y]%    │  [+/-Z%]   │ [green/yellow/red]

INTERPRETATION:
Green: Above benchmark (>10% better)
Yellow: At benchmark (+/-10%)
Red: Below benchmark (>10% worse)

RECOMMENDATIONS:
├── [Focus area 1]
├── [Focus area 2]
└── [Focus area 3]
```

## MCP Tool Integration

### Pulling Real Data for Benchmark Comparison

Never benchmark against user-provided numbers alone — always pull live account data first:

```
1. Get current metrics (last 30 days):
→ meta_get_insights(account_id="...", level="campaign", date_preset="last_30d", fields=["spend","impressions","ctr","inline_link_click_ctr","inline_link_clicks","cpc","cpm","actions","cost_per_action_type","purchase_roas"])

2. Drill into ad set level for audience-specific benchmarks:
→ meta_get_insights(account_id="...", level="adset", date_preset="last_30d", fields=["ctr","cpc","cost_per_action_type","frequency"])

3. meta_get_insights does not follow paging. If a response has
   paging.next, fetch the next page with:
→ meta_query(account_id="...", entity_type="ads", pagination_url="<paging.next>")
```

`ctr` is CTR (All) and `inline_link_click_ctr` is CTR (Link). Not every metric in the tables comes back from `meta_get_insights`: ThruPlay and cost per ThruPlay are Ads Manager only, Instant Experience metrics are not available through the tool either, and bounce rate and time on site come from the site's analytics (for example `ga4_run_report`), not from Meta.

Then compare the returned metrics with the account's own history first and with the rule-of-thumb tables above second, applying seasonal adjustment factors if relevant.

## Example Interaction

**User**: "My e-commerce fashion campaign has a CTR of 1.2%, CPA of $35 and ROAS of 2.8x. Is that good?"

**Claude response**:

"Let me place your metrics against the rule-of-thumb ranges for fashion e-commerce:

---

**BENCHMARK COMPARISON - Fashion E-commerce:**

| Metric | Your Value | Rule-of-thumb Range | Status |
|--------|------------|-----------------|--------|
| CTR (All) | 1.2% | 1.0-2.0% (average band) | Average |
| CPA | $35 | $20-40 (fashion range) | Within range |
| ROAS | 2.8x | 2.5-4x (fashion range) | Within range |

---

**INTERPRETATION:**

**CTR (1.2%)** - In the average band. Compare it with this campaign's own CTR over the last months before drawing conclusions about the creatives.

**CPA ($35)** - Inside the fashion range. Whether that is good depends on your order value and margin.

**ROAS (2.8x)** - Inside the fashion range. It is profitable only above your breakeven ROAS (1 / gross margin; for example 2.5x at a 40% margin).

---

**RECOMMENDATIONS:**

1. **Lowering CPA** is your biggest opportunity
   - Test genuinely different creative concepts, for example UGC-style against studio
   - Optimize landing page conversion
   - Check audience overlap

2. **Scale potential**: If 2.8x is above your breakeven ROAS, raise the budget in steps while CPA holds

Would you like specific benchmarks for another metric or a comparison with last period?"

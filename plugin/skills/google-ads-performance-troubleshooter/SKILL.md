---
name: google-ads-performance-troubleshooter
description: |
  Diagnoses and resolves Google Ads performance problems using systematic decision trees
  and root cause analysis. Covers CPA/ROAS degradation, conversion volume drops,
  impression share declines, Quality Score problems, Smart Bidding issues, and delivery failures.
  Use when: campaign performance declining, CPA increasing, ROAS dropping, conversions dropping,
  impressions declining, Quality Score issues, Smart Bidding not learning, ads not delivering,
  budget not spending, sudden performance changes.
  Do NOT use for: full account audits (use google-ads-account-auditor), conversion tracking
  setup issues (use google-ads-conversion-tracking-debugger), keyword strategy (use
  google-ads-keyword-strategy-planner).
metadata:
  author: "AdSuperpowers"
  version: "2.0.0"
  platform: "google_ads"
  phase: "fase-4-measurement-attribution"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---

# Performance Troubleshooter

Systematic guide for diagnosing and resolving Google Ads performance problems. Start with the master diagnostic tree, then follow the relevant section for deep-dive analysis.

## Master Diagnostic Tree

```
WHAT IS THE PROBLEM?
│
├─► CONVERSIONS DROPPED
│   Go to: Section 1
│
├─► CPA INCREASED / ROAS DECREASED
│   Go to: Section 2
│
├─► IMPRESSIONS / CLICKS DROPPED
│   Go to: Section 3
│
├─► NO DELIVERY (0 impressions)
│   Go to: Section 4
│
├─► QUALITY SCORE DROPPED
│   Go to: Section 5
│
└─► SMART BIDDING NOT WORKING
    Go to: Section 6
```

---

## Section 1: Conversion Drop Diagnosis

```
CONVERSIONS DROPPED
│
├── Tracking issue? (most common cause)
│   ├── Check: Google Ads → Conversions → Status column
│   │   ├── "No recent conversions" → tag broken or consent blocking
│   │   ├── "Recording conversions" → tracking is fine, issue is elsewhere
│   │   └── "Inactive" → conversion action was paused/removed
│   ├── Check: GA4 events still recording? (cross-reference)
│   ├── Check: GTM container → recent changes published?
│   └── Action: Use conversion-tracking-debugger skill for deep investigation
│
├── Landing page issue?
│   ├── Check: Landing page speed (>3s load = 50%+ bounce increase)
│   ├── Check: Is the page returning 404 or errors?
│   ├── Check: Mobile experience (60%+ of traffic is mobile)
│   └── Action: Test landing pages manually + check GA4 bounce rate trend
│
├── Seasonal/external factor?
│   ├── Check: YoY data — same dip last year?
│   ├── Check: Industry news — competitor launches, market shifts?
│   ├── Check: Day-of-week pattern — was it a holiday?
│   └── Action: Compare with GA4 organic traffic — if organic also dropped, it's market-wide
│
├── Competition increased?
│   ├── Check: Auction Insights → impression share trend
│   ├── Check: Avg CPC trend — rising CPCs = more competition
│   ├── Check: Search impression share → if declining, you're losing auctions
│   └── Action: Review competitor strategies, consider bid adjustments
│
└── Audience exhaustion?
    ├── Check: Frequency (Display/Video) — are you showing ads to same people?
    ├── Check: Audience size — has remarketing pool shrunk?
    └── Action: Refresh audiences, expand targeting, create new segments
```

### MCP Diagnostic Queries

**Check conversion trend:**
```
google_ads_run_gaql(query="
  SELECT segments.date, metrics.conversions, metrics.conversions_value,
         metrics.cost_micros, metrics.cost_per_conversion
  FROM campaign
  WHERE segments.date DURING LAST_30_DAYS
  ORDER BY segments.date DESC
")
```

**Check auction insights:**
```
google_ads_run_gaql(query="
  SELECT campaign.name, metrics.search_impression_share,
         metrics.search_top_impression_percentage,
         metrics.search_budget_lost_impression_share,
         metrics.search_rank_lost_impression_share
  FROM campaign
  WHERE segments.date DURING LAST_14_DAYS
  AND campaign.status = 'ENABLED'
")
```

---

## Section 2: Efficiency Degradation (CPA Up / ROAS Down)

```
CPA INCREASING / ROAS DECLINING
│
├── Gradual increase over weeks?
│   ├── Creative fatigue → CTR declining while impressions stable
│   ├── Audience saturation → same users seeing ads repeatedly
│   ├── Competitive pressure → CPCs rising across the board
│   └── Seasonal trend → compare YoY
│
├── Sudden spike?
│   ├── Tracking change → conversions undercounted (check tracking)
│   ├── Landing page broken → check for 404, slow load, form errors
│   ├── Budget change triggered learning phase reset
│   ├── Bid strategy change → still in learning (wait 2 weeks)
│   └── New competitor → check Auction Insights for new entrants
│
├── Only specific campaigns?
│   ├── Check per-campaign CPA trend to isolate the problem
│   ├── Is it a Search, Display, PMax, or Video campaign?
│   │   ├── Search: Check search terms report for irrelevant queries
│   │   ├── Display: Check placement report for low-quality sites
│   │   ├── PMax: Check asset group performance and search terms
│   │   └── Video: Check view-through vs click-through conversions
│   └── Action: Pause worst performers, reallocate to efficient campaigns
│
└── Account-wide?
    ├── Market shift → industry CPA benchmarks changed
    ├── Attribution window change → compare "Conversions" vs "All conversions"
    ├── Conversion action change → primary vs secondary conversion settings
    └── Action: Review conversion settings, compare with industry benchmarks
```

### CPA Benchmark Reference

| Campaign Type | Good CPA | Average CPA | Investigate If |
|--------------|----------|-------------|---------------|
| Search (non-brand) | <€30 | €30-75 | >€100 |
| Search (brand) | <€10 | €10-25 | >€40 |
| Display | <€50 | €50-150 | >€200 |
| PMax (e-com) | ROAS >300% | ROAS 200-300% | ROAS <150% |
| PMax (lead gen) | <€50 | €50-100 | >€150 |
| YouTube | <€75 | €75-200 | >€300 |

*Note: Benchmarks vary significantly by industry. Use `google-ads-benchmark-database` skill for vertical-specific data.*

---

## Section 3: Volume Decline (Impressions/Clicks Dropping)

```
IMPRESSIONS DECLINING
│
├── Search campaigns?
│   ├── Search impression share dropping?
│   │   ├── "Budget lost" share increasing → budget too low, increase or narrow targeting
│   │   ├── "Rank lost" share increasing → bids too low or Quality Score declining
│   │   └── Both stable → search volume itself is declining (seasonal/market)
│   ├── Check: Google Trends for your keywords — is demand down?
│   ├── Check: Keyword status — are keywords paused, disapproved, or "Below first page bid"?
│   └── Check: Negative keywords — did you accidentally add broad negatives that block traffic?
│
├── Display/Video campaigns?
│   ├── Audience exhaustion → same people targeted repeatedly
│   ├── Placement exclusions → too many sites excluded
│   ├── Frequency cap → set too low?
│   └── Budget constraint → daily budget fully consumed before end of day?
│
├── PMax campaigns?
│   ├── Asset group status → "Limited" or "Low" performance?
│   ├── Audience signals → too narrow?
│   ├── Search themes → check PMax search terms for relevance
│   └── Budget → PMax needs sufficient budget for cross-channel optimization
│
└── All campaigns?
    ├── Account-level issue → payment method declined? Account suspended?
    ├── Billing → check billing summary for payment failures
    ├── Policy → check Ads → Policy details for disapprovals
    └── Geographic → did targeting accidentally narrow?
```

### MCP Diagnostic Queries

**Impression share analysis:**
```
google_ads_run_gaql(query="
  SELECT campaign.name, campaign.advertising_channel_type,
         metrics.impressions, metrics.clicks, metrics.ctr,
         metrics.search_impression_share,
         metrics.search_budget_lost_impression_share,
         metrics.search_rank_lost_impression_share
  FROM campaign
  WHERE segments.date DURING LAST_14_DAYS
  AND campaign.status = 'ENABLED'
  ORDER BY metrics.impressions DESC
")
```

**Search terms quality check:**
```
google_ads_run_gaql(query="
  SELECT search_term_view.search_term, metrics.impressions,
         metrics.clicks, metrics.conversions, metrics.cost_micros
  FROM search_term_view
  WHERE segments.date DURING LAST_14_DAYS
  ORDER BY metrics.cost_micros DESC
  LIMIT 50
")
```

---

## Section 4: No Delivery (0 Impressions)

```
0 IMPRESSIONS
│
├── Check campaign status
│   ├── Campaign enabled? Ad group enabled? Ads enabled?
│   ├── Campaign start/end dates correct?
│   └── Daily budget > €0?
│
├── Check ad approval
│   ├── Ads → Policy details → any disapprovals?
│   ├── Common: restricted content, misleading claims, trademark issues
│   └── Fix: Edit ad to comply with policy, request re-review
│
├── Check targeting
│   ├── Location targeting → is it set to "Presence" not "Presence or interest"?
│   ├── Audience targeting → "Targeting" mode vs "Observation" mode?
│   ├── Keyword status → "Below first page bid" or "Rarely shown"?
│   └── Fix: Broaden targeting, increase bids, or switch to broader match types
│
├── Check billing
│   ├── Payment method active?
│   ├── Account balance/credit available?
│   └── Fix: Update payment method, contact billing support
│
└── Check account status
    ├── Account → Admin → Account status
    ├── Suspended? → review suspension reason, submit appeal
    └── Under review? → wait or contact support
```

---

## Section 5: Quality Score Troubleshooting

```
QUALITY SCORE DECLINING
│
├── Check which component is low (1-10 scale, 7+ is good)
│   ├── Ad Relevance: "Below Average"
│   │   ├── Ad text doesn't contain the keyword or its theme
│   │   ├── Fix: Include keyword in headline 1 or 2
│   │   ├── Fix: Use RSAs with 15 headlines covering key themes
│   │   └── Fix: Tighten ad group structure (fewer, more related keywords)
│   │
│   ├── Expected CTR: "Below Average"
│   │   ├── Ad isn't compelling enough vs competitors
│   │   ├── Fix: Improve headlines — use numbers, urgency, specificity
│   │   ├── Fix: Add all relevant extensions (sitelinks, callouts, structured snippets)
│   │   └── Fix: Test new ad variations focusing on click-through
│   │
│   └── Landing Page Experience: "Below Average"
│       ├── Page load speed (>3 seconds = penalty)
│       ├── Mobile responsiveness
│       ├── Content relevance to ad/keyword
│       ├── Fix: Improve page speed (compress images, reduce scripts)
│       ├── Fix: Ensure keyword theme appears on landing page
│       └── Fix: Improve user experience (clear CTA, no intrusive popups)
│
└── Historical vs current QS
    ├── QS is calculated at auction time — historical QS in reporting is lagged
    ├── Focus on trends, not absolute numbers
    └── QS impact: 7→10 = ~50% CPC reduction; 7→4 = ~100% CPC increase
```

### MCP Quality Score Query

```
google_ads_run_gaql(query="
  SELECT ad_group_criterion.keyword.text,
         ad_group_criterion.quality_info.quality_score,
         ad_group_criterion.quality_info.creative_quality_score,
         ad_group_criterion.quality_info.post_click_quality_score,
         ad_group_criterion.quality_info.search_predicted_ctr,
         metrics.impressions, metrics.clicks, metrics.cost_micros
  FROM keyword_view
  WHERE ad_group_criterion.quality_info.quality_score IS NOT NULL
  AND metrics.impressions > 100
  ORDER BY ad_group_criterion.quality_info.quality_score ASC
  LIMIT 30
")
```

---

## Section 6: Smart Bidding Problems

```
SMART BIDDING NOT PERFORMING
│
├── Still in learning phase?
│   ├── Check: Campaign status shows "Learning" or "Learning (limited)"?
│   ├── Learning requires: ~50 conversions in 30 days (per campaign)
│   ├── "Learning (limited)" = not enough conversion data
│   ├── Fix: Wait 2 weeks without making changes
│   ├── Fix: If limited, consider combining campaigns for more data
│   └── Fix: Use a higher-funnel conversion action (e.g., add-to-cart vs purchase)
│
├── Target too aggressive?
│   ├── tCPA set below historical CPA → algorithm can't find enough auctions
│   ├── tROAS set above historical ROAS → same problem
│   ├── Fix: Start with 20% above current CPA/below current ROAS
│   └── Fix: Gradually tighten targets by 10-15% every 2 weeks
│
├── Not enough conversion data?
│   ├── <30 conversions/month → Maximize Conversions (no target) is better
│   ├── 30-50 conversions/month → tCPA possible but volatile
│   ├── 50+ conversions/month → tCPA/tROAS reliable
│   └── Fix: Use google-ads-bid-strategy-selector skill for right strategy
│
├── Conversion value not set?
│   ├── Using tROAS but no conversion value → bidding blind
│   ├── Fix: Set static values per conversion action
│   ├── Better: Pass dynamic values (cart total, lead score)
│   └── Best: Use value rules to adjust by audience, location, device
│
└── Recent major changes?
    ├── Budget change >20% → triggers learning reset
    ├── Conversion action change → triggers learning reset
    ├── Audience/targeting change → partial reset
    ├── Fix: Make incremental changes (max 15-20% per adjustment)
    └── Fix: Wait 2 weeks between significant changes
```

---

## Output: Troubleshooting Report Template

```markdown
# Google Ads Performance Troubleshooting Report

## Issue Summary
- **Problem:** [CPA increase / conversion drop / impression decline / etc.]
- **First observed:** [Date]
- **Impacted campaigns:** [List]
- **Severity:** [Critical / Warning / Monitor]

## Data Analysis
| Metric | Previous 14d | Current 14d | Change | Status |
|--------|-------------|-------------|--------|--------|
| Impressions | X | X | % | 🟢/🟡/🔴 |
| Clicks | X | X | % | 🟢/🟡/🔴 |
| CTR | X% | X% | % | 🟢/🟡/🔴 |
| Conversions | X | X | % | 🟢/🟡/🔴 |
| CPA | €X | €X | % | 🟢/🟡/🔴 |
| ROAS | X% | X% | % | 🟢/🟡/🔴 |
| Impression Share | X% | X% | % | 🟢/🟡/🔴 |

## Root Cause Analysis
- [ ] Conversion tracking: [OK / Issue found]
- [ ] Landing pages: [OK / Issue found]
- [ ] Ad quality/relevance: [OK / Issue found]
- [ ] Bidding strategy: [OK / Issue found]
- [ ] Budget adequacy: [OK / Issue found]
- [ ] Competition changes: [Stable / Increased]
- [ ] Seasonal factors: [None / Present]

**Identified cause:** [Description with evidence]

## Recommended Actions

### Immediate (Today)
1. [Action with expected impact]

### This Week
1. [Action with expected impact]

### Ongoing Prevention
1. [Monitoring plan]
```

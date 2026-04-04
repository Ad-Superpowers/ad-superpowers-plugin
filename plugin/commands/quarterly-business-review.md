---
description: Quarterly business review template — 90-day performance trends, YoY comparison, strategic recommendations, and next quarter plan
---

# Quarterly Business Review (QBR)

Generate a comprehensive quarterly business review covering all connected advertising platforms.

## Step 1: Define Review Period

Ask the user for:
- **Quarter**: Q1/Q2/Q3/Q4 and year
- **Comparison period**: Previous quarter and/or same quarter last year
- **Business context**: Any major changes (new products, market shifts, seasonal events)

## Step 2: Gather Cross-Platform Data

Pull 90-day data from all connected platforms:

**Meta Ads:**
- `meta_get_insights` with date_preset="last_90d" at account and campaign level

**Google Ads:**
- `google_ads_run_gaql` for quarterly campaign performance with monthly segments

**GA4:**
- `ga4_run_report` for website metrics, traffic sources, and conversion trends

**LinkedIn Ads:**
- `linkedin_get_analytics` for quarterly B2B performance

**TikTok Ads:**
- `tiktok_get_report` for quarterly campaign data

**GSC:**
- `gsc_search_analytics` for organic search trends (90 days)

## Step 3: Executive Summary

```
## Quarterly Business Review: [Client] — [Quarter Year]

### Executive Summary
- Total investment: €X (+/- X% vs previous quarter)
- Total conversions: X (+/- X%)
- Blended CPA: €X (+/- X%)
- Blended ROAS: Xx (+/- X%)
- Key achievement: [biggest win]
- Key challenge: [biggest issue]
```

## Step 4: Platform Performance

| Platform | Q Spend | Conversions | CPA | ROAS | QoQ Change | Status |
|----------|---------|-------------|-----|------|------------|--------|
| Meta | ... | ... | ... | ... | ... | ... |
| Google Ads | ... | ... | ... | ... | ... | ... |
| LinkedIn | ... | ... | ... | ... | ... | ... |
| TikTok | ... | ... | ... | ... | ... | ... |
| **Total** | ... | ... | ... | ... | ... | ... |

## Step 5: Monthly Trend Analysis

Show month-by-month progression within the quarter:
| Month | Spend | Conversions | CPA | ROAS | Notable Events |
|-------|-------|-------------|-----|------|---------------|

## Step 6: Channel Analysis

For each active platform, analyze:
- **What worked**: Top campaigns, audiences, creatives
- **What didn't**: Underperformers, wasted spend, missed opportunities
- **Key learnings**: Data-driven insights for next quarter

## Step 7: Organic vs Paid (if GSC connected)

- Organic traffic trend vs paid traffic
- Keyword overlap opportunities
- Content gaps identified from paid search data

## Step 8: Strategic Recommendations

### Next Quarter Plan
1. **Budget recommendation**: Increase/decrease/maintain per platform with rationale
2. **Testing agenda**: What to test next quarter (audiences, creatives, channels)
3. **Growth opportunities**: New platforms, campaign types, or audiences to explore
4. **Risk mitigation**: Issues to address before they impact performance

### 90-Day Roadmap
- **Month 1**: [Specific actions and goals]
- **Month 2**: [Specific actions and goals]
- **Month 3**: [Specific actions and goals]

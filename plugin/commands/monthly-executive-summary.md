---
description: High-level monthly report designed for stakeholders. Focuses on business impact, ROI, key learnings, and strategic recommendations. (requires Pro subscription)
---

> **Platforms:** all
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Monthly Executive Summary

Generate an executive-level report for the previous month, ranked by ROAS.

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### EXECUTIVE DASHBOARD
| Metric | This Month | Last Month | Change | Target | Status |
|--------|------------|------------|--------|--------|--------|
| Total Ad Spend | | | | | |
| Attributed Revenue | | | | | |
| Blended ROAS | | | | | |
| Total Conversions | | | | | |
| Avg CPA | | | | | |

### CHANNEL PERFORMANCE
| Channel | Spend | ROAS | Conversions | % of Total | MoM Change | Verdict |
|---------|-------|------|-------------|------------|------------|---------|
| Meta | | | | | | |
| Google | | | | | | |
| LinkedIn | | | | | | |
| TikTok | | | | | | |

### TOP 5 CAMPAIGNS (by ROAS)
| # | Campaign | Platform | Spend | ROAS | Key Insight |
|---|----------|----------|-------|------|-------------|

### EXECUTIVE NARRATIVE
[2-3 paragraphs covering: overall performance vs goals, key wins with contributing factors, challenges and how addressed, strategic implications for next month]

### KEY LEARNINGS
1. [Learning with supporting data]
2. [Learning with supporting data]
3. [Learning with supporting data]

### NEXT MONTH PRIORITIES
| Priority | Expected Impact | Channel | Owner |
|----------|-----------------|---------|-------|

### BUDGET REALLOCATION
| Channel | This Month | Recommended | Change | Rationale |
|---------|------------|-------------|--------|-----------|

## EXECUTION STEPS

### Step 1: Discover All Accounts
- `meta_list_ad_accounts()`
- `google_ads_list_accounts()`
- `linkedin_list_ad_accounts()`
- `tiktok_get_advertiser_info()`
- `ga4_list_properties()`

### Step 2: Pull Monthly Data from Each Platform

**Meta:** `meta_get_insights(account_id="FROM_STEP_1", date_preset="last_month", level="account", fields=["spend","impressions","reach","frequency","clicks","actions","action_values","purchase_roas","cpm","cpc","ctr"])`

Then campaign-level for top 5: `meta_get_insights(account_id="FROM_STEP_1", date_preset="last_month", level="campaign", fields=["campaign_name","spend","actions","action_values","purchase_roas"])`

**Google Ads:** `google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT campaign.name, metrics.cost_micros, metrics.impressions, metrics.clicks, metrics.conversions, metrics.conversions_value, metrics.ctr, metrics.average_cpc FROM campaign WHERE segments.date DURING LAST_MONTH ORDER BY metrics.cost_micros DESC")`

**LinkedIn:** `linkedin_get_analytics(account_id="FROM_STEP_1", start_date="FIRST_OF_LAST_MONTH", end_date="LAST_OF_LAST_MONTH", fields=["impressions","clicks","costInLocalCurrency","externalWebsiteConversions"])`

**TikTok:** `tiktok_get_report(start_date="FIRST_OF_LAST_MONTH", end_date="LAST_OF_LAST_MONTH", level="campaign", metrics=["spend","impressions","clicks","conversions","cost_per_conversion"])`

**GA4 (cross-channel truth):** `ga4_run_report(property_id="FROM_STEP_1", start_date="FIRST_OF_LAST_MONTH", end_date="LAST_OF_LAST_MONTH", metrics=["totalRevenue","conversions","sessions"], dimensions=["sessionDefaultChannelGroup"])`

### Step 3: Pull Prior Month for MoM Comparison

Repeat Step 2 queries with the month before last month date ranges to calculate month-over-month changes.

### Step 4: Analyze

**Executive narrative guidance:**
- Lead with business impact, not raw metrics
- Frame changes in context: "Revenue grew 15% driven by Meta prospecting scaling"
- Acknowledge challenges honestly: "CPA rose 8% as we tested new audiences"
- End with clear forward-looking strategy

**Channel verdict rules:**
- ROAS > target + MoM improving = "Strong - Scale"
- ROAS > target + MoM declining = "Watch - Optimize"
- ROAS < target + MoM improving = "Recovering - Monitor"
- ROAS < target + MoM declining = "Underperforming - Review"

**Top campaigns:** Rank all campaigns across all platforms by ROAS, take top 5.

### Step 5: Present Results
Follow OUTPUT FORMAT above EXACTLY. Fill all tables with real data. Write executive narrative in a professional, stakeholder-friendly tone.

## EDGE CASES
- Partial month (mid-month run): Note "Partial month data (X of Y days)" and adjust projections accordingly
- Single platform connected: Generate report for that platform only, skip channel comparison table
- No targets set: Omit Target/Status columns, use MoM change as primary benchmark
- Platform API error: Note "[Platform] data unavailable" in channel table, continue with remaining platforms
- Zero conversions on a platform: Include it with "0" values, flag as potential tracking issue in narrative
- First month (no prior month): Skip MoM columns, note "First month of tracking - no comparison available"
---
description: Generate professional, client-ready weekly reports in one click. Automatically adapts tone and metrics based on client type (e-commerce, B2B lead gen, brand awareness). (requires Pro subscription)
disable-model-invocation: true
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Weekly Client Summary Generator

Generate a professional, client-ready summary for the past 7 days.
Client type: ecommerce | Tone: professional

## OUTPUT FORMAT (CRITICAL - follow this EXACT structure)

### EXECUTIVE SUMMARY
[2-3 sentences: overall performance, key win, focus area. Use professional tone. Be specific with numbers.]

### KEY METRICS
| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| [Primary KPI 1] | | | +/-% |
| [Primary KPI 2] | | | +/-% |
| [Primary KPI 3] | | | +/-% |
| Total Spend | | | +/-% |

**Primary KPIs by client type:**
- Ecommerce: Revenue, ROAS, Orders, AOV
- B2B Lead Gen: Leads, CPL, MQL Rate (if available)
- Brand Awareness: Reach, Impressions, Frequency, CPM

### PLATFORM BREAKDOWN
| Platform | Spend | Primary KPI | Secondary KPI | Trend |
|----------|-------|-------------|---------------|-------|

### HIGHLIGHTS
- [Specific win #1 with numbers]
- [Specific win #2 with numbers]
- [Specific win #3 with numbers]

### AREAS OF FOCUS
- [Area needing attention #1 - with context, not alarming]
- [Area needing attention #2 - with context, not alarming]

### RECOMMENDED NEXT STEPS
1. [Actionable recommendation #1]
2. [Actionable recommendation #2]
3. [Actionable recommendation #3]

### LOOKING AHEAD
[Brief note on planned activities, tests, or optimizations for next week]

## EXECUTION STEPS

### Step 1: Discover Accounts
- `meta_list_ad_accounts()`
- `google_ads_list_accounts()`
- `linkedin_list_ad_accounts()`
- `tiktok_get_advertiser_info()`

### Step 2: Pull This Week's Data (Last 7 Days)

**Meta:** `meta_get_insights(account_id="FROM_STEP_1", date_preset="last_7d", level="account", fields=["spend","impressions","reach","frequency","clicks","actions","action_values","cpm","cpc","ctr","purchase_roas"])`

**Google Ads:** `google_ads_run_gaql(customer_id="FROM_STEP_1", query="SELECT campaign.name, metrics.impressions, metrics.clicks, metrics.ctr, metrics.average_cpc, metrics.cost_micros, metrics.conversions, metrics.conversions_value FROM campaign WHERE segments.date DURING LAST_7_DAYS AND campaign.status = 'ENABLED' ORDER BY metrics.cost_micros DESC")`

**TikTok:** `tiktok_get_report(start_date="YYYY-MM-DD", end_date="YYYY-MM-DD", level="campaign", metrics=["spend","impressions","reach","clicks","conversions","conversion_rate"])`

**LinkedIn:** `linkedin_get_analytics(account_id="FROM_STEP_1", start_date="YYYY-MM-DD", end_date="YYYY-MM-DD", fields=["impressions","clicks","costInLocalCurrency","externalWebsiteConversions"])`

### Step 3: Pull Previous Week's Data (8-14 Days Ago)

Repeat Step 2 with date range shifted back 7 days for week-over-week comparison.

**Meta:** `meta_get_insights(account_id="FROM_STEP_1", date_preset="last_14d", level="account", fields=["spend","impressions","reach","clicks","actions","action_values","purchase_roas"])`
Then subtract this week from 14-day totals to derive prior week.

**Google Ads:** Same GAQL query but with explicit date filter: `WHERE segments.date BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD'`

**TikTok / LinkedIn:** Same calls with prior week date range.

### Step 4: Analyze & Present

Apply client type focus:
- **Ecommerce:** Lead with Revenue + ROAS. Highlight AOV trends, top-performing products/campaigns.
- **B2B Lead Gen:** Lead with Leads + CPL. Note lead quality signals, pipeline impact.
- **Brand Awareness:** Lead with Reach + CPM. Highlight frequency management, audience growth.

**Tone guidelines:**
- Professional: Formal language, third-person, data-focused. "Campaign performance exceeded targets by 15%."
- Casual: Conversational, first-person, enthusiastic wins. "Great week! We crushed it with a 15% ROAS boost."

Follow OUTPUT FORMAT above EXACTLY. Include all tables with real data.

## EDGE CASES
- No previous week data (new account): Show this week only, note "First week - no comparison available"
- Single platform connected: Run for that platform only, skip Platform Breakdown table
- Zero spend week: Flag as "Campaigns paused or no delivery" - investigate
- Missing conversion data: Note "Conversion tracking not detected" and focus on upper-funnel metrics
- Mixed currencies across platforms: Report each in its native currency, note the difference
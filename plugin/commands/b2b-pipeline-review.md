---
description: B2B lead pipeline review — CPL trends, lead quality scoring, and MQL-to-SQL conversion analysis across LinkedIn and Google Ads
---

# B2B Pipeline Review

Perform a B2B lead generation pipeline review focused on lead quality and cost efficiency.

## Step 1: Gather Lead Gen Data

**LinkedIn Ads:**
- `linkedin_list_ad_accounts` → `linkedin_get_analytics` for lead metrics
- `linkedin_query` for campaign-level lead form performance
- Key metrics: leads, CPL, lead form completion rate, cost per qualified lead

**Google Ads:**
- `google_ads_run_gaql` for lead gen campaigns:
  ```
  SELECT campaign.name, metrics.conversions, metrics.cost_per_conversion, metrics.conversions_value
  FROM campaign
  WHERE campaign.advertising_channel_type = 'SEARCH'
  AND segments.date DURING LAST_30_DAYS
  ```

**GA4:**
- `ga4_run_report` for website lead behavior: form submissions, demo requests, content downloads

## Step 2: Lead Volume & Cost Analysis

| Platform | Leads | CPL | Budget | Trend (vs prev period) |
|----------|-------|-----|--------|----------------------|
| LinkedIn | ... | ... | ... | ... |
| Google Ads Search | ... | ... | ... | ... |
| Google Ads Display | ... | ... | ... | ... |
| Total | ... | ... | ... | ... |

## Step 3: Lead Quality Assessment

If CRM data is available, analyze:
- **MQL → SQL conversion rate** (benchmark: 20-30%)
- **SQL → Opportunity rate** (benchmark: 40-60%)
- **Opportunity → Closed Won rate** (benchmark: 15-25%)
- **Average deal size** from ad-sourced leads
- **Cost per SQL** (the true efficiency metric)

If no CRM data, assess quality signals:
- Form completion rates (higher = lower friction but potentially lower quality)
- Time on site after lead submission
- Return visit rate of leads
- LinkedIn audience quality (seniority level, company size)

## Step 4: Platform Comparison

| Metric | LinkedIn | Google Ads | Benchmark |
|--------|----------|-----------|-----------|
| CPL | ... | ... | LinkedIn: €30-150, Google: €15-80 |
| Lead Quality | ... | ... | LinkedIn typically higher quality |
| Volume | ... | ... | Google typically higher volume |
| Best for | ... | ... | ... |

## Step 5: Pipeline Recommendations

1. **Budget reallocation**: Shift budget toward platform with better cost-per-SQL (not just CPL)
2. **Audience refinement**: Tighten targeting on high-CPL platforms
3. **Content strategy**: Which content types drive qualified leads?
4. **Form optimization**: Length vs quality tradeoff
5. **Nurture gaps**: Are leads being followed up quickly enough?

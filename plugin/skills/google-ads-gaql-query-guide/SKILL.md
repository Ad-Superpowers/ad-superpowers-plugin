---
name: gaql-query-guide
description: |
  Complete GAQL reference for Google Ads API v23. Use for: (1) Writing GAQL queries, (2) Metric and dimension selection, (3) Date range filtering, (4) v23 migration (video_views → video_trueview_views), (5) Common query patterns. Triggers: gaql, google ads query, metrics, report, video_views, LAST_90_DAYS.
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "google_ads"
  phase: "fase-1-foundation"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---
# GAQL Query Guide (API v23)

Complete reference for Google Ads Query Language. Updated for API v23 (released 2026-01-28).

## Quick Reference

```
BASIC QUERY STRUCTURE
═════════════════════

SELECT field1, field2, metrics.clicks, metrics.impressions
FROM resource_type
WHERE condition1 AND condition2
ORDER BY field [ASC|DESC]
LIMIT n
```

## API v23 Breaking Changes

### Video Metrics Renamed

```
v22 → v23 METRIC RENAMES (AUTO-MIGRATED)
════════════════════════════════════════

OLD (v22)                    →  NEW (v23)
─────────────────────────────────────────────────────────
metrics.video_views          →  metrics.video_trueview_views
metrics.video_view_rate      →  metrics.video_trueview_view_rate
metrics.average_cpv          →  metrics.trueview_average_cpv

NEW VIDEO METRICS IN v23:
─────────────────────────
• metrics.video_trueview_view_rate_in_feed
• metrics.video_trueview_view_rate_in_stream
• metrics.video_trueview_view_rate_shorts
```

**Our system auto-migrates v22 metric names to v23.**

### Removed Metrics in v23

```
REMOVED (NO LONGER AVAILABLE)
═════════════════════════════

Asset Performance Sample Metrics (removed):
• metrics.sample_best_performance_entities
• metrics.sample_good_performance_entities
• metrics.sample_low_performance_entities
• metrics.sample_learning_performance_entities
• metrics.sample_unrated_performance_entities

Asset Performance Percentage Metrics (removed):
• metrics.asset_best_performance_impression_percentage
• metrics.asset_good_performance_impression_percentage
• metrics.asset_low_performance_impression_percentage
• metrics.asset_learning_performance_impression_percentage
• metrics.asset_unrated_performance_impression_percentage
• metrics.asset_*_performance_cost_percentage
```

## Date Ranges

### Valid DURING Presets

```
VALID DATE PRESETS
══════════════════

TODAY             - Current day
YESTERDAY         - Previous day
LAST_7_DAYS       - Past 7 days
LAST_14_DAYS      - Past 14 days
LAST_30_DAYS      - Past 30 days
LAST_BUSINESS_WEEK - Mon-Fri of last week
LAST_WEEK_SUN_SAT - Sun-Sat of last week
LAST_WEEK_MON_SUN - Mon-Sun of last week
THIS_MONTH        - Current month to date
LAST_MONTH        - Previous month
THIS_QUARTER      - Current quarter
LAST_QUARTER      - Previous quarter
THIS_YEAR         - Current year to date
LAST_YEAR         - Previous year
```

### LAST_90_DAYS Workaround

```
⚠️  LAST_90_DAYS IS NOT A VALID PRESET!
════════════════════════════════════════

❌ WRONG:
WHERE segments.date DURING LAST_90_DAYS

✅ CORRECT (use BETWEEN):
WHERE segments.date BETWEEN '2024-11-04' AND '2025-02-01'
```

### BETWEEN Syntax

```sql
-- Explicit date range
WHERE segments.date BETWEEN '2024-01-01' AND '2024-12-31'

-- Combine with other conditions
WHERE campaign.status = 'ENABLED'
  AND segments.date BETWEEN '2024-10-01' AND '2024-12-31'
```

## Common Resource Types

```
RESOURCE TYPES & USE CASES
══════════════════════════

campaign              - Campaign-level data
ad_group              - Ad group data
ad_group_ad           - Ad-level data
keyword_view          - Keyword performance
search_term_view      - Search queries that triggered ads
asset_group           - Performance Max asset groups
asset_group_asset     - Assets within asset groups
customer              - Account-level metrics
geographic_view       - Location performance
gender_view           - Gender demographics
age_range_view        - Age demographics
video                 - Video campaign data
youtube_video_stat    - YouTube video statistics
```

## Core Metrics

### Traffic Metrics

```sql
SELECT
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.average_cpc,
  metrics.average_cpm,
  metrics.cost_micros
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
```

### Conversion Metrics

```sql
SELECT
  campaign.name,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_per_conversion,
  metrics.conversions_from_interactions_rate,
  metrics.value_per_conversion
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
```

### Video Metrics (v23)

```sql
-- YouTube/Video campaign performance
SELECT
  campaign.name,
  metrics.video_trueview_views,           -- Was: video_views
  metrics.video_trueview_view_rate,       -- Was: video_view_rate
  metrics.trueview_average_cpv,           -- Was: average_cpv
  metrics.video_quartile_p25_rate,
  metrics.video_quartile_p50_rate,
  metrics.video_quartile_p75_rate,
  metrics.video_quartile_p100_rate
FROM campaign
WHERE campaign.advertising_channel_type = 'VIDEO'
  AND segments.date DURING LAST_30_DAYS
```

## Common Query Patterns

### Campaign Performance Report

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

### Search Terms Report

```sql
SELECT
  search_term_view.search_term,
  campaign.name,
  ad_group.name,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.conversions,
  metrics.cost_micros
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.impressions > 10
ORDER BY metrics.impressions DESC
LIMIT 100
```

### Keyword Performance

```sql
SELECT
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  ad_group.name,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.average_cpc,
  metrics.conversions,
  metrics.quality_score
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
ORDER BY metrics.impressions DESC
```

### Performance Max Asset Groups

```sql
SELECT
  asset_group.id,
  asset_group.name,
  asset_group.status,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.cost_micros
FROM asset_group
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.advertising_channel_type = 'PERFORMANCE_MAX'
```

### Geographic Performance

```sql
SELECT
  geographic_view.country_criterion_id,
  geographic_view.location_type,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.cost_micros
FROM geographic_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

## Field Compatibility

### Metrics Requiring Date Segments

```
METRICS THAT NEED DATE FILTERING
════════════════════════════════

Most metrics require date segmentation for accurate data:
• metrics.impressions
• metrics.clicks
• metrics.cost_micros
• metrics.conversions
• metrics.conversions_value

Always include: WHERE segments.date DURING {preset}
or: WHERE segments.date BETWEEN '{start}' AND '{end}'
```

### Incompatible Field Combinations

```
FIELD COMPATIBILITY RULES
═════════════════════════

1. Can't mix campaign-level and ad-level fields in same query
2. Can't use video metrics on non-video campaigns
3. search_term_view only works with Search campaigns
4. asset_group only works with Performance Max campaigns
5. Some segments can't be combined:
   - segments.hour with segments.day_of_week
   - segments.device with segments.slot
```

## Error Handling

### Common Errors & Fixes

```
ERROR: "Unrecognized field: metrics.video_views"
FIX: Use metrics.video_trueview_views (v23 rename)

ERROR: "Invalid date preset: LAST_90_DAYS"
FIX: Use BETWEEN with explicit dates

ERROR: "Field is not compatible"
FIX: Check field compatibility rules above

ERROR: "Customer not found"
FIX: Verify customer_id format (10 digits, no dashes)

ERROR: "Access denied"
FIX: Check manager_id for sub-accounts
```

## Tips & Best Practices

```
GAQL BEST PRACTICES
═══════════════════

1. Always include date filtering for metrics
2. Use LIMIT to avoid large result sets
3. Filter by status = 'ENABLED' for active items
4. All queries go through google_ads_run_gaql — use the recipes
   in the tool's docstring for common patterns (campaign performance,
   keyword performance, image assets, responsive display ads)
5. For any custom report, use google_ads_run_gaql
6. Cost is in micros: divide by 1,000,000 for actual currency
7. Rates are decimals: multiply by 100 for percentage
```

## Quick Copy-Paste Templates

### Basic Campaign Report
```sql
SELECT campaign.id, campaign.name, campaign.status, metrics.impressions, metrics.clicks, metrics.conversions, metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_30_DAYS AND campaign.status = 'ENABLED' ORDER BY metrics.cost_micros DESC
```

### Search Terms (Last 7 Days)
```sql
SELECT search_term_view.search_term, metrics.impressions, metrics.clicks, metrics.conversions, metrics.cost_micros FROM search_term_view WHERE segments.date DURING LAST_7_DAYS AND metrics.impressions > 5 ORDER BY metrics.clicks DESC LIMIT 100
```

### Video Campaign (v23)
```sql
SELECT campaign.name, metrics.video_trueview_views, metrics.video_trueview_view_rate, metrics.trueview_average_cpv, metrics.cost_micros FROM campaign WHERE campaign.advertising_channel_type = 'VIDEO' AND segments.date DURING LAST_30_DAYS
```

### 90-Day Report (BETWEEN)
```sql
SELECT campaign.name, metrics.impressions, metrics.clicks, metrics.conversions FROM campaign WHERE segments.date BETWEEN '2024-11-04' AND '2025-02-01' ORDER BY metrics.impressions DESC
```

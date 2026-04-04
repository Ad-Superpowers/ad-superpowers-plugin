---
description: E-commerce performance health check — ROAS by product/category, funnel conversion rates, and shopping feed status
---

# E-Commerce Health Check

Perform a comprehensive e-commerce advertising health check across connected platforms.

## Step 1: Gather E-Commerce Data

Pull performance data with e-commerce focus:

**Meta Ads:**
- `meta_get_insights` with breakdowns by campaign and ad set for ROAS, purchase value, cost per purchase
- `meta_get_creatives` to check product ad creative health

**Google Ads:**
- `google_ads_run_gaql` — Shopping campaign performance:
  ```
  SELECT campaign.name, metrics.conversions, metrics.conversions_value, metrics.cost_micros, metrics.all_conversions_from_interactions_rate
  FROM shopping_performance_view
  WHERE segments.date DURING LAST_30_DAYS
  ```
- Search campaign ROAS by product/service keywords

**GA4:**
- `ga4_run_report` — E-commerce funnel metrics:
  - Sessions → Product views → Add to cart → Begin checkout → Purchase
  - Conversion rate per step
  - Revenue by traffic source

**TikTok (if connected):**
- `tiktok_get_report` for product ad performance

## Step 2: Funnel Analysis

Calculate and present:

| Funnel Stage | Sessions | Rate | Benchmark | Status |
|-------------|----------|------|-----------|--------|
| Product View | ... | ... | ... | ... |
| Add to Cart | ... | ... | 8-12% | ... |
| Begin Checkout | ... | ... | 40-60% of carts | ... |
| Purchase | ... | ... | 2-4% overall | ... |

## Step 3: ROAS Analysis

| Platform | Spend | Revenue | ROAS | Target | Status |
|----------|-------|---------|------|--------|--------|
| Meta (Prospecting) | ... | ... | ... | >2x | ... |
| Meta (Retargeting) | ... | ... | ... | >5x | ... |
| Google Shopping | ... | ... | ... | >3x | ... |
| Google Search | ... | ... | ... | >4x | ... |

## Step 4: Identify Issues & Opportunities

Flag:
- Products/categories with negative ROAS
- Funnel drop-off points above benchmark
- Creative fatigue on product ads
- Budget allocation inefficiencies
- Retargeting window gaps

## Step 5: Recommendations

Provide prioritized actions:
1. **Quick wins** (implement this week)
2. **Medium-term** (next 2 weeks)
3. **Strategic** (next month)

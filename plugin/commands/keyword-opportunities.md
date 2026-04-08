---
name: keyword-opportunities
description: Compare organic keywords (GSC) with paid keywords (Google Ads) to find savings and content gaps
user_invocable: true
tier: pro
platforms: [gsc, google_ads]
disable-model-invocation: true
---

# Keyword Opportunities — SEO vs SEA Gap Analysis

Compare organic keywords from Google Search Console with paid keywords from Google Ads to find cannibalization savings and content opportunities.

## Requirements
- Google Search Console connection
- Google Ads connection

## Instructions

1. **Pull organic data** — Use `gsc_search_analytics(dimensions=["query"], days=28, row_limit=5000)` to get organic keyword performance.

2. **Pull paid data** — Use `google_ads_run_gaql` to query keyword_view with clicks, impressions, CPC, cost, and conversions for the last 30 days.

3. **Match keywords** — Cross-reference organic and paid keyword lists to find overlaps.

4. **Classify into four quadrants:**

   | Quadrant | Organic Position | Paid Status | Action |
   |----------|-----------------|-------------|--------|
   | Q1: Cannibalization | ≤ 5 | Active + spending | Test pausing ads → potential savings |
   | Q2: Paid-Only | > 10 or absent | Active + spending | Create content to reduce CPC dependency |
   | Q3: Organic Winners | ≤ 5 | Not bidding | No ads needed — free traffic |
   | Q4: Blind Spots | > 10 or absent | Not bidding | Evaluate: worth SEO or SEA investment? |

5. **Calculate savings** for Q1 keywords where organic position ≤ 3, CTR > 20%, and not a competitor branded term.

6. **Prioritize content opportunities** for Q2 keywords by (conversions × CPC) score.

## Output Format

Present as a gap analysis report with:
- Executive summary (total overlap %, potential monthly savings)
- Quadrant breakdown table with counts and monthly spend
- Top 10 cannibalized keywords with organic position, CTR, and monthly ad cost
- Top 10 content opportunities with CPC, conversions, and content ROI estimate
- Industry benchmark comparison (expected overlap rates by vertical)

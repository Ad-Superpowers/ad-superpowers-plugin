---
description: Comprehensive organic search health check using Google Search Console data
disable-model-invocation: true
---

# SEO Health Check

Perform a comprehensive organic search health check using Google Search Console data.

## Instructions

1. **Discover properties** — Use `gsc_list_sites(include_sitemaps=true)` to find connected GSC properties and their sitemaps.

2. **Pull search performance** — Use `gsc_search_analytics` with dimensions=["query"] for the last 28 days to get top keywords, clicks, impressions, CTR, and average position.

3. **Analyze by page** — Run `gsc_search_analytics` with dimensions=["page"] to identify top and bottom performing pages.

4. **Check indexing health** — For the top 5 most important pages, use `gsc_manage_url(action="inspect")` to verify indexing status.

5. **Identify opportunities:**
   - **Quick wins:** Keywords in positions 4-10 with high impressions (within striking distance of page 1 top 3)
   - **Declining keywords:** Compare last 7 days vs previous 7 days — flag any keyword with >20% CTR drop
   - **CTR optimization:** Pages ranking positions 1-3 but with CTR below expected benchmarks

6. **CTR benchmarks by position:**

   | Position | Expected CTR |
   |----------|-------------|
   | 1 | 25-35% |
   | 2 | 12-18% |
   | 3 | 8-12% |
   | 4-5 | 5-8% |
   | 6-10 | 2-5% |

## Output Format

Present as an SEO health scorecard:
- Property overview (total clicks, impressions, avg CTR, avg position)
- Top 10 keywords with trends
- Quick wins table (striking distance keywords)
- Indexing status summary
- Prioritized action items

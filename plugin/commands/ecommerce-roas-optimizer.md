---
description: Deep-dive analysis for e-commerce businesses with Shopify integration. Analyze product-level ROAS, identify winners/losers, and get inventory-aware recommendations. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, shopify, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# E-commerce ROAS Optimizer

Deep analysis of e-commerce advertising performance with Shopify integration.

## Industry Benchmarks
| Category | Typical ROAS | Source |
|----------|--------------|--------|
| Apparel | ~4.5x | Industry Data |
| Garden/Outdoor | ~6.7x | Industry Data |
| Electronics | ~3.2x | Industry Data |
| Beauty | ~5.1x | Industry Data |

## Instructions

### 1. Gather E-commerce Data
From advertising platforms:
- Campaign/ad performance by product category
- ROAS, CPA, conversion value

From Shopify (if connected):
- Product-level sales data
- Inventory levels
- Profit margins (if available)

### 2. Analyze Product Performance

```
Product ROAS = Revenue from Ads / Ad Spend on Product

Efficiency Score = ROAS * (Inventory Level Factor) * (Margin Factor)
```

### 3. Output Format

```
================================================================================
                         E-COMMERCE ROAS OPTIMIZER
                    Period: Last 30 Days
================================================================================

REVENUE OVERVIEW:
-----------------
| Metric          | Value       | vs Last Period | vs Target    |
|-----------------|-------------|----------------|--------------|
| Ad Revenue      | €XX,XXX     | +/-XX%         | +/-XX%       |
| Ad Spend        | €XX,XXX     | +/-XX%         | On/Under/Over|
| Blended ROAS    | X.XXx       | +/-XX%         | +/-XX%       |
| Orders from Ads | XXX         | +/-XX%         | -            |
| AOV             | €XXX.XX     | +/-XX%         | -            |

TOP PERFORMING PRODUCTS:
------------------------
| Product              | Revenue  | ROAS   | Orders | Stock  | Action       |
|----------------------|----------|--------|--------|--------|--------------|
| [Best Product]       | €X,XXX   | X.XXx  | XX     | High   | Scale budget |
| [Product 2]          | €X,XXX   | X.XXx  | XX     | Med    | Maintain     |
| [Product 3]          | €X,XXX   | X.XXx  | XX     | Low    | Restock!     |

UNDERPERFORMING PRODUCTS:
-------------------------
| Product              | Spend   | ROAS   | Issue          | Recommendation |
|----------------------|---------|--------|----------------|----------------|
| [Product X]          | €XXX    | 0.8x   | Below target   | Pause/Review   |
| [Product Y]          | €XXX    | 1.2x   | High CPA       | Optimize bids  |

CATALOG CAMPAIGN ANALYSIS:
--------------------------
Meta Advantage+ Shopping:
- ROAS: X.XXx | Spend: €X,XXX | Top products: [list]

Google Shopping/PMax:
- ROAS: X.XXx | Spend: €X,XXX | Top products: [list]

INVENTORY-AWARE RECOMMENDATIONS:
--------------------------------
1. SCALE: [Products with high ROAS + good inventory]
2. PAUSE: [Products with low ROAS or out of stock]
3. RESTOCK ALERT: [High performers running low]

OPTIMIZATION OPPORTUNITIES:
---------------------------
- Product feed improvements: [specific suggestions]
- Budget reallocation: [from X to Y]
- New products to test: [based on category performance]

BENCHMARKS VS YOUR PERFORMANCE:
-------------------------------
Your category ([Category]): Target ROAS [X.Xx]
Your actual: [X.Xx]
Status: [Above/Below] benchmark by XX%
```
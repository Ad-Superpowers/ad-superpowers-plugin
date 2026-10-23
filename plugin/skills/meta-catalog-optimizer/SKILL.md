---
name: meta-catalog-optimizer
description: "This skill should be used when the user asks to \"optimize product catalog\", \"improve catalog ad performance\", \"fix catalog feed issues\", or mentions \"Advantage+ Catalog Ads\", \"product set strategy\", or \"catalog feed optimization\". Do NOT use for: campaign structure (use campaign-structure-advisor), creative diversification (use creative-diversification-generator), full-funnel design (use full-funnel-designer)."
---
# Catalog Optimizer

## Overview

This skill helps optimize Meta product catalogs for Advantage+ catalog ads and Advantage+ sales campaigns, including feed optimization, product set strategies, and troubleshooting of common issues.

> **Heads-up: catalog data is not reachable through MCP yet.** This release ships no catalog tool, so catalogs, product sets, and product-set items can be neither read nor created through Ad Superpowers. Use this skill for feed and product-set **strategy and diagnosis**, and inspect catalogs in Commerce Manager. With a product set ID from Commerce Manager, the catalog ad itself can still be created through MCP: an ad set whose `promoted_object` binds that product set, then `meta_create_ad(product_set_id=...)`. For the full ad creation sequence, `use ad-launch-playbook`.

## Catalog Fundamentals

### Catalog Ecosystem

```
┌─────────────────────────────────────────────────────────────────┐
│  META CATALOG STRUCTURE                                         │
│                                                                 │
│  DATA FEED (your source)                                        │
│  ├── Shopify, WooCommerce, Magento feed                         │
│  ├── Google Merchant Center feed                                │
│  └── Custom CSV/XML feed                                        │
│         │                                                       │
│         v                                                       │
│  PRODUCT CATALOG (Meta)                                         │
│  ├── All products from feed                                     │
│  ├── Product sets (filtered subsets)                            │
│  └── Catalog settings                                           │
│         │                                                       │
│         v                                                       │
│  AD TYPES                                                       │
│  ├── Advantage+ Catalog Ads (formerly dynamic ads)              │
│  ├── Advantage+ Sales Campaigns                                 │
│  └── Collection Ads with catalog                                │
└─────────────────────────────────────────────────────────────────┘
```

**Naming:** Meta now calls Advantage+ catalog ads "Products from your catalog" in sales campaigns. You select the catalog under Product data at the campaign level, then choose Products from your catalog as the creative source at the ad level ("Meta Advantage+ Catalog Ads", Meta for Business, https://www.facebook.com/business/ads/meta-advantage-plus/catalog-ads). Help Center articles, and this skill, still say Advantage+ catalog ads.

## Feed Optimization

### Required Fields

```
REQUIRED FIELDS
===============

Field           │ Description               │ Best Practice
────────────────┼───────────────────────────┼────────────────────
id              │ Unique product ID         │ Consistent with pixel
title           │ Product name              │ Keywords first
description     │ Product description       │ Plain text, 30-9,999 chars
availability    │ in stock / out of stock   │ Real-time sync
condition       │ new / refurbished / used  │ Accurate
price           │ Price with currency       │ Format: "29.99 USD"
link            │ Product URL               │ Deep link to PDP
image_link      │ Main image URL            │ Min 500x500px
brand           │ Brand name                │ Consistent spelling
```

Source for the required fields and their limits: "Product data specifications for catalogs in Commerce Manager", Meta Business Help Center. Meta's feed troubleshooting guide asks for at least one of brand, gtin or mpn per product ("Troubleshoot data feed errors in your catalog").

### Recommended Fields (High Impact)

```
RECOMMENDED FIELDS
==================

Field               │ Impact │ Use
────────────────────┼────────┼────────────────────────────
additional_image_link│ High   │ Up to 20; 4+ images for slideshow/shops
sale_price          │ High   │ Strikethrough pricing
product_type        │ High   │ Categorization for sets
google_product_category│Med  │ Better matching
internal_label      │ High   │ Segmentation (see below)
color               │ Medium │ Filter option
size                │ Medium │ Filter option
gender              │ Medium │ Filter option
age_group           │ Medium │ Filter option
shipping            │ Low    │ Free shipping highlight
```

Rules of thumb, not Meta figures: check them against the account's own history. That covers the Impact column; the field facts are Meta's: up to 20 additional images (`additional_image_link`; "Product data specifications for catalogs"), and 4 or more images recommended for carousel slideshows and shops ("Product image specifications for catalogs"); `shipping` with a price of 0.0 enables the Free shipping overlay, and `sale_price` feeds the Strikethrough price and Percentage off overlays ("Add dynamic overlays in Advantage+ catalog ads").

### Custom Labels Strategy

```
CUSTOM LABEL BEST PRACTICES
===========================

For product set filters, Meta recommends internal_label over
custom_label_0 to custom_label_4: internal labels can change without
a policy review. Custom labels hold text for the ad creative. Feeds that
already use custom_label_0 to custom_label_4 for filters can keep them: the
scheme below works with either field.

RECOMMENDED SETUP (internal_label values, one from each group):

MARGIN
├── "high_margin" (>40% margin)
├── "medium_margin" (20-40%)
└── "low_margin" (<20%)

BESTSELLER STATUS
├── "bestseller" (top 20% sales)
├── "regular"
└── "slow_mover" (bottom 20%)

PRICE RANGE
├── "budget" (<$25)
├── "mid_range" ($25-75)
├── "premium" ($75-150)
└── "luxury" (>$150)

SEASONAL
├── "evergreen"
├── "summer"
├── "winter"
└── "holiday"

INVENTORY STATUS
├── "plenty" (>50 units)
├── "limited" (10-50)
└── "almost_gone" (<10)
```

Rules of thumb, not Meta figures: check them against the account's own history. That covers the cut-offs above. Sources for internal_label: "Product data specifications for catalogs in Commerce Manager" and "Tips for creating and managing product sets in your catalog".

## Title & Description Optimization

### Title Best Practices

```
TITLE OPTIMIZATION
==================

FORMAT: [Brand] + [Product Type] + [Key Feature] + [Variant]

EXAMPLES:
Bad: "Nice dress"
Good: "Zara Maxi Dress Floral Print Blue Size M"

Bad: "iPhone case"
Good: "Apple iPhone 15 Pro Silicone Case Midnight Black"

RULES:
├── Max 150 characters per the Help Center (the catalog API reference allows 200);
│   Meta recommends under 65 so titles are not cut off
├── Most important keywords first
├── No ALL CAPS
├── No promotional text ("SALE", "BEST DEAL")
└── Include variant info (size, color)
```

Source: "Product title specifications for catalogs", Meta Business Help Center. It also asks for no keyword stuffing.

### Description Best Practices

```
DESCRIPTION OPTIMIZATION
========================

STRUCTURE:
1. Opening with key benefit
2. Product features (plain text only, no HTML: use clear sentences)
3. Specifications (material, dimensions)
4. Use case / scenario

EXAMPLE:
"Stylish maxi dress with floral print, perfect for summer days.
Made from breathable viscose for optimal wearing comfort. The
dress features a flattering A-line silhouette and adjustable
shoulder straps. Suitable for casual outings and beach vacations."

LENGTH: 30-9,999 characters (Meta's limits), longer than the title
```

Source: "Product description specifications for catalogs", Meta Business Help Center.

## Product Set Strategies

### High-Performance Product Sets

```
PRODUCT SET TYPES
=================

SET 1: BESTSELLERS
├── Filter: internal_label contains "bestseller"
├── Use: Prospecting campaigns
└── Why: Proven performers

SET 2: HIGH MARGIN
├── Filter: internal_label contains "high_margin"
├── Use: ROAS-focused campaigns
└── Why: More profit per sale

SET 3: SALE ITEMS
├── Filter: sale_price is greater than 0
├── Use: Retargeting, promotions
└── Why: Urgency

SET 4: NEW ARRIVALS
├── Filter: internal_label contains "new_arrival" (your feed sets it
│   for products added in the last [30] days)
├── Use: Email subscribers, loyal customers
└── Why: Novelty, FOMO

SET 5: PRICE BASED
├── Filter: price > $50 AND price < $100
├── Use: Segmented audiences
└── Why: Match with target audience purchasing power

SET 6: CATEGORY SPECIFIC
├── Filter: product_type contains "Dresses"
├── Use: Interest-based targeting
└── Why: Relevance for specific interest
```

### Dynamic Product Set Logic

```
ADVANCED FILTERS
================

COMBINATION FILTERS (match All filters = AND, At least one filter = OR):
├── Bestseller + High Margin
│   └── internal_label contains "bestseller" AND
│       internal_label contains "high_margin"
│
├── Premium products for High-Value audiences
│   └── internal_label contains "premium" OR
│       internal_label contains "luxury"
│
└── Urgency set (almost sold out)
    └── internal_label contains "almost_gone"

Out-of-stock products are already left out of ads, so a filter on
availability = "in stock" is not needed.
```

Source: "Tips for creating and managing product sets in your catalog", Meta Business Help Center, for the filter options, the sale price filter and out-of-stock products. Meta also advises against very narrow filters, which limit product recommendations.

## Advantage+ Catalog Ads Campaign Structure

Rules of thumb, not Meta figures: check them against the account's own history. That covers the audience windows and budget splits below.

### Retargeting Setup

```
ADVANTAGE+ CATALOG ADS RETARGETING STRUCTURE
=============================================

CAMPAIGN: [Brand]_CatalogAds_Retargeting
├── Objective: Sales
├── Optimization: Purchase
└── Catalog: [Your Catalog]

AD SET 1: Viewed Not Purchased (3d)
├── Audience: ViewContent 3d, exclude Purchase 7d
├── Product Set: All products
├── Budget: 40% of catalog ads budget
└── Expected ROAS: [from this account's own history]

AD SET 2: Add to Cart (7d)
├── Audience: AddToCart 7d, exclude Purchase 7d
├── Product Set: All products
├── Budget: 35% of catalog ads budget
└── Expected ROAS: [from this account's own history]

AD SET 3: Past Purchasers - Cross-sell (30d)
├── Audience: Purchase 30d
├── Product Set: Complementary products
├── Budget: 25% of catalog ads budget
└── Expected ROAS: [from this account's own history]
```

### Prospecting Setup

```
ADVANTAGE+ CATALOG ADS PROSPECTING STRUCTURE
=============================================

CAMPAIGN: [Brand]_CatalogAds_Prospecting
├── Objective: Sales
├── Optimization: Purchase
└── Catalog: [Your Catalog]

AD SET 1: Broad Prospecting
├── Audience: Broad (demographics + geo only)
├── Product Set: Bestsellers only
├── Budget: 50% of prospecting budget
└── Expected ROAS: [from this account's own history]

AD SET 2: Interest-Based
├── Audience: Relevant interests
├── Product Set: Category specific
├── Budget: 30% of prospecting budget
└── Expected ROAS: [from this account's own history]

AD SET 3: Lookalike Purchasers
├── Audience: LAL 1-3% purchasers
├── Product Set: High margin products
├── Budget: 20% of prospecting budget
└── Expected ROAS: [from this account's own history]
```

## Advantage+ Sales Campaigns

### Advantage+ Sales Campaign Optimization

Rules of thumb, not Meta figures: check them against the account's own history. That covers the volumes, budget and timing below; the product names and levers are Meta's (sources under the block).

```
ADVANTAGE+ SALES CAMPAIGN SETUP
================================
(Meta renamed Advantage+ shopping campaigns to Advantage+ sales campaigns.
Since Marketing API v24.0 (8 October 2025), and in all API versions since
19 May 2026, Advantage+ shopping campaigns can't be created, duplicated or updated.)

WHEN TO USE:
├── E-commerce with 50+ conversions/week
├── Catalog with 20+ products
├── Willing to give up control
└── Focus on volume + efficiency

SETUP:
├── Objective: Sales, with Advantage+ on for budget, audience and placements
├── Catalog: Full catalog (or bestseller set), under Product data
├── Budget: at least [target CPA x 50 / 7] per day, so about 50 results
│   a week is possible
├── Existing customers: the existing customer budget cap is no longer
│   available. To limit spend on them, use a campaign budget with one
│   ad set for existing customers that has an ad set spending limit,
│   and a second ad set that excludes them (Meta's method limits the
│   first ad set to that audience with Use as a suggestion unchecked,
│   which usually turns Advantage+ off for audience on that ad set)
└── Countries: Focus markets

CREATIVE INPUT:
├── Distinct creative concepts, not cosmetic variants of one ad
├── Mix: lifestyle images, product images, video (Reels-format 9:16)
├── Strong hooks in the first 3 seconds of video
└── Headlines & primary text variations

AUTOMATION LEVERS (Advantage+ stays on when all three are on):
├── Budget automation: Advantage+ campaign budget (shown as Campaign budget)
├── Audience automation: Advantage+ audience (your audience settings act
│   as suggestions)
└── Placement automation: Advantage+ placements (the Threads feed is one
    of the placements)

OPTIMIZATION TIPS:
├── Give campaign at least 7 days without changes
├── Review "Audience segments" for insights
├── Limit spend on existing customers with an ad set spending limit, if needed
└── Combine with separate retargeting if needed
```

Sources: "Meta Advantage+ Shopping Campaigns" (Meta for Business, https://www.facebook.com/business/ads/meta-advantage/advantage-plus-shopping-ads) for the rename; Marketing API v25.0 changelog, 18 Feb 2026; "How to replicate existing customer budget cap"; "What turns Advantage+ on and Advantage+ off"; "About Advantage+ campaign budget"; "Extend Meta Campaigns With Ads in Threads" (https://www.facebook.com/business/ads/threads).

## Catalog Troubleshooting

### Common Problems

```
TROUBLESHOOTING GUIDE
=====================

PROBLEM: Products not approved
├── Check: Policy violations (alcohol, adult, etc.)
├── Check: Missing required fields
├── Check: Image quality issues
└── Fix: Commerce Manager > Catalog > Products, filtered by Issues

PROBLEM: Feed sync errors
├── Check: Feed URL accessible?
├── Check: XML/CSV format correct?
├── Check: Encoding issues (UTF-8)?
└── Fix: Commerce Manager > Catalog > Data sources: open the feed and
    download its issue report

PROBLEM: Low delivery in Catalog Ads
├── Check: Product set too small? (Meta's minimum: 2 unique, valid
│   products for carousel, 4 for collection; variants count once)
├── Check: Audience too narrow?
├── Check: All products in stock?
└── Fix: Expand product set, broaden audience

PROBLEM: Wrong products shown
├── Check: Product matching correct?
├── Check: Content IDs in pixel = feed IDs?
├── Check: Pixel events firing correctly?
└── Fix: Verify the content_ids mapping (the parameter is content_ids,
    with an s, even for one product)

PROBLEM: High CPA in Catalog Ads
├── Check: Product set quality
├── Check: Catalog completeness
├── Check: Image quality
└── Fix: Focus on bestsellers, optimize feed
```

Sources: "Troubleshoot products not showing in your ads, shop or product tags on Facebook and Instagram", "Troubleshoot data feed errors in your catalog", "Troubleshoot not enough products in product set or product set is empty in Meta Ads Manager" and "Troubleshoot catalog match rate issues", all Meta Business Help Center.

### Catalog Health Checklist

```
CATALOG AUDIT CHECKLIST
=======================

□ FEED QUALITY
├── All required fields present?
├── Titles optimized (keywords first)?
├── Descriptions plain text, 30+ characters and longer than the title?
├── Images high quality (500x500+)?
└── Prices correct and up-to-date?

□ SYNC STATUS
├── Last upload on schedule (hourly, daily or weekly)?
├── No feed errors?
├── Update schedule configured?
└── Out of stock items correct?

□ PRODUCT SETS
├── Each set has enough unique, valid products (2+ carousel, 4+ collection)?
├── Bestseller set present?
├── High margin set present?
├── Sets regularly updated?
└── No empty sets?

□ PIXEL MATCHING
├── Content IDs match feed IDs?
├── Catalog match rate 90% or higher (Meta's recommendation)?
├── ViewContent, AddToCart, Purchase events OK?
├── Microdata and pixel checked (Meta Ads Data Advisor, formerly
│   Meta Pixel Helper)?
└── Deduplication correct?

□ PERFORMANCE REVIEW
├── CTR per product set monitored?
├── Low performers identified?
├── Best performers scaled?
└── Regular feed optimization?
```

Sources: "About scheduled data feed uploads for catalogs" for the schedule options, "Troubleshoot catalog match rate issues" for the 90% match rate, and "Meta Ads Data Advisor" (Meta for Developers).

## MCP Tool Integration

### Diagnosing Catalog Ad Performance with Live Data

```
1. Catalog health and diagnostics: not available through MCP; in Commerce Manager, check
   Catalog > Products (filtered by Issues) and Data sources (issue report per feed).

2. Check catalog campaign ROAS and delivery:
→ meta_get_insights(account_id="...", fields=["spend","purchase_roas","cost_per_action_type","impressions","frequency"], date_preset="last_14d", level="campaign")

3. Ad set level — check audience segments:
→ meta_get_insights(account_id="...", fields=["spend","purchase_roas","cost_per_action_type","reach","frequency"], date_preset="last_14d", level="adset")

4. Creative performance of one catalog campaign (scope="account" ranks ads
   across the whole account, not only catalog ads):
→ meta_get_creatives(account_id="...", scope="campaign", campaign_id="...")
```

`meta_get_insights` returns one page: while a response has `paging.next`, fetch the next page with `meta_query(account_id, "adsets", pagination_url=<paging.next>)` and add its rows.

Use the results to see which campaigns, ad sets (product sets, audience windows) and creatives pull ROAS down; feed issues show only in Commerce Manager.

## Example Interaction

**User**: "My Advantage+ Catalog Ads are performing poorly. The ROAS is only 1.5x while I expected 3x. What can I do?"

**Claude response**:

"Let's systematically troubleshoot your Catalog Ads performance:

---

**DIAGNOSTIC QUESTIONS:**

1. **Feed Quality:**
   - How many products are in your catalog?
   - Do you have internal labels (or custom labels) set up?
   - Are titles optimized?

2. **Campaign Setup:**
   - Retargeting or prospecting catalog ads?
   - Which product sets are you using?
   - What is your audience window?

3. **Creative:**
   - Are you using catalog-only or custom creative overlay?
   - Are product images high-quality?

---

**QUICK CHECKS (do now):**

1. **Catalog diagnostics** (Commerce Manager: Catalog > Products, filtered by Issues; not available through MCP):
   - Are there warnings/errors?
   - % approved products?

2. **Events Manager → Test events** (in Events Manager only; not available through MCP)
   - Are ViewContent/ATC/Purchase firing correctly?
   - Do content_ids match the feed? (meta_query(account_id, "pixel_da_checks", entity_id=<pixel_id>) reports Meta's match check)

3. **Ad performance data** (use `meta_get_insights` with `level="adset"`):
   - Check frequency and delivery metrics
   - Identify underperforming ad sets

---

**THINGS TO TEST (measure the ROAS effect in this account):**

1. **Product Set Focus**
   ```
   Create a "Top Performers" set:
   - Filter: Bestsellers + High Margin (out-of-stock products are
     already left out of ads)
   - Test this separately from full catalog
   ```

2. **Audience Narrowing**
   ```
   Retargeting: Shorten window from 30d → 14d
   More recent = higher intent
   ```

3. **Creative Overlay**
   ```
   Turn on dynamic overlays: Free shipping (needs a shipping price
   of 0.0 in the feed), Strikethrough price or Percentage off (need
   sale_price). They show on Facebook Feed only. Keep this text out
   of the product images themselves.
   ```

Share your specific setup and I'll give more targeted recommendations!"

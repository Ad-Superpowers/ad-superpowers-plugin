---
name: catalog-optimizer
description: Optimaliseer Meta Product Catalogs voor betere DPA (Dynamic Product Ads) performance met feed optimalisatie, product set strategieën en troubleshooting. Gebruik deze skill wanneer je werkt met catalogi, DPA's of Advantage+ Shopping.
---

# Catalog Optimizer

## Overview

Deze skill helpt bij het optimaliseren van Meta Product Catalogs voor maximale DPA en Advantage+ Shopping performance, inclusief feed optimalisatie, product set strategieën en troubleshooting van veelvoorkomende problemen.

## Catalog Fundamentals

### Catalog Ecosysteem

```
┌─────────────────────────────────────────────────────────────────┐
│  META CATALOG STRUCTUUR                                         │
│                                                                 │
│  DATA FEED (jouw bron)                                          │
│  ├── Shopify, WooCommerce, Magento feed                         │
│  ├── Google Merchant Center feed                                │
│  └── Custom CSV/XML feed                                        │
│         │                                                       │
│         ▼                                                       │
│  PRODUCT CATALOG (Meta)                                         │
│  ├── Alle producten uit feed                                    │
│  ├── Product sets (filtered subsets)                            │
│  └── Cataloog instellingen                                      │
│         │                                                       │
│         ▼                                                       │
│  AD TYPES                                                       │
│  ├── Dynamic Product Ads (DPA)                                  │
│  ├── Advantage+ Catalog Ads                                     │
│  ├── Advantage+ Shopping Campaigns                              │
│  └── Collection Ads met catalog                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Feed Optimization

### Verplichte Velden

```
REQUIRED FIELDS
===============

Field           │ Beschrijving              │ Best Practice
────────────────┼───────────────────────────┼────────────────────
id              │ Unieke product ID         │ Consistent met pixel
title           │ Productnaam               │ Keywords vooraan
description     │ Productomschrijving       │ 150-300 woorden
availability    │ in stock / out of stock   │ Real-time sync
condition       │ new / refurbished / used  │ Accurate
price           │ Prijs met valuta          │ Format: "29.99 EUR"
link            │ Product URL               │ Deep link naar PDP
image_link      │ Hoofdafbeelding URL       │ Min 500x500px
brand           │ Merknaam                  │ Consistent spelling
```

### Aanbevolen Velden (High Impact)

```
RECOMMENDED FIELDS
==================

Field               │ Impact │ Gebruik
────────────────────┼────────┼────────────────────────────
additional_image_link│ Hoog   │ 3-8 extra afbeeldingen
sale_price          │ Hoog   │ Strikethrough pricing
product_type        │ Hoog   │ Categorisatie voor sets
google_product_category│Med  │ Betere matching
custom_label_[0-4]  │ Hoog   │ Segmentatie (zie onder)
color               │ Medium │ Filter optie
size                │ Medium │ Filter optie
gender              │ Medium │ Targeting optie
age_group           │ Medium │ Targeting optie
shipping            │ Low    │ Gratis verzending highlight
```

### Custom Labels Strategie

```
CUSTOM LABEL BEST PRACTICES
===========================

Custom labels = 5 extra velden (0-4) voor segmentatie

AANBEVOLEN SETUP:

custom_label_0: MARGIN
├── "high_margin" (>40% marge)
├── "medium_margin" (20-40%)
└── "low_margin" (<20%)

custom_label_1: BESTSELLER STATUS
├── "bestseller" (top 20% verkoop)
├── "regular"
└── "slow_mover" (bottom 20%)

custom_label_2: PRICE RANGE
├── "budget" (<€25)
├── "mid_range" (€25-75)
├── "premium" (€75-150)
└── "luxury" (>€150)

custom_label_3: SEASONAL
├── "evergreen"
├── "summer"
├── "winter"
└── "holiday"

custom_label_4: INVENTORY STATUS
├── "plenty" (>50 stuks)
├── "limited" (10-50)
└── "almost_gone" (<10)
```

## Title & Description Optimization

### Title Best Practices

```
TITLE OPTIMIZATION
==================

FORMAT: [Brand] + [Product Type] + [Key Feature] + [Variant]

VOORBEELDEN:
❌ Slecht: "Mooie jurk"
✅ Goed: "Zara Maxi Jurk Bloemenprint Blauw Maat M"

❌ Slecht: "iPhone hoesje"
✅ Goed: "Apple iPhone 15 Pro Siliconen Hoesje Midnight Black"

REGELS:
├── Max 150 karakters (65-70 char optimal)
├── Belangrijkste keywords vooraan
├── Geen ALL CAPS
├── Geen promotional tekst ("SALE", "BESTE DEAL")
└── Include variant info (maat, kleur)
```

### Description Best Practices

```
DESCRIPTION OPTIMIZATION
========================

STRUCTUUR:
1. Opening met key benefit (eerste 50 karakters cruciaal)
2. Product features (bullets werken niet, maar duidelijke zinnen)
3. Specificaties (materiaal, afmetingen)
4. Use case / situatie

VOORBEELD:
"Stijlvolle maxi jurk met bloemenprint, perfect voor zomerse
dagen. Gemaakt van luchtige viscose voor optimaal draagcomfort.
De jurk heeft een flatterende A-lijn en verstelbare schouderbandjes.
Geschikt voor casual uitjes en strandvakanties."

LENGTH: 150-500 karakters optimal
```

## Product Set Strategies

### High-Performance Product Sets

```
PRODUCT SET TYPES
=================

SET 1: BESTSELLERS
├── Filter: custom_label_1 = "bestseller"
├── Use: Prospecting campaigns
└── Why: Bewezen performers, hogere CTR

SET 2: HIGH MARGIN
├── Filter: custom_label_0 = "high_margin"
├── Use: ROAS-focused campaigns
└── Why: Meer winst per sale

SET 3: SALE ITEMS
├── Filter: sale_price is not empty
├── Use: Retargeting, promotions
└── Why: Urgency, hogere conversie

SET 4: NEW ARRIVALS
├── Filter: created_date > [30 dagen geleden]
├── Use: Email subscribers, loyale klanten
└── Why: Nieuwigheid, FOMO

SET 5: PRICE BASED
├── Filter: price > €50 AND price < €100
├── Use: Segmented audiences
└── Why: Match met koopkracht doelgroep

SET 6: CATEGORY SPECIFIC
├── Filter: product_type contains "Jurken"
├── Use: Interest-based targeting
└── Why: Relevantie voor specifieke interesse
```

### Dynamic Product Set Logic

```
GEAVANCEERDE FILTERS
====================

COMBINATIE FILTERS:
├── Bestseller + High Margin + In Stock
│   └── custom_label_1 = "bestseller" AND
│       custom_label_0 = "high_margin" AND
│       availability = "in stock"
│
├── Premium producten voor High-Value audiences
│   └── custom_label_2 = "premium" OR
│       custom_label_2 = "luxury"
│
└── Urgency set (bijna uitverkocht)
    └── custom_label_4 = "almost_gone" AND
        availability = "in stock"
```

## DPA Campaign Structure

### Retargeting DPA Setup

```
DPA RETARGETING STRUCTURE
=========================

CAMPAIGN: [Brand]_DPA_Retargeting
├── Objective: Sales
├── Optimization: Purchase
└── Catalog: [Your Catalog]

AD SET 1: Viewed Not Purchased (3d)
├── Audience: ViewContent 3d, exclude Purchase 7d
├── Product Set: All products
├── Budget: 40% van DPA budget
└── Expected ROAS: 6-12x

AD SET 2: Add to Cart (7d)
├── Audience: AddToCart 7d, exclude Purchase 7d
├── Product Set: All products
├── Budget: 35% van DPA budget
└── Expected ROAS: 8-15x

AD SET 3: Past Purchasers - Cross-sell (30d)
├── Audience: Purchase 30d
├── Product Set: Complementary products
├── Budget: 25% van DPA budget
└── Expected ROAS: 4-8x
```

### Prospecting DPA Setup

```
DPA PROSPECTING STRUCTURE
=========================

CAMPAIGN: [Brand]_DPA_Prospecting
├── Objective: Sales
├── Optimization: Purchase
└── Catalog: [Your Catalog]

AD SET 1: Broad Prospecting
├── Audience: Broad (alleen demo + geo)
├── Product Set: Bestsellers only
├── Budget: 50% van prospecting budget
└── Expected ROAS: 2-4x

AD SET 2: Interest-Based
├── Audience: Relevante interesses
├── Product Set: Category specific
├── Budget: 30% van prospecting budget
└── Expected ROAS: 2.5-4.5x

AD SET 3: Lookalike Purchasers
├── Audience: LAL 1-3% purchasers
├── Product Set: High margin products
├── Budget: 20% van prospecting budget
└── Expected ROAS: 3-5x
```

## Advantage+ Shopping Campaigns

### ASC Optimization

```
ADVANTAGE+ SHOPPING SETUP
=========================

WANNEER GEBRUIKEN:
├── E-commerce met 50+ conversies/week
├── Catalog met 20+ producten
├── Bereid om controle op te geven
└── Focus op volume + efficiency

SETUP:
├── Campaign: Advantage+ Shopping
├── Catalog: Full catalog (of bestseller set)
├── Budget: Start met 2x normale CPA × 50
├── Existing customer budget cap: 30-50%
└── Countries: Focus markets

CREATIVE INPUT:
├── 3-5 lifestyle images
├── 3-5 product images
├── 3-5 video assets
└── Headlines & primary text variaties

OPTIMIZATION TIPS:
├── Geef ASC minimaal 7 dagen zonder wijzigingen
├── Review "Audience segments" voor insights
├── Gebruik existing customer cap slim
└── Combineer met separate retargeting indien nodig
```

## Catalog Troubleshooting

### Veelvoorkomende Problemen

```
TROUBLESHOOTING GUIDE
=====================

PROBLEEM: Producten niet goedgekeurd
├── Check: Policy violations (alcohol, adult, etc.)
├── Check: Missing required fields
├── Check: Image quality issues
└── Fix: Review Diagnostics tab in Commerce Manager

PROBLEEM: Feed sync errors
├── Check: Feed URL accessible?
├── Check: XML/CSV format correct?
├── Check: Encoding issues (UTF-8)?
└── Fix: Validate feed met Facebook Debug Tool

PROBLEEM: Lage delivery in DPA
├── Check: Product set te klein? (min 20 products)
├── Check: Audience te smal?
├── Check: Alle producten in stock?
└── Fix: Expand product set, broaden audience

PROBLEEM: Verkeerde producten getoond
├── Check: Product matching correct?
├── Check: Content IDs in pixel = feed IDs?
├── Check: Pixel events vuren correct?
└── Fix: Verify content_id mapping

PROBLEEM: Hoge CPA in DPA
├── Check: Product set kwaliteit
├── Check: Catalog completeness
├── Check: Image quality
└── Fix: Focus op bestsellers, optimize feed
```

### Catalog Health Checklist

```
CATALOG AUDIT CHECKLIST
=======================

□ FEED QUALITY
├── Alle required fields aanwezig?
├── Titles geoptimaliseerd (keywords vooraan)?
├── Descriptions informatief (>100 char)?
├── Images high quality (500x500+)?
└── Prijzen correct en up-to-date?

□ SYNC STATUS
├── Laatste sync recent (<24 uur)?
├── Geen feed errors?
├── Update schedule ingesteld?
└── Out of stock items correct?

□ PRODUCT SETS
├── Minimaal 3-5 strategische sets?
├── Bestseller set aanwezig?
├── High margin set aanwezig?
├── Sets regelmatig geüpdatet?
└── Geen lege sets?

□ PIXEL MATCHING
├── Content IDs matchen feed IDs?
├── ViewContent, AddToCart, Purchase events OK?
├── Microdata/Pixel helper validated?
└── Deduplication correct?

□ PERFORMANCE REVIEW
├── CTR per product set monitored?
├── Low performers identified?
├── Best performers scaled?
└── Regular feed optimization?
```

## Voorbeeld Interactie

**Gebruiker**: "Mijn DPA campagnes presteren slecht. De ROAS is maar 1.5x terwijl ik 3x verwacht. Wat kan ik doen?"

**Claude response**:

"Laten we je DPA performance systematisch troubleshooten:

---

**DIAGNOSTISCHE VRAGEN:**

1. **Feed Quality:**
   - Hoeveel producten in je catalog?
   - Heb je custom labels ingesteld?
   - Zijn titles geoptimaliseerd?

2. **Campaign Setup:**
   - Retargeting of prospecting DPA?
   - Welke product sets gebruik je?
   - Wat is je audience window?

3. **Creative:**
   - Gebruik je catalog-only of custom creative overlay?
   - Zijn product images high-quality?

---

**SNELLE CHECKS (doe nu):**

1. **Commerce Manager → Diagnostics**
   - Zijn er warnings/errors?
   - % approved products?

2. **Events Manager → Test Events**
   - Vuren ViewContent/ATC/Purchase correct?
   - Matchen content_ids met feed?

3. **Ad Set → Delivery Insights**
   - Auction overlap?
   - Audience saturation?

---

**QUICK WINS voor ROAS verbetering:**

1. **Product Set Focus**
   ```
   Maak een "Top Performers" set:
   - Filter: Bestsellers + In Stock + High Margin
   - Test dit apart van full catalog
   ```

2. **Audience Narrowing**
   ```
   Retargeting: Verkort window van 30d → 14d
   Meer recent = hogere intent = betere ROAS
   ```

3. **Creative Overlay**
   ```
   Voeg "Free Shipping" of "Sale" badges toe
   Kan CTR met 15-30% verhogen
   ```

Deel je specifieke setup en ik geef gerichtere aanbevelingen!"

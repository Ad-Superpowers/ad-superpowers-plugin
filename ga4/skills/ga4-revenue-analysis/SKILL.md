---
name: ga4-revenue-analysis
description: "Revenue en product performance analyse in GA4. Gebruik voor: (1) Revenue reports interpreteren, (2) Product performance analyseren, (3) Checkout funnel analyse, (4) Purchase journey insights, (5) E-commerce KPI dashboards bouwen. Triggers: revenue analyse, product performance, checkout funnel, conversie analyse, omzet rapportage, e-commerce kpi, best sellers."
---

# GA4 Revenue Analysis Guide

Complete gids voor het analyseren van e-commerce revenue, product performance en checkout funnels in Google Analytics 4.

## Quick Decision Tree

```
GA4 REVENUE ANALYSE FLOW
│
├─► WAT WIL JE ANALYSEREN?
│   ├─► Overall revenue & trends
│   │   └─► Monetization overview report
│   │       └─► Date comparison voor trends
│   │
│   ├─► Product performance
│   │   └─► E-commerce purchases report
│   │       └─► Items viewed vs purchased
│   │
│   ├─► Checkout dropoff
│   │   └─► Custom funnel exploration
│   │       └─► Checkout stap analyse
│   │
│   └─► Customer journey
│       └─► Path exploration
│           └─► Purchase pad analyse
│
├─► WELKE DIMENSIES NODIG?
│   ├─► Traffic source impact
│   │   └─► Session source/medium breakdown
│   │
│   ├─► Device/platform
│   │   └─► Device category, platform
│   │
│   └─► Audience segments
│       └─► Custom segments of audiences
│
└─► RAPPORTAGE BEHOEFTE?
    ├─► Ad-hoc analyse
    │   └─► Explorations (vrije analyse)
    │
    ├─► Recurring reports
    │   └─► Custom reports in Library
    │
    └─► External dashboards
        └─► Looker Studio / BigQuery export
```

## Monetization Reports Overzicht

```
GA4 MONETIZATION REPORTS
========================

LOCATIE: Reports → Monetization

BESCHIKBARE REPORTS:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Report                  │ Toont                                    │
├─────────────────────────┼──────────────────────────────────────────┤
│ Overview                │ Revenue KPIs, trends, top items          │
├─────────────────────────┼──────────────────────────────────────────┤
│ E-commerce purchases    │ Product-level metrics (views, carts,     │
│                         │ purchases, revenue)                      │
├─────────────────────────┼──────────────────────────────────────────┤
│ In-app purchases        │ App subscription/purchase data           │
├─────────────────────────┼──────────────────────────────────────────┤
│ Publisher ads           │ Ad revenue (AdMob/Ad Manager)            │
├─────────────────────────┼──────────────────────────────────────────┤
│ Promotions              │ Promotion performance                    │
└─────────────────────────┴──────────────────────────────────────────┘

MONETIZATION OVERVIEW METRICS:
──────────────────────────────
┌─────────────────────────┬──────────────────────────────────────────┐
│ Metric                  │ Definitie                                │
├─────────────────────────┼──────────────────────────────────────────┤
│ Total revenue           │ purchase + in_app_purchase + ad revenue  │
├─────────────────────────┼──────────────────────────────────────────┤
│ E-commerce revenue      │ Alleen purchase event revenue            │
├─────────────────────────┼──────────────────────────────────────────┤
│ Total purchasers        │ Unieke users met purchase event          │
├─────────────────────────┼──────────────────────────────────────────┤
│ First-time purchasers   │ Users met eerste purchase ooit           │
├─────────────────────────┼──────────────────────────────────────────┤
│ ARPPU                   │ Average Revenue Per Paying User          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Average purchase value  │ Gemiddelde orderwaarde                   │
└─────────────────────────┴──────────────────────────────────────────┘
```

## Product Performance Analyse

```
E-COMMERCE PURCHASES REPORT
===========================

LOCATIE: Reports → Monetization → E-commerce purchases

KEY METRICS PER PRODUCT:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Metric                  │ Betekenis                                │
├─────────────────────────┼──────────────────────────────────────────┤
│ Items viewed            │ Aantal view_item events                  │
├─────────────────────────┼──────────────────────────────────────────┤
│ Items added to cart     │ Aantal add_to_cart events                │
├─────────────────────────┼──────────────────────────────────────────┤
│ Items purchased         │ Aantal items in purchase events          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Item revenue            │ Totale omzet per product                 │
├─────────────────────────┼──────────────────────────────────────────┤
│ Cart-to-view rate       │ (added to cart / viewed) × 100%          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Purchase-to-view rate   │ (purchased / viewed) × 100%              │
└─────────────────────────┴──────────────────────────────────────────┘

BESCHIKBARE DIMENSIES:
├── Item name
├── Item ID
├── Item brand
├── Item category (1-5 levels)
├── Item variant
└── Item list name

ANALYSE TIPS:
─────────────
1. VIEW-TO-CART RATE < 5%
   └── Product pagina optimalisatie nodig
       ├── Betere productfoto's
       ├── Duidelijkere pricing
       └── Verbeter product beschrijving

2. CART-TO-PURCHASE RATE < 30%
   └── Checkout optimalisatie nodig
       ├── Verzendkosten duidelijker
       ├── Trust badges toevoegen
       └── Checkout simplificeren

3. HOGE VIEWS, LAGE REVENUE
   └── Onderzoek product issues
       ├── Pricing vs concurrentie
       ├── Stock availability
       └── Product-market fit
```

## Checkout Funnel Analyse

```
CHECKOUT FUNNEL EXPLORATION
===========================

LOCATIE: Explore → Funnel exploration

SETUP STAPPEN:
┌────┬────────────────────────────────────────────────────────────────┐
│ 1  │ Explore → Blank → Kies "Funnel exploration"                   │
├────┼────────────────────────────────────────────────────────────────┤
│ 2  │ Tab Settings → Steps → Edit                                   │
├────┼────────────────────────────────────────────────────────────────┤
│ 3  │ Voeg checkout events toe als stappen:                         │
│    │ ├── Step 1: view_cart                                         │
│    │ ├── Step 2: begin_checkout                                    │
│    │ ├── Step 3: add_shipping_info                                 │
│    │ ├── Step 4: add_payment_info                                  │
│    │ └── Step 5: purchase                                          │
├────┼────────────────────────────────────────────────────────────────┤
│ 4  │ Optioneel: Maak stappen "closed" voor stricte sequence        │
├────┼────────────────────────────────────────────────────────────────┤
│ 5  │ Breakdown toevoegen (device, source, etc.)                    │
└────┴────────────────────────────────────────────────────────────────┘

FUNNEL METRICS:
───────────────
┌─────────────────────────┬──────────────────────────────────────────┐
│ Metric                  │ Betekenis                                │
├─────────────────────────┼──────────────────────────────────────────┤
│ Users (per step)        │ Unieke users die stap bereiken           │
├─────────────────────────┼──────────────────────────────────────────┤
│ Completion rate         │ % users die volgende stap bereiken       │
├─────────────────────────┼──────────────────────────────────────────┤
│ Abandonment rate        │ % users die afhaken bij stap             │
├─────────────────────────┼──────────────────────────────────────────┤
│ Time to convert         │ Gemiddelde tijd door funnel              │
└─────────────────────────┴──────────────────────────────────────────┘

BENCHMARK COMPLETION RATES:
───────────────────────────
┌─────────────────────────┬──────────────┬───────────────────────────┐
│ Stap                    │ Benchmark    │ Actie bij lagere rate     │
├─────────────────────────┼──────────────┼───────────────────────────┤
│ Cart → Checkout         │ 50-70%       │ Cart abandonment emails   │
├─────────────────────────┼──────────────┼───────────────────────────┤
│ Checkout → Shipping     │ 70-85%       │ Simplify form fields      │
├─────────────────────────┼──────────────┼───────────────────────────┤
│ Shipping → Payment      │ 80-90%       │ Meer verzendopties        │
├─────────────────────────┼──────────────┼───────────────────────────┤
│ Payment → Purchase      │ 70-85%       │ Meer betaalopties         │
├─────────────────────────┼──────────────┼───────────────────────────┤
│ Overall funnel          │ 25-40%       │ End-to-end optimalisatie  │
└─────────────────────────┴──────────────┴───────────────────────────┘
```

## Revenue per Traffic Source

```
TRAFFIC SOURCE REVENUE ANALYSE
==============================

LOCATIE: Reports → Acquisition → Traffic acquisition

SECONDARY DIMENSION TOEVOEGEN:
──────────────────────────────
1. Click "+" naast primaire dimensie
2. Selecteer "E-commerce" → "Total revenue"
3. Of voeg metrics toe via "Edit comparisons"

CUSTOM EXPLORATION VOOR REVENUE:
────────────────────────────────
SETUP:
├── Technique: Free form
├── Rows: Session source/medium
├── Values:
│   ├── Total revenue
│   ├── Transactions
│   ├── Average purchase value
│   ├── E-commerce conversion rate
│   └── Sessions
└── Filter: Alleen sessies met transactions (optioneel)

KEY ANALYSES:
─────────────
1. REVENUE PER SOURCE
   ├── Welke bronnen genereren meeste omzet?
   ├── Welke hebben hoogste conversie rate?
   └── Welke hebben hoogste AOV?

2. ROAS BEREKENING (handmatig)
   ├── Export revenue per source
   ├── Match met ad spend data
   └── Bereken: Revenue / Ad Spend

3. ASSISTED CONVERSIONS
   ├── Welke bronnen assisteren purchases?
   └── Zie Attribution → Conversion paths
```

## Key E-commerce KPIs

```
ESSENTIËLE E-COMMERCE KPIs
==========================

REVENUE KPIs:
┌─────────────────────────┬──────────────────────────────────────────┐
│ KPI                     │ Berekening / Locatie                     │
├─────────────────────────┼──────────────────────────────────────────┤
│ Total Revenue           │ Monetization → Overview                  │
├─────────────────────────┼──────────────────────────────────────────┤
│ Average Order Value     │ Total revenue / Transactions             │
│ (AOV)                   │                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Revenue per Session     │ Total revenue / Sessions                 │
│ (RPS)                   │                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Revenue per User        │ Total revenue / Total users              │
│ (RPU)                   │                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Customer Lifetime       │ Requires cohort analysis                 │
│ Value (CLV)             │                                          │
└─────────────────────────┴──────────────────────────────────────────┘

CONVERSION KPIs:
┌─────────────────────────┬──────────────────────────────────────────┐
│ KPI                     │ Berekening                               │
├─────────────────────────┼──────────────────────────────────────────┤
│ E-commerce Conv. Rate   │ Purchasers / Total users × 100%         │
├─────────────────────────┼──────────────────────────────────────────┤
│ Cart Abandonment Rate   │ (Carts - Purchases) / Carts × 100%      │
├─────────────────────────┼──────────────────────────────────────────┤
│ Checkout Abandon Rate   │ (Checkouts - Purchases) / Checkouts     │
├─────────────────────────┼──────────────────────────────────────────┤
│ Add-to-Cart Rate        │ Add to cart users / Total users × 100%  │
└─────────────────────────┴──────────────────────────────────────────┘

PRODUCT KPIs:
┌─────────────────────────┬──────────────────────────────────────────┐
│ KPI                     │ Berekening                               │
├─────────────────────────┼──────────────────────────────────────────┤
│ Product View Rate       │ Item views / Sessions × 100%            │
├─────────────────────────┼──────────────────────────────────────────┤
│ Cart-to-Detail Rate     │ Add to cart / Item views × 100%         │
├─────────────────────────┼──────────────────────────────────────────┤
│ Buy-to-Detail Rate      │ Purchases / Item views × 100%           │
├─────────────────────────┼──────────────────────────────────────────┤
│ Average Items/Order     │ Items purchased / Transactions          │
└─────────────────────────┴──────────────────────────────────────────┘
```

## Custom Explorations voor E-commerce

```
EXPLORATION 1: PRODUCT CATEGORY PERFORMANCE
===========================================

SETUP:
├── Technique: Free form
├── Rows: Item category
├── Values:
│   ├── Item revenue
│   ├── Items purchased
│   ├── Item views
│   ├── Cart-to-view rate
│   └── Purchase-to-view rate
└── Filters: Date range

INZICHTEN:
├── Welke categorieën presteren best?
├── Waar zijn optimalisatie kansen?
└── Category growth trends


EXPLORATION 2: DEVICE REVENUE VERGELIJKING
==========================================

SETUP:
├── Technique: Free form
├── Rows: Device category
├── Values:
│   ├── Total revenue
│   ├── Transactions
│   ├── Average purchase value
│   ├── E-commerce conversion rate
│   └── Sessions
└── Visualisatie: Bar chart

INZICHTEN:
├── Mobile vs Desktop conversie gaps
├── Waar mobile optimalisatie nodig?
└── Cross-device journey impact


EXPLORATION 3: NEW VS RETURNING PURCHASERS
==========================================

SETUP:
├── Technique: Free form
├── Rows: New/established
├── Values:
│   ├── Total revenue
│   ├── First-time purchasers
│   ├── Purchasers
│   ├── Average purchase value
│   └── Transactions
└── Segmenteer op tijd voor trends

INZICHTEN:
├── Retentie health check
├── Nieuwe klant acquisitie kost
└── Repeat purchase rate
```

## Cohort Analyse voor CLV

```
PURCHASER COHORT ANALYSIS
=========================

LOCATIE: Explore → Cohort exploration

SETUP:
┌────┬────────────────────────────────────────────────────────────────┐
│ 1  │ Cohort inclusion: first_open of first_visit                   │
├────┼────────────────────────────────────────────────────────────────┤
│ 2  │ Return criteria: purchase (of custom purchase event)          │
├────┼────────────────────────────────────────────────────────────────┤
│ 3  │ Cohort granularity: Weekly of Monthly                         │
├────┼────────────────────────────────────────────────────────────────┤
│ 4  │ Values: User retention of Event count of Metric sum           │
├────┼────────────────────────────────────────────────────────────────┤
│ 5  │ Breakdown: Traffic source (optioneel)                         │
└────┴────────────────────────────────────────────────────────────────┘

COHORT METRIC OPTIONS:
──────────────────────
├── User retention: % users die terugkomen en kopen
├── Event count: Aantal aankopen per cohort over tijd
└── Metric sum: Revenue per cohort over tijd

ANALYSE VRAGEN:
───────────────
├── Welk % koopt opnieuw na 30/60/90 dagen?
├── Welke acquisitie bron heeft beste CLV?
├── Hoe lang duurt het tot repeat purchase?
└── Welke cohorts (seizoenen) presteren best?

PREDICTIVE CLV BEREKENING:
──────────────────────────
CLV = AOV × Aankoopfrequentie × Klantlevensduur

Voorbeeld:
├── AOV: €75
├── Aankopen per jaar: 3
├── Gemiddelde klantduur: 2.5 jaar
└── CLV = €75 × 3 × 2.5 = €562.50
```

## Veelvoorkomende Problemen

```
TROUBLESHOOTING REVENUE ANALYSE
===============================

PROBLEEM: Revenue toont €0 of ontbreekt
───────────────────────────────────────
Oorzaken:
├── purchase event niet geïmplementeerd
├── value parameter ontbreekt
├── Currency niet geconfigureerd
├── Data processing delay (24-48 uur)
└── Filters in report

Oplossing:
├── Verify purchase event in DebugView
├── Check dataLayer voor value parameter
├── Controleer property currency setting
├── Wacht op data processing
└── Remove report filters en test opnieuw


PROBLEEM: AOV onrealistisch hoog/laag
─────────────────────────────────────
Oorzaken:
├── Test transactions in data
├── Duplicate purchases
├── Pricing in verkeerde currency
├── Tax/shipping incorrect meegerekend
└── Item quantities fout

Oplossing:
├── Exclude test orders met segment
├── Check transaction_id duplicates
├── Verify currency matching
├── Review value berekening in code
└── Audit quantity parameters


PROBLEEM: Product data niet zichtbaar
─────────────────────────────────────
Oorzaken:
├── items array ontbreekt in events
├── Item parameters incorrect
├── item_id/item_name ontbreekt
├── GA4 report processing time
└── Onvoldoende data volume

Oplossing:
├── Check items array in dataLayer
├── Verify verplichte item parameters
├── Ensure item_id en item_name aanwezig
├── Wacht 24-48 uur voor processing
└── Langere date range selecteren


PROBLEEM: Funnel toont geen data
────────────────────────────────
Oorzaken:
├── Checkout events niet geïmplementeerd
├── Event namen incorrect
├── Closed funnel te strict
├── Segment filters te narrow
└── Date range te kort

Oplossing:
├── Verify alle checkout events actief
├── Check exacte event namen in DebugView
├── Maak funnel "open" voor testen
├── Verwijder of verbreed segments
└── Selecteer langere date range
```

## Output: Revenue Analysis Report Template

```markdown
# GA4 Revenue Analyse Rapport

## Rapportage Periode
- **Van:** [Startdatum]
- **Tot:** [Einddatum]
- **Vergelijking:** [Vorige periode/Vorig jaar]

## Executive Summary

| KPI | Huidige Periode | Vergelijking | Trend |
|-----|-----------------|--------------|-------|
| Total Revenue | €XX,XXX | €XX,XXX | +X% |
| Transactions | X,XXX | X,XXX | +X% |
| Average Order Value | €XX.XX | €XX.XX | +X% |
| Conversion Rate | X.X% | X.X% | +X% |
| Cart Abandonment | XX% | XX% | -X% |

## Revenue per Traffic Source

| Source/Medium | Revenue | % van Totaal | Conv. Rate | AOV |
|---------------|---------|--------------|------------|-----|
| google / organic | €X,XXX | XX% | X.X% | €XX |
| google / cpc | €X,XXX | XX% | X.X% | €XX |
| direct / (none) | €X,XXX | XX% | X.X% | €XX |
| [Overige] | €X,XXX | XX% | X.X% | €XX |

## Top 10 Products (Revenue)

| Product | Revenue | Units Sold | View-to-Cart | Cart-to-Purchase |
|---------|---------|------------|--------------|------------------|
| [Product 1] | €X,XXX | XXX | XX% | XX% |
| [Product 2] | €X,XXX | XXX | XX% | XX% |
| ... | ... | ... | ... | ... |

## Category Performance

| Category | Revenue | Growth | Contribution |
|----------|---------|--------|--------------|
| [Category 1] | €X,XXX | +XX% | XX% |
| [Category 2] | €X,XXX | +XX% | XX% |
| [Category 3] | €X,XXX | -XX% | XX% |

## Checkout Funnel Performance

| Stap | Users | Drop-off | Benchmark |
|------|-------|----------|-----------|
| View Cart | X,XXX | - | - |
| Begin Checkout | X,XXX | XX% | 30-50% |
| Add Shipping | X,XXX | XX% | 15-30% |
| Add Payment | X,XXX | XX% | 10-20% |
| Purchase | X,XXX | XX% | 15-30% |

**Overall Funnel Conversion:** XX% (benchmark: 25-40%)

## Device Breakdown

| Device | Revenue | % Share | Conv. Rate | AOV |
|--------|---------|---------|------------|-----|
| Desktop | €X,XXX | XX% | X.X% | €XX |
| Mobile | €X,XXX | XX% | X.X% | €XX |
| Tablet | €X,XXX | XX% | X.X% | €XX |

## Key Insights

### Positieve Trends
1. [Inzicht 1]
2. [Inzicht 2]

### Aandachtspunten
1. [Probleem 1] - Impact: [Hoog/Midden/Laag]
2. [Probleem 2] - Impact: [Hoog/Midden/Laag]

## Aanbevelingen

| Prioriteit | Actie | Verwachte Impact |
|------------|-------|------------------|
| 🔴 Hoog | [Actie 1] | +XX% revenue |
| 🟡 Midden | [Actie 2] | +XX% conversion |
| 🟢 Laag | [Actie 3] | UX verbetering |

## Volgende Stappen
1. [ ] [Eerste actie]
2. [ ] [Tweede actie]
3. [ ] [Derde actie]
```

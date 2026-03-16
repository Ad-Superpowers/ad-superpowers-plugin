---
name: full-funnel-designer
description: Ontwerp complete full-funnel Meta Ads strategieën met geoptimaliseerde campagne-structuren voor elke fase van de customer journey. Gebruik deze skill wanneer je een volledige funnel moet opzetten, budget moet verdelen over funnel-fases, of een bestaande funnel wilt optimaliseren.
---

# Full-Funnel Designer

## Overview

Deze skill helpt bij het ontwerpen van complete full-funnel advertentiestrategieën voor Meta Ads, inclusief budget allocatie, audience targeting per fase, en creative afstemming op de customer journey.

## Funnel Framework

### De 3 Funnel Fases

```
┌─────────────────────────────────────────────────────────────────┐
│  TOFU (Top of Funnel) - AWARENESS                               │
│  ├── Doel: Bereik & merkbekendheid                              │
│  ├── Budget: 20-30% van totaal                                  │
│  ├── Audiences: Broad, Lookalikes 3-10%, Interest-based         │
│  ├── Objectives: Reach, Video Views, Brand Awareness            │
│  ├── Creatives: Educational, entertaining, brand story          │
│  └── KPIs: CPM, Reach, Video ThruPlay, Frequency                │
├─────────────────────────────────────────────────────────────────┤
│  MOFU (Middle of Funnel) - CONSIDERATION                        │
│  ├── Doel: Engagement & interesse opbouwen                      │
│  ├── Budget: 30-40% van totaal                                  │
│  ├── Audiences: Engagers, Video viewers, Website visitors       │
│  ├── Objectives: Traffic, Engagement, Lead Generation           │
│  ├── Creatives: Product demos, testimonials, comparisons        │
│  └── KPIs: CTR, CPC, Landing page views, Time on site           │
├─────────────────────────────────────────────────────────────────┤
│  BOFU (Bottom of Funnel) - CONVERSION                           │
│  ├── Doel: Conversies & sales                                   │
│  ├── Budget: 30-50% van totaal                                  │
│  ├── Audiences: Add to cart, High-intent visitors, Customers    │
│  ├── Objectives: Conversions, Catalog Sales                     │
│  ├── Creatives: Urgency, offers, social proof, retargeting      │
│  └── KPIs: CPA, ROAS, Conversion rate, AOV                      │
└─────────────────────────────────────────────────────────────────┘
```

## Budget Allocatie Calculator

### Vraag de gebruiker:

1. **Wat is je totale maandbudget?**
2. **Wat is je huidige situatie?**
   - Nieuw merk (weinig awareness) → Meer TOFU
   - Gevestigd merk (veel traffic) → Meer BOFU
   - Groeiend merk (balans nodig) → Evenwichtige verdeling

### Budget Verdeelmodellen

#### Model A: Nieuw Merk / Awareness Focus
```
TOFU: 40% │████████████████████
MOFU: 35% │█████████████████▌
BOFU: 25% │████████████▌
```

#### Model B: Gebalanceerd / Groei Focus
```
TOFU: 25% │████████████▌
MOFU: 35% │█████████████████▌
BOFU: 40% │████████████████████
```

#### Model C: Gevestigd Merk / Performance Focus
```
TOFU: 15% │███████▌
MOFU: 25% │████████████▌
BOFU: 60% │██████████████████████████████
```

## Audience Mapping per Fase

### TOFU Audiences (Cold)

| Audience Type | Beschrijving | Verwachte CPM |
|---------------|--------------|---------------|
| Broad | Alleen demo + geo | €3-8 |
| Interest Stacking | 3-5 gerelateerde interesses | €5-10 |
| Lookalike 6-10% | Brede lookalike van purchasers | €4-8 |
| Video Viewers LAL | Lookalike van 95% video viewers | €5-9 |

### MOFU Audiences (Warm)

| Audience Type | Beschrijving | Window |
|---------------|--------------|--------|
| Video Viewers | 50%, 75%, 95% van video gekeken | 30-60 dagen |
| Page Engagers | Likes, comments, shares | 30-90 dagen |
| Website Visitors | Alle bezoekers (excl. converters) | 30-60 dagen |
| Blog Readers | Specifieke content pagina's | 30-60 dagen |
| IG/FB Engagers | Profiel bezoekers, post engagers | 30-90 dagen |

### BOFU Audiences (Hot)

| Audience Type | Beschrijving | Window |
|---------------|--------------|--------|
| Add to Cart | Product toegevoegd, niet gekocht | 7-14 dagen |
| View Content | Productpagina bekeken | 7-14 dagen |
| Initiate Checkout | Checkout gestart, niet afgerond | 3-7 dagen |
| Past Purchasers | Cross-sell/upsell | 30-180 dagen |
| High-Value Customers | Top 20% LTV | 180-365 dagen |

## Creative Strategy per Fase

### TOFU Creative Formats

```
Aanbevolen formats:
├── Video (15-30 sec) - Hook binnen 3 seconden
├── Carousel - Storytelling of educational
├── Reels - Native, entertaining content
└── Collection - Brand discovery

Content types:
├── Educational ("Wist je dat...")
├── Entertainment (Relatable content)
├── Brand story (Waarden, missie)
└── User generated (Authentiek)
```

### MOFU Creative Formats

```
Aanbevolen formats:
├── Video (30-60 sec) - Product demo's
├── Carousel - Feature highlights
├── Lead ads - Gated content
└── Instant Experience - Immersive storytelling

Content types:
├── Product demonstrations
├── Customer testimonials
├── How-to guides
├── Comparison content
└── Behind the scenes
```

### BOFU Creative Formats

```
Aanbevolen formats:
├── DPA (Dynamic Product Ads)
├── Carousel - Retargeting viewed products
├── Single image - Strong CTA
└── Collection - Product catalog

Content types:
├── Urgency ("Laatste kans", "Bijna uitverkocht")
├── Social proof (Reviews, ratings)
├── Special offers (Korting, gratis verzending)
├── Abandoned cart reminders
└── Limited time deals
```

## Full-Funnel Campagne Template

### Wanneer de gebruiker vraagt om een funnel op te zetten:

```
CAMPAGNE STRUCTUUR TEMPLATE
===========================

📊 Budget: [TOTAAL BUDGET]

🔵 TOFU CAMPAGNE - Awareness
   ├── Naam: [BRAND]_TOFU_Awareness_[MAAND]
   ├── Objective: Reach / Video Views
   ├── Budget: [X]% = €[BEDRAG]
   ├── Audiences:
   │   ├── Ad Set 1: Broad (18-65, [LAND])
   │   ├── Ad Set 2: Interest Stack ([INTERESSES])
   │   └── Ad Set 3: LAL 6-10% Purchasers
   └── Creatives:
       ├── Video 1: Brand story (15 sec)
       ├── Video 2: Educational hook
       └── Carousel: Value proposition

🟡 MOFU CAMPAGNE - Consideration
   ├── Naam: [BRAND]_MOFU_Consideration_[MAAND]
   ├── Objective: Traffic / Engagement
   ├── Budget: [X]% = €[BEDRAG]
   ├── Audiences:
   │   ├── Ad Set 1: Video Viewers 50%+ (30d)
   │   ├── Ad Set 2: Page Engagers (60d)
   │   └── Ad Set 3: Website Visitors (30d)
   └── Creatives:
       ├── Video 1: Product demo
       ├── Carousel: Features & benefits
       └── Testimonial: Customer story

🟢 BOFU CAMPAGNE - Conversion
   ├── Naam: [BRAND]_BOFU_Conversion_[MAAND]
   ├── Objective: Conversions / Sales
   ├── Budget: [X]% = €[BEDRAG]
   ├── Audiences:
   │   ├── Ad Set 1: Add to Cart (14d)
   │   ├── Ad Set 2: View Content (7d)
   │   └── Ad Set 3: Past Purchasers (90d)
   └── Creatives:
       ├── DPA: Viewed products
       ├── Single image: Urgency offer
       └── Carousel: Social proof
```

## Frequentie & Overlap Management

### Frequentie Richtlijnen per Fase

| Fase | Max Frequentie/Week | Actie bij Overschrijding |
|------|---------------------|--------------------------|
| TOFU | 2-3x | Audience uitbreiden |
| MOFU | 3-4x | Creative refreshen |
| BOFU | 5-7x | Exclusions toevoegen |

### Audience Exclusions Setup

```
TOFU exclusions:
└── Exclude: MOFU + BOFU audiences

MOFU exclusions:
├── Exclude: Purchasers (30d)
└── Exclude: Add to Cart (7d)

BOFU exclusions:
└── Exclude: Purchasers (7d) of converters
```

## Funnel Diagnose Framework

### Wanneer de funnel niet presteert:

```
PROBLEEM: Weinig awareness/reach
├── Check: Is TOFU budget voldoende? (min 20%)
├── Check: Zijn audiences te smal?
└── Actie: Breder targeten, meer video content

PROBLEEM: Hoge TOFU metrics, lage MOFU engagement
├── Check: Sluit MOFU content aan bij TOFU messaging?
├── Check: Zijn retargeting windows correct?
└── Actie: Content afstemmen, windows verlengen

PROBLEEM: Goede engagement, weinig conversies
├── Check: Is landing page geoptimaliseerd?
├── Check: Zijn BOFU offers compelling genoeg?
└── Actie: A/B test offers, urgency toevoegen

PROBLEEM: Hoge CPA in BOFU
├── Check: Is audience te klein (audience exhaustion)?
├── Check: Frequentie te hoog?
└── Actie: TOFU/MOFU versterken, creative refresh
```

## Voorbeeld Interactie

**Gebruiker**: "Ik wil een full-funnel opzetten voor mijn e-commerce webshop. Budget is €5000/maand."

**Claude response**:

"Ik help je met een complete full-funnel strategie. Eerst een paar vragen:

1. **Wat verkoop je?** (product categorie)
2. **Is je merk al bekend of start je nieuw?**
3. **Heb je al bestaande pixel data/audiences?**
4. **Wat is je gemiddelde orderwaarde (AOV)?**

Op basis van €5000/maand en een gemiddeld scenario zou ik voorstellen:

| Fase | Budget | Doel |
|------|--------|------|
| TOFU | €1.250 (25%) | Nieuwe mensen bereiken |
| MOFU | €1.750 (35%) | Interest opbouwen |
| BOFU | €2.000 (40%) | Conversies realiseren |

Wil je dat ik de complete campagnestructuur uitwerk met audiences en creative suggesties?"

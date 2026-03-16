---
name: lookalike-strategy-planner
description: Ontwikkel effectieve Lookalike Audience strategieën voor Meta Ads met optimale source audiences, percentages en layering technieken. Gebruik deze skill wanneer je lookalikes wilt opzetten, optimaliseren, of wanneer bestaande lookalikes niet presteren.
---

# Lookalike Strategy Planner

## Overview

Deze skill helpt bij het creëren van hoogwaardige Lookalike Audiences door de juiste source audiences te selecteren, optimale percentages te kiezen, en geavanceerde strategieën toe te passen voor maximale performance.

## Lookalike Fundamentals

### Hoe Meta Lookalikes Werkt

```
┌─────────────────────────────────────────────────────────────────┐
│  LOOKALIKE CREATION PROCES                                      │
│                                                                 │
│  1. SOURCE AUDIENCE (jouw data)                                 │
│     └── Minimaal 100 mensen (1000+ aanbevolen)                  │
│                                                                 │
│  2. META's ALGORITME analyseert:                                │
│     ├── Demografische data                                      │
│     ├── Interesses & gedrag                                     │
│     ├── Engagement patronen                                     │
│     ├── Purchase behavior                                       │
│     └── Cross-platform activiteit                               │
│                                                                 │
│  3. LOOKALIKE OUTPUT                                            │
│     └── Top X% van mensen die het meest lijken op source        │
│                                                                 │
│  Belangrijk: Kwaliteit source > Grootte source                  │
└─────────────────────────────────────────────────────────────────┘
```

## Source Audience Ranking

### Tier 1: Hoogste Kwaliteit (Aanbevolen)

| Source Type | Min. Grootte | Waarom Effectief |
|-------------|--------------|------------------|
| Purchasers (180d) | 500+ | Bewezen koopintentie |
| High-Value Customers (Top 20% LTV) | 200+ | Kwaliteit > kwantiteit |
| Repeat Purchasers | 200+ | Loyaliteit signaal |
| Subscribers (Email/SMS) | 1000+ | Actieve interesse |

### Tier 2: Goede Kwaliteit

| Source Type | Min. Grootte | Waarom Effectief |
|-------------|--------------|------------------|
| Add to Cart (30d) | 500+ | Hoge intentie |
| Lead Form Completers | 300+ | Gekwalificeerde interesse |
| Checkout Initiators | 300+ | Bijna-kopers |
| App Installers (Active) | 500+ | Engaged users |

### Tier 3: Bruikbaar maar Minder Specifiek

| Source Type | Min. Grootte | Waarom Effectief |
|-------------|--------------|------------------|
| Website Visitors (30d) | 1000+ | Breed maar relevant |
| Video Viewers 95% | 1000+ | Hoge engagement |
| Page Engagers (90d) | 2000+ | Social interesse |
| Content Viewers | 1000+ | Topic interesse |

### Tier 4: Vermijden als Source

```
❌ NIET GEBRUIKEN ALS SOURCE:
├── Alle website bezoekers (te breed)
├── Video viewers <25% (lage kwaliteit)
├── Page likes alleen (passief)
├── Zeer oude data (>1 jaar)
└── Gemixte audiences (purchasers + browsers)
```

## Percentage Selectie Guide

### Percentage vs Bereik Trade-off

```
LOOKALIKE PERCENTAGE SPECTRUM
=============================

1%  ████                    ~200K-500K mensen
    └── Meest vergelijkbaar met source
    └── Beste voor: High-value producten, beperkt budget

2%  ████████                ~400K-1M mensen
    └── Goede balans kwaliteit/bereik
    └── Beste voor: Algemene prospecting

3%  ████████████            ~600K-1.5M mensen
    └── Breder bereik, nog steeds relevant
    └── Beste voor: Schaalbare campagnes

5%  ████████████████████    ~1M-2.5M mensen
    └── Groot bereik, meer variatie
    └── Beste voor: Awareness, grote budgetten

10% ████████████████████████████████████████  ~2M-5M mensen
    └── Zeer breed, beperkte gelijkenis
    └── Beste voor: Maximum bereik nodig
```

### Percentage Selectie Decision Tree

```
START: Welk percentage moet ik kiezen?
│
├─► Vraag 1: Wat is je dagbudget per ad set?
│   ├── <€20/dag → Gebruik 1-2%
│   ├── €20-50/dag → Gebruik 2-3%
│   ├── €50-100/dag → Gebruik 3-5%
│   └── >€100/dag → Gebruik 5-10%
│
├─► Vraag 2: Wat is je product type?
│   ├── High-ticket (>€200) → Gebruik 1-2%
│   ├── Mid-range (€50-200) → Gebruik 2-4%
│   └── Low-ticket (<€50) → Gebruik 3-6%
│
├─► Vraag 3: Wat is je campagne doel?
│   ├── Pure performance/ROAS → Gebruik 1-2%
│   ├── Gebalanceerde groei → Gebruik 2-4%
│   └── Scale/volume → Gebruik 4-6%
│
└─► RESULTAAT: Kies percentage op basis van overlap
```

## Geavanceerde Lookalike Strategieën

### Strategie 1: Value-Based Lookalikes

```
STAPPEN:
1. Maak Custom Audience van purchasers
2. Bij creatie: "Include LTV" of purchase value
3. Meta optimaliseert voor high-value matches

SETUP IN META:
├── Audiences → Create Audience → Custom Audience
├── Website → Purchase event
├── "Sort by value" of "Include value"
└── Create Lookalike van deze audience

RESULTAAT: LAL vindt mensen die lijken op je BESTE klanten
```

### Strategie 2: Layered Lookalikes

```
DOEL: Maximaal bereik zonder overlap

SETUP:
├── Ad Set 1: LAL 0-1% (meest waardevolle)
│   └── Budget: 40% van LAL budget
│
├── Ad Set 2: LAL 1-3%
│   └── Exclude: LAL 0-1%
│   └── Budget: 35% van LAL budget
│
└── Ad Set 3: LAL 3-5%
    └── Exclude: LAL 0-3%
    └── Budget: 25% van LAL budget

VOORDEEL: Test welke laag best presteert
```

### Strategie 3: Multi-Source Lookalikes

```
DOEL: Verschillende klantsegmenten bereiken

SETUP:
├── LAL 2%: Purchasers (alle kopers)
├── LAL 2%: High-AOV Customers (>€150 orders)
├── LAL 2%: Repeat Purchasers (2+ orders)
├── LAL 2%: Email Engagers (opens/clicks)
└── LAL 2%: Video Completers (95% viewed)

BELANGRIJK: Check overlap tussen deze LALs!
Vaak 20-40% overlap, gebruik exclusions indien nodig
```

### Strategie 4: Stacked Lookalikes

```
DOEL: Combineer meerdere high-intent sources

SETUP:
1. Maak Super Source Audience:
   ├── Purchasers (180d) +
   ├── Repeat Purchasers +
   ├── High-Value Customers +
   └── Active Email Subscribers

2. Maak LAL van gecombineerde audience

VOORDEEL: Grotere source = meer data voor algoritme
NADEEL: Kan signaal "verwateren" als sources te divers
```

## Lookalike Troubleshooting

### Probleem: LAL presteert slechter dan Interest audiences

```
MOGELIJKE OORZAKEN:
├── Source audience te klein (<500)
├── Source audience te oud (>180 dagen)
├── Source bevat lage-kwaliteit users
├── LAL percentage te breed voor budget
└── Learning phase niet voltooid

OPLOSSINGEN:
├── Upgrade naar Tier 1 source (purchasers)
├── Ververs source met recente data
├── Filter source op high-value alleen
├── Verlaag percentage (bijv. 3% → 1%)
└── Verhoog budget of consolideer ad sets
```

### Probleem: LAL heeft te weinig bereik

```
MOGELIJKE OORZAKEN:
├── Percentage te laag voor markt
├── Te veel exclusions actief
├── Geographic targeting te smal
└── Source te specifiek

OPLOSSINGEN:
├── Verhoog percentage (bijv. 1% → 3%)
├── Review en reduceer exclusions
├── Breid geo targeting uit
└── Combineer meerdere sources
```

### Probleem: LAL audience groeit niet

```
LOOKALIKE REFRESH CYCLUS:
├── Meta update LALs automatisch elke 3-7 dagen
├── Source audience moet blijven groeien
└── Stagnatie = source audience stagneert

ACTIE:
├── Check of source audience nog events ontvangt
├── Verifieer pixel/CAPI werkt correct
└── Overweeg bredere event als source
```

## Lookalike Creation Template

### Wanneer gebruiker vraagt om LAL strategie:

```
LOOKALIKE STRATEGIE TEMPLATE
============================

📊 ACCOUNT INFO:
├── Maandbudget: [BEDRAG]
├── Huidige purchasers: [AANTAL]
├── Product type: [TYPE]
└── Gemiddelde orderwaarde: [AOV]

🎯 AANBEVOLEN LOOKALIKES:

PRIMARY LAL (beste kans op conversie):
├── Source: [Purchasers 180d / High-Value]
├── Percentage: [1-2%]
├── Geschatte grootte: [XXX.XXX]
└── Budget allocatie: 40-50%

SECONDARY LAL (scale potentieel):
├── Source: [Add to Cart / Leads]
├── Percentage: [2-3%]
├── Geschatte grootte: [XXX.XXX]
└── Budget allocatie: 30-35%

TERTIARY LAL (bereik/awareness):
├── Source: [Engagers / Video Viewers]
├── Percentage: [3-5%]
├── Geschatte grootte: [XXX.XXX]
└── Budget allocatie: 15-25%

📋 EXCLUSIONS SETUP:
├── Alle LALs: Exclude purchasers (30d)
├── Secondary: Exclude Primary LAL
└── Tertiary: Exclude Primary + Secondary
```

## Source Audience Optimization

### Checklist voor Beste Source Quality

```
✅ SOURCE AUDIENCE CHECKLIST:

□ Minimaal 1000 mensen in source (ideaal 5000+)
□ Data is recent (laatste 180 dagen)
□ Gebaseerd op conversion events (niet pageviews)
□ Geografisch relevant voor target market
□ Bevat geen test/spam accounts
□ Value-based indien beschikbaar
□ Single intent (niet gemixed)
```

## Voorbeeld Interactie

**Gebruiker**: "Ik wil lookalike audiences opzetten maar weet niet welke source ik moet gebruiken. Ik heb ongeveer 2000 purchasers in de afgelopen 6 maanden."

**Claude response**:

"Met 2000 purchasers in 6 maanden heb je een uitstekende basis voor lookalikes! Hier is mijn aanbevolen strategie:

**Primaire Lookalike (hoogste prioriteit):**
- Source: Purchasers (180 dagen)
- Percentage: 1-2%
- Waarom: Je hebt voldoende data voor een sterk signaal

**Overweeg ook een Value-Based LAL:**
- Source: Top 20% klanten op orderwaarde
- Percentage: 1%
- Waarom: Vindt mensen die lijken op je BESTE klanten

**Vragen om te optimaliseren:**
1. Heb je toegang tot orderwaarde data in je pixel events?
2. Hoeveel repeat purchasers heb je (2+ orders)?
3. Wat is je dagbudget voor prospecting?

Met die info kan ik de percentages finetunen en een layered strategie uitwerken!"

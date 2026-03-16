---
name: audience-overlap-detector
description: Analyseer en detecteer audience overlap in Meta Ads campagnes om budget verspilling te voorkomen en auction competition te minimaliseren. Gebruik deze skill wanneer je overlap wilt identificeren, audiences wilt consolideren, of exclusion strategieën wilt opzetten.
---

# Audience Overlap Detector

## Overview

Deze skill helpt bij het identificeren van audience overlap in Meta Ads accounts, wat leidt tot interne competitie (zelf-bieden), hogere kosten en inconsistente delivery. Het biedt frameworks voor overlap analyse en oplossingsstrategieën.

## Waarom Overlap Problematisch Is

```
┌─────────────────────────────────────────────────────────────────┐
│  AUCTION DYNAMICS BIJ OVERLAP                                   │
│                                                                 │
│  Gebruiker "Anna" zit in:                                       │
│  ├── Ad Set A: Interest "Fitness"                               │
│  ├── Ad Set B: Lookalike 1% Purchasers                          │
│  └── Ad Set C: Website Visitors 30d                             │
│                                                                 │
│  Resultaat:                                                     │
│  ├── Je biedt 3x tegen jezelf voor dezelfde impressie           │
│  ├── CPM stijgt kunstmatig                                      │
│  ├── Budget wordt inefficiënt verdeeld                          │
│  └── Learning phase duurt langer (gesplitste data)              │
└─────────────────────────────────────────────────────────────────┘
```

## Overlap Check Methode

### Stap 1: Audience Overlap Tool (Meta)

```
Locatie: Ads Manager → Audiences → Select 2+ audiences →
         Actions → Show Audience Overlap

Interpretatie:
├── <10% overlap: Acceptabel, geen actie nodig
├── 10-30% overlap: Monitor, overweeg exclusions
├── 30-50% overlap: Problematisch, consolideer of exclude
└── >50% overlap: Kritiek, audiences samenvoegen
```

### Stap 2: Overlap Matrix Maken

Vraag de gebruiker om hun audiences te delen, en maak een matrix:

```
AUDIENCE OVERLAP MATRIX
=======================

              │ Broad │ LAL 1% │ LAL 3% │ Interest │ Retarg │
──────────────┼───────┼────────┼────────┼──────────┼────────┤
Broad         │   -   │  15%   │  25%   │   35%    │   5%   │
LAL 1%        │  15%  │   -    │  70%   │   20%    │  10%   │
LAL 3%        │  25%  │  70%   │   -    │   30%    │  15%   │
Interest      │  35%  │  20%   │  30%   │    -     │   8%   │
Retargeting   │   5%  │  10%   │  15%   │    8%    │   -    │

🔴 Kritiek: LAL 1% ↔ LAL 3% = 70% overlap
🟡 Waarschuwing: Broad ↔ Interest = 35% overlap
```

## Overlap Scenario's & Oplossingen

### Scenario 1: Lookalike Overlap

**Probleem**: LAL 1%, LAL 2%, LAL 3% draaien tegelijk

```
HUIDIGE SITUATIE:
├── Ad Set 1: LAL 1% Purchasers
├── Ad Set 2: LAL 2% Purchasers
└── Ad Set 3: LAL 3% Purchasers

OVERLAP: 60-80% tussen aangrenzende percentages

OPLOSSING A - Layered Lookalikes:
├── Ad Set 1: LAL 0-1%
├── Ad Set 2: LAL 1-3% (exclude 0-1%)
└── Ad Set 3: LAL 3-5% (exclude 0-3%)

OPLOSSING B - Consolidatie:
└── Ad Set 1: LAL 0-3% (één audience)

OPLOSSING C - Source Differentiatie:
├── Ad Set 1: LAL 1% van Purchasers
├── Ad Set 2: LAL 1% van High-Value Customers
└── Ad Set 3: LAL 1% van Email Subscribers
```

### Scenario 2: Interest vs Lookalike Overlap

**Probleem**: Interest audiences overlappen met lookalikes

```
HUIDIGE SITUATIE:
├── Ad Set 1: Interest "Luxury Fashion"
└── Ad Set 2: LAL 2% Purchasers (luxury items)

OVERLAP: 25-40% typisch

OPLOSSING A - Interest Exclusion:
├── Ad Set 1: Interest "Luxury Fashion"
│   └── EXCLUDE: LAL 2% Purchasers
└── Ad Set 2: LAL 2% Purchasers

OPLOSSING B - Broad Audience:
└── Ad Set 1: Advantage+ Audience
    └── Suggestie: Interest "Luxury Fashion"
    (Laat algoritme optimaliseren)
```

### Scenario 3: Retargeting Overlap

**Probleem**: Meerdere retargeting audiences overlappen

```
HUIDIGE SITUATIE:
├── Ad Set 1: All Website Visitors (30d)
├── Ad Set 2: Product Page Viewers (30d)
└── Ad Set 3: Add to Cart (14d)

OVERLAP: Product viewers EN ATC zitten ook in "All visitors"

OPLOSSING - Funnel Exclusions:
├── Ad Set 1: All Visitors (30d)
│   └── EXCLUDE: Product Viewers + ATC
├── Ad Set 2: Product Viewers (30d)
│   └── EXCLUDE: ATC
└── Ad Set 3: Add to Cart (14d)
    └── EXCLUDE: Purchasers (7d)
```

## Exclusion Strategy Framework

### Verticale Exclusions (Funnel-based)

```
TOFU CAMPAIGN
├── Target: Broad/Cold audiences
└── Exclude: All warm + hot audiences

MOFU CAMPAIGN
├── Target: Engagers, video viewers
└── Exclude: High-intent (ATC, IC) + purchasers

BOFU CAMPAIGN
├── Target: ATC, View Content, IC
└── Exclude: Recent purchasers (7-14d)
```

### Horizontale Exclusions (Binnen dezelfde fase)

```
Wanneer je meerdere ad sets in één campagne hebt:

Ad Set A: Interest Stack 1
└── Exclude: Custom Audience van Interest Stack 2

Ad Set B: Interest Stack 2
└── Exclude: Custom Audience van Interest Stack 1

OF gebruik Advantage Campaign Budget (CBO) om Meta
automatisch budget te verdelen zonder overlap issues
```

## Account Audit Checklist

### Vraag de gebruiker om deze info:

```
OVERLAP AUDIT VRAGENLIJST
=========================

1. AUDIENCE INVENTARIS
   □ Hoeveel actieve audiences heb je?
   □ Welke types? (LAL, Interest, Custom, Saved)
   □ Welke windows gebruik je voor retargeting?

2. CAMPAGNE STRUCTUUR
   □ Hoeveel campagnes draaien er simultaan?
   □ Gebruiken meerdere campagnes dezelfde audiences?
   □ Heb je exclusions ingesteld?

3. SIGNALEN VAN OVERLAP
   □ Fluctuerende delivery tussen ad sets?
   □ Onverwacht hoge CPM's?
   □ Ad sets die niet uit learning komen?
   □ Inconsistente resultaten bij gelijk budget?
```

## Overlap Diagnose Decision Tree

```
START: Vermoeden van overlap
│
├─► Check 1: Gebruik je LAL 1%, 2%, 3% tegelijk?
│   ├── JA → Consolideer of layer met exclusions
│   └── NEE → Ga naar Check 2
│
├─► Check 2: Draaien interest + LAL audiences tegelijk?
│   ├── JA → Check overlap %, exclude indien >20%
│   └── NEE → Ga naar Check 3
│
├─► Check 3: Heb je retargeting audiences zonder exclusions?
│   ├── JA → Implementeer funnel-based exclusions
│   └── NEE → Ga naar Check 4
│
├─► Check 4: Draaien meerdere campagnes op zelfde audiences?
│   ├── JA → Consolideer campagnes of splits audiences
│   └── NEE → Overlap waarschijnlijk niet het probleem
│
└─► RESULTAAT: Implementeer aanbevolen exclusion strategie
```

## Audience Consolidatie Gids

### Wanneer Consolideren?

| Situatie | Actie |
|----------|-------|
| 2+ ad sets met >50% overlap | Samenvoegen tot 1 ad set |
| LAL 1% + LAL 2% + LAL 3% | Gebruik LAL 0-3% of layer |
| 5+ interest ad sets | Consolideer tot 2-3 stacks |
| Meerdere retargeting windows | Gebruik langste window + exclusions |

### Consolidatie Template

```
VAN (gefragmenteerd):
├── Campaign 1
│   ├── Ad Set: LAL 1% - €20/dag
│   ├── Ad Set: LAL 2% - €20/dag
│   └── Ad Set: LAL 3% - €20/dag
└── Total: €60/dag, veel overlap

NAAR (geconsolideerd):
├── Campaign 1
│   ├── Ad Set: LAL 0-2% - €40/dag
│   └── Ad Set: LAL 2-5% - €20/dag (exclude 0-2%)
└── Total: €60/dag, minimale overlap
```

## Performance Impact Monitoring

### Metrics om te volgen na overlap fix:

```
VOOR/NA VERGELIJKING
====================

Metric              │ Voor Fix │ Na Fix │ Doel
────────────────────┼──────────┼────────┼─────────
CPM                 │  €12.50  │  €9.80 │ ↓ 15-25%
Frequency (7d)      │   4.2    │   2.8  │ ↓ naar <3
Delivery Stability  │  Volatiel│ Stabiel│ Consistent
Learning Phase Exit │  Traag   │ Sneller│ <7 dagen
Budget Spend Rate   │  Oneven  │  Even  │ Consistent
```

## Voorbeeld Interactie

**Gebruiker**: "Mijn CPM's zijn de laatste weken enorm gestegen en sommige ad sets krijgen nauwelijks delivery. Kan het aan overlap liggen?"

**Claude response**:

"Dat klinkt inderdaad als mogelijke audience overlap. Laten we het checken:

**Kun je me vertellen:**
1. Welke audiences draaien er momenteel actief?
2. Heb je recentelijk nieuwe ad sets toegevoegd?
3. Gebruik je meerdere Lookalike percentages (1%, 2%, 3%)?
4. Heb je exclusions ingesteld tussen je ad sets?

**Typische signalen van overlap:**
- ✅ Stijgende CPM's zonder externe reden
- ✅ Sommige ad sets krijgen geen delivery
- Ad sets blijven lang in learning phase
- Inconsistente kosten tussen vergelijkbare ad sets

Als je naar **Ads Manager → Audiences** gaat en 2 of meer audiences selecteert, kun je via **Actions → Show Audience Overlap** de exacte overlap zien.

Deel die percentages en ik help je met een oplossingsplan!"

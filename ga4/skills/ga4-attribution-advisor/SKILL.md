---
name: ga4-attribution-advisor
description: "GA4 attribution model advies en configuratie. Gebruik voor: (1) Kiezen tussen DDA, last-click, first-click, position-based, (2) Attribution model instellen per conversie, (3) Attribution windows configureren, (4) Cross-channel attribution analyseren, (5) Model comparisons uitvoeren. Triggers: attribution model, dda, last click, first click, linear attribution, conversie toewijzing, position based."
---

# GA4 Attribution Advisor

Complete gids voor het kiezen en configureren van het juiste attribution model in Google Analytics 4 voor accurate conversie-toewijzing.

## Quick Decision Tree

```
GA4 ATTRIBUTION MODEL SELECTIE
│
├─► WAT IS JE PRIMAIRE DOEL?
│   ├─► Maximale Smart Bidding performance
│   │   └─► DATA-DRIVEN ATTRIBUTION (DDA)
│   │       └─► Aanbevolen voor Google Ads
│   │
│   ├─► Eenvoudige, voorspelbare rapportage
│   │   └─► LAST CLICK
│   │       └─► Makkelijk uit te leggen aan stakeholders
│   │
│   ├─► Focus op awareness campagnes meten
│   │   └─► FIRST CLICK
│   │       └─► Waardeert top-of-funnel touchpoints
│   │
│   └─► Alle touchpoints gelijk waarderen
│       └─► LINEAR
│           └─► Eerlijke verdeling over journey
│
├─► HOEVEEL DATA HEB JE?
│   ├─► < 300 conversies/maand
│   │   └─► DDA niet beschikbaar
│   │   └─► Gebruik Position-Based of Last Click
│   │
│   └─► > 300 conversies/maand
│       └─► DDA aanbevolen
│       └─► Machine learning kan patronen vinden
│
└─► WELKE KANALEN GEBRUIK JE?
    ├─► Alleen Google Ads
    │   └─► DDA in Google Ads
    │   └─► Sync met GA4 voor consistentie
    │
    ├─► Google + Meta/LinkedIn/TikTok
    │   └─► GA4 DDA als single source of truth
    │   └─► Cross-channel comparison reports
    │
    └─► Complex multi-touch journey
        └─► DDA met Model Comparison tool
        └─► Analyseer touchpoint waarde
```

## Attribution Modellen Vergelijking

```
ATTRIBUTION MODELLEN OVERZICHT
==============================

┌─────────────────┬───────────────────────────────────────────────────────┐
│ Model           │ Hoe het werkt                                         │
├─────────────────┼───────────────────────────────────────────────────────┤
│ DATA-DRIVEN     │ Machine learning bepaalt credit op basis van          │
│ (DDA)           │ werkelijke conversiepatronen in jouw data             │
│                 │ ✅ Beste voor: Smart Bidding, Google Ads              │
│                 │ ⚠️ Vereist: 300+ conversies/maand                     │
├─────────────────┼───────────────────────────────────────────────────────┤
│ LAST CLICK      │ 100% credit naar laatste touchpoint                   │
│                 │ (excl. direct traffic)                                │
│                 │ ✅ Beste voor: Eenvoudige rapportage                  │
│                 │ ⚠️ Nadeel: Onderwaardeert upper funnel                │
├─────────────────┼───────────────────────────────────────────────────────┤
│ FIRST CLICK     │ 100% credit naar eerste touchpoint                    │
│                 │ ✅ Beste voor: Awareness campagne evaluatie           │
│                 │ ⚠️ Nadeel: Onderwaardeert converters                  │
├─────────────────┼───────────────────────────────────────────────────────┤
│ LINEAR          │ Gelijke credit verdeling over alle touchpoints        │
│                 │ ✅ Beste voor: Lange customer journeys                │
│                 │ ⚠️ Nadeel: Geen differentiatie in touchpoint impact   │
├─────────────────┼───────────────────────────────────────────────────────┤
│ POSITION-BASED  │ 40% first, 40% last, 20% verdeeld over midden         │
│                 │ ✅ Beste voor: Awareness + conversion focus           │
│                 │ ⚠️ Nadeel: Arbitraire verdeling                       │
├─────────────────┼───────────────────────────────────────────────────────┤
│ TIME DECAY      │ Meer credit naar recentere touchpoints                │
│                 │ ✅ Beste voor: Korte sales cycles                     │
│                 │ ⚠️ Nadeel: Onderwaardeert brand building              │
└─────────────────┴───────────────────────────────────────────────────────┘

VOORBEELD: Customer Journey met 4 touchpoints
─────────────────────────────────────────────
Touchpoints: Google Ads → Organic → Email → Direct → Conversie (€100)

Model vergelijking:
┌─────────────────┬───────────┬─────────┬─────────┬────────┐
│ Model           │ Google Ads│ Organic │ Email   │ Direct │
├─────────────────┼───────────┼─────────┼─────────┼────────┤
│ Last Click      │ €0        │ €0      │ €100    │ €0*    │
│ First Click     │ €100      │ €0      │ €0      │ €0     │
│ Linear          │ €33.33    │ €33.33  │ €33.33  │ €0     │
│ Position-Based  │ €40       │ €10     │ €50     │ €0     │
│ Time Decay      │ €10       │ €20     │ €70     │ €0     │
│ DDA             │ €35       │ €25     │ €40     │ €0     │
└─────────────────┴───────────┴─────────┴─────────┴────────┘
*Direct wordt meestal geëxcludeerd en toegewezen aan vorig touchpoint
```

## GA4 Attribution Configureren

```
ATTRIBUTION SETTINGS CONFIGUREREN
=================================

LOCATIE: Admin → Attribution Settings

STAP 1: REPORTING ATTRIBUTION MODEL
───────────────────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Ga naar Admin → Attribution Settings                      │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Onder "Reporting attribution model" selecteer:            │
│    │ • Data-driven (aanbevolen indien beschikbaar)             │
│    │ • Paid and organic last click                             │
│    │ • Google paid channels last click                         │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Kies "Acquisition conversion events" scope                │
│    │ (first user touchpoint vs session-based)                  │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Click "Save"                                              │
└────┴────────────────────────────────────────────────────────────┘

⚠️ BELANGRIJK:
├── Wijzigingen zijn NIET retroactief
├── Nieuwe model geldt vanaf moment van wijziging
├── Historische data behoudt oude attribution
└── Test eerst met Model Comparison tool

STAP 2: LOOKBACK WINDOWS
────────────────────────
┌────────────────────────┬────────────────────────────────────────┐
│ Setting                │ Aanbeveling                            │
├────────────────────────┼────────────────────────────────────────┤
│ Acquisition events     │ 30 dagen (default)                     │
│ lookback window        │ Verleng voor lange sales cycles        │
├────────────────────────┼────────────────────────────────────────┤
│ All other events       │ 90 dagen (default)                     │
│ lookback window        │ B2B: overweeg 90 dagen                 │
│                        │ E-commerce: 30 dagen vaak voldoende    │
├────────────────────────┼────────────────────────────────────────┤
│ Maximum                │ 90 dagen                               │
│                        │ GA360: tot 1 jaar mogelijk             │
└────────────────────────┴────────────────────────────────────────┘

LOOKBACK WINDOW PER INDUSTRIE:
├── E-commerce: 7-30 dagen (snelle beslissingen)
├── SaaS: 30-60 dagen (consideration phase)
├── B2B: 60-90 dagen (lange sales cycles)
├── Real estate: 90 dagen (zeer lange cycles)
└── Lead gen: 30-60 dagen (afhankelijk van product)
```

## Data-Driven Attribution (DDA)

```
DATA-DRIVEN ATTRIBUTION DETAILS
===============================

HOE DDA WERKT:
├── Analyseert alle customer journeys
├── Vergelijkt converting vs non-converting paths
├── Berekent incrementele waarde per touchpoint
├── Past machine learning toe op jouw specifieke data
└── Update continu op basis van nieuwe data

VEREISTEN VOOR DDA:
┌─────────────────────────┬──────────────────────────────────────┐
│ Requirement             │ Minimum                              │
├─────────────────────────┼──────────────────────────────────────┤
│ Conversies per maand    │ 300+ (per conversion event)          │
├─────────────────────────┼──────────────────────────────────────┤
│ Clicks/visits per maand │ 3,000+                               │
├─────────────────────────┼──────────────────────────────────────┤
│ Data history            │ Minimaal 28 dagen                    │
├─────────────────────────┼──────────────────────────────────────┤
│ Consent mode            │ Geen impact, werkt met modeled data  │
└─────────────────────────┴──────────────────────────────────────┘

DDA VERIFICATIE:
LOCATIE: Admin → Attribution Settings

Check beschikbaarheid:
├── Groen vinkje = DDA beschikbaar
├── Grijs/locked = Onvoldoende data
└── Tip: Check per conversion event

DDA VS GOOGLE ADS DDA:
──────────────────────
┌─────────────────────┬───────────────────┬───────────────────┐
│ Aspect              │ GA4 DDA           │ Google Ads DDA    │
├─────────────────────┼───────────────────┼───────────────────┤
│ Data scope          │ Alle kanalen      │ Alleen Google Ads │
├─────────────────────┼───────────────────┼───────────────────┤
│ Cross-device        │ Google Signals    │ Google accounts   │
├─────────────────────┼───────────────────┼───────────────────┤
│ Touchpoints         │ Web + App         │ Ads clicks only   │
├─────────────────────┼───────────────────┼───────────────────┤
│ Best for            │ Holistische view  │ Google Ads optim. │
└─────────────────────┴───────────────────┴───────────────────┘

⚠️ VERWACHT VERSCHILLEN:
├── GA4 en Google Ads DDA geven verschillende resultaten
├── Dit is NORMAAL (verschillende data scopes)
├── Kies één bron als "source of truth"
└── Document keuze voor stakeholders
```

## Model Comparison Analyse

```
MODEL COMPARISON TOOL
=====================

LOCATIE: Advertising → Attribution → Model Comparison

HOE TE GEBRUIKEN:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Selecteer date range (minimaal 28 dagen)                  │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Kies dimensie: Default Channel Group of Source/Medium     │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Selecteer twee modellen om te vergelijken                 │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Analyseer conversie en revenue verschillen                │
└────┴────────────────────────────────────────────────────────────┘

ANALYSE FRAMEWORK:
──────────────────

Vergelijk DDA vs Last Click:

┌─────────────────────┬────────────┬────────────┬─────────────────┐
│ Channel             │ DDA Conv.  │ LC Conv.   │ Verschil        │
├─────────────────────┼────────────┼────────────┼─────────────────┤
│ Paid Search         │ 120        │ 100        │ +20% (Upper)    │
│ Display             │ 45         │ 20         │ +125% (Intro)   │
│ Organic Search      │ 80         │ 95         │ -16% (Closer)   │
│ Email               │ 55         │ 85         │ -35% (Closer)   │
└─────────────────────┴────────────┴────────────┴─────────────────┘

INTERPRETATIE:
├── Kanaal krijgt MEER credit in DDA = sterke upper funnel rol
├── Kanaal krijgt MINDER credit in DDA = sterke closer rol
├── Grote verschillen = kanaal heeft specifieke journey positie
└── Kleine verschillen = consistent over hele journey

ACTIE MATRIX:
┌───────────────────────────┬────────────────────────────────────┐
│ Bevinding                 │ Actie                              │
├───────────────────────────┼────────────────────────────────────┤
│ Display: DDA >> LC        │ Verhoog Display budget             │
│ (onderwaardering in LC)   │ Awareness waarde is hoger          │
├───────────────────────────┼────────────────────────────────────┤
│ Email: DDA << LC          │ Email is sterke closer             │
│ (overwaardering in LC)    │ Invest in list growth              │
├───────────────────────────┼────────────────────────────────────┤
│ Paid Search: DDA ≈ LC     │ Consistent performer               │
│ (weinig verschil)         │ Stabiel kanaal, behoud budget      │
└───────────────────────────┴────────────────────────────────────┘
```

## Conversion Paths Analyse

```
CONVERSION PATH ANALYSIS
========================

LOCATIE: Advertising → Attribution → Conversion Paths

WAT JE LEERT:
├── Gemiddeld aantal touchpoints tot conversie
├── Meest voorkomende kanaal sequenties
├── Tijd tot conversie (days to convert)
└── Touchpoint patronen per segment

BELANGRIJKE METRICS:
┌─────────────────────────┬────────────────────────────────────────┐
│ Metric                  │ Wat het betekent                       │
├─────────────────────────┼────────────────────────────────────────┤
│ Avg. touchpoints        │ Gemiddelde journey lengte              │
│                         │ Lager = directe response               │
│                         │ Hoger = consideration needed           │
├─────────────────────────┼────────────────────────────────────────┤
│ Days to conversion      │ Typische sales cycle                   │
│                         │ Basis voor lookback window             │
├─────────────────────────┼────────────────────────────────────────┤
│ Early touchpoints       │ Awareness drivers                      │
│                         │ Vaak: Display, Video, Social           │
├─────────────────────────┼────────────────────────────────────────┤
│ Late touchpoints        │ Conversion drivers                     │
│                         │ Vaak: Brand Search, Email, Direct      │
└─────────────────────────┴────────────────────────────────────────┘

TYPISCHE CONVERSION PATHS:
──────────────────────────

E-commerce (korte cycle):
├── Display → Paid Search → Organic → Purchase
├── Social → Direct → Purchase
└── Avg: 2-3 touchpoints, 3-7 dagen

B2B SaaS (lange cycle):
├── Content → Paid Search → Demo Page → Email → Meeting → Sign-up
├── LinkedIn → Blog → Webinar → Sales Call → Contract
└── Avg: 5-8 touchpoints, 30-90 dagen

Lead Generation:
├── Paid Search → Landing → Email Nurture → Conversion
├── Display → Organic → Form Submit
└── Avg: 2-4 touchpoints, 7-21 dagen
```

## Troubleshooting Attribution

```
ATTRIBUTION TROUBLESHOOTING
===========================

PROBLEEM: DDA niet beschikbaar
──────────────────────────────
Oorzaken:
├── Minder dan 300 conversies/maand
├── Te weinig traffic volume
├── Nieuw property (< 28 dagen data)
└── Specifieke conversie heeft te weinig volume

Oplossing:
├── Wacht op meer data (minimaal 28 dagen)
├── Combineer micro-conversies tijdelijk
├── Gebruik Position-Based als alternatief
└── Focus op Last Click tot volume groeit

PROBLEEM: Attribution data verschilt van platform data
──────────────────────────────────────────────────────
Oorzaken:
├── Verschillende attribution windows
├── View-through vs click-through verschil
├── Cross-device tracking gaps
├── Consent mode impact
└── Platform-specific attribution (Meta, etc.)

Oplossing:
├── Document verwachte verschillen (10-30% normaal)
├── Kies één source of truth (meestal GA4)
├── Align lookback windows waar mogelijk
└── Accepteer dat platforms zichzelf over-attributen

PROBLEEM: Direct verkeer krijgt veel credit
───────────────────────────────────────────
Oorzaken:
├── Ontbrekende UTM parameters
├── JavaScript blocking
├── App traffic zonder tracking
├── Bookmarks en typed URLs
└── Dark social (gekopieerde links)

Oplossing:
├── Audit UTM implementation
├── Check cross-domain tracking
├── Implementeer link shorteners met tracking
└── Accepteer dat ~20% direct normaal is

PROBLEEM: Organic krijgt weinig credit in DDA
─────────────────────────────────────────────
Oorzaken:
├── Organic vaak in middle of journey
├── Brand searches geattribueerd aan andere touchpoints
├── Laatste click bias in veel journeys
└── DDA waardeert incrementele waarde

Oplossing:
├── Analyseer conversion paths voor organic rol
├── Split brand vs non-brand organic
├── Bekijk first-click model voor awareness waarde
└── Organic waarde is vaak hoger dan DDA toont
```

## Output: Attribution Analysis Template

```markdown
# GA4 Attribution Analyse Rapport

## Property & Period
- **Property:** [Property naam]
- **Analyse periode:** [Start] - [Eind]
- **Huidig attribution model:** [Model]
- **Lookback window:** [X] dagen

## Data Volume Check
| Metric | Waarde | DDA Requirement | Status |
|--------|--------|-----------------|--------|
| Conversies/maand | [X] | 300+ | ✅/❌ |
| Sessions/maand | [X] | 3,000+ | ✅/❌ |
| Data history | [X] dagen | 28+ | ✅/❌ |

## Model Comparison Results

### DDA vs Last Click Vergelijking
| Channel | DDA Conv. | LC Conv. | Verschil | Interpretatie |
|---------|-----------|----------|----------|---------------|
| Paid Search | [X] | [X] | [±X%] | [Upper/Lower funnel] |
| Display | [X] | [X] | [±X%] | [Upper/Lower funnel] |
| Organic | [X] | [X] | [±X%] | [Upper/Lower funnel] |
| Social | [X] | [X] | [±X%] | [Upper/Lower funnel] |
| Email | [X] | [X] | [±X%] | [Upper/Lower funnel] |

## Conversion Path Insights
- **Gem. touchpoints tot conversie:** [X]
- **Gem. dagen tot conversie:** [X]
- **Meest voorkomende path:** [Pad beschrijving]

## Attribution Model Aanbeveling

### Aanbevolen Model: [MODEL]

**Rationale:**
1. [Reden 1]
2. [Reden 2]
3. [Reden 3]

### Aanbevolen Lookback Window
- **Acquisition events:** [X] dagen
- **Other conversion events:** [X] dagen

## Budget Implicaties
| Channel | Huidige attributie | DDA attributie | Aanbevolen actie |
|---------|-------------------|----------------|------------------|
| [Channel] | [€X] | [€X] | [Verhoog/Verlaag/Behoud] |

## Volgende Stappen
1. [ ] Attribution model wijzigen naar [Model]
2. [ ] Lookback window aanpassen naar [X] dagen
3. [ ] Budget herallocation op basis van DDA insights
4. [ ] Maandelijkse model comparison review inplannen

## Notities
[Aanvullende observaties en aandachtspunten]
```

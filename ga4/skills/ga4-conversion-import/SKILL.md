---
name: ga4-conversion-import
description: "GA4 conversies importeren naar Google Ads voor Smart Bidding. Gebruik voor: (1) GA4 key events exporteren naar Google Ads, (2) Primary vs secondary conversions configureren, (3) Smart Bidding optimaliseren met GA4 data, (4) Conversion counting en waarde instellen, (5) Offline conversions importeren. Triggers: conversie import, ga4 naar google ads, smart bidding, key events, conversion tracking, pmax optimalisatie."
---

# GA4 Conversion Import Guide

Complete gids voor het importeren van GA4 conversies naar Google Ads voor optimale Smart Bidding performance.

## Quick Decision Tree

```
GA4 CONVERSIE IMPORT FLOW
│
├─► WELKE CONVERSIES IMPORTEREN?
│   ├─► Macro-conversies (hoofddoel)
│   │   └─► Purchase, Lead, Sign-up
│   │   └─► Als PRIMARY conversion importeren
│   │
│   ├─► Micro-conversies (stappen)
│   │   └─► Add to cart, Begin checkout, Form start
│   │   └─► Als SECONDARY conversion importeren
│   │
│   └─► Alle site engagement
│       └─► Page views, Scroll, Video views
│       └─► NIET importeren (noise voor bidding)
│
├─► SMART BIDDING STRATEGIE?
│   ├─► Target CPA / Maximize Conversions
│   │   └─► Import lead/purchase als primary
│   │   └─► Counting: One per click
│   │
│   ├─► Target ROAS / Maximize Conv. Value
│   │   └─► Import purchase met waarde
│   │   └─► Counting: Every conversion
│   │
│   └─► Performance Max
│       └─► Minimum 1 primary conversion
│       └─► Voeg micro-conversies als secondary
│       └─► Geef 30 dagen leertijd
│
└─► VOLUME CHECK
    ├─► < 30 conversies/maand per campagne
    │   └─► Voeg micro-conversies toe als primary
    │   └─► Of gebruik account-level bidding
    │
    └─► > 30 conversies/maand per campagne
        └─► Gebruik alleen macro-conversies als primary
        └─► Smart Bidding kan optimaliseren
```

## Google Ads Koppeling Verificatie

```
GOOGLE ADS LINK VERIFICATIE
===========================

STAP 1: CHECK GA4 KANT
LOCATIE: GA4 Admin → Product Links → Google Ads Links

┌─────────────────────┬────────────────────────────────────────┐
│ Check item          │ Verwachte status                       │
├─────────────────────┼────────────────────────────────────────┤
│ Link status         │ "Active"                               │
├─────────────────────┼────────────────────────────────────────┤
│ Personalized ads    │ Enabled (voor remarketing)             │
├─────────────────────┼────────────────────────────────────────┤
│ Auto-tagging        │ Enabled in Google Ads                  │
├─────────────────────┼────────────────────────────────────────┤
│ Linked accounts     │ Alle relevante Google Ads accounts     │
└─────────────────────┴────────────────────────────────────────┘

STAP 2: CHECK GOOGLE ADS KANT
LOCATIE: Google Ads → Tools → Data Manager → Google Analytics 4

┌─────────────────────┬────────────────────────────────────────┐
│ Check item          │ Verwachte status                       │
├─────────────────────┼────────────────────────────────────────┤
│ Property status     │ "Linked"                               │
├─────────────────────┼────────────────────────────────────────┤
│ Data sharing        │ Enabled                                │
├─────────────────────┼────────────────────────────────────────┤
│ Import status       │ "Active" per conversie                 │
└─────────────────────┴────────────────────────────────────────┘

⚠️ TROUBLESHOOTING LINK ISSUES:
├── Link niet zichtbaar? Check permissions beide platforms
├── Status "Error"? Unlink en re-link
├── Data mismatch? Check auto-tagging is ON
└── Geen import opties? Wacht 24-48 uur na linking
```

## GA4 Key Events Configureren

```
GA4 KEY EVENTS (CONVERSIES) SETUP
=================================

LOCATIE: GA4 Admin → Data display → Events → Mark as key event

STAP 1: IDENTIFICEER KEY EVENTS
───────────────────────────────
┌─────────────────────┬───────────┬───────────────────────────────┐
│ Event type          │ Priority  │ Import als                    │
├─────────────────────┼───────────┼───────────────────────────────┤
│ purchase            │ HIGH      │ Primary - Every conversion    │
├─────────────────────┼───────────┼───────────────────────────────┤
│ generate_lead       │ HIGH      │ Primary - One per click       │
├─────────────────────┼───────────┼───────────────────────────────┤
│ sign_up             │ HIGH      │ Primary - One per click       │
├─────────────────────┼───────────┼───────────────────────────────┤
│ begin_checkout      │ MEDIUM    │ Secondary observation only    │
├─────────────────────┼───────────┼───────────────────────────────┤
│ add_to_cart         │ MEDIUM    │ Secondary observation only    │
├─────────────────────┼───────────┼───────────────────────────────┤
│ page_view           │ LOW       │ Niet importeren               │
├─────────────────────┼───────────┼───────────────────────────────┤
│ scroll              │ LOW       │ Niet importeren               │
└─────────────────────┴───────────┴───────────────────────────────┘

STAP 2: MARKEER ALS KEY EVENT
─────────────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Ga naar Admin → Data display → Events                     │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Vind je event in de lijst                                 │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Toggle "Mark as key event" → ON                           │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Event verschijnt nu in Admin → Key events                 │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Wacht 24-48 uur voor import beschikbaarheid               │
└────┴────────────────────────────────────────────────────────────┘

⚠️ KEY EVENT LIMIETEN:
├── Maximum 30 key events per property
├── Selecteer alleen events met business waarde
├── Avoid marking page_view of scroll als key event
└── Custom events moeten eerst data hebben
```

## Conversies Importeren in Google Ads

```
GOOGLE ADS IMPORT STAPPEN
=========================

LOCATIE: Google Ads → Goals → Conversions → New conversion action

STAP 1: START IMPORT
────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Click "+ New conversion action"                           │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Selecteer "Import"                                        │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Kies "Google Analytics 4 properties"                      │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Selecteer "Web" of "App" (match je data stream)           │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Click "Continue"                                          │
└────┴────────────────────────────────────────────────────────────┘

STAP 2: SELECTEER CONVERSIES
────────────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Vink de key events aan die je wilt importeren             │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Check dat elke conversie minimaal 1 event heeft           │
│    │ (anders niet importeerbaar)                               │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click "Import and continue"                               │
└────┴────────────────────────────────────────────────────────────┘

STAP 3: CONFIGUREER ELKE CONVERSIE
──────────────────────────────────
Voor ELKE geïmporteerde conversie, configureer:

┌─────────────────────┬────────────────────────────────────────────┐
│ Setting             │ Aanbeveling per type                       │
├─────────────────────┼────────────────────────────────────────────┤
│ Goal and action     │ Kies meest passende categorie              │
│ optimization        │ (Purchase, Lead, Sign-up, etc.)            │
├─────────────────────┼────────────────────────────────────────────┤
│ Conversion name     │ Prefix met "GA4 - " voor herkenbaarheid    │
│                     │ Bijv: "GA4 - Purchase"                     │
├─────────────────────┼────────────────────────────────────────────┤
│ Value               │ • E-commerce: "Use different values"       │
│                     │ • Leads: "Use same value" + vul in         │
│                     │ • Let op: GA4 stuurt value mee             │
├─────────────────────┼────────────────────────────────────────────┤
│ Count               │ • Purchase: "Every"                        │
│                     │ • Lead/Sign-up: "One"                      │
├─────────────────────┼────────────────────────────────────────────┤
│ Click-through       │ 30-90 dagen (match je sales cycle)         │
│ window              │                                            │
├─────────────────────┼────────────────────────────────────────────┤
│ View-through        │ 1-7 dagen (conservatief)                   │
│ window              │ Display/Video: 7 dagen                     │
├─────────────────────┼────────────────────────────────────────────┤
│ Attribution model   │ Data-driven (aanbevolen)                   │
│                     │ Sync met GA4 model indien mogelijk         │
└─────────────────────┴────────────────────────────────────────────┘
```

## Primary vs Secondary Conversions

```
PRIMARY VS SECONDARY CONVERSIONS
================================

DEFINITIE:
├── PRIMARY: Gebruikt voor Smart Bidding optimalisatie
├── SECONDARY: Alleen voor observation/reporting
└── Account default: Nieuwe imports zijn secondary

LOCATIE: Google Ads → Goals → Conversions → [Conversie] → Edit goal

┌─────────────────────┬───────────────────┬───────────────────────┐
│ Conversion type     │ Primary/Secondary │ Rationale             │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Purchase            │ PRIMARY           │ Hoofddoel e-commerce  │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Generate Lead       │ PRIMARY           │ Hoofddoel lead gen    │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Sign Up             │ PRIMARY           │ Hoofddoel SaaS        │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Phone Call (60s+)   │ PRIMARY           │ Gekwalificeerde call  │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Begin Checkout      │ SECONDARY         │ Micro-conversie       │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Add to Cart         │ SECONDARY         │ Micro-conversie       │
├─────────────────────┼───────────────────┼───────────────────────┤
│ Contact Form View   │ SECONDARY         │ Te vroeg in funnel    │
├─────────────────────┼───────────────────┼───────────────────────┤
│ PDF Download        │ SECONDARY         │ Soft conversie        │
└─────────────────────┴───────────────────┴───────────────────────┘

CONFIGUREN PRIMARY CONVERSION:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Ga naar Goals → Conversions → Summary                     │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Click op de conversie naam                                │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click "Edit goal"                                         │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Bij "Goal and action optimization":                       │
│    │ • Primary: "Use as primary action for bidding"            │
│    │ • Secondary: "Use as secondary action (observe only)"     │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Save                                                      │
└────┴────────────────────────────────────────────────────────────┘

⚠️ BELANGRIJKE REGELS:
├── Maximum 1-3 primary conversions (focus bidding)
├── Avoid conflicting primary conversions (lead + purchase)
├── PMax vereist minimaal 1 primary conversion
├── Te veel primary = verwarrende bidding signals
└── Secondary conversions zijn nog steeds waardevol voor analyse
```

## Smart Bidding Optimalisatie

```
SMART BIDDING MET GA4 CONVERSIES
================================

MINIMUM VOLUME REQUIREMENTS:
┌─────────────────────────────┬─────────────────────────────────┐
│ Bidding Strategy            │ Minimum conversies              │
├─────────────────────────────┼─────────────────────────────────┤
│ Maximize Conversions        │ 15/maand per campagne           │
├─────────────────────────────┼─────────────────────────────────┤
│ Target CPA                  │ 30/maand per campagne           │
├─────────────────────────────┼─────────────────────────────────┤
│ Target ROAS                 │ 50/maand per campagne           │
│                             │ (met revenue waarde)            │
├─────────────────────────────┼─────────────────────────────────┤
│ Performance Max             │ 30/maand per account            │
└─────────────────────────────┴─────────────────────────────────┘

LEARNING PERIOD:
├── Nieuwe conversie import: 7-14 dagen
├── Significant wijzigingen: 7 dagen
├── Vermijd grote wijzigingen tijdens learning
└── Check "Learning" status in campagne overview

CONVERSION LAG INSTELLEN:
─────────────────────────
LOCATIE: Goals → Conversions → Settings → Conversion window

┌─────────────────────┬────────────────────┬───────────────────┐
│ Business type       │ Click-through      │ View-through      │
├─────────────────────┼────────────────────┼───────────────────┤
│ E-commerce          │ 30 dagen           │ 1 dag             │
├─────────────────────┼────────────────────┼───────────────────┤
│ Lead generation     │ 30-60 dagen        │ 1-7 dagen         │
├─────────────────────┼────────────────────┼───────────────────┤
│ B2B SaaS            │ 60-90 dagen        │ 7 dagen           │
├─────────────────────┼────────────────────┼───────────────────┤
│ High-value purchase │ 90 dagen           │ 7 dagen           │
└─────────────────────┴────────────────────┴───────────────────┘

⚠️ REPORTING VERTRAGING:
├── GA4 naar Google Ads sync: tot 24 uur
├── Conversion reporting: tot 48 uur
├── Attribution updates: tot 7 dagen
└── Plan je analyses met deze vertragingen
```

## Conversion Value Optimalisatie

```
CONVERSION VALUE CONFIGURATIE
=============================

WANNEER VALUE GEBRUIKEN:
├── E-commerce: altijd (transactie waarde)
├── Lead gen: vaste waarde per lead type
├── SaaS: trial value of LTV-based
└── B2B: deal waarde indien bekend

GA4 VALUE DOORSTUREN:
─────────────────────
GA4 event met value parameter:

gtag('event', 'purchase', {
  'value': 150.00,
  'currency': 'EUR'
});

gtag('event', 'generate_lead', {
  'value': 50.00,     // geschatte lead waarde
  'currency': 'EUR'
});

GOOGLE ADS VALUE SETTINGS:
┌─────────────────────┬────────────────────────────────────────────┐
│ Setting             │ Wanneer gebruiken                          │
├─────────────────────┼────────────────────────────────────────────┤
│ Use different       │ E-commerce (variabele order values)        │
│ values for each     │ GA4 stuurt value automatisch mee           │
├─────────────────────┼────────────────────────────────────────────┤
│ Use same value      │ Lead gen (vaste waarde)                    │
│ for each            │ Vul geschatte waarde in                    │
├─────────────────────┼────────────────────────────────────────────┤
│ Don't use value     │ Alleen voor observation conversions        │
│                     │ Niet aanbevolen voor primary               │
└─────────────────────┴────────────────────────────────────────────┘

LEAD VALUE BEREKENING:
──────────────────────
Formule: Lead Value = (Close Rate × Avg. Deal Size)

Voorbeeld:
├── Close rate: 10%
├── Avg. deal size: €1,000
├── Lead value: 0.10 × €1,000 = €100 per lead

Lead type tiers:
┌─────────────────────┬────────────┬───────────────────────────────┐
│ Lead Type           │ Value      │ Rationale                     │
├─────────────────────┼────────────┼───────────────────────────────┤
│ Demo request        │ €150       │ High intent, warme lead       │
├─────────────────────┼────────────┼───────────────────────────────┤
│ Contact form        │ €75        │ Medium intent                 │
├─────────────────────┼────────────┼───────────────────────────────┤
│ Newsletter signup   │ €10        │ Low intent, nurture needed    │
├─────────────────────┼────────────┼───────────────────────────────┤
│ Whitepaper download │ €25        │ Research phase                │
└─────────────────────┴────────────┴───────────────────────────────┘
```

## Troubleshooting Conversion Import

```
CONVERSION IMPORT TROUBLESHOOTING
=================================

PROBLEEM: Conversies niet zichtbaar voor import
───────────────────────────────────────────────
Oorzaken:
├── Event niet gemarkeerd als key event in GA4
├── Key event heeft 0 events (geen data)
├── Google Ads link niet actief
├── Wachttijd na marking (24-48 uur)
└── Permissions issue (geen admin access)

Oplossing:
├── Check GA4: Admin → Key events → is event listed?
├── Check GA4: Events → heeft event data afgelopen 7 dagen?
├── Check link: Admin → Product Links → Google Ads
├── Wacht 24-48 uur na nieuwe key event marking
└── Verify je hebt admin access op beide platforms

PROBLEEM: Conversion data mismatch GA4 vs Google Ads
────────────────────────────────────────────────────
Oorzaken:
├── Verschillende attribution modellen
├── Verschillende conversion windows
├── Counting method verschil (one vs every)
├── Timezone verschil
└── Data import vertraging

Verwachte verschillen:
├── 5-15% verschil is NORMAAL
├── > 20% verschil = investigate

Oplossing:
├── Sync attribution models waar mogelijk
├── Match conversion windows
├── Document verwachte discrepancy
└── Kies één source of truth

PROBLEEM: Smart Bidding levert geen resultaten
──────────────────────────────────────────────
Oorzaken:
├── Onvoldoende conversie volume
├── Te kort learning period
├── Conflicting primary conversions
├── Conversion lag niet ingesteld
└── Budget te laag voor doel

Oplossing:
├── Check minimum volumes (30/maand voor tCPA)
├── Geef 2-4 weken learning time
├── Gebruik max 1-2 primary conversions
├── Pas targets aan naar realistisch niveau
└── Voeg micro-conversies toe als volume te laag

PROBLEEM: GA4 conversies stoppen met importeren
───────────────────────────────────────────────
Oorzaken:
├── Google Ads link verbroken
├── GA4 property permissions gewijzigd
├── Key event unmarked in GA4
├── Data stream issues
└── Consent mode blocking

Oplossing:
├── Re-check en re-link indien nodig
├── Verify permissions op beide platforms
├── Check key event status in GA4
├── Test met GA4 DebugView
└── Review consent mode implementation
```

## Output: Conversion Import Checklist Template

```markdown
# GA4 Conversie Import Rapport

## Account Informatie
- **GA4 Property:** [Property naam]
- **Measurement ID:** G-XXXXXXXXXX
- **Google Ads Account:** XXX-XXX-XXXX
- **Link Status:** ✅ Active / ❌ Not linked

## Key Events Status (GA4)
| Event Name | Key Event | Volume (30d) | Import Status |
|------------|-----------|--------------|---------------|
| purchase | ✅ | [X] | ✅ Imported |
| generate_lead | ✅ | [X] | ✅ Imported |
| begin_checkout | ❌ | [X] | Secondary only |
| add_to_cart | ❌ | [X] | Not imported |

## Google Ads Conversion Configuratie
| Conversion | Goal Type | Count | Value | Attribution | Primary/Sec |
|------------|-----------|-------|-------|-------------|-------------|
| GA4 - Purchase | Purchase | Every | Dynamic | DDA | Primary |
| GA4 - Lead | Lead | One | €100 | DDA | Primary |
| GA4 - Checkout | Add to cart | Every | - | DDA | Secondary |

## Conversion Windows
| Conversion | Click-through | View-through | Rationale |
|------------|---------------|--------------|-----------|
| Purchase | 30 dagen | 1 dag | E-commerce standaard |
| Lead | 60 dagen | 7 dagen | Lange consideration |

## Smart Bidding Readiness
| Check | Status | Details |
|-------|--------|---------|
| Minimum volume (30/mo) | ✅/❌ | [X] conversies |
| Single primary focus | ✅/❌ | [X] primary conversions |
| Value tracking | ✅/❌ | [Dynamic/Fixed/None] |
| Learning period | ✅/❌ | [X] dagen actief |

## Volume Analyse
- **Conversies afgelopen 30 dagen:** [X]
- **Verwacht volume komende 30 dagen:** [X]
- **Geschikt voor Smart Bidding:** ✅/❌

## Aanbevelingen

### Immediate Actions
1. [ ] [Actie 1]
2. [ ] [Actie 2]

### Optimalisatie Suggesties
1. [ ] [Suggestie 1]
2. [ ] [Suggestie 2]

## Data Sync Verificatie
- **Laatste GA4 → Google Ads sync:** [Datum/tijd]
- **Data lag:** [X] uur
- **Discrepancy percentage:** [X]% (target: < 15%)

## Notities
[Aanvullende observaties, afwijkingen, of speciale configuraties]
```

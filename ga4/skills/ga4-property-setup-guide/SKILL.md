---
name: ga4-property-setup-guide
description: "Google Analytics 4 property setup en configuratie gids. Gebruik voor: (1) Nieuwe GA4 property aanmaken en configureren, (2) Data streams instellen voor web en app, (3) Enhanced Measurement configureren, (4) Data retention en privacy settings, (5) Google Ads en Search Console koppelen. Triggers: ga4 setup, property configuratie, data stream, enhanced measurement, ga4 installatie, analytics setup."
---

# GA4 Property Setup Guide

Complete gids voor het correct opzetten en configureren van een Google Analytics 4 property voor adverteerders en agencies.

## Quick Decision Tree

```
GA4 PROPERTY SETUP FLOW
│
├─► NIEUWE PROPERTY NODIG?
│   ├─► JA, geen GA4 property
│   │   └─► Stap 1: Property aanmaken in Admin
│   │       └─► Stap 2: Data Stream toevoegen
│   │           └─► Stap 3: Tag implementeren
│   │
│   └─► NEE, bestaande property optimaliseren
│       └─► Ga naar "Property Audit Checklist"
│
├─► WELK TYPE DATA STREAM?
│   ├─► Website only
│   │   └─► Web Data Stream + GTM of gtag.js
│   │
│   ├─► App only (iOS/Android)
│   │   └─► Firebase SDK integratie
│   │
│   └─► Website + App
│       └─► Meerdere streams, 1 property
│       └─► Cross-platform user tracking
│
└─► ADVERTISING USE CASE?
    ├─► Google Ads optimalisatie
    │   └─► Link Google Ads account
    │   └─► Enable Google Signals
    │
    └─► Multi-platform advertising
        └─► Correcte UTM setup
        └─► Cross-domain tracking indien nodig
```

## Property Setup Stappen

### Stap 1: Property Aanmaken

```
GA4 PROPERTY AANMAKEN
=====================

LOCATIE: admin.google.com → Admin → Create Property

VEREISTE INFORMATIE:
┌─────────────────────┬────────────────────────────────────────┐
│ Veld                │ Aanbeveling                            │
├─────────────────────┼────────────────────────────────────────┤
│ Property name       │ [Brand] - [Environment]                │
│                     │ Voorbeeld: "Acme Corp - Production"    │
├─────────────────────┼────────────────────────────────────────┤
│ Reporting timezone  │ Kies lokale timezone van business      │
│                     │ (belangrijk voor reports!)             │
├─────────────────────┼────────────────────────────────────────┤
│ Currency            │ Kies valuta van business               │
│                     │ (belangrijk voor revenue tracking!)    │
├─────────────────────┼────────────────────────────────────────┤
│ Industry category   │ Selecteer meest passende categorie     │
│                     │ (gebruikt voor benchmarking)           │
├─────────────────────┼────────────────────────────────────────┤
│ Business size       │ Aantal employees (voor benchmarks)     │
└─────────────────────┴────────────────────────────────────────┘

⚠️ BELANGRIJK:
├── Timezone en currency KUNNEN later niet makkelijk wijzigen
├── Kies ALTIJD production timezone, niet UTC
└── Eén property per brand/business (niet per domein)
```

### Stap 2: Data Stream Configureren

```
WEB DATA STREAM SETUP
=====================

LOCATIE: Admin → Data Streams → Add Stream → Web

CONFIGURATIE:
┌─────────────────────┬────────────────────────────────────────┐
│ Veld                │ Aanbeveling                            │
├─────────────────────┼────────────────────────────────────────┤
│ Website URL         │ Primaire domein (zonder www)           │
│                     │ Voorbeeld: example.com                 │
├─────────────────────┼────────────────────────────────────────┤
│ Stream name         │ "Web - [domein]"                       │
│                     │ Voorbeeld: "Web - example.com"         │
├─────────────────────┼────────────────────────────────────────┤
│ Enhanced            │ AAN (altijd aanzetten!)                │
│ Measurement         │ Fine-tune specifieke events            │
└─────────────────────┴────────────────────────────────────────┘

MEASUREMENT ID FORMAT:
├── G-XXXXXXXXXX (Web streams)
├── Dit ID gebruik je in GTM of gtag.js
└── Bewaar dit ID veilig
```

### Stap 3: Enhanced Measurement Configureren

```
ENHANCED MEASUREMENT EVENTS
===========================

LOCATIE: Data Stream → Enhanced measurement → Settings icon

┌───────────────────────┬────────┬────────────────────────────────┐
│ Event                 │ Status │ Notities                       │
├───────────────────────┼────────┼────────────────────────────────┤
│ Page views            │ ✅ AAN │ Altijd aan, basis tracking     │
├───────────────────────┼────────┼────────────────────────────────┤
│ Scrolls               │ ✅ AAN │ 90% scroll depth trigger       │
├───────────────────────┼────────┼────────────────────────────────┤
│ Outbound clicks       │ ✅ AAN │ Clicks naar externe domeinen   │
├───────────────────────┼────────┼────────────────────────────────┤
│ Site search           │ ✅ AAN │ Configureer search parameter   │
│                       │        │ (meestal: q, s, search, query) │
├───────────────────────┼────────┼────────────────────────────────┤
│ Video engagement      │ ✅ AAN │ YouTube embeds automatisch     │
├───────────────────────┼────────┼────────────────────────────────┤
│ File downloads        │ ✅ AAN │ PDF, docx, xlsx, etc.          │
├───────────────────────┼────────┼────────────────────────────────┤
│ Form interactions     │ ⚠️     │ Test eerst! Kan dubbel tellen  │
│                       │        │ met custom form tracking       │
└───────────────────────┴────────┴────────────────────────────────┘

SITE SEARCH PARAMETER CONFIGURATIE:
────────────────────────────────────
1. Check huidige zoek-URL: example.com/search?q=term
2. Identificeer parameter: "q"
3. Vul in bij Enhanced Measurement → Site search
4. Test met DebugView

VEELVOORKOMENDE SEARCH PARAMETERS:
├── q (Google default)
├── s (WordPress default)
├── search
├── query
├── keyword
└── term
```

## Google Signals Configureren

```
GOOGLE SIGNALS SETUP
====================

WAT IS HET:
├── Cross-device tracking via Google accounts
├── Vereist voor remarketing audiences
├── Demografische data in reports
└── Enhanced conversions support

LOCATIE: Admin → Data Settings → Data Collection

SETUP STAPPEN:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Ga naar Admin → Data Settings → Data Collection           │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Click "Get Started" bij Google signals data collection    │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Review en Accept de data collection terms                 │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Toggle "Enable Google signals data collection" → ON       │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Kies regio's (meestal "All regions")                      │
└────┴────────────────────────────────────────────────────────────┘

⚠️ PRIVACY OVERWEGINGEN:
├── Data thresholding kan reports beperken bij laag volume
├── Vereist cookie consent in EU (GDPR)
├── Niet beschikbaar voor alle gebruikers (opt-in required)
└── Kan data sampling verhogen bij hoog volume
```

## Data Retention Configureren

```
DATA RETENTION SETTINGS
=======================

LOCATIE: Admin → Data Settings → Data Retention

OPTIES:
┌───────────────────┬────────────────────────────────────────────┐
│ Setting           │ Aanbeveling                                │
├───────────────────┼────────────────────────────────────────────┤
│ Event data        │ 14 maanden (maximum voor gratis)           │
│ retention         │ GA360: tot 50 maanden                      │
├───────────────────┼────────────────────────────────────────────┤
│ User data         │ 14 maanden (maximum voor gratis)           │
│ retention         │ Bevat user-level dimensions                │
├───────────────────┼────────────────────────────────────────────┤
│ Reset user data   │ AAN - reset bij nieuwe activiteit          │
│ on new activity   │ Houdt actieve users langer                 │
└───────────────────┴────────────────────────────────────────────┘

⚠️ BELANGRIJK:
├── Aggregated data (reports) blijft altijd beschikbaar
├── Retention geldt voor user-level en event-level data
├── Explorations kunnen beperkt worden na expiry
└── BigQuery export is niet affected (als geconfigureerd)
```

## Google Ads Koppeling

```
GOOGLE ADS LINKING
==================

WAAROM KOPPELEN:
├── Importeer GA4 conversies naar Google Ads
├── Bouw remarketing audiences in GA4
├── Zie Google Ads data in GA4 reports
├── Enable cross-platform attribution
└── Smart Bidding optimalisatie met GA4 data

LOCATIE: Admin → Product Links → Google Ads Links

SETUP STAPPEN:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Click "Link" → Selecteer Google Ads account(s)            │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Enable "Personalized advertising" (voor remarketing)      │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Enable auto-tagging in Google Ads (aanbevolen)            │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Click "Submit" → Link is nu actief                        │
└────┴────────────────────────────────────────────────────────────┘

VERIFICATIE:
├── GA4: Admin → Product Links → Google Ads Links → Status "Active"
├── Google Ads: Tools → Linked accounts → Google Analytics
└── Test: Acquisition report moet Google Ads data tonen

AUTO-TAGGING VS UTM:
────────────────────
✅ AUTO-TAGGING (Aanbevolen):
├── Automatisch door Google Ads
├── Nauwkeuriger dan UTM
├── Nodig voor RLSA en remarketing
└── gclid parameter automatisch toegevoegd

⚠️ UTM TOEVOEGEN:
├── Alleen nodig als auto-tagging problemen geeft
├── Of voor third-party tracking naast GA4
└── Nooit UTM + auto-tagging duplicate data
```

## Search Console Koppeling

```
SEARCH CONSOLE LINKING
======================

WAAROM KOPPELEN:
├── Zie organic search queries in GA4
├── Landing page performance data
├── Search impressions en CTR
└── SEO ↔ Analytics alignment

LOCATIE: Admin → Product Links → Search Console Links

VEREISTEN:
├── Verified Search Console property
├── Property owner of full user access
└── Zelfde Google account als GA4 admin

SETUP STAPPEN:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Click "Link" → Selecteer Search Console property          │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Match web stream met Search Console property              │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click "Submit"                                            │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Data verschijnt binnen 48 uur                             │
└────┴────────────────────────────────────────────────────────────┘

DATA BESCHIKBAAR NA KOPPELING:
├── Reports → Search Console → Queries
├── Reports → Search Console → Google organic search traffic
└── Explorations met Search Console dimensions
```

## Cross-Domain Tracking

```
CROSS-DOMAIN TRACKING SETUP
===========================

WANNEER NODIG:
├── Checkout op ander domein (shop.brand.com → checkout.provider.com)
├── Subdomeinen die apart moeten worden getrackt
├── Multi-brand sites met gedeelde cart
└── Third-party booking/payment systems

LOCATIE: Data Stream → Configure tag settings → Configure your domains

SETUP:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Ga naar Admin → Data Streams → [je stream]                │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Click "Configure tag settings"                            │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click "Configure your domains"                            │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Add alle domeinen die gelinkt moeten worden               │
│    │ Match type: "Contains" meestal voldoende                  │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Save en test met DebugView                                │
└────┴────────────────────────────────────────────────────────────┘

VOORBEELD CONFIGURATIE:
├── Domein 1: example.com (Contains)
├── Domein 2: checkout.example-pay.com (Contains)
└── Domein 3: shop.example.nl (Contains)

VERIFICATIE:
├── Ga naar domein A → click link naar domein B
├── Check URL: moet _gl parameter bevatten
├── Check DebugView: session moet doorlopen
└── Check reports: geen session breaks
```

## Property Audit Checklist

```
GA4 PROPERTY AUDIT CHECKLIST
============================

□ PROPERTY SETTINGS
├── □ Correct timezone ingesteld
├── □ Correct currency ingesteld
├── □ Industry category geselecteerd
└── □ Property name is duidelijk

□ DATA STREAMS
├── □ Web stream actief
├── □ Measurement ID correct geïmplementeerd
├── □ Enhanced Measurement geconfigureerd
├── □ Site search parameter correct
└── □ Cross-domain tracking (indien nodig)

□ DATA COLLECTION
├── □ Google Signals enabled (voor remarketing)
├── □ Data retention op 14 maanden
├── □ User data reset on activity: ON
└── □ Consent mode geïmplementeerd (EU)

□ PRODUCT LINKS
├── □ Google Ads gekoppeld
├── □ Search Console gekoppeld
├── □ BigQuery export (optioneel)
└── □ Andere producten (Merchant Center, etc.)

□ ACCESS & PERMISSIONS
├── □ Juiste users met juiste rollen
├── □ Admin access beperkt
├── □ Service accounts gedocumenteerd
└── □ Audit log reviewen

□ KEY EVENTS (CONVERSIONS)
├── □ Belangrijkste conversies ingesteld
├── □ Conversies getest in DebugView
├── □ Geen duplicate conversies
└── □ Primary conversions gemarkeerd

□ AUDIENCES
├── □ Basis audiences aangemaakt
├── □ Remarketing audiences voor Google Ads
└── □ Predictive audiences (indien eligible)
```

## Veelvoorkomende Problemen

```
TROUBLESHOOTING GUIDE
=====================

PROBLEEM: Geen data in GA4
──────────────────────────
Oorzaken:
├── Tag niet correct geïmplementeerd
├── Verkeerde Measurement ID
├── Ad blocker tijdens testen
├── Consent mode blokkeert tracking
└── Data vertraging (tot 24-48 uur)

Oplossing:
├── Check met GA Debugger browser extension
├── Gebruik DebugView in GA4
├── Verify tag fires in GTM Preview mode
└── Test in Incognito zonder ad blocker

PROBLEEM: Data discrepancies met Google Ads
───────────────────────────────────────────
Oorzaken:
├── Verschillende attribution modellen
├── Conversion counting verschil (one per click vs many)
├── Cross-device tracking gaps
├── Consent mode differences
└── Timezone mismatches

Oplossing:
├── Align attribution windows
├── Document expected differences (5-15% normaal)
├── Use same conversion counting method
└── Verify timezone settings match

PROBLEEM: Enhanced Measurement events niet werkend
──────────────────────────────────────────────────
Oorzaken:
├── Custom implementation conflicts
├── SPA (Single Page App) routing issues
├── Events gefilterd door consent
└── Verkeerde event parameters

Oplossing:
├── Check DebugView voor event triggering
├── Voor SPA: gebruik page_view event bij route change
├── Review consent mode implementation
└── Disable conflicting custom events

PROBLEEM: Google Signals thresholding
─────────────────────────────────────
Oorzaken:
├── Te weinig data volume
├── Privacy thresholds toegepast
└── Specific dimensions gecombineerd

Oplossing:
├── Gebruik bredere date ranges
├── Aggregeer naar hogere dimensies
├── Overweeg BigQuery export voor raw data
└── Accepteer dat sommige data niet beschikbaar is
```

## Output: GA4 Property Setup Recommendation Template

```markdown
# GA4 Property Setup Rapport

## Property Informatie
- **Property naam:** [Naam]
- **Measurement ID:** G-XXXXXXXXXX
- **Timezone:** [Timezone]
- **Currency:** [Currency]
- **Setup datum:** [Datum]

## Data Stream Configuratie
- **Stream type:** Web / iOS / Android
- **Website URL:** [URL]
- **Enhanced Measurement:** ✅ Geconfigureerd

### Enhanced Measurement Status
| Event | Status | Notities |
|-------|--------|----------|
| Page views | ✅ | - |
| Scrolls | ✅ | - |
| Outbound clicks | ✅ | - |
| Site search | ✅ | Parameter: [X] |
| Video engagement | ✅ | - |
| File downloads | ✅ | - |
| Form interactions | ⚠️ | [Notities] |

## Data Settings
- **Google Signals:** ✅ Enabled
- **Data retention:** 14 maanden
- **User data reset:** ✅ Enabled

## Product Links
| Product | Status | Account ID |
|---------|--------|------------|
| Google Ads | ✅ Linked | XXX-XXX-XXXX |
| Search Console | ✅ Linked | [Property] |
| BigQuery | [Status] | [Project ID] |

## Key Events Geconfigureerd
| Event naam | Type | Status |
|------------|------|--------|
| purchase | E-commerce | ✅ Active |
| generate_lead | Lead gen | ✅ Active |
| [Custom event] | [Type] | [Status] |

## Cross-Domain Setup
- **Configured domains:** [Lijst domeinen]
- **Verificatie status:** ✅ Getest en werkend

## Volgende Stappen
1. [ ] [Eerste actie]
2. [ ] [Tweede actie]
3. [ ] [Derde actie]

## Notities
[Eventuele aanvullende opmerkingen of aandachtspunten]
```

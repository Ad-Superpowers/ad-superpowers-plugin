---
name: ga4-key-events-config
description: "Google Analytics 4 Key Events (conversies) configuratie gids. Gebruik voor: (1) Events markeren als Key Event/conversie, (2) Conversion value instellen, (3) Primary vs secondary conversions kiezen, (4) Google Ads conversion import voorbereiden, (5) Conversion tracking valideren. Triggers: key events, conversions, conversion tracking, conversion value, ga4 conversions, goal setup, conversion import."
---

# GA4 Key Events Configuratie

Complete gids voor het configureren van Key Events (voorheen "Conversions") in Google Analytics 4 voor optimale advertising performance.

## Quick Decision Tree

```
WELKE EVENTS MOETEN KEY EVENTS WORDEN?
│
├─► BUSINESS-KRITIEKE ACTIES
│   ├── E-commerce: purchase, begin_checkout
│   ├── Lead Gen: generate_lead, sign_up, contact_form
│   ├── SaaS: trial_start, subscription_start
│   └── Content: newsletter_signup, download
│       └─► MARKEER ALS KEY EVENT ✅
│
├─► ENGAGEMENT EVENTS
│   ├── page_view, scroll, video_start
│   ├── cta_click, outbound_click
│   └── time_on_page
│       └─► NIET als Key Event (tenzij primary goal)
│
├─► MICRO-CONVERSIES
│   ├── add_to_cart, view_item
│   ├── pricing_page_view
│   └── chat_open
│       └─► OVERWEEG als secondary conversion
│
└─► VOOR GOOGLE ADS IMPORT
    ├─► Primary Conversion: Hoofd-KPI (purchase, lead)
    ├─► Secondary Conversion: Optimization signals
    └─► Kies MAX 1-2 primary per campaign type
```

## Key Events vs Events

```
KEY EVENTS UITLEG (2024+ terminologie)
======================================

┌────────────────────────────────────────────────────────────────┐
│  EVENTS                          KEY EVENTS                   │
│  ═══════════════════════════     ═══════════════════════════  │
│  Alle gebruikersacties           Belangrijkste acties         │
│                                                                │
│  Automatisch getrackt:           Door jou gemarkeerd:         │
│  ├── page_view                   ├── purchase                 │
│  ├── scroll                      ├── generate_lead            │
│  ├── click                       ├── sign_up                  │
│  ├── file_download               └── [jouw business goals]    │
│  └── etc.                                                      │
│                                                                │
│  Zichtbaar in: Events reports    Zichtbaar in: Key Events     │
│                                  + Conversion reports          │
│                                  + Kan importeren naar Ads     │
└────────────────────────────────────────────────────────────────┘

TERMINOLOGIE VERANDERING:
├── "Conversions" → "Key Events" (GA4 interface, 2024)
├── Nog steeds "Conversions" in Google Ads
├── Zelfde functionaliteit, nieuwe naam
└── Import naar Google Ads blijft "Conversion Import"
```

## Key Event Markeren

```
EVENT MARKEREN ALS KEY EVENT
============================

METHODE 1: Via Events Report
────────────────────────────
LOCATIE: Reports → Engagement → Events

STAPPEN:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Ga naar Events report                                     │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Zoek het event dat je wilt markeren                       │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click op de toggle in "Mark as key event" kolom           │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Toggle naar ON (blauw)                                    │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Event is nu een Key Event                                 │
└────┴────────────────────────────────────────────────────────────┘


METHODE 2: Via Admin → Key Events
─────────────────────────────────
LOCATIE: Admin → Data display → Key events

STAPPEN:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Click "New key event"                                     │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Voer exact de event name in (case-sensitive!)             │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Click "Save"                                              │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Event wordt Key Event zodra data binnenkomt               │
└────┴────────────────────────────────────────────────────────────┘

⚠️ BELANGRIJK:
├── Event name moet EXACT matchen (case-sensitive)
├── Event moet al bestaan OF wordt actief bij eerste trigger
├── Retroactief: alleen nieuwe data vanaf moment van markering
└── Max ~30 key events per property (soft limit)
```

## Conversion Value Instellen

```
CONVERSION VALUE CONFIGURATIE
=============================

WAAROM VALUE TOEKENNEN?
├── Value-based bidding in Google Ads (tROAS)
├── ROI berekeningen in reports
├── Prioritering van conversie types
└── Beter budget allocation advies

METHODE 1: Dynamische Value (aanbevolen voor e-commerce)
────────────────────────────────────────────────────────

Stuur value mee met event:

GTM GA4 Event Tag:
├── Event name: purchase
├── Event Parameters:
│   ├── value: {{DLV - transaction_value}}
│   ├── currency: EUR
│   └── transaction_id: {{DLV - order_id}}

Of via gtag.js:
```javascript
gtag('event', 'purchase', {
  'transaction_id': 'T12345',
  'value': 150.00,
  'currency': 'EUR',
  'items': [...]
});
```


METHODE 2: Statische Value (voor lead gen)
──────────────────────────────────────────

LOCATIE: Admin → Key events → Click event → "Edit"

CONFIGURATIE:
┌────────────────────────────────────────────────────────────────┐
│ Default conversion value: €[X]                                 │
│ Currency: EUR                                                  │
│                                                                │
│ ⚠️ NOOT: Dit overschrijft NIET dynamische values              │
│    Wordt alleen gebruikt als geen value wordt meegestuurd      │
└────────────────────────────────────────────────────────────────┘

VALUE BEREKENING VOOR LEAD GEN:
───────────────────────────────
Lead Value = Average Deal Size × Close Rate

Voorbeeld:
├── Gemiddelde deal: €5.000
├── Close rate: 10%
├── Lead value: €5.000 × 0.10 = €500

Alternatief per lead type:
├── Contact form: €100
├── Demo request: €300
├── Phone call: €150
└── Chat lead: €75
```

## Counting Method

```
CONVERSION COUNTING CONFIGUREREN
================================

LOCATIE: Admin → Key events → [event] → Edit

OPTIES:
┌─────────────────┬───────────────────────────────────────────────┐
│ Once per event  │ Elke keer dat event fired = 1 conversie       │
│ (default)       │ ✅ Gebruik voor: purchases, form submits       │
│                 │                                                │
│                 │ Voorbeeld: 3× purchase = 3 conversies          │
├─────────────────┼───────────────────────────────────────────────┤
│ Once per        │ Max 1 conversie per sessie                    │
│ session         │ ✅ Gebruik voor: signups, lead forms           │
│                 │                                                │
│                 │ Voorbeeld: 3× form submit = 1 conversie        │
└─────────────────┴───────────────────────────────────────────────┘

AANBEVELINGEN PER USE CASE:
───────────────────────────

E-COMMERCE:
├── purchase → Once per event (elk order telt)
├── begin_checkout → Once per session (1 intent per sessie)
├── add_to_cart → Once per event (telt volume)
└── view_item → Niet als conversie

LEAD GENERATION:
├── generate_lead → Once per session (1 lead per sessie)
├── phone_click → Once per session (1 intent per sessie)
├── form_submit → Once per session
└── contact_request → Once per session

SAAS:
├── trial_start → Once per session
├── subscription_purchase → Once per event (elk subscription)
├── upgrade → Once per event
└── feature_activation → Once per session
```

## Primary vs Secondary Conversions

```
PRIMARY VS SECONDARY VOOR GOOGLE ADS
====================================

CONCEPT:
┌────────────────────────────────────────────────────────────────┐
│  PRIMARY CONVERSIONS              SECONDARY CONVERSIONS        │
│  ═══════════════════════════     ═══════════════════════════  │
│  Gebruikt voor:                  Gebruikt voor:                │
│  ├── Smart Bidding optimalisatie ├── Reporting/observatie     │
│  ├── ROAS/CPA berekening         ├── Funnel inzichten          │
│  └── Budget optimalisatie        └── Extra signalen            │
│                                                                │
│  Impact op bidding: JA           Impact op bidding: NEE        │
│                                                                │
│  Voorbeeld:                      Voorbeeld:                    │
│  └── purchase                    ├── add_to_cart               │
│  └── qualified_lead              ├── begin_checkout            │
│                                  └── page_view (pricing)       │
└────────────────────────────────────────────────────────────────┘

WANNEER GEKOZEN:
├── Primary wordt bepaald bij import in Google Ads
├── GA4 markeert alleen als "key event"
├── Google Ads onderscheidt primary/secondary
└── Kies in: Google Ads → Goals → Conversions → Settings

BEST PRACTICES:
───────────────
✅ MAX 1-2 PRIMARY conversions per campaign type
✅ Zelfde primary gebruiken in related campaigns
✅ Secondary voor observatie zonder bidding impact
✅ Consistent houden over tijd (AI heeft history nodig)

❌ VERMIJD:
├── Te veel primary conversions (verwart algoritme)
├── Mix van upper en lower funnel als primary
├── Constant wisselen van primary
└── Overlappende conversies als primary
```

## Aanbevolen Key Events per Business Type

```
KEY EVENT CONFIGURATIE PER BUSINESS TYPE
========================================

E-COMMERCE
──────────
┌──────────────────┬──────────┬──────────┬─────────────────────┐
│ Event            │ Priority │ Value    │ Counting            │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ purchase         │ Primary  │ Dynamic  │ Once per event      │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ begin_checkout   │ Secondary│ €5-10    │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ add_to_cart      │ Secondary│ €2-5     │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ add_payment_info │ Secondary│ €3-7     │ Once per session    │
└──────────────────┴──────────┴──────────┴─────────────────────┘


LEAD GENERATION (B2B)
─────────────────────
┌──────────────────┬──────────┬──────────┬─────────────────────┐
│ Event            │ Priority │ Value    │ Counting            │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ generate_lead    │ Primary  │ €50-500  │ Once per session    │
│ (demo request)   │          │          │                     │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ phone_click      │ Secondary│ €30-100  │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ contact_submit   │ Secondary│ €20-50   │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ pricing_view     │ Secondary│ €5-10    │ Once per session    │
└──────────────────┴──────────┴──────────┴─────────────────────┘


SAAS / SUBSCRIPTION
───────────────────
┌──────────────────┬──────────┬──────────┬─────────────────────┐
│ Event            │ Priority │ Value    │ Counting            │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ trial_start      │ Primary  │ €25-100  │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ subscription_    │ Primary  │ Dynamic  │ Once per event      │
│ purchase         │          │ (MRR)    │                     │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ sign_up          │ Secondary│ €10-30   │ Once per session    │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ feature_activate │ Secondary│ €5-15    │ Once per session    │
└──────────────────┴──────────┴──────────┴─────────────────────┘


CONTENT / PUBLISHER
───────────────────
┌──────────────────┬──────────┬──────────┬─────────────────────┐
│ Event            │ Priority │ Value    │ Counting            │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ newsletter_      │ Primary  │ €5-20    │ Once per session    │
│ signup           │          │          │                     │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ premium_article_ │ Secondary│ €2-5     │ Once per session    │
│ view             │          │          │                     │
├──────────────────┼──────────┼──────────┼─────────────────────┤
│ content_download │ Secondary│ €3-10    │ Once per event      │
└──────────────────┴──────────┴──────────┴─────────────────────┘
```

## Key Event Validatie

```
KEY EVENT TESTING WORKFLOW
==========================

STAP 1: Check in DebugView
──────────────────────────
LOCATIE: Admin → DebugView

VERIFICATIE:
├── Event verschijnt in stream
├── Event is gemarkeerd met 🎯 (key event indicator)
├── Parameters correct (value, currency)
└── Geen duplicate events

STAP 2: Check in Realtime
─────────────────────────
LOCATIE: Reports → Realtime

VERIFICATIE:
├── Key event count telt op
├── Conversion card toont event
└── Value wordt geregistreerd (indien van toepassing)

STAP 3: Check in Key Events Report
──────────────────────────────────
LOCATIE: Reports → Engagement → Key events

⚠️ NOOT: Data kan 24-48 uur vertraagd zijn

VERIFICATIE:
├── Event verschijnt in lijst
├── Count is correct
├── Value is correct
└── Trend ziet er normaal uit

STAP 4: Check in Admin → Key Events
───────────────────────────────────
LOCATIE: Admin → Data display → Key events

VERIFICATIE:
├── Event status: Active
├── Counting method correct
├── Value correct geconfigureerd
└── Geen duplicate entries
```

## Google Ads Conversion Import Voorbereiding

```
VOORBEREIDEN VOOR GOOGLE ADS IMPORT
===================================

CHECKLIST VOOR GA4 KEY EVENTS:
┌────┬────────────────────────────────────────────────────────────┐
│ □  │ Key Event correct gemarkeerd in GA4                       │
├────┼────────────────────────────────────────────────────────────┤
│ □  │ Event heeft value (dynamisch of statisch)                 │
├────┼────────────────────────────────────────────────────────────┤
│ □  │ Currency correct ingesteld                                │
├────┼────────────────────────────────────────────────────────────┤
│ □  │ Counting method correct (once per event/session)          │
├────┼────────────────────────────────────────────────────────────┤
│ □  │ Google Ads account gelinked met GA4                       │
├────┼────────────────────────────────────────────────────────────┤
│ □  │ Voldoende conversies voor betrouwbare data (50+/maand)    │
├────┼────────────────────────────────────────────────────────────┤
│ □  │ DebugView test passed                                     │
└────┴────────────────────────────────────────────────────────────┘

IMPORT FLOW (NA VOORBEREIDING):
───────────────────────────────
1. Google Ads → Goals → Conversions
2. + New conversion action
3. Import → Google Analytics 4 properties
4. Selecteer je property
5. Selecteer key event(s) om te importeren
6. Configureer als Primary of Secondary
7. Save

⚠️ IMPORT OVERWEGINGEN:
├── Import sync duurt 4-6 uur initieel
├── Ongoing sync: elke paar uur
├── 5-15% discrepancy met native GA4 is normaal
├── Attribution window differences bestaan
└── Test ALTIJD voor je live campaigns wijzigt
```

## Troubleshooting

```
KEY EVENT TROUBLESHOOTING
=========================

PROBLEEM: Key Event telt niet
─────────────────────────────
Checklist:
□ Is event daadwerkelijk aan het firen? (DebugView)
□ Is event naam EXACT correct (case-sensitive)?
□ Is counting method correct ingesteld?
□ Is er consent gegeven? (consent mode)
□ Wacht je lang genoeg? (24-48 uur processing)

PROBLEEM: Value wordt niet geregistreerd
────────────────────────────────────────
Checklist:
□ Wordt 'value' parameter meegestuurd?
□ Is value een NUMBER, niet een string?
□ Wordt 'currency' parameter meegestuurd?
□ Currency code correct? (EUR, USD, niet "euro")
□ Is default value ingesteld als fallback?

PROBLEEM: Duplicate Key Events
──────────────────────────────
Oorzaken:
├── Event wordt meerdere keren getriggerd
├── GTM tag fires multiple times
├── SPA route changes triggeren opnieuw
└── Page refresh triggers opnieuw

Oplossing:
├── Review trigger condities in GTM
├── Gebruik "Once per session" counting
├── Implementeer event deduplication
└── Add session-based blocking trigger

PROBLEEM: Key Event verschijnt niet in Google Ads
─────────────────────────────────────────────────
Checklist:
□ Is Google Ads account gelinked?
□ Is link actief? (check beide kanten)
□ Wacht je lang genoeg? (24-48 uur eerste sync)
□ Is property correct geselecteerd?
□ Heb je permissions in beide accounts?

PROBLEEM: Conversion count verschilt GA4 vs Google Ads
──────────────────────────────────────────────────────
Normaal: 5-15% verschil is acceptabel

Oorzaken voor groter verschil:
├── Verschillende attribution windows
├── Verschillende counting methods
├── Time zone differences
├── Cross-device tracking differences
└── Consent mode differences

Oplossing:
├── Align attribution windows
├── Document expected difference
├── Gebruik GA4 als source of truth voor reporting
└── Gebruik Google Ads numbers voor bidding decisions
```

## Key Event Audit Checklist

```
KEY EVENT CONFIGURATIE AUDIT
============================

□ INVENTARISATIE
├── □ Alle key events gedocumenteerd
├── □ Geen onnodige key events actief
├── □ Consistent met business goals
└── □ Aligned met advertising strategie

□ VALUE CONFIGURATIE
├── □ Primary conversions hebben value
├── □ Values zijn realistisch (niet €0 of €999999)
├── □ Currency correct
└── □ Dynamische values waar mogelijk

□ COUNTING CONFIGURATIE
├── □ Counting method past bij use case
├── □ Geen over-counting door duplicates
├── □ Consistent over related events
└── □ Gedocumenteerd

□ GOOGLE ADS ALIGNMENT
├── □ Belangrijke key events geïmporteerd
├── □ Primary/Secondary correct ingesteld
├── □ Attribution settings aligned
└── □ Conversion lag windows passend

□ TESTING
├── □ Alle key events getest in DebugView
├── □ Values correct geregistreerd
├── □ Geen duplicate counting
└── □ Realtime tracking werkend
```

## Output: Key Events Configuration Template

```markdown
# Key Events Configuratie Rapport

## Property Informatie
- **Property:** [Property Name]
- **Measurement ID:** G-XXXXXXXXXX
- **Configuratie datum:** [Datum]

## Key Events Overzicht

### Primary Key Events (voor bidding)
| Event Name | Value | Counting | Google Ads Status |
|------------|-------|----------|-------------------|
| purchase | Dynamic | Per event | ✅ Imported (Primary) |
| generate_lead | €200 | Per session | ✅ Imported (Primary) |

### Secondary Key Events (voor observatie)
| Event Name | Value | Counting | Google Ads Status |
|------------|-------|----------|-------------------|
| begin_checkout | €10 | Per session | ✅ Imported (Secondary) |
| add_to_cart | €3 | Per session | ⏳ Not imported |
| phone_click | €50 | Per session | ✅ Imported (Secondary) |

## Value Berekening

### Lead Value Berekening
```
Average Deal Size: €[X]
Close Rate: [X]%
Calculated Lead Value: €[X]
Applied Value: €[X]
```

### E-commerce Value
```
Method: Dynamic (transaction value)
Currency: EUR
Fallback Value: €[X] (indien geen value meegestuurd)
```

## Counting Method Rationale

| Event | Method | Rationale |
|-------|--------|-----------|
| purchase | Per event | Elk order is een aparte transactie |
| generate_lead | Per session | Voorkom duplicate leads |
| begin_checkout | Per session | 1 checkout intent per bezoek |

## Google Ads Import Status
- **Link Status:** ✅ Active
- **Import Sync:** Every 4-6 hours
- **Last Sync:** [Datum/tijd]

## Validatie Status
- [x] DebugView test passed
- [x] Realtime tracking verified
- [x] Value registration confirmed
- [x] No duplicate counting
- [x] Google Ads import verified

## Aanbevelingen
1. [Eerste aanbeveling]
2. [Tweede aanbeveling]
3. [Derde aanbeveling]

## Notities
[Eventuele aandachtspunten of bijzonderheden]
```

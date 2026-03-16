---
name: ga4-event-tracking-setup
description: "Google Analytics 4 event tracking implementatie gids. Gebruik voor: (1) Custom events configureren in GTM, (2) Form submission tracking opzetten, (3) Video engagement tracking, (4) Click tracking en CTA monitoring, (5) Event parameters en user properties instellen. Triggers: event tracking, custom events, gtm events, form tracking, click tracking, ga4 events, event parameters."
---

# GA4 Event Tracking Setup

Complete gids voor het implementeren van custom event tracking in Google Analytics 4 via Google Tag Manager.

## Quick Decision Tree

```
WELK EVENT TYPE HEB JE NODIG?
│
├─► AUTOMATISCH GETRACKT (Enhanced Measurement)
│   ├── page_view (automatisch)
│   ├── scroll (90% depth)
│   ├── click (outbound links)
│   ├── file_download
│   ├── video_start/progress/complete (YouTube)
│   └── view_search_results
│       └─► CHECK: Is Enhanced Measurement AAN?
│
├─► RECOMMENDED EVENTS (Google's standaard namen)
│   ├── E-commerce: view_item, add_to_cart, purchase
│   ├── Lead gen: generate_lead, sign_up
│   ├── Content: share, search
│   └── Gaming: earn_virtual_currency, level_up
│       └─► GEBRUIK: Google's event namen voor betere AI/reports
│
├─► CUSTOM EVENTS (eigen namen)
│   ├── Specifieke business acties
│   ├── Interactie tracking
│   └── Micro-conversies
│       └─► NAAMGEVING: snake_case, max 40 chars
│
└─► WELKE TRIGGER?
    ├── Click → Element Click / Just Links trigger
    ├── Form Submit → Form Submission trigger
    ├── Page Load → Page View trigger + conditions
    ├── Scroll → Scroll Depth trigger
    ├── Timer → Timer trigger
    └── Custom → Custom Event / dataLayer push
```

## GA4 Event Model Basics

```
GA4 EVENT STRUCTUUR
===================

┌────────────────────────────────────────────────────────────────┐
│  ELKE HIT IN GA4 IS EEN EVENT                                  │
│                                                                │
│  Event Naam: generate_lead                                     │
│  ├── Parameter 1: form_name = "contact_form"                   │
│  ├── Parameter 2: form_location = "footer"                     │
│  ├── Parameter 3: lead_value = 50                              │
│  └── Parameter 4: page_location = (automatisch)                │
│                                                                │
│  AUTOMATISCHE PARAMETERS (altijd meegestuurd):                 │
│  ├── page_location (URL)                                       │
│  ├── page_title                                                │
│  ├── page_referrer                                             │
│  ├── screen_resolution                                         │
│  ├── language                                                  │
│  └── engagement_time_msec                                      │
└────────────────────────────────────────────────────────────────┘

LIMIETEN:
├── Event naam: max 40 characters
├── Parameter naam: max 40 characters
├── Parameter value: max 100 characters
├── Parameters per event: max 25
└── Unique event names per property: max 500
```

## Event Naamgeving Conventies

```
EVENT NAMING BEST PRACTICES
===========================

FORMAT: [object]_[action] in snake_case

VOORBEELDEN:
┌─────────────────────┬────────────────────────────────────────┐
│ Actie               │ Event Naam                             │
├─────────────────────┼────────────────────────────────────────┤
│ Form versturen      │ form_submit                            │
├─────────────────────┼────────────────────────────────────────┤
│ CTA klikken         │ cta_click                              │
├─────────────────────┼────────────────────────────────────────┤
│ Video afspelen      │ video_play                             │
├─────────────────────┼────────────────────────────────────────┤
│ PDF downloaden      │ pdf_download                           │
├─────────────────────┼────────────────────────────────────────┤
│ Newsletter signup   │ newsletter_signup                      │
├─────────────────────┼────────────────────────────────────────┤
│ Chat openen         │ chat_open                              │
├─────────────────────┼────────────────────────────────────────┤
│ Calculator gebruiken│ calculator_use                         │
├─────────────────────┼────────────────────────────────────────┤
│ Pricing bekijken    │ pricing_view                           │
└─────────────────────┴────────────────────────────────────────┘

❌ VERMIJD:
├── Spaties: "form submit" → form_submit
├── Hoofdletters: "FormSubmit" → form_submit
├── Speciale tekens: "form-submit!" → form_submit
├── Te lange namen: "user_clicked_the_contact_button" → contact_click
└── Generic namen: "click", "event", "action"

✅ GEBRUIK RECOMMENDED EVENTS waar mogelijk:
├── generate_lead (niet: lead_generated, form_complete)
├── sign_up (niet: signup, registration, user_signup)
├── purchase (niet: buy, order, transaction)
└── add_to_cart (niet: cart_add, add_item)
```

## Form Tracking Setup

```
FORM SUBMISSION TRACKING
========================

METHODE 1: GTM Form Submission Trigger (simpelst)
─────────────────────────────────────────────────

TRIGGER SETUP:
┌────────────────────────────────────────────────────────────────┐
│ Trigger Type: Form Submission                                  │
│                                                                │
│ Wait for Tags: ✅ Check                                        │
│ Max wait time: 2000ms                                          │
│                                                                │
│ Check Validation: ✅ Check (alleen valid submits)              │
│                                                                │
│ Trigger fires on:                                              │
│ ├── Some Forms (aanbevolen)                                    │
│ └── Form ID / Form Classes contains: [jouw form identifier]   │
└────────────────────────────────────────────────────────────────┘

TAG SETUP (GA4 Event):
┌────────────────────────────────────────────────────────────────┐
│ Tag Type: Google Analytics: GA4 Event                          │
│                                                                │
│ Configuration Tag: [Je GA4 Config tag]                         │
│ Event Name: generate_lead                                      │
│                                                                │
│ Event Parameters:                                              │
│ ├── form_name: {{Form ID}} of hardcoded                        │
│ ├── form_location: {{Page Path}}                               │
│ └── method: "form"                                             │
└────────────────────────────────────────────────────────────────┘


METHODE 2: dataLayer Push (voor complexe forms)
───────────────────────────────────────────────

JAVASCRIPT (bij form success):
```javascript
// Na succesvolle form submit
dataLayer.push({
  'event': 'form_submit',
  'form_name': 'contact_form',
  'form_location': 'homepage_hero',
  'lead_value': 50
});
```

GTM TRIGGER:
├── Type: Custom Event
├── Event name: form_submit
└── Fires on: All Custom Events

TAG (GA4 Event):
├── Event name: generate_lead
├── Parameters: Pull from dataLayer variables
└── form_name: {{DLV - form_name}}


METHODE 3: Thank You Page (fallback)
────────────────────────────────────

TRIGGER:
├── Type: Page View
├── Fires on: Some Page Views
└── Page Path contains: /thank-you of /bedankt

TAG:
├── Event name: generate_lead
├── Parameters: form_name = {{Page Referrer}} of hardcoded
└── ⚠️ NADEEL: Mist directe form context
```

## Click Tracking Setup

```
CLICK TRACKING CONFIGURATIE
===========================

STAP 1: Enable Built-in Variables (GTM)
───────────────────────────────────────
Variables → Configure → Enable:
├── Click Element
├── Click Classes
├── Click ID
├── Click Target
├── Click URL
└── Click Text

STAP 2: Create Click Trigger
────────────────────────────

TYPE A: All Elements Click (voor buttons, divs, etc.)
┌────────────────────────────────────────────────────────────────┐
│ Trigger Type: Click - All Elements                             │
│                                                                │
│ Trigger fires on: Some Clicks                                  │
│                                                                │
│ Conditions (één of meer):                                      │
│ ├── Click Classes contains: cta-button                         │
│ ├── Click ID equals: main-cta                                  │
│ ├── Click Text contains: "Request Demo"                        │
│ └── Click Element matches CSS: .hero-section .btn-primary      │
└────────────────────────────────────────────────────────────────┘

TYPE B: Just Links Click (voor <a> tags)
┌────────────────────────────────────────────────────────────────┐
│ Trigger Type: Click - Just Links                               │
│                                                                │
│ Wait for Tags: ✅ Check                                        │
│ Max wait time: 2000ms                                          │
│                                                                │
│ Check Validation: ✅ Check                                     │
│                                                                │
│ Trigger fires on: Some Link Clicks                             │
│ Click URL contains: tel: / mailto: / .pdf                      │
└────────────────────────────────────────────────────────────────┘

STAP 3: Create GA4 Event Tag
────────────────────────────
┌────────────────────────────────────────────────────────────────┐
│ Tag Type: GA4 Event                                            │
│                                                                │
│ Event Name: cta_click                                          │
│                                                                │
│ Event Parameters:                                              │
│ ├── click_text: {{Click Text}}                                 │
│ ├── click_url: {{Click URL}}                                   │
│ ├── click_location: {{Page Path}}                              │
│ └── click_element: {{Click Classes}}                           │
└────────────────────────────────────────────────────────────────┘
```

## Phone & Email Click Tracking

```
PHONE & EMAIL TRACKING
======================

PHONE CLICKS (tel: links)
─────────────────────────

TRIGGER:
├── Type: Click - Just Links
├── Fires on: Some Link Clicks
└── Click URL starts with: tel:

TAG:
├── Event name: phone_click
├── Parameters:
│   ├── phone_number: {{Click URL}} (strip 'tel:' via variable)
│   └── click_location: {{Page Path}}

VARIABLE (Clean phone number):
├── Type: Custom JavaScript
└── Code:
```javascript
function() {
  var url = {{Click URL}};
  return url.replace('tel:', '').replace(/\s/g, '');
}
```

EMAIL CLICKS (mailto: links)
────────────────────────────

TRIGGER:
├── Type: Click - Just Links
├── Fires on: Some Link Clicks
└── Click URL starts with: mailto:

TAG:
├── Event name: email_click
├── Parameters:
│   ├── email_address: (⚠️ overweeg privacy)
│   └── click_location: {{Page Path}}

⚠️ PRIVACY NOOT:
├── Overweeg om email addresses te hashen
├── Of alleen tellen, niet de waarde opslaan
└── Check GDPR compliance
```

## Video Tracking Setup

```
VIDEO TRACKING CONFIGURATIE
===========================

YOUTUBE VIDEOS (Enhanced Measurement)
─────────────────────────────────────
GA4 trackt automatisch YouTube embeds met Enhanced Measurement:
├── video_start
├── video_progress (10%, 25%, 50%, 75%)
└── video_complete

Vereisten:
├── Enhanced Measurement → Video engagement: ON
├── YouTube embed met JS API enabled
└── ?enablejsapi=1 in iframe src (wordt automatisch toegevoegd)

CUSTOM VIDEO PLAYERS (Vimeo, HTML5, etc.)
─────────────────────────────────────────

STAP 1: YouTube Video Trigger in GTM
├── Type: YouTube Video
├── Capture: Start, Complete, Pause, Progress
├── Progress percentages: 25, 50, 75, 90

STAP 2: Voor Vimeo/HTML5 - Custom JavaScript
```javascript
// HTML5 Video Tracking
document.querySelectorAll('video').forEach(function(video) {

  video.addEventListener('play', function() {
    dataLayer.push({
      'event': 'video_play',
      'video_title': this.getAttribute('data-title') || 'Unknown',
      'video_provider': 'html5',
      'video_url': this.currentSrc
    });
  });

  video.addEventListener('ended', function() {
    dataLayer.push({
      'event': 'video_complete',
      'video_title': this.getAttribute('data-title') || 'Unknown',
      'video_provider': 'html5'
    });
  });
});
```

STAP 3: GA4 Event Tag
├── Trigger: Custom Event = video_play / video_complete
├── Event name: video_start / video_complete
├── Parameters:
│   ├── video_title: {{DLV - video_title}}
│   ├── video_provider: {{DLV - video_provider}}
│   └── video_percent: {{DLV - video_percent}}
```

## Scroll Depth Tracking

```
SCROLL DEPTH TRACKING
=====================

ENHANCED MEASUREMENT (standaard)
────────────────────────────────
GA4 trackt automatisch 90% scroll depth.
Event naam: scroll

CUSTOM SCROLL DEPTH (meerdere thresholds)
─────────────────────────────────────────

TRIGGER SETUP:
┌────────────────────────────────────────────────────────────────┐
│ Trigger Type: Scroll Depth                                     │
│                                                                │
│ Scroll Depth Type: ✅ Vertical Scroll Depths                   │
│ Percentages: 25, 50, 75, 90                                    │
│                                                                │
│ Trigger fires on: All Pages of Some Pages                      │
│ (Filter op belangrijke content pages)                          │
└────────────────────────────────────────────────────────────────┘

ENABLE BUILT-IN VARIABLES:
├── Scroll Depth Threshold
├── Scroll Depth Units
└── Scroll Direction

TAG SETUP:
├── Event name: scroll_depth
├── Parameters:
│   ├── scroll_percent: {{Scroll Depth Threshold}}
│   ├── page_path: {{Page Path}}
│   └── content_type: (optioneel, hardcoded of via variable)

⚠️ NOOT:
├── Disable Enhanced Measurement scroll als je custom gebruikt
├── Anders krijg je dubbele data
└── Custom geeft meer granulariteit
```

## User Properties Setup

```
USER PROPERTIES CONFIGURATIE
============================

WAT ZIJN USER PROPERTIES?
├── Attributen die bij een USER horen (niet bij event)
├── Persistent over sessies
├── Gebruikt voor segmentatie
└── Max 25 user properties per property

VOORBEELDEN:
┌─────────────────────┬────────────────────────────────────────┐
│ User Property       │ Voorbeeld Waarde                       │
├─────────────────────┼────────────────────────────────────────┤
│ membership_level    │ free / pro / enterprise                │
├─────────────────────┼────────────────────────────────────────┤
│ customer_type       │ new / returning / vip                  │
├─────────────────────┼────────────────────────────────────────┤
│ industry            │ ecommerce / saas / agency              │
├─────────────────────┼────────────────────────────────────────┤
│ signup_date         │ 2024-01-15                             │
├─────────────────────┼────────────────────────────────────────┤
│ lifetime_value      │ 500 (€)                                │
└─────────────────────┴────────────────────────────────────────┘

IMPLEMENTATIE VIA GTM:
──────────────────────

GA4 CONFIG TAG → User Properties:
┌────────────────────────────────────────────────────────────────┐
│ Property Name: membership_level                                │
│ Value: {{DLV - user_membership}} of {{Cookie - membership}}   │
│                                                                │
│ Property Name: customer_type                                   │
│ Value: {{DLV - customer_type}}                                 │
└────────────────────────────────────────────────────────────────┘

OF VIA DATALAYER:
```javascript
dataLayer.push({
  'user_properties': {
    'membership_level': 'pro',
    'customer_type': 'returning',
    'lifetime_value': 500
  }
});
```

GA4 REGISTRATIE:
├── Admin → Custom definitions → Custom dimensions
├── Scope: User
├── Dimension name: Membership Level
├── User property: membership_level
└── ⚠️ Moet geregistreerd zijn om in reports te zien!
```

## Custom Dimensions & Metrics

```
CUSTOM DIMENSIONS REGISTREREN
=============================

LOCATIE: Admin → Custom definitions → Custom dimensions

EVENT-SCOPED DIMENSIONS (meest gebruikt):
┌─────────────────────┬─────────────┬────────────────────────────┐
│ Dimension Name      │ Event Param │ Gebruik                    │
├─────────────────────┼─────────────┼────────────────────────────┤
│ Form Name           │ form_name   │ Welke form werd ingevuld   │
├─────────────────────┼─────────────┼────────────────────────────┤
│ CTA Location        │ cta_location│ Waar stond de CTA          │
├─────────────────────┼─────────────┼────────────────────────────┤
│ Content Type        │ content_type│ Blog, product, landing page│
├─────────────────────┼─────────────┼────────────────────────────┤
│ Product Category    │ item_category│ Voor e-commerce           │
├─────────────────────┼─────────────┼────────────────────────────┤
│ Author              │ author      │ Content creator            │
└─────────────────────┴─────────────┴────────────────────────────┘

CUSTOM METRICS:
├── Scope: Event
├── Voorbeeld: Lead Value (€), Engagement Score
└── Unit of measurement: Standard / Currency / Time

LIMIETEN:
├── Event-scoped dimensions: 50
├── User-scoped dimensions: 25
├── Custom metrics: 50
└── ⚠️ Eenmaal aangemaakt, kan naam niet wijzigen
```

## GTM Preview & Debug

```
EVENT TESTING WORKFLOW
======================

STAP 1: GTM Preview Mode
────────────────────────
├── In GTM: Click "Preview"
├── Enter website URL
├── Preview window opens
└── Tag Assistant shows all firing tags

STAP 2: Check Tag Firing
────────────────────────
In Tag Assistant panel:
├── ✅ Groen = Tag fired successfully
├── ❌ Rood = Tag blocked of error
├── Check "Tags Fired" vs "Tags Not Fired"
└── Click tag voor details (parameters, trigger)

STAP 3: GA4 DebugView
─────────────────────
LOCATIE: GA4 → Admin → DebugView

ENABLEN:
├── GTM Preview auto-enabled DebugView
├── Of: gtag('config', 'G-XXX', { 'debug_mode': true });
├── Of: URL parameter ?debug_mode=1
└── Check: GA Debugger browser extension

WAT TE CHECKEN:
├── Event name correct
├── Alle parameters aanwezig
├── Parameter values correct
├── User properties set
└── Timestamp en volgorde

STAP 4: Realtime Reports
────────────────────────
LOCATIE: GA4 → Reports → Realtime
├── Check event count
├── Check parameter values (click event card)
└── Verify user count
```

## Veelvoorkomende Problemen

```
TROUBLESHOOTING EVENT TRACKING
==============================

PROBLEEM: Event fires niet
──────────────────────────
Checklist:
□ Is trigger correct geconfigureerd?
□ Is built-in variable enabled?
□ Is CSS selector/ID correct?
□ Test in GTM Preview - check "Tags Not Fired"
□ Is er een blocking trigger?
□ Is consent gegeven (consent mode)?

PROBLEEM: Dubbele events
────────────────────────
Oorzaken:
├── Trigger fires multiple times
├── Enhanced Measurement + custom tracking
├── Multiple tags voor zelfde event
└── SPA route changes

Oplossing:
├── Add trigger conditions om te beperken
├── Disable overlapping Enhanced Measurement
├── Use event deduplication
└── Trigger only once per page/session

PROBLEEM: Parameters verschijnen niet in reports
────────────────────────────────────────────────
Checklist:
□ Is parameter geregistreerd als custom dimension?
□ Wacht je 24-48 uur? (processing time)
□ Is parameter naam exact gelijk (case-sensitive)?
□ Check DebugView - zijn parameters visible daar?

PROBLEEM: Event naam validation error
─────────────────────────────────────
Oorzaken:
├── Spaties in event naam
├── Speciale tekens
├── Begint met cijfer
├── Reserved event name gebruikt

Oplossing:
├── Use snake_case: contact_form_submit
├── Alleen letters, cijfers, underscores
├── Begin met letter
├── Check reserved names list
```

## Event Tracking Checklist

```
PRE-LAUNCH EVENT TRACKING CHECKLIST
===================================

□ PLANNING
├── □ Event tracking plan gedocumenteerd
├── □ Event namen volgen naming conventions
├── □ Parameters gedefinieerd per event
└── □ Custom dimensions gepland

□ IMPLEMENTATIE
├── □ GTM container correct geïnstalleerd
├── □ GA4 Config tag aanwezig
├── □ Built-in variables enabled
├── □ Alle event tags gecreëerd
├── □ Triggers correct geconfigureerd
└── □ User properties ingesteld (indien nodig)

□ TESTING
├── □ GTM Preview mode getest
├── □ DebugView events verified
├── □ Parameter values correct
├── □ Geen dubbele events
├── □ Consent mode werkt correct
└── □ Cross-browser getest

□ GA4 CONFIGURATIE
├── □ Custom dimensions geregistreerd
├── □ Custom metrics geregistreerd (indien nodig)
├── □ Key events (conversions) gemarkeerd
└── □ Realtime reports tonen events

□ DOCUMENTATIE
├── □ Event tracking sheet bijgewerkt
├── □ GTM container gedocumenteerd
└── □ Stakeholders geïnformeerd
```

## Output: Event Tracking Implementation Template

```markdown
# Event Tracking Implementation Plan

## Overzicht
- **Website:** [URL]
- **GTM Container:** GTM-XXXXXXX
- **GA4 Property:** G-XXXXXXXXXX
- **Implementation datum:** [Datum]

## Events Geïmplementeerd

### Lead Generation Events
| Event Name | Trigger | Parameters | Status |
|------------|---------|------------|--------|
| generate_lead | Form submit | form_name, form_location | ✅ Live |
| phone_click | Tel: link click | phone_number | ✅ Live |
| email_click | Mailto: link click | - | ✅ Live |

### Engagement Events
| Event Name | Trigger | Parameters | Status |
|------------|---------|------------|--------|
| cta_click | Button click | click_text, click_location | ✅ Live |
| video_start | Video play | video_title, video_provider | ✅ Live |
| scroll_depth | 25/50/75/90% | scroll_percent | ✅ Live |

### E-commerce Events
| Event Name | Trigger | Parameters | Status |
|------------|---------|------------|--------|
| view_item | Product view | item_id, item_name, price | ⏳ Pending |
| add_to_cart | Add to cart | item_id, quantity, value | ⏳ Pending |
| purchase | Order complete | transaction_id, value, items | ⏳ Pending |

## Custom Dimensions Geregistreerd
| Dimension Name | Scope | Event Parameter |
|----------------|-------|-----------------|
| Form Name | Event | form_name |
| CTA Location | Event | cta_location |
| Customer Type | User | customer_type |

## Testing Resultaten
- [ ] GTM Preview: All tags firing correctly
- [ ] DebugView: Events appearing with correct parameters
- [ ] Realtime: Events counting properly
- [ ] Cross-browser: Chrome, Safari, Firefox verified

## Notities
[Eventuele aandachtspunten of follow-up items]
```

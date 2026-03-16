---
name: enhanced-conversions-setup
description: "Google Ads Enhanced Conversions implementatie gids. Gebruik voor: (1) First-party data integratie, (2) Server-side tagging setup, (3) Consent Mode V2 configuratie, (4) Enhanced conversions for leads, (5) Offline conversion import, (6) Customer data hashing. Triggers: enhanced conversions, first party data, server side tagging, consent mode, gdpr, offline conversions, customer match, data privacy, hashing, gtm server."
---

# Enhanced Conversions Setup

Complete gids voor het implementeren van Enhanced Conversions voor betere conversie-attributie in een privacy-first wereld met first-party data en consent management.

## Quick Decision Guide

```
WELKE ENHANCED CONVERSIONS OPTIE PAST BIJ JOU?
│
├─► E-COMMERCE (Online Sales)
│   └─► ENHANCED CONVERSIONS FOR WEB
│       ├── Automatisch via Google Tag
│       ├── Of manual via GTM
│       └── Vereist: checkout form data
│
├─► LEAD GENERATION (Forms)
│   └─► ENHANCED CONVERSIONS FOR LEADS
│       ├── Capture lead data bij form submit
│       ├── Later: koppel aan offline sale
│       └── Vereist: CRM integratie
│
├─► OFFLINE SALES / LONG SALES CYCLE
│   └─► OFFLINE CONVERSION IMPORT
│       ├── Import sales data via API/upload
│       ├── Match met GCLID of enhanced matching
│       └── Vereist: CRM met GCLID tracking
│
└─► FULL ATTRIBUTION STACK
    └─► SERVER-SIDE TAGGING
        ├── First-party data collection
        ├── Meer controle over data
        ├── Betere ad blocker bypass
        └── Vereist: Server infrastructure
```

## Enhanced Conversions Overzicht

### Wat Zijn Enhanced Conversions?

```
ENHANCED CONVERSIONS FUNDAMENTALS
═════════════════════════════════

TRADITIONELE CONVERSIE TRACKING:
────────────────────────────────
User clicks ad → Cookie stored → Converts → Cookie matched
├── Probleem 1: Cookie blocking (ITP, browsers)
├── Probleem 2: Cross-device gaps
├── Probleem 3: Privacy regulations
└── Resultaat: ~40-60% conversion loss

ENHANCED CONVERSIONS:
─────────────────────
User clicks ad → Cookie stored → Converts → First-party data hashed & sent
├── Email (SHA256 hashed)
├── Phone (SHA256 hashed)
├── Name + Address (SHA256 hashed)
└── Google matches met signed-in users

┌─────────────────────────────────────────────────────────────────┐
│  ENHANCED CONVERSIONS FLOW                                       │
│                                                                  │
│  1. User clicks ad                                               │
│     └─► GCLID stored in cookie                                  │
│                                                                  │
│  2. User converts (fills form/buys)                             │
│     └─► First-party data collected (email, phone, etc.)         │
│                                                                  │
│  3. Data hashed on client/server                                │
│     └─► SHA256 one-way hash (irreversible)                      │
│                                                                  │
│  4. Hashed data sent to Google                                  │
│     └─► Matched with Google account data                        │
│                                                                  │
│  5. Conversion attributed                                        │
│     └─► Even without cookies!                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Privacy & Compliance

```
PRIVACY COMPLIANCE CHECKLIST
════════════════════════════

GDPR VEREISTEN:
───────────────
□ Consent verkregen VOOR data collectie
□ Privacy policy beschrijft data gebruik
□ Data minimalisatie (alleen noodzakelijke data)
□ User heeft opt-out mogelijkheid
□ Data niet gedeeld met derden (alleen hashed)

CONSENT MODE V2 (VERPLICHT EU - Maart 2024):
────────────────────────────────────────────
□ ad_storage consent
□ ad_user_data consent (NIEUW)
□ ad_personalization consent (NIEUW)
□ analytics_storage consent

IMPLEMENTATIE:
──────────────
Consent = GRANTED:
├── Full tracking enabled
├── First-party data kan worden verzameld
└── Enhanced conversions actief

Consent = DENIED:
├── Cookieless pings (voor modellering)
├── Geen first-party data verzonden
└── Conversion modeling wordt gebruikt
```

## Enhanced Conversions for Web

### Setup via Google Tag (Automatisch)

```
ENHANCED CONVERSIONS FOR WEB - AUTO SETUP
═════════════════════════════════════════

WANNEER: E-commerce of forms met standaard velden

STAP 1: ENABLE IN GOOGLE ADS
────────────────────────────
1. Tools & Settings → Conversions
2. Klik op je purchase/lead conversie
3. "Enhanced conversions" sectie → Turn on
4. Kies: "Google tag"
5. Selecteer: "Automatic collection"

STAP 2: VERIFIEER DATA COLLECTIE
────────────────────────────────
Google Tag zoekt automatisch naar:
├── Email velden (input type="email")
├── Phone velden (input type="tel")
├── Name velden (autocomplete="name")
└── Address velden (autocomplete="address-line1")

STAP 3: TEST
────────────
1. Tag Assistant (legacy) of Preview mode
2. Voer test conversie uit
3. Check of "user_data" parameter aanwezig is
4. Google Ads → Conversions → Check enhanced conv. status

⚠️ AUTOMATISCH WERKT NIET ALTIJD:
├── Custom form frameworks (React, Vue forms)
├── Niet-standaard veld names
├── Forms in iframes
└── → Gebruik Manual setup
```

### Setup via GTM (Manual)

```
ENHANCED CONVERSIONS VIA GTM - MANUAL SETUP
════════════════════════════════════════════

STAP 1: DATA LAYER SETUP
────────────────────────
Voeg toe aan je form success page of event:

<script>
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  'event': 'conversion',
  'enhanced_conversion_data': {
    'email': 'user@example.com',           // Plain text, wordt gehasht
    'phone_number': '+31612345678',         // E.164 format
    'first_name': 'Jan',
    'last_name': 'de Vries',
    'home_address': {
      'street': 'Damrak 1',
      'city': 'Amsterdam',
      'region': 'Noord-Holland',
      'postal_code': '1012LG',
      'country': 'NL'
    }
  }
});
</script>

⚠️ LET OP: Verstuur plain text, GTM/Google hasht automatisch

STAP 2: GTM VARIABELEN
──────────────────────
Maak Data Layer Variables:

Variable 1: dlv_email
├── Variable Type: Data Layer Variable
└── Data Layer Variable Name: enhanced_conversion_data.email

Variable 2: dlv_phone
├── Variable Type: Data Layer Variable
└── Data Layer Variable Name: enhanced_conversion_data.phone_number

(Herhaal voor andere velden)

STAP 3: USER-PROVIDED DATA VARIABLE
───────────────────────────────────
1. Variables → New → User-Provided Data
2. Vul in:
   ├── Email: {{dlv_email}}
   ├── Phone: {{dlv_phone}}
   ├── First Name: {{dlv_first_name}}
   └── etc.

STAP 4: CONVERSION TAG UPDATE
─────────────────────────────
1. Open je Google Ads Conversion Tag
2. Include user-provided data: Yes
3. User-provided data variable: {{User-Provided Data}}
4. Save

STAP 5: TEST & VERIFY
─────────────────────
1. GTM Preview mode
2. Voer conversie uit
3. Check tag → "user_data" parameter aanwezig
4. Google Ads diagnostics na 48-72 uur
```

### Data Formatting Requirements

```
DATA FORMATTING VOOR ENHANCED CONVERSIONS
═════════════════════════════════════════

EMAIL:
──────
□ Lowercase
□ Geen spaties voor/na
□ Geen aliassen expanderen (user+alias@gmail.com = user@gmail.com)

Voorbeeld: "John.Doe@Gmail.com" → "john.doe@gmail.com"

PHONE:
──────
□ E.164 format (landcode + nummer)
□ Geen spaties, streepjes, haakjes

Voorbeelden:
├── Nederland: +31612345678
├── België: +32471234567
└── Duitsland: +491521234567

NAAM:
─────
□ Alleen voornaam OF achternaam per veld
□ Geen titels (Dr., Mr., etc.)
□ Lowercase (Google normaliseert)

ADRES:
──────
□ Straat: alleen straatnaam en nummer
□ Stad: volledige stadsnaam
□ Postcode: zonder spaties
□ Land: ISO 3166-1 alpha-2 (NL, BE, DE)

┌────────────────────────────────────────────────────────────────┐
│ DATA KWALITEIT IMPACT OP MATCH RATE                            │
│                                                                │
│ Data punt          │ Impact op match rate                     │
│────────────────────┼────────────────────────────────────────│
│ Email alleen       │ 40-60% match rate                        │
│ Email + Phone      │ 60-75% match rate                        │
│ Email + Name       │ 55-70% match rate                        │
│ All fields         │ 70-85% match rate                        │
└────────────────────────────────────────────────────────────────┘
```

## Enhanced Conversions for Leads

### Implementatie Flow

```
ENHANCED CONVERSIONS FOR LEADS
══════════════════════════════

USE CASE:
─────────
Lead wordt offline gekwalificeerd/geconverteerd
Bijv: Form submit → Sales call → Close deal

FLOW:
─────
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  1. User clicks ad               2. User submits form           │
│     └─► GCLID captured              └─► Lead data + GCLID saved │
│                                                                  │
│  3. Enhanced conv captures       4. Lead qualifies (offline)    │
│     └─► Email hashed & sent         └─► In CRM: status updated  │
│                                                                  │
│  5. Upload offline conversion    6. Attribution complete        │
│     └─► Via API, GCLID match        └─► Google Ads sees close   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

STAP 1: CAPTURE GCLID
─────────────────────
JavaScript om GCLID te capturen:

<script>
function getGclid() {
  var params = new URLSearchParams(window.location.search);
  var gclid = params.get('gclid');
  if (gclid) {
    // Store in cookie (30 days)
    var d = new Date();
    d.setTime(d.getTime() + 30*24*60*60*1000);
    document.cookie = "gclid=" + gclid + ";expires=" + d.toUTCString() + ";path=/";

    // Store in hidden form field
    var gclidField = document.getElementById('gclid');
    if (gclidField) gclidField.value = gclid;
  }
}
window.onload = getGclid;
</script>

STAP 2: STORE IN CRM
────────────────────
Bij form submit, sla op:
├── Lead data (email, phone, name)
├── GCLID (als aanwezig)
├── Timestamp van conversie
└── UTM parameters

STAP 3: ENABLE IN GOOGLE ADS
────────────────────────────
1. Conversions → [Lead Conversion] → Edit
2. Enhanced conversions for leads: ON
3. Choose method: Google tag or API

STAP 4: OFFLINE CONVERSION IMPORT
─────────────────────────────────
Wanneer lead converteert (sale):
1. Export uit CRM: email + GCLID + conversion time + value
2. Upload via Google Ads UI of API
3. Google matched met enhanced conversion data
```

### Offline Conversion Import

```
OFFLINE CONVERSION IMPORT SETUP
═══════════════════════════════

OPTIE 1: MANUAL UPLOAD (UI)
───────────────────────────
1. Tools → Conversions → Uploads
2. Template downloaden
3. Vul in:
   ├── Google Click ID (GCLID)
   ├── Conversion Name (exact match)
   ├── Conversion Time (timezone aware)
   └── Conversion Value

4. Upload CSV
5. Monitor status

CSV FORMAT:
───────────
Google Click ID,Conversion Name,Conversion Time,Conversion Value
EAIaIQobChMI...,Lead Qualified,2025-01-15 14:30:00+01:00,500

OPTIE 2: GOOGLE ADS API
───────────────────────
Voor automatische sync vanuit CRM:

// Python example (Google Ads API)
from google.ads.googleads.client import GoogleAdsClient

def upload_offline_conversion(client, customer_id, gclid, conversion_action_id, conversion_datetime, conversion_value):
    conversion_upload_service = client.get_service("ConversionUploadService")

    click_conversion = client.get_type("ClickConversion")
    click_conversion.gclid = gclid
    click_conversion.conversion_action = f"customers/{customer_id}/conversionActions/{conversion_action_id}"
    click_conversion.conversion_date_time = conversion_datetime
    click_conversion.conversion_value = conversion_value
    click_conversion.currency_code = "EUR"

    request = client.get_type("UploadClickConversionsRequest")
    request.customer_id = customer_id
    request.conversions = [click_conversion]
    request.partial_failure = True

    response = conversion_upload_service.upload_click_conversions(request=request)
    return response

OPTIE 3: ENHANCED CONVERSIONS FOR LEADS (Zonder GCLID)
──────────────────────────────────────────────────────
Als GCLID niet beschikbaar:

1. Bij form submit: stuur email (hashed) naar Google
2. Bij offline sale: upload met zelfde email (hashed)
3. Google matched op basis van hashed email

// CSV met enhanced matching
Email,Conversion Name,Conversion Time,Conversion Value
8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92,Lead Qualified,2025-01-15,500

⚠️ Email moet SHA256 gehasht zijn
```

## Consent Mode V2 Implementatie

### Consent Mode Setup

```
CONSENT MODE V2 IMPLEMENTATIE
═════════════════════════════

WAAROM VERPLICHT (EU, Maart 2024):
──────────────────────────────────
□ Google vereist consent signals voor personalisatie
□ Remarketing audiences werken niet zonder consent
□ Enhanced conversions vereist ad_user_data consent
□ Measurement kan doorgaan met conversion modeling

CONSENT TYPES:
──────────────
ad_storage         - Advertising cookies
analytics_storage  - Analytics cookies
ad_user_data      - First-party data voor ads (NIEUW)
ad_personalization - Personalized ads (NIEUW)

IMPLEMENTATIE VIA GTM:
──────────────────────

1. DEFAULT CONSENT STATE
────────────────────────
In GTM: Tags → Consent Initialization - All Pages

<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}

// Default: denied (EU users)
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'wait_for_update': 500  // Wait for CMP
});

// Region-specific defaults
gtag('consent', 'default', {
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted',
  'region': ['US', 'CA']  // Non-EU = granted
});
</script>

2. CONSENT UPDATE (Na CMP interactie)
─────────────────────────────────────
Je CMP (Cookiebot, OneTrust, etc.) moet triggeren:

<script>
gtag('consent', 'update', {
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted'
});
</script>

3. GTM CONSENT MODE SETTINGS
────────────────────────────
1. Admin → Container Settings
2. Enable consent overview
3. Per tag: configure consent requirements
4. Google tags: Require ad_storage, ad_user_data

CONSENT MODE BEHAVIOR:
──────────────────────
┌─────────────────────┬─────────────────────────────────────────┐
│ Consent State       │ Behavior                                │
├─────────────────────┼─────────────────────────────────────────┤
│ ad_storage: denied  │ Geen advertising cookies                │
│ ad_user_data: denied│ Geen first-party data naar Google      │
│ analytics: denied   │ Geen analytics cookies                  │
│                     │                                         │
│ ALL denied          │ Cookieless pings (voor modeling)       │
│                     │ Conversion modeling actief              │
│                     │ Enhanced conversions: NIET actief       │
├─────────────────────┼─────────────────────────────────────────┤
│ ALL granted         │ Full tracking                           │
│                     │ Enhanced conversions: ACTIEF            │
│                     │ Remarketing: ACTIEF                     │
└─────────────────────┴─────────────────────────────────────────┘
```

### CMP Integratie

```
CMP (CONSENT MANAGEMENT PLATFORM) SETUP
════════════════════════════════════════

POPULAIRE CMPs MET NATIVE GTM INTEGRATIE:
─────────────────────────────────────────
□ Cookiebot
□ OneTrust
□ Usercentrics
□ Cookie Information
□ Complianz (WordPress)

COOKIEBOT VOORBEELD:
────────────────────

1. Maak Cookiebot account
2. Configureer cookie categorieën:
   ├── Necessary: altijd enabled
   ├── Preference: analytics_storage
   ├── Statistics: analytics_storage
   └── Marketing: ad_storage, ad_user_data, ad_personalization

3. GTM Setup:
   └── Cookiebot biedt template in GTM Gallery

4. Mapping Cookiebot → Consent Mode:
   ├── marketing=true → ad_storage: granted
   ├── marketing=true → ad_user_data: granted
   ├── marketing=true → ad_personalization: granted
   └── statistics=true → analytics_storage: granted

GTM TRIGGER VOOR CONSENT UPDATE:
────────────────────────────────
Trigger Type: Custom Event
Event Name: cookie_consent_update

OF via Cookiebot listener:
window.addEventListener('CookiebotOnAccept', function() {
  if (Cookiebot.consent.marketing) {
    gtag('consent', 'update', {
      'ad_storage': 'granted',
      'ad_user_data': 'granted',
      'ad_personalization': 'granted'
    });
  }
});
```

## Server-Side Tagging

### GTM Server Container Setup

```
SERVER-SIDE TAGGING SETUP
═════════════════════════

VOORDELEN:
──────────
□ First-party context (je eigen domain)
□ Meer controle over data naar vendors
□ Beter tegen ad blockers
□ Lagere page load impact
□ GDPR compliance (data blijft in EU)

HOSTING OPTIES:
───────────────
1. Google Cloud Run (aanbevolen)
   ├── Auto-scaling
   ├── Pay-per-use
   └── ~€50-200/maand voor medium traffic

2. Manual deployment (AWS, Azure)
   └── Meer controle, meer werk

SETUP STAPPEN:
──────────────

1. GTM SERVER CONTAINER MAKEN
─────────────────────────────
1. tagmanager.google.com
2. Create Container → Server
3. Kies: Manually provision

2. CLOUD RUN DEPLOYMENT
───────────────────────
1. Cloud Run → Create Service
2. Container image: gcr.io/cloud-tagging-public/gtm-cloud-image:stable
3. Environment variables:
   ├── CONTAINER_CONFIG: [van GTM]
   ├── PORT: 8080
4. Allow unauthenticated invocations
5. Set region (EU voor GDPR)

3. CUSTOM DOMAIN SETUP
──────────────────────
□ Subdomain van je site: data.jouwsite.nl
□ DNS: CNAME naar Cloud Run URL
□ SSL: automatisch via Google

4. CLIENT-SIDE GTM AANPASSEN
────────────────────────────
Google tag configuratie:
├── server_container_url: https://data.jouwsite.nl
└── First-party mode: enabled

5. SERVER-SIDE TAGS CONFIGUREREN
────────────────────────────────
In Server Container:
├── GA4 Client (ontvangt hits)
├── Google Ads Conversion Tracking tag
├── Enhanced Conversions tag
└── Consent Mode settings

ARCHITECTUUR:
─────────────
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  Browser                Server Container          Third Parties │
│  ─────────             ─────────────────         ───────────── │
│                                                                  │
│  GTM Web Container ──────► Server Container ──────► Google Ads  │
│  (sends to your domain)   (data.jouwsite.nl)      (via API)    │
│                                                                  │
│  VOORDEEL: Eerste request is first-party (jouw domain)         │
│  Ad blockers blokkeren niet                                     │
│  Je controleert welke data doorgaat                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Server-Side Enhanced Conversions

```
ENHANCED CONVERSIONS VIA SERVER-SIDE
════════════════════════════════════

SETUP IN SERVER CONTAINER:

1. GA4 CLIENT
─────────────
□ Klant ontvangt alle hits van web container
□ Parse user_data uit requests

2. GOOGLE ADS CONVERSION TAG (Server)
─────────────────────────────────────
Tag Type: Google Ads Conversion Tracking

Settings:
├── Conversion ID: [van Google Ads]
├── Conversion Label: [van Google Ads]
├── Use Data Layer: enhanced_conversion_data
└── Hash user data: enabled (als plain text)

3. STAG ENHANCED CONVERSIONS TAG
────────────────────────────────
Dedicated tag voor enhanced conversions:

Tag Type: Google Ads: User-Provided Data

Settings:
├── Email: {{user_data.email}}
├── Phone: {{user_data.phone}}
├── First Name: {{user_data.first_name}}
├── Last Name: {{user_data.last_name}}
├── Street: {{user_data.address.street}}
├── City: {{user_data.address.city}}
├── Postal Code: {{user_data.address.postal_code}}
├── Country: {{user_data.address.country}}
└── Hash data: enabled

TRIGGER:
────────
Event Name: purchase, form_submit, etc.
Condition: user_data aanwezig
```

## Diagnostics & Troubleshooting

### Enhanced Conversions Diagnostics

```
DIAGNOSTICS CHECKLIST
═════════════════════

GOOGLE ADS UI CHECK:
────────────────────
1. Tools → Conversions → [Conversie]
2. Check "Diagnostics" tab
3. Status should show:
   ├── "Recording conversions": Active
   ├── "Enhanced conversions": Active
   └── "Data quality": Good/Excellent

COMMON ISSUES:
──────────────

ISSUE: "Not receiving enhanced conversion data"
CAUSES:
├── Tag niet correct geconfigureerd
├── Consent niet granted
├── Form velden niet gevonden (auto mode)
FIXES:
├── Verify tag setup in GTM
├── Check consent mode signals
└── Switch naar manual data layer

ISSUE: "Low match rate"
CAUSES:
├── Data niet correct geformatteerd
├── Alleen email, geen phone/name
├── Hash mismatch
FIXES:
├── Normalize data (lowercase, trim)
├── Add more data points
└── Verify hashing (of stuur plain text)

ISSUE: "Enhanced conversions not recording"
CAUSES:
├── Conversion action niet geconfigureerd
├── Tag fires maar geen data
├── Consent denied voor ad_user_data
FIXES:
├── Enable in conversion settings
├── Add user-provided data to tag
└── Check consent mode implementation

VERIFICATION SCRIPT:
────────────────────
// Console check voor enhanced conversions data
console.log('Checking enhanced conversions data...');
if (window.google_tag_manager) {
  // Check dataLayer
  var dl = window.dataLayer || [];
  var ecData = dl.find(function(item) {
    return item.enhanced_conversion_data;
  });
  if (ecData) {
    console.log('Enhanced Conversion Data Found:', ecData.enhanced_conversion_data);
  } else {
    console.warn('No enhanced_conversion_data in dataLayer');
  }
}
```

## Google Ads Script: Enhanced Conversions Monitor

```javascript
/**
 * Enhanced Conversions Health Monitor
 *
 * Monitort enhanced conversion status en diagnostics
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Schedule: Wekelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',
  MIN_MATCH_RATE: 0.4 // 40% minimum match rate
};

function main() {
  var report = {
    conversions: [],
    issues: []
  };

  // Check conversion actions
  var conversionActions = AdsApp.conversions().get();

  while (conversionActions.hasNext()) {
    var conversion = conversionActions.next();
    var name = conversion.getName();

    // Enhanced conversions status is niet direct beschikbaar via API
    // Dit script logt conversie configuratie voor manual review

    report.conversions.push({
      name: name,
      category: conversion.getCategory(),
      status: conversion.isEnabled() ? 'Enabled' : 'Disabled',
      countingType: conversion.getCountingType()
    });
  }

  // Generate summary
  var enabledCount = report.conversions.filter(function(c) {
    return c.status === 'Enabled';
  }).length;

  Logger.log('Conversion Actions Report');
  Logger.log('========================');
  Logger.log('Total conversions: ' + report.conversions.length);
  Logger.log('Enabled: ' + enabledCount);

  // Log details
  for (var i = 0; i < report.conversions.length; i++) {
    var conv = report.conversions[i];
    Logger.log('');
    Logger.log('Conversion: ' + conv.name);
    Logger.log('  Category: ' + conv.category);
    Logger.log('  Status: ' + conv.status);
    Logger.log('  Counting: ' + conv.countingType);
  }

  // Recommendations
  Logger.log('');
  Logger.log('RECOMMENDATIONS:');
  Logger.log('----------------');
  Logger.log('1. Check Google Ads UI → Conversions → Diagnostics');
  Logger.log('   for enhanced conversions match rate');
  Logger.log('2. Target match rate: 40%+ for good attribution');
  Logger.log('3. Add more data points (phone, name) for better matching');
}
```

## Output: Enhanced Conversions Implementation Plan

```markdown
# Enhanced Conversions Implementation Plan

## Huidige Status
- **Enhanced Conversions status:** [Not enabled / Enabled - Web / Enabled - Leads]
- **Consent Mode V2:** [Not implemented / Implemented]
- **Server-side tagging:** [No / Yes]
- **Huidige conversion tracking:** [Client-side only / Mixed]

## Implementation Checklist

### Phase 1: Consent Mode V2 (Week 1)
- [ ] CMP gekozen/geconfigureerd
- [ ] Default consent state ingesteld (denied voor EU)
- [ ] Consent update triggers werkend
- [ ] GTM tags configureren met consent requirements
- [ ] Testing: consent flows werken correct

### Phase 2: Enhanced Conversions for Web (Week 2)
- [ ] Conversion action enhanced conversions enabled
- [ ] Data layer setup voor form data
- [ ] GTM User-Provided Data variable gemaakt
- [ ] Google Ads Conversion tag updated
- [ ] Testing: user_data in tag assistant zichtbaar

### Phase 3: Enhanced Conversions for Leads (Week 3)
- [ ] GCLID capture script geïmplementeerd
- [ ] CRM velden toegevoegd (GCLID storage)
- [ ] Offline conversion import process opgezet
- [ ] API integratie of manual upload workflow
- [ ] Testing: offline conversions matchen

### Phase 4: Server-Side Tagging (Optional, Week 4+)
- [ ] Server container deployed (Cloud Run)
- [ ] Custom domain geconfigureerd
- [ ] Clients en tags gemigreerd
- [ ] Testing: server-side conversions werken

## Data Requirements

### Velden te capturen:
| Field | Format | Required |
|-------|--------|----------|
| Email | lowercase, trimmed | Yes |
| Phone | E.164 (+31612345678) | Recommended |
| First Name | lowercase | Recommended |
| Last Name | lowercase | Recommended |
| Street | street + number | Optional |
| City | full name | Optional |
| Postal Code | no spaces | Optional |
| Country | ISO alpha-2 | Optional |

## Success Metrics
- [ ] Enhanced conversions match rate: Target 40%+
- [ ] Consent rate: Track % granted vs denied
- [ ] Conversion delta: Compare before/after EC implementation
- [ ] Attribution improvement: Measured vs modeled conversions
```

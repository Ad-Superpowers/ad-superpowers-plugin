---
name: conversion-tracking-setup
description: "Complete Google Ads conversion tracking implementatie gids. Gebruik voor: (1) Conversion actions configureren, (2) Google Tag setup, (3) Enhanced Conversions implementatie, (4) Value tracking opzetten, (5) Offline conversions importeren, (6) Primary vs secondary conversions. Triggers: conversion tracking, google tag, gtag, enhanced conversions, offline conversions, conversion value, attribution."
---

# Conversion Tracking Setup

Complete gids voor het correct opzetten en optimaliseren van Google Ads conversion tracking, inclusief Enhanced Conversions en offline conversion import.

## Conversion Tracking Methoden

```
WELKE TRACKING METHODE?
=======================

┌─────────────────────────────────────────────────────────────────┐
│  METHODE                 │ BEST FOR                            │
├──────────────────────────┼─────────────────────────────────────┤
│ Google Ads Tag (gtag.js) │ Meeste accuraatheid, Smart Bidding  │
│                          │ optimization, Enhanced Conversions   │
├──────────────────────────┼─────────────────────────────────────┤
│ GA4 Imported Conversions │ Cross-platform view, unified        │
│                          │ reporting, als GA4 al geïmplementeerd│
├──────────────────────────┼─────────────────────────────────────┤
│ Google Tag Manager       │ Complex implementations, developer  │
│                          │ control, meerdere platforms         │
├──────────────────────────┼─────────────────────────────────────┤
│ Server-Side GTM          │ Hoogste data quality, iOS tracking, │
│                          │ privacy-first setup                  │
└──────────────────────────┴─────────────────────────────────────┘

AANBEVELING:
├── E-commerce: Google Ads Tag + Enhanced Conversions
├── Lead Gen: Google Ads Tag + Offline Conversion Import
├── Complex Setup: GTM + Server-Side
└── GA4 Heavy Users: GA4 Import (maar verliest wat features)
```

## Conversion Actions Configuratie

### Conversion Action Types

```
CONVERSION ACTION TYPES
=======================

PURCHASE (E-commerce)
├── Category: Purchase
├── Value: Dynamic (transaction value)
├── Count: Every conversion
├── Window: 30-90 dagen
└── Include in Conversions: YES

LEAD (Lead Gen)
├── Category: Submit lead form
├── Value: Static of dynamic lead value
├── Count: One per click
├── Window: 30-90 dagen
└── Include in Conversions: YES (primary)

SIGN UP (SaaS/Registration)
├── Category: Sign-up
├── Value: Static (estimated value)
├── Count: One per click
├── Window: 30-60 dagen
└── Include in Conversions: YES/NO (based on funnel)

PAGE VIEW (Micro-conversions)
├── Category: Page view
├── Value: Static (klein)
├── Count: One per click
├── Window: 7-30 dagen
└── Include in Conversions: NO (observation only)

PHONE CALL
├── Category: Phone call
├── Value: Per call of static
├── Count: One/Every (based on use case)
├── Window: 30 dagen
└── Include in Conversions: YES
```

### Primary vs Secondary Conversions

```
PRIMARY VS SECONDARY CONVERSIONS
================================

PRIMARY CONVERSIONS:
├── "Include in Conversions: YES"
├── Gebruikt voor Smart Bidding optimalisatie
├── Telt mee in "Conversions" kolom
└── Kies: Je hoofddoel (purchase, lead, etc.)

SECONDARY CONVERSIONS:
├── "Include in Conversions: NO"
├── NIET gebruikt voor bidding
├── Zichtbaar in "All Conversions" kolom
└── Kies: Micro-conversions, observation metrics

BEST PRACTICE:
──────────────
E-commerce:
├── Primary: Purchase
├── Secondary: Add to Cart, Begin Checkout, View Product

Lead Gen:
├── Primary: Qualified Lead (of SQL)
├── Secondary: Form Submit, Click-to-Call, PDF Download

SaaS:
├── Primary: Trial Start of Signup
├── Secondary: Feature Engagement, Pricing Page View
```

### Conversion Settings

```
CONVERSION SETTINGS DETAIL
==========================

COUNT:
├── "Every": Elke conversie telt (e-commerce: elke purchase)
├── "One": Eén conversie per click (leads: één lead per click)
└── Advies: Purchases = Every, Leads = One

CONVERSION WINDOW:
├── Click-through: 30-90 dagen (standaard 30)
├── View-through: 1-30 dagen (standaard 1)
├── Engaged-view: 3-30 dagen (standaard 3)
└── Advies: Pas aan op basis van sales cycle

ATTRIBUTION MODEL:
├── Data-driven (aanbevolen, default sinds 2024)
├── Last click
├── First click
├── Linear / Time decay / Position-based (deprecated)
└── Advies: Gebruik Data-driven (DDA)
```

## Google Ads Tag Setup

### Basic Tag Implementation

```html
<!-- Google Tag (gtag.js) - BASE CODE -->
<!-- Plaats in <head> van elke pagina -->

<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  // Google Ads Tag
  gtag('config', 'AW-XXXXXXXXX');
</script>
```

### Conversion Event Implementation

```html
<!-- PURCHASE CONVERSION (E-commerce) -->
<!-- Plaats op bedankpagina / order confirmation -->

<script>
  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/YYYYYYYYYYYY',
    'value': 150.00,                    // Transactiewaarde
    'currency': 'EUR',                  // Valuta
    'transaction_id': 'ORDER-12345'     // Unieke order ID (deduplicatie)
  });
</script>

<!-- LEAD CONVERSION -->
<!-- Plaats op bedankpagina na form submit -->

<script>
  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/ZZZZZZZZZZZZ',
    'value': 50.00,                     // Geschatte lead waarde
    'currency': 'EUR'
  });
</script>

<!-- PHONE CALL CONVERSION -->
<!-- Via Google forwarding number of handmatig -->

<script>
  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/CALLCONVID',
    'value': 25.00,
    'currency': 'EUR'
  });
</script>
```

### Dynamic Value Tracking

```javascript
// DYNAMIC VALUE TRACKING (E-commerce)
// Haal transactiewaarde op uit je e-commerce platform

// Voorbeeld voor standaard e-commerce
<script>
  // Zorg dat deze variabelen beschikbaar zijn op confirmation page
  var orderValue = {{order_total}};      // Vul in vanuit platform
  var orderId = '{{order_id}}';          // Unieke order ID
  var orderCurrency = 'EUR';

  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/YYYYYYYYYYYY',
    'value': orderValue,
    'currency': orderCurrency,
    'transaction_id': orderId
  });
</script>

// DYNAMIC VALUE MET ITEMS (Enhanced E-commerce)
<script>
  gtag('event', 'purchase', {
    'send_to': 'AW-XXXXXXXXX/YYYYYYYYYYYY',
    'value': 150.00,
    'currency': 'EUR',
    'transaction_id': 'ORDER-12345',
    'items': [
      {
        'id': 'SKU001',
        'name': 'Product Naam',
        'quantity': 2,
        'price': 75.00
      }
    ]
  });
</script>
```

## Enhanced Conversions

### Wat Zijn Enhanced Conversions?

```
ENHANCED CONVERSIONS UITLEG
===========================

WAT:
├── Verzend first-party data (email, phone, name, address)
├── Data wordt gehasht (SHA256) voor privacy
├── Google matcht met ingelogde users
└── Verbetert conversie attributie, vooral na iOS 14.5

VOORDELEN:
├── +5-15% meer gemeten conversies
├── Betere cross-device tracking
├── Resilient tegen cookie blocking
├── Verbeterde Smart Bidding optimization
└── Vereist voor optimale performance

TYPES:
├── Enhanced Conversions for Web: Website purchases/leads
├── Enhanced Conversions for Leads: Offline lead tracking
└── Customer Match: Audience building
```

### Enhanced Conversions for Web (GTM)

```
GTM SETUP: ENHANCED CONVERSIONS FOR WEB
========================================

STAP 1: Enable in Google Ads
────────────────────────────
1. Goals → Conversions → Settings
2. Enhanced conversions: Turn on
3. Kies: Google Tag Manager

STAP 2: GTM Configuratie
────────────────────────
1. Google Ads Conversion Tracking Tag aanpassen
2. "Include user-provided data from your website": ✓
3. Data source kiezen:
   - New Variable: User-Provided Data
   - Of: Data Layer

STAP 3: User Data Variable Setup (GTM)
──────────────────────────────────────
Variable Type: User-Provided Data
Data Source: Manual Configuration of Data Layer

VELDEN (minimaal email):
├── Email: {{user_email}}
├── Phone: {{user_phone}}
├── First Name: {{user_firstname}}
├── Last Name: {{user_lastname}}
├── Street: {{user_street}}
├── City: {{user_city}}
├── Postal Code: {{user_zip}}
└── Country: {{user_country}}
```

### Enhanced Conversions Code (Direct)

```javascript
// ENHANCED CONVERSIONS - DIRECT IMPLEMENTATION
// Verstuur user data met conversie event

<script>
  // Methode 1: Via gtag set command (aanbevolen)
  gtag('set', 'user_data', {
    'email': 'klant@email.com',           // Plain text of SHA256
    'phone_number': '+31612345678',       // E.164 format
    'address': {
      'first_name': 'Jan',
      'last_name': 'Jansen',
      'street': 'Hoofdstraat 123',
      'city': 'Amsterdam',
      'postal_code': '1012AB',
      'country': 'NL'
    }
  });

  // Daarna conversion event
  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/YYYYYYYYYYYY',
    'value': 150.00,
    'currency': 'EUR',
    'transaction_id': 'ORDER-12345'
  });
</script>

// Methode 2: SHA256 hashing (privacy-first)
<script>
  async function hashData(data) {
    const encoder = new TextEncoder();
    const dataBuffer = encoder.encode(data.toLowerCase().trim());
    const hashBuffer = await crypto.subtle.digest('SHA-256', dataBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  }

  async function sendConversion() {
    const hashedEmail = await hashData('klant@email.com');

    gtag('set', 'user_data', {
      'sha256_email_address': hashedEmail
    });

    gtag('event', 'conversion', {
      'send_to': 'AW-XXXXXXXXX/YYYYYYYYYYYY',
      'value': 150.00,
      'currency': 'EUR',
      'transaction_id': 'ORDER-12345'
    });
  }

  sendConversion();
</script>
```

## Enhanced Conversions for Leads

### Lead Conversion Flow

```
ENHANCED CONVERSIONS FOR LEADS
==============================

DOEL:
├── Match offline sales data met ads clicks
├── Optimaliseer op echte sales, niet form fills
├── Importeer lead → opportunity → closed won data
└── Smart Bidding leert op high-quality leads

FLOW:
─────
1. User klikt op ad
2. User vult form in (email captured)
3. Form submit = "conversion" event MET email
4. Lead gaat naar CRM
5. Lead wordt qualified/closed
6. Import qualified lead terug naar Google Ads
7. Smart Bidding leert wat goede leads zijn
```

### Setup Lead Enhanced Conversions

```javascript
// LEAD FORM SUBMISSION - ENHANCED CONVERSIONS
// Verstuur bij form submission

<script>
  // Bij form submit, verzamel user data
  document.getElementById('leadForm').addEventListener('submit', function(e) {
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;

    // Set user data
    gtag('set', 'user_data', {
      'email': email,
      'phone_number': phone
    });

    // Fire conversion
    gtag('event', 'conversion', {
      'send_to': 'AW-XXXXXXXXX/LEADCONVID',
      'value': 50.00,
      'currency': 'EUR'
    });
  });
</script>
```

## Offline Conversion Import

### Wanneer Offline Conversions Gebruiken

```
OFFLINE CONVERSION USE CASES
============================

1. LEAD GEN (B2B)
   ├── Online: Form submit
   ├── Offline: Lead → Opportunity → Closed Won
   └── Import: Qualified leads en deals

2. E-COMMERCE (High-value)
   ├── Online: Quote request
   ├── Offline: Sales call → Purchase
   └── Import: Completed purchases

3. HYBRID BUSINESSES
   ├── Online: Store locator, book appointment
   ├── Offline: In-store purchase
   └── Import: In-store transactions

4. CALL TRACKING
   ├── Online: Click-to-call
   ├── Offline: Call qualified/resulted in sale
   └── Import: Qualified calls
```

### Offline Conversion Setup

```
OFFLINE CONVERSION SETUP
========================

METHODE 1: GCLID-based (Traditioneel)
─────────────────────────────────────
1. Capture GCLID bij click
   - URL parameter: ?gclid=XXXXX
   - Sla op in CRM bij lead record

2. Create Offline Conversion Action
   - Google Ads → Goals → Conversions → + New
   - Type: Import → CRM, files, or other sources
   - Naam: "Qualified Lead" of "Closed Won"

3. Import conversions
   - Via Upload (CSV/Google Sheets)
   - Via API (automated)
   - Via Partner integration (Salesforce, HubSpot, etc.)

UPLOAD FORMAT:
Parameters:
├── Google Click ID (GCLID)
├── Conversion Name
├── Conversion Time
├── Conversion Value
└── Conversion Currency

METHODE 2: Enhanced Conversions for Leads
─────────────────────────────────────────
1. Capture user data bij form submit (email, phone)
2. Send Enhanced Conversion event
3. Import offline conversions met zelfde user data
4. Google matcht op basis van gehashte data

VOORDEEL: Geen GCLID capturing nodig
```

### Offline Conversion Upload Template

```csv
# CSV FORMAT VOOR OFFLINE CONVERSIONS (GCLID)
Google Click ID,Conversion Name,Conversion Time,Conversion Value,Conversion Currency
EAIaIQobChMI...,Qualified Lead,2025-01-28 14:30:00,50,EUR
EAIaIQobChMI...,Closed Won,2025-01-28 15:45:00,5000,EUR

# CSV FORMAT VOOR ENHANCED CONVERSIONS FOR LEADS
Email,Conversion Name,Conversion Time,Conversion Value,Conversion Currency
klant@email.com,Qualified Lead,2025-01-28 14:30:00,50,EUR
```

### Automated Import via API

```python
# PYTHON SCRIPT VOOR OFFLINE CONVERSION UPLOAD
# Gebruik de Google Ads API

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

def upload_offline_conversions(customer_id, conversions):
    """
    Upload offline conversions naar Google Ads.

    Args:
        customer_id: Google Ads customer ID
        conversions: List van conversion dicts
    """
    client = GoogleAdsClient.load_from_storage()
    conversion_upload_service = client.get_service("ConversionUploadService")
    conversion_action_service = client.get_service("ConversionActionService")

    # Build conversion operations
    operations = []
    for conv in conversions:
        click_conversion = client.get_type("ClickConversion")
        click_conversion.gclid = conv['gclid']
        click_conversion.conversion_action = f"customers/{customer_id}/conversionActions/{conv['conversion_action_id']}"
        click_conversion.conversion_date_time = conv['conversion_time']
        click_conversion.conversion_value = conv['value']
        click_conversion.currency_code = conv['currency']

        operations.append(click_conversion)

    # Upload
    request = client.get_type("UploadClickConversionsRequest")
    request.customer_id = customer_id
    request.conversions = operations
    request.partial_failure = True

    response = conversion_upload_service.upload_click_conversions(request=request)

    print(f"Uploaded {len(response.results)} conversions")
    return response

# Voorbeeld gebruik
conversions = [
    {
        'gclid': 'EAIaIQobChMI...',
        'conversion_action_id': '123456789',
        'conversion_time': '2025-01-28 14:30:00+01:00',
        'value': 50.00,
        'currency': 'EUR'
    }
]

upload_offline_conversions('123-456-7890', conversions)
```

## Consent Mode v2

### Consent Mode Implementatie

```
CONSENT MODE V2 (Vereist voor EU)
=================================

WAT:
├── Respecteert user consent preferences
├── Past tag behavior aan op basis van consent
├── Verzamelt geaggregeerde data zonder consent
├── Gebruikt modelling om gaps op te vullen
└── VEREIST voor adverteren in EU vanaf maart 2024

CONSENT TYPES:
├── ad_storage: Advertising cookies
├── analytics_storage: Analytics cookies
├── ad_user_data: Send user data for ads (NIEUW)
├── ad_personalization: Personalized ads
└── functionality_storage: Functional cookies
```

### Consent Mode Code

```html
<!-- CONSENT MODE DEFAULT STATE -->
<!-- Plaats VOOR gtag.js laden -->

<script>
  // Default consent state (denied)
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}

  gtag('consent', 'default', {
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'analytics_storage': 'denied',
    'wait_for_update': 500  // Wacht op CMP
  });

  // Enable URL passthrough voor cross-domain
  gtag('set', 'url_passthrough', true);

  // Enable ads data redaction when denied
  gtag('set', 'ads_data_redaction', true);
</script>

<!-- Na user consent (via CMP) -->
<script>
  // Update consent state wanneer user accepteert
  function updateConsent(adConsent, analyticsConsent) {
    gtag('consent', 'update', {
      'ad_storage': adConsent ? 'granted' : 'denied',
      'ad_user_data': adConsent ? 'granted' : 'denied',
      'ad_personalization': adConsent ? 'granted' : 'denied',
      'analytics_storage': analyticsConsent ? 'granted' : 'denied'
    });
  }

  // Voorbeeld: User klikt "Accept All"
  document.getElementById('acceptAll').addEventListener('click', function() {
    updateConsent(true, true);
  });
</script>
```

## Tracking Verification

### Conversion Tracking Test Checklist

```
TRACKING VERIFICATIE CHECKLIST
==============================

□ BASIC SETUP
├── Google Tag geladen op alle pagina's?
├── Tag ID correct (AW-XXXXXXXXX)?
├── Geen JavaScript errors in console?
└── Test in Tag Assistant (legacy) of Preview mode

□ CONVERSION EVENTS
├── Event fires op juiste pagina/actie?
├── Correct conversion ID/label?
├── Value correct doorgestuurd?
├── Transaction ID uniek per conversie?
└── Currency correct (EUR, USD)?

□ ENHANCED CONVERSIONS
├── User data wordt meegezonden?
├── Email format correct?
├── Phone in E.164 format (+31...)?
├── Data gehashed of plain text (beide OK)?
└── Status: "Recording" in Google Ads

□ REAL-TIME CHECK
├── Maak test conversie
├── Check in Google Ads → Conversions → Recent
├── Controleer value en details
└── Latency: Max 3-6 uur voor zichtbaarheid

□ DATA QUALITY
├── Geen duplicate conversies
├── Values zijn realistisch
├── Conversion rate is logisch
└── Vergelijk met GA4/backend data
```

### Debugging Script

```javascript
/**
 * Conversion Tracking Debug Helper
 *
 * Voeg toe aan console om tracking te debuggen
 */

(function() {
  // Check if gtag exists
  if (typeof gtag === 'undefined') {
    console.error('❌ gtag not found! Google Tag not loaded.');
    return;
  }
  console.log('✓ gtag found');

  // Check dataLayer
  if (window.dataLayer) {
    console.log('✓ dataLayer exists with', window.dataLayer.length, 'items');

    // Find conversion events
    var conversions = window.dataLayer.filter(function(item) {
      return item[0] === 'event' && item[1] === 'conversion';
    });

    if (conversions.length > 0) {
      console.log('✓ Found', conversions.length, 'conversion event(s)');
      conversions.forEach(function(conv, i) {
        console.log('  Conversion', i + 1, ':', conv);
      });
    } else {
      console.warn('⚠ No conversion events found in dataLayer');
    }

    // Find user_data
    var userData = window.dataLayer.filter(function(item) {
      return item[0] === 'set' && item[1] === 'user_data';
    });

    if (userData.length > 0) {
      console.log('✓ Enhanced Conversions user_data found');
    } else {
      console.warn('⚠ No user_data found - Enhanced Conversions may not be active');
    }

    // Find consent events
    var consent = window.dataLayer.filter(function(item) {
      return item[0] === 'consent';
    });
    console.log('✓ Consent events:', consent.length);

  } else {
    console.error('❌ dataLayer not found!');
  }

  // Check for common issues
  var scripts = document.querySelectorAll('script[src*="googletagmanager.com/gtag"]');
  if (scripts.length === 0) {
    console.error('❌ Google Tag script not found in DOM');
  } else if (scripts.length > 1) {
    console.warn('⚠ Multiple Google Tag scripts found - may cause issues');
  } else {
    console.log('✓ Google Tag script found');
  }

})();
```

## Conversion Tracking Audit

```markdown
# Conversion Tracking Audit Report

## Account Info
- Account ID: [AW-XXXXXXXXX]
- Date: [DATUM]
- Auditor: [NAAM]

## Conversion Actions Summary

| Action Name | Type | Primary | Value | Count | Status |
|-------------|------|---------|-------|-------|--------|
| Purchase | Sale | Yes | Dynamic | Every | ✓ |
| Lead Form | Lead | Yes | €50 | One | ✓ |
| Add to Cart | Engagement | No | - | Every | ✓ |

## Tracking Implementation

### Tag Status
- [ ] Google Tag installed: [Yes/No]
- [ ] Tag on all pages: [Yes/No]
- [ ] No console errors: [Yes/No]
- [ ] Consent Mode active: [Yes/No]

### Enhanced Conversions
- [ ] Enabled in Google Ads: [Yes/No]
- [ ] User data sent: [Yes/No]
- [ ] Match rate: [X%]
- [ ] Data fields: [email, phone, etc.]

### Data Quality
- [ ] Conversion rate logical: [Yes/No]
- [ ] Values accurate: [Yes/No]
- [ ] No duplicates: [Yes/No]
- [ ] GA4 comparison: [Match/Discrepancy X%]

## Issues Found

1. **[Issue]**
   - Impact: [High/Medium/Low]
   - Fix: [Description]

2. **[Issue]**
   - Impact: [High/Medium/Low]
   - Fix: [Description]

## Recommendations

1. [Recommendation with priority]
2. [Recommendation with priority]
3. [Recommendation with priority]

## Action Plan

### Week 1
- [ ] [Action item]
- [ ] [Action item]

### Week 2-4
- [ ] [Action item]
- [ ] [Action item]
```

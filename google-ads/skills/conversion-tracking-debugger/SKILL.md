---
name: conversion-tracking-debugger
description: "Diagnose en fix Google Ads conversion tracking problemen. Gebruik voor: (1) Conversies niet zichtbaar, (2) Dubbele conversies, (3) GA4 vs Google Ads discrepanties, (4) Enhanced Conversions issues, (5) Offline conversion problemen, (6) Tag firing issues. Triggers: conversions not showing, conversion missing, tracking broken, duplicate conversions, conversion discrepancy, tag not firing, GCLID issues."
---

# Conversion Tracking Debugger

Complete troubleshooting guide voor Google Ads conversion tracking problemen. Volg het diagnostisch stappenplan om tracking issues snel te identificeren en op te lossen.

## Diagnostic Decision Tree

```
CONVERSION TRACKING ISSUES - DIAGNOSE
=====================================

START HIER: Wat is het probleem?
│
├── [A] Conversies verschijnen NIET
│   └── Ga naar: SECTION 1 - Missing Conversions
│
├── [B] Te VEEL conversies (duplicates)
│   └── Ga naar: SECTION 2 - Duplicate Conversions
│
├── [C] Aantallen KLOPPEN NIET (GA4 vs Ads)
│   └── Ga naar: SECTION 3 - Discrepancy Analysis
│
├── [D] Enhanced Conversions werkt niet
│   └── Ga naar: SECTION 4 - Enhanced Conversions Debug
│
├── [E] Offline conversions importeren mislukt
│   └── Ga naar: SECTION 5 - Offline Conversion Issues
│
└── [F] Tag/Pixel firing issues
    └── Ga naar: SECTION 6 - Tag Debugging
```

## Section 1: Missing Conversions

### 1.1 Quick Diagnostic Checklist

```
CONVERSIES NIET ZICHTBAAR - CHECKLIST
=====================================

□ STAP 1: Timing Check
├── Conversie latency: 3-24 uur normaal
├── Enhanced Conversions: Tot 48 uur
├── Offline imports: 12-24 uur na upload
└── CHECK: Is het langer dan 24-48 uur geleden?

□ STAP 2: Conversion Action Status
├── Google Ads → Goals → Conversions
├── Status kolom: "Recording" of "No recent conversions"?
├── "Inactive" = Tag niet gevonden
└── "Unverified" = Setup incomplete

□ STAP 3: Tag Presence Check
├── Open website in Chrome Incognito
├── Ga naar conversiepagina (thank you page)
├── Open DevTools (F12) → Network tab
├── Filter op "google" of "gtag"
└── Zoek naar: googleadservices.com/pagead/conversion/

□ STAP 4: Conversion Window
├── Check: conversion_time vs click_time
├── Click-through window: Standaard 30 dagen
├── View-through window: Standaard 1 dag
└── Is conversie buiten window? → Wordt niet geattribueerd
```

### 1.2 Common Causes & Fixes

```
OORZAAK → OPLOSSING MATRIX
==========================

1. TAG NIET OP PAGINA
   Symptoom: Geen requests naar googleadservices
   Fix:
   ├── Verificeer tag in <head> of via GTM
   ├── Check of tag op ALLE bedankpagina's staat
   └── Test in GTM Preview mode

2. VERKEERDE CONVERSION ID/LABEL
   Symptoom: Request zichtbaar maar andere ID
   Fix:
   ├── Vergelijk ID in tag met Google Ads conversie setup
   ├── Format: AW-XXXXXXXXX/YYYYYYYYYYYY
   └── Herinstalleer tag met correcte credentials

3. CONSENT MODE BLOCKING
   Symptoom: Tag aanwezig, maar geen data
   Fix:
   ├── Check consent state: ad_storage, ad_user_data
   ├── Test met cookie banner geaccepteerd
   └── Verify: gtag('consent', 'update', {ad_storage: 'granted'})

4. NO GOOGLE ADS CLICKS (GCLID MISSING)
   Symptoom: Conversies via organic/direct, niet ads
   Fix:
   ├── Check campaign URLs voor gclid parameter
   ├── Auto-tagging enabled? → Google Ads Settings
   └── URL parameters worden niet gestript door redirect?

5. CONVERSION TE OUD (BUITEN WINDOW)
   Symptoom: Clicks >30 dagen geleden
   Fix:
   ├── Verleng conversion window indien sales cycle langer
   └── Max: 90 dagen voor click-through
```

### 1.3 API Diagnostic Queries (GAQL)

```sql
-- Check conversion action status en recente data
SELECT
  conversion_action.name,
  conversion_action.status,
  conversion_action.counting_type,
  conversion_action.category,
  conversion_action.include_in_conversions_metric,
  metrics.conversions,
  metrics.all_conversions
FROM conversion_action
WHERE segments.date DURING LAST_7_DAYS

-- Check campaign conversions vs all_conversions
SELECT
  campaign.name,
  campaign.status,
  metrics.conversions,
  metrics.all_conversions,
  metrics.conversions_value
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date DURING LAST_7_DAYS
ORDER BY metrics.conversions DESC
```

## Section 2: Duplicate Conversions

### 2.1 Duplicate Detection

```
DUPLICATE CONVERSIE DIAGNOSE
============================

SYMPTOMEN:
├── Conversion rate onrealistisch hoog (>20%)
├── Meer conversies dan daadwerkelijke orders
├── Revenue hoger dan backend data
└── Eén user genereert meerdere conversies

OORZAKEN IDENTIFICEREN:

1. DUBBELE TAGS
   Test: Network tab → zoek meerdere calls naar:
   ├── googleadservices.com/pagead/conversion
   ├── gtag('event', 'conversion', ...)
   └── Fix: Verwijder duplicate tags

2. VERKEERDE COUNT SETTING
   Check: Conversion action → Count setting
   ├── "Every conversion" = elke keer tellen
   ├── "One conversion" = één per click
   └── Fix: Leads = One, Purchases = Every

3. GEEN TRANSACTION ID
   Probleem: Zelfde conversie bij page refresh
   Fix: Voeg transaction_id toe:
   gtag('event', 'conversion', {
     'send_to': 'AW-XXX/YYY',
     'transaction_id': 'UNIQUE-ORDER-ID'
   });

4. MEERDERE CONVERSION ACTIONS VOOR ZELFDE ACTIE
   Check: Heb je 2+ conversion actions voor "Purchase"?
   Fix: Consolideer naar één primary conversion
```

### 2.2 Deduplication Fixes

```javascript
// DEDUPLICATIE MET TRANSACTION ID
// Implementeer op thank you page

<script>
  // Haal order ID op uit je platform
  var orderId = '{{ORDER_ID}}';  // Verplicht uniek per order

  // Controleer of al gefired
  if (!sessionStorage.getItem('conversion_' + orderId)) {
    gtag('event', 'conversion', {
      'send_to': 'AW-XXXXXXXXX/YYYYYYYYYYYY',
      'value': {{ORDER_VALUE}},
      'currency': 'EUR',
      'transaction_id': orderId
    });
    sessionStorage.setItem('conversion_' + orderId, 'true');
  }
</script>

// GTM DEDUPLICATIE
// Custom JavaScript Variable: Check if already fired
function() {
  var orderId = {{DLV - Order ID}};
  if (localStorage.getItem('gtm_conv_' + orderId)) {
    return false;  // Block trigger
  }
  localStorage.setItem('gtm_conv_' + orderId, Date.now());
  return true;  // Allow trigger
}
```

## Section 3: GA4 vs Google Ads Discrepancy

### 3.1 Expected Discrepancy Range

```
NORMALE DISCREPANTIE VERWACHTING
================================

GA4 vs Google Ads: 10-30% verschil is NORMAAL

WAAROM VERSCHILLEN?
├── Attribution window verschilt
│   ├── Google Ads: 30d click, 1d view (standaard)
│   └── GA4: 90d cross-channel (standaard)
│
├── Attribution model verschilt
│   ├── Google Ads: Data-driven (ads-focused)
│   └── GA4: Data-driven (cross-channel)
│
├── Deduplicatie verschilt
│   ├── Google Ads: Per click
│   └── GA4: Per user
│
├── Cross-device tracking
│   ├── Google Ads: Via gclid + user matching
│   └── GA4: Via Google Signals + user ID
│
└── Consent impact
    ├── Google Ads: Modelleert denied traffic
    └── GA4: Alleen consented data (standaard)
```

### 3.2 Discrepancy Investigation Steps

```
STAP-VOOR-STAP VERGELIJKING
===========================

STAP 1: Align Time Periods
├── Gebruik exact dezelfde datums
├── Account voor timezones
└── GA4: UTC standaard

STAP 2: Align Attribution Settings
├── GA4: Admin → Attribution Settings
├── Verander naar: Last click, 30 day window
└── Vergelijk opnieuw (wacht 24-48 uur voor recalc)

STAP 3: Compare Apples to Apples
├── Google Ads: Use "All Conversions" kolom
├── GA4: Include all events (not just key events)
└── Check: Is het dezelfde conversion action?

STAP 4: Check Data Quality
├── GA4: Filter internal traffic, bots
├── Google Ads: Check voor duplicate conversions
└── Vergelijk order IDs in backend

STAP 5: Document Baseline
├── Accepteer structurele discrepantie
├── Focus op trend consistency
└── Red flag: Discrepantie >30% of plots verandert
```

### 3.3 Alignment Recommendations

```
DISCREPANTIE REDUCEREN
======================

ACTION 1: Unify Attribution Windows
├── Google Ads: Goals → Settings → Attribution
├── GA4: Admin → Attribution Settings
└── Advies: Beide op 30-day click, data-driven

ACTION 2: Use Same Tracking Source
├── Optie A: Native Google Ads tag voor Ads reporting
├── Optie B: GA4 import voor unified view
└── Niet beide mixen voor zelfde conversie

ACTION 3: Implement Enhanced Conversions
├── Verhoogt match rate met 5-15%
├── Vermindert discrepantie
└── Vooral voor cross-device gaps

ACTION 4: Accept & Document
├── Perfect match is onmogelijk
├── Focus op relative trends
└── Rapporteer uit één bron voor stakeholders
```

## Section 4: Enhanced Conversions Debug

### 4.1 Enhanced Conversions Status Check

```
ENHANCED CONVERSIONS DIAGNOSE
=============================

STAP 1: Check Status in Google Ads
├── Goals → Conversions → [Select Action]
├── Klik "Details"
├── Zoek: "Enhanced conversions"
└── Status: "Recording", "Pending", of "Not set up"

STATUS MEANINGS:
├── "Recording" = Werkt correct
├── "Pending" = Setup gedaan, wacht op data
├── "Not set up" = Niet geconfigureerd
├── "Inactive" = Was actief, nu geen data
└── "Health: Poor" = Data quality issues

STAP 2: Check Tag Implementation
Open DevTools → Network → Filter "conversion"
Zoek in request payload naar:
├── "em" (hashed email)
├── "ph" (hashed phone)
├── "fn" / "ln" (hashed name)
└── Geen user_data = Enhanced Conversions niet actief
```

### 4.2 Common Enhanced Conversions Issues

```
PROBLEEM → OPLOSSING
====================

1. USER_DATA NIET ZICHTBAAR IN TAG
   Check:
   ├── gtag('set', 'user_data', {...}) VOOR conversion event?
   ├── Data correct gevuld? (niet undefined/null)
   └── GTM: User-Provided Data variable configured?

   Fix:
   ├── Vul user data in op moment van beschikbaarheid
   └── Debug: console.log(dataLayer) na form submit

2. HASH FORMAT INCORRECT
   Check:
   ├── Email lowercase + trimmed voor hashing?
   ├── Phone in E.164 format (+31612345678)?
   └── SHA256 output is 64 hex characters?

   Fix:
   function normalizeEmail(email) {
     return email.toLowerCase().trim();
   }

3. CONSENT MODE BLOCKING USER_DATA
   Check:
   ├── ad_user_data consent state
   ├── Moet "granted" zijn voor Enhanced Conversions

   Fix:
   gtag('consent', 'update', {
     'ad_user_data': 'granted'
   });

4. MATCH RATE TE LAAG (<10%)
   Check:
   ├── Alleen email? Voeg phone/name/address toe
   ├── Data kwaliteit: echte emails of fake?
   └── Business type: B2B heeft lagere match rates

   Fix:
   ├── Voeg meer data fields toe
   └── Validate email format client-side
```

### 4.3 Enhanced Conversions Verification Script

```javascript
/**
 * Enhanced Conversions Debug Script
 * Run in browser console op conversion page
 */

(function debugEnhancedConversions() {
  console.log('=== Enhanced Conversions Debug ===');

  // Check dataLayer for user_data
  if (window.dataLayer) {
    var userData = window.dataLayer.filter(function(item) {
      return item[0] === 'set' && item[1] === 'user_data';
    });

    if (userData.length > 0) {
      console.log('✓ user_data found in dataLayer:');
      console.log(userData[0][2]);

      // Validate fields
      var data = userData[0][2];
      if (data.email) console.log('  ✓ Email present');
      if (data.phone_number) console.log('  ✓ Phone present');
      if (data.address) console.log('  ✓ Address present');
      if (data.sha256_email_address) console.log('  ✓ Hashed email present');
    } else {
      console.error('✗ No user_data found - Enhanced Conversions NOT active');
    }
  }

  // Check consent state
  if (window.gtag) {
    console.log('\nChecking consent state...');
    // Note: consent state not directly readable, check Network tab
    console.log('→ Verify in Network tab: look for "gcs=" parameter');
    console.log('→ gcs=G111 = all granted');
    console.log('→ gcs=G100 = analytics only');
  }

  // Check recent conversion calls
  if (window.dataLayer) {
    var conversions = window.dataLayer.filter(function(item) {
      return item[0] === 'event' && item[1] === 'conversion';
    });
    console.log('\n✓ Found', conversions.length, 'conversion event(s)');
  }
})();
```

## Section 5: Offline Conversion Import Issues

### 5.1 Import Failure Diagnostics

```
OFFLINE CONVERSION IMPORT PROBLEMEN
===================================

COMMON ERRORS:

1. "GCLID NOT FOUND"
   Oorzaak:
   ├── GCLID verlopen (>90 dagen)
   ├── GCLID incorrect gekopieerd (whitespace, truncated)
   ├── Click kwam niet van Google Ads

   Fix:
   ├── Verify GCLID format: ~100 characters, starts with specific pattern
   ├── Check capture timestamp vs upload
   └── Ensure auto-tagging enabled

2. "CONVERSION ACTION NOT FOUND"
   Oorzaak:
   ├── Verkeerde conversion_action naam/ID
   ├── Conversion action deleted/renamed

   Fix:
   ├── Use exact name as shown in Google Ads
   └── Or use resource_name: customers/{id}/conversionActions/{id}

3. "INVALID TIMESTAMP FORMAT"
   Required format: YYYY-MM-DD HH:MM:SS+TZ
   Examples:
   ├── 2025-01-28 14:30:00+01:00 (Amsterdam)
   ├── 2025-01-28 13:30:00+00:00 (UTC)

   Fix:
   ├── Consistent timezone in all uploads
   └── Validate with regex before upload

4. "PARTIAL FAILURE"
   Oorzaak: Sommige rows valid, andere niet
   Fix:
   ├── Check API response voor failed_conversions details
   ├── Log individuele errors
   └── Retry failed rows na fixing

5. "DUPLICATE CONVERSION"
   Oorzaak: Zelfde GCLID + conversion_action + timestamp
   Fix:
   ├── Add unique identifier (order_id) to prevent
   └── Or skip already-imported conversions
```

### 5.2 GCLID Capture Best Practices

```javascript
// GCLID CAPTURE SCRIPT
// Plaats op alle landing pages

<script>
  (function captureGCLID() {
    // Get GCLID from URL
    var urlParams = new URLSearchParams(window.location.search);
    var gclid = urlParams.get('gclid');

    if (gclid) {
      // Store in cookie (90 day expiry = max attribution window)
      var expires = new Date();
      expires.setDate(expires.getDate() + 90);
      document.cookie = 'gclid=' + gclid +
                        '; expires=' + expires.toUTCString() +
                        '; path=/; SameSite=Lax';

      // Also store in localStorage as backup
      localStorage.setItem('gclid', gclid);
      localStorage.setItem('gclid_timestamp', Date.now());

      console.log('GCLID captured:', gclid);
    }
  })();

  // RETRIEVE GCLID ON FORM SUBMIT
  function getStoredGCLID() {
    // Try cookie first
    var match = document.cookie.match(/gclid=([^;]+)/);
    if (match) return match[1];

    // Fallback to localStorage
    return localStorage.getItem('gclid');
  }
</script>

// HIDDEN FIELD IN FORM
<input type="hidden" name="gclid" id="gclid-field">
<script>
  document.getElementById('gclid-field').value = getStoredGCLID() || '';
</script>
```

### 5.3 Upload Validation Checklist

```
VOOR UPLOAD VALIDEREN
=====================

□ GCLID Validation
├── Length: 90-120 characters typical
├── No whitespace/newlines
├── Age: <90 days from click

□ Timestamp Validation
├── Format: YYYY-MM-DD HH:MM:SS+TZ
├── Timezone consistent
├── After click time, before upload time

□ Value Validation
├── Positive number
├── Correct currency code (EUR, USD)
├── No currency symbols in value

□ Conversion Action
├── Name matches exactly (case-sensitive)
├── Action exists and is "recording"
├── Include_in_conversions setting correct

□ Required Fields Present
├── gclid (of email voor Enhanced)
├── conversion_action
├── conversion_time
├── Optional: value, currency
```

## Section 6: Tag Debugging

### 6.1 Tag Verification Tools

```
TAG DEBUG TOOLS
===============

1. CHROME TAG ASSISTANT (Extension)
   ├── Install: Chrome Web Store → Tag Assistant Legacy
   ├── Navigate to conversion page
   ├── Click extension → Enable → Refresh
   └── Check for green/yellow/red indicators

2. GOOGLE ADS TAG DIAGNOSTICS
   ├── Google Ads → Tools → Google Tag
   ├── "Diagnose issues" feature
   └── Shows firing status per page

3. GOOGLE TAG MANAGER PREVIEW
   ├── GTM → Preview → Enter URL
   ├── Navigate through conversion flow
   ├── Check "Tags Fired" panel
   └── Verify trigger conditions

4. NETWORK TAB INSPECTION
   ├── DevTools (F12) → Network → Filter
   ├── Search: "googleads", "conversion", "gtag"
   ├── Verify request fires on conversion
   └── Check response: 200 OK?

5. REAL-TIME REPORTS
   ├── GA4 → Reports → Realtime
   ├── Trigger test conversion
   ├── Verify event appears (if GA4 linked)
   └── For Google Ads: Wait 3-6 hours
```

### 6.2 Tag Firing Issues

```
TAG FIRING PROBLEMEN
====================

1. TAG FIRES TE VROEG (voor conversie)
   Symptoom: Alle pageviews worden conversies
   Fix:
   ├── Trigger alleen op thank you page URL
   ├── Of: Trigger op form submission event
   └── GTM: Add trigger condition

2. TAG FIRES NIET
   Symptomen: Geen network requests
   Causes:
   ├── JavaScript error blokkeert
   ├── Consent blocking
   ├── Tag not published (GTM)
   ├── Wrong trigger condition

   Fix:
   ├── Check Console voor JS errors
   ├── Test met consent granted
   ├── GTM: Publish container
   └── Verify trigger matches page/event

3. TAG FIRES MEERDERE KEREN
   Symptoom: Multiple requests per pageview
   Causes:
   ├── SPA: Tag fires on every route change
   ├── Duplicate tags (GTM + hardcoded)
   ├── Multiple trigger conditions matching

   Fix:
   ├── SPA: Use history change trigger properly
   ├── Remove duplicate implementations
   └── Consolidate triggers

4. WRONG DATA IN TAG
   Symptoom: Values incorrect (0, undefined)
   Fix:
   ├── Debug variables in GTM preview
   ├── Verify data layer timing
   └── Add fallback values
```

### 6.3 Complete Debug Workflow

```
SYSTEMATISCHE DEBUG WORKFLOW
============================

FASE 1: VERIFICATION (5 min)
├── Open conversion page in Incognito
├── Open DevTools Network tab
├── Complete conversion action
├── Screenshot all google* requests
└── Note: Firing? Correct data?

FASE 2: TAG INSPECTION (5 min)
├── View page source (Ctrl+U)
├── Search for "gtag" of "googletagmanager"
├── Verify tag ID matches Google Ads
└── Check placement (<head> preferred)

FASE 3: GTM VALIDATION (5 min)
├── GTM Preview mode
├── Walk through conversion flow
├── Verify:
│   ├── Container loads
│   ├── Triggers fire correctly
│   ├── Variables populated
│   └── Tags execute
└── Check for blocking triggers

FASE 4: CONSENT CHECK (3 min)
├── Accept all cookies
├── Verify consent state updates
├── Test: Does tag fire after consent?
└── Check gcs parameter in requests

FASE 5: GOOGLE ADS VERIFICATION (2 min)
├── Goals → Conversions → [Action]
├── Check "Recording" status
├── Verify settings match implementation
└── Test conversion (may take hours to show)
```

## Quick Reference Card

```
CONVERSION TRACKING DEBUG CHEAT SHEET
=====================================

NOT SHOWING?
→ Check tag presence (Network tab)
→ Verify conversion ID/label
→ Test consent state
→ Wait 24-48 hours

DUPLICATES?
→ Add transaction_id
→ Set Count: "One" for leads
→ Check for duplicate tags
→ Implement sessionStorage check

GA4 DISCREPANCY?
→ 10-30% difference = normal
→ Align attribution windows
→ Compare All Conversions column
→ Accept baseline, track trends

ENHANCED NOT WORKING?
→ Check user_data in dataLayer
→ Verify consent: ad_user_data
→ Validate hash format
→ Wait 48 hours for status

OFFLINE IMPORT FAILING?
→ Validate GCLID format/age
→ Check timestamp timezone
→ Verify conversion action name
→ Handle partial failures

TAG NOT FIRING?
→ Check JS console for errors
→ Verify GTM published
→ Test trigger conditions
→ Remove duplicate implementations
```

## Voorbeeld Interactie

**Gebruiker**: "Mijn conversies verschijnen niet in Google Ads. De tag staat er wel op."

**Claude response**:

"Laat me je door een gestructureerde diagnose leiden:

**STAP 1: Timing Check**
- Wanneer was de laatste conversie? Standaard latency is 3-24 uur, tot 48 uur voor Enhanced Conversions.

**STAP 2: Verifieer Tag Firing**
1. Open je thank you page in Chrome Incognito
2. Open DevTools (F12) → Network tab
3. Filter op `googleadservices` of `conversion`
4. Completeer een test-conversie
5. Zie je een request verschijnen?

**STAP 3: Check Conversion Action Status**
Ga naar Google Ads → Goals → Conversions:
- Staat er "Recording" of "No recent conversions"?
- "Unverified" = setup nog niet compleet

**STAP 4: Consent Mode**
Is Consent Mode actief? Test:
- Accepteer alle cookies
- Completeer conversie
- Check of request nu wel verschijnt

**Meest voorkomende oorzaken:**
1. **Consent blocking** (ad_storage denied) - 40% van gevallen
2. **Verkeerde page** (tag niet op bedankpagina) - 25%
3. **GCLID missing** (auto-tagging uit) - 20%
4. **Timing** (gewoon wachten) - 15%

Wat zie je als je deze stappen doorloopt?"

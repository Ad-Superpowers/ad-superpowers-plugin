## Diagnostic Decision Tree

```
CONVERSION TRACKING ISSUES - DIAGNOSE
=====================================

START HERE: What is the problem?
|
+-- [A] Conversions NOT appearing
|   +-- Go to: SECTION 1 - Missing Conversions
|
+-- [B] Too MANY conversions (duplicates)
|   +-- Go to: SECTION 2 - Duplicate Conversions
|
+-- [C] Numbers DON'T MATCH (GA4 vs Ads)
|   +-- Go to: SECTION 3 - Discrepancy Analysis
|
+-- [D] Enhanced Conversions not working
|   +-- Go to: SECTION 4 - Enhanced Conversions Debug
|
+-- [E] Offline conversion import failing
|   +-- Go to: SECTION 5 - Offline Conversion Issues
|
+-- [F] Tag/Pixel firing issues
    +-- Go to: SECTION 6 - Tag Debugging
```

## Section 1: Missing Conversions

### 1.1 Quick Diagnostic Checklist

```
CONVERSIONS NOT VISIBLE - CHECKLIST
====================================

[ ] STEP 1: Timing Check
+-- Conversion latency: 3-24 hours is normal
+-- Enhanced Conversions: Up to 48 hours
+-- Offline imports: 12-24 hours after upload
+-- CHECK: Has it been more than 24-48 hours?

[ ] STEP 2: Conversion Action Status
+-- Google Ads -> Goals -> Conversions
+-- Status column: "Recording" or "No recent conversions"?
+-- "Inactive" = Tag not found
+-- "Unverified" = Setup incomplete

[ ] STEP 3: Tag Presence Check
+-- Open website in Chrome Incognito
+-- Navigate to conversion page (thank you page)
+-- Open DevTools (F12) -> Network tab
+-- Filter on "google" or "gtag"
+-- Look for: googleadservices.com/pagead/conversion/

[ ] STEP 4: Conversion Window
+-- Check: conversion_time vs click_time
+-- Click-through window: Default 30 days
+-- View-through window: Default 1 day
+-- Is conversion outside window? -> Will not be attributed
```

### 1.2 Common Causes & Fixes

```
CAUSE -> SOLUTION MATRIX
=========================

1. TAG NOT ON PAGE
   Symptom: No requests to googleadservices
   Fix:
   +-- Verify tag in <head> or via GTM
   +-- Check if tag is on ALL thank-you pages
   +-- Test in GTM Preview mode

2. WRONG CONVERSION ID/LABEL
   Symptom: Request visible but different ID
   Fix:
   +-- Compare ID in tag with Google Ads conversion setup
   +-- Format: AW-XXXXXXXXX/YYYYYYYYYYYY
   +-- Reinstall tag with correct credentials

3. CONSENT MODE BLOCKING
   Symptom: Tag present, but no data
   Fix:
   +-- Check consent state: ad_storage, ad_user_data
   +-- Test with cookie banner accepted
   +-- Verify: gtag('consent', 'update', {ad_storage: 'granted'})

4. NO GOOGLE ADS CLICKS (GCLID MISSING)
   Symptom: Conversions via organic/direct, not ads
   Fix:
   +-- Check campaign URLs for gclid parameter
   +-- Auto-tagging enabled? -> Google Ads Settings
   +-- URL parameters not being stripped by redirect?

5. CONVERSION TOO OLD (OUTSIDE WINDOW)
   Symptom: Clicks >30 days ago
   Fix:
   +-- Extend conversion window if sales cycle is longer
   +-- Max: 90 days for click-through
```

### 1.3 API Diagnostic Queries (GAQL)

```sql
-- Check conversion action status and recent data
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

### 1.1 Quick Diagnostic Checklist

```
CONVERSIONS NOT VISIBLE - CHECKLIST
====================================

[ ] STEP 1: Timing Check
+-- Conversion latency: 3-24 hours is normal
+-- Enhanced Conversions: Up to 48 hours
+-- Offline imports: 12-24 hours after upload
+-- CHECK: Has it been more than 24-48 hours?

[ ] STEP 2: Conversion Action Status
+-- Google Ads -> Goals -> Conversions
+-- Status column: "Recording" or "No recent conversions"?
+-- "Inactive" = Tag not found
+-- "Unverified" = Setup incomplete

[ ] STEP 3: Tag Presence Check
+-- Open website in Chrome Incognito
+-- Navigate to conversion page (thank you page)
+-- Open DevTools (F12) -> Network tab
+-- Filter on "google" or "gtag"
+-- Look for: googleadservices.com/pagead/conversion/

[ ] STEP 4: Conversion Window
+-- Check: conversion_time vs click_time
+-- Click-through window: Default 30 days
+-- View-through window: Default 1 day
+-- Is conversion outside window? -> Will not be attributed
```

### 1.3 API Diagnostic Queries (GAQL)

```sql
-- Check conversion action status and recent data
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
DUPLICATE CONVERSION DIAGNOSIS
==============================

SYMPTOMS:
+-- Conversion rate unrealistically high (>20%)
+-- More conversions than actual orders
+-- Revenue higher than backend data
+-- One user generates multiple conversions

IDENTIFYING CAUSES:

1. DUPLICATE TAGS
   Test: Network tab -> look for multiple calls to:
   +-- googleadservices.com/pagead/conversion
   +-- gtag('event', 'conversion', ...)
   +-- Fix: Remove duplicate tags

2. WRONG COUNT SETTING
   Check: Conversion action -> Count setting
   +-- "Every conversion" = count each time
   +-- "One conversion" = one per click
   +-- Fix: Leads = One, Purchases = Every

3. NO TRANSACTION ID
   Problem: Same conversion on page refresh
   Fix: Add transaction_id:
   gtag('event', 'conversion', {
     'send_to': 'AW-XXX/YYY',
     'transaction_id': 'UNIQUE-ORDER-ID'
   });

4. MULTIPLE CONVERSION ACTIONS FOR SAME ACTION
   Check: Do you have 2+ conversion actions for "Purchase"?
   Fix: Consolidate to one primary conversion
```

### 2.2 Deduplication Fixes

```javascript
// DEDUPLICATION WITH TRANSACTION ID
// Implement on thank you page

<script>
  // Get order ID from your platform
  var orderId = '{{ORDER_ID}}';  // Must be unique per order

  // Check if already fired
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

// GTM DEDUPLICATION
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

### 2.1 Duplicate Detection

```
DUPLICATE CONVERSION DIAGNOSIS
==============================

SYMPTOMS:
+-- Conversion rate unrealistically high (>20%)
+-- More conversions than actual orders
+-- Revenue higher than backend data
+-- One user generates multiple conversions

IDENTIFYING CAUSES:

1. DUPLICATE TAGS
   Test: Network tab -> look for multiple calls to:
   +-- googleadservices.com/pagead/conversion
   +-- gtag('event', 'conversion', ...)
   +-- Fix: Remove duplicate tags

2. WRONG COUNT SETTING
   Check: Conversion action -> Count setting
   +-- "Every conversion" = count each time
   +-- "One conversion" = one per click
   +-- Fix: Leads = One, Purchases = Every

3. NO TRANSACTION ID
   Problem: Same conversion on page refresh
   Fix: Add transaction_id:
   gtag('event', 'conversion', {
     'send_to': 'AW-XXX/YYY',
     'transaction_id': 'UNIQUE-ORDER-ID'
   });

4. MULTIPLE CONVERSION ACTIONS FOR SAME ACTION
   Check: Do you have 2+ conversion actions for "Purchase"?
   Fix: Consolidate to one primary conversion
```

## Section 4: Enhanced Conversions Debug

### 4.1 Enhanced Conversions Status Check

```
ENHANCED CONVERSIONS DIAGNOSIS
===============================

STEP 1: Check Status in Google Ads
+-- Goals -> Conversions -> [Select Action]
+-- Click "Details"
+-- Look for: "Enhanced conversions"
+-- Status: "Recording", "Pending", or "Not set up"

STATUS MEANINGS:
+-- "Recording" = Working correctly
+-- "Pending" = Setup done, waiting for data
+-- "Not set up" = Not configured
+-- "Inactive" = Was active, now no data
+-- "Health: Poor" = Data quality issues

STEP 2: Check Tag Implementation
Open DevTools -> Network -> Filter "conversion"
Look in request payload for:
+-- "em" (hashed email)
+-- "ph" (hashed phone)
+-- "fn" / "ln" (hashed name)
+-- No user_data = Enhanced Conversions not active
```

### 4.2 Common Enhanced Conversions Issues

```
PROBLEM -> SOLUTION
====================

1. USER_DATA NOT VISIBLE IN TAG
   Check:
   +-- gtag('set', 'user_data', {...}) BEFORE conversion event?
   +-- Data properly populated? (not undefined/null)
   +-- GTM: User-Provided Data variable configured?

   Fix:
   +-- Populate user data at moment of availability
   +-- Debug: console.log(dataLayer) after form submit

2. HASH FORMAT INCORRECT
   Check:
   +-- Email lowercase + trimmed before hashing?
   +-- Phone in E.164 format (+31612345678)?
   +-- SHA256 output is 64 hex characters?

   Fix:
   function normalizeEmail(email) {
     return email.toLowerCase().trim();
   }

3. CONSENT MODE BLOCKING USER_DATA
   Check:
   +-- ad_user_data consent state
   +-- Must be "granted" for Enhanced Conversions

   Fix:
   gtag('consent', 'update', {
     'ad_user_data': 'granted'
   });

4. MATCH RATE TOO LOW (<10%)
   Check:
   +-- Only email? Add phone/name/address
   +-- Data quality: real emails or fake?
   +-- Business type: B2B has lower match rates

   Fix:
   +-- Add more data fields
   +-- Validate email format client-side
```

### 4.3 Enhanced Conversions Verification Script

```javascript
/**
 * Enhanced Conversions Debug Script
 * Run in browser console on conversion page
 */

(function debugEnhancedConversions() {
  console.log('=== Enhanced Conversions Debug ===');

  // Check dataLayer for user_data
  if (window.dataLayer) {
    var userData = window.dataLayer.filter(function(item) {
      return item[0] === 'set' && item[1] === 'user_data';
    });

    if (userData.length > 0) {
      console.log('user_data found in dataLayer:');
      console.log(userData[0][2]);

      // Validate fields
      var data = userData[0][2];
      if (data.email) console.log('  Email present');
      if (data.phone_number) console.log('  Phone present');
      if (data.address) console.log('  Address present');
      if (data.sha256_email_address) console.log('  Hashed email present');
    } else {
      console.error('No user_data found - Enhanced Conversions NOT active');
    }
  }

  // Check consent state
  if (window.gtag) {
    console.log('\nChecking consent state...');
    // Note: consent state not directly readable, check Network tab
    console.log('-> Verify in Network tab: look for "gcs=" parameter');
    console.log('-> gcs=G111 = all granted');
    console.log('-> gcs=G100 = analytics only');
  }

  // Check recent conversion calls
  if (window.dataLayer) {
    var conversions = window.dataLayer.filter(function(item) {
      return item[0] === 'event' && item[1] === 'conversion';
    });
    console.log('\nFound', conversions.length, 'conversion event(s)');
  }
})();
```

### 4.1 Enhanced Conversions Status Check

```
ENHANCED CONVERSIONS DIAGNOSIS
===============================

STEP 1: Check Status in Google Ads
+-- Goals -> Conversions -> [Select Action]
+-- Click "Details"
+-- Look for: "Enhanced conversions"
+-- Status: "Recording", "Pending", or "Not set up"

STATUS MEANINGS:
+-- "Recording" = Working correctly
+-- "Pending" = Setup done, waiting for data
+-- "Not set up" = Not configured
+-- "Inactive" = Was active, now no data
+-- "Health: Poor" = Data quality issues

STEP 2: Check Tag Implementation
Open DevTools -> Network -> Filter "conversion"
Look in request payload for:
+-- "em" (hashed email)
+-- "ph" (hashed phone)
+-- "fn" / "ln" (hashed name)
+-- No user_data = Enhanced Conversions not active
```

## Section 5: Offline Conversion Import Issues

### 5.1 Import Failure Diagnostics

```
OFFLINE CONVERSION IMPORT PROBLEMS
====================================

COMMON ERRORS:

1. "GCLID NOT FOUND"
   Cause:
   +-- GCLID expired (>90 days)
   +-- GCLID incorrectly copied (whitespace, truncated)
   +-- Click did not come from Google Ads

   Fix:
   +-- Verify GCLID format: ~100 characters, starts with specific pattern
   +-- Check capture timestamp vs upload
   +-- Ensure auto-tagging enabled

2. "CONVERSION ACTION NOT FOUND"
   Cause:
   +-- Wrong conversion_action name/ID
   +-- Conversion action deleted/renamed

   Fix:
   +-- Use exact name as shown in Google Ads
   +-- Or use resource_name: customers/{id}/conversionActions/{id}

3. "INVALID TIMESTAMP FORMAT"
   Required format: YYYY-MM-DD HH:MM:SS+TZ
   Examples:
   +-- 2025-01-28 14:30:00+01:00 (Amsterdam)
   +-- 2025-01-28 13:30:00+00:00 (UTC)

   Fix:
   +-- Consistent timezone in all uploads
   +-- Validate with regex before upload

4. "PARTIAL FAILURE"
   Cause: Some rows valid, others not
   Fix:
   +-- Check API response for failed_conversions details
   +-- Log individual errors
   +-- Retry failed rows after fixing

5. "DUPLICATE CONVERSION"
   Cause: Same GCLID + conversion_action + timestamp
   Fix:
   +-- Add unique identifier (order_id) to prevent
   +-- Or skip already-imported conversions
```

### 5.2 GCLID Capture Best Practices

```javascript
// GCLID CAPTURE SCRIPT
// Place on all landing pages

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
VALIDATE BEFORE UPLOAD
=======================

[ ] GCLID Validation
+-- Length: 90-120 characters typical
+-- No whitespace/newlines
+-- Age: <90 days from click

[ ] Timestamp Validation
+-- Format: YYYY-MM-DD HH:MM:SS+TZ
+-- Timezone consistent
+-- After click time, before upload time

[ ] Value Validation
+-- Positive number
+-- Correct currency code (EUR, USD)
+-- No currency symbols in value

[ ] Conversion Action
+-- Name matches exactly (case-sensitive)
+-- Action exists and is "recording"
+-- Include_in_conversions setting correct

[ ] Required Fields Present
+-- gclid (or email for Enhanced)
+-- conversion_action
+-- conversion_time
+-- Optional: value, currency
```

### 5.1 Import Failure Diagnostics

```
OFFLINE CONVERSION IMPORT PROBLEMS
====================================

COMMON ERRORS:

1. "GCLID NOT FOUND"
   Cause:
   +-- GCLID expired (>90 days)
   +-- GCLID incorrectly copied (whitespace, truncated)
   +-- Click did not come from Google Ads

   Fix:
   +-- Verify GCLID format: ~100 characters, starts with specific pattern
   +-- Check capture timestamp vs upload
   +-- Ensure auto-tagging enabled

2. "CONVERSION ACTION NOT FOUND"
   Cause:
   +-- Wrong conversion_action name/ID
   +-- Conversion action deleted/renamed

   Fix:
   +-- Use exact name as shown in Google Ads
   +-- Or use resource_name: customers/{id}/conversionActions/{id}

3. "INVALID TIMESTAMP FORMAT"
   Required format: YYYY-MM-DD HH:MM:SS+TZ
   Examples:
   +-- 2025-01-28 14:30:00+01:00 (Amsterdam)
   +-- 2025-01-28 13:30:00+00:00 (UTC)

   Fix:
   +-- Consistent timezone in all uploads
   +-- Validate with regex before upload

4. "PARTIAL FAILURE"
   Cause: Some rows valid, others not
   Fix:
   +-- Check API response for failed_conversions details
   +-- Log individual errors
   +-- Retry failed rows after fixing

5. "DUPLICATE CONVERSION"
   Cause: Same GCLID + conversion_action + timestamp
   Fix:
   +-- Add unique identifier (order_id) to prevent
   +-- Or skip already-imported conversions
```

## Example Interaction

**User**: "My conversions are not showing in Google Ads. The tag is installed."

**Claude response**:

"Let me walk you through a structured diagnosis:

**STEP 1: Timing Check**
- When was the last conversion? Standard latency is 3-24 hours, up to 48 hours for Enhanced Conversions.

**STEP 2: Verify Tag Firing**
1. Open your thank you page in Chrome Incognito
2. Open DevTools (F12) -> Network tab
3. Filter on `googleadservices` or `conversion`
4. Complete a test conversion
5. Do you see a request appearing?

**STEP 3: Check Conversion Action Status**
Go to Google Ads -> Goals -> Conversions:
- Does it say "Recording" or "No recent conversions"?
- "Unverified" = setup not yet complete

**STEP 4: Consent Mode**
Is Consent Mode active? Test:
- Accept all cookies
- Complete conversion
- Check if request now appears

**Most common causes:**
1. **Consent blocking** (ad_storage denied) - 40% of cases
2. **Wrong page** (tag not on thank-you page) - 25%
3. **GCLID missing** (auto-tagging off) - 20%
4. **Timing** (just wait) - 15%

What do you see when you go through these steps?"
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
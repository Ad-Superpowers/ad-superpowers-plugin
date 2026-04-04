## Section 3: GA4 vs Google Ads Discrepancy

### 3.1 Expected Discrepancy Range

```
NORMAL DISCREPANCY EXPECTATION
===============================

GA4 vs Google Ads: 10-30% difference is NORMAL

WHY DIFFERENCES?
+-- Attribution window differs
|   +-- Google Ads: 30d click, 1d view (default)
|   +-- GA4: 90d cross-channel (default)
|
+-- Attribution model differs
|   +-- Google Ads: Data-driven (ads-focused)
|   +-- GA4: Data-driven (cross-channel)
|
+-- Deduplication differs
|   +-- Google Ads: Per click
|   +-- GA4: Per user
|
+-- Cross-device tracking
|   +-- Google Ads: Via gclid + user matching
|   +-- GA4: Via Google Signals + user ID
|
+-- Consent impact
    +-- Google Ads: Models denied traffic
    +-- GA4: Only consented data (default)
```

### 3.2 Discrepancy Investigation Steps

```
STEP-BY-STEP COMPARISON
========================

STEP 1: Align Time Periods
+-- Use exactly the same dates
+-- Account for timezones
+-- GA4: UTC by default

STEP 2: Align Attribution Settings
+-- GA4: Admin -> Attribution Settings
+-- Change to: Last click, 30 day window
+-- Compare again (wait 24-48 hours for recalculation)

STEP 3: Compare Apples to Apples
+-- Google Ads: Use "All Conversions" column
+-- GA4: Include all events (not just key events)
+-- Check: Is it the same conversion action?

STEP 4: Check Data Quality
+-- GA4: Filter internal traffic, bots
+-- Google Ads: Check for duplicate conversions
+-- Compare order IDs in backend

STEP 5: Document Baseline
+-- Accept structural discrepancy
+-- Focus on trend consistency
+-- Red flag: Discrepancy >30% or suddenly changes
```

### 3.3 Alignment Recommendations

```
REDUCING DISCREPANCY
=====================

ACTION 1: Unify Attribution Windows
+-- Google Ads: Goals -> Settings -> Attribution
+-- GA4: Admin -> Attribution Settings
+-- Recommendation: Both on 30-day click, data-driven

ACTION 2: Use Same Tracking Source
+-- Option A: Native Google Ads tag for Ads reporting
+-- Option B: GA4 import for unified view
+-- Do not mix both for the same conversion

ACTION 3: Implement Enhanced Conversions
+-- Increases match rate by 5-15%
+-- Reduces discrepancy
+-- Especially for cross-device gaps

ACTION 4: Accept & Document
+-- Perfect match is impossible
+-- Focus on relative trends
+-- Report from one source for stakeholders
```

## Section 6: Tag Debugging

### 6.1 Tag Verification Tools

```
TAG DEBUG TOOLS
===============

1. CHROME TAG ASSISTANT (Extension)
   +-- Install: Chrome Web Store -> Tag Assistant Legacy
   +-- Navigate to conversion page
   +-- Click extension -> Enable -> Refresh
   +-- Check for green/yellow/red indicators

2. GOOGLE ADS TAG DIAGNOSTICS
   +-- Google Ads -> Tools -> Google Tag
   +-- "Diagnose issues" feature
   +-- Shows firing status per page

3. GOOGLE TAG MANAGER PREVIEW
   +-- GTM -> Preview -> Enter URL
   +-- Navigate through conversion flow
   +-- Check "Tags Fired" panel
   +-- Verify trigger conditions

4. NETWORK TAB INSPECTION
   +-- DevTools (F12) -> Network -> Filter
   +-- Search: "googleads", "conversion", "gtag"
   +-- Verify request fires on conversion
   +-- Check response: 200 OK?

5. REAL-TIME REPORTS
   +-- GA4 -> Reports -> Realtime
   +-- Trigger test conversion
   +-- Verify event appears (if GA4 linked)
   +-- For Google Ads: Wait 3-6 hours
```

### 6.2 Tag Firing Issues

```
TAG FIRING PROBLEMS
====================

1. TAG FIRES TOO EARLY (before conversion)
   Symptom: All pageviews become conversions
   Fix:
   +-- Trigger only on thank you page URL
   +-- Or: Trigger on form submission event
   +-- GTM: Add trigger condition

2. TAG NOT FIRING
   Symptoms: No network requests
   Causes:
   +-- JavaScript error blocking
   +-- Consent blocking
   +-- Tag not published (GTM)
   +-- Wrong trigger condition

   Fix:
   +-- Check Console for JS errors
   +-- Test with consent granted
   +-- GTM: Publish container
   +-- Verify trigger matches page/event

3. TAG FIRES MULTIPLE TIMES
   Symptom: Multiple requests per pageview
   Causes:
   +-- SPA: Tag fires on every route change
   +-- Duplicate tags (GTM + hardcoded)
   +-- Multiple trigger conditions matching

   Fix:
   +-- SPA: Use history change trigger properly
   +-- Remove duplicate implementations
   +-- Consolidate triggers

4. WRONG DATA IN TAG
   Symptom: Values incorrect (0, undefined)
   Fix:
   +-- Debug variables in GTM preview
   +-- Verify data layer timing
   +-- Add fallback values
```

### 6.3 Complete Debug Workflow

```
SYSTEMATIC DEBUG WORKFLOW
==========================

PHASE 1: VERIFICATION (5 min)
+-- Open conversion page in Incognito
+-- Open DevTools Network tab
+-- Complete conversion action
+-- Screenshot all google* requests
+-- Note: Firing? Correct data?

PHASE 2: TAG INSPECTION (5 min)
+-- View page source (Ctrl+U)
+-- Search for "gtag" or "googletagmanager"
+-- Verify tag ID matches Google Ads
+-- Check placement (<head> preferred)

PHASE 3: GTM VALIDATION (5 min)
+-- GTM Preview mode
+-- Walk through conversion flow
+-- Verify:
|   +-- Container loads
|   +-- Triggers fire correctly
|   +-- Variables populated
|   +-- Tags execute
+-- Check for blocking triggers

PHASE 4: CONSENT CHECK (3 min)
+-- Accept all cookies
+-- Verify consent state updates
+-- Test: Does tag fire after consent?
+-- Check gcs parameter in requests

PHASE 5: GOOGLE ADS VERIFICATION (2 min)
+-- Goals -> Conversions -> [Action]
+-- Check "Recording" status
+-- Verify settings match implementation
+-- Test conversion (may take hours to show)
```

### 6.3 Complete Debug Workflow

```
SYSTEMATIC DEBUG WORKFLOW
==========================

PHASE 1: VERIFICATION (5 min)
+-- Open conversion page in Incognito
+-- Open DevTools Network tab
+-- Complete conversion action
+-- Screenshot all google* requests
+-- Note: Firing? Correct data?

PHASE 2: TAG INSPECTION (5 min)
+-- View page source (Ctrl+U)
+-- Search for "gtag" or "googletagmanager"
+-- Verify tag ID matches Google Ads
+-- Check placement (<head> preferred)

PHASE 3: GTM VALIDATION (5 min)
+-- GTM Preview mode
+-- Walk through conversion flow
+-- Verify:
|   +-- Container loads
|   +-- Triggers fire correctly
|   +-- Variables populated
|   +-- Tags execute
+-- Check for blocking triggers

PHASE 4: CONSENT CHECK (3 min)
+-- Accept all cookies
+-- Verify consent state updates
+-- Test: Does tag fire after consent?
+-- Check gcs parameter in requests

PHASE 5: GOOGLE ADS VERIFICATION (2 min)
+-- Goals -> Conversions -> [Action]
+-- Check "Recording" status
+-- Verify settings match implementation
+-- Test conversion (may take hours to show)
```
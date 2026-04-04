---
name: google-ads-conversion-tracking-debugger
description: |
  Diagnoses and fixes Google Ads conversion tracking issues including missing conversions,
  duplicate counting, GA4 vs Google Ads discrepancies, Enhanced Conversions failures,
  offline conversion import errors, and tag firing problems.
  Use when: conversions not showing, tracking broken, duplicate conversions, conversion
  count mismatch between GA4 and Google Ads, Enhanced Conversions not working, GCLID
  issues, offline conversion import failing, consent mode impact on tracking.
  Do NOT use for: initial conversion tracking setup (use google-ads-conversion-tracking-setup),
  Enhanced Conversions setup (use google-ads-enhanced-conversions-setup),
  Meta pixel issues (use meta-capi-implementation-guide).
metadata:
  author: "AdSuperpowers"
  version: "2.0.0"
  platform: "google_ads"
  phase: "fase-2-measurement"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---

# Conversion Tracking Debugger

Systematic troubleshooting guide for Google Ads conversion tracking issues. Follow the diagnostic trees to identify root causes and apply fixes.

## Master Diagnostic Tree

```
CONVERSION TRACKING ISSUE
│
├─► CONVERSIONS NOT SHOWING (0 conversions)
│   │
│   ├── Tag not firing?
│   │   ├── Check: Browser DevTools → Network tab → filter "googleads" or "conversion"
│   │   ├── Check: GTM Preview mode → is the tag firing?
│   │   ├── Fix: Verify trigger conditions match actual page behavior
│   │   └── Fix: Ensure GTM container is published (not just previewed)
│   │
│   ├── Tag firing but no conversion recorded?
│   │   ├── Check: Conversion ID and Label match Google Ads settings
│   │   ├── Check: Conversion action status in Google Ads → Tools → Conversions
│   │   ├── Fix: "No recent conversions" status = tag mismatch or consent blocking
│   │   └── Fix: Wait 24-48 hours — Google Ads has reporting lag
│   │
│   ├── Consent blocking?
│   │   ├── Check: Consent Mode v2 → is ad_storage = "denied"?
│   │   ├── Check: Consent banner implementation → does it fire consent_update?
│   │   ├── Impact: Strict consent (EU) can reduce tracked conversions 30-60%
│   │   └── Fix: Implement Consent Mode modeling (Google models ~70% recovery)
│   │
│   └── Attribution window mismatch?
│       ├── Check: Click-through window (default 30 days) vs actual conversion lag
│       ├── Check: View-through window (default 1 day for Display/Video)
│       └── Fix: Align windows with actual customer journey length
│
├─► DUPLICATE CONVERSIONS (too many)
│   │
│   ├── Same conversion counted multiple times per user?
│   │   ├── Check: Count setting → "One" for leads, "Every" for purchases
│   │   ├── Check: Is the tag firing on confirmation page AND thank-you page?
│   │   ├── Fix: Set Count = "One" for lead/signup actions
│   │   └── Fix: Add transaction_id / order_id for deduplication
│   │
│   ├── Duplicate tags in GTM?
│   │   ├── Check: `gtm_audit` for duplicate conversion tags
│   │   ├── Check: Both global site tag AND GTM tag firing?
│   │   └── Fix: Remove one implementation — use GTM only
│   │
│   └── GA4 imported conversion + direct tag = double counting?
│       ├── Check: Google Ads Conversions → are there both "Website" and "GA4" sources?
│       ├── Fix: Use ONE source — either GA4 import OR direct Google Ads tag
│       └── Recommendation: GA4 import preferred (single source of truth)
│
├─► GA4 vs GOOGLE ADS DISCREPANCY
│   │
│   ├── Expected discrepancy: 10-30% difference is NORMAL
│   │   ├── Reason: Different attribution models (GA4 data-driven vs Google Ads last-click)
│   │   ├── Reason: Different counting methods (GA4 = user-scoped, Google Ads = click-scoped)
│   │   ├── Reason: Different attribution windows
│   │   └── Reason: Cross-device tracking differences
│   │
│   ├── Large discrepancy (>30%)?
│   │   ├── Check: GA4 property → Admin → Google Ads Linking → is it active?
│   │   ├── Check: GA4 Key Events → are the right events marked?
│   │   ├── Check: Google Ads → "All Conversions" column vs "Conversions" column
│   │   ├── Fix: Align attribution windows between GA4 and Google Ads
│   │   └── Fix: Compare same date ranges (GA4 uses event date, Google Ads uses click date)
│   │
│   └── Best practice: Pick ONE source for optimization decisions
│       ├── GA4 for holistic view (all traffic sources)
│       └── Google Ads for in-platform optimization (use its own data)
│
├─► ENHANCED CONVERSIONS NOT WORKING
│   │
│   ├── Status shows "No recent data"?
│   │   ├── Check: user_data object in dataLayer → email, phone, name, address
│   │   ├── Check: SHA-256 hashing format (lowercase, trimmed, no spaces)
│   │   ├── Check: Consent → ad_user_data must be "granted"
│   │   └── Fix: Wait 48-72 hours for status to update after implementation
│   │
│   ├── Low match rate (<30%)?
│   │   ├── Add more user data fields (each additional field improves matching)
│   │   ├── Priority order: email > phone > first_name + last_name > address
│   │   ├── Fix: Ensure hashing is correct (common: email not lowercased before hashing)
│   │   └── Fix: Send unhashed data if using Google's auto-hashing (via gtag or GTM)
│   │
│   └── Enhanced Conversions for Leads (offline)?
│       ├── Check: GCLID being captured and stored in CRM
│       ├── Check: Upload format matches expected schema
│       ├── Check: Conversion action name matches exactly (case-sensitive)
│       └── Fix: Validate with test upload (small batch) before full import
│
├─► OFFLINE CONVERSION IMPORT FAILING
│   │
│   ├── GCLID issues?
│   │   ├── Check: GCLID format (starts with "Cj" or "EAI", 50-100 chars)
│   │   ├── Check: GCLID age (must be within 90 days)
│   │   ├── Check: Auto-tagging enabled in Google Ads settings
│   │   ├── Fix: Capture GCLID from URL parameter on landing page
│   │   └── Fix: Store with lead record in CRM immediately on form submit
│   │
│   ├── Upload errors?
│   │   ├── "INVALID_CONVERSION_ACTION" → conversion action name doesn't match
│   │   ├── "TOO_RECENT" → conversion happened within last 6 hours
│   │   ├── "EXPIRED_CLICK" → GCLID is older than 90 days
│   │   ├── "DUPLICATE" → same GCLID + conversion action + timestamp already uploaded
│   │   └── Fix: Handle partial failures — some rows may succeed while others fail
│   │
│   └── Timezone issues?
│       ├── Check: Upload timestamps include timezone offset
│       ├── Check: Account timezone matches upload data timezone
│       └── Fix: Use UTC with explicit offset (e.g., "2026-04-04 14:30:00+02:00")
│
└─► TAG FIRING BUT WRONG VALUES
    │
    ├── Revenue/value not recording?
    │   ├── Check: value parameter is a number (not string, not formatted with currency symbol)
    │   ├── Check: currency parameter is ISO 4217 (e.g., "EUR" not "€")
    │   ├── Fix: Use dataLayer push: dataLayer.push({value: 49.99, currency: 'EUR'})
    │   └── Fix: In GTM, map Data Layer Variable to conversion tag value field
    │
    └── Wrong conversion action recording?
        ├── Check: Multiple conversion actions → is the right one set as "Primary"?
        ├── Check: "Include in Conversions" setting per action
        └── Fix: Only primary conversions are used for bidding; secondary for observation
```

## Debugging with MCP Tools

### Step 1: Check conversion setup
```
google_ads_run_gaql(query="
  SELECT conversion_action.name, conversion_action.status,
         conversion_action.type, conversion_action.counting_type,
         conversion_action.include_in_conversions_metric,
         conversion_action.attribution_model_settings.attribution_model
  FROM conversion_action
  WHERE conversion_action.status = 'ENABLED'
")
```

### Step 2: Check recent conversion data
```
google_ads_run_gaql(query="
  SELECT campaign.name, metrics.conversions, metrics.all_conversions,
         metrics.conversions_value, metrics.view_through_conversions
  FROM campaign
  WHERE segments.date DURING LAST_7_DAYS
  AND metrics.conversions > 0
  ORDER BY metrics.conversions DESC
")
```

### Step 3: Check conversion by action
```
google_ads_run_gaql(query="
  SELECT conversion_action.name, metrics.conversions,
         metrics.all_conversions, metrics.conversions_value
  FROM conversion_action
  WHERE segments.date DURING LAST_30_DAYS
  ORDER BY metrics.conversions DESC
")
```

### Step 4: Verify GTM tags
```
gtm_audit(container_id="GTM-XXXXXXX")
```
Look for: duplicate conversion tags, missing triggers, tag sequencing issues.

### Step 5: Cross-reference with GA4
```
ga4_run_report(dimensions=["sessionSource", "sessionMedium"],
               metrics=["conversions", "totalRevenue"],
               date_range="last7days")
```
Compare GA4 totals with Google Ads "All Conversions" column.

## Common Discrepancy Benchmarks

| Discrepancy | Typical Range | When to Investigate |
|------------|--------------|-------------------|
| GA4 vs Google Ads | 10-30% | >30% means setup issue |
| Google Ads vs Meta | 20-50% | Expected (different attribution) |
| Enhanced Conversions match rate | 50-80% | <30% means data quality issue |
| Consent Mode data recovery | 40-70% | <40% check modeling eligibility |
| Offline import success rate | 85-95% | <80% check GCLID capture |

## Quick Reference Card

```
CONVERSION NOT SHOWING?
→ Tag present? (DevTools → Network)
→ ID/Label correct? (Google Ads → Conversions)
→ Consent granted? (Check Consent Mode state)
→ Wait 24-48h for reporting lag

DUPLICATES?
→ Count = "One" for leads
→ Add transaction_id for purchases
→ Remove duplicate tags (gtm_audit)
→ Use ONE source: GA4 import OR direct tag

GA4 ≠ GOOGLE ADS?
→ 10-30% difference = normal
→ Align attribution windows
→ Compare "All Conversions" column
→ Pick ONE source for decisions

ENHANCED CONVERSIONS?
→ user_data in dataLayer?
→ ad_user_data consent = "granted"?
→ Correct hash format (SHA-256, lowercase)?
→ Wait 48-72h for status update
```

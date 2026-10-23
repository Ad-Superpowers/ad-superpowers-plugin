---
name: meta-privacy-compliance-checker
description: "This skill should be used when the user asks to \"check privacy compliance\", \"validate GDPR setup\", \"implement cookieless tracking\", or mentions \"Meta privacy compliance\", \"iOS 14 tracking setup\", or \"consent management for ads\". Do NOT use for: CAPI implementation details (use capi-implementation-guide), EMQ optimization (use emq-optimizer), attribution window decisions (use attribution-window-advisor)."
---
# Privacy Compliance Checker

## Overview

This skill helps check and implement privacy-compliant Meta Ads setups, including GDPR compliance, iOS 14+ adjustments, consent management, and cookieless tracking strategies.

## Privacy Landscape 2025-2026

### Key Privacy Developments

```
┌─────────────────────────────────────────────────────────────────┐
│  PRIVACY TIMELINE                                               │
│                                                                 │
│  2021: iOS 14.5 ATT - App Tracking Transparency (Apple)         │
│  2022: Google delays Chrome 3rd party cookie phase-out to 2024  │
│  Feb 2024: EU Digital Services Act applies to all platforms     │
│  Jul 2024: Google drops its plan to phase out 3rd party cookies │
│  Apr 2025: Chrome keeps 3rd party cookie choice, no new prompt  │
│  Jan 2026: Meta API stops returning 7d_view and 28d_view        │
│                                                                 │
│  IMPACT ON META ADS:                                            │
│  ├── Signal loss: less tracking data (size differs per account) │
│  ├── Attribution gaps: Conversions harder to measure            │
│  ├── Audience shrinkage: Retargeting pools smaller              │
│  └── Modeling: More reliant on AI/statistical modeling          │
└─────────────────────────────────────────────────────────────────┘
```

Sources (checked 2026-10-10): Apple Newsroom, iOS 14.5 release, 26 Apr 2021,
https://www.apple.com/newsroom/2021/04/ios-14-5-offers-unlock-iphone-with-apple-watch-diverse-siri-voices-and-more/;
Google, "Expanding testing for the Privacy Sandbox for the Web", 27 Jul 2022,
https://blog.google/products/chrome/update-testing-privacy-sandbox-web/; European Commission, "Digital Services Act
starts applying to all online platforms in the EU", 16 Feb 2024 (in force for all online intermediaries from
17 February 2024), https://digital-strategy.ec.europa.eu/en/news/digital-services-act-starts-applying-all-online-platforms-eu;
Google, "A new path for Privacy Sandbox on the web", 22 Jul 2024,
https://privacysandbox.google.com/blog/privacy-sandbox-update; Google, "Next steps for Privacy Sandbox and tracking
protections in Chrome", 22 Apr 2025, https://privacysandbox.google.com/blog/privacy-sandbox-next-steps; Meta for
Developers blog, "Ads Insights API Metric Availability Updates", 16 Oct 2025

## GDPR Compliance Checklist

### Data Collection & Consent

```
GDPR COMPLIANCE CHECKLIST
=========================

□ LEGAL BASIS FOR TRACKING
├── Consent mechanism on website?
├── Cookie banner compliant (not pre-checked)?
├── Clear opt-in for marketing cookies?
├── Rejection possible without disadvantages?
└── Status: [OK / Fix needed]

□ PRIVACY POLICY
├── Meta/Facebook pixel mentioned?
├── Purpose of data collection explained?
├── Third-party sharing disclosed?
├── Retention periods stated?
└── Status: [OK / Fix needed]

□ DATA SUBJECT RIGHTS
├── Right of access facilitated?
├── Right to deletion possible?
├── Right to object respected?
├── Contact for privacy questions?
└── Status: [OK / Fix needed]

□ COOKIE CONSENT MANAGEMENT
├── CMP (Consent Management Platform) active?
├── Pixel fires only AFTER consent?
├── Server events (CAPI) follow the same consent choice?
├── Audit trail of consent?
└── Status: [OK / Fix needed]
```

Meta's Business Tools Terms (effective 3 November 2025) say that where the law requires consent for cookies (the EU
is one example), you must ensure "in a verifiable manner" that people consent before you use Meta Business Tools to
store or access Meta cookies or other information on their device: https://www.facebook.com/legal/businesstech
(checked 2026-10-10).

### Consent Mode Implementation

```
CONSENT-BASED TRACKING SETUP
============================

OPTION 1: Load the Meta Pixel only after consent

// Only load pixel after consent
if (userHasConsented()) {
  // Load Facebook Pixel
  fbq('init', 'YOUR_PIXEL_ID');
  fbq('track', 'PageView');
} else {
  // Don't load pixel - no tracking
}

OPTION 2: Meta's own consent API (pauses Pixel fires until granted)

// Call revoke on every page, before init
fbq('consent', 'revoke');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');

// Once the visitor gives consent:
fbq('consent', 'grant');

OPTION 3: Google Consent Mode v2 (Google tags only)

// Consent Mode tells Google tags the consent state. It does not stop
// the Meta Pixel: gate the Meta Pixel tag in Google Tag Manager with
// Consent Settings > "Require additional consent for tag to fire"
// (for example ad_storage), or use option 1 or 2.
gtag('consent', 'default', {
  'analytics_storage': 'denied',
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied'
});

// After consent update:
gtag('consent', 'update', {
  'analytics_storage': 'granted',
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted'
});
```

Sources (checked 2026-10-10): Meta for Developers, Meta Pixel, "General Data Protection Regulation"; Google Ads Help, "About consent mode" ("Consent
mode lets you communicate your users' cookie or app identifier consent status to Google"),
https://support.google.com/google-ads/answer/10000067; Google for Developers, "Set up consent mode on websites"; Tag Manager Help, "Tag Manager consent mode
support", https://support.google.com/tagmanager/answer/10718549

## ATT & Signal Loss (Baseline Since 2021)

### Current State

```
ATT IMPACT (standard operating conditions since iOS 14.5)
=========================================================

ATTRIBUTION CHANGES (checked 2026-10-10):
├── Ad set settings: 1-day or 7-day click, 1-day view,
│   1-day engage-through (no 7d view, 28d view or 28d click)
├── Click-through counts only link clicks for website and
│   in-store conversions (rollout from March 2026)
├── Ads Insights API: 7d_view and 28d_view no longer returned
│   since 12 January 2026 (28d_click is still returned)
├── IMPORTANT: Data built on the old definitions or windows is
│   not like for like with newer data
├── SKAdNetwork app reporting: delays of at least 24 hours
└── API breakdowns of unique counts: 13 months of history

OPT-IN RATES:
└── No reliable average here: measure consent and ATT opt-in
    rates in your own CMP and app data

SIGNAL RECOVERY STRATEGIES:
├── Conversions API implementation
├── Aggregated Event Measurement (automatic for web events)
├── Value optimization (for high-value events)
└── Modeling (Meta's AI for gaps)
```

Sources (checked 2026-10-10): Meta Business Help Center, "About attribution models and attribution settings"; Meta for Business, "Simplifying Ad Measurement for a
Social-First World", 3 Mar 2026, https://www.facebook.com/business/news/click-attribution; Meta for Developers blog,
"Ads Insights API Metric Availability Updates", 16 Oct 2025; Meta Business
Help Center, "About Meta Ads Manager reporting for Apple's SKAdNetwork"

### Aggregated Event Measurement (AEM)

```
AEM CHECKLIST (web events)
==========================

AEM TODAY:
├── Events go through AEM automatically: no setup steps
├── The 8-event priority list per domain is gone, and so is
│   the AEM tab in Events Manager
└── No conversion domain to pick when you create a campaign

□ DOMAIN VERIFICATION (no longer needed for event configuration)
├── Still needed for other reasons, such as ad link editing
│   permissions or business verification?
├── DNS TXT record correct?
└── Status: [OK / Fix needed]

□ VALUE OPTIMIZATION
├── Value and currency sent with Purchase events?
├── No value sets needed any more
└── Status: [OK / Fix needed]
```

Sources (checked 2026-10-10, the AEM page carries no date for this change): Meta Business Help Center, "About Meta's
Aggregated Event Measurement"; "When to use domain
verification to verify your business"

## Conversions API Compliance

### CAPI Privacy Best Practices

```
CAPI PRIVACY SETUP
==================

□ DATA MINIMIZATION
├── Only send necessary parameters
├── No unnecessary PII
├── Hash every field Meta marks "hashing required"
└── Document which data you send

□ HASHING REQUIREMENTS
├── Email: SHA256, lowercase, trimmed
├── Phone: SHA256, digits only with country code
│   (no symbols, letters or leading zeros)
├── Names: SHA256, lowercase, no punctuation
├── The Meta Business SDK hashes these fields automatically
├── Do not hash client_ip_address, client_user_agent, fbc, fbp
└── Status: [OK / Fix needed]

□ CONSENT IN SERVER EVENTS
├── CAPI has no consent field: apply the visitor's consent
│   choice before you send an event
├── opt_out: true only keeps an event out of ads delivery
│   optimization; it is not a consent signal
├── data_processing_options ["LDU"] is Limited Data Use for
│   US state privacy laws, not GDPR consent
└── Status: [OK / Fix needed]

□ DATA PROCESSING TERMS
├── Meta Business Tools Terms accepted? Under GDPR they make
│   Meta Ireland your processor for matching, measurement and
│   analytics (Data Processing Terms) and a joint controller for
│   collecting event data (Controller Addendum)
├── DPA with CAPI partner (if applicable)?
└── Status: [OK / Fix needed]

CAPI EVENT EXAMPLE (Privacy-compliant):

{
  "event_name": "Purchase",
  "event_time": 1704067200,
  "action_source": "website",
  "event_source_url": "https://www.example.com/checkout/thank-you",
  "user_data": {
    "em": ["SHA256_HASH_EMAIL"],
    "ph": ["SHA256_HASH_PHONE"],
    "fbc": "fb.1.1234567890.AbCdEf",
    "fbp": "fb.1.1234567890.1234567890",
    "client_ip_address": "123.45.67.89",
    "client_user_agent": "Mozilla/5.0..."
  },
  "custom_data": {
    "currency": "USD",
    "value": 99.00
  },
  "opt_out": false,
  "data_processing_options": [],
  "data_processing_options_country": 0,
  "data_processing_options_state": 0
}
```

`action_source` is required for every event; `event_source_url` and `client_user_agent` are required for website
events. An empty `data_processing_options` list means Limited Data Use is off. Sources (checked 2026-10-10): Meta for
Developers, Conversions API, "Server Event Parameters"; "Customer Information
Parameters";
"Data Processing Options for US Users";
Meta Business Tools Terms (effective 3 November 2025), https://www.facebook.com/legal/businesstech

## Cookieless Future Preparation

### First-Party Data Strategy

```
FIRST-PARTY DATA PRIORITIES
============================

1. EMAIL COLLECTION
├── Incentivize newsletter signups
├── Promote account creation
├── Post-purchase email capture
└── Use: Custom Audiences, Value-based LAL

2. PHONE NUMBER
├── SMS marketing opt-in
├── Checkout phone field
└── Use: High-match custom audiences

3. ZERO-PARTY DATA
├── Preference surveys
├── Quiz/configurator data
├── Explicit stated interests
└── Use: Segmentation, personalization

4. SERVER-SIDE TRACKING
├── CAPI implementation
├── Server-side GTM
├── Hybrid pixel + CAPI
└── Use: Signal recovery, accuracy

FIRST-PARTY DATA COLLECTION FRAMEWORK:

Touchpoint          │ Data to Collect        │ Consent
────────────────────┼────────────────────────┼──────────
Newsletter popup    │ Email, name            │ Explicit
Account creation    │ Email, phone, address  │ Explicit
Purchase            │ Full contact + purchase│ Contract*
Quiz/Survey         │ Preferences, interests │ Explicit
Loyalty program     │ Purchase history       │ Explicit

*Not consent: GDPR has no implicit consent. Order data rests on the
 contract (Art. 6(1)(b)); for ad use, check consent or legitimate
 interest (Art. 6(1)(f)) against local regulations
```

GDPR (Regulation (EU) 2016/679), Art. 4(11) (consent is an "unambiguous indication"), Art. 6(1) and Recital 32
("Silence, pre-ticked boxes or inactivity should not therefore constitute consent"):
https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng (checked 2026-10-10).

### Audience Building Without Cookies

```
COOKIELESS AUDIENCE STRATEGIES
===============================

1. CUSTOMER LIST UPLOADS
├── Upload hashed email/phone lists
├── Match rate: compare with the account's earlier uploads
├── Refresh regularly (for example monthly)
└── Use for: Retargeting, Exclusions, LAL seed

2. ENGAGEMENT-BASED AUDIENCES
├── Video viewers (platform-native)
├── Page/Profile engagers
├── Ad engagers
├── Form engagers (Lead Ads)
└── No cookies needed - Meta platform data

3. WEBSITE CUSTOM AUDIENCES (with consent)
├── Implement with consent-first approach
├── Combine pixel + CAPI for accuracy
├── Shorter windows (consent decay)
└── Supplement with engagement audiences

4. BROAD TARGETING + AI
├── Let Meta's algorithm work
├── Advantage+ audience
├── Less specific = more scale
└── Trust machine learning

AUDIENCE MIX (set the split from the account's own results):
├── First-party data (uploads, engagement)
├── Broad/Advantage+ audience (AI-optimized)
├── Website audiences (consent-based)
└── Interest targeting
```

Meta's name for the product is "Advantage+ audience" (Meta Business Help Center, "About Advantage+ audience", checked 2026-10-10).

## Compliance Audit Template

### Full Privacy Audit Checklist

```
PRIVACY COMPLIANCE AUDIT
========================

Audit Date: [DATE]
Account: [ACCOUNT]
Region: [EU/US/Other]

SECTION 1: WEBSITE COMPLIANCE
────────────────────────────
□ Cookie banner present
□ Opt-in (not pre-checked)
□ Easy reject option
□ Privacy policy link
□ Cookie policy detailed
Score: ___/5

SECTION 2: PIXEL IMPLEMENTATION
──────────────────────────────
□ Pixel loads after consent
□ Consent choice applied (fbq consent API, CMP or GTM check)
□ No pre-consent tracking
□ Deduplication with CAPI
Score: ___/4

SECTION 3: CAPI COMPLIANCE
─────────────────────────
□ Data hashing correct
□ Minimal data principle
□ Consent choice applied to server events
□ Meta Business Tools Terms in place
Score: ___/4

SECTION 4: iOS 14+ SETUP & ATTRIBUTION
──────────────────────────────────────
□ Domain verified where still needed (link editing, business verification)
□ No leftover AEM setup relied on (the 8-event list is gone)
□ Value and currency sent with purchase events
□ Modeled results understood (statistical modeling for missing data)
□ Attribution setting per ad set known (1d/7d click, 1d view, 1d engage-through)
□ Reports and connectors no longer request 7d_view or 28d_view (API stopped returning them 12 Jan 2026)
Score: ___/6

SECTION 5: AUDIENCE COMPLIANCE
─────────────────────────────
□ Consent for custom audiences
□ Customer list compliance
□ Retention policies
□ Data deletion process
Score: ___/4

TOTAL SCORE: ___/21

INTERPRETATION (rules of thumb, not Meta figures or a legal standard):
├── 19-21: Excellent compliance
├── 15-18: Good, minor fixes needed
├── 10-14: Fair, significant gaps
└── <10:   Poor, urgent action needed

ACTION ITEMS:
1. [Item]
2. [Item]
3. [Item]
```

## MCP Tool Integration

### Checking Signal Quality with Live Data

```
1. Attributed conversions (not CAPI event volumes: check those in Events Manager;
   EMQ per event comes from meta_query(account_id, "dataset_quality", entity_id=<pixel_id>)):
→ meta_get_insights(account_id="...", fields=["action_values","actions","cost_per_action_type"], date_preset="last_7d", level="account")

2. Pixel status (last_fired_time, automatic matching, first_party_cookie_status):
→ meta_query(account_id="...", entity_type="adspixels")

3. Attribution setting per ad set:
→ meta_query(account_id="...", entity_type="adsets", fields=["id","name","attribution_spec"])
   Note: meta_get_insights has no attribution-window parameter; results follow each
   ad set's own setting. A break against history can come from the March 2026
   click-through change (link clicks only) or from reports that used 7d_view or 28d_view.
```

## Example Interaction

**User**: "I want to make sure my Meta Ads setup is GDPR-compliant. What should I check?"

**Claude response**:

"I'll help you with a GDPR compliance check for your Meta Ads. Here are the key points:

---

**QUICK GDPR CHECK:**

**1. Cookie Consent Banner:**
- [ ] Banner appears for ALL cookies?
- [ ] Reject button as prominent as Accept?
- [ ] No pre-checked boxes?
- [ ] Pixel does NOT load before consent?

**2. Privacy Policy:**
- [ ] Meta/Facebook pixel mentioned?
- [ ] Purpose of tracking explained?
- [ ] Contact for privacy requests?

**3. Technical Implementation:**
- [ ] Pixel conditional on consent?
- [ ] CAPI sends events only for visitors who consented?

---

**TEST YOUR SETUP:**

1. **Open your website in incognito**
2. **Open browser DevTools → Network tab**
3. **Filter on 'facebook'**
4. **BEFORE you give consent:**
   - Do you see facebook requests? → Not compliant
   - No requests? → Good
5. **AFTER consent:**
   - Do you see pixel fire? → Correct

---

**RED FLAGS:**

- Cookie banner with only 'Accept' button
- Pre-checked consent boxes
- Pixel loads before consent
- No privacy policy
- No data deletion process

---

**RECOMMENDED TOOLS:**

- **CMP**: Cookiebot, OneTrust, Usercentrics
- **Testing**: Meta Ads Data Advisor (formerly Meta Pixel Helper), Ghostery

Would you like me to dive deeper into a specific area?"

---
name: privacy-compliance-checker
description: Controleer Meta Ads setup op privacy compliance met GDPR, iOS 14+ tracking en cookieless advertising best practices. Gebruik deze skill wanneer je compliance wilt valideren of privacy-first strategieën wilt implementeren.
---

# Privacy Compliance Checker

## Overview

Deze skill helpt bij het controleren en implementeren van privacy-compliant Meta Ads setups, inclusief GDPR naleving, iOS 14+ aanpassingen, consent management en cookieless tracking strategieën.

## Privacy Landscape 2025-2026

### Belangrijke Privacy Ontwikkelingen

```
┌─────────────────────────────────────────────────────────────────┐
│  PRIVACY TIMELINE                                               │
│                                                                 │
│  2021: iOS 14 ATT - App Tracking Transparency                   │
│  2022: Meta Conversions API mainstream                          │
│  2023: Google delays 3rd party cookie deprecation               │
│  2024: DSA (Digital Services Act) enforcement EU                │
│  2025: Chrome 3rd party cookie phase-out begint                 │
│  2026: Volledig cookieless advertising era                      │
│                                                                 │
│  IMPACT OP META ADS:                                            │
│  ├── Signal loss: ~50% minder tracking data                     │
│  ├── Attribution gaps: Conversies moeilijker te meten           │
│  ├── Audience shrinkage: Retargeting pools kleiner              │
│  └── Modeling: Meer afhankelijk van AI/statistical modeling     │
└─────────────────────────────────────────────────────────────────┘
```

## GDPR Compliance Checklist

### Data Collection & Consent

```
GDPR COMPLIANCE CHECKLIST
=========================

□ LEGAL BASIS VOOR TRACKING
├── Consent mechanism op website?
├── Cookie banner compliant (niet pre-checked)?
├── Duidelijke opt-in voor marketing cookies?
├── Weigering mogelijk zonder nadelen?
└── Status: [✅ OK / ❌ Fix needed]

□ PRIVACY POLICY
├── Meta/Facebook pixel vermeld?
├── Doel van data collection uitgelegd?
├── Third-party sharing disclosed?
├── Retentie periodes vermeld?
└── Status: [✅ OK / ❌ Fix needed]

□ DATA SUBJECT RIGHTS
├── Recht op inzage facilitated?
├── Recht op verwijdering mogelijk?
├── Recht op bezwaar gerespecteerd?
├── Contact voor privacy vragen?
└── Status: [✅ OK / ❌ Fix needed]

□ COOKIE CONSENT MANAGEMENT
├── CMP (Consent Management Platform) actief?
├── Pixel vuur alleen NA consent?
├── Consent signal naar Meta gestuurd?
├── Audit trail van consent?
└── Status: [✅ OK / ❌ Fix needed]
```

### Consent Mode Implementation

```
CONSENT-BASED TRACKING SETUP
============================

OPTIE 1: Meta Pixel met Consent Mode

// Pixel alleen laden na consent
if (userHasConsented()) {
  // Load Facebook Pixel
  fbq('init', 'YOUR_PIXEL_ID');
  fbq('track', 'PageView');
} else {
  // Don't load pixel - geen tracking
}

OPTIE 2: Meta met Google Consent Mode v2

// Consent Mode v2 integratie
gtag('consent', 'default', {
  'analytics_storage': 'denied',
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied'
});

// Na consent update:
gtag('consent', 'update', {
  'analytics_storage': 'granted',
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted'
});
```

## iOS 14+ Compliance

### ATT Framework Impact

```
iOS 14+ IMPACT ASSESSMENT
=========================

ATTRIBUTION CHANGES:
├── 28-day click: Beperkt tot 7-day
├── 28-day view: Beperkt tot 1-day
├── Real-time reporting: Vertraagd (tot 72 uur)
└── Breakdown: Minder granular

OPT-IN RATES (gemiddeld):
├── Worldwide: ~25-35% opt-in
├── EU: ~20-30% opt-in
├── US: ~30-40% opt-in
└── App vs Web: Apps harder getroffen

SIGNAL RECOVERY STRATEGIEËN:
├── Conversions API implementatie
├── Aggregated Event Measurement (AEM)
├── Value optimization (voor high-value events)
└── Modeling (Meta's AI voor gaps)
```

### Aggregated Event Measurement (AEM)

```
AEM SETUP CHECKLIST
===================

□ DOMEIN VERIFICATIE
├── Domein geverifieerd in Business Settings?
├── DNS TXT record correct?
└── Status: [✅ OK / ❌ Fix needed]

□ EVENT PRIORITERING (Max 8 events)
├── Top 8 events geselecteerd?
├── Prioriteit volgorde bepaald?
├── Hoogste prioriteit = belangrijkste conversie?
└── Status: [✅ OK / ❌ Fix needed]

AANBEVOLEN PRIORITERING (E-commerce):
1. Purchase (hoogste)
2. InitiateCheckout
3. AddToCart
4. AddPaymentInfo
5. ViewContent
6. Lead
7. CompleteRegistration
8. PageView (laagste)

□ VALUE OPTIMIZATION
├── Value enabled voor Purchase event?
├── Value ranges ingesteld (4 buckets)?
└── Status: [✅ OK / ❌ Fix needed]
```

## Conversions API Compliance

### CAPI Privacy Best Practices

```
CAPI PRIVACY SETUP
==================

□ DATA MINIMIZATION
├── Stuur alleen noodzakelijke parameters
├── Geen onnodige PII
├── Hash alle identificeerbare data
└── Document welke data je stuurt

□ HASHING REQUIREMENTS
├── Email: SHA256, lowercase, trimmed
├── Phone: SHA256, E.164 format
├── Names: SHA256, lowercase
├── Gebruik Meta's hashing libraries
└── Status: [✅ OK / ❌ Fix needed]

□ CONSENT FORWARDING
├── Stuur consent status mee naar CAPI
├── opt_out parameter gebruiken
├── Respecteer user preferences
└── Status: [✅ OK / ❌ Fix needed]

□ DATA PROCESSING AGREEMENT
├── DPA met Meta ondertekend?
├── DPA met CAPI partner (als van toepassing)?
└── Status: [✅ OK / ❌ Fix needed]

CAPI EVENT VOORBEELD (Privacy-compliant):

{
  "event_name": "Purchase",
  "event_time": 1704067200,
  "user_data": {
    "em": ["SHA256_HASH_EMAIL"],
    "ph": ["SHA256_HASH_PHONE"],
    "fbc": "fb.1.1234567890.AbCdEf",
    "fbp": "fb.1.1234567890.1234567890",
    "client_ip_address": "123.45.67.89",
    "client_user_agent": "Mozilla/5.0..."
  },
  "custom_data": {
    "currency": "EUR",
    "value": 99.00
  },
  "opt_out": false,
  "data_processing_options": [],
  "data_processing_options_country": 0,
  "data_processing_options_state": 0
}
```

## Cookieless Future Preparation

### First-Party Data Strategy

```
FIRST-PARTY DATA PRIORITEITEN
=============================

1. EMAIL COLLECTION
├── Newsletter signups incentiveren
├── Account creation promoten
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
└── Use: Segmentatie, personalisatie

4. SERVER-SIDE TRACKING
├── CAPI implementatie
├── Server-side GTM
├── Hybrid pixel + CAPI
└── Use: Signal recovery, accuracy

FIRST-PARTY DATA COLLECTION FRAMEWORK:

Touchpoint          │ Data te Collecten      │ Consent
────────────────────┼────────────────────────┼──────────
Newsletter popup    │ Email, naam            │ Explicit
Account creation    │ Email, phone, address  │ Explicit
Purchase            │ Full contact + purchase│ Implicit*
Quiz/Survey         │ Preferences, interests │ Explicit
Loyalty program     │ Purchase history       │ Explicit

*Check local regulations for legitimate interest
```

### Audience Building Without Cookies

```
COOKIELESS AUDIENCE STRATEGIEËN
===============================

1. CUSTOMER LIST UPLOADS
├── Upload hashed email/phone lists
├── Match rate: 50-70% typisch
├── Refresh regelmatig (monthly)
└── Use for: Retargeting, Exclusions, LAL seed

2. ENGAGEMENT-BASED AUDIENCES
├── Video viewers (platform-native)
├── Page/Profile engagers
├── Ad engagers
├── Form engagers (Lead Ads)
└── No cookies needed - Meta platform data

3. WEBSITE CUSTOM AUDIENCES (met consent)
├── Implementeer met consent-first approach
├── Combineer pixel + CAPI voor accuracy
├── Kortere windows (consent decay)
└── Supplement met engagement audiences

4. BROAD TARGETING + AI
├── Laat Meta's algoritme werken
├── Advantage+ audiences
├── Minder specifiek = meer scale
└── Trust machine learning

RECOMMENDED AUDIENCE MIX 2025+:
├── 40% - First-party data (uploads, engagement)
├── 30% - Broad/Advantage+ (AI-optimized)
├── 20% - Website audiences (consent-based)
└── 10% - Interest targeting (declining utility)
```

## Compliance Audit Template

### Full Privacy Audit Checklist

```
PRIVACY COMPLIANCE AUDIT
========================

📅 Audit Datum: [DATUM]
🏢 Account: [ACCOUNT]
🌍 Regio: [EU/US/Other]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTIE 1: WEBSITE COMPLIANCE
────────────────────────────
□ Cookie banner aanwezig
□ Opt-in (niet pre-checked)
□ Easy reject optie
□ Privacy policy link
□ Cookie policy detailed
Score: ___/5

SECTIE 2: PIXEL IMPLEMENTATION
──────────────────────────────
□ Pixel laadt na consent
□ Consent signal correct
□ No pre-consent tracking
□ Deduplication met CAPI
Score: ___/4

SECTIE 3: CAPI COMPLIANCE
─────────────────────────
□ Data hashing correct
□ Minimal data principle
□ Consent forwarding
□ DPA in place
Score: ___/4

SECTIE 4: iOS 14+ SETUP
───────────────────────
□ Domain verified
□ AEM configured
□ Event prioritization
□ Value optimization
Score: ___/4

SECTIE 5: AUDIENCE COMPLIANCE
─────────────────────────────
□ Consent voor custom audiences
□ Customer list compliance
□ Retention policies
□ Data deletion process
Score: ___/4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TOTAL SCORE: ___/21

INTERPRETATIE:
├── 19-21: 🟢 Excellent compliance
├── 15-18: 🟡 Good, minor fixes needed
├── 10-14: 🟠 Fair, significant gaps
└── <10:   🔴 Poor, urgent action needed

ACTION ITEMS:
1. [Item]
2. [Item]
3. [Item]
```

## Voorbeeld Interactie

**Gebruiker**: "Ik wil zeker weten dat mijn Meta Ads setup GDPR-compliant is. Wat moet ik checken?"

**Claude response**:

"Ik help je met een GDPR compliance check voor je Meta Ads. Hier zijn de belangrijkste punten:

---

**QUICK GDPR CHECK (5 minuten):**

**1. Cookie Consent Banner:**
- [ ] Banner verschijnt voor ALLE cookies?
- [ ] Reject button even prominent als Accept?
- [ ] Geen pre-checked boxes?
- [ ] Pixel laadt NIET voor consent?

**2. Privacy Policy:**
- [ ] Meta/Facebook pixel mentioned?
- [ ] Doel van tracking uitgelegd?
- [ ] Contact voor privacy requests?

**3. Technical Implementation:**
- [ ] Pixel conditional op consent?
- [ ] CAPI stuurt consent signal mee?

---

**TEST JE SETUP:**

1. **Open je website in incognito**
2. **Open browser DevTools → Network tab**
3. **Filter op 'facebook'**
4. **VOOR je consent geeft:**
   - Zie je facebook requests? → ❌ Niet compliant
   - Geen requests? → ✅ Goed
5. **NA consent:**
   - Zie je pixel fire? → ✅ Correct

---

**RODE VLAGGEN:**

🚩 Cookie banner met alleen 'Accept' button
🚩 Pre-checked consent boxes
🚩 Pixel laadt voor consent
🚩 Geen privacy policy
🚩 Geen data deletion process

---

**AANBEVOLEN TOOLS:**

- **CMP**: Cookiebot, OneTrust, Usercentrics
- **Testing**: Facebook Pixel Helper, Ghostery

Wil je dat ik een specifiek onderdeel dieper uitwerk?"

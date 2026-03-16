---
name: ga4-debugging-validation
description: "GA4 debugging en data validatie gids. Gebruik voor: (1) DebugView gebruiken voor real-time debugging, (2) Tag implementatie valideren, (3) Data quality checks uitvoeren, (4) Event tracking problemen oplossen, (5) GA4 audit en troubleshooting. Triggers: debugview, tag validatie, data quality, event debugging, ga4 troubleshooting, tracking audit, implementation check."
---

# GA4 Debugging & Validation Guide

Complete gids voor het debuggen van GA4 implementaties en het waarborgen van data kwaliteit.

## Quick Decision Tree

```
GA4 DEBUGGING FLOW
│
├─► WAT WIL JE DEBUGGEN?
│   ├─► Real-time event testing
│   │   └─► GA4 DebugView
│   │
│   ├─► Tag firing issues
│   │   └─► GTM Preview Mode + Tag Assistant
│   │
│   ├─► Network requests
│   │   └─► Browser DevTools Network tab
│   │
│   └─► Historical data issues
│       └─► Data Quality reports + Explorations
│
├─► WANNEER TESTEN?
│   ├─► Tijdens development
│   │   └─► Chrome extension + DebugView
│   │
│   ├─► Na deployment
│   │   └─► QA checklist + automated tests
│   │
│   └─► Ongoing monitoring
│       └─► Data anomaly alerts
│
└─► WELKE BROWSER/DEVICE?
    ├─► Desktop Chrome
    │   └─► GA Debugger extension + DevTools
    │
    ├─► Mobile web
    │   └─► Remote debugging + DebugView
    │
    └─► Mobile app
        └─► Firebase DebugView
```

## GA4 DebugView Setup

```
DEBUGVIEW CONFIGUREREN
======================

WAT IS DEBUGVIEW:
├── Real-time event monitoring in GA4
├── Toont events binnen 1 minuut
├── Inclusief parameters en user properties
├── Perfect voor development en QA
└── Geen impact op productie data

LOCATIE: GA4 Admin → Property → DebugView

METHODE 1: CHROME EXTENSION
───────────────────────────
1. Installeer "Google Analytics Debugger" extension
   └── Chrome Web Store → zoek "GA Debugger"

2. Activeer extension (icon in toolbar)

3. Refresh pagina waar GA4 actief is

4. Open GA4 → Admin → DebugView

5. Selecteer je device in dropdown

⚠️ LET OP:
├── Extension moet AAN staan
├── Kan 1-2 minuten duren voor device verschijnt
└── Meerdere devices kunnen zichtbaar zijn


METHODE 2: GTM PREVIEW MODE
───────────────────────────
1. Open GTM → Preview

2. Vul website URL in

3. Debug sessie start automatisch

4. Events zijn zichtbaar in:
   ├── GTM Preview panel
   └── GA4 DebugView

VOORDEEL: Zie GTM tag firing + GA4 tegelijk


METHODE 3: DEBUG PARAMETER
──────────────────────────
Voeg parameter toe aan URL:
https://example.com?debug_mode=true

OF in GTM tag configuratie:
├── GA4 Configuration tag
├── Fields to Set
├── Field name: debug_mode
└── Value: true

OF via dataLayer:
gtag('config', 'G-XXXXXXXXXX', { 'debug_mode': true });


METHODE 4: MOBILE APP DEBUGGING
───────────────────────────────
iOS:
├── Xcode → Product → Scheme → Edit Scheme
├── Arguments Passed On Launch
└── Add: -FIRAnalyticsDebugEnabled

Android:
adb shell setprop debug.firebase.analytics.app [package_name]

Stop debugging:
adb shell setprop debug.firebase.analytics.app .none.
```

## DebugView Interpreteren

```
DEBUGVIEW INTERFACE UITLEG
==========================

HOOFDSECTIES:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Sectie                  │ Toont                                    │
├─────────────────────────┼──────────────────────────────────────────┤
│ Device selector         │ Debug devices (kies juiste device)       │
├─────────────────────────┼──────────────────────────────────────────┤
│ Timeline (links)        │ Chronologische event stream              │
├─────────────────────────┼──────────────────────────────────────────┤
│ Event details (rechts)  │ Parameters van geselecteerd event        │
├─────────────────────────┼──────────────────────────────────────────┤
│ Top events (boven)      │ Meest recente events (snel overzicht)    │
└─────────────────────────┴──────────────────────────────────────────┘

EVENT KLEUR CODES:
──────────────────
🟢 Groen     → Automatisch verzamelde events (first_visit, session_start)
🔵 Blauw    → Enhanced Measurement events (scroll, click, etc.)
🟣 Paars    → Custom events (jouw implementatie)
🟡 Geel     → Conversies (key events)
🔴 Rood     → Errors of issues

EVENT PARAMETERS CHECKEN:
─────────────────────────
1. Klik op event in timeline
2. Bekijk "Parameters" sectie rechts
3. Verify:
   ├── Alle verwachte parameters aanwezig
   ├── Waarden correct (types: string/int/double)
   ├── Geen lege waarden waar data verwacht
   └── Parameter namen exact juist (case sensitive!)

USER PROPERTIES:
────────────────
├── Scroll naar beneden in event details
├── "User properties" sectie
├── Check dat custom user properties correct set zijn
└── Persistent across sessions

COMMON ISSUES TE SPOTTEN:
─────────────────────────
├── Event niet zichtbaar → Tag niet gefired
├── Parameters ontbreken → DataLayer issue
├── Verkeerde waarden → Mapping/transformatie fout
├── Duplicate events → Meerdere tags voor zelfde event
└── Events te snel → Possible bot/automation
```

## GTM Preview Mode

```
GTM PREVIEW DEBUGGING
=====================

STARTEN:
────────
1. Open GTM container
2. Click "Preview" (rechtsboven)
3. Vul website URL in
4. Debug tab opent automatisch

INTERFACE ONDERDELEN:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Panel                   │ Functie                                  │
├─────────────────────────┼──────────────────────────────────────────┤
│ Summary                 │ Overzicht van gefirde tags               │
├─────────────────────────┼──────────────────────────────────────────┤
│ Tags                    │ Alle tags, welke fired/not fired         │
├─────────────────────────┼──────────────────────────────────────────┤
│ Variables               │ Waarden van alle variabelen              │
├─────────────────────────┼──────────────────────────────────────────┤
│ Data Layer              │ Complete dataLayer inhoud                │
├─────────────────────────┼──────────────────────────────────────────┤
│ Errors                  │ JavaScript errors, tag failures         │
└─────────────────────────┴──────────────────────────────────────────┘

EVENT SELECTIE:
───────────────
├── Links: Lijst van GTM events
├── Selecteer event om state te zien
├── "Container Loaded" = DOM Ready
├── "Window Loaded" = Window Load
├── Custom events (add_to_cart, purchase, etc.)
└── DataLayer events

VEELVOORKOMENDE DEBUG ACTIES:
─────────────────────────────
1. TAG FIRED NIET
   ├── Check Triggers: Klopt trigger conditie?
   ├── Check Variables: Hebben expected values?
   ├── Check Blocking: Zijn er exception triggers?
   └── Check event timing: Komt event aan?

2. TAG FIRED VERKEERDE WAARDEN
   ├── Variables tab: Check variable waarden
   ├── Data Layer tab: Check source data
   └── Compare met verwachte waarden

3. DUPLICATE TAGS
   ├── Tags tab: Check "Times Fired"
   └── Review trigger configuratie

GTM PREVIEW TIPS:
─────────────────
├── Share preview link met team (knop rechtsboven)
├── Clear cookies als preview niet werkt
├── Check voor conflicting extensions
├── Use incognito als normaal window issues geeft
└── Break on event voor complexe debugging
```

## Browser DevTools Debugging

```
CHROME DEVTOOLS VOOR GA4
========================

NETWORK TAB:
────────────
1. Open DevTools (F12 of Cmd+Opt+I)
2. Ga naar Network tab
3. Filter op: "collect" of "google-analytics"

WAT TE ZIEN:
├── collect requests = events naar GA4
├── Payload bevat encoded event data
├── Response 204 = success
└── Response errors = tracking issues

DECODED PARAMETERS:
───────────────────
Query string parameters decoderen:
├── en = event name
├── ep.* = event parameters
├── up.* = user properties
├── cid = client ID
├── tid = tracking/measurement ID
└── _ss = session start (1 = new session)

CONSOLE TAB:
────────────
// DataLayer inspecteren
console.log(dataLayer);

// GA4 debug logging aanzetten
gtag('config', 'G-XXXXXX', { 'debug_mode': true });

// Custom event testen
gtag('event', 'test_event', {
  'custom_param': 'test_value'
});

// DataLayer event pushen
dataLayer.push({
  event: 'test_event',
  test_param: 'test_value'
});


ELEMENTS TAB:
─────────────
├── Verify GTM container snippet aanwezig
├── Check voor gtag.js of analytics.js conflicts
├── Inspect data attributes op elementen
└── Check consent management implementation


APPLICATION TAB:
────────────────
├── Cookies: Check _ga, _gid cookies
├── LocalStorage: Check GTM storage
├── Session Storage: Check session data
└── Verify consent preferences stored
```

## Data Quality Checks

```
GA4 DATA QUALITY CHECKLIST
==========================

DAGELIJKSE CHECKS:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Check                   │ Hoe te verifiëren                        │
├─────────────────────────┼──────────────────────────────────────────┤
│ Events coming in        │ Realtime rapport > 0 users               │
├─────────────────────────┼──────────────────────────────────────────┤
│ Key events tracking     │ Conversions rapport heeft data           │
├─────────────────────────┼──────────────────────────────────────────┤
│ E-commerce data         │ Monetization rapport heeft revenue       │
├─────────────────────────┼──────────────────────────────────────────┤
│ No sudden drops         │ Vergelijk met vorige dag/week            │
├─────────────────────────┼──────────────────────────────────────────┤
│ No sudden spikes        │ Check voor bot traffic of errors         │
└─────────────────────────┴──────────────────────────────────────────┘

WEKELIJKSE CHECKS:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Check                   │ Verwachte uitkomst                       │
├─────────────────────────┼──────────────────────────────────────────┤
│ Bounce rate             │ 20-70% (afhankelijk van site type)       │
├─────────────────────────┼──────────────────────────────────────────┤
│ Avg. session duration   │ > 30 seconden (meeste sites)             │
├─────────────────────────┼──────────────────────────────────────────┤
│ Conversion rate         │ Consistent met historisch                │
├─────────────────────────┼──────────────────────────────────────────┤
│ Traffic source data     │ (not set) < 5% van traffic               │
├─────────────────────────┼──────────────────────────────────────────┤
│ Device distribution     │ Consistent met verwachtingen             │
└─────────────────────────┴──────────────────────────────────────────┘

DATA ANOMALY DETECTION:
───────────────────────
SIGNIFICANT DEVIATION THRESHOLDS:
├── Users: > 30% verschil vs vorige week
├── Sessions: > 30% verschil
├── Pageviews: > 30% verschil
├── Conversions: > 20% verschil
├── Revenue: > 20% verschil
└── Bounce rate: > 10 percentage points

AUTOMATED ALERTS SETUP:
───────────────────────
1. GA4 → Admin → Custom Insights
2. Create → Anomaly detection
3. Configure:
   ├── Metric: Users/Sessions/etc.
   ├── Evaluation period: Daily/Weekly
   ├── Anomaly condition: % change
   └── Notification: Email
```

## Event Validation Queries

```
GA4 EXPLORATION VOOR VALIDATIE
==============================

EXPLORATION 1: EVENT COMPLETENESS
─────────────────────────────────
Technique: Free form

Setup:
├── Rows: Event name
├── Values:
│   ├── Event count
│   ├── Users
│   └── Event value (indien relevant)
├── Date range: Last 7 days
└── Export en vergelijk met expected events

CHECK:
├── Alle verwachte events aanwezig
├── Geen onverwachte event namen
├── Event counts in verwachte range
└── Geen events met 0 users (ghost events)


EXPLORATION 2: PARAMETER FILL RATE
──────────────────────────────────
Technique: Free form

Setup:
├── Rows: Event name
├── Values:
│   ├── Event count (alle)
│   ├── [Custom metric voor parameter count]
├── Filter: Specifiek event type

⚠️ Noot: Parameter fill rate vereist BigQuery of calculated metric


EXPLORATION 3: ECOMMERCE FUNNEL VALIDATION
──────────────────────────────────────────
Technique: Funnel exploration

Setup:
├── Steps:
│   ├── view_item
│   ├── add_to_cart
│   ├── begin_checkout
│   └── purchase
└── Validate drop-off rates zijn realistisch

RED FLAGS:
├── 100% completion rate → possible duplicate events
├── 0% completion rate → broken tracking
├── Completion > 100% → sequence issues
└── Grote gaps → missing events


EXPLORATION 4: SOURCE/MEDIUM QUALITY
────────────────────────────────────
Technique: Free form

Setup:
├── Rows: Session source/medium
├── Values: Sessions
├── Sort: Descending

CHECK:
├── "(not set)" percentage (doel: < 5%)
├── "(direct) / (none)" niet te hoog
├── Verwachte sources aanwezig
└── Geen bizarre/spam sources
```

## Implementation Audit Checklist

```
GA4 IMPLEMENTATION AUDIT
========================

□ BASE SETUP
├── □ Measurement ID correct (G-XXXXXXXXXX)
├── □ Property timezone juist
├── □ Property currency juist
├── □ Data retention op 14 maanden
├── □ Google Signals geconfigureerd
└── □ BigQuery export (indien nodig)

□ DATA STREAMS
├── □ Web stream actief
├── □ Enhanced Measurement geconfigureerd
├── □ Site search parameter correct
├── □ Cross-domain tracking (indien nodig)
└── □ Referral exclusion list juist

□ EVENT TRACKING
├── □ page_view fires op alle pagina's
├── □ Automatic events werken
├── □ Custom events correct geïmplementeerd
├── □ Event parameters aanwezig
├── □ Event naming consistent
└── □ Geen duplicate events

□ E-COMMERCE (indien van toepassing)
├── □ view_item event werkt
├── □ add_to_cart event werkt
├── □ purchase event werkt
├── □ transaction_id is uniek
├── □ Revenue data correct
├── □ Currency juist
└── □ Items array populated

□ CONVERSIONS
├── □ Key events gemarkeerd
├── □ Conversion counting juist
├── □ Attribution settings correct
└── □ Google Ads import (indien gekoppeld)

□ USER TRACKING
├── □ user_id correct geïmplementeerd (indien nodig)
├── □ User properties correct set
├── □ Consent mode werkend
└── □ PII compliance (geen PII in data)

□ GTM CONFIGURATION
├── □ Container correct geplaatst
├── □ Tags correct geconfigureerd
├── □ Triggers correct
├── □ Variables werken
├── □ No JavaScript errors
└── □ Container gepubliceerd

□ INTEGRATIONS
├── □ Google Ads gekoppeld
├── □ Search Console gekoppeld
├── □ BigQuery gekoppeld (optioneel)
└── □ Third-party tools werkend
```

## Veelvoorkomende Tracking Problemen

```
TROUBLESHOOTING COMMON ISSUES
=============================

PROBLEEM: Events niet zichtbaar in DebugView
────────────────────────────────────────────
Oorzaken:
├── Debug mode niet actief
├── Ad blocker aan
├── Verkeerd device geselecteerd
├── Tag niet gefired
└── Consent niet gegeven

Oplossing:
├── Verify debug mode parameter/extension
├── Disable ad blockers
├── Check device selector in DebugView
├── Check GTM Preview
└── Accept consent, retry


PROBLEEM: Duplicate events
──────────────────────────
Oorzaken:
├── GTM tag fired meerdere keren
├── Zowel GTM als gtag.js implementatie
├── DataLayer push meerdere keren
├── Single Page App routing issues
└── Page reload triggers

Oplossing:
├── Check "Times Fired" in GTM Preview
├── Remove duplicate implementations
├── Add deduplication logic
├── Implement proper SPA tracking
└── Use session-based deduplication


PROBLEEM: Missing parameters
────────────────────────────
Oorzaken:
├── DataLayer niet correct
├── Variable mapping fout
├── Parameter naam typo
├── Timing issues (async)
└── Scope issues

Oplossing:
├── Log dataLayer in console
├── Check GTM variable values
├── Verify exact parameter names
├── Add wait/callback logic
├── Check JavaScript scope


PROBLEEM: (not set) in reports
──────────────────────────────
Oorzaken:
├── Traffic source data ontbreekt
├── UTM parameters niet geparsed
├── Cross-domain tracking issues
├── Referral exclusion incorrect
└── Direct traffic (legitimate)

Oplossing:
├── Review UTM tagging
├── Check auto-tagging (Google Ads)
├── Verify cross-domain setup
├── Review exclusion list
├── Accept some direct is normal


PROBLEEM: Revenue discrepancies
───────────────────────────────
Oorzaken:
├── Currency mismatch
├── Tax/shipping handling
├── Test orders in data
├── Duplicate transactions
├── Timing differences

Oplossing:
├── Verify currency settings
├── Document value calculation
├── Exclude test transactions
├── Check transaction_id uniqueness
├── Compare same time periods


PROBLEEM: Self-referrals
────────────────────────
Oorzaken:
├── Cross-domain tracking niet correct
├── Payment gateway redirects
├── Subdomains niet excluded
└── Third-party hosted pages

Oplossing:
├── Configure cross-domain list
├── Add payment domains to tracking
├── Add subdomains to stream
└── Implement linker on third-party
```

## Automated Testing Setup

```
AUTOMATED GA4 TESTING
=====================

PLAYWRIGHT TEST VOORBEELD:
──────────────────────────
// playwright.config.ts
import { PlaywrightTestConfig } from '@playwright/test';

const config: PlaywrightTestConfig = {
  use: {
    baseURL: 'https://example.com',
  },
};

export default config;

// tests/ga4-tracking.spec.ts
import { test, expect } from '@playwright/test';

test('GA4 page_view fires on page load', async ({ page }) => {
  // Intercept GA4 requests
  const ga4Requests: string[] = [];

  page.on('request', request => {
    if (request.url().includes('google-analytics.com/g/collect')) {
      ga4Requests.push(request.url());
    }
  });

  await page.goto('/');
  await page.waitForTimeout(2000);

  // Verify page_view event
  expect(ga4Requests.some(url => url.includes('en=page_view'))).toBeTruthy();
});

test('GA4 add_to_cart fires correctly', async ({ page }) => {
  const ga4Requests: string[] = [];

  page.on('request', request => {
    if (request.url().includes('google-analytics.com/g/collect')) {
      ga4Requests.push(request.url());
    }
  });

  await page.goto('/product/test-product');
  await page.click('[data-testid="add-to-cart"]');
  await page.waitForTimeout(2000);

  // Verify add_to_cart event
  const addToCartRequest = ga4Requests.find(url => url.includes('en=add_to_cart'));
  expect(addToCartRequest).toBeTruthy();

  // Verify item parameters
  expect(addToCartRequest).toContain('ep.item_id');
});

test('GA4 purchase fires with correct revenue', async ({ page }) => {
  // Complete checkout flow...
  // Verify purchase event with transaction_id and value
});


CYPRESS TEST VOORBEELD:
───────────────────────
// cypress/support/commands.ts
Cypress.Commands.add('interceptGA4', () => {
  cy.intercept('POST', '**/google-analytics.com/g/collect*').as('ga4');
});

// cypress/e2e/ga4-tracking.cy.ts
describe('GA4 Tracking', () => {
  beforeEach(() => {
    cy.interceptGA4();
  });

  it('fires page_view on load', () => {
    cy.visit('/');
    cy.wait('@ga4').then((interception) => {
      expect(interception.request.url).to.include('en=page_view');
    });
  });

  it('fires add_to_cart with parameters', () => {
    cy.visit('/product/123');
    cy.get('[data-testid="add-to-cart"]').click();
    cy.wait('@ga4').then((interception) => {
      expect(interception.request.url).to.include('en=add_to_cart');
      expect(interception.request.url).to.include('ep.item_id');
    });
  });
});


CI/CD INTEGRATION:
──────────────────
# .github/workflows/ga4-tests.yml
name: GA4 Tracking Tests

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 18

      - name: Install dependencies
        run: npm ci

      - name: Install Playwright
        run: npx playwright install

      - name: Run GA4 tests
        run: npx playwright test tests/ga4-tracking.spec.ts

      - name: Upload report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: playwright-report
          path: playwright-report/
```

## Output: Debugging Report Template

```markdown
# GA4 Debugging & Validation Rapport

## Audit Informatie
- **Property ID:** G-XXXXXXXXXX
- **Website:** [URL]
- **Audit datum:** [Datum]
- **Auditor:** [Naam]

## Executive Summary

| Categorie | Status | Score |
|-----------|--------|-------|
| Base Setup | ✅ Pass | 100% |
| Event Tracking | ⚠️ Issues | 85% |
| E-commerce | ✅ Pass | 100% |
| Data Quality | ⚠️ Issues | 90% |
| **Overall** | **⚠️** | **94%** |

## Base Setup Verification

| Check | Status | Notes |
|-------|--------|-------|
| Measurement ID correct | ✅ | G-XXXXXXXXXX |
| Timezone | ✅ | Europe/Amsterdam |
| Currency | ✅ | EUR |
| Data retention | ✅ | 14 months |
| Google Signals | ✅ | Enabled |
| Enhanced Measurement | ✅ | All enabled |

## Event Tracking Validation

### Automatic Events

| Event | Status | Notes |
|-------|--------|-------|
| page_view | ✅ | Fires correctly |
| first_visit | ✅ | Working |
| session_start | ✅ | Working |
| scroll | ✅ | 90% threshold |
| click | ✅ | Outbound clicks |

### Custom Events

| Event | Status | Parameters Verified | Notes |
|-------|--------|---------------------|-------|
| sign_up | ✅ | method | Working |
| login | ✅ | method | Working |
| purchase | ⚠️ | transaction_id, value | Missing coupon |
| add_to_cart | ✅ | items array | Working |

## E-commerce Validation

| Event | Status | Notes |
|-------|--------|-------|
| view_item | ✅ | All parameters present |
| add_to_cart | ✅ | Items array correct |
| begin_checkout | ✅ | Value matches cart |
| purchase | ✅ | Revenue verified vs backend |

### Revenue Reconciliation

| Source | Revenue | Variance |
|--------|---------|----------|
| GA4 | €12,345 | - |
| Backend | €12,401 | 0.45% |

**Status:** ✅ Within acceptable range (<1%)

## Data Quality Metrics

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| (not set) source | 3.2% | <5% | ✅ |
| Bounce rate | 45% | 20-70% | ✅ |
| Avg session | 2:34 | >30s | ✅ |
| Self-referrals | 0.1% | <1% | ✅ |

## Issues Found

### Critical (Blocking)
- None

### High Priority
1. **Missing coupon parameter in purchase event**
   - Impact: Cannot track promotion effectiveness
   - Fix: Add coupon to dataLayer purchase push

### Medium Priority
1. **Form submission double-firing**
   - Impact: Inflated form submission counts (~5%)
   - Fix: Add deduplication logic

### Low Priority
1. **Video engagement not tracking on custom player**
   - Impact: Missing video metrics
   - Fix: Implement custom video tracking

## Recommended Actions

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| 🔴 High | Add coupon parameter | Low | High |
| 🟡 Medium | Fix form double-fire | Medium | Medium |
| 🟢 Low | Video tracking | High | Low |

## Test Results

| Test Suite | Passed | Failed | Skipped |
|------------|--------|--------|---------|
| Page tracking | 12 | 0 | 0 |
| E-commerce | 8 | 1 | 0 |
| Custom events | 15 | 2 | 1 |
| **Total** | **35** | **3** | **1** |

## Next Steps

1. [ ] Fix coupon parameter in purchase event
2. [ ] Implement form deduplication
3. [ ] Re-run validation after fixes
4. [ ] Set up automated monitoring alerts

## Appendix

### DebugView Screenshots
[Attach relevant screenshots]

### GTM Preview Logs
[Attach relevant logs]

### Network Requests Sample
[Attach sample collect requests]
```

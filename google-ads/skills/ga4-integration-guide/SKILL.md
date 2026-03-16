---
name: ga4-integration-guide
description: "Google Ads en GA4 integratie gids. Gebruik voor: (1) Google Ads ↔ GA4 account linking, (2) GA4 conversies importeren naar Google Ads, (3) Audience import en sync, (4) Attribution model alignment, (5) Cross-platform reporting, (6) Campaign URL tagging. Triggers: ga4, google analytics, linking, audience, import, conversions, attribution, utm, campaign tagging, measurement."
---

# GA4 Integration Guide

Complete gids voor het koppelen van Google Ads met Google Analytics 4 voor betere audience targeting, conversie-attributie en cross-platform inzichten.

## Quick Decision Guide

```
WELKE GA4 INTEGRATIE HEB JE NODIG?
│
├─► BASIC LINKING
│   └─► GOOGLE ADS ↔ GA4 ACCOUNT LINK
│       ├── Zie Google Ads data in GA4
│       ├── Zie GA4 conversies in Google Ads
│       └── Automatische UTM parameter herkenning
│
├─► CONVERSIE TRACKING
│   └─► GA4 CONVERSIES → GOOGLE ADS IMPORT
│       ├── Gebruik GA4 als single source of truth
│       ├── Cross-device conversie tracking
│       └── Betere attributie dan client-side tags
│
├─► AUDIENCE TARGETING
│   └─► GA4 AUDIENCES → GOOGLE ADS
│       ├── Remarketing op basis van GA4 gedrag
│       ├── Lookalike audiences
│       └── Geavanceerde segment targeting
│
└─► FULL INTEGRATION
    └─► ALLE BOVENSTAANDE + REPORTING
        ├── Unified reporting
        ├── Cross-platform attribution
        └── Custom dimensions/metrics
```

## Google Ads ↔ GA4 Linking

### Linking Setup

```
GOOGLE ADS EN GA4 KOPPELEN
══════════════════════════

VEREISTEN:
──────────
□ Admin access in GA4 property
□ Admin access in Google Ads account
□ Zelfde Google account (of gekoppelde accounts)

STAP 1: VANUIT GA4
──────────────────
1. GA4 → Admin → Product links → Google Ads links
2. Click "Link"
3. Selecteer Google Ads account(s)
4. Configure settings:
   ├── Enable personalized advertising: ON
   ├── Enable auto-tagging: Aanbevolen ON
   └── Click "Next" → "Submit"

STAP 2: VERIFIEER LINKING
─────────────────────────
In GA4:
├── Admin → Google Ads links
└── Status: "Active" ✓

In Google Ads:
├── Tools → Linked accounts → Google Analytics (GA4)
└── Status: "Linked" ✓

WAT DEZE LINK ENABLED:
──────────────────────
┌─────────────────────────────────────────────────────────────────┐
│  FUNCTIONALITEIT               │ STATUS NA LINKING             │
├────────────────────────────────┼───────────────────────────────┤
│ Google Ads data in GA4         │ ✓ Automatisch                 │
│ GA4 conversies → Google Ads    │ ◐ Handmatig importeren       │
│ GA4 audiences → Google Ads     │ ◐ Handmatig enablen          │
│ Google Ads metrics in GA4      │ ✓ cost, clicks, impressions   │
│ Cross-platform attribution     │ ◐ Attribution settings        │
└────────────────────────────────┴───────────────────────────────┘

AUTO-TAGGING VS MANUAL TAGGING:
───────────────────────────────
AUTO-TAGGING (Aanbevolen):
├── Google Ads voegt gclid toe aan URLs
├── GA4 herkent automatisch
├── Meest accurate tracking
└── Enables: full Google Ads integration

MANUAL TAGGING (UTM):
├── Je voegt UTM parameters toe
├── Meer controle over source/medium
├── Nodig voor: cross-domain, third-party tools
└── Kan naast auto-tagging werken
```

### Attribution Model Alignment

```
ATTRIBUTION MODELS ALIGNEREN
════════════════════════════

PROBLEEM: GA4 EN GOOGLE ADS TONEN VERSCHILLENDE CONVERSIES
──────────────────────────────────────────────────────────

Oorzaken:
├── Verschillende attribution models
├── Verschillende lookback windows
├── Conversion counting (one vs every)
└── Cross-device handling

ATTRIBUTION MODEL OPTIES:
─────────────────────────

┌──────────────────────────────────────────────────────────────────┐
│ Model                │ Beschrijving           │ Use Case         │
├──────────────────────┼────────────────────────┼──────────────────┤
│ Data-driven          │ AI-based, adapteert    │ Aanbevolen      │
│                      │ zich aan jouw data     │ (default 2024+)  │
├──────────────────────┼────────────────────────┼──────────────────┤
│ Last Click           │ 100% naar laatste     │ Simpele funnel   │
│                      │ (non-direct) klik      │ vergelijking     │
├──────────────────────┼────────────────────────┼──────────────────┤
│ First Click          │ 100% naar eerste klik │ Awareness focus  │
├──────────────────────┼────────────────────────┼──────────────────┤
│ Linear               │ Gelijk verdeeld       │ Alle touchpoints │
│                      │                        │ even belangrijk  │
├──────────────────────┼────────────────────────┼──────────────────┤
│ Position-based       │ 40% first, 40% last   │ Balans awareness │
│                      │ 20% middle             │ + conversion     │
├──────────────────────┼────────────────────────┼──────────────────┤
│ Time decay           │ Meer naar recent      │ Short sales      │
│                      │                        │ cycles           │
└──────────────────────┴────────────────────────┴──────────────────┘

AANBEVOLEN ALIGNMENT:
─────────────────────
1. GA4: Admin → Attribution settings
   └── Reporting attribution model: Data-driven

2. Google Ads: Tools → Conversions → [Conversion] → Settings
   └── Attribution model: Data-driven

3. Lookback windows aligneren:
   ├── GA4: 30, 60, of 90 dagen
   └── Google Ads: Match met GA4 setting

⚠️ DATA-DRIVEN VEREIST:
├── Minimaal 300 conversies in 30 dagen
├── Minimaal 3000 ad interactions
└── Anders: fallback naar last-click
```

## GA4 Conversies Importeren

### Conversie Import Setup

```
GA4 CONVERSIES IMPORTEREN NAAR GOOGLE ADS
═════════════════════════════════════════

WAAROM GA4 CONVERSIES IMPORTEREN?
─────────────────────────────────
□ Single source of truth
□ Betere cross-device tracking
□ Inclusief modeled conversions
□ Minder duplicate tracking
□ Consistent met web analytics

WELKE CONVERSIES IMPORTEREN:
────────────────────────────
✓ Purchase (e-commerce)
✓ Form submissions (lead gen)
✓ Sign ups
✗ Page views (niet geschikt)
✗ Scroll depth (niet geschikt)
✗ Engagement events (gebruik GA4 audiences ipv)

STAP 1: GA4 CONVERSIE MARKEREN
──────────────────────────────
1. GA4 → Admin → Events
2. Vind of maak event (bijv. "generate_lead")
3. Toggle "Mark as conversion" ON

OF via custom event:
gtag('event', 'generate_lead', {
  'currency': 'EUR',
  'value': 50
});

STAP 2: IMPORTEREN IN GOOGLE ADS
────────────────────────────────
1. Google Ads → Tools → Conversions
2. "+ New conversion action"
3. "Import" → "Google Analytics 4 properties"
4. Selecteer gekoppelde GA4 property
5. Vink conversies aan die je wilt importeren
6. Configureer:
   ├── Conversion name (optioneel aanpassen)
   ├── Goal category: Lead, Purchase, etc.
   ├── Value: Use value from GA4 / Fixed value
   ├── Count: One (leads) / Every (sales)
   └── Attribution model: Data-driven

STAP 3: PRIMARY VS SECONDARY
────────────────────────────
□ Primary: Gebruikt voor bidding optimization
□ Secondary: Alleen voor observation

TIP: Start met secondary, promoveer naar primary
     na validatie (1-2 weken data)

SYNC TIMING:
────────────
□ Conversies sync elke 4-6 uur
□ Tot 24 uur vertraging mogelijk
□ Historical data: niet retroactief
```

### Conversie Discrepanties Oplossen

```
CONVERSIE DISCREPANTIES TROUBLESHOOTING
═══════════════════════════════════════

PROBLEEM: GOOGLE ADS EN GA4 CONVERSIES MATCHEN NIET
───────────────────────────────────────────────────

CHECK 1: ATTRIBUTION MODEL
──────────────────────────
GA4: Admin → Attribution settings
Google Ads: Conversions → Settings → Attribution

Zorg dat beide dezelfde model gebruiken (data-driven)

CHECK 2: LOOKBACK WINDOW
────────────────────────
GA4: Default 30 dagen
Google Ads: Check per conversie action

Aligneer beide naar 30 of 90 dagen

CHECK 3: COUNTING METHOD
────────────────────────
GA4: Telt unieke users per event (standaard)
Google Ads: "One" vs "Every"

Voor leads: "One" (één per user per day)
Voor purchases: "Every" (elke transactie)

CHECK 4: CONVERSION TIME
────────────────────────
GA4: Rapporteert op conversie timestamp
Google Ads (imported): Rapporteert op klik timestamp

→ Dit is normaal verschil, niet te fixen

CHECK 5: FILTERS EN SEGMENTS
────────────────────────────
GA4: Check of geen filters actief zijn
Google Ads: Check conversion action status

VERWACHTE DISCREPANTIES:
────────────────────────
□ 5-15% verschil is normaal
□ Cross-device conversies (GA4 heeft meer)
□ Modeled conversions (GA4 modelleert meer)
□ Timing verschillen (klik vs conversie datum)

ACTIE BIJ >20% VERSCHIL:
────────────────────────
1. Verify tracking implementation
2. Check voor duplicate tags
3. Verify consent mode is consistent
4. Check voor bot traffic filters
```

## GA4 Audiences naar Google Ads

### Audience Export Setup

```
GA4 AUDIENCES EXPORTEREN NAAR GOOGLE ADS
════════════════════════════════════════

VOORDELEN:
──────────
□ Gebaseerd op site gedrag (niet alleen ad clicks)
□ Complex conditions (sequences, exclusions)
□ Predictive audiences (likely to purchase)
□ Automatische sync

STAP 1: AUDIENCE MAKEN IN GA4
─────────────────────────────
1. GA4 → Admin → Audiences → "New audience"
2. Kies template of "Create custom audience"

AUDIENCE VOORBEELDEN:

HIGH-VALUE USERS:
├── Condition: transaction_value > €100
├── In last: 30 days
└── Use: High-value remarketing

CART ABANDONERS:
├── Condition 1: add_to_cart (include)
├── Condition 2: purchase (exclude)
├── In last: 7 days
└── Use: Cart recovery campaigns

ENGAGED USERS (NO CONVERSION):
├── Condition 1: session_duration > 120s
├── Condition 2: page_view count > 3
├── Condition 3: form_submit (exclude)
├── In last: 30 days
└── Use: Consideration remarketing

PREDICTIVE AUDIENCE:
├── Template: "Likely 7-day purchasers"
├── Google ML-based
├── Vereist: 1000+ purchases, 1000+ non-purchases
└── Use: Acquisition lookalike

STAP 2: ENABLE GOOGLE ADS EXPORT
────────────────────────────────
Bij audience creation:
□ "Enable personalized advertising" = ON

Dit enabled automatische sync naar Google Ads

STAP 3: VERIFICATIE IN GOOGLE ADS
─────────────────────────────────
1. Google Ads → Tools → Audience Manager
2. Filter: "GA4" or "[GA4 property name]"
3. Check:
   ├── List size (moet >1000 voor targeting)
   ├── Status: "Active"
   └── Last updated: Recent

AUDIENCE SIZING:
────────────────
┌─────────────────────────────────────────────────────────────────┐
│ Audience Size │ Search Remarketing │ Display/YouTube           │
├───────────────┼────────────────────┼───────────────────────────┤
│ <100          │ Te klein           │ Te klein                  │
│ 100-1,000     │ Usable             │ Te klein                  │
│ 1,000-10,000  │ Good               │ Usable                    │
│ 10,000+       │ Excellent          │ Good                      │
│ 100,000+      │ Excellent          │ Excellent                 │
└───────────────┴────────────────────┴───────────────────────────┘

⚠️ Audiences kleiner dan minimums worden niet gevuld
```

### Predictive Audiences

```
GA4 PREDICTIVE AUDIENCES
════════════════════════

BESCHIKBARE PREDICTIVE AUDIENCES:
─────────────────────────────────

1. LIKELY TO PURCHASE (7-DAY)
   ├── Users die waarschijnlijk kopen in 7 dagen
   ├── Vereist: 1000+ purchases in 28 dagen
   ├── Use: Bid boost, aggressive targeting
   └── Combined met: abandon cart, high-intent

2. LIKELY TO CHURN
   ├── Users die waarschijnlijk niet terugkomen
   ├── Vereist: 1000+ active + 1000+ churned users
   ├── Use: Retention campaigns, win-back
   └── Combined met: high-value customers

3. PREDICTED REVENUE (Top X%)
   ├── Highest predicted revenue users
   ├── Vereist: Revenue data, sufficient volume
   ├── Use: VIP targeting, premium campaigns
   └── Combined met: cross-sell audiences

SETUP:
──────
1. GA4 → Admin → Audiences
2. "New audience" → "Predictive"
3. Kies predictive metric
4. Set threshold (bijv. top 20%)
5. Enable Google Ads export

BEST PRACTICES:
───────────────
□ Combine predictive + behavioral
  Bijv: "Likely to purchase" + "Viewed product page"

□ Exclude converters
  Predictive audiences bevatten soms recente kopers

□ Adjust bids based on score
  Higher predicted value = higher bid

□ Monitor performance separately
  Predictive vs non-predictive segments
```

## Campaign URL Tagging

### UTM Parameter Strategy

```
UTM TAGGING STRATEGIE
═════════════════════

WANNEER UTM GEBRUIKEN:
──────────────────────
□ Naast auto-tagging (voor GA4 custom reports)
□ Cross-platform tracking (Meta, LinkedIn, etc.)
□ Email campaigns
□ Organic social posts
□ Partner/affiliate links

UTM PARAMETERS:
───────────────
┌───────────────────┬────────────────────────────────────────────┐
│ Parameter         │ Beschrijving                               │
├───────────────────┼────────────────────────────────────────────┤
│ utm_source        │ Platform (google, facebook, newsletter)    │
│ utm_medium        │ Type (cpc, display, email, social)        │
│ utm_campaign      │ Campaign naam                              │
│ utm_term          │ Keyword (auto-filled door Google Ads)     │
│ utm_content       │ Ad variant (voor A/B testing)             │
└───────────────────┴────────────────────────────────────────────┘

GOOGLE ADS UTM TEMPLATE (Account Level):
────────────────────────────────────────
Settings → Account settings → Tracking → Final URL suffix

{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={_campaign}&utm_content={_adgroupname}&utm_term={keyword}

OF met ValueTrack parameters:
{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={creative}&utm_term={keyword}

VALUETRACK PARAMETERS REFERENTIE:
─────────────────────────────────
{campaignid}    - Campaign ID
{campaign}      - Campaign name (gebruik {_campaign} voor custom)
{adgroupid}     - Ad group ID
{creative}      - Ad ID
{keyword}       - Triggered keyword
{device}        - Device (m, t, c)
{matchtype}     - Match type (e, p, b)
{network}       - Network (g=Search, s=Search partner, d=Display)
{placement}     - Display placement URL
{loc_physical}  - Physical location ID
{loc_interest}  - Location of interest ID

NAMING CONVENTIONS:
───────────────────
Campaign names (consistent format):
├── [Platform]_[Type]_[Target]_[Date]
├── Voorbeeld: Google_Search_NL_LeadGen_2025Q1
└── Geen spaties, gebruik underscores

utm_content voor A/B testing:
├── v1, v2, v3
├── headline-a, headline-b
└── image-product, image-lifestyle
```

### Cross-Platform Tracking

```
CROSS-PLATFORM TRACKING MET GA4
═══════════════════════════════

ALLE TRAFFIC NAAR GA4:
──────────────────────

GOOGLE ADS:
├── Auto-tagging: gclid captured
├── Plus UTM: voor custom reports
└── Linked: conversies syncen terug

META ADS:
├── UTM tagging verplicht
├── utm_source=facebook of meta
├── utm_medium=paid_social
└── Optioneel: fbclid parameter capturen

LINKEDIN ADS:
├── UTM tagging verplicht
├── utm_source=linkedin
├── utm_medium=paid_social
└── LinkedIn insight tag voor conversies

MICROSOFT ADS:
├── Auto-tagging mogelijk (msclkid)
├── Plus UTM: voor GA4
└── Link: Microsoft Ads ↔ GA4 ook mogelijk

EMAIL:
├── utm_source=newsletter of [email_name]
├── utm_medium=email
├── utm_campaign=[campaign_name]
└── utm_content=[variant]

UNIFIED REPORTING IN GA4:
─────────────────────────
1. Reports → Acquisition → Traffic acquisition
2. Dimension: Session source/medium
3. Filter: Medium = cpc, paid_social, email

CREATE CROSS-PLATFORM REPORT:
─────────────────────────────
1. Explore → Free form
2. Rows: Session source, Session medium
3. Values: Sessions, Conversions, Revenue
4. Filter: Paid channels only

ATTRIBUTION COMPARISON:
───────────────────────
1. Advertising → Attribution paths
2. Compare: First click vs Last click vs Data-driven
3. See: Hoe kanalen samenwerken
```

## GA4 Reports voor Google Ads

### Custom Reports Setup

```
GA4 REPORTS VOOR GOOGLE ADS PERFORMANCE
═══════════════════════════════════════

REPORT 1: GOOGLE ADS CAMPAIGN PERFORMANCE
─────────────────────────────────────────
Location: Reports → Acquisition → Google Ads campaigns

Metrics available:
├── Sessions
├── Engaged sessions
├── Users
├── Conversions
├── Revenue
└── Engagement rate

Customize:
1. Click "Customize report" (pencil icon)
2. Add metrics: Avg engagement time, Bounce rate
3. Add dimensions: Landing page, Device category

REPORT 2: GOOGLE ADS KEYWORDS
─────────────────────────────
Location: Reports → Acquisition → Google Ads keywords

Shows: Search query data (with keyword matching)

REPORT 3: CUSTOM EXPLORATION - FUNNEL
─────────────────────────────────────
1. Explore → Funnel exploration
2. Steps:
   ├── Step 1: session_start (from: google/cpc)
   ├── Step 2: product_view OR page_view
   ├── Step 3: add_to_cart
   └── Step 4: purchase
3. Segment: Google Ads campaigns

REPORT 4: CUSTOM EXPLORATION - PATH
───────────────────────────────────
1. Explore → Path exploration
2. Starting point: google/cpc session
3. See: User journey after ad click
4. Identify: Drop-off points, key pages

REPORT 5: LANDING PAGE PERFORMANCE
──────────────────────────────────
1. Reports → Engagement → Pages and screens
2. Filter: Session source = google
3. Metrics: Engagement rate, Conversions
4. Identify: Best/worst performing landing pages
```

### Linking Google Ads Cost Data

```
COST DATA IN GA4
════════════════

WAT IS AUTOMATISCH BESCHIKBAAR:
───────────────────────────────
Na linking, GA4 toont:
├── Google Ads clicks
├── Google Ads impressions
├── Google Ads cost
└── Google Ads conversions (bijv. clicks to GA4 conversions)

WAAR TE VINDEN:
───────────────
1. Reports → Acquisition → Acquisition overview
2. Card: "Google Ads campaigns"
3. Metrics: Cost, Clicks, Impressions

COST DATA IMPORT VOOR ANDERE PLATFORMS:
───────────────────────────────────────
GA4 ondersteunt ook cost data import voor:
├── Meta Ads
├── Microsoft Ads
├── Display & Video 360
└── Search Ads 360

Setup:
1. Admin → Data import
2. "+ Create data source"
3. "Cost data"
4. Upload CSV of connect API

CSV FORMAT:
───────────
date,utm_source,utm_medium,utm_campaign,impressions,clicks,cost
2025-01-15,facebook,paid_social,spring_sale,10000,250,125.00

CALCULATED METRICS:
───────────────────
Na cost import kun je berekenen:
├── CPA = Cost / Conversions
├── ROAS = Revenue / Cost
└── CPM = (Cost / Impressions) * 1000
```

## Google Ads Script: GA4 Sync Checker

```javascript
/**
 * GA4 Integration Health Checker
 *
 * Controleert:
 * - Linked accounts status
 * - Imported conversions
 * - Audience sync status
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Schedule: Wekelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Expected GA4 conversions (names)
  EXPECTED_GA4_CONVERSIONS: [
    'generate_lead',
    'purchase',
    'sign_up'
  ],

  // Minimum audience size
  MIN_AUDIENCE_SIZE: 1000
};

function main() {
  var report = {
    conversions: [],
    audiences: [],
    issues: []
  };

  // Check conversion actions
  Logger.log('Checking conversion actions...');

  var conversions = AdsApp.conversions().get();

  while (conversions.hasNext()) {
    var conversion = conversions.next();
    var name = conversion.getName();
    var source = getConversionSource(name);

    report.conversions.push({
      name: name,
      source: source,
      status: conversion.isEnabled() ? 'Enabled' : 'Disabled',
      category: conversion.getCategory()
    });

    // Check voor expected GA4 conversions
    if (source === 'GA4' || source === 'Analytics') {
      Logger.log('Found GA4 conversion: ' + name);
    }
  }

  // Check voor missing expected conversions
  for (var i = 0; i < CONFIG.EXPECTED_GA4_CONVERSIONS.length; i++) {
    var expected = CONFIG.EXPECTED_GA4_CONVERSIONS[i];
    var found = report.conversions.some(function(c) {
      return c.name.toLowerCase().indexOf(expected.toLowerCase()) !== -1;
    });

    if (!found) {
      report.issues.push({
        type: 'MISSING_CONVERSION',
        message: 'Expected GA4 conversion not found: ' + expected
      });
    }
  }

  // Check audiences
  Logger.log('Checking audiences...');

  var audienceIterator = AdsApp.userlists().get();

  while (audienceIterator.hasNext()) {
    var audience = audienceIterator.next();
    var name = audience.getName();
    var size = audience.getSizeForSearch();

    // GA4 audiences often have "GA4" or property name in name
    if (name.indexOf('GA4') !== -1 ||
        name.indexOf('Analytics') !== -1 ||
        name.indexOf('All visitors') !== -1) {

      report.audiences.push({
        name: name,
        size: size,
        status: size >= CONFIG.MIN_AUDIENCE_SIZE ? 'OK' : 'Small'
      });

      if (size < CONFIG.MIN_AUDIENCE_SIZE) {
        report.issues.push({
          type: 'SMALL_AUDIENCE',
          message: 'Audience too small for targeting: ' + name + ' (' + size + ')'
        });
      }
    }
  }

  // Generate report
  generateReport(report);
}

function getConversionSource(name) {
  if (name.indexOf('GA4') !== -1 ||
      name.indexOf('Analytics') !== -1) {
    return 'GA4';
  } else if (name.indexOf('firebase') !== -1) {
    return 'Firebase';
  } else {
    return 'Google Ads';
  }
}

function generateReport(report) {
  Logger.log('');
  Logger.log('=== GA4 INTEGRATION REPORT ===');
  Logger.log('');

  Logger.log('CONVERSIONS:');
  Logger.log('───────────');
  for (var i = 0; i < report.conversions.length; i++) {
    var c = report.conversions[i];
    Logger.log(c.name + ' [' + c.source + '] - ' + c.status);
  }

  Logger.log('');
  Logger.log('GA4 AUDIENCES:');
  Logger.log('──────────────');
  for (var j = 0; j < report.audiences.length; j++) {
    var a = report.audiences[j];
    Logger.log(a.name + ' - Size: ' + a.size + ' - ' + a.status);
  }

  if (report.issues.length > 0) {
    Logger.log('');
    Logger.log('ISSUES:');
    Logger.log('───────');
    for (var k = 0; k < report.issues.length; k++) {
      var issue = report.issues[k];
      Logger.log('[' + issue.type + '] ' + issue.message);
    }

    // Send email alert
    sendAlertEmail(report);
  } else {
    Logger.log('');
    Logger.log('✓ No issues found');
  }
}

function sendAlertEmail(report) {
  var subject = 'GA4 Integration Issues - ' + AdsApp.currentAccount().getName();
  var body = 'GA4 Integration Check Results\n';
  body += '=============================\n\n';

  body += 'ISSUES FOUND:\n';
  for (var i = 0; i < report.issues.length; i++) {
    var issue = report.issues[i];
    body += '• [' + issue.type + '] ' + issue.message + '\n';
  }

  body += '\nACTIONS:\n';
  body += '• Missing conversions: Import from GA4 in Google Ads\n';
  body += '• Small audiences: Wait for list growth or expand criteria\n';

  body += '\n---\nGenerated by GA4 Integration Checker';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
  Logger.log('Alert email sent');
}
```

## Output: GA4 Integration Checklist

```markdown
# GA4 Integration Implementation Checklist

## Account Information
- **Google Ads Account ID:** [ID]
- **GA4 Property ID:** [ID]
- **Website:** [URL]

## Phase 1: Basic Linking
- [ ] Admin access to both GA4 and Google Ads
- [ ] Accounts linked (GA4 → Google Ads links)
- [ ] Auto-tagging enabled in Google Ads
- [ ] Verify link shows "Active" in both platforms

## Phase 2: Conversion Import
- [ ] Key events marked as conversions in GA4
- [ ] Conversions imported to Google Ads
- [ ] Conversion counting configured (One/Every)
- [ ] Attribution model set to Data-driven
- [ ] Primary/Secondary status set correctly
- [ ] Test conversion tracked successfully

### Conversions to Import:
| GA4 Event | Google Ads Name | Goal Category | Count |
|-----------|-----------------|---------------|-------|
| [event]   | [name]          | [category]    | One   |

## Phase 3: Audience Setup
- [ ] Remarketing audiences created in GA4
- [ ] Audiences enabled for Google Ads export
- [ ] Audiences visible in Google Ads Audience Manager
- [ ] Audience size meets minimums (1000+ for Search)

### Audiences to Create:
| Audience Name | Definition | Expected Size |
|---------------|------------|---------------|
| All Visitors 30d | All users, 30 days | [size] |
| Converters | purchase event | [size] |
| Cart Abandoners | add_to_cart excl purchase | [size] |

## Phase 4: UTM Strategy
- [ ] UTM template set at account level
- [ ] ValueTrack parameters configured
- [ ] Naming conventions documented
- [ ] Test URLs verified

## Phase 5: Reporting Setup
- [ ] Google Ads campaign report customized
- [ ] Landing page performance exploration created
- [ ] Funnel exploration for ad traffic created
- [ ] Cost data displaying correctly

## Validation Checklist
- [ ] Conversions match within 15% between platforms
- [ ] Audiences populating as expected
- [ ] No "unassigned" traffic from Google Ads
- [ ] Attribution model consistent

## Troubleshooting Reference
- Conversion discrepancy >20%: Check attribution models
- Audience not syncing: Verify personalized advertising enabled
- Missing Google Ads data: Check linking status
```

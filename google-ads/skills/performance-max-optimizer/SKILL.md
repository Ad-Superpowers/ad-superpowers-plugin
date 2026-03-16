---
name: performance-max-optimizer
description: "Performance Max campaign optimalisatie voor Google Ads. Gebruik voor: (1) PMax setup en architectuur, (2) Asset groups strategie, (3) Audience signals configuratie, (4) Search themes toevoegen, (5) E-commerce vs Lead Gen PMax setup, (6) Channel performance analyse. Triggers: performance max, pmax, asset groups, audience signals, shopping, search themes, retail."
---

# Performance Max Optimizer

Complete gids voor het opzetten, optimaliseren en schalen van Google Ads Performance Max campagnes voor e-commerce en lead generation.

## Quick Decision Guide

```
WELK TYPE PMAX HEB JE NODIG?
│
├─► E-commerce met product feed
│   └─► SHOPPING-FOCUSED PMAX
│       ├── Merchant Center feed vereist
│       ├── Listing groups voor product targeting
│       └── Asset groups per productcategorie
│
├─► E-commerce zonder feed / DTC
│   └─► STANDARD PMAX
│       ├── URL-based targeting
│       ├── Asset groups per productlijn
│       └── Final URL expansion: aan
│
├─► Lead Generation (B2B/Services)
│   └─► LEAD GEN PMAX
│       ├── Form submissions of calls
│       ├── Lead form assets
│       └── Final URL expansion: uit (of beperkt)
│
└─► Brand Awareness / Consideration
    └─► NIET PMAX - Gebruik Demand Gen of Video
```

## Performance Max Architectuur

### Hoe PMax Werkt

```
┌─────────────────────────────────────────────────────────────────┐
│  PERFORMANCE MAX CAMPAIGN                                        │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  GOOGLE AI ENGINE                                          │ │
│  │  ├── Real-time bidding optimization                        │ │
│  │  ├── Audience discovery & expansion                        │ │
│  │  ├── Creative assembly & testing                           │ │
│  │  └── Cross-channel budget allocation                       │ │
│  └────────────────────────────────────────────────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  CHANNELS (Automatic Distribution)                         │ │
│  │  ├── Search (incl. Shopping)                               │ │
│  │  ├── YouTube                                               │ │
│  │  ├── Display Network                                       │ │
│  │  ├── Discover                                              │ │
│  │  ├── Gmail                                                 │ │
│  │  └── Maps (local campaigns)                                │ │
│  └────────────────────────────────────────────────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  INPUTS (Jouw Control)                                     │ │
│  │  ├── Assets (images, videos, headlines, descriptions)      │ │
│  │  ├── Audience Signals (hints, geen targeting)              │ │
│  │  ├── Search Themes (nieuwe feature 2024+)                  │ │
│  │  ├── Goals (conversions, value)                            │ │
│  │  └── Budget & Bid Strategy                                 │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## E-commerce PMax Setup

### Stap 1: Merchant Center Verificatie

```
MERCHANT CENTER CHECKLIST
=========================

□ Feed Status
├── Alle producten approved?
├── Geen disapprovals of warnings?
├── Product data kwaliteit >90%?
└── Feed refresh frequentie: minimaal dagelijks

□ Product Data Kwaliteit
├── Titles: Keyword-first, max 150 chars
├── Descriptions: Unieke, keyword-rich content
├── Images: Hoge kwaliteit, witte achtergrond
├── GTIN/MPN: Correct ingevuld
├── Price: Up-to-date, inclusief sale prices
└── Availability: Real-time sync met voorraad

□ Free Listings
├── Free listings actief?
├── Surfaces across Google enabled?
└── Enhanced listings attributen ingevuld?
```

### Stap 2: Campaign Structuur

```
AANBEVOLEN PMAX STRUCTUUR (E-commerce)
======================================

Optie A: Product Category Based (Aanbevolen voor 50+ producten)
───────────────────────────────────────────────────────────────
Campaign: PMax - All Products
├── Asset Group 1: Bestsellers
│   ├── Listing Group: Top 20 products
│   ├── Audience Signal: Past purchasers
│   └── Search Themes: [brand] + [top categories]
│
├── Asset Group 2: Category A (bijv. Kleding)
│   ├── Listing Group: Category = Kleding
│   ├── Audience Signal: Fashion interests
│   └── Search Themes: [kleding keywords]
│
├── Asset Group 3: Category B (bijv. Schoenen)
│   ├── Listing Group: Category = Schoenen
│   ├── Audience Signal: Shoe shoppers
│   └── Search Themes: [schoenen keywords]
│
└── Asset Group 4: Sale Items
    ├── Listing Group: Custom Label = Sale
    ├── Audience Signal: Deal seekers
    └── Search Themes: [category] sale, korting

Optie B: Margin/Performance Based (Aanbevolen voor winstoptimalisatie)
──────────────────────────────────────────────────────────────────────
Campaign 1: PMax - High Margin Products (Custom Label 0 = High Margin)
├── Bid Strategy: Target ROAS (hogere target)
└── Budget: 60% van totaal

Campaign 2: PMax - Standard Margin Products
├── Bid Strategy: Target ROAS (standaard target)
└── Budget: 30% van totaal

Campaign 3: PMax - Low Margin/Clearance
├── Bid Strategy: Maximize Conversion Value
└── Budget: 10% van totaal
```

### Stap 3: Asset Group Setup

```
ASSET REQUIREMENTS (2025/2026)
==============================

HEADLINES (Vereist: 3-5, Aanbevolen: 5-15)
├── 30 karakters max per headline
├── Mix van:
│   ├── Brand headlines: "[Brand] Official Store"
│   ├── Benefit headlines: "Free Shipping Above €50"
│   ├── USP headlines: "Handmade in Netherlands"
│   ├── Action headlines: "Shop Now - 30% Off"
│   └── Category headlines: "Premium [Category]"
└── Geen duplicate headlines

LONG HEADLINES (Vereist: 1-5)
├── 90 karakters max
├── Meer descriptief, storytelling
└── Inclusief CTA

DESCRIPTIONS (Vereist: 2-5, Aanbevolen: 4-5)
├── 90 karakters max
├── Eerste description: Core value prop
├── Varieer met benefits, features, social proof
└── Geen herhaling van headlines

IMAGES (Vereist: 3+)
├── Landscape (1.91:1): 1200x628 min, vereist
├── Square (1:1): 1200x1200 min, vereist
├── Portrait (4:5): 960x1200 min, aanbevolen
├── Mix van product shots en lifestyle
└── Logo: 1200x1200 (square) + 1200x300 (landscape)

VIDEOS (Aanbevolen, niet vereist)
├── Landscape: 16:9
├── Square: 1:1
├── Portrait: 9:16 (voor YouTube Shorts/Reels)
├── Minimum 10 seconden
└── Google kan auto-generate videos uit images
```

## Audience Signals

### Belangrijke Nuance: Signals ≠ Targeting

```
⚠️  CRUCIAAL BEGRIP
===================

Audience Signals = HINTS voor Google AI
Audience Signals ≠ Targeting restricties

Google ZAL buiten je signals adverteren als het
betere resultaten verwacht. Signals versnellen
de learning phase en geven richting.

Goede Signals → Snellere optimalisatie
Slechte Signals → Langzamere learning, maar geen ramp
```

### Audience Signal Strategie

```
AUDIENCE SIGNAL LAYERING
========================

LAAG 1: First-Party Data (Hoogste waarde)
─────────────────────────────────────────
□ Customer Match
├── All Customers (conversions)
├── High-Value Customers (top 20% LTV)
├── Recent Buyers (30 dagen)
└── Lapsed Customers (180+ dagen)

□ Website Visitors
├── All visitors (180 dagen)
├── Product viewers (90 dagen)
├── Cart abandoners (30 dagen)
└── Converters (exclude of include)

LAAG 2: Google Audiences
────────────────────────
□ In-Market Segments
├── Selecteer 3-5 meest relevante
├── Basis: Echte koopintentie
└── Voorbeeld: "Apparel & Accessories Shoppers"

□ Affinity Segments
├── Breder, meer volume
├── Voorbeeld: "Fashionistas", "Bargain Hunters"
└── Minder specifiek, meer reach

□ Life Events
├── Zeer krachtig voor specifieke momenten
├── Voorbeeld: "Recently Moved", "Getting Married"
└── Kleinere audiences, hoge intent

LAAG 3: Custom Segments
───────────────────────
□ Search Term Based
├── Mensen die specifieke termen zochten
├── Competitor namen
└── Product-specifieke queries

□ Website Based
├── Bezoekers van competitor sites
├── Review sites
└── Industry publications
```

## Search Themes (2024+ Feature)

### Wat Zijn Search Themes?

```
SEARCH THEMES UITLEG
====================

Search Themes = Keywords die je aan PMax geeft
om te helpen begrijpen welke zoekopdrachten relevant zijn.

VERSCHIL MET SEARCH CAMPAIGNS:
├── Search Campaign Keywords: Exacte match/phrase targeting
└── PMax Search Themes: Hints voor AI, geen garantie

WANNEER GEBRUIKEN:
├── Nieuwe PMax campaigns (versnelt learning)
├── Specifieke product niches
├── Wanneer je Search ook draait (alignment)
└── Branded terms beschermen
```

### Search Themes Best Practices

```
SEARCH THEMES SETUP
===================

AANBEVELINGEN PER ASSET GROUP:
├── Aantal: 3-7 themes per asset group
├── Type: Mix van broad en specific
└── Geen negative keywords mogelijk in PMax

VOORBEELD (Fashion E-commerce):
Asset Group: Winterjassen
├── Theme 1: "winterjas dames"
├── Theme 2: "warme jas kopen"
├── Theme 3: "[brand] winterjassen"
├── Theme 4: "parka dames"
└── Theme 5: "winterjas sale"

VOORBEELD (B2B Software):
Asset Group: CRM Software
├── Theme 1: "crm software"
├── Theme 2: "klantenbeheer systeem"
├── Theme 3: "sales pipeline tool"
└── Theme 4: "[brand] crm"

TIPS:
├── Gebruik keyword research data
├── Include branded terms
├── Check Search Terms report voor ideeën
└── Update maandelijks op basis van performance
```

## Lead Generation PMax

### Lead Gen Specifieke Setup

```
LEAD GEN PMAX CONFIGURATIE
==========================

CONVERSION SETUP
├── Primary: Qualified Lead of SQL
├── Secondary: Form Submit (MQL)
├── Offline Imports: Lead → Opportunity → Won
└── Enhanced Conversions: VERPLICHT voor lead gen

FINAL URL EXPANSION
├── Aan: Meer volume, minder controle
├── Uit: Strikte controle, minder volume
├── Aanbeveling: Start UIT, test AAN later
└── Exclude URLs: Privacy policy, careers, etc.

ASSET GROUP STRUCTUUR (Lead Gen):
─────────────────────────────────
Campaign: PMax - Lead Gen
├── Asset Group 1: Main Service
│   ├── Final URL: /diensten/
│   ├── Lead Form: Full form
│   └── Search Themes: service keywords
│
├── Asset Group 2: Free Consultation
│   ├── Final URL: /gratis-adviesgesprek/
│   ├── Lead Form: Quick form
│   └── Search Themes: consultation keywords
│
└── Asset Group 3: Download/Whitepaper
    ├── Final URL: /resources/
    ├── Lead Form: Email only
    └── Search Themes: informational queries
```

### Lead Quality Optimization

```
LEAD KWALITEIT VERBETEREN
=========================

1. OFFLINE CONVERSION IMPORT
   ├── Importeer lead → sale conversies
   ├── Minimaal wekelijks uploaden
   ├── Google optimaliseert op echte waarde
   └── Setup via Google Ads API of manual upload

2. VALUE-BASED BIDDING
   ├── Ken waarde toe aan leads
   ├── SQL = €500, MQL = €50
   ├── Closed Won = €5000
   └── PMax optimaliseert op waarde

3. FORM OPTIMALISATIE
   ├── Meer velden = hogere kwaliteit, minder volume
   ├── Qualification vragen toevoegen
   ├── Business email required
   └── Phone number required

4. NEGATIVE AUDIENCES (indirect)
   ├── Exclude bestaande klanten
   ├── Exclude competitors (via Customer Match)
   └── Exclude employees
```

## Channel Performance Analyse

### Insights Reporting (2025+)

```
PMAX CHANNEL BREAKDOWN
======================

Locatie: Campaign → Insights → Asset Performance

BESCHIKBARE METRICS PER CHANNEL:
├── Search (incl. Shopping)
├── YouTube
├── Display
├── Discover
├── Gmail
└── Maps (als lokaal actief)

WAT TE ANALYSEREN:
├── Welk kanaal levert meeste conversies?
├── ROAS per kanaal (indien zichtbaar)
├── Video views en engagement (YouTube)
├── Impression share (Search/Shopping)
└── Top converting asset combinations
```

### Asset Performance Optimalisatie

```
ASSET PERFORMANCE RATINGS
=========================

RATINGS SYSTEEM:
├── Best: Hoogste performance, keep running
├── Good: Solide performance, monitor
├── Low: Underperformend, vervang na 30 dagen
└── Pending: Nog niet genoeg data

OPTIMALISATIE WORKFLOW:
───────────────────────
Week 1-2: Learning phase, geen changes
Week 3-4: Check asset ratings
├── Remove: Assets met "Low" rating >30 dagen
├── Add: Nieuwe variaties van "Best" assets
└── Test: Nieuwe concepten

Maandelijks:
├── Refresh 20% van assets
├── Nieuwe headlines testen
├── Seizoensgebonden updates
└── Performance trends analyseren
```

## Bid Strategies voor PMax

### Strategie Selectie

```
PMAX BID STRATEGY DECISION TREE
===============================

NIEUW ACCOUNT / CAMPAIGN?
│
├─► Ja, <30 conversies/maand verwacht
│   └─► MAXIMIZE CONVERSIONS
│       (geen target, verzamel data)
│
├─► Ja, 30+ conversies/maand verwacht
│   └─► MAXIMIZE CONVERSIONS + optional tCPA
│       (start 20% boven expected CPA)
│
├─► Nee, e-commerce met waarde
│   └─► MAXIMIZE CONVERSION VALUE + tROAS
│       ├── Start: 80% van break-even ROAS
│       └── Tighten: 10% per 2 weken
│
└─► Nee, lead gen
    └─► MAXIMIZE CONVERSIONS + tCPA
        ├── Start: 120% van target CPA
        └── Tighten: 10% per 2 weken
```

### Budget Recommendations

```
MINIMUM BUDGET RICHTLIJNEN
==========================

E-commerce:
├── Minimum: €50/dag (absolute minimum)
├── Aanbevolen: €100-200/dag
├── Optimal: 10x target CPA per dag
└── Scaling: Max 20% increase per week

Lead Gen:
├── Minimum: €30/dag
├── Aanbevolen: €50-100/dag
├── Optimal: 5x target CPA per dag
└── Scaling: Max 15% increase per week

LEARNING PHASE:
├── Duur: 1-2 weken typisch
├── Requirement: ~50 conversies
├── Tip: Hoger budget = snellere learning
└── Geen grote changes tijdens learning
```

## Troubleshooting

### Veel Voorkomende Issues

```
PMAX TROUBLESHOOTING GUIDE
==========================

ISSUE: Lage of geen delivery
────────────────────────────
□ Check: Budget te laag?
□ Check: Bid targets te agressief?
□ Check: Asset group status (eligible?)
□ Check: Merchant Center disapprovals?
□ Fix: Verhoog budget 20%
□ Fix: Verlaag tROAS/tCPA target 15%
□ Fix: Voeg meer assets toe

ISSUE: Hoge CPA / Lage ROAS
───────────────────────────
□ Check: Conversion tracking correct?
□ Check: Learning phase nog actief?
□ Check: Asset performance (veel "Low"?)
□ Check: Audience signals relevant?
□ Fix: Wacht tot learning phase klaar
□ Fix: Upgrade assets met "Low" rating
□ Fix: Tighten bid targets geleidelijk

ISSUE: Slechte lead kwaliteit (Lead Gen)
────────────────────────────────────────
□ Check: Welke conversie actie is primary?
□ Check: Enhanced Conversions actief?
□ Check: Offline conversion imports?
□ Fix: Switch naar qualified lead als primary
□ Fix: Implementeer offline conversion import
□ Fix: Voeg form qualification vragen toe

ISSUE: PMax "steelt" van Search
───────────────────────────────
□ Dit is normaal gedrag
□ PMax en Search kunnen coexisteren
□ Brand keywords: Voeg als Search Themes toe
□ Optie: Brand exclusions in PMax
□ Monitor: Incrementality, niet kannibalisatie
```

## Google Ads Script: PMax Performance Monitor

```javascript
/**
 * Performance Max Campaign Monitor
 *
 * Dit script monitort PMax campagnes en stuurt alerts
 * bij significante performance changes.
 *
 * Setup:
 * 1. Pas SETTINGS aan naar je wensen
 * 2. Schedule: Dagelijks om 9:00
 */

// === SETTINGS ===
var SETTINGS = {
  // Email voor alerts
  EMAIL: 'jouw@email.com',

  // Performance thresholds
  CPA_INCREASE_THRESHOLD: 0.25,    // Alert bij 25% CPA stijging
  ROAS_DECREASE_THRESHOLD: 0.20,   // Alert bij 20% ROAS daling
  SPEND_CHANGE_THRESHOLD: 0.30,    // Alert bij 30% spend change

  // Vergelijkingsperiode
  COMPARE_DAYS: 7,  // Vergelijk laatste 7 dagen met vorige 7 dagen

  // Minimum spend voor analyse
  MIN_SPEND: 100
};

function main() {
  var pMaxCampaigns = AdsApp.performanceMaxCampaigns()
    .withCondition('Status = ENABLED')
    .get();

  var alerts = [];

  while (pMaxCampaigns.hasNext()) {
    var campaign = pMaxCampaigns.next();
    var campaignAlerts = analyzeCampaign(campaign);
    alerts = alerts.concat(campaignAlerts);
  }

  if (alerts.length > 0) {
    sendAlertEmail(alerts);
  }

  Logger.log('PMax Monitor completed. Alerts: ' + alerts.length);
}

function analyzeCampaign(campaign) {
  var alerts = [];
  var campaignName = campaign.getName();

  // Huidige periode
  var currentStats = campaign.getStatsFor('LAST_' + SETTINGS.COMPARE_DAYS + '_DAYS');

  // Vorige periode (handmatig berekenen)
  var today = new Date();
  var previousEnd = new Date(today.getTime() - (SETTINGS.COMPARE_DAYS * 24 * 60 * 60 * 1000));
  var previousStart = new Date(previousEnd.getTime() - (SETTINGS.COMPARE_DAYS * 24 * 60 * 60 * 1000));

  var previousStats = campaign.getStatsFor(
    formatDate(previousStart),
    formatDate(previousEnd)
  );

  // Check minimum spend
  if (currentStats.getCost() < SETTINGS.MIN_SPEND) {
    return alerts;
  }

  // CPA Analysis
  var currentCPA = calculateCPA(currentStats);
  var previousCPA = calculateCPA(previousStats);

  if (previousCPA > 0 && currentCPA > 0) {
    var cpaChange = (currentCPA - previousCPA) / previousCPA;
    if (cpaChange > SETTINGS.CPA_INCREASE_THRESHOLD) {
      alerts.push({
        campaign: campaignName,
        metric: 'CPA',
        current: currentCPA.toFixed(2),
        previous: previousCPA.toFixed(2),
        change: (cpaChange * 100).toFixed(1) + '%',
        severity: cpaChange > 0.5 ? 'HIGH' : 'MEDIUM'
      });
    }
  }

  // ROAS Analysis
  var currentROAS = calculateROAS(currentStats);
  var previousROAS = calculateROAS(previousStats);

  if (previousROAS > 0 && currentROAS > 0) {
    var roasChange = (currentROAS - previousROAS) / previousROAS;
    if (roasChange < -SETTINGS.ROAS_DECREASE_THRESHOLD) {
      alerts.push({
        campaign: campaignName,
        metric: 'ROAS',
        current: currentROAS.toFixed(2),
        previous: previousROAS.toFixed(2),
        change: (roasChange * 100).toFixed(1) + '%',
        severity: roasChange < -0.4 ? 'HIGH' : 'MEDIUM'
      });
    }
  }

  // Spend Analysis
  var currentSpend = currentStats.getCost();
  var previousSpend = previousStats.getCost();

  if (previousSpend > 0) {
    var spendChange = (currentSpend - previousSpend) / previousSpend;
    if (Math.abs(spendChange) > SETTINGS.SPEND_CHANGE_THRESHOLD) {
      alerts.push({
        campaign: campaignName,
        metric: 'Spend',
        current: '€' + currentSpend.toFixed(2),
        previous: '€' + previousSpend.toFixed(2),
        change: (spendChange * 100).toFixed(1) + '%',
        severity: 'LOW'
      });
    }
  }

  return alerts;
}

function calculateCPA(stats) {
  var conversions = stats.getConversions();
  var cost = stats.getCost();
  return conversions > 0 ? cost / conversions : 0;
}

function calculateROAS(stats) {
  var conversionValue = stats.getConversionValue();
  var cost = stats.getCost();
  return cost > 0 ? conversionValue / cost : 0;
}

function formatDate(date) {
  return Utilities.formatDate(date, AdsApp.currentAccount().getTimeZone(), 'yyyyMMdd');
}

function sendAlertEmail(alerts) {
  var subject = '⚠️ PMax Performance Alert - ' + AdsApp.currentAccount().getName();

  var body = 'Performance Max Campaign Alerts\n';
  body += '================================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Date: ' + new Date().toDateString() + '\n\n';

  for (var i = 0; i < alerts.length; i++) {
    var alert = alerts[i];
    body += '[' + alert.severity + '] ' + alert.campaign + '\n';
    body += '  ' + alert.metric + ': ' + alert.previous + ' → ' + alert.current;
    body += ' (' + alert.change + ')\n\n';
  }

  body += '\n---\nGenerated by PMax Performance Monitor Script';

  MailApp.sendEmail(SETTINGS.EMAIL, subject, body);
}
```

## PMax vs Search: Coexistentie Strategie

```
PMAX + SEARCH SAMENWERKING
==========================

GOOGLE'S PRIORITERING:
├── Exact match Search keyword → Search wint
├── Phrase/Broad match → Kan beide zijn
├── Geen keyword match → PMax wint
└── Shopping queries → PMax Shopping wint

AANBEVOLEN SETUP:
─────────────────
1. Search Campaign: Brand + Top non-brand exact match
2. PMax: Alles overige (laat AI optimaliseren)
3. Monitor: Search Terms report in beide

BRAND BESCHERMING:
├── Optie 1: Brand keywords in Search (exact)
├── Optie 2: Brand exclusions in PMax
├── Optie 3: Beide (maximale controle)
└── Check: Search Themes voor brand alignment

INCREMENTALITY METEN:
├── Run: 2 weken met beide aan
├── Pause: PMax voor 2 weken
├── Compare: Total conversions + CPA
└── Besluit: Op basis van incremental lift
```

## Output: PMax Setup Checklist

```markdown
# Performance Max Setup Checklist

## Pre-Launch
□ Conversion tracking verified (test conversions)
□ Merchant Center feed approved (e-commerce)
□ Enhanced Conversions enabled
□ Minimum budget allocated (€50+/dag)

## Campaign Setup
□ Campaign type: Performance Max
□ Goal: Sales / Leads (correct geselecteerd)
□ Bid strategy: [Maximize Conversions / tROAS / tCPA]
□ Target: [X] (indien van toepassing)
□ Budget: €[X]/dag

## Asset Groups
□ Asset Group 1: [Name]
  □ Final URL: [URL]
  □ Headlines: 5-15 stuks
  □ Long headlines: 1-5 stuks
  □ Descriptions: 4-5 stuks
  □ Images: Landscape + Square + Portrait
  □ Logo: Square + Landscape
  □ Video: Optional maar aanbevolen
  □ Audience Signals: Configured
  □ Search Themes: 3-7 stuks

## Listing Groups (E-commerce)
□ Product selection correct
□ Custom labels gebruikt voor segmentatie
□ Exclusions ingesteld (out of stock, low margin)

## Final Checks
□ Final URL expansion: [Aan/Uit]
□ Brand exclusions: [Ja/Nee, welke]
□ URL exclusions configured
□ Schedule: 24/7 of custom

## Post-Launch Monitoring
□ Day 1: Verify delivery
□ Day 3: Check asset eligibility
□ Week 1: Monitor learning phase
□ Week 2: First asset performance check
□ Week 4: Full optimization review
```

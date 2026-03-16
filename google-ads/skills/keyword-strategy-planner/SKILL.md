---
name: keyword-strategy-planner
description: "Google Ads keyword strategie en match type planner. Gebruik voor: (1) Match type selectie (Broad, Phrase, Exact), (2) Negative keyword strategie, (3) Search Terms analyse, (4) Keyword clustering en structuur, (5) Query sculpting, (6) SKAGs vs moderne structuur. Triggers: keywords, match types, negatives, search terms, broad match, phrase match, exact match, keyword research, query sculpting."
---

# Keyword Strategy Planner

Complete gids voor het opzetten van een effectieve Google Ads keyword strategie met match types, negatives en search terms analyse.

## Quick Decision Guide

```
WELKE MATCH TYPE STRATEGIE PAST BIJ JOU?
│
├─► NIEUW ACCOUNT / WEINIG DATA
│   └─► BROAD MATCH + SMART BIDDING
│       ├── Maximale reach
│       ├── Laat AI queries ontdekken
│       └── Strict negative management
│
├─► BEWEZEN KEYWORDS / HOGE VOLUME
│   └─► PHRASE MATCH (Core)
│       ├── Balans tussen reach en control
│       ├── Intent behouden
│       └── Voorspelbare performance
│
├─► BRAND / HIGH-VALUE KEYWORDS
│   └─► EXACT MATCH
│       ├── Maximale controle
│       ├── Premium bidding
│       └── Quality traffic
│
└─► MODERNE BEST PRACTICE (2025+)
    └─► HYBRID APPROACH
        ├── Broad Match + Smart Bidding (discovery)
        ├── Phrase Match (core volume)
        ├── Exact Match (top performers)
        └── Aggressive negatives
```

## Match Types Vergelijking

### 2025 Match Type Behavior

```
MATCH TYPE EVOLUTION (2025)
═══════════════════════════

┌─────────────┬────────────────────────────────────────────────────┐
│ MATCH TYPE  │ MATCHING BEHAVIOR                                  │
├─────────────┼────────────────────────────────────────────────────┤
│ BROAD       │ Synoniem, gerelateerd, intent-based               │
│ [keyword]   │ "hardloopschoenen" → "running sneakers kopen"     │
│             │ "beste sportschoenen", "nike runners"              │
│             │ ⚠️ ALLEEN effectief met Smart Bidding!            │
├─────────────┼────────────────────────────────────────────────────┤
│ PHRASE      │ Betekenis moet behouden blijven                    │
│ "keyword"   │ "hardloopschoenen" → "goedkope hardloopschoenen"  │
│             │ "hardloopschoenen dames sale"                      │
│             │ ✓ Meest voorspelbaar, intent-focused              │
├─────────────┼────────────────────────────────────────────────────┤
│ EXACT       │ Zelfde betekenis, close variants                   │
│ [keyword]   │ [hardloopschoenen] → "hardloopschoenen"           │
│             │ "hardloop schoenen", "hardloopschoen"              │
│             │ ✓ Maximale controle, premium bids                 │
└─────────────┴────────────────────────────────────────────────────┘

⚠️ BELANGRIJKE VERANDERING 2024+:
   - Broad Match modifier (BMM) bestaat niet meer
   - Phrase Match heeft BMM functionaliteit overgenomen
   - Broad Match is véél breder dan vroeger
   - AI-based matching op intent, niet alleen woorden
```

### Match Type Selection Matrix

```
MATCH TYPE KEUZE MATRIX
═══════════════════════

                    │ Control │ Volume │ CPA Risk │ Best For
────────────────────┼─────────┼────────┼──────────┼───────────────
BROAD MATCH         │ Laag    │ Hoog   │ Hoog     │ Discovery,
                    │         │        │          │ Smart Bidding
────────────────────┼─────────┼────────┼──────────┼───────────────
PHRASE MATCH        │ Medium  │ Medium │ Medium   │ Core keywords,
                    │         │        │          │ Voorspelbaar
────────────────────┼─────────┼────────┼──────────┼───────────────
EXACT MATCH         │ Hoog    │ Laag   │ Laag     │ Top performers,
                    │         │        │          │ Brand keywords
────────────────────┴─────────┴────────┴──────────┴───────────────

BUDGET ALLOCATIE RICHTLIJN:
├── Exact Match: 30-40% (proven keywords)
├── Phrase Match: 40-50% (core volume)
└── Broad Match: 10-30% (discovery/Smart Bidding)
```

## Keyword Structuur Strategieën

### Moderne Account Structuur (2025)

```
AANBEVOLEN KEYWORD STRUCTUUR
════════════════════════════

OUDE METHODE (NIET MEER AANBEVOLEN):
────────────────────────────────────
SKAGs (Single Keyword Ad Groups)
├── Extreme granulariteit
├── Veel maintenance
├── Beperkte data per ad group
└── ❌ Niet compatibel met Smart Bidding

MODERNE METHODE (AANBEVOLEN):
─────────────────────────────
Theme-Based Ad Groups (STAGs)
├── Keywords gegroepeerd op intent/theme
├── 10-20 keywords per ad group
├── Voldoende data voor Smart Bidding
└── ✓ RSA's kunnen optimaliseren

VOORBEELD STRUCTUUR:
────────────────────
Campaign: Running Shoes
│
├── Ad Group: Men's Running Shoes
│   ├── [hardloopschoenen heren] (exact)
│   ├── "hardloopschoenen mannen" (phrase)
│   ├── "running shoes heren" (phrase)
│   ├── hardloopschoenen heren (broad)
│   └── ... (10-15 related keywords)
│
├── Ad Group: Women's Running Shoes
│   ├── [hardloopschoenen dames] (exact)
│   ├── "hardloopschoenen vrouwen" (phrase)
│   └── ... (10-15 related keywords)
│
└── Ad Group: Running Shoes Sale
    ├── [hardloopschoenen sale] (exact)
    ├── "hardloopschoenen korting" (phrase)
    └── ... (10-15 related keywords)
```

### Keyword Clustering Methode

```
KEYWORD CLUSTERING WORKFLOW
═══════════════════════════

STAP 1: Keyword Research
────────────────────────
□ Google Keyword Planner
□ Search Terms Report (bestaande campaigns)
□ Competitor analysis tools
□ Google Autocomplete
□ Related searches

STAP 2: Intent Categorisatie
────────────────────────────
TRANSACTIONAL (Koop-intent)
├── "kopen", "bestellen", "prijs"
├── "online shop", "sale", "korting"
└── Prioriteit: HOOG

COMMERCIAL (Vergelijk-intent)
├── "beste", "review", "vergelijken"
├── "vs", "of", "alternatieven"
└── Prioriteit: MEDIUM-HOOG

INFORMATIONAL (Info-intent)
├── "hoe", "wat is", "waarom"
├── "guide", "tips", "tutorial"
└── Prioriteit: LAAG (meestal excluden)

NAVIGATIONAL (Merk-intent)
├── Brand names, specifieke producten
├── Competitor brands
└── Prioriteit: VARIABEL

STAP 3: Cluster Formatie
────────────────────────
Groepeer keywords met:
├── Zelfde landing page intent
├── Zelfde user journey fase
├── Vergelijkbare CPC range
└── Logical ad copy fit
```

## Negative Keyword Strategie

### Negative Match Types

```
NEGATIVE MATCH TYPES UITLEG
═══════════════════════════

⚠️ NEGATIVES WERKEN ANDERS DAN POSITIEVE KEYWORDS!

NEGATIVE EXACT [keyword]
────────────────────────
Blokkeert ALLEEN die exacte query
├── Negative: [gratis hardloopschoenen]
├── Blokkeert: "gratis hardloopschoenen"
├── Blokkeert NIET: "gratis hardloopschoenen kopen"
└── Gebruik: Zeer specifieke blokkades

NEGATIVE PHRASE "keyword"
─────────────────────────
Blokkeert queries die de phrase bevatten
├── Negative: "gratis"
├── Blokkeert: "gratis hardloopschoenen"
├── Blokkeert: "hardloopschoenen gratis verzending"
├── Blokkeert NIET: "gratuite chaussures" (andere taal)
└── Gebruik: Meest gebruikte negative type

NEGATIVE BROAD keyword
──────────────────────
Blokkeert queries met ALLE woorden (any order)
├── Negative: gratis korting
├── Blokkeert: "korting gratis verzending"
├── Blokkeert: "gratis items met korting"
├── Blokkeert NIET: "gratis verzending" (mist "korting")
└── Gebruik: Voorzichtig, kan te breed blokkeren
```

### Negative Keyword Lijst Structuur

```
NEGATIVE KEYWORD MANAGEMENT
═══════════════════════════

ACCOUNT-LEVEL NEGATIVES (Shared Library)
────────────────────────────────────────
Blokkeer voor ALLE campaigns:

□ Gratis/Free Seekers
├── "gratis", "free", "download"
├── "torrent", "crack", "pirate"
└── Tenzij je freemium aanbiedt

□ Job Seekers
├── "vacature", "baan", "werken bij"
├── "salary", "career", "job"
└── Tenzij je recruitment doet

□ DIY/How-to (vaak low-value)
├── "hoe maak je", "zelf maken"
├── "tutorial", "diy"
└── Evalueer per business

□ Competitor Exclusions (optioneel)
├── Competitor brand names
├── Als je niet wilt bieden op competitors
└── Of juist in aparte campaign

CAMPAIGN-LEVEL NEGATIVES
────────────────────────
Specifiek per campaign type:

E-commerce Campaign Negatives:
├── "tweedehands", "gebruikt", "refurbished"
├── "reparatie", "repareren"
├── Product types die je NIET verkoopt
└── Competitor product names (optioneel)

Lead Gen Campaign Negatives:
├── "gratis consult" (als je betaald aanbiedt)
├── Geografische uitsluiting (andere regio's)
├── Industry verticals die je niet bedient
└── Job-related searches

Brand Campaign Negatives:
├── "[brand] vacatures"
├── "[brand] klachten"
├── "[brand] login" (support, niet sales)
└── "[brand] customer service"
```

### Negative Keyword Discovery

```
NEGATIVE DISCOVERY WORKFLOW
═══════════════════════════

WEKELIJKSE SEARCH TERMS REVIEW:
──────────────────────────────
1. Ga naar: Keywords → Search Terms
2. Filter: Last 7 days
3. Sorteer op: Impressions (hoog naar laag)
4. Analyseer elke term:
   ├── Relevant + Converted → Keep
   ├── Relevant + No Conv → Monitor
   ├── Irrelevant + Spend → NEGATIVE
   └── Irrelevant + No Spend → Negeer of negative

QUICK FILTERS VOOR NEGATIVES:
─────────────────────────────
□ Conversions = 0 AND Clicks > 10
□ Cost > €X AND Conversions = 0
□ CTR < 1% (vaak irrelevant)
□ Avg CPC > €X AND geen conversies

AUTO-NEGATIVE RULES (Script):
────────────────────────────
Automatisch negative toevoegen wanneer:
├── Query heeft 5+ clicks, 0 conversies
├── Query CPA > 3x campaign average
├── Query bevat known negative terms
└── Query CTR < 0.5%
```

## Search Terms Analyse

### Search Terms Report Optimalisatie

```
SEARCH TERMS ANALYSE FRAMEWORK
══════════════════════════════

STAP 1: DATA EXPORT
───────────────────
1. Keywords → Search Terms
2. Date range: Last 30-90 days
3. Download als CSV/Excel
4. Include: All columns

STAP 2: CATEGORISATIE
─────────────────────
Maak kolommen voor:
├── Category: [Brand/Non-brand/Competitor]
├── Intent: [Trans/Comm/Info/Nav]
├── Action: [Keep/Negative/New Keyword]
└── Priority: [High/Med/Low]

STAP 3: ANALYSE METRICS
───────────────────────
POSITIEVE INDICATORS:
├── Conversions > 0
├── Conv. Rate > Campaign Avg
├── ROAS > Target
└── High CTR (>3%)

NEGATIVE INDICATORS:
├── Clicks > 5, Conv = 0
├── CTR < 1%
├── Irrelevante intent
└── CPA > 3x target

STAP 4: ACTIES
──────────────
UPGRADE TO KEYWORD:
├── Search term met 3+ conversies
├── Betere CPA dan campaign avg
├── Voeg toe als Exact Match
└── Create dedicated ad copy

ADD AS NEGATIVE:
├── 0 conversies, significant spend
├── Duidelijk irrelevante intent
├── Voeg toe op juiste level
└── Phrase of Exact negative
```

### Query Sculpting Techniek

```
QUERY SCULPTING STRATEGIE
═════════════════════════

WAT IS QUERY SCULPTING?
───────────────────────
= Queries sturen naar de meest geschikte ad group
  door strategisch gebruik van negatives

VOORBEELD:
──────────
Campaign: Running Shoes
├── Ad Group: Premium Running Shoes
│   ├── "nike hardloopschoenen" (phrase)
│   └── Negative: "goedkoop", "budget", "sale"
│
├── Ad Group: Budget Running Shoes
│   ├── "goedkope hardloopschoenen" (phrase)
│   └── Negative: "nike", "adidas", "premium"
│
└── Resultaat: Queries gaan naar juiste ad group

VOORDELEN:
├── Relevantere ads per query
├── Betere Quality Score
├── Hogere CTR
└── Geoptimaliseerde bids per segment

IMPLEMENTATIE:
──────────────
1. Identificeer overlappende keywords
2. Bepaal welke ad group primair is
3. Voeg cross-negatives toe
4. Monitor search terms voor leakage
5. Adjust negatives waar nodig
```

## Keyword Research Tools & Methodes

### Google Keyword Planner Optimaal Gebruik

```
KEYWORD PLANNER BEST PRACTICES
══════════════════════════════

DISCOVERY MODE:
───────────────
1. "Discover new keywords"
2. Start met:
   ├── Competitor URL (discover their keywords)
   ├── Seed keywords (je top 5 keywords)
   └── Product/Service category

3. Filter op:
   ├── Avg monthly searches: 100-10000
   ├── Competition: Low-Medium (voor nieuwe accounts)
   ├── Top of page bid: Within budget
   └── Language & Location: Your targets

FORECAST MODE:
──────────────
1. "Get search volume and forecasts"
2. Upload je keyword list
3. Set:
   ├── Budget: Your planned budget
   ├── Date range: Next 3 months
   └── Match types: All (compare)

4. Analyseer:
   ├── Estimated clicks
   ├── Estimated CPC
   ├── Total cost
   └── Match type differences

COMPETITOR ANALYSIS:
────────────────────
1. Tools → Keyword Planner
2. "Start with a website"
3. Enter: competitor URL
4. Filter: Products/Services only
5. Export hun top keywords
6. Vergelijk met je eigen lijst
```

### Alternatieve Keyword Research

```
AANVULLENDE KEYWORD BRONNEN
═══════════════════════════

GOOGLE SEARCH FEATURES:
───────────────────────
□ Autocomplete
├── Typ je keyword, noteer suggesties
├── Voeg letters toe: "[keyword] a", "[keyword] b"
└── Andere talen checken

□ Related Searches
├── Onderaan SERP
├── "People also search for"
└── Vaak long-tail variaties

□ "People Also Ask"
├── FAQ-style queries
├── Goed voor content/ad copy
└── Informational intent

TOOLS (Naast Keyword Planner):
──────────────────────────────
□ Google Trends
├── Seizoenspatronen
├── Trending topics
└── Geographic data

□ Search Console
├── Queries waar je organisch rankt
├── Impressions = search volume proxy
└── CTR data voor ad copy

□ Competitor Ad Libraries
├── Facebook Ad Library
├── Google Ads Transparency Center
└── Wat adverteren zij?
```

## Google Ads Script: Search Terms Analyzer

```javascript
/**
 * Search Terms Analyzer Script
 *
 * Analyseert search terms en genereert:
 * - Negative keyword suggesties
 * - New keyword opportunities
 * - Performance alerts
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Schedule: Wekelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Thresholds voor negatives
  NEGATIVE_CLICKS_THRESHOLD: 5,      // Min clicks zonder conversie
  NEGATIVE_COST_THRESHOLD: 20,       // Min cost zonder conversie
  NEGATIVE_CTR_THRESHOLD: 0.01,      // Max CTR voor low performers

  // Thresholds voor nieuwe keywords
  NEW_KEYWORD_CONVERSIONS: 2,        // Min conversies
  NEW_KEYWORD_CPA_MULTIPLIER: 0.8,   // Max CPA vs campaign (80%)

  // Known negative terms (always exclude)
  ALWAYS_NEGATIVE: [
    'gratis', 'free', 'download',
    'vacature', 'baan', 'job',
    'hoe maak', 'diy', 'zelf maken'
  ],

  // Date range
  DATE_RANGE: 'LAST_30_DAYS'
};

function main() {
  var report = {
    negativesSuggested: [],
    newKeywords: [],
    alerts: []
  };

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    analyzeSearchTerms(campaign, report);
  }

  if (report.negativesSuggested.length > 0 ||
      report.newKeywords.length > 0) {
    sendReport(report);
  }

  Logger.log('Analysis complete.');
  Logger.log('Negative suggestions: ' + report.negativesSuggested.length);
  Logger.log('New keyword opportunities: ' + report.newKeywords.length);
}

function analyzeSearchTerms(campaign, report) {
  var campaignName = campaign.getName();
  var campaignStats = campaign.getStatsFor(CONFIG.DATE_RANGE);
  var campaignCPA = campaignStats.getConversions() > 0 ?
    campaignStats.getCost() / campaignStats.getConversions() : 0;

  var searchTerms = campaign.searchTerms()
    .forDateRange(CONFIG.DATE_RANGE)
    .withCondition('Impressions > 10')
    .get();

  while (searchTerms.hasNext()) {
    var term = searchTerms.next();
    var query = term.getText().toLowerCase();
    var stats = term.getStatsFor(CONFIG.DATE_RANGE);

    var clicks = stats.getClicks();
    var cost = stats.getCost();
    var conversions = stats.getConversions();
    var ctr = stats.getCtr();

    // Check for always-negative terms
    for (var i = 0; i < CONFIG.ALWAYS_NEGATIVE.length; i++) {
      if (query.indexOf(CONFIG.ALWAYS_NEGATIVE[i]) !== -1) {
        report.negativesSuggested.push({
          campaign: campaignName,
          term: query,
          reason: 'Contains excluded term: ' + CONFIG.ALWAYS_NEGATIVE[i],
          clicks: clicks,
          cost: cost,
          conversions: conversions
        });
        break;
      }
    }

    // Check for non-converting high-spend terms
    if (conversions === 0) {
      if (clicks >= CONFIG.NEGATIVE_CLICKS_THRESHOLD ||
          cost >= CONFIG.NEGATIVE_COST_THRESHOLD) {
        report.negativesSuggested.push({
          campaign: campaignName,
          term: query,
          reason: 'High spend, no conversions',
          clicks: clicks,
          cost: cost.toFixed(2),
          conversions: conversions
        });
      }
    }

    // Check for low CTR terms
    if (ctr < CONFIG.NEGATIVE_CTR_THRESHOLD && clicks > 0) {
      report.negativesSuggested.push({
        campaign: campaignName,
        term: query,
        reason: 'Very low CTR: ' + (ctr * 100).toFixed(2) + '%',
        clicks: clicks,
        cost: cost.toFixed(2),
        conversions: conversions
      });
    }

    // Check for new keyword opportunities
    if (conversions >= CONFIG.NEW_KEYWORD_CONVERSIONS) {
      var termCPA = cost / conversions;
      if (campaignCPA === 0 || termCPA < (campaignCPA * CONFIG.NEW_KEYWORD_CPA_MULTIPLIER)) {
        report.newKeywords.push({
          campaign: campaignName,
          term: query,
          conversions: conversions,
          cpa: termCPA.toFixed(2),
          campaignCPA: campaignCPA.toFixed(2),
          cost: cost.toFixed(2)
        });
      }
    }
  }
}

function sendReport(report) {
  var subject = 'Search Terms Analysis - ' + AdsApp.currentAccount().getName();
  var body = 'Weekly Search Terms Analysis\n';
  body += '============================\n\n';

  if (report.negativesSuggested.length > 0) {
    body += 'NEGATIVE KEYWORD SUGGESTIONS:\n';
    body += '─────────────────────────────\n';
    for (var i = 0; i < Math.min(report.negativesSuggested.length, 20); i++) {
      var neg = report.negativesSuggested[i];
      body += '• "' + neg.term + '"\n';
      body += '  Campaign: ' + neg.campaign + '\n';
      body += '  Reason: ' + neg.reason + '\n';
      body += '  Clicks: ' + neg.clicks + ', Cost: €' + neg.cost + '\n\n';
    }
    if (report.negativesSuggested.length > 20) {
      body += '... and ' + (report.negativesSuggested.length - 20) + ' more\n';
    }
    body += '\n';
  }

  if (report.newKeywords.length > 0) {
    body += 'NEW KEYWORD OPPORTUNITIES:\n';
    body += '─────────────────────────\n';
    for (var j = 0; j < Math.min(report.newKeywords.length, 10); j++) {
      var kw = report.newKeywords[j];
      body += '• "' + kw.term + '"\n';
      body += '  Campaign: ' + kw.campaign + '\n';
      body += '  Conversions: ' + kw.conversions + ', CPA: €' + kw.cpa + '\n';
      body += '  (Campaign avg CPA: €' + kw.campaignCPA + ')\n\n';
    }
  }

  body += '\n---\nGenerated by Search Terms Analyzer Script';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
  Logger.log('Report sent to ' + CONFIG.EMAIL);
}
```

## Output: Keyword Strategy Template

```markdown
# Keyword Strategy Plan

## Account Overzicht
- **Business type:** [E-commerce / Lead Gen / SaaS]
- **Monthly budget:** €[X]
- **Target CPA/ROAS:** €[X] / [X]%
- **Primary markets:** [NL/BE/DACH/etc.]

## Keyword Structuur

### Campaign: [Campaign Name]
**Match Type Mix:**
- Exact Match: [X]%
- Phrase Match: [X]%
- Broad Match: [X]%

**Ad Groups:**

#### Ad Group 1: [Theme]
| Keyword | Match Type | Expected CPC | Priority |
|---------|------------|--------------|----------|
| [keyword] | Exact | €X.XX | High |
| "keyword phrase" | Phrase | €X.XX | High |
| keyword broad | Broad | €X.XX | Medium |

## Negative Keyword Lists

### Account-Level Negatives
```
gratis
free
vacature
job
diy
zelf maken
```

### Campaign-Specific Negatives
```
[Campaign 1]: competitor name, irrelevant category
[Campaign 2]: out-of-scope locations, services not offered
```

## Search Terms Review Schedule
- **Frequency:** [Weekly/Bi-weekly]
- **Owner:** [Name]
- **Actions:**
  - [ ] Add converting terms as keywords
  - [ ] Add non-converting terms as negatives
  - [ ] Update ad copy based on insights

## KPIs & Monitoring
- **Target CTR:** [X]%
- **Target Quality Score:** [X]+
- **Max keyword CPA:** €[X]
- **Review date:** [Date]
```

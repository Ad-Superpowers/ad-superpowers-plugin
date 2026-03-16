---
name: competitive-analysis-toolkit
description: "Google Ads Competitive Analysis Toolkit voor marktanalyse en competitor monitoring. Gebruik voor: (1) Auction Insights analyse en interpretatie, (2) Competitor strategie identificatie, (3) Market share berekening, (4) Competitive response strategie, (5) Share of Voice monitoring. Triggers: auction insights, competitors, concurrentie, marktaandeel, market share, overlap rate, outranking share, competitive analysis, concurrentieanalyse, wie adverteert."
---

# Competitive Analysis Toolkit

Complete gids voor het analyseren van competitie in Google Ads, van Auction Insights interpretatie tot strategische respons op competitor activiteiten.

## Quick Analysis Guide

```
WAT WIL JE WETEN?
│
├─► WIE ZIJN MIJN COMPETITORS?
│   └─► Ga naar: "Auction Insights Basis"
│
├─► HOE PRESTEREN COMPETITORS VS MIJ?
│   └─► Ga naar: "Competitive Metrics Analyse"
│
├─► COMPETITOR IS AGRESSIEVER GEWORDEN
│   └─► Ga naar: "Competitive Response Strategie"
│
├─► HOEVEEL MARKTAANDEEL HEB IK?
│   └─► Ga naar: "Market Share Berekening"
│
├─► WAT DOEN COMPETITORS IN HUN ADS?
│   └─► Ga naar: "Competitor Ad Intelligence"
│
└─► HOE MONITOR IK COMPETITORS CONTINU?
    └─► Ga naar: "Competitive Monitoring Setup"
```

## Auction Insights Basis

### Waar Te Vinden

```
AUCTION INSIGHTS LOCATIE
════════════════════════

NIVEAU 1: CAMPAIGN
──────────────────
Campaigns → Selecteer campaign → Auction Insights

NIVEAU 2: AD GROUP
──────────────────
Ad Groups → Selecteer ad group → Auction Insights

NIVEAU 3: KEYWORD
─────────────────
Keywords → Selecteer keywords → Auction Insights

⚠️ BELANGRIJK:
├── Auction Insights alleen beschikbaar bij voldoende data
├── Minimaal impressies nodig voor statistisch relevant
├── Data is geaggregeerd (geen exacte getallen)
└── Updates dagelijks, niet real-time
```

### Metrics Uitleg

```
AUCTION INSIGHTS METRICS VERKLAARD
══════════════════════════════════

┌────────────────────────┬─────────────────────────────────────────────┐
│ Metric                 │ Wat Het Meet                                │
├────────────────────────┼─────────────────────────────────────────────┤
│ Impression Share       │ % van impressies die JIJ kreeg vs totaal    │
│                        │ beschikbaar voor jouw keywords              │
├────────────────────────┼─────────────────────────────────────────────┤
│ Overlap Rate           │ % van JOUW impressies waarbij competitor    │
│                        │ OOK een impressie kreeg                     │
├────────────────────────┼─────────────────────────────────────────────┤
│ Position Above Rate    │ % van overlapping impressies waar           │
│                        │ competitor BOVEN jou stond                  │
├────────────────────────┼─────────────────────────────────────────────┤
│ Top of Page Rate       │ % van impressies in top positions           │
│                        │ (boven organische resultaten)               │
├────────────────────────┼─────────────────────────────────────────────┤
│ Abs. Top of Page Rate  │ % van impressies op EERSTE positie          │
│                        │ (absolute top)                              │
├────────────────────────┼─────────────────────────────────────────────┤
│ Outranking Share       │ % van auctions waar jij BOVEN competitor    │
│                        │ stond OF wel verscheen en zij niet          │
└────────────────────────┴─────────────────────────────────────────────┘

FORMULE RELATIES:
─────────────────
Outranking Share = (Jij hoger) + (Jij wel, zij niet)
                   ────────────────────────────────
                   Totaal eligible auctions

Position Above Rate + Position Below Rate = 100%
(voor overlapping auctions)

⚠️ NOTE: Deze metrics zijn relatief tot JOU, niet absolute markt shares.
```

### Interpretatie Gids

```
HOE AUCTION INSIGHTS TE INTERPRETEREN
═════════════════════════════════════

SCENARIO 1: HOGE OVERLAP, LAGE OUTRANKING
─────────────────────────────────────────
Overlap Rate: 85%
Outranking Share: 30%
Position Above Rate: 55%

Interpretatie:
├── Competitor target dezelfde keywords
├── Zij winnen vaker (staan boven jou)
├── Possible: Hogere bids of betere Quality Score

Actie:
├── Check Quality Score verschil
├── Evalueer bid strategy
├── Overweeg differentiation (andere keywords)

SCENARIO 2: LAGE OVERLAP, HOGE IMPRESSION SHARE
───────────────────────────────────────────────
Overlap Rate: 20%
Your Impression Share: 70%

Interpretatie:
├── Jij domineert dit keyword segment
├── Weinig directe competitie
├── Possible: Niche of branded terms

Actie:
├── Behoud positie
├── Overweeg bid efficiency (niet overbieden)
├── Explore expansion opportunities

SCENARIO 3: NIEUWE COMPETITOR VERSCHIJNT
────────────────────────────────────────
Week 1: Competitor niet in insights
Week 2: Competitor met 40% overlap, 60% position above

Interpretatie:
├── Nieuwe marktentrant
├── Agressieve bidding strategie
├── Impact op jouw impression share

Actie:
├── Monitor trends
├── Analyseer hun ads (manual search)
├── Bepaal of response nodig is

SCENARIO 4: COMPETITOR IMPRESSION SHARE STIJGT
──────────────────────────────────────────────
Competitor IS: 30% → 50% over 4 weken
Jouw IS: 60% → 45% over 4 weken

Interpretatie:
├── Competitor investeert meer
├── Jouw market share daalt
├── Directe competitie intensiever

Actie:
├── Evalueer ROI van deze keywords
├── Verhoog bids indien profitable
├── Of: Shift naar minder competitive segments
```

## Competitive Metrics Analyse

### Benchmark Dashboard

```
COMPETITIVE BENCHMARK ANALYSE
═════════════════════════════

STAP 1: EXPORT AUCTION INSIGHTS DATA
────────────────────────────────────
Campaigns → Auction Insights → Download

Selecteer periode: Minimaal 30 dagen

STAP 2: BOUW BENCHMARK TABEL
────────────────────────────

Voor TOP 5 competitors:

┌─────────────────────────────────────────────────────────────────────────┐
│ Competitor   │ Imp Share │ Overlap │ Pos Above │ Outranking │ Trend    │
├──────────────┼───────────┼─────────┼───────────┼────────────┼──────────┤
│ You          │ 45%       │ -       │ -         │ -          │ Baseline │
│ Competitor A │ 52%       │ 78%     │ 55%       │ 42%        │ ↑ +5%    │
│ Competitor B │ 38%       │ 65%     │ 35%       │ 58%        │ → Stable │
│ Competitor C │ 30%       │ 45%     │ 20%       │ 72%        │ ↓ -8%    │
│ Competitor D │ 25%       │ 40%     │ 50%       │ 48%        │ NEW      │
│ Competitor E │ 18%       │ 30%     │ 25%       │ 68%        │ → Stable │
└──────────────┴───────────┴─────────┴───────────┴────────────┴──────────┘

STAP 3: BEREKEN COMPETITIVE INDEX
─────────────────────────────────
Per competitor:

Threat Score = (Overlap Rate × Position Above Rate) / 100

Voorbeeld:
├── Competitor A: (78% × 55%) / 100 = 42.9 (HOOG)
├── Competitor B: (65% × 35%) / 100 = 22.8 (MEDIUM)
└── Competitor C: (45% × 20%) / 100 = 9.0 (LAAG)

Prioriteer focus op hoogste Threat Scores.
```

### Trend Analyse

```
COMPETITIVE TREND TRACKING
══════════════════════════

WEEK-OVER-WEEK ANALYSE:
───────────────────────
Track per competitor:

Week 1 → Week 2 → Week 3 → Week 4

Metrics te tracken:
├── Impression Share delta
├── Position Above Rate delta
├── Outranking Share delta
└── Nieuwe verschijningen

SIGNALEN VAN COMPETITOR ACTIVITEIT:
───────────────────────────────────

🔴 AGRESSIEVE EXPANSIE:
├── Impression Share stijgt >10% per week
├── Nieuwe keywords waar overlap verschijnt
├── Stijgende Position Above Rate
└── Actie: Analyseer strategie, overweeg response

🟡 STABIELE COMPETITIE:
├── Metrics +/- 5% range
├── Geen nieuwe competitors
├── Voorspelbare patterns
└── Actie: Maintain current strategy

🟢 COMPETITOR RETREAT:
├── Dalende Impression Share
├── Dalende Overlap Rate
├── Verdwijnen uit insights
└── Actie: Opportunity om market share te pakken

SEASONALITY IN COMPETITION:
───────────────────────────
Track year-over-year:
├── Q4: E-commerce competitors agressiever
├── Januari: B2B budget renewals
├── Industry-specific patterns
└── Plan budget/bids rond competitive peaks
```

## Market Share Berekening

### Impression Share als Proxy

```
MARKET SHARE CALCULATION
════════════════════════

METHODE 1: IMPRESSION SHARE BASIS
─────────────────────────────────
Jouw Impression Share geeft indicatie van jouw aandeel
in het totaal beschikbare volume.

Voorbeeld:
├── Jouw Search Impression Share: 45%
├── Interpretation: Je vangt 45% van eligible searches
└── Remaining 55%: Competitors of gemiste opportunities

Verfijning:
├── Lost IS (Budget): 20%
├── Lost IS (Rank): 35%
├── Jouw Share: 45%
└── Total: 100%

Als je budget had en rank verbeterde:
├── Potential Share: 45% + 35% (rank) = 80%
└── Budget-constrained ceiling: 45% + 20% = 65%

METHODE 2: RELATIVE MARKET SHARE
────────────────────────────────
Bereken jouw share relatief tot bekende competitors:

Total Known IS = Jouw IS + Sum(Competitor IS)

Jouw Relative Share = Jouw IS / Total Known IS

Voorbeeld:
├── Jouw IS: 45%
├── Competitor A: 52%
├── Competitor B: 38%
├── Competitor C: 30%
├── Total Known: 165%* (overlap betekent >100% mogelijk)
└── Jouw Relative: 45/165 = 27%

*Note: Overlap maakt dat som >100% kan zijn

METHODE 3: SHARE OF VOICE (SOV)
───────────────────────────────
Share of Voice = Jouw Impressions / Total Market Impressions

Probleem: Je weet niet hoeveel impressies markt totaal heeft.

Proxy:
├── Gebruik Keyword Planner voor search volumes
├── Jouw impressies / Estimated total searches
└── Geeft indicatie van SOV

Voorbeeld:
├── Keywords: 100,000 monthly searches (KW Planner)
├── Jouw impressies: 40,000 (Google Ads)
├── SOV: 40,000 / 100,000 = 40%
```

### Competitive Position Matrix

```
COMPETITIVE POSITION MATRIX
═══════════════════════════

Plot competitors op 2 assen:

Y-axis: Impression Share (markt presence)
X-axis: Position Above Rate (competitive strength)

        HIGH IS
           │
    MARKET │  DOMINANT
    LEADERS│  PLAYERS
           │
LOW ───────┼─────────── HIGH
Position   │           Position
Above      │           Above
           │
    NICHE  │  AGGRESSIVE
    PLAYERS│  CHALLENGERS
           │
        LOW IS

QUADRANT INTERPRETATIE:
───────────────────────

DOMINANT PLAYERS (High IS, High Position Above):
├── Grote budgetten
├── Sterke Quality Scores
├── Moeilijk te verslaan direct
└── Strategie: Differentiate, niche down

MARKET LEADERS (High IS, Low Position Above):
├── Veel volume, maar niet altijd bovenaan
├── Mogelijk breed targeting
├── Opportunity: Outbid op specifics
└── Strategie: Focus op high-value auctions

AGGRESSIVE CHALLENGERS (Low IS, High Position Above):
├── Selectief maar agressief bieden
├── Cherry-picking beste opportunities
├── Sterk op specifieke segments
└── Strategie: Monitor en learn

NICHE PLAYERS (Low IS, Low Position Above):
├── Kleine spelers
├── Limited competition
├── Possible future threats
└── Strategie: Monitor for growth
```

## Competitor Ad Intelligence

### Manual Research

```
COMPETITOR AD RESEARCH
══════════════════════

METHODE 1: MANUAL SEARCH
────────────────────────
□ Open incognito/private browser
□ Search op jouw belangrijkste keywords
□ Noteer:
  ├── Welke competitors verschijnen
  ├── Ad positions
  ├── Headlines en descriptions
  ├── Extensions in gebruik
  ├── Offers en promoties
  └── Landing page URLs

TEMPLATE VOOR AD NOTITIES:
──────────────────────────
Keyword: [keyword]
Datum: [datum]

Competitor A:
├── Positie: [1/2/3/etc]
├── Headline 1: "[tekst]"
├── Headline 2: "[tekst]"
├── Headline 3: "[tekst]"
├── Description: "[tekst]"
├── Extensions: [Sitelinks/Callouts/etc]
├── Offer: [Korting/Gratis/etc]
└── Landing Page: [URL]

Competitor B:
└── ...

FREQUENTIE:
├── Weekly check: Top 10 keywords
├── Monthly deep dive: Top 50 keywords
└── Event-based: Bij grote competitor changes

METHODE 2: GOOGLE ADS TRANSPARENCY CENTER
─────────────────────────────────────────
https://adstransparency.google.com/

□ Search op competitor naam
□ Zie alle ads die ze runnen
□ Filter op regio, tijd, format
□ Bekijk creative variaties

Beperkingen:
├── Alleen actieve ads
├── Geen performance data
└── Geen targeting info
```

### Competitor Strategy Patterns

```
COMPETITOR STRATEGIE HERKENNEN
══════════════════════════════

PATTERN 1: AGGRESSIVE MARKET SHARE
──────────────────────────────────
Signalen:
├── Hoge bids (top positions always)
├── Brede keyword coverage
├── Aggressive offers in ads
└── Hoge Impression Share over alle terms

Waarschijnlijke strategie:
├── Growth/market share focus
├── Venture-backed of nieuw in markt
├── Bereid om te verliezen voor share
└── Kan lange termijn duur zijn

Jouw response:
├── NIET matchen (cost war je verliest)
├── Focus op efficiency en niche
├── Wacht tot zij optimaliseren of stoppen
└── Differentiate op value, niet prijs

PATTERN 2: CHERRY-PICKING
─────────────────────────
Signalen:
├── Hoge position alleen op specifieke keywords
├── Lage Impression Share overall
├── Zeer gerichte targeting
└── Premium ads op high-value terms

Waarschijnlijke strategie:
├── ROI-focused
├── Alleen bieden waar winstgevend
├── Slimme optimalisatie
└── Sustainable approach

Jouw response:
├── Identificeer keywords waar zij NIET zijn
├── Test hun high-value keywords (competitive)
├── Learn van hun keyword selectie
└── Match quality, niet volume

PATTERN 3: DEFENSIVE/BRAND
──────────────────────────
Signalen:
├── Dominant alleen op eigen brand terms
├── Low presence op generic terms
├── High IS op branded
└── Minimal non-brand activity

Waarschijnlijke strategie:
├── Bescherm bestaande traffic
├── Minimal acquisition focus
├── Kostenefficiënt
└── Mature/established player

Jouw response:
├── Opportunity op non-brand
├── Voorzichtig met competitor conquesting
├── Focus op generics waar zij afwezig
└── Bouw eigen brand

PATTERN 4: PROMOTIONAL SURGE
────────────────────────────
Signalen:
├── Plotselinge IS increase
├── Aggressive offers in ads
├── Tijdelijk (sales periods)
└── Terug naar baseline na event

Waarschijnlijke strategie:
├── Seasonal/event-driven
├── Sale periods
├── Product launches
└── Short-term focus

Jouw response:
├── Track timing en patronen
├── Plan eigen promoties strategisch
├── Avoid direct competition tijdens peaks
└── Capture traffic wanneer zij normaliseren
```

## Competitive Response Strategie

### Response Framework

```
COMPETITIVE RESPONSE DECISION TREE
══════════════════════════════════

COMPETITOR WORDT AGRESSIEVER
│
├─► STAP 1: ASSESS IMPACT
│   ├── Jouw IS gedaald >10%? → Significant impact
│   ├── CPA/ROAS verslechterd? → Direct financial impact
│   └── Conversies gedaald? → Business impact
│
├─► STAP 2: EVALUATE PROFITABILITY
│   ├── Kunnen we matchen en winstgevend blijven?
│   │   ├── JA → Overweeg bid increase
│   │   └── NEE → Ga naar differentiation
│   │
│   └── Break-even CPA/ROAS berekenen:
│       └── Als competitor wins = boven jouw break-even?
│           └── Laat ze "winnen" op verliesgevende auctions
│
├─► STAP 3: CHOOSE STRATEGY
│   │
│   ├─► OPTIE A: COMPETE DIRECT
│   │   ├── Verhoog bids/targets
│   │   ├── Verbeter Quality Score
│   │   ├── Expand budget
│   │   └── Beste als: Je kunt winstgevend concurreren
│   │
│   ├─► OPTIE B: DIFFERENTIATE
│   │   ├── Focus op andere keywords
│   │   ├── Target andere audiences
│   │   ├── Andere USPs in ads
│   │   └── Beste als: Direct concurreren te duur
│   │
│   ├─► OPTIE C: NICHE DOWN
│   │   ├── Zeer specifieke long-tail
│   │   ├── Geographic niches
│   │   ├── Audience niches
│   │   └── Beste als: Grote speler die je niet kunt matchen
│   │
│   └─► OPTIE D: WAIT & MONITOR
│       ├── Track competitor over tijd
│       ├── Vaak unsustainable strategies
│       ├── Wacht op normalisatie
│       └── Beste als: Competitor lijkt irrationeel
│
└─► STAP 4: IMPLEMENT & MONITOR
    ├── Implementeer gekozen strategie
    ├── Track resultaten weekly
    ├── Adjust based on response
    └── Document learnings
```

### Tactical Responses

```
TACTISCHE COMPETITIEVE RESPONSES
════════════════════════════════

TACTIEK 1: QUALITY SCORE VERBETERING
────────────────────────────────────
Impact: Lagere CPCs, betere posities zonder hogere bids

Acties:
□ Verbeter ad relevance (keyword in ad)
□ Verbeter expected CTR (better ads, extensions)
□ Verbeter landing page experience
□ Tight themed ad groups

ROI: Hoog (duurzaam voordeel)

TACTIEK 2: BID STRATEGY OPTIMIZATION
────────────────────────────────────
Impact: Slimmer bieden, niet per se meer

Acties:
□ Target Impression Share voor visibility
□ Portfolio strategies voor efficiency
□ Maximize Conversion Value voor revenue focus
□ Dayparting rond competitor zwakke momenten

ROI: Medium (requires monitoring)

TACTIEK 3: COVERAGE EXPANSION
─────────────────────────────
Impact: Win waar competitor niet is

Acties:
□ Long-tail keyword expansion
□ Geographic expansion
□ Device-specific campaigns
□ Audience targeting toevoegen

ROI: Medium-High (less competitive = cheaper)

TACTIEK 4: AD CREATIVE DIFFERENTIATION
──────────────────────────────────────
Impact: Win clicks met betere ads, niet hogere bids

Acties:
□ Unique value propositions
□ Aggressive offers (if possible)
□ Social proof (reviews, ratings)
□ Full extension usage

ROI: High (sustainable, improves QS too)

TACTIEK 5: LANDING PAGE ADVANTAGE
─────────────────────────────────
Impact: Win de conversion, niet alleen de click

Acties:
□ Faster page speed
□ Better mobile experience
□ Clearer value proposition
□ Stronger CTAs

ROI: High (improves QS AND conversion rate)
```

## Competitive Monitoring Setup

### Automated Alerts

```
COMPETITIVE MONITORING ALERTS
═════════════════════════════

ALERT 1: IMPRESSION SHARE DROP
──────────────────────────────
Trigger: Jouw IS daalt >15% week-over-week
Action: Email alert
Cause: Competitor agressiever of jouw issue
Response: Investigate root cause

ALERT 2: NEW COMPETITOR
───────────────────────
Trigger: Nieuwe domeinnaam in Auction Insights
Action: Email alert met competitor details
Cause: Market entry
Response: Analyze and monitor

ALERT 3: POSITION LOSS
──────────────────────
Trigger: Avg position daalt >0.5 of Top IS drops >20%
Action: Email alert
Cause: Competitor bids, jouw QS, of budget
Response: Diagnose and adjust

ALERT 4: CPC SPIKE
──────────────────
Trigger: Avg CPC stijgt >20%
Action: Email alert
Cause: Competitive pressure of QS decline
Response: Check auction insights for correlation

SETUP VIA GOOGLE ADS RULES:
───────────────────────────
Tools → Bulk Actions → Rules → Create Rule

Voorbeeld:
├── Rule Type: Email when...
├── Condition: Search Impr. Share < 40%
├── Frequency: Weekly
└── Action: Send email to team
```

### Weekly Competitive Review

```
WEEKLY COMPETITIVE REVIEW CHECKLIST
═══════════════════════════════════

ELKE MAANDAG (15-30 min):
─────────────────────────

□ 1. AUCTION INSIGHTS REVIEW
  ├── Download Auction Insights (last 7 days)
  ├── Compare to previous week
  ├── Note significant changes
  └── Identify new competitors

□ 2. IMPRESSION SHARE TREND
  ├── Chart IS over last 4 weeks
  ├── Identify trends (up/down/stable)
  └── Correlate with competitor activity

□ 3. POSITION METRICS
  ├── Top of page rate trend
  ├── Abs top of page rate trend
  └── Compare to competitors

□ 4. MANUAL SPOT CHECK
  ├── Search top 5 keywords (incognito)
  ├── Screenshot competitor ads
  ├── Note new offers/messages
  └── Check landing pages

□ 5. ACTION ITEMS
  ├── List required responses
  ├── Prioritize by impact
  ├── Assign and schedule
  └── Document decisions

MAANDELIJKSE DEEP DIVE (1 uur):
───────────────────────────────

□ Full competitor landscape analysis
□ Strategy assessment per competitor
□ Trend analysis (3-month view)
□ Strategic recommendations
□ Budget allocation review
```

## Google Ads Script: Competitive Monitor

```javascript
/**
 * Competitive Analysis Monitor
 *
 * Monitort Auction Insights data en stuurt alerts
 * bij significante competitor veranderingen.
 *
 * Note: Auction Insights data niet direct via API.
 * Dit script monitort proxy metrics en impression share.
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Schedule: Dagelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Thresholds for alerts
  IMPRESSION_SHARE_DROP_THRESHOLD: -0.15,  // -15%
  CPC_INCREASE_THRESHOLD: 0.20,            // +20%
  POSITION_DROP_THRESHOLD: 0.5,            // 0.5 positions

  // Campaigns to monitor (leave empty for all)
  CAMPAIGNS_TO_MONITOR: [], // e.g., ['Brand', 'Non-Brand']

  // Date ranges
  CURRENT_PERIOD: 'LAST_7_DAYS',
  PREVIOUS_PERIOD: 'LAST_14_DAYS'
};

function main() {
  var report = {
    alerts: [],
    metrics: [],
    summary: {}
  };

  var campaignIterator;
  if (CONFIG.CAMPAIGNS_TO_MONITOR.length > 0) {
    campaignIterator = AdsApp.campaigns()
      .withCondition('Status = ENABLED')
      .withCondition("Name IN ['" + CONFIG.CAMPAIGNS_TO_MONITOR.join("','") + "']")
      .get();
  } else {
    campaignIterator = AdsApp.campaigns()
      .withCondition('Status = ENABLED')
      .get();
  }

  while (campaignIterator.hasNext()) {
    var campaign = campaignIterator.next();
    var analysis = analyzeCampaignCompetitiveness(campaign);

    report.metrics.push(analysis.metrics);
    report.alerts = report.alerts.concat(analysis.alerts);
  }

  report.summary = {
    campaignsAnalyzed: report.metrics.length,
    alertsGenerated: report.alerts.length,
    timestamp: new Date().toISOString()
  };

  if (report.alerts.length > 0) {
    sendCompetitiveReport(report);
  }

  Logger.log('Competitive analysis complete');
  Logger.log('Campaigns analyzed: ' + report.metrics.length);
  Logger.log('Alerts: ' + report.alerts.length);
}

function analyzeCampaignCompetitiveness(campaign) {
  var name = campaign.getName();
  var alerts = [];

  // Get current period stats
  var currentStats = campaign.getStatsFor(CONFIG.CURRENT_PERIOD);
  var previousStats = campaign.getStatsFor(CONFIG.PREVIOUS_PERIOD);

  // Current metrics
  var current = {
    impressions: currentStats.getImpressions(),
    clicks: currentStats.getClicks(),
    cost: currentStats.getCost(),
    avgCpc: currentStats.getAverageCpc()
  };

  // Previous period (subtract current to get prev week)
  var previous = {
    impressions: previousStats.getImpressions() - current.impressions,
    clicks: previousStats.getClicks() - current.clicks,
    cost: previousStats.getCost() - current.cost
  };
  previous.avgCpc = previous.clicks > 0 ?
    previous.cost / previous.clicks : 0;

  // Calculate changes
  var metrics = {
    name: name,
    currentImpressions: current.impressions,
    previousImpressions: previous.impressions,
    impressionChange: previous.impressions > 0 ?
      (current.impressions - previous.impressions) / previous.impressions : 0,
    currentCpc: current.avgCpc,
    previousCpc: previous.avgCpc,
    cpcChange: previous.avgCpc > 0 ?
      (current.avgCpc - previous.avgCpc) / previous.avgCpc : 0
  };

  // Get Search Impression Share if available
  try {
    var report = AdsApp.report(
      'SELECT CampaignName, SearchImpressionShare ' +
      'FROM CAMPAIGN_PERFORMANCE_REPORT ' +
      'WHERE CampaignName = "' + name + '" ' +
      'DURING ' + CONFIG.CURRENT_PERIOD.replace('_', '').replace('LAST', 'LAST_')
    );

    var rows = report.rows();
    if (rows.hasNext()) {
      var row = rows.next();
      var isStr = row['SearchImpressionShare'];
      if (isStr && isStr !== '--' && isStr !== ' --') {
        metrics.impressionShare = parseFloat(isStr.replace('%', '')) / 100;
      }
    }
  } catch (e) {
    // Impression share not available via report
    Logger.log('Could not get impression share for ' + name);
  }

  // Generate alerts

  // Impression drop alert
  if (metrics.impressionChange <= CONFIG.IMPRESSION_SHARE_DROP_THRESHOLD &&
      previous.impressions > 100) {
    alerts.push({
      campaign: name,
      type: 'IMPRESSION_DROP',
      severity: 'WARNING',
      message: 'Impressies gedaald met ' +
               (Math.abs(metrics.impressionChange) * 100).toFixed(1) + '%',
      current: current.impressions,
      previous: previous.impressions,
      possibleCause: 'Competitor activiteit of budget/bid issues'
    });
  }

  // CPC increase alert
  if (metrics.cpcChange >= CONFIG.CPC_INCREASE_THRESHOLD &&
      previous.avgCpc > 0) {
    alerts.push({
      campaign: name,
      type: 'CPC_SPIKE',
      severity: 'WARNING',
      message: 'Gemiddelde CPC gestegen met ' +
               (metrics.cpcChange * 100).toFixed(1) + '%',
      current: '€' + current.avgCpc.toFixed(2),
      previous: '€' + previous.avgCpc.toFixed(2),
      possibleCause: 'Verhoogde competitie of Quality Score daling'
    });
  }

  // Low impression share alert
  if (metrics.impressionShare && metrics.impressionShare < 0.30) {
    alerts.push({
      campaign: name,
      type: 'LOW_IMPRESSION_SHARE',
      severity: 'INFO',
      message: 'Impression Share is ' +
               (metrics.impressionShare * 100).toFixed(1) + '%',
      possibleCause: 'Budget of bid beperkingen, of sterke competitie'
    });
  }

  return {
    metrics: metrics,
    alerts: alerts
  };
}

function sendCompetitiveReport(report) {
  var subject = 'Competitive Alert - ' + AdsApp.currentAccount().getName();
  var body = 'Competitive Analysis Report\n';
  body += '===========================\n\n';

  body += 'SUMMARY:\n';
  body += '• Campaigns analyzed: ' + report.summary.campaignsAnalyzed + '\n';
  body += '• Alerts generated: ' + report.summary.alertsGenerated + '\n';
  body += '• Timestamp: ' + report.summary.timestamp + '\n\n';

  if (report.alerts.length > 0) {
    body += 'COMPETITIVE ALERTS:\n';
    body += '───────────────────\n\n';

    for (var i = 0; i < report.alerts.length; i++) {
      var alert = report.alerts[i];
      body += '[' + alert.severity + '] ' + alert.campaign + '\n';
      body += 'Type: ' + alert.type + '\n';
      body += 'Issue: ' + alert.message + '\n';
      if (alert.current) {
        body += 'Current: ' + alert.current + ' | Previous: ' + alert.previous + '\n';
      }
      body += 'Possible cause: ' + alert.possibleCause + '\n\n';
    }
  }

  body += 'CAMPAIGN METRICS:\n';
  body += '─────────────────\n\n';

  for (var j = 0; j < Math.min(report.metrics.length, 10); j++) {
    var m = report.metrics[j];
    body += '• ' + m.name + '\n';
    body += '  Impressions: ' + m.currentImpressions;
    body += ' (change: ' + (m.impressionChange * 100).toFixed(1) + '%)\n';
    body += '  Avg CPC: €' + m.currentCpc.toFixed(2);
    body += ' (change: ' + (m.cpcChange * 100).toFixed(1) + '%)\n';
    if (m.impressionShare) {
      body += '  Impression Share: ' + (m.impressionShare * 100).toFixed(1) + '%\n';
    }
    body += '\n';
  }

  body += '\n---\nGenerated by Competitive Monitor Script\n';
  body += 'Note: For full Auction Insights data, check Google Ads UI.';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Output: Competitive Analysis Report Template

```markdown
# Competitive Analysis Report

## Executive Summary
- **Reporting period:** [Datum range]
- **Market position:** [Leader/Challenger/Follower]
- **Key trend:** [Beschrijf belangrijkste ontwikkeling]
- **Action required:** [Ja/Nee + korte toelichting]

## Competitive Landscape

### Top Competitors
| Competitor | Imp Share | Overlap | Position Above | Outranking | Trend |
|------------|-----------|---------|----------------|------------|-------|
| [Jij] | [X]% | - | - | - | Baseline |
| [Comp A] | [X]% | [X]% | [X]% | [X]% | [↑/↓/→] |
| [Comp B] | [X]% | [X]% | [X]% | [X]% | [↑/↓/→] |
| [Comp C] | [X]% | [X]% | [X]% | [X]% | [↑/↓/→] |

### Market Dynamics
- **Nieuwe entrants:** [Beschrijf]
- **Vertrekkende competitors:** [Beschrijf]
- **Trend in competitie intensiteit:** [Toenemend/Stabiel/Afnemend]

## Competitor Deep Dives

### [Competitor A]
**Strategy type:** [Aggressive/Selective/Defensive]

**Observed tactics:**
- [Tactiek 1]
- [Tactiek 2]
- [Tactiek 3]

**Ad messaging:**
- Headlines: [Voorbeeld headlines]
- Offers: [Promoties/aanbiedingen]
- USPs: [Unique selling points]

**Threat level:** [Hoog/Medium/Laag]

### [Competitor B]
[Zelfde structuur]

## Strategic Recommendations

### Immediate Actions (This Week)
1. [Actie 1] - [Rationale]
2. [Actie 2] - [Rationale]

### Short-term Actions (This Month)
1. [Actie 1] - [Rationale]
2. [Actie 2] - [Rationale]

### Long-term Strategy
- [Strategische richting]
- [Investment areas]
- [Differentiation opportunities]

## Monitoring Plan
- **Daily:** [Metrics om te checken]
- **Weekly:** [Review activiteiten]
- **Monthly:** [Deep dive analyses]

## Appendix
- Raw Auction Insights data
- Competitor ad screenshots
- Historical trend charts
```

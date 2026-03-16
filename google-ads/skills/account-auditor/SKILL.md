---
name: account-auditor
description: "Complete Google Ads account audit met health score en actionable aanbevelingen. Gebruik voor: (1) Account takeover audits, (2) Periodieke reviews, (3) Performance diagnose, (4) Optimization opportunities identificeren, (5) Quick health checks. Triggers: audit, account review, health check, optimization, takeover, diagnose."
---

# Account Auditor

Systematisch framework voor het uitvoeren van complete Google Ads account audits, inclusief health scoring, issue identificatie en geprioriteerde aanbevelingen.

## Audit Framework

### Audit Scope Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  GOOGLE ADS ACCOUNT AUDIT GEBIEDEN                              │
│                                                                 │
│  1. CONVERSION TRACKING & DATA QUALITY                          │
│     └── Tags, Enhanced Conversions, Attribution, Values         │
│                                                                 │
│  2. ACCOUNT STRUCTURE                                           │
│     └── Campaigns, Ad Groups, Naming, Organization              │
│                                                                 │
│  3. KEYWORD STRATEGY                                            │
│     └── Match Types, Negatives, Quality Score, Search Terms     │
│                                                                 │
│  4. AD COPY & CREATIVE                                          │
│     └── RSAs, Ad Strength, Extensions, Asset Groups             │
│                                                                 │
│  5. BIDDING & BUDGET                                            │
│     └── Smart Bidding, Targets, Budget Allocation               │
│                                                                 │
│  6. AUDIENCES                                                   │
│     └── Remarketing, Customer Match, Signals, Exclusions        │
│                                                                 │
│  7. PERFORMANCE METRICS                                         │
│     └── KPIs, Trends, Benchmarks, Efficiency                    │
└─────────────────────────────────────────────────────────────────┘
```

## Complete Audit Checklist

### Section 1: Conversion Tracking & Data Quality

```
TRACKING AUDIT
==============

□ CONVERSION ACTIONS
├── Welke conversion actions zijn actief?
├── Correct ingesteld als Primary vs Secondary?
├── Juiste counting method (One/Every)?
├── Attribution model: Data-driven actief?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ GOOGLE TAG STATUS
├── Tag geïnstalleerd op alle pagina's?
├── Geen duplicate tags?
├── Tag fires correct bij conversies?
├── Values worden correct doorgestuurd?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ ENHANCED CONVERSIONS
├── Enhanced Conversions ingeschakeld?
├── User data wordt verzonden (email, phone)?
├── Match rate acceptabel (>70%)?
├── Consent Mode v2 geïmplementeerd?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ DATA QUALITY
├── Conversion rate realistisch vs industry?
├── Values komen overeen met backend/GA4?
├── Geen duplicate conversies?
├── Conversion lag acceptabel (<24u)?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ OFFLINE CONVERSIONS (Lead Gen)
├── Worden offline conversions geïmporteerd?
├── Import frequentie voldoende (wekelijks min)?
├── Lead → Sale tracking actief?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

TRACKING SCORE: ___/50 punten
```

### Section 2: Account Structure

```
STRUCTUUR AUDIT
===============

□ CAMPAIGN ORGANISATIE
├── Aantal actieve campaigns? (Ideaal: 3-10)
├── Logische campaign types mix (Search, PMax, Display)?
├── Duidelijke doelstellingen per campaign?
├── Geen overlappende campaigns?
├── Naming convention consistent?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ AD GROUP / ASSET GROUP STRUCTUUR
├── Aantal ad groups per campaign (Ideaal: 3-20)?
├── Thematisch georganiseerd?
├── Voldoende ads per ad group (3-5 RSAs)?
├── Keywords-to-ad alignment?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ PMAX STRUCTUUR (indien van toepassing)
├── Logische asset group segmentatie?
├── Producten correct ingedeeld via listing groups?
├── Audience signals per asset group?
├── Search themes toegevoegd?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ SHOPPING/MERCHANT CENTER (indien van toepassing)
├── Feed health status?
├── Disapprovals percentage (<5%)?
├── Custom labels in gebruik?
├── Product data quality score?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ NAMING CONVENTIONS
├── Consistent systeem aanwezig?
├── Bevat: Campaign type, target, date?
├── Eenvoudig te filteren en sorteren?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

STRUCTUUR SCORE: ___/50 punten
```

### Section 3: Keyword Strategy

```
KEYWORD AUDIT
=============

□ KEYWORD COVERAGE
├── Totaal aantal actieve keywords?
├── Brand vs non-brand verdeling?
├── Category coverage volledig?
├── Long-tail keywords aanwezig?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ MATCH TYPES
├── Match type verdeling (exact/phrase/broad)?
├── Broad match + Smart Bidding combinatie?
├── Geen conflicterende keywords?
├── Match type strategie consistent?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ NEGATIVE KEYWORDS
├── Account-level negatives aanwezig?
├── Campaign-level negatives ingesteld?
├── Negative keyword lists gebruikt?
├── Regelmatige search terms review?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ SEARCH TERMS ANALYSE
├── Search terms report recent bekeken?
├── Irrelevante termen ge-negatived?
├── Nieuwe keyword opportunities gevonden?
├── Wasted spend percentage (<15%)?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ QUALITY SCORE
├── Gemiddelde QS account-wide (>6)?
├── Keywords met QS <5 geïdentificeerd?
├── Expected CTR status?
├── Landing page experience status?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

KEYWORD SCORE: ___/50 punten
```

### Section 4: Ad Copy & Creative

```
CREATIVE AUDIT
==============

□ RSA (RESPONSIVE SEARCH ADS)
├── Minimaal 2 RSAs per ad group?
├── 8-15 unieke headlines per RSA?
├── 4 unieke descriptions per RSA?
├── Variatie in messaging angles?
├── Pinning strategisch gebruikt (niet overused)?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ AD STRENGTH
├── Percentage ads met "Excellent" strength?
├── "Poor" of "Average" ads geïdentificeerd?
├── Recommendations geïmplementeerd?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ AD EXTENSIONS/ASSETS
├── Sitelinks actief (4+ per campaign)?
├── Callouts aanwezig (4+)?
├── Structured snippets gebruikt?
├── Image extensions (indien eligible)?
├── Call extensions (indien relevant)?
├── Location extensions (indien lokaal)?
├── Price extensions (indien relevant)?
├── Promotion extensions (indien sale)?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ PMAX ASSETS (indien van toepassing)
├── Voldoende images (10+ per asset group)?
├── Video assets aanwezig?
├── Asset performance: hoeveel "Low" rating?
├── Regelmatige asset refresh?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ LANDING PAGES
├── Relevante landing pages per ad group?
├── Mobile-friendly?
├── Page speed acceptabel (<3s)?
├── Clear CTA aanwezig?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

CREATIVE SCORE: ___/50 punten
```

### Section 5: Bidding & Budget

```
BUDGET & BIDDING AUDIT
======================

□ BID STRATEGY
├── Welke bid strategies in gebruik?
├── Passend bij account maturity/data?
├── Learning phase status per campaign?
├── Geen "Limited" statussen?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ BID TARGETS
├── Target CPA/ROAS realistisch?
├── Targets gebaseerd op actuale data?
├── Regelmatige target evaluatie?
├── Niet te agressief (delivery stable)?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ BUDGET ALLOCATIE
├── Budget verdeeld over campaigns?
├── Top performers krijgen voldoende budget?
├── Geen "Limited by Budget" issues?
├── Daily vs shared budgets logisch?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ BUDGET EFFICIENCY
├── Spend vs budget ratio (>90%)?
├── Geen campaigns met extreme underspend?
├── Budget naar ROI-positive campaigns?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ PORTFOLIO STRATEGIES
├── Portfolio strategies waar logisch?
├── Voldoende data per portfolio?
├── Performance vs individual strategies?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

BUDGET SCORE: ___/50 punten
```

### Section 6: Audiences

```
AUDIENCE AUDIT
==============

□ FIRST-PARTY AUDIENCES
├── Remarketing lists actief?
├── Customer Match geüpload?
├── Website visitor lists (30/60/90/180 dagen)?
├── Converters list voor exclusions?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ PMAX AUDIENCE SIGNALS (indien van toepassing)
├── Custom segments geconfigureerd?
├── First-party data als signal?
├── In-market audiences toegevoegd?
├── Relevante affinity audiences?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ REMARKETING STRATEGY
├── RLSA actief op Search?
├── Display remarketing campagnes?
├── Membership duration logisch?
├── Frequency caps ingesteld?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ AUDIENCE EXCLUSIONS
├── Converters ge-excludeerd waar nodig?
├── Irrelevante audiences uitgesloten?
├── Employee/competitor exclusions?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

AUDIENCE SCORE: ___/40 punten
```

### Section 7: Performance Review

```
PERFORMANCE AUDIT
=================

□ KEY METRICS (vs benchmarks)
├── CTR: ___% (benchmark: 3-5% Search)
├── CPC: €___ (benchmark: varies)
├── CPA: €___ (target: €___)
├── ROAS: ___ (target: ___)
├── Conversion Rate: ___% (benchmark: 2-5%)
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ IMPRESSION SHARE
├── Search Impression Share: ___%
├── Search Lost IS (Budget): ___%
├── Search Lost IS (Rank): ___%
├── Absolute Top IS (Brand): ___%
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ TREND ANALYSIS (Last 30 vs Previous 30 days)
├── CPA trend: [↑ / → / ↓] (__%)
├── ROAS trend: [↑ / → / ↓] (__%)
├── Volume trend: [↑ / → / ↓] (__%)
├── Spend trend: [↑ / → / ↓] (__%)
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ CAMPAIGN PERFORMANCE
├── Best performing campaign: ___
├── Worst performing campaign: ___
├── Candidates for scaling: ___
├── Candidates for pause: ___
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ WASTED SPEND ANALYSIS
├── Low QS keywords spend: €___
├── Irrelevante search terms spend: €___
├── Non-converting placements spend: €___
├── Total waste estimate: €___
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

PERFORMANCE SCORE: ___/50 punten
```

### Section 8: Unused Feature Detection (NEW)

```
UNUSED FEATURES AUDIT
=====================
⚡ This section identifies money left on the table - features that are
   available but not being used, representing optimization opportunities.

□ PERFORMANCE MAX (E-commerce Not Using?)
├── E-commerce account with Shopping feed but no PMax?
│   └── Potential: 15-30% more conversions across channels
├── PMax active but no Search themes configured?
│   └── Missing: Search coverage control
├── PMax active but weak audience signals?
│   └── Missing: Faster learning, better targeting
├── Asset groups not segmented (all products in one)?
│   └── Missing: Granular optimization
└── Score: [🟢 Optimized / 🟡 Basic / 🔴 Not Using]

□ ENHANCED CONVERSIONS (Enabled but Low Match?)
├── Enhanced Conversions enabled but match rate <70%?
│   └── Missing: Full attribution value
├── Only email sent? Phone/address not included?
│   └── Missing: Additional match signals
├── Server-side implementation not done?
│   └── Missing: Best match rates (vs tag-only)
├── Consent Mode v2 not implemented?
│   └── Risk: EU compliance, data loss
└── Score: [🟢 OK / 🟡 Partial / 🔴 Not Optimized]

□ AUDIENCE ASSETS (Created but Not Used?)
├── Customer Match lists uploaded but not active?
│   └── Wasted: First-party data not leveraged
├── Remarketing lists exist but no RLSA campaigns?
│   └── Wasted: Warm audiences not being targeted
├── Website visitors list exists but no Display remarketing?
│   └── Missing: Cross-network retargeting
├── Similar audiences available but not used?
│   └── Missing: Expansion targeting
├── Customer list for exclusions not set up?
│   └── Waste: Paying for existing customer clicks
└── Score: [🟢 Using All / 🟡 Partial / 🔴 Many Unused]

□ AD EXTENSIONS/ASSETS (Not Enabled?)
├── Sitelink extensions missing?
│   └── Missing: ~10-15% CTR lift
├── Callout extensions missing?
│   └── Missing: USP communication
├── Structured snippets missing?
│   └── Missing: Additional info
├── Image extensions not enabled (eligible accounts)?
│   └── Missing: Visual differentiation
├── Call extensions (if phone conversions matter)?
│   └── Missing: Direct response channel
├── Location extensions (if local business)?
│   └── Missing: Local presence
├── Price extensions (if applicable)?
│   └── Missing: Price transparency
├── Promotion extensions (if sales active)?
│   └── Missing: Promotion visibility
└── Score: [🟢 Full / 🟡 Partial / 🔴 Missing Many]

□ AUTOMATION & RULES (Not Configured?)
├── No automated rules for basic management?
│   └── Missing: Proactive alerts, less manual work
├── No scripts for advanced automation?
│   └── Missing: Custom optimization opportunities
├── No portfolio bid strategies (multi-campaign)?
│   └── Missing: Unified optimization across campaigns
├── Conversion value rules not configured?
│   └── Missing: Value-based optimization accuracy
├── Scheduled bid adjustments not set?
│   └── Missing: Time-of-day optimization
└── Score: [🟢 Using / 🟡 Basic / 🔴 None]

□ DEMAND GEN & YOUTUBE (Not Tested?)
├── E-commerce/Lead Gen but no Demand Gen campaigns?
│   └── Missing: YouTube, Discover, Gmail reach
├── YouTube available but no Video campaigns?
│   └── Missing: Video advertising channel
├── YouTube remarketing not set up?
│   └── Missing: Video viewer retargeting
├── In-feed video ads not tested?
│   └── Missing: Discovery format
└── Score: [🟢 Using / 🟡 Tested / 🔴 None]

□ FEED OPTIMIZATION (Shopping/PMax)
├── Merchant Center promotions not used?
│   └── Missing: Promotional visibility
├── Custom labels not configured?
│   └── Missing: Granular bidding control
├── Product ratings not enabled?
│   └── Missing: Social proof in ads
├── Free listings not enabled?
│   └── Missing: Free organic traffic
├── Local inventory ads (if stores)?
│   └── Missing: O2O traffic
└── Score: [🟢 Optimized / 🟡 Basic / 🔴 Not Using]

□ MEASUREMENT TOOLS (Not Used?)
├── Experiments (A/B testing) not running?
│   └── Missing: Statistical testing framework
├── Bid simulator not reviewed?
│   └── Missing: Budget optimization insights
├── Recommendations review not regular?
│   └── Missing: Google's optimization suggestions
├── Attribution reports not analyzed?
│   └── Missing: Cross-channel journey insights
├── Auction insights not monitored?
│   └── Missing: Competitive intelligence
└── Score: [🟢 Using / 🟡 Basic / 🔴 None]

UNUSED FEATURES SCORE: ___/80 punten

⚠️ OPPORTUNITY COST ESTIMATE:
├── No PMax (e-commerce): ~15-30% fewer conversions
├── Low Enhanced Conversions adoption: ~10-20% attribution loss
├── Missing extensions: ~10-15% lower CTR
├── Unused audiences: ~15-25% efficiency loss
├── No automation: ~3-5 hours/week manual work
├── No Demand Gen/YouTube: ~20-40% of audience unreached
└── TOTAL ESTIMATED OPPORTUNITY: €___/month
```

## Health Score Calculator

### Score Berekening

```
ACCOUNT HEALTH SCORE
====================

SECTIE                    │ MAX PUNTEN │ JOUW SCORE
──────────────────────────┼────────────┼───────────
Tracking & Data Quality   │     50     │    ___
Account Structure         │     50     │    ___
Keyword Strategy          │     50     │    ___
Ad Copy & Creative        │     50     │    ___
Budget & Bidding          │     50     │    ___
Audiences                 │     40     │    ___
Performance Metrics       │     50     │    ___
Unused Features           │     80     │    ___    ← NEW
──────────────────────────┼────────────┼───────────
TOTAAL                    │    420     │    ___

PERCENTAGE: ___/420 × 100 = ___%

SCORE INTERPRETATIE:
├── 85-100%: 🟢 EXCELLENT - Minor tweaks only
├── 70-84%:  🟡 GOOD - Several improvements needed
├── 55-69%:  🟠 FAIR - Significant optimization required
├── 40-54%:  🔴 POOR - Major restructuring needed
└── <40%:    ⚫ CRITICAL - Fundamental rebuild required
```

### Scoring Guidelines

```
SUBSECTION SCORING GUIDE
========================

Per checkbox item:
├── 🟢 OK (volledig in orde): 10 punten
├── 🟡 Issues (deels in orde): 5 punten
└── 🔴 Kritiek (niet in orde): 0 punten

Voorbeeld berekening (Tracking sectie):
├── Conversion Actions: 🟢 = 10
├── Google Tag Status: 🟢 = 10
├── Enhanced Conversions: 🟡 = 5
├── Data Quality: 🟢 = 10
├── Offline Conversions: 🔴 = 0 (N/A voor e-commerce)
└── Totaal: 35/50

Adjust voor N/A items:
├── Als item niet van toepassing is
├── Haal af van max punten
└── Bereken percentage op aangepast totaal
```

## Issue Prioritization Matrix

```
ISSUE PRIORITERING
==================

🔴 KRITIEK (Fix binnen 24-48 uur):
─────────────────────────────────
• Conversion tracking niet werkend
• Geen conversies gemeten
• Budget limiet bereikt op top campaigns
• Policy violations/suspensions
• Tag errors/niet laden
• Major tracking discrepancies (>30%)

🟠 HOOG (Fix binnen 1 week):
────────────────────────────
• Enhanced Conversions niet actief
• >20% keywords met QS <5
• Learning phase >3 weken stuck
• CPA/ROAS >30% boven target
• Significant wasted spend (>15%)
• Missing ad extensions op major campaigns

🟡 MEDIUM (Fix binnen 2 weken):
───────────────────────────────
• Ad strength "Poor" of "Average"
• Naming conventions inconsistent
• Negative keywords incomplete
• Audience exclusions ontbreken
• Budget misallocation
• Outdated ad copy (>6 maanden)

🟢 LAAG (Fix binnen 1 maand):
─────────────────────────────
• Optimization opportunities
• Nice-to-have extensions
• Testing nieuwe strategies
• Documentation updates
• Advanced audience strategies
```

## Quick Audit (15 Minuten)

```
QUICK AUDIT CHECKLIST
=====================

Open Google Ads en check deze 10 items:

□ 1. Conversies laatste 7 dagen?
     └── Ja/Nee, hoeveel: ___

□ 2. Campaigns met "Limited" status?
     └── Ja/Nee, welke: ___

□ 3. Learning phase issues?
     └── # campaigns in learning: ___

□ 4. CPA/ROAS vs target?
     └── [Op target / Onder / Boven __%]

□ 5. Top campaign performance?
     └── Best: ___, Worst: ___

□ 6. Search Terms check (random sample)?
     └── Irrelevant termen: [Veel / Weinig]

□ 7. Ad Strength verdeling?
     └── Excellent: ___%, Poor: ___%

□ 8. Budget spend rate?
     └── [>90% / 70-90% / <70%]

□ 9. Impression Share (top campaign)?
     └── __%, Lost to budget: ___%

□ 10. Recent changes (Change History)?
      └── Door wie, wat: ___

QUICK SCORE: ___/10 items OK
├── 9-10: Account gezond, maandelijkse check
├── 7-8:  Aandachtspunten, plan actie
├── 5-6:  Issues aanwezig, prioriteer
└── <5:   Diepgaande audit nodig
```

## Google Ads Script: Account Health Monitor

```javascript
/**
 * Google Ads Account Health Monitor
 *
 * Voert wekelijkse health check uit en stuurt rapport.
 *
 * Setup:
 * 1. Pas EMAIL aan
 * 2. Pas THRESHOLDS aan naar je wensen
 * 3. Schedule wekelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Thresholds
  MIN_CTR: 0.02,           // 2% minimum CTR
  MAX_CPA_INCREASE: 0.25,  // 25% CPA increase = alert
  MIN_QUALITY_SCORE: 5,    // Quality Score minimum
  MIN_IMPRESSION_SHARE: 0.5, // 50% minimum IS
  MIN_AD_STRENGTH: 'GOOD'  // Minimum ad strength
};

function main() {
  var report = {
    date: new Date().toDateString(),
    accountName: AdsApp.currentAccount().getName(),
    issues: [],
    metrics: {},
    score: 0
  };

  // Run all checks
  checkConversions(report);
  checkCampaignStatus(report);
  checkKeywordQuality(report);
  checkAdStrength(report);
  checkImpressionShare(report);
  checkBudgetUtilization(report);

  // Calculate health score
  calculateHealthScore(report);

  // Send report
  sendHealthReport(report);

  Logger.log('Health check complete. Score: ' + report.score + '/100');
}

function checkConversions(report) {
  var stats = AdsApp.currentAccount().getStatsFor('LAST_7_DAYS');
  var conversions = stats.getConversions();
  var cost = stats.getCost();

  report.metrics.conversions7d = conversions;
  report.metrics.cost7d = cost;
  report.metrics.cpa7d = conversions > 0 ? cost / conversions : 0;

  // Compare to previous period
  var prevStats = AdsApp.currentAccount().getStatsFor('LAST_14_DAYS');
  var prevConv = prevStats.getConversions() - conversions;
  var prevCost = prevStats.getCost() - cost;
  var prevCPA = prevConv > 0 ? prevCost / prevConv : 0;

  if (prevCPA > 0 && report.metrics.cpa7d > 0) {
    var cpaChange = (report.metrics.cpa7d - prevCPA) / prevCPA;
    if (cpaChange > CONFIG.MAX_CPA_INCREASE) {
      report.issues.push({
        severity: 'HIGH',
        area: 'Performance',
        issue: 'CPA increased by ' + (cpaChange * 100).toFixed(1) + '%',
        action: 'Review bid strategies and targeting'
      });
    }
  }

  if (conversions === 0) {
    report.issues.push({
      severity: 'CRITICAL',
      area: 'Tracking',
      issue: 'Zero conversions in last 7 days',
      action: 'Verify conversion tracking immediately'
    });
  }
}

function checkCampaignStatus(report) {
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  var limitedCount = 0;
  var learningCount = 0;

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();

    // Check for Limited status (budget or bid)
    var stats = campaign.getStatsFor('LAST_7_DAYS');
    var impressions = stats.getImpressions();
    var budget = campaign.getBudget().getAmount();

    // Simple heuristic: if spend > 95% of budget, might be limited
    var spend = stats.getCost();
    var spendRatio = spend / (budget * 7);

    if (spendRatio > 0.95) {
      limitedCount++;
    }
  }

  if (limitedCount > 0) {
    report.issues.push({
      severity: 'MEDIUM',
      area: 'Budget',
      issue: limitedCount + ' campaign(s) may be limited by budget',
      action: 'Review budget allocation'
    });
  }

  report.metrics.limitedCampaigns = limitedCount;
}

function checkKeywordQuality(report) {
  var keywords = AdsApp.keywords()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignStatus = ENABLED')
    .withCondition('AdGroupStatus = ENABLED')
    .forDateRange('LAST_30_DAYS')
    .get();

  var totalKeywords = 0;
  var lowQSCount = 0;

  while (keywords.hasNext()) {
    var keyword = keywords.next();
    totalKeywords++;

    var qs = keyword.getQualityScore();
    if (qs && qs < CONFIG.MIN_QUALITY_SCORE) {
      lowQSCount++;
    }
  }

  report.metrics.totalKeywords = totalKeywords;
  report.metrics.lowQSKeywords = lowQSCount;

  var lowQSPercentage = totalKeywords > 0 ? lowQSCount / totalKeywords : 0;
  if (lowQSPercentage > 0.2) {
    report.issues.push({
      severity: 'MEDIUM',
      area: 'Keywords',
      issue: (lowQSPercentage * 100).toFixed(1) + '% of keywords have QS < 5',
      action: 'Improve ad relevance and landing pages'
    });
  }
}

function checkAdStrength(report) {
  var ads = AdsApp.ads()
    .withCondition('Type = RESPONSIVE_SEARCH_AD')
    .withCondition('Status = ENABLED')
    .get();

  var totalAds = 0;
  var poorAds = 0;

  while (ads.hasNext()) {
    var ad = ads.next();
    totalAds++;

    // Note: Ad strength not directly available via API
    // This is a placeholder - in practice use Reports API
  }

  report.metrics.totalAds = totalAds;
}

function checkImpressionShare(report) {
  // Use Search campaigns only
  var campaignIterator = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .withCondition('AdvertisingChannelType = SEARCH')
    .forDateRange('LAST_7_DAYS')
    .get();

  var totalIS = 0;
  var count = 0;

  while (campaignIterator.hasNext()) {
    var campaign = campaignIterator.next();
    var stats = campaign.getStatsFor('LAST_7_DAYS');
    // Note: IS not directly in stats, would need report
    count++;
  }

  report.metrics.searchCampaigns = count;
}

function checkBudgetUtilization(report) {
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .forDateRange('LAST_7_DAYS')
    .get();

  var totalBudget = 0;
  var totalSpend = 0;

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var budget = campaign.getBudget().getAmount() * 7; // Weekly
    var spend = campaign.getStatsFor('LAST_7_DAYS').getCost();

    totalBudget += budget;
    totalSpend += spend;
  }

  var utilization = totalBudget > 0 ? totalSpend / totalBudget : 0;
  report.metrics.budgetUtilization = utilization;

  if (utilization < 0.7) {
    report.issues.push({
      severity: 'LOW',
      area: 'Budget',
      issue: 'Budget utilization at ' + (utilization * 100).toFixed(1) + '%',
      action: 'Review targeting or increase bids'
    });
  }
}

function calculateHealthScore(report) {
  var score = 100;

  for (var i = 0; i < report.issues.length; i++) {
    var issue = report.issues[i];
    switch (issue.severity) {
      case 'CRITICAL': score -= 25; break;
      case 'HIGH': score -= 15; break;
      case 'MEDIUM': score -= 10; break;
      case 'LOW': score -= 5; break;
    }
  }

  report.score = Math.max(0, score);
}

function sendHealthReport(report) {
  var subject = '🏥 Account Health: ' + report.score + '/100 - ' + report.accountName;

  var body = 'GOOGLE ADS ACCOUNT HEALTH REPORT\n';
  body += '=================================\n\n';
  body += 'Account: ' + report.accountName + '\n';
  body += 'Date: ' + report.date + '\n';
  body += 'Health Score: ' + report.score + '/100\n\n';

  body += 'KEY METRICS (Last 7 Days)\n';
  body += '-------------------------\n';
  body += 'Conversions: ' + report.metrics.conversions7d + '\n';
  body += 'Cost: €' + report.metrics.cost7d.toFixed(2) + '\n';
  body += 'CPA: €' + report.metrics.cpa7d.toFixed(2) + '\n';
  body += 'Budget Utilization: ' + (report.metrics.budgetUtilization * 100).toFixed(1) + '%\n\n';

  if (report.issues.length > 0) {
    body += 'ISSUES FOUND (' + report.issues.length + ')\n';
    body += '-------------\n';

    for (var i = 0; i < report.issues.length; i++) {
      var issue = report.issues[i];
      body += '\n[' + issue.severity + '] ' + issue.area + '\n';
      body += 'Issue: ' + issue.issue + '\n';
      body += 'Action: ' + issue.action + '\n';
    }
  } else {
    body += '✓ No issues found!\n';
  }

  body += '\n---\nGenerated by Account Health Monitor';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Audit Report Template

```markdown
# Google Ads Account Audit Report

📅 **Audit Datum:** [DATUM]
🏢 **Account:** [ACCOUNT NAAM]
🆔 **Account ID:** [XXX-XXX-XXXX]
👤 **Auditor:** [NAAM]

---

## 📊 Executive Summary

### Health Score: [X]/340 ([X]%) - [STATUS]

**Sterke Punten:**
1. [Sterk punt met specifiek voorbeeld]
2. [Sterk punt met specifiek voorbeeld]
3. [Sterk punt met specifiek voorbeeld]

**Kritieke Issues:**
1. 🔴 [Issue met impact]
2. 🟠 [Issue met impact]
3. 🟡 [Issue met impact]

**Estimated Wasted Spend:** €[X]/maand
**Potential Improvement:** [X-Y]% CPA reduction / ROAS increase

---

## 📋 Gedetailleerde Bevindingen

### 1. Conversion Tracking & Data Quality
**Score:** [X]/50 - [🟢/🟡/🔴]

| Check Item | Status | Notes |
|------------|--------|-------|
| Conversion Actions | 🟢 | [Details] |
| Google Tag | 🟢 | [Details] |
| Enhanced Conversions | 🟡 | [Details] |
| Data Quality | 🟢 | [Details] |

**Issues:**
- [Issue 1]
- [Issue 2]

**Aanbevelingen:**
1. [Aanbeveling met priority]
2. [Aanbeveling met priority]

---

### 2. Account Structure
**Score:** [X]/50 - [🟢/🟡/🔴]

[Herhaal format voor elke sectie]

---

## 📋 Geprioriteerd Actieplan

### Week 1 (Kritiek)
- [ ] [Actie 1 met verantwoordelijke]
- [ ] [Actie 2 met verantwoordelijke]

### Week 2-3 (Hoog)
- [ ] [Actie 3]
- [ ] [Actie 4]

### Maand 1 (Medium)
- [ ] [Actie 5]
- [ ] [Actie 6]

### Ongoing (Laag)
- [ ] [Actie 7]
- [ ] [Actie 8]

---

## 📈 Verwachte Impact

Na implementatie van alle aanbevelingen:

| Metric | Huidig | Verwacht | Verbetering |
|--------|--------|----------|-------------|
| CPA | €[X] | €[Y] | -[Z]% |
| ROAS | [X] | [Y] | +[Z]% |
| Conv Rate | [X]% | [Y]% | +[Z]% |
| Wasted Spend | €[X] | €[Y] | -€[Z] |

---

## 🔄 Follow-Up

**Next Audit Recommended:** [DATUM]
**Review Meeting:** [DATUM + TIJD]
**Contact:** [EMAIL/PHONE]

---

*Rapport gegenereerd met Account Auditor Skill*
```

## Voorbeeld Interactie

**Gebruiker:** "Ik heb net een nieuw Google Ads account overgenomen. Kun je een audit doen?"

**Claude Response:**

Ik help je met een systematische account audit. Laten we beginnen met het verzamelen van basis info en dan een gestructureerde audit doorlopen.

---

**STAP 1: Basis Informatie**

Kun je me vertellen:
1. Account type: E-commerce of Lead Gen?
2. Maandelijks budget: €___
3. Huidige KPIs (CPA/ROAS targets)?
4. Hoe lang bestaat dit account?
5. Welke campaign types zijn actief (Search, PMax, Display)?

---

**STAP 2: Quick Health Check (5 minuten)**

Open Google Ads en check deze items:

□ **Conversies (laatste 7 dagen):** Hoeveel?
□ **Campaigns met warnings:** Zijn er "Limited" of "Learning" statussen?
□ **Tracking status:** Open Goals → Conversions - zijn er rode warnings?

---

**STAP 3: Deep Dive (na basis info)**

Op basis van je antwoorden loop ik de volledige audit checklist door:

1. Tracking & Data Quality
2. Account Structure
3. Keyword Strategy (Search)
4. Ad Copy & Creative
5. Bidding & Budget
6. Audiences
7. Performance Metrics

Deel de basis info en ik start de gedetailleerde audit met health score en actieplan!

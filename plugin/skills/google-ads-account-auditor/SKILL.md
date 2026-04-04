---
name: google-ads-account-auditor
description: |
  Performs complete Google Ads account audits with health scoring and actionable recommendations. Use when: account takeover, periodic review, performance diagnosis, optimization opportunity identification, quick health check. Do NOT use for: single campaign troubleshooting (use performance-troubleshooter), keyword-only analysis (use keyword-strategy-planner).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "google_ads"
  phase: "fase-5-advanced"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---
# Account Auditor

Systematic framework for performing complete Google Ads account audits, including health scoring, issue identification, and prioritized recommendations.

## Audit Framework

### Audit Scope Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  GOOGLE ADS ACCOUNT AUDIT AREAS                                  │
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
├── Which conversion actions are active?
├── Correctly configured as Primary vs Secondary?
├── Correct counting method (One/Every)?
├── Attribution model: Data-driven active?
└── Score: [OK / Issues / Critical]

□ GOOGLE TAG STATUS
├── Tag installed on all pages?
├── No duplicate tags?
├── Tag fires correctly on conversions?
├── Values being sent correctly?
└── Score: [OK / Issues / Critical]

□ ENHANCED CONVERSIONS
├── Enhanced Conversions enabled?
├── User data being sent (email, phone)?
├── Match rate acceptable (>70%)?
├── Consent Mode v2 implemented?
└── Score: [OK / Issues / Critical]

□ DATA QUALITY
├── Conversion rate realistic vs industry?
├── Values match backend/GA4?
├── No duplicate conversions?
├── Conversion lag acceptable (<24h)?
└── Score: [OK / Issues / Critical]

□ OFFLINE CONVERSIONS (Lead Gen)
├── Are offline conversions being imported?
├── Import frequency sufficient (weekly min)?
├── Lead-to-Sale tracking active?
└── Score: [OK / Issues / Critical]

TRACKING SCORE: ___/50 points
```

### Section 2: Account Structure

```
STRUCTURE AUDIT
===============

□ CAMPAIGN ORGANIZATION
├── Number of active campaigns? (Ideal: 3-10)
├── Logical campaign types mix (Search, PMax, Display)?
├── Clear objectives per campaign?
├── No overlapping campaigns?
├── Naming convention consistent?
└── Score: [OK / Issues / Critical]

□ AD GROUP / ASSET GROUP STRUCTURE
├── Number of ad groups per campaign (Ideal: 3-20)?
├── Thematically organized?
├── Sufficient ads per ad group (3-5 RSAs)?
├── Keywords-to-ad alignment?
└── Score: [OK / Issues / Critical]

□ PMAX STRUCTURE (if applicable)
├── Logical asset group segmentation?
├── Products correctly assigned via listing groups?
├── Audience signals per asset group?
├── Search themes added?
└── Score: [OK / Issues / Critical]

□ SHOPPING/MERCHANT CENTER (if applicable)
├── Feed health status?
├── Disapprovals percentage (<5%)?
├── Custom labels in use?
├── Product data quality score?
└── Score: [OK / Issues / Critical]

□ NAMING CONVENTIONS
├── Consistent system in place?
├── Contains: Campaign type, target, date?
├── Easy to filter and sort?
└── Score: [OK / Issues / Critical]

STRUCTURE SCORE: ___/50 points
```

### Section 3: Keyword Strategy

```
KEYWORD AUDIT
=============

□ KEYWORD COVERAGE
├── Total number of active keywords?
├── Brand vs non-brand distribution?
├── Category coverage complete?
├── Long-tail keywords present?
└── Score: [OK / Issues / Critical]

□ MATCH TYPES
├── Match type distribution (exact/phrase/broad)?
├── Broad match + Smart Bidding combination?
├── No conflicting keywords?
├── Match type strategy consistent?
└── Score: [OK / Issues / Critical]

□ NEGATIVE KEYWORDS
├── Account-level negatives present?
├── Campaign-level negatives configured?
├── Negative keyword lists used?
├── Regular search terms review?
└── Score: [OK / Issues / Critical]

□ SEARCH TERMS ANALYSIS
├── Search terms report recently reviewed?
├── Irrelevant terms added as negatives?
├── New keyword opportunities found?
├── Wasted spend percentage (<15%)?
└── Score: [OK / Issues / Critical]

□ QUALITY SCORE
├── Average QS account-wide (>6)?
├── Keywords with QS <5 identified?
├── Expected CTR status?
├── Landing page experience status?
└── Score: [OK / Issues / Critical]

KEYWORD SCORE: ___/50 points
```

### Section 4: Ad Copy & Creative

```
CREATIVE AUDIT
==============

□ RSA (RESPONSIVE SEARCH ADS)
├── At least 2 RSAs per ad group?
├── 8-15 unique headlines per RSA?
├── 4 unique descriptions per RSA?
├── Variation in messaging angles?
├── Pinning used strategically (not overused)?
└── Score: [OK / Issues / Critical]

□ AD STRENGTH
├── Percentage of ads with "Excellent" strength?
├── "Poor" or "Average" ads identified?
├── Recommendations implemented?
└── Score: [OK / Issues / Critical]

□ AD EXTENSIONS/ASSETS
├── Sitelinks active (4+ per campaign)?
├── Callouts present (4+)?
├── Structured snippets used?
├── Image extensions (if eligible)?
├── Call extensions (if relevant)?
├── Location extensions (if local)?
├── Price extensions (if relevant)?
├── Promotion extensions (if sale)?
└── Score: [OK / Issues / Critical]

□ PMAX ASSETS (if applicable)
├── Sufficient images (10+ per asset group)?
├── Video assets present?
├── Asset performance: how many "Low" rating?
├── Regular asset refresh?
└── Score: [OK / Issues / Critical]

□ LANDING PAGES
├── Relevant landing pages per ad group?
├── Mobile-friendly?
├── Page speed acceptable (<3s)?
├── Clear CTA present?
└── Score: [OK / Issues / Critical]

CREATIVE SCORE: ___/50 points
```

### Section 5: Bidding & Budget

```
BUDGET & BIDDING AUDIT
======================

□ BID STRATEGY
├── Which bid strategies are in use?
├── Appropriate for account maturity/data?
├── Learning phase status per campaign?
├── No "Limited" statuses?
└── Score: [OK / Issues / Critical]

□ BID TARGETS
├── Target CPA/ROAS realistic?
├── Targets based on actual data?
├── Regular target evaluation?
├── Not too aggressive (delivery stable)?
└── Score: [OK / Issues / Critical]

□ BUDGET ALLOCATION
├── Budget distributed across campaigns?
├── Top performers getting sufficient budget?
├── No "Limited by Budget" issues?
├── Daily vs shared budgets logical?
└── Score: [OK / Issues / Critical]

□ BUDGET EFFICIENCY
├── Spend vs budget ratio (>90%)?
├── No campaigns with extreme underspend?
├── Budget directed to ROI-positive campaigns?
└── Score: [OK / Issues / Critical]

□ PORTFOLIO STRATEGIES
├── Portfolio strategies where logical?
├── Sufficient data per portfolio?
├── Performance vs individual strategies?
└── Score: [OK / Issues / Critical]

BUDGET SCORE: ___/50 points
```

### Section 6: Audiences

```
AUDIENCE AUDIT
==============

□ FIRST-PARTY AUDIENCES
├── Remarketing lists active?
├── Customer Match uploaded?
├── Website visitor lists (30/60/90/180 days)?
├── Converters list for exclusions?
└── Score: [OK / Issues / Critical]

□ PMAX AUDIENCE SIGNALS (if applicable)
├── Custom segments configured?
├── First-party data as signal?
├── In-market audiences added?
├── Relevant affinity audiences?
└── Score: [OK / Issues / Critical]

□ REMARKETING STRATEGY
├── RLSA active on Search?
├── Display remarketing campaigns?
├── Membership duration logical?
├── Frequency caps set?
└── Score: [OK / Issues / Critical]

□ AUDIENCE EXCLUSIONS
├── Converters excluded where needed?
├── Irrelevant audiences excluded?
├── Employee/competitor exclusions?
└── Score: [OK / Issues / Critical]

AUDIENCE SCORE: ___/40 points
```

### Section 7: Performance Review

```
PERFORMANCE AUDIT
=================

□ KEY METRICS (vs benchmarks)
├── CTR: ___% (benchmark: 3-5% Search)
├── CPC: ___  (benchmark: varies)
├── CPA: ___  (target: ___)
├── ROAS: ___ (target: ___)
├── Conversion Rate: ___% (benchmark: 2-5%)
└── Score: [OK / Issues / Critical]

□ IMPRESSION SHARE
├── Search Impression Share: ___%
├── Search Lost IS (Budget): ___%
├── Search Lost IS (Rank): ___%
├── Absolute Top IS (Brand): ___%
└── Score: [OK / Issues / Critical]

□ TREND ANALYSIS (Last 30 vs Previous 30 days)
├── CPA trend: [up / flat / down] (__%)
├── ROAS trend: [up / flat / down] (__%)
├── Volume trend: [up / flat / down] (__%)
├── Spend trend: [up / flat / down] (__%)
└── Score: [OK / Issues / Critical]

□ CAMPAIGN PERFORMANCE
├── Best performing campaign: ___
├── Worst performing campaign: ___
├── Candidates for scaling: ___
├── Candidates for pause: ___
└── Score: [OK / Issues / Critical]

□ WASTED SPEND ANALYSIS
├── Low QS keywords spend: ___
├── Irrelevant search terms spend: ___
├── Non-converting placements spend: ___
├── Total waste estimate: ___
└── Score: [OK / Issues / Critical]

PERFORMANCE SCORE: ___/50 points
```

### Section 8: Unused Feature Detection (NEW)

```
UNUSED FEATURES AUDIT
=====================
This section identifies money left on the table - features that are
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
└── Score: [Optimized / Basic / Not Using]

□ ENHANCED CONVERSIONS (Enabled but Low Match?)
├── Enhanced Conversions enabled but match rate <70%?
│   └── Missing: Full attribution value
├── Only email sent? Phone/address not included?
│   └── Missing: Additional match signals
├── Server-side implementation not done?
│   └── Missing: Best match rates (vs tag-only)
├── Consent Mode v2 not implemented?
│   └── Risk: EU compliance, data loss
└── Score: [OK / Partial / Not Optimized]

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
└── Score: [Using All / Partial / Many Unused]

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
└── Score: [Full / Partial / Missing Many]

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
└── Score: [Using / Basic / None]

□ DEMAND GEN & YOUTUBE (Not Tested?)
├── E-commerce/Lead Gen but no Demand Gen campaigns?
│   └── Missing: YouTube, Discover, Gmail reach
├── YouTube available but no Video campaigns?
│   └── Missing: Video advertising channel
├── YouTube remarketing not set up?
│   └── Missing: Video viewer retargeting
├── In-feed video ads not tested?
│   └── Missing: Discovery format
└── Score: [Using / Tested / None]

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
└── Score: [Optimized / Basic / Not Using]

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
└── Score: [Using / Basic / None]

UNUSED FEATURES SCORE: ___/80 points

OPPORTUNITY COST ESTIMATE:
├── No PMax (e-commerce): ~15-30% fewer conversions
├── Low Enhanced Conversions adoption: ~10-20% attribution loss
├── Missing extensions: ~10-15% lower CTR
├── Unused audiences: ~15-25% efficiency loss
├── No automation: ~3-5 hours/week manual work
├── No Demand Gen/YouTube: ~20-40% of audience unreached
└── TOTAL ESTIMATED OPPORTUNITY: ___/month
```

## Health Score Calculator

### Score Calculation

```
ACCOUNT HEALTH SCORE
====================

SECTION                   │ MAX POINTS │ YOUR SCORE
──────────────────────────┼────────────┼───────────
Tracking & Data Quality   │     50     │    ___
Account Structure         │     50     │    ___
Keyword Strategy          │     50     │    ___
Ad Copy & Creative        │     50     │    ___
Budget & Bidding          │     50     │    ___
Audiences                 │     40     │    ___
Performance Metrics       │     50     │    ___
Unused Features           │     80     │    ___    <- NEW
──────────────────────────┼────────────┼───────────
TOTAL                     │    420     │    ___

PERCENTAGE: ___/420 x 100 = ___%

SCORE INTERPRETATION:
├── 85-100%: EXCELLENT - Minor tweaks only
├── 70-84%:  GOOD - Several improvements needed
├── 55-69%:  FAIR - Significant optimization required
├── 40-54%:  POOR - Major restructuring needed
└── <40%:    CRITICAL - Fundamental rebuild required
```

### Scoring Guidelines

```
SUBSECTION SCORING GUIDE
========================

Per checkbox item:
├── OK (fully in order): 10 points
├── Issues (partially in order): 5 points
└── Critical (not in order): 0 points

Example calculation (Tracking section):
├── Conversion Actions: OK = 10
├── Google Tag Status: OK = 10
├── Enhanced Conversions: Issues = 5
├── Data Quality: OK = 10
├── Offline Conversions: Critical = 0 (N/A for e-commerce)
└── Total: 35/50

Adjust for N/A items:
├── If item is not applicable
├── Subtract from max points
└── Calculate percentage on adjusted total
```

## Issue Prioritization Matrix

```
ISSUE PRIORITIZATION
====================

CRITICAL (Fix within 24-48 hours):
───────────────────────────────────
- Conversion tracking not working
- No conversions being measured
- Budget limit reached on top campaigns
- Policy violations/suspensions
- Tag errors/not loading
- Major tracking discrepancies (>30%)

HIGH (Fix within 1 week):
─────────────────────────
- Enhanced Conversions not active
- >20% keywords with QS <5
- Learning phase stuck >3 weeks
- CPA/ROAS >30% above target
- Significant wasted spend (>15%)
- Missing ad extensions on major campaigns

MEDIUM (Fix within 2 weeks):
────────────────────────────
- Ad strength "Poor" or "Average"
- Naming conventions inconsistent
- Negative keywords incomplete
- Audience exclusions missing
- Budget misallocation
- Outdated ad copy (>6 months)

LOW (Fix within 1 month):
─────────────────────────
- Optimization opportunities
- Nice-to-have extensions
- Testing new strategies
- Documentation updates
- Advanced audience strategies
```

## Quick Audit (15 Minutes)

```
QUICK AUDIT CHECKLIST
=====================

Open Google Ads and check these 10 items:

□ 1. Conversions in last 7 days?
     └── Yes/No, how many: ___

□ 2. Campaigns with "Limited" status?
     └── Yes/No, which ones: ___

□ 3. Learning phase issues?
     └── # campaigns in learning: ___

□ 4. CPA/ROAS vs target?
     └── [On target / Below / Above __%]

□ 5. Top campaign performance?
     └── Best: ___, Worst: ___

□ 6. Search Terms check (random sample)?
     └── Irrelevant terms: [Many / Few]

□ 7. Ad Strength distribution?
     └── Excellent: ___%, Poor: ___%

□ 8. Budget spend rate?
     └── [>90% / 70-90% / <70%]

□ 9. Impression Share (top campaign)?
     └── __%, Lost to budget: ___%

□ 10. Recent changes (Change History)?
      └── By whom, what: ___

QUICK SCORE: ___/10 items OK
├── 9-10: Account healthy, monthly check
├── 7-8:  Attention points, plan action
├── 5-6:  Issues present, prioritize
└── <5:   In-depth audit needed
```

## Google Ads Script: Account Health Monitor

```javascript
/**
 * Google Ads Account Health Monitor
 *
 * Runs weekly health check and sends report.
 *
 * Setup:
 * 1. Update EMAIL
 * 2. Adjust THRESHOLDS to your preferences
 * 3. Schedule weekly
 */

var CONFIG = {
  EMAIL: 'your@email.com',

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
  var subject = 'Account Health: ' + report.score + '/100 - ' + report.accountName;

  var body = 'GOOGLE ADS ACCOUNT HEALTH REPORT\n';
  body += '=================================\n\n';
  body += 'Account: ' + report.accountName + '\n';
  body += 'Date: ' + report.date + '\n';
  body += 'Health Score: ' + report.score + '/100\n\n';

  body += 'KEY METRICS (Last 7 Days)\n';
  body += '-------------------------\n';
  body += 'Conversions: ' + report.metrics.conversions7d + '\n';
  body += 'Cost: ' + report.metrics.cost7d.toFixed(2) + '\n';
  body += 'CPA: ' + report.metrics.cpa7d.toFixed(2) + '\n';
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
    body += 'No issues found!\n';
  }

  body += '\n---\nGenerated by Account Health Monitor';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Audit Report Template

```markdown
# Google Ads Account Audit Report

**Audit Date:** [DATE]
**Account:** [ACCOUNT NAME]
**Account ID:** [XXX-XXX-XXXX]
**Auditor:** [NAME]

---

## Executive Summary

### Health Score: [X]/340 ([X]%) - [STATUS]

**Strengths:**
1. [Strength with specific example]
2. [Strength with specific example]
3. [Strength with specific example]

**Critical Issues:**
1. [Critical] [Issue with impact]
2. [High] [Issue with impact]
3. [Medium] [Issue with impact]

**Estimated Wasted Spend:** [X]/month
**Potential Improvement:** [X-Y]% CPA reduction / ROAS increase

---

## Detailed Findings

### 1. Conversion Tracking & Data Quality
**Score:** [X]/50

| Check Item | Status | Notes |
|------------|--------|-------|
| Conversion Actions | OK | [Details] |
| Google Tag | OK | [Details] |
| Enhanced Conversions | Issues | [Details] |
| Data Quality | OK | [Details] |

**Issues:**
- [Issue 1]
- [Issue 2]

**Recommendations:**
1. [Recommendation with priority]
2. [Recommendation with priority]

---

### 2. Account Structure
**Score:** [X]/50

[Repeat format for each section]

---

## Prioritized Action Plan

### Week 1 (Critical)
- [ ] [Action 1 with responsible party]
- [ ] [Action 2 with responsible party]

### Week 2-3 (High)
- [ ] [Action 3]
- [ ] [Action 4]

### Month 1 (Medium)
- [ ] [Action 5]
- [ ] [Action 6]

### Ongoing (Low)
- [ ] [Action 7]
- [ ] [Action 8]

---

## Expected Impact

After implementing all recommendations:

| Metric | Current | Expected | Improvement |
|--------|---------|----------|-------------|
| CPA | [X] | [Y] | -[Z]% |
| ROAS | [X] | [Y] | +[Z]% |
| Conv Rate | [X]% | [Y]% | +[Z]% |
| Wasted Spend | [X] | [Y] | -[Z] |

---

## Follow-Up

**Next Audit Recommended:** [DATE]
**Review Meeting:** [DATE + TIME]
**Contact:** [EMAIL/PHONE]

---

*Report generated with Account Auditor Skill*
```

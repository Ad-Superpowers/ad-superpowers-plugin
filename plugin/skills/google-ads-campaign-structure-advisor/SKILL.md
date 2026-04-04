---
name: campaign-structure-advisor
description: |
  Google Ads Campaign Structure advisor for optimal account organization. Use when: restructuring or consolidating accounts, selecting campaign types, organizing ad groups, migrating from SKAGs to modern structure, or optimizing for Smart Bidding. Do NOT use for: bid strategy selection (use bid-strategy-selector), keyword strategy (use keyword-strategy-planner), or performance diagnosis (use performance-troubleshooter).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "google_ads"
  phase: "fase-4-measurement-attribution"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---
# Campaign Structure Advisor

Complete guide for structuring and optimizing Google Ads accounts with focus on modern, Smart Bidding-optimized architectures.
## Modern Account Structure

### Fundamental Principles

```
MODERN GOOGLE ADS STRUCTURE PRINCIPLES
═══════════════════════════════════════

PRINCIPLE 1: CONSOLIDATION OVER FRAGMENTATION
──────────────────────────────────────────────
OLD: Many small campaigns with little data
NEW: Fewer campaigns with more conversions

Why:
├── Smart Bidding learns faster with more data
├── Less management overhead
├── Better budget allocation
└── Faster Learning Phase

PRINCIPLE 2: MACHINE LEARNING FIRST
────────────────────────────────────
OLD: Manual bids, exact match focus
NEW: Smart Bidding, broad match allowed

Why:
├── Google's AI sees signals you can't
├── Real-time bid optimization per auction
├── Broad match + Smart Bidding = powerful combo
└── Focus on strategy, not tactics

PRINCIPLE 3: THEME-BASED AD GROUPS
───────────────────────────────────
OLD: SKAG (Single Keyword Ad Groups)
NEW: STAG (Single Theme Ad Groups)

Why:
├── Enough variation for AI to learn
├── Ads still relevant
├── Manageable scale
└── Flexible for query expansion

PRINCIPLE 4: BUDGET = BUSINESS CONSTRAINT
─────────────────────────────────────────
Separate campaigns only for:
├── Different budget pools
├── Different geographic targets
├── Different business units/products
├── Different performance targets (CPA/ROAS)
└── Regulatory/compliance requirements
```

### Ideal Account Structure

```
RECOMMENDED ACCOUNT ARCHITECTURE
═════════════════════════════════

E-COMMERCE STRUCTURE:
─────────────────────
Account
├── Campaign 1: Brand Search
│   ├── Budget: 10-15% of total
│   ├── Bidding: Max Conversions or tCPA
│   ├── Keywords: Branded terms (exact/phrase)
│   └── Purpose: Capture branded intent
│
├── Campaign 2: Performance Max
│   ├── Budget: 40-50% of total
│   ├── Bidding: Max Conv Value + tROAS
│   ├── Asset Groups: By product category
│   └── Purpose: Full-funnel automation
│
├── Campaign 3: Non-Brand Search
│   ├── Budget: 30-40% of total
│   ├── Bidding: tCPA or tROAS
│   ├── Ad Groups: By product theme/intent
│   └── Purpose: High-intent traffic
│
└── Campaign 4: Display Remarketing (optional)
    ├── Budget: 5-10% of total
    ├── Bidding: tCPA
    └── Purpose: Re-engage visitors

LEAD GEN STRUCTURE:
───────────────────
Account
├── Campaign 1: Brand Search
│   ├── Budget: 10-15%
│   └── Low CPA, high conversion rate
│
├── Campaign 2: High-Intent Non-Brand
│   ├── Budget: 50-60%
│   ├── Keywords: [service] + [action terms]
│   └── Focus: Qualified leads
│
├── Campaign 3: Consideration/Research
│   ├── Budget: 20-25%
│   ├── Keywords: [service] + [question terms]
│   └── Focus: Top-funnel leads
│
└── Campaign 4: Performance Max (optional)
    ├── Budget: 10-15%
    └── Broader reach
```

### Ad Group Organization

```
AD GROUP BEST PRACTICES
═══════════════════════

STAG (Single Theme Ad Groups):
──────────────────────────────
= Keywords with the same intent grouped together

EXAMPLE - Product Theme:
Ad Group: "Running Shoes"
├── running shoes
├── buy running shoes
├── best running shoes
├── running sneakers
├── running shoes online
└── trail running shoes

GUIDELINES:
───────────
□ 10-20 keywords per ad group
□ All keywords same intent/theme
□ Same landing page
□ 2-3 RSAs per ad group
□ Specific ad copy for theme

MATCH TYPE STRATEGY (Modern):
─────────────────────────────
Recommended with Smart Bidding:
├── Broad Match: 40-60% (with good negatives)
├── Phrase Match: 30-40%
└── Exact Match: 10-20% (top performers)

Legacy accounts:
├── Start with phrase/exact
├── Add broad with monitoring
├── Expand based on search term performance

NEGATIVES ARE CRUCIAL:
──────────────────────
With broad match:
□ Account-level negative list
□ Campaign-level specifics
□ Weekly search term review
□ Proactive negatives (irrelevant terms)
```

## Campaign Consolidation

### When to Consolidate

```
CONSOLIDATION ASSESSMENT
════════════════════════

CONSOLIDATE WHEN:
─────────────────

✓ CONVERSION VOLUME TOO LOW
  └── <50 conversions per campaign per month
  └── Smart Bidding in "Learning Limited"

✓ OVERLAPPING KEYWORDS
  └── Same keywords in multiple campaigns
  └── Internal competition
  └── Fragmented data

✓ SAME TARGETS
  └── Campaigns with identical CPA/ROAS targets
  └── No reason for separation

✓ FRAGMENTED BUDGET
  └── Small budgets spread across many campaigns
  └── No single campaign has enough for learning

✓ MANAGEMENT OVERHEAD
  └── Too much time on small campaigns
  └── Difficult to optimize

KEEP SEPARATE CAMPAIGNS WHEN:
─────────────────────────────

✗ DIFFERENT BUDGETS
  └── Separate funding pools
  └── Client/business unit separation

✗ DIFFERENT GEO TARGETS
  └── Different countries
  └── Different languages
  └── Different bid landscapes

✗ SIGNIFICANTLY DIFFERENT TARGETS
  └── Brand vs Non-brand (often different CPA)
  └── High-value vs Volume
  └── Different margins

✗ COMPLIANCE/ORGANIZATIONAL
  └── Regulatory requirements
  └── Reporting requirements
  └── Organizational structure
```

### Consolidation Strategy

```
CONSOLIDATION STEP-BY-STEP PLAN
════════════════════════════════

PHASE 1: ANALYSIS (Week 1)
───────────────────────────
□ Export all campaign data (30/90 days)
□ Identify campaigns for consolidation
□ Map keyword overlap
□ Document current performance baselines
□ Plan new structure

Consolidation candidates:
┌─────────────────────────────────────────────────────────┐
│ Campaign          │ Conv/month │ CPA    │ Overlap? │ ?  │
├───────────────────┼────────────┼────────┼──────────┼────┤
│ Product A Search  │ 15         │ €45    │ Yes      │ ✓  │
│ Product B Search  │ 22         │ €48    │ Yes      │ ✓  │
│ Brand Search      │ 150        │ €12    │ No       │ ✗  │
│ Display Retarget  │ 35         │ €28    │ No       │ ✗  │
└───────────────────┴────────────┴────────┴──────────┴────┘

PHASE 2: BUILD NEW STRUCTURE (Week 2)
─────────────────────────────────────
□ Create new consolidated campaigns
□ Import/reorganize keywords
□ Create new ad groups (themed)
□ Write new RSAs
□ Setup extensions
□ Configure bid strategy
□ TEST: Verify setup

New structure example:
├── [Old] Product A Search →
├── [Old] Product B Search → [New] Products Search (combined)
└── [Old] Product C Search →

PHASE 3: MIGRATION (Week 3)
────────────────────────────
Option A: Hard switch
├── Pause old campaigns
├── Enable new campaigns
└── Monitor intensively

Option B: Soft transition (recommended)
├── Reduce old budgets by 50%
├── Enable new with 50% budget
├── Shift gradually over 7-14 days
└── Pause old when new is stable

PHASE 4: OPTIMIZATION (Week 4+)
────────────────────────────────
□ Monitor Learning Phase
□ Adjust targets if needed
□ Optimize negatives
□ Review search terms
□ Fine-tune ad copy
```

### Portfolio Bid Strategies

```
PORTFOLIO BID STRATEGIES
════════════════════════

WHAT: One bid strategy across multiple campaigns

WHEN TO USE:
────────────
✓ Campaigns too small for individual learning
✓ Same business objective
✓ Want centralized bid management
✓ Want to aggregate data

SETUP:
──────
Tools → Shared Library → Bid Strategies → +

PORTFOLIO OPTIONS:
──────────────────
1. Target CPA Portfolio
   └── Multiple lead gen campaigns
   └── Same CPA target

2. Target ROAS Portfolio
   └── Multiple e-commerce campaigns
   └── Same margin target

3. Maximize Conversions Portfolio
   └── New/small campaigns
   └── Data aggregation for learning

EXAMPLE SETUP:
──────────────
Portfolio: "Non-Brand Search - tCPA €50"
├── Campaign: Generic Keywords
├── Campaign: Competitor Keywords
├── Campaign: Long-tail Keywords
└── Shared target: €50 CPA

ADVANTAGES:
├── Aggregated learning
├── Faster learning phase
├── Centralized management
├── Budget flexibility

DISADVANTAGES:
├── Less granular control
├── Shared targets not always optimal
├── Reporting more complex
└── Suboptimal if campaigns are very different
```

## SKAG to Modern Migration

### SKAG Problems

```
WHY SKAG NO LONGER WORKS
═════════════════════════

SKAG = Single Keyword Ad Groups
= One keyword per ad group (exact match)

WHY IT WAS POPULAR:
├── Maximum keyword-ad relevance
├── Perfect Quality Score
├── Granular bid control
└── Pre-Smart Bidding logic

WHY IT DOESN'T WORK NOW:
─────────────────────────

1. SMART BIDDING NEEDS DATA
   ├── SKAG = few conversions per ad group
   ├── AI can't learn from small samples
   └── "Learning Limited" everywhere

2. CLOSE VARIANTS MAKE IT POINTLESS
   ├── [running shoes] also triggers "sneakers running"
   ├── Exact match is no longer exact
   └── SKAG advantage gone

3. MANAGEMENT NIGHTMARE
   ├── Thousands of ad groups
   ├── Difficult to optimize
   ├── RSA needs headroom that isn't there
   └── Time better spent elsewhere

4. BROAD MATCH + SMART BIDDING IS BETTER
   ├── AI selects best queries
   ├── More reach
   ├── Automatic query expansion
   └── Focus on outcomes, not structure
```

### Migration Strategy

```
SKAG → MODERN MIGRATION
════════════════════════

STEP 1: INVENTORY
─────────────────
□ Export all SKAGs
□ Group keywords by theme/intent
□ Identify top performers (preserve intent)
□ Note best performing ad copy

Grouping example:
SKAGs:
├── [running shoes]
├── [running shoes men]
├── [best running shoes]
├── [buy running shoes]
└── [running shoes sale]

→ New Ad Group: "Running Shoes"
  (all above + variations)

STEP 2: DEFINE NEW STRUCTURE
────────────────────────────
From: 500 SKAGs
To: 30-50 themed ad groups in 3-5 campaigns

Rules of thumb:
├── Max 5-10 ad groups per campaign
├── Max 20 keywords per ad group
├── Min 50 conv/campaign/month target
└── Themed groupings

STEP 3: AD COPY CONSOLIDATION
──────────────────────────────
From: 500 exact-match ads
To: 100-150 RSAs with variation

Per ad group:
├── 2-3 RSAs
├── Use best performers as base
├── Vary headlines/descriptions
└── Use keyword insertion where logical

STEP 4: MIGRATION EXECUTION
────────────────────────────
Week 1:
├── Build new campaigns alongside SKAG
├── Mirror best keywords and ads
├── Setup bid strategy (start conservative)
└── Enable with 20% budget

Week 2:
├── Monitor new campaigns
├── Shift budget: 50% new, 50% SKAG
├── Check search terms
└── Add negatives

Week 3:
├── If stable: 80% new, 20% SKAG
├── Pause low performers in SKAG
└── Continue monitoring

Week 4:
├── Pause all SKAG campaigns
├── 100% on new structure
├── Delete/archive old campaigns
└── Full optimization mode

STEP 5: POST-MIGRATION
───────────────────────
□ Monitor Learning Phase (2-4 weeks)
□ Optimize bid targets
□ Expand with broad match (gradually)
□ Continue negative keyword management
□ Document learnings
```

## Enterprise Account Structure

### Multi-Product/Region Accounts

```
ENTERPRISE ACCOUNT ARCHITECTURE
════════════════════════════════

ORGANIZATION PRINCIPLES:
────────────────────────

1. CAMPAIGN = BUDGET ALLOCATION UNIT
   └── Separate campaigns for separate budgets
   └── Not: Separate campaigns for organization

2. LABELS = ORGANIZATION
   └── Product lines
   └── Teams/ownership
   └── Initiatives
   └── Reporting groups

3. MCC FOR TRUE SEPARATION
   └── Different business units
   └── Different billing
   └── Compliance requirements

STRUCTURE EXAMPLE:
──────────────────

Large E-commerce (3 product lines, 2 regions):

Account
├── Campaign: NL - Brand Search
│   ├── Labels: [Netherlands] [Brand]
│   └── All product lines (shared brand)
│
├── Campaign: NL - Electronics Search
│   ├── Labels: [Netherlands] [Electronics] [Non-Brand]
│   ├── Ad Groups: TVs, Laptops, Phones
│   └── Bidding: tROAS 400%
│
├── Campaign: NL - Home & Living Search
│   ├── Labels: [Netherlands] [Home] [Non-Brand]
│   ├── Ad Groups: Furniture, Decor, Kitchen
│   └── Bidding: tROAS 350%
│
├── Campaign: NL - Performance Max
│   ├── Labels: [Netherlands] [Full-funnel]
│   ├── Asset Groups: Per category
│   └── All products feed
│
├── Campaign: BE - Brand Search
│   ├── Labels: [Belgium] [Brand]
│   └── Belgian brand terms
│
├── Campaign: BE - Non-Brand (Combined)
│   ├── Labels: [Belgium] [Non-Brand]
│   └── Smaller market = combined
│
└── Campaign: Retargeting (All regions)
    ├── Labels: [Remarketing] [Cross-region]
    └── Shared audiences

BUDGET MANAGEMENT:
──────────────────
□ Shared budgets per region/product line
□ Portfolio bid strategies where relevant
□ Seasonal budget rules
□ Automated rules for pacing
```

### Budget & Target Hierarchies

```
BUDGET HIERARCHY
════════════════

LEVEL 1: ACCOUNT TOTAL
──────────────────────
= Total monthly budget for all advertising

Allocation to:
├── Per market/region
├── Per business unit
└── Per objective

LEVEL 2: CAMPAIGN GROUPS
────────────────────────
= Grouped campaigns with shared budget

Example:
├── Brand Protection: €5,000/month
│   └── Campaigns: NL Brand, BE Brand
│
├── Volume Drivers: €30,000/month
│   └── Campaigns: NL Non-Brand, BE Non-Brand, PMax
│
└── Efficiency Focus: €15,000/month
    └── Campaigns: High-ROAS campaigns

LEVEL 3: INDIVIDUAL CAMPAIGNS
─────────────────────────────
= Daily budgets per campaign

Setting:
├── Standard: Even spread over month
├── Accelerated: Spend as fast as possible (riskier)
└── Shared: Pool budget over campaigns

TARGET HIERARCHY:
─────────────────

Account Target:
├── Blended ROAS: 380%
└── Blended CPA: N/A (e-commerce)

Campaign Targets:
├── Brand: ROAS 800% (low cost, high return)
├── Non-Brand: ROAS 350% (acquisition)
├── Retargeting: ROAS 500% (warm audience)
└── PMax: ROAS 400% (blended)

Ad Group Targets:
└── Inherited from campaign (Smart Bidding)
```

## Google Ads Script: Structure Analyzer

```javascript
/**
 * Account Structure Analyzer
 *
 * Analyzes account structure and provides recommendations
 * for consolidation and optimization.
 *
 * Setup:
 * 1. Adjust CONFIG
 * 2. Run manually or schedule monthly
 */

var CONFIG = {
  EMAIL: 'your@email.com',
  DATE_RANGE: 'LAST_30_DAYS',

  // Thresholds
  MIN_CONVERSIONS_PER_CAMPAIGN: 30,
  MIN_CONVERSIONS_PER_ADGROUP: 5,
  MAX_KEYWORDS_PER_ADGROUP: 30,
  MIN_KEYWORDS_PER_ADGROUP: 3
};

function main() {
  var report = {
    overview: {},
    consolidationCandidates: [],
    structureIssues: [],
    recommendations: []
  };

  // Account overview
  report.overview = getAccountOverview();

  // Analyze campaigns
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var analysis = analyzeCampaign(campaign);

    if (analysis.isConsolidationCandidate) {
      report.consolidationCandidates.push(analysis);
    }

    report.structureIssues = report.structureIssues.concat(analysis.issues);
  }

  // Generate recommendations
  report.recommendations = generateStructureRecommendations(report);

  // Send report
  sendStructureReport(report);

  Logger.log('Structure analysis complete');
  Logger.log('Consolidation candidates: ' + report.consolidationCandidates.length);
  Logger.log('Issues found: ' + report.structureIssues.length);
}

function getAccountOverview() {
  var stats = AdsApp.currentAccount().getStatsFor(CONFIG.DATE_RANGE);

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  var adGroups = AdsApp.adGroups()
    .withCondition('Status = ENABLED')
    .get();

  var keywords = AdsApp.keywords()
    .withCondition('Status = ENABLED')
    .get();

  var campaignCount = 0;
  while (campaigns.hasNext()) { campaigns.next(); campaignCount++; }

  var adGroupCount = 0;
  while (adGroups.hasNext()) { adGroups.next(); adGroupCount++; }

  var keywordCount = 0;
  while (keywords.hasNext()) { keywords.next(); keywordCount++; }

  return {
    campaigns: campaignCount,
    adGroups: adGroupCount,
    keywords: keywordCount,
    conversions: stats.getConversions(),
    cost: stats.getCost(),
    avgConvPerCampaign: stats.getConversions() / Math.max(campaignCount, 1),
    avgKeywordsPerAdGroup: keywordCount / Math.max(adGroupCount, 1)
  };
}

function analyzeCampaign(campaign) {
  var name = campaign.getName();
  var stats = campaign.getStatsFor(CONFIG.DATE_RANGE);
  var conversions = stats.getConversions();
  var cost = stats.getCost();

  var analysis = {
    name: name,
    conversions: conversions,
    cost: cost,
    adGroups: 0,
    keywords: 0,
    isConsolidationCandidate: false,
    issues: []
  };

  // Count ad groups and keywords
  var adGroups = campaign.adGroups()
    .withCondition('Status = ENABLED')
    .get();

  while (adGroups.hasNext()) {
    var adGroup = adGroups.next();
    analysis.adGroups++;

    var agStats = adGroup.getStatsFor(CONFIG.DATE_RANGE);
    var agConversions = agStats.getConversions();

    // Count keywords in ad group
    var keywords = adGroup.keywords()
      .withCondition('Status = ENABLED')
      .get();

    var kwCount = 0;
    while (keywords.hasNext()) {
      keywords.next();
      kwCount++;
      analysis.keywords++;
    }

    // Check ad group structure
    if (kwCount > CONFIG.MAX_KEYWORDS_PER_ADGROUP) {
      analysis.issues.push({
        campaign: name,
        adGroup: adGroup.getName(),
        type: 'TOO_MANY_KEYWORDS',
        detail: kwCount + ' keywords (max ' + CONFIG.MAX_KEYWORDS_PER_ADGROUP + ')'
      });
    }

    if (kwCount === 1) {
      analysis.issues.push({
        campaign: name,
        adGroup: adGroup.getName(),
        type: 'SKAG_DETECTED',
        detail: 'Single keyword ad group - consider consolidating'
      });
    }
  }

  // Check if consolidation candidate
  if (conversions < CONFIG.MIN_CONVERSIONS_PER_CAMPAIGN && cost > 0) {
    analysis.isConsolidationCandidate = true;
    analysis.consolidationReason = 'Low conversion volume (' + conversions.toFixed(0) + '/month)';
  }

  return analysis;
}

function generateStructureRecommendations(report) {
  var recs = [];

  // SKAG detection
  var skagCount = report.structureIssues.filter(function(i) {
    return i.type === 'SKAG_DETECTED';
  }).length;

  if (skagCount > 10) {
    recs.push({
      priority: 'HIGH',
      category: 'SKAG_MIGRATION',
      action: skagCount + ' SKAGs detected. Migrate to themed ad groups.',
      impact: 'Improved Smart Bidding performance, easier management'
    });
  }

  // Consolidation opportunity
  if (report.consolidationCandidates.length > 2) {
    var totalConv = report.consolidationCandidates.reduce(function(sum, c) {
      return sum + c.conversions;
    }, 0);

    recs.push({
      priority: 'HIGH',
      category: 'CONSOLIDATION',
      action: 'Consolidate ' + report.consolidationCandidates.length +
              ' low-volume campaigns (' + totalConv.toFixed(0) + ' total conv/month)',
      impact: 'Faster learning, better optimization'
    });
  }

  // Account complexity
  if (report.overview.campaigns > 20 &&
      report.overview.avgConvPerCampaign < 50) {
    recs.push({
      priority: 'MEDIUM',
      category: 'SIMPLIFICATION',
      action: 'Account has ' + report.overview.campaigns +
              ' campaigns with avg ' + report.overview.avgConvPerCampaign.toFixed(0) +
              ' conv/campaign',
      impact: 'Consider reducing campaign count for better data aggregation'
    });
  }

  return recs;
}

function sendStructureReport(report) {
  var subject = 'Account Structure Analysis - ' + AdsApp.currentAccount().getName();
  var body = 'Account Structure Analysis Report\n';
  body += '==================================\n\n';

  body += 'ACCOUNT OVERVIEW:\n';
  body += '• Campaigns: ' + report.overview.campaigns + '\n';
  body += '• Ad Groups: ' + report.overview.adGroups + '\n';
  body += '• Keywords: ' + report.overview.keywords + '\n';
  body += '• Avg conversions/campaign: ' + report.overview.avgConvPerCampaign.toFixed(1) + '\n';
  body += '• Avg keywords/ad group: ' + report.overview.avgKeywordsPerAdGroup.toFixed(1) + '\n\n';

  if (report.consolidationCandidates.length > 0) {
    body += 'CONSOLIDATION CANDIDATES:\n';
    body += '─────────────────────────\n';

    for (var i = 0; i < report.consolidationCandidates.length; i++) {
      var c = report.consolidationCandidates[i];
      body += '• ' + c.name + '\n';
      body += '  Conv: ' + c.conversions.toFixed(0) + ' | Reason: ' + c.consolidationReason + '\n\n';
    }
  }

  if (report.structureIssues.length > 0) {
    body += 'STRUCTURE ISSUES (first 20):\n';
    body += '────────────────────────────\n';

    var issuesToShow = report.structureIssues.slice(0, 20);
    for (var j = 0; j < issuesToShow.length; j++) {
      var issue = issuesToShow[j];
      body += '• [' + issue.type + '] ' + issue.campaign;
      if (issue.adGroup) body += ' / ' + issue.adGroup;
      body += '\n  ' + issue.detail + '\n\n';
    }

    if (report.structureIssues.length > 20) {
      body += '... and ' + (report.structureIssues.length - 20) + ' more issues\n\n';
    }
  }

  if (report.recommendations.length > 0) {
    body += 'RECOMMENDATIONS:\n';
    body += '────────────────\n';

    for (var k = 0; k < report.recommendations.length; k++) {
      var rec = report.recommendations[k];
      body += '[' + rec.priority + '] ' + rec.category + '\n';
      body += 'Action: ' + rec.action + '\n';
      body += 'Impact: ' + rec.impact + '\n\n';
    }
  }

  body += '\n---\nGenerated by Account Structure Analyzer';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Output: Structure Recommendation Template

```markdown
# Account Structure Recommendation

## Current State Analysis

### Account Statistics
- **Total campaigns:** [X]
- **Total ad groups:** [X]
- **Total keywords:** [X]
- **Avg conversions/campaign/month:** [X]
- **Avg keywords/ad group:** [X]

### Structure Assessment
| Aspect | Current | Best Practice | Status |
|--------|---------|---------------|--------|
| Campaign count | [X] | [Based on budget/conversions] | [OK/Issue] |
| Ad groups/campaign | [X] | 5-15 | [OK/Issue] |
| Keywords/ad group | [X] | 10-20 | [OK/Issue] |
| Conv/campaign | [X] | 50+ | [OK/Issue] |
| SKAG count | [X] | 0 | [OK/Issue] |

## Recommended Structure

### Proposed Architecture
```
[New Account Structure Diagram]
├── Campaign 1: [Name]
│   ├── Ad Groups: [List]
│   ├── Budget: €[X]/day
│   └── Bidding: [Strategy]
├── Campaign 2: [Name]
│   └── ...
└── Campaign N: [Name]
```

### Campaign Consolidation Plan
| Old Campaigns | New Campaign | Reason |
|---------------|--------------|--------|
| [List] | [New name] | [Low volume/overlap] |
| [List] | [New name] | [Same targets] |

### Ad Group Reorganization
| Current Ad Groups | New Ad Group | Theme |
|-------------------|--------------|-------|
| [SKAGs to merge] | [New name] | [Theme description] |

## Migration Plan

### Phase 1: Preparation (Week 1)
- [ ] Export current performance data
- [ ] Map keyword overlap
- [ ] Design new structure
- [ ] Create new campaigns (paused)

### Phase 2: Migration (Week 2-3)
- [ ] Enable new campaigns with 50% budget
- [ ] Reduce old campaigns to 50%
- [ ] Monitor performance daily
- [ ] Shift budget gradually

### Phase 3: Consolidation (Week 4)
- [ ] 100% on new structure
- [ ] Pause old campaigns
- [ ] Optimize new structure
- [ ] Document changes

## Expected Outcomes
- Faster learning phase
- Improved Smart Bidding performance
- Reduced management overhead
- Better budget allocation
- Cleaner reporting

## Monitoring Plan
- Week 1-2: Daily performance check
- Week 3-4: Learning phase monitoring
- Month 2: Full optimization cycle
```

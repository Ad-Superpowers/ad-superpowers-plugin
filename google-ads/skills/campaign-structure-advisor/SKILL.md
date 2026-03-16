---
name: campaign-structure-advisor
description: "Google Ads Campaign Structure advisor voor optimale account organisatie. Gebruik voor: (1) Account herstructurering en consolidatie, (2) Campaign type selectie, (3) Ad group organisatie, (4) Best practices voor Smart Bidding structuur, (5) Schaal- en efficiency optimalisatie. Triggers: account structuur, campaign structuur, ad group structuur, consolidatie, herstructureren, reorganiseren, skag, stag, hagakure, modern structure, simplified."
---

# Campaign Structure Advisor

Complete gids voor het structureren en optimaliseren van Google Ads accounts met focus op moderne, Smart Bidding-optimale architecturen.

## Quick Decision Guide

```
WELKE STRUCTUUR PAST BIJ JOU?
│
├─► NIEUW ACCOUNT (Greenfield)
│   └─► MODERN SIMPLIFIED STRUCTURE
│       ├── Minder campaigns, meer data per campaign
│       ├── Broad match + Smart Bidding
│       ├── Optimaal voor machine learning
│       └── Zie: "Modern Account Structure"
│
├─► BESTAAND ACCOUNT MET VEEL CAMPAIGNS
│   └─► CONSOLIDATIE NODIG?
│       ├── Check: <50 conv/campaign/maand? → JA
│       ├── Check: Veel overlappende keywords? → JA
│       ├── Check: Fragmenteerde budgetten? → JA
│       └── Zie: "Campaign Consolidatie"
│
├─► LEGACY SKAG/ZEER GRANULAR
│   └─► MODERNISEER
│       ├── SKAGs zijn outdated voor Smart Bidding
│       ├── Consolideer naar STAG of Themed
│       ├── Behoud best performers
│       └── Zie: "SKAG naar Modern Migratie"
│
└─► HIGH-VOLUME MATURE ACCOUNT
    └─► HYBRID APPROACH
        ├── Separate campaigns waar nodig (budgets, targets)
        ├── Consolideer waar mogelijk
        ├── Portfolio strategies voor aggregatie
        └── Zie: "Enterprise Account Structure"
```

## Moderne Account Structuur

### Fundamentele Principes

```
MODERNE GOOGLE ADS STRUCTUUR PRINCIPES
══════════════════════════════════════

PRINCIPE 1: CONSOLIDATIE OVER FRAGMENTATIE
──────────────────────────────────────────
OUD: Veel kleine campaigns met weinig data
NIEUW: Minder campaigns met meer conversies

Waarom:
├── Smart Bidding leert sneller met meer data
├── Minder management overhead
├── Betere budget allocatie
└── Snellere Learning Phase

PRINCIPE 2: MACHINE LEARNING FIRST
──────────────────────────────────
OUD: Manual bids, exact match focus
NIEUW: Smart Bidding, broad match toegestaan

Waarom:
├── Google's AI ziet signalen die jij niet ziet
├── Real-time bid optimalisatie per auction
├── Broad match + Smart Bidding = powerful combo
└── Focus op strategie, niet tactiek

PRINCIPE 3: THEME-BASED AD GROUPS
─────────────────────────────────
OUD: SKAG (Single Keyword Ad Groups)
NIEUW: STAG (Single Theme Ad Groups)

Waarom:
├── Genoeg variatie voor AI om te leren
├── Ads nog steeds relevant
├── Manageable scale
└── Flexibel voor query expansion

PRINCIPE 4: BUDGET = BUSINESS CONSTRAINT
────────────────────────────────────────
Separate campaigns alleen bij:
├── Verschillende budget pools
├── Verschillende geographic targets
├── Verschillende business units/products
├── Verschillende performance targets (CPA/ROAS)
└── Regulatory/compliance requirements
```

### Ideale Account Structuur

```
RECOMMENDED ACCOUNT ARCHITECTURE
════════════════════════════════

E-COMMERCE STRUCTURE:
─────────────────────
Account
├── Campaign 1: Brand Search
│   ├── Budget: 10-15% of total
│   ├── Bidding: Max Conversions of tCPA
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
│   ├── Bidding: tCPA of tROAS
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

### Ad Group Organisatie

```
AD GROUP BEST PRACTICES
═══════════════════════

STAG (Single Theme Ad Groups):
──────────────────────────────
= Keywords met dezelfde intent gegroepeerd

VOORBEELD - Product Theme:
Ad Group: "Running Shoes"
├── running shoes
├── running shoes kopen
├── beste running shoes
├── hardloopschoenen
├── hardloopschoenen kopen
└── sneakers voor hardlopen

RICHTLIJNEN:
────────────
□ 10-20 keywords per ad group
□ Alle keywords zelfde intent/theme
□ Zelfde landing page
□ 2-3 RSAs per ad group
□ Specifieke ad copy voor theme

MATCH TYPE STRATEGIE (Modern):
──────────────────────────────
Aanbevolen met Smart Bidding:
├── Broad Match: 40-60% (met goede negatives)
├── Phrase Match: 30-40%
└── Exact Match: 10-20% (top performers)

Legacy accounts:
├── Start met phrase/exact
├── Voeg broad toe met monitoring
├── Expand based on search term performance

NEGATIVES CRUCIAAL:
───────────────────
Bij broad match:
□ Account-level negative list
□ Campaign-level specifics
□ Wekelijkse search term review
□ Proactieve negatives (irrelevant terms)
```

## Campaign Consolidatie

### Wanneer Consolideren

```
CONSOLIDATIE ASSESSMENT
═══════════════════════

CONSOLIDEER WANNEER:
────────────────────

✓ CONVERSIE VOLUME TE LAAG
  └── <50 conversies per campaign per maand
  └── Smart Bidding in "Learning Limited"

✓ OVERLAPPENDE KEYWORDS
  └── Zelfde keywords in meerdere campaigns
  └── Internal competition
  └── Fragmenteerde data

✓ ZELFDE TARGETS
  └── Campaigns met identieke CPA/ROAS targets
  └── Geen reden voor separatie

✓ GEFRAGMENTEERD BUDGET
  └── Kleine budgetten over veel campaigns
  └── Geen enkele campaign genoeg voor learning

✓ MANAGEMENT OVERHEAD
  └── Te veel tijd aan kleine campaigns
  └── Moeilijk te optimaliseren

BEHOUD SEPARATE CAMPAIGNS WANNEER:
──────────────────────────────────

✗ VERSCHILLENDE BUDGETS
  └── Separate funding pools
  └── Client/business unit separation

✗ VERSCHILLENDE GEO TARGETS
  └── Andere landen
  └── Andere talen
  └── Andere bid landscapes

✗ SIGNIFICANT ANDERE TARGETS
  └── Brand vs Non-brand (vaak andere CPA)
  └── High-value vs Volume
  └── Verschillende margins

✗ COMPLIANCE/ORGANISATORISCH
  └── Regulatory requirements
  └── Reporting requirements
  └── Organizational structure
```

### Consolidatie Strategie

```
CONSOLIDATIE STAPPENPLAN
════════════════════════

FASE 1: ANALYSE (Week 1)
────────────────────────
□ Exporteer alle campaign data (30/90 dagen)
□ Identificeer campaigns voor consolidatie
□ Map keyword overlap
□ Document huidige performance baselines
□ Plan nieuwe structuur

Consolidatie kandidaten:
┌─────────────────────────────────────────────────────────┐
│ Campaign          │ Conv/maand │ CPA    │ Overlap? │ ? │
├───────────────────┼────────────┼────────┼──────────┼───┤
│ Product A Search  │ 15         │ €45    │ Yes      │ ✓ │
│ Product B Search  │ 22         │ €48    │ Yes      │ ✓ │
│ Brand Search      │ 150        │ €12    │ No       │ ✗ │
│ Display Retarget  │ 35         │ €28    │ No       │ ✗ │
└───────────────────┴────────────┴────────┴──────────┴───┘

FASE 2: NIEUWE STRUCTUUR BOUWEN (Week 2)
────────────────────────────────────────
□ Creëer nieuwe geconsolideerde campaigns
□ Importeer/reorganiseer keywords
□ Creëer nieuwe ad groups (themed)
□ Schrijf nieuwe RSAs
□ Setup extensions
□ Configureer bid strategy
□ TEST: Verify setup

Nieuwe structuur voorbeeld:
├── [Oude] Product A Search →
├── [Oude] Product B Search → [Nieuw] Products Search (combined)
└── [Oude] Product C Search →

FASE 3: MIGRATIE (Week 3)
─────────────────────────
Optie A: Hard switch
├── Pause oude campaigns
├── Enable nieuwe campaigns
└── Monitor intensief

Optie B: Soft transition (aanbevolen)
├── Verlaag oude budgets met 50%
├── Enable nieuwe met 50% budget
├── Shift geleidelijk over 7-14 dagen
└── Pause oude wanneer nieuwe stabiel

FASE 4: OPTIMALISATIE (Week 4+)
───────────────────────────────
□ Monitor Learning Phase
□ Adjust targets indien nodig
□ Optimize negatives
□ Review search terms
□ Fine-tune ad copy
```

### Portfolio Bid Strategies

```
PORTFOLIO BID STRATEGIES
════════════════════════

WAT: Eén bid strategy over meerdere campaigns

WANNEER GEBRUIKEN:
──────────────────
✓ Campaigns te klein voor individuele learning
✓ Zelfde business objective
✓ Wil centraal bid management
✓ Data wil aggregeren

SETUP:
──────
Tools → Shared Library → Bid Strategies → +

PORTFOLIO OPTIES:
─────────────────
1. Target CPA Portfolio
   └── Meerdere lead gen campaigns
   └── Zelfde CPA target

2. Target ROAS Portfolio
   └── Meerdere e-commerce campaigns
   └── Zelfde margin target

3. Maximize Conversions Portfolio
   └── Nieuwe/kleine campaigns
   └── Data aggregatie voor learning

VOORBEELD SETUP:
────────────────
Portfolio: "Non-Brand Search - tCPA €50"
├── Campaign: Generic Keywords
├── Campaign: Competitor Keywords
├── Campaign: Long-tail Keywords
└── Shared target: €50 CPA

VOORDELEN:
├── Geaggregeerde learning
├── Snellere learning phase
├── Centraal management
├── Budget flexibiliteit

NADELEN:
├── Minder granular control
├── Shared targets niet altijd optimaal
├── Reporting complexer
└── Suboptimaal als campaigns heel verschillend zijn
```

## SKAG naar Modern Migratie

### SKAG Problematiek

```
WAAROM SKAG NIET MEER WERKT
═══════════════════════════

SKAG = Single Keyword Ad Groups
= Één keyword per ad group (exact match)

WAAROM HET POPULAIR WAS:
├── Maximale keyword-ad relevance
├── Perfecte Quality Score
├── Granulaire bid control
└── Pre-Smart Bidding logica

WAAROM HET NU NIET WERKT:
─────────────────────────

1. SMART BIDDING NEEDS DATA
   ├── SKAG = weinig conversies per ad group
   ├── AI kan niet leren met kleine samples
   └── "Learning Limited" overal

2. CLOSE VARIANTS MAKEN HET ZINLOOS
   ├── [running shoes] triggered ook "sneakers running"
   ├── Exact match is niet meer exact
   └── SKAG voordeel verdwenen

3. MANAGEMENT NIGHTMARE
   ├── Duizenden ad groups
   ├── Moeilijk te optimaliseren
   ├── RSA needs headroom die er niet is
   └── Tijd beter besteed elders

4. BROAD MATCH + SMART BIDDING IS BETER
   ├── AI selecteert beste queries
   ├── Meer reach
   ├── Automatic query expansion
   └── Focus op outcomes, niet structure
```

### Migratie Strategie

```
SKAG → MODERN MIGRATIE
══════════════════════

STAP 1: INVENTORY
─────────────────
□ Exporteer alle SKAGs
□ Groepeer keywords op theme/intent
□ Identificeer top performers (behouden intent)
□ Noteer best performing ad copy

Grouping voorbeeld:
SKAGs:
├── [running shoes]
├── [running shoes men]
├── [best running shoes]
├── [buy running shoes]
└── [running shoes sale]

→ Nieuwe Ad Group: "Running Shoes"
  (alle bovenstaande + variaties)

STAP 2: NIEUWE STRUCTUUR DEFINIËREN
───────────────────────────────────
Van: 500 SKAGs
Naar: 30-50 themed ad groups in 3-5 campaigns

Vuistregels:
├── Max 5-10 ad groups per campaign
├── Max 20 keywords per ad group
├── Min 50 conv/campaign/maand target
└── Themed groupings

STAP 3: AD COPY CONSOLIDATIE
────────────────────────────
Van: 500 exact-match ads
Naar: 100-150 RSAs met variatie

Per ad group:
├── 2-3 RSAs
├── Gebruik best performers als base
├── Varieer headlines/descriptions
└── Gebruik keyword insertion waar logisch

STAP 4: MIGRATIE EXECUTIE
─────────────────────────
Week 1:
├── Bouw nieuwe campaigns naast SKAG
├── Mirror best keywords en ads
├── Setup bid strategy (start conservatief)
└── Enable met 20% budget

Week 2:
├── Monitor nieuwe campaigns
├── Shift budget: 50% nieuw, 50% SKAG
├── Check search terms
└── Add negatives

Week 3:
├── Als stabiel: 80% nieuw, 20% SKAG
├── Pause low performers in SKAG
└── Continue monitoring

Week 4:
├── Pause alle SKAG campaigns
├── 100% op nieuwe structuur
├── Delete/archive oude campaigns
└── Full optimization mode

STAP 5: POST-MIGRATIE
─────────────────────
□ Monitor Learning Phase (2-4 weken)
□ Optimaliseer bid targets
□ Expand met broad match (geleidelijk)
□ Continue negative keyword management
□ Document learnings
```

## Enterprise Account Structure

### Multi-Product/Region Accounts

```
ENTERPRISE ACCOUNT ARCHITECTUUR
═══════════════════════════════

ORGANISATIE PRINCIPES:
──────────────────────

1. CAMPAIGN = BUDGET ALLOCATION UNIT
   └── Separate campaigns voor separate budgets
   └── Niet: Separate campaigns voor organisatie

2. LABELS = ORGANISATIE
   └── Product lines
   └── Teams/ownership
   └── Initiatives
   └── Reporting groups

3. MCC VOOR ECHTE SCHEIDING
   └── Verschillende business units
   └── Verschillende billing
   └── Compliance requirements

STRUCTUUR VOORBEELD:
────────────────────

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
□ Portfolio bid strategies waar relevant
□ Seasonal budget rules
□ Automated rules voor pacing
```

### Budget & Target Hierarchies

```
BUDGET HIËRARCHIE
═════════════════

LEVEL 1: ACCOUNT TOTAL
──────────────────────
= Totaal maandbudget voor alle advertising

Allocatie naar:
├── Per market/region
├── Per business unit
└── Per objective

LEVEL 2: CAMPAIGN GROUPS
────────────────────────
= Gegroepeerde campaigns met shared budget

Voorbeeld:
├── Brand Protection: €5,000/maand
│   └── Campaigns: NL Brand, BE Brand
│
├── Volume Drivers: €30,000/maand
│   └── Campaigns: NL Non-Brand, BE Non-Brand, PMax
│
└── Efficiency Focus: €15,000/maand
    └── Campaigns: High-ROAS campaigns

LEVEL 3: INDIVIDUAL CAMPAIGNS
─────────────────────────────
= Daily budgets per campaign

Setting:
├── Standard: Even spread over month
├── Accelerated: Spend as fast as possible (riskier)
└── Shared: Pool budget over campaigns

TARGET HIËRARCHIE:
──────────────────

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
 * Analyseert account structuur en geeft aanbevelingen
 * voor consolidatie en optimalisatie.
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Run manually of schedule monthly
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',
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

---
name: scaling-calculator
description: "Google Ads budget scaling en iROAS calculator. Gebruik voor: (1) Budget scaling strategieën, (2) Incremental ROAS (iROAS) berekening, (3) Diminishing returns analyse, (4) Break-even calculaties, (5) Profit maximalisatie modellen, (6) Scaling roadmap planning. Triggers: scaling, budget increase, iroas, incremental roas, diminishing returns, profit margin, budget planning, schaalbaar, opschalen."
---

# Scaling Calculator

Complete gids voor het berekenen en implementeren van Google Ads budget scaling strategieën met focus op profitability en incremental ROAS.

## Scaling Fundamentals

```
SCALING PRINCIPES
═════════════════

KERNPRINCIPE:
Méér budget ≠ Lineair méér resultaat

┌─────────────────────────────────────────────────────────────────┐
│  DIMINISHING RETURNS CURVE                                      │
│                                                                 │
│  Conversions                                                    │
│  │                           ╭─────────────────────             │
│  │                      ╭────╯                                  │
│  │                 ╭────╯                                       │
│  │            ╭────╯   ← Sweet Spot (highest efficiency)        │
│  │       ╭────╯                                                 │
│  │  ╭────╯                                                      │
│  │──╯                                                           │
│  └─────────────────────────────────────────────────► Budget    │
│                                                                 │
│  ⚠️ Op een bepaald punt kosten extra conversies MEER           │
│  ⚠️ Niet elke euro brengt dezelfde return                      │
└─────────────────────────────────────────────────────────────────┘

WAAROM DIMINISHING RETURNS?
───────────────────────────
├── Beste audience bereik je eerst
├── Beste zoektermen triggeren eerst
├── Meer budget = bredere, minder relevante reach
├── Competitie dwingt hogere bids
└── Quality audience is eindig
```

## Break-Even Calculaties

### ROAS Break-Even Calculator

```
ROAS BREAK-EVEN BEREKENING
══════════════════════════

FORMULE:
Break-Even ROAS = 1 / Gross Margin %

VOORBEELDEN:
────────────
Profit Margin 20%:  Break-even ROAS = 1 / 0.20 = 5.00x (500%)
Profit Margin 30%:  Break-even ROAS = 1 / 0.30 = 3.33x (333%)
Profit Margin 40%:  Break-even ROAS = 1 / 0.40 = 2.50x (250%)
Profit Margin 50%:  Break-even ROAS = 1 / 0.50 = 2.00x (200%)
Profit Margin 60%:  Break-even ROAS = 1 / 0.60 = 1.67x (167%)

┌────────────────┬──────────────┬───────────────┬──────────────┐
│ GROSS MARGIN   │ BREAK-EVEN   │ TARGET ROAS   │ IDEAL ROAS   │
│ (na COGS)      │ ROAS         │ (10% profit)  │ (20% profit) │
├────────────────┼──────────────┼───────────────┼──────────────┤
│ 20%            │ 5.00x        │ 5.55x         │ 6.25x        │
│ 25%            │ 4.00x        │ 4.44x         │ 5.00x        │
│ 30%            │ 3.33x        │ 3.70x         │ 4.17x        │
│ 35%            │ 2.86x        │ 3.17x         │ 3.57x        │
│ 40%            │ 2.50x        │ 2.78x         │ 3.13x        │
│ 45%            │ 2.22x        │ 2.47x         │ 2.78x        │
│ 50%            │ 2.00x        │ 2.22x         │ 2.50x        │
│ 60%            │ 1.67x        │ 1.85x         │ 2.08x        │
└────────────────┴──────────────┴───────────────┴──────────────┘

UITGEBREIDE FORMULE:
────────────────────
Target ROAS = 1 / (Gross Margin - Desired Net Margin)

Voorbeeld:
├── Gross Margin: 40%
├── Desired Net Profit Margin: 10%
├── Available for Ads: 40% - 10% = 30%
└── Target ROAS = 1 / 0.30 = 3.33x
```

### CPA Break-Even Calculator

```
CPA BREAK-EVEN BEREKENING
═════════════════════════

FORMULE (E-commerce):
Break-Even CPA = AOV × Gross Margin %

FORMULE (Lead Gen):
Break-Even CPL = Customer Value × Conversion Rate × Margin

VOORBEELDEN E-COMMERCE:
───────────────────────
AOV €100, Margin 40%:  Break-even CPA = €100 × 0.40 = €40
AOV €80, Margin 50%:   Break-even CPA = €80 × 0.50 = €40
AOV €150, Margin 30%:  Break-even CPA = €150 × 0.30 = €45
AOV €200, Margin 25%:  Break-even CPA = €200 × 0.25 = €50

VOORBEELDEN LEAD GEN:
─────────────────────
Customer Value €2000, Close Rate 10%, Margin 30%:
Break-even CPL = €2000 × 0.10 × 0.30 = €60

Customer Value €5000, Close Rate 5%, Margin 40%:
Break-even CPL = €5000 × 0.05 × 0.40 = €100

┌────────────┬───────────┬──────────────┬──────────────┐
│ AOV        │ MARGIN    │ BREAK-EVEN   │ TARGET CPA   │
│            │           │ CPA          │ (20% profit) │
├────────────┼───────────┼──────────────┼──────────────┤
│ €50        │ 40%       │ €20          │ €16          │
│ €75        │ 40%       │ €30          │ €24          │
│ €100       │ 40%       │ €40          │ €32          │
│ €100       │ 50%       │ €50          │ €40          │
│ €150       │ 35%       │ €52.50       │ €42          │
│ €200       │ 30%       │ €60          │ €48          │
│ €300       │ 25%       │ €75          │ €60          │
└────────────┴───────────┴──────────────┴──────────────┘
```

## Incremental ROAS (iROAS)

### Wat Is iROAS?

```
INCREMENTAL ROAS UITLEG
═══════════════════════

DEFINITIE:
iROAS = Extra Revenue / Extra Ad Spend

VERSCHIL MET BLENDED ROAS:
──────────────────────────
┌────────────────────────────────────────────────────────────────┐
│ BLENDED ROAS (wat je in Google Ads ziet):                      │
│ = Totale Attributed Revenue / Totale Ad Spend                  │
│                                                                │
│ INCREMENTAL ROAS (echte waarde van extra spend):               │
│ = (Revenue met meer budget - Revenue met minder budget)        │
│   / (Extra Budget)                                             │
│                                                                │
│ ⚠️ Blended ROAS overschat vaak de waarde!                     │
│ ⚠️ Deel van conversies zou ook zonder ads gebeuren            │
└────────────────────────────────────────────────────────────────┘

VOORBEELD:
──────────
Huidige situatie:
├── Budget: €10,000/maand
├── Revenue: €50,000
├── Blended ROAS: 5.0x

Na budget verhoging:
├── Budget: €15,000/maand (+€5,000)
├── Revenue: €65,000 (+€15,000)
├── Blended ROAS: 4.3x (lijkt slechter!)
├── iROAS: €15,000 / €5,000 = 3.0x

Conclusie:
├── Blended ROAS daalde van 5.0x naar 4.3x
├── MAAR: Extra €5,000 spend leverde €15,000 op
├── Als break-even = 2.5x, is 3.0x iROAS winstgevend!
└── Schalen is slim, ondanks lagere blended ROAS
```

### iROAS Berekenen

```
iROAS BEREKENING METHODES
═════════════════════════

METHODE 1: GEO EXPERIMENT
─────────────────────────
1. Split audiences geografisch
2. Groep A: Current budget
3. Groep B: Increased budget
4. Meet verschil in revenue
5. Bereken: (Rev B - Rev A) / (Budget B - Budget A)

METHODE 2: BUDGET STAPPEN TEST
──────────────────────────────
1. Meet performance per budget niveau
2. Plot revenue vs spend curve
3. Bereken marginale return per stap

Budget Stappen:
├── Week 1: €1,000 → Revenue €4,500 (4.5x)
├── Week 2: €1,500 → Revenue €6,000 (4.0x)
│   └── iROAS stap: (€6,000-€4,500)/(€1,500-€1,000) = 3.0x
├── Week 3: €2,000 → Revenue €7,200 (3.6x)
│   └── iROAS stap: (€7,200-€6,000)/(€2,000-€1,500) = 2.4x
└── Week 4: €2,500 → Revenue €8,000 (3.2x)
    └── iROAS stap: (€8,000-€7,200)/(€2,500-€2,000) = 1.6x

METHODE 3: HOLDOUT EXPERIMENT
─────────────────────────────
1. Pauzeer campaign voor subset audience
2. Meet organic/other channel lift
3. Verschil = incremental value
4. Bereken true incrementality %

Typische Incrementality:
├── Brand campaigns: 30-60% incremental
├── Non-brand Search: 60-80% incremental
├── Shopping: 50-70% incremental
├── PMax: 60-80% incremental
└── Remarketing: 20-50% incremental
```

## Scaling Strategieën

### Veilige Scaling Methode

```
CONSERVATIVE SCALING PROTOCOL
═════════════════════════════

REGEL: Maximaal 15-20% budget verhoging per week

┌───────────────────────────────────────────────────────────────┐
│  SCALING STAPPENPLAN                                          │
│                                                               │
│  Week 0: Baseline                                             │
│  ├── Budget: €1,000                                           │
│  ├── ROAS: 4.5x                                               │
│  └── Conversies: 45                                           │
│                                                               │
│  Week 1: +15%                                                 │
│  ├── Budget: €1,150                                           │
│  ├── Expected ROAS: 4.2-4.5x                                  │
│  └── Monitor: iROAS, CPA trend                                │
│                                                               │
│  Week 2: +15% (als stable)                                    │
│  ├── Budget: €1,322                                           │
│  ├── Expected ROAS: 4.0-4.3x                                  │
│  └── Monitor: Quality Score, auction insights                 │
│                                                               │
│  Week 3: +15% (als stable)                                    │
│  ├── Budget: €1,520                                           │
│  └── Continue monitoring                                      │
│                                                               │
│  Week 4: Evaluate                                             │
│  ├── Compare: Week 4 vs Week 0 metrics                        │
│  ├── Calculate: True iROAS over period                        │
│  └── Decide: Continue, pause, of rollback                     │
└───────────────────────────────────────────────────────────────┘

STOPPING CRITERIA:
──────────────────
❌ Stop scaling wanneer:
├── iROAS < Break-even ROAS
├── ROAS daalt >25% week-over-week
├── CPA stijgt >30% vs baseline
├── Learning phase niet compleet wordt
└── Impression share daalt significant (budget cap)
```

### Aggressive Scaling (Voor Proven Winners)

```
AGGRESSIVE SCALING PROTOCOL
═══════════════════════════

ALLEEN WANNEER:
├── Campaign draait >3 maanden profitable
├── Smart Bidding learning phase stable
├── iROAS bewezen via tests
└── Sufficient margin boven break-even

METHODE: 2x BUDGET IN 4 WEKEN
─────────────────────────────
Week 1: +20%
Week 2: +25%
Week 3: +20%
Week 4: +15%
Result: ~2x original budget

VOORBEELD:
──────────
Start: €5,000/maand, ROAS 5.0x
Week 1: €6,000 (+20%)
Week 2: €7,500 (+25%)
Week 3: €9,000 (+20%)
Week 4: €10,350 (+15%)
Target: Maintain ROAS >3.5x

MONITORING CADENCE:
───────────────────
├── Daily: Spend pacing, CPA spikes
├── Every 3 days: Conversion lag adjusted ROAS
├── Weekly: Full performance review
└── Bi-weekly: iROAS calculation
```

### Horizontal vs Vertical Scaling

```
SCALING DIMENSIES
═════════════════

VERTICAAL SCALING (Meer budget, zelfde campaigns)
─────────────────────────────────────────────────
✅ Voordelen:
├── Eenvoudig te implementeren
├── Behoudt proven structure
├── Smart Bidding kan optimaliseren
└── Snelle impact

❌ Nadelen:
├── Diminishing returns
├── Beperkt door audience size
├── Competition increases
└── Bid inflation

HORIZONTAAL SCALING (Nieuwe campaigns, audiences)
─────────────────────────────────────────────────
✅ Voordelen:
├── Nieuwe audiences = fresh potential
├── Test new channels (YouTube, Discover)
├── Geographic expansion
├── Product category expansion

❌ Nadelen:
├── Nieuwe learning phases
├── Meer management overhead
├── Uncertain performance
└── Resource intensive

OPTIMALE STRATEGIE: HYBRIDE
───────────────────────────
1. Verticaal: Scale proven campaigns tot iROAS < target
2. Horizontaal: Launch new campaigns met 20% van nieuwe budget
3. Itereren: Move budget naar best performers

BUDGET ALLOCATIE BIJ SCHALEN:
─────────────────────────────
├── 70% → Bestaande top performers
├── 20% → Uitbreiding proven concepts (nieuw geo, new products)
└── 10% → Experimenteel (nieuwe campaign types, audiences)
```

## Profit Maximization Model

### MER (Marketing Efficiency Ratio)

```
MARKETING EFFICIENCY RATIO
══════════════════════════

DEFINITIE:
MER = Total Revenue / Total Marketing Spend

VERSCHIL MET ROAS:
──────────────────
ROAS = Attributed Revenue / Specific Channel Spend
MER = ALL Revenue / ALL Marketing Spend

WAAROM MER BELANGRIJKER BIJ SCALING:
────────────────────────────────────
├── ROAS meet alleen directe attribution
├── MER meet holistische marketing efficiency
├── Bij schalen: cross-channel effects matter
└── Brand impact niet gemeten in ROAS

MER BENCHMARKS:
───────────────
├── Startup/Growth: MER 3-5x acceptable
├── Mature E-commerce: MER 5-8x target
├── Market Leader: MER 8-15x possible
└── Direct Response: MER 2-4x typical

VOORBEELD MER ANALYSE:
──────────────────────
Maand 1 (€20k spend):
├── Google Ads Revenue: €70k (ROAS 3.5x)
├── Meta Ads Revenue: €30k (ROAS 3.0x)
├── Organic/Direct Revenue: €50k
├── Total Revenue: €150k
└── MER: €150k / €20k = 7.5x

Maand 2 (€30k spend, +50%):
├── Google Ads Revenue: €90k (ROAS 3.0x)
├── Meta Ads Revenue: €40k (ROAS 2.7x)
├── Organic/Direct Revenue: €70k (+40% halo)
├── Total Revenue: €200k
└── MER: €200k / €30k = 6.7x

Conclusie:
├── Channel ROAS daalde
├── MER daalde minder (7.5x → 6.7x)
├── Brand lift boosted organic
└── Scaling was profitable overall
```

### Profit Curve Optimalisatie

```
PROFIT MAXIMIZATION CURVE
═════════════════════════

┌─────────────────────────────────────────────────────────────────┐
│  Profit €                                                        │
│  │                                                               │
│  │                    ╭──────────╮ ← Maximum Profit Point       │
│  │               ╭────╯          ╰────╮                         │
│  │          ╭────╯                    ╰────╮                    │
│  │     ╭────╯                              ╰────╮               │
│  │ ────╯                                        ╰────           │
│  │╱                                                  ╲          │
│  └─────────────────────────────────────────────────────► Spend  │
│    ↑                    ↑                        ↑              │
│    Too Little           Optimal                  Too Much       │
│                                                                 │
│  Zone A: Underspending = Missing profitable conversions         │
│  Zone B: Optimal = Maximum profit                               │
│  Zone C: Overspending = Marginal conversions cost too much      │
└─────────────────────────────────────────────────────────────────┘

FORMULE:
Profit = Revenue - COGS - Ad Spend
Profit = (Conversions × AOV × Margin) - Ad Spend

VIND OPTIMAL SPEND:
───────────────────
Optimal wanneer: Marginal Cost = Marginal Revenue
= iCPA = Break-Even CPA
= iROAS = Break-Even ROAS

PRACTICAL APPROACH:
───────────────────
1. Start met profitable spend level
2. Increase budget in stappen
3. Track iROAS per stap
4. Stop wanneer iROAS < Break-even
5. Optimal = stap vóór iROAS < break-even
```

## Google Ads Script: Scaling Monitor

```javascript
/**
 * Scaling Performance Monitor
 *
 * Features:
 * - Track performance bij budget changes
 * - Calculate incremental metrics
 * - Alert bij significant performance drops
 * - Recommend scaling decisions
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Stel BREAK_EVEN_ROAS in voor jouw business
 * 3. Schedule: Dagelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Jouw break-even ROAS (1 / margin)
  BREAK_EVEN_ROAS: 2.5,

  // Scaling alert thresholds
  ROAS_DROP_ALERT: 0.20,         // Alert bij 20% ROAS drop
  CPA_INCREASE_ALERT: 0.25,      // Alert bij 25% CPA stijging
  MIN_SPEND_FOR_ANALYSIS: 100,   // Minimum spend voor analyse

  // Comparison periods
  CURRENT_PERIOD: 'LAST_7_DAYS',
  PREVIOUS_PERIOD: 14             // Days back for comparison
};

function main() {
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .withCondition('Cost > ' + CONFIG.MIN_SPEND_FOR_ANALYSIS)
    .forDateRange(CONFIG.CURRENT_PERIOD)
    .get();

  var report = {
    date: new Date().toDateString(),
    accountName: AdsApp.currentAccount().getName(),
    campaigns: [],
    alerts: [],
    recommendations: []
  };

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var analysis = analyzeCampaign(campaign);
    report.campaigns.push(analysis);

    if (analysis.alerts.length > 0) {
      report.alerts = report.alerts.concat(analysis.alerts);
    }
    if (analysis.recommendation) {
      report.recommendations.push(analysis.recommendation);
    }
  }

  if (report.alerts.length > 0 || report.recommendations.length > 0) {
    sendScalingReport(report);
  }

  logSummary(report);
}

function analyzeCampaign(campaign) {
  var name = campaign.getName();

  // Current period stats
  var currentStats = campaign.getStatsFor(CONFIG.CURRENT_PERIOD);
  var currentSpend = currentStats.getCost();
  var currentRevenue = currentStats.getConversionValue();
  var currentConversions = currentStats.getConversions();
  var currentROAS = currentSpend > 0 ? currentRevenue / currentSpend : 0;
  var currentCPA = currentConversions > 0 ? currentSpend / currentConversions : 0;

  // Previous period stats
  var today = new Date();
  var previousEnd = new Date(today.getTime() - (7 * 24 * 60 * 60 * 1000));
  var previousStart = new Date(previousEnd.getTime() - (7 * 24 * 60 * 60 * 1000));

  var previousStats = campaign.getStatsFor(
    formatDate(previousStart),
    formatDate(previousEnd)
  );
  var previousSpend = previousStats.getCost();
  var previousRevenue = previousStats.getConversionValue();
  var previousConversions = previousStats.getConversions();
  var previousROAS = previousSpend > 0 ? previousRevenue / previousSpend : 0;
  var previousCPA = previousConversions > 0 ? previousSpend / previousConversions : 0;

  // Calculate changes
  var spendChange = previousSpend > 0 ?
    (currentSpend - previousSpend) / previousSpend : 0;
  var roasChange = previousROAS > 0 ?
    (currentROAS - previousROAS) / previousROAS : 0;
  var cpaChange = previousCPA > 0 ?
    (currentCPA - previousCPA) / previousCPA : 0;

  // Calculate incremental metrics (if spend increased)
  var iROAS = 0;
  var iCPA = 0;
  if (spendChange > 0) {
    var incrementalSpend = currentSpend - previousSpend;
    var incrementalRevenue = currentRevenue - previousRevenue;
    var incrementalConversions = currentConversions - previousConversions;

    iROAS = incrementalSpend > 0 ? incrementalRevenue / incrementalSpend : 0;
    iCPA = incrementalConversions > 0 ?
      incrementalSpend / incrementalConversions : 0;
  }

  // Generate alerts
  var alerts = [];
  if (roasChange < -CONFIG.ROAS_DROP_ALERT) {
    alerts.push({
      type: 'ROAS_DROP',
      campaign: name,
      message: 'ROAS dropped ' + Math.abs(roasChange * 100).toFixed(1) + '%',
      current: currentROAS.toFixed(2),
      previous: previousROAS.toFixed(2)
    });
  }

  if (cpaChange > CONFIG.CPA_INCREASE_ALERT) {
    alerts.push({
      type: 'CPA_INCREASE',
      campaign: name,
      message: 'CPA increased ' + (cpaChange * 100).toFixed(1) + '%',
      current: currentCPA.toFixed(2),
      previous: previousCPA.toFixed(2)
    });
  }

  // Generate recommendation
  var recommendation = null;
  if (currentROAS > CONFIG.BREAK_EVEN_ROAS * 1.5 && spendChange <= 0) {
    recommendation = {
      campaign: name,
      action: 'SCALE_UP',
      reason: 'ROAS ' + currentROAS.toFixed(2) + 'x is well above break-even (' +
              CONFIG.BREAK_EVEN_ROAS + 'x). Consider +15-20% budget increase.'
    };
  } else if (iROAS > 0 && iROAS < CONFIG.BREAK_EVEN_ROAS) {
    recommendation = {
      campaign: name,
      action: 'PAUSE_SCALING',
      reason: 'Incremental ROAS ' + iROAS.toFixed(2) + 'x is below break-even. ' +
              'Recent budget increase may not be profitable.'
    };
  } else if (currentROAS < CONFIG.BREAK_EVEN_ROAS * 0.8) {
    recommendation = {
      campaign: name,
      action: 'REDUCE_BUDGET',
      reason: 'ROAS ' + currentROAS.toFixed(2) + 'x is below break-even. ' +
              'Consider reducing budget or pausing campaign.'
    };
  }

  return {
    name: name,
    currentSpend: currentSpend,
    currentROAS: currentROAS,
    currentCPA: currentCPA,
    spendChange: spendChange,
    roasChange: roasChange,
    iROAS: iROAS,
    iCPA: iCPA,
    alerts: alerts,
    recommendation: recommendation
  };
}

function formatDate(date) {
  return Utilities.formatDate(date, AdsApp.currentAccount().getTimeZone(), 'yyyyMMdd');
}

function sendScalingReport(report) {
  var subject = 'Scaling Monitor Alert - ' + report.accountName;

  var body = 'Scaling Performance Report\n';
  body += '==========================\n';
  body += 'Date: ' + report.date + '\n';
  body += 'Account: ' + report.accountName + '\n';
  body += 'Break-Even ROAS Target: ' + CONFIG.BREAK_EVEN_ROAS + 'x\n\n';

  if (report.alerts.length > 0) {
    body += '⚠️ ALERTS:\n';
    body += '─────────\n';
    for (var i = 0; i < report.alerts.length; i++) {
      var alert = report.alerts[i];
      body += '• [' + alert.type + '] ' + alert.campaign + '\n';
      body += '  ' + alert.message + '\n';
      body += '  Previous: ' + alert.previous + ' → Current: ' + alert.current + '\n\n';
    }
  }

  if (report.recommendations.length > 0) {
    body += '📊 RECOMMENDATIONS:\n';
    body += '──────────────────\n';
    for (var j = 0; j < report.recommendations.length; j++) {
      var rec = report.recommendations[j];
      body += '• [' + rec.action + '] ' + rec.campaign + '\n';
      body += '  ' + rec.reason + '\n\n';
    }
  }

  body += '\n---\nGenerated by Scaling Monitor Script';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}

function logSummary(report) {
  Logger.log('=== Scaling Monitor Summary ===');
  Logger.log('Campaigns analyzed: ' + report.campaigns.length);
  Logger.log('Alerts: ' + report.alerts.length);
  Logger.log('Recommendations: ' + report.recommendations.length);

  for (var i = 0; i < report.campaigns.length; i++) {
    var c = report.campaigns[i];
    Logger.log(c.name + ': ROAS=' + c.currentROAS.toFixed(2) +
               ', Spend Change=' + (c.spendChange * 100).toFixed(1) + '%' +
               (c.iROAS > 0 ? ', iROAS=' + c.iROAS.toFixed(2) : ''));
  }
}
```

## Scaling Roadmap Template

```markdown
# Scaling Roadmap

## Current State Analysis

### Account Metrics
- **Current Monthly Spend:** €[X]
- **Current ROAS:** [X.X]x
- **Break-Even ROAS:** [X.X]x
- **Margin Above Break-Even:** [X]%

### Scaling Potential Assessment
- **Impression Share:** [X]% (room to grow: [X]%)
- **Budget Limited Days:** [X] per month
- **Top Performers:** [Campaign names]
- **iROAS Estimate:** [X.X]x

## Scaling Plan

### Phase 1: Preparation (Week 1-2)
- [ ] Calculate break-even ROAS for all campaigns
- [ ] Identify top 3 scalable campaigns
- [ ] Set up incrementality tracking
- [ ] Document baseline metrics

### Phase 2: Conservative Scaling (Week 3-6)
| Week | Campaign | Budget Change | Target ROAS |
|------|----------|---------------|-------------|
| 3 | [Top 1] | +15% | >[X]x |
| 4 | [Top 1] | +15% | >[X]x |
| 5 | [Top 2] | +15% | >[X]x |
| 6 | [Top 2] | +15% | >[X]x |

### Phase 3: Evaluation (Week 7-8)
- [ ] Calculate true iROAS per campaign
- [ ] Compare MER before/after
- [ ] Identify diminishing returns point
- [ ] Adjust targets

### Phase 4: Optimization (Week 9+)
- [ ] Reallocate budget to highest iROAS
- [ ] Test horizontal expansion
- [ ] Implement learnings

## Budget Projection

| Month | Spend | Expected Revenue | Target ROAS |
|-------|-------|------------------|-------------|
| Current | €X | €X | X.Xx |
| +1 Month | €X (+X%) | €X | X.Xx |
| +2 Month | €X (+X%) | €X | X.Xx |
| +3 Month | €X (+X%) | €X | X.Xx |

## Success Criteria
- Maintain iROAS above [X.X]x
- Achieve [X]% spend increase
- MER decrease maximum [X]%

## Rollback Triggers
- iROAS drops below [X.X]x for 2 consecutive weeks
- CPA increases >30% vs baseline
- Quality Score drops significantly
```

---
name: competitive-analysis-toolkit
description: |
  Google Ads Competitive Analysis Toolkit for market analysis and competitor monitoring. Use when: analyzing Auction Insights, identifying competitor strategies, calculating market share, building competitive response strategies, or setting up Share of Voice monitoring. Do NOT use for: keyword strategy (use keyword-strategy-planner), bid strategy selection (use bid-strategy-selector), or campaign performance diagnosis (use performance-troubleshooter).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "google_ads"
  phase: "fase-4-measurement-attribution"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---
# Competitive Analysis Toolkit

Complete guide for analyzing competition in Google Ads, from Auction Insights interpretation to strategic response to competitor activities.

## Quick Analysis Guide

```
WHAT DO YOU WANT TO KNOW?
│
├─► WHO ARE MY COMPETITORS?
│   └─► Go to: "Auction Insights Basics"
│
├─► HOW DO COMPETITORS PERFORM VS ME?
│   └─► Go to: "Competitive Metrics Analysis"
│
├─► A COMPETITOR HAS BECOME MORE AGGRESSIVE
│   └─► Go to: "Competitive Response Strategy"
│
├─► HOW MUCH MARKET SHARE DO I HAVE?
│   └─► Go to: "Market Share Calculation"
│
├─► WHAT ARE COMPETITORS DOING IN THEIR ADS?
│   └─► Go to: "Competitor Ad Intelligence"
│
└─► HOW DO I MONITOR COMPETITORS CONTINUOUSLY?
    └─► Go to: "Competitive Monitoring Setup"
```

## Auction Insights Basics

### Where to Find

```
AUCTION INSIGHTS LOCATION
═════════════════════════

LEVEL 1: CAMPAIGN
──────────────────
Campaigns → Select campaign → Auction Insights

LEVEL 2: AD GROUP
─────────────────
Ad Groups → Select ad group → Auction Insights

LEVEL 3: KEYWORD
────────────────
Keywords → Select keywords → Auction Insights

⚠️ IMPORTANT:
├── Auction Insights only available with sufficient data
├── Minimum impressions needed for statistical relevance
├── Data is aggregated (no exact numbers)
└── Updates daily, not real-time
```

### Metrics Explained

```
AUCTION INSIGHTS METRICS EXPLAINED
═══════════════════════════════════

┌────────────────────────┬─────────────────────────────────────────────┐
│ Metric                 │ What It Measures                            │
├────────────────────────┼─────────────────────────────────────────────┤
│ Impression Share       │ % of impressions YOU received vs total      │
│                        │ available for your keywords                 │
├────────────────────────┼─────────────────────────────────────────────┤
│ Overlap Rate           │ % of YOUR impressions where competitor      │
│                        │ ALSO received an impression                 │
├────────────────────────┼─────────────────────────────────────────────┤
│ Position Above Rate    │ % of overlapping impressions where          │
│                        │ competitor was ABOVE you                    │
├────────────────────────┼─────────────────────────────────────────────┤
│ Top of Page Rate       │ % of impressions in top positions           │
│                        │ (above organic results)                     │
├────────────────────────┼─────────────────────────────────────────────┤
│ Abs. Top of Page Rate  │ % of impressions at FIRST position          │
│                        │ (absolute top)                              │
├────────────────────────┼─────────────────────────────────────────────┤
│ Outranking Share       │ % of auctions where you ranked ABOVE        │
│                        │ competitor OR appeared when they didn't      │
└────────────────────────┴─────────────────────────────────────────────┘

FORMULA RELATIONSHIPS:
──────────────────────
Outranking Share = (You higher) + (You appeared, they didn't)
                   ─────────────────────────────────────────
                   Total eligible auctions

Position Above Rate + Position Below Rate = 100%
(for overlapping auctions)

⚠️ NOTE: These metrics are relative to YOU, not absolute market shares.
```

### Interpretation Guide

```
HOW TO INTERPRET AUCTION INSIGHTS
══════════════════════════════════

SCENARIO 1: HIGH OVERLAP, LOW OUTRANKING
─────────────────────────────────────────
Overlap Rate: 85%
Outranking Share: 30%
Position Above Rate: 55%

Interpretation:
├── Competitor targets the same keywords
├── They win more often (rank above you)
├── Possible: Higher bids or better Quality Score

Action:
├── Check Quality Score difference
├── Evaluate bid strategy
├── Consider differentiation (different keywords)

SCENARIO 2: LOW OVERLAP, HIGH IMPRESSION SHARE
───────────────────────────────────────────────
Overlap Rate: 20%
Your Impression Share: 70%

Interpretation:
├── You dominate this keyword segment
├── Little direct competition
├── Possible: Niche or branded terms

Action:
├── Maintain position
├── Consider bid efficiency (don't overbid)
├── Explore expansion opportunities

SCENARIO 3: NEW COMPETITOR APPEARS
───────────────────────────────────
Week 1: Competitor not in insights
Week 2: Competitor with 40% overlap, 60% position above

Interpretation:
├── New market entrant
├── Aggressive bidding strategy
├── Impact on your impression share

Action:
├── Monitor trends
├── Analyze their ads (manual search)
├── Determine if response is needed

SCENARIO 4: COMPETITOR IMPRESSION SHARE RISING
──────────────────────────────────────────────
Competitor IS: 30% → 50% over 4 weeks
Your IS: 60% → 45% over 4 weeks

Interpretation:
├── Competitor is investing more
├── Your market share is declining
├── Direct competition is intensifying

Action:
├── Evaluate ROI of these keywords
├── Increase bids if profitable
├── Or: Shift to less competitive segments
```

## Competitive Metrics Analysis

### Benchmark Dashboard

```
COMPETITIVE BENCHMARK ANALYSIS
══════════════════════════════

STEP 1: EXPORT AUCTION INSIGHTS DATA
─────────────────────────────────────
Campaigns → Auction Insights → Download

Select period: Minimum 30 days

STEP 2: BUILD BENCHMARK TABLE
──────────────────────────────

For TOP 5 competitors:

┌─────────────────────────────────────────────────────────────────────────┐
│ Competitor   │ Imp Share │ Overlap │ Pos Above │ Outranking │ Trend    │
├──────────────┼───────────┼─────────┼───────────┼────────────┼──────────┤
│ You          │ 45%       │ -       │ -         │ -          │ Baseline │
│ Competitor A │ 52%       │ 78%     │ 55%       │ 42%        │ ↑ +5%   │
│ Competitor B │ 38%       │ 65%     │ 35%       │ 58%        │ → Stable│
│ Competitor C │ 30%       │ 45%     │ 20%       │ 72%        │ ↓ -8%   │
│ Competitor D │ 25%       │ 40%     │ 50%       │ 48%        │ NEW     │
│ Competitor E │ 18%       │ 30%     │ 25%       │ 68%        │ → Stable│
└──────────────┴───────────┴─────────┴───────────┴────────────┴──────────┘

STEP 3: CALCULATE COMPETITIVE INDEX
────────────────────────────────────
Per competitor:

Threat Score = (Overlap Rate × Position Above Rate) / 100

Example:
├── Competitor A: (78% × 55%) / 100 = 42.9 (HIGH)
├── Competitor B: (65% × 35%) / 100 = 22.8 (MEDIUM)
└── Competitor C: (45% × 20%) / 100 = 9.0 (LOW)

Prioritize focus on highest Threat Scores.
```

### Trend Analysis

```
COMPETITIVE TREND TRACKING
═══════════════════════════

WEEK-OVER-WEEK ANALYSIS:
─────────────────────────
Track per competitor:

Week 1 → Week 2 → Week 3 → Week 4

Metrics to track:
├── Impression Share delta
├── Position Above Rate delta
├── Outranking Share delta
└── New appearances

SIGNALS OF COMPETITOR ACTIVITY:
───────────────────────────────

AGGRESSIVE EXPANSION:
├── Impression Share rising >10% per week
├── New keywords where overlap appears
├── Rising Position Above Rate
└── Action: Analyze strategy, consider response

STABLE COMPETITION:
├── Metrics +/- 5% range
├── No new competitors
├── Predictable patterns
└── Action: Maintain current strategy

COMPETITOR RETREAT:
├── Declining Impression Share
├── Declining Overlap Rate
├── Disappearing from insights
└── Action: Opportunity to capture market share

SEASONALITY IN COMPETITION:
───────────────────────────
Track year-over-year:
├── Q4: E-commerce competitors more aggressive
├── January: B2B budget renewals
├── Industry-specific patterns
└── Plan budget/bids around competitive peaks
```

## Market Share Calculation

### Impression Share as Proxy

```
MARKET SHARE CALCULATION
════════════════════════

METHOD 1: IMPRESSION SHARE BASIS
─────────────────────────────────
Your Impression Share indicates your share
of the total available volume.

Example:
├── Your Search Impression Share: 45%
├── Interpretation: You capture 45% of eligible searches
└── Remaining 55%: Competitors or missed opportunities

Refinement:
├── Lost IS (Budget): 20%
├── Lost IS (Rank): 35%
├── Your Share: 45%
└── Total: 100%

If you had budget and improved rank:
├── Potential Share: 45% + 35% (rank) = 80%
└── Budget-constrained ceiling: 45% + 20% = 65%

METHOD 2: RELATIVE MARKET SHARE
────────────────────────────────
Calculate your share relative to known competitors:

Total Known IS = Your IS + Sum(Competitor IS)

Your Relative Share = Your IS / Total Known IS

Example:
├── Your IS: 45%
├── Competitor A: 52%
├── Competitor B: 38%
├── Competitor C: 30%
├── Total Known: 165%* (overlap means >100% possible)
└── Your Relative: 45/165 = 27%

*Note: Overlap means the sum can exceed 100%

METHOD 3: SHARE OF VOICE (SOV)
──────────────────────────────
Share of Voice = Your Impressions / Total Market Impressions

Problem: You don't know total market impressions.

Proxy:
├── Use Keyword Planner for search volumes
├── Your impressions / Estimated total searches
└── Provides an indication of SOV

Example:
├── Keywords: 100,000 monthly searches (KW Planner)
├── Your impressions: 40,000 (Google Ads)
├── SOV: 40,000 / 100,000 = 40%
```

### Competitive Position Matrix

```
COMPETITIVE POSITION MATRIX
════════════════════════════

Plot competitors on 2 axes:

Y-axis: Impression Share (market presence)
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

QUADRANT INTERPRETATION:
────────────────────────

DOMINANT PLAYERS (High IS, High Position Above):
├── Large budgets
├── Strong Quality Scores
├── Difficult to beat directly
└── Strategy: Differentiate, niche down

MARKET LEADERS (High IS, Low Position Above):
├── High volume, but not always on top
├── Possibly broad targeting
├── Opportunity: Outbid on specifics
└── Strategy: Focus on high-value auctions

AGGRESSIVE CHALLENGERS (Low IS, High Position Above):
├── Selective but aggressive bidding
├── Cherry-picking best opportunities
├── Strong on specific segments
└── Strategy: Monitor and learn

NICHE PLAYERS (Low IS, Low Position Above):
├── Small players
├── Limited competition
├── Possible future threats
└── Strategy: Monitor for growth
```

## Competitor Ad Intelligence

### Manual Research

```
COMPETITOR AD RESEARCH
══════════════════════

METHOD 1: MANUAL SEARCH
────────────────────────
□ Open incognito/private browser
□ Search your most important keywords
□ Note:
  ├── Which competitors appear
  ├── Ad positions
  ├── Headlines and descriptions
  ├── Extensions in use
  ├── Offers and promotions
  └── Landing page URLs

TEMPLATE FOR AD NOTES:
──────────────────────
Keyword: [keyword]
Date: [date]

Competitor A:
├── Position: [1/2/3/etc]
├── Headline 1: "[text]"
├── Headline 2: "[text]"
├── Headline 3: "[text]"
├── Description: "[text]"
├── Extensions: [Sitelinks/Callouts/etc]
├── Offer: [Discount/Free/etc]
└── Landing Page: [URL]

Competitor B:
└── ...

FREQUENCY:
├── Weekly check: Top 10 keywords
├── Monthly deep dive: Top 50 keywords
└── Event-based: When major competitor changes occur

METHOD 2: GOOGLE ADS TRANSPARENCY CENTER
─────────────────────────────────────────
https://adstransparency.google.com/

□ Search by competitor name
□ See all ads they are running
□ Filter by region, time, format
□ View creative variations

Limitations:
├── Only active ads
├── No performance data
└── No targeting info
```

### Competitor Strategy Patterns

```
RECOGNIZING COMPETITOR STRATEGIES
═════════════════════════════════

PATTERN 1: AGGRESSIVE MARKET SHARE
───────────────────────────────────
Signals:
├── High bids (top positions always)
├── Broad keyword coverage
├── Aggressive offers in ads
└── High Impression Share across all terms

Likely strategy:
├── Growth/market share focus
├── Venture-backed or new to market
├── Willing to lose money for share
└── Can be expensive long-term

Your response:
├── DO NOT match (cost war you'll lose)
├── Focus on efficiency and niche
├── Wait until they optimize or stop
└── Differentiate on value, not price

PATTERN 2: CHERRY-PICKING
──────────────────────────
Signals:
├── High position only on specific keywords
├── Low Impression Share overall
├── Very targeted approach
└── Premium ads on high-value terms

Likely strategy:
├── ROI-focused
├── Only bidding where profitable
├── Smart optimization
└── Sustainable approach

Your response:
├── Identify keywords where they are NOT present
├── Test their high-value keywords (competitive)
├── Learn from their keyword selection
└── Match quality, not volume

PATTERN 3: DEFENSIVE/BRAND
───────────────────────────
Signals:
├── Dominant only on own brand terms
├── Low presence on generic terms
├── High IS on branded
└── Minimal non-brand activity

Likely strategy:
├── Protect existing traffic
├── Minimal acquisition focus
├── Cost-efficient
└── Mature/established player

Your response:
├── Opportunity on non-brand
├── Be cautious with competitor conquesting
├── Focus on generics where they are absent
└── Build your own brand

PATTERN 4: PROMOTIONAL SURGE
─────────────────────────────
Signals:
├── Sudden IS increase
├── Aggressive offers in ads
├── Temporary (sales periods)
└── Returns to baseline after event

Likely strategy:
├── Seasonal/event-driven
├── Sale periods
├── Product launches
└── Short-term focus

Your response:
├── Track timing and patterns
├── Plan your own promotions strategically
├── Avoid direct competition during peaks
└── Capture traffic when they normalize
```



See [decision-trees.md](references/decision-trees.md) for details.



## Competitive Monitoring Setup

### Automated Alerts

```
COMPETITIVE MONITORING ALERTS
═════════════════════════════

ALERT 1: IMPRESSION SHARE DROP
──────────────────────────────
Trigger: Your IS drops >15% week-over-week
Action: Email alert
Cause: Competitor more aggressive or your issue
Response: Investigate root cause

ALERT 2: NEW COMPETITOR
───────────────────────
Trigger: New domain name in Auction Insights
Action: Email alert with competitor details
Cause: Market entry
Response: Analyze and monitor

ALERT 3: POSITION LOSS
──────────────────────
Trigger: Avg position drops >0.5 or Top IS drops >20%
Action: Email alert
Cause: Competitor bids, your QS, or budget
Response: Diagnose and adjust

ALERT 4: CPC SPIKE
──────────────────
Trigger: Avg CPC rises >20%
Action: Email alert
Cause: Competitive pressure or QS decline
Response: Check auction insights for correlation

SETUP VIA GOOGLE ADS RULES:
───────────────────────────
Tools → Bulk Actions → Rules → Create Rule

Example:
├── Rule Type: Email when...
├── Condition: Search Impr. Share < 40%
├── Frequency: Weekly
└── Action: Send email to team
```

### Weekly Competitive Review

```
WEEKLY COMPETITIVE REVIEW CHECKLIST
════════════════════════════════════

EVERY MONDAY (15-30 min):
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

MONTHLY DEEP DIVE (1 hour):
────────────────────────────

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
 * Monitors proxy metrics and impression share,
 * sending alerts on significant competitor changes.
 *
 * Note: Auction Insights data is not directly available via API.
 * This script monitors proxy metrics and impression share.
 *
 * Setup:
 * 1. Adjust CONFIG
 * 2. Schedule: Daily
 */

var CONFIG = {
  EMAIL: 'your@email.com',

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
      message: 'Impressions dropped by ' +
               (Math.abs(metrics.impressionChange) * 100).toFixed(1) + '%',
      current: current.impressions,
      previous: previous.impressions,
      possibleCause: 'Competitor activity or budget/bid issues'
    });
  }

  // CPC increase alert
  if (metrics.cpcChange >= CONFIG.CPC_INCREASE_THRESHOLD &&
      previous.avgCpc > 0) {
    alerts.push({
      campaign: name,
      type: 'CPC_SPIKE',
      severity: 'WARNING',
      message: 'Average CPC increased by ' +
               (metrics.cpcChange * 100).toFixed(1) + '%',
      current: '€' + current.avgCpc.toFixed(2),
      previous: '€' + previous.avgCpc.toFixed(2),
      possibleCause: 'Increased competition or Quality Score decline'
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
      possibleCause: 'Budget or bid limitations, or strong competition'
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
- **Reporting period:** [Date range]
- **Market position:** [Leader/Challenger/Follower]
- **Key trend:** [Describe main development]
- **Action required:** [Yes/No + brief explanation]

## Competitive Landscape

### Top Competitors
| Competitor | Imp Share | Overlap | Position Above | Outranking | Trend |
|------------|-----------|---------|----------------|------------|-------|
| [You] | [X]% | - | - | - | Baseline |
| [Comp A] | [X]% | [X]% | [X]% | [X]% | [up/down/stable] |
| [Comp B] | [X]% | [X]% | [X]% | [X]% | [up/down/stable] |
| [Comp C] | [X]% | [X]% | [X]% | [X]% | [up/down/stable] |

### Market Dynamics
- **New entrants:** [Describe]
- **Departing competitors:** [Describe]
- **Trend in competition intensity:** [Increasing/Stable/Decreasing]

## Competitor Deep Dives

### [Competitor A]
**Strategy type:** [Aggressive/Selective/Defensive]

**Observed tactics:**
- [Tactic 1]
- [Tactic 2]
- [Tactic 3]

**Ad messaging:**
- Headlines: [Example headlines]
- Offers: [Promotions/deals]
- USPs: [Unique selling points]

**Threat level:** [High/Medium/Low]

### [Competitor B]
[Same structure]

## Strategic Recommendations

### Immediate Actions (This Week)
1. [Action 1] - [Rationale]
2. [Action 2] - [Rationale]

### Short-term Actions (This Month)
1. [Action 1] - [Rationale]
2. [Action 2] - [Rationale]

### Long-term Strategy
- [Strategic direction]
- [Investment areas]
- [Differentiation opportunities]

## Monitoring Plan
- **Daily:** [Metrics to check]
- **Weekly:** [Review activities]
- **Monthly:** [Deep dive analyses]

## Appendix
- Raw Auction Insights data
- Competitor ad screenshots
- Historical trend charts
```

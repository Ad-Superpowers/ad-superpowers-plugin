---
name: automated-rules-builder
description: "Google Ads automated rules en automation setup. Gebruik voor: (1) Automated rules configuratie, (2) Budget management automation, (3) Bid adjustment rules, (4) Performance alerts, (5) Scheduling automation, (6) Scripts vs rules advies. Triggers: automated rules, automation, scheduling, alerts, budget rules, bid rules, pause rules, enable rules."
---

# Automated Rules Builder

Complete gids voor Google Ads automated rules - van budget management tot performance alerts en bid optimalisatie.

## Quick Decision Guide

```
AUTOMATED RULES OF SCRIPTS?
│
├─► Simpele actie, UI-configureerbaar
│   └─► AUTOMATED RULES
│       ├── Geen code nodig
│       ├── Makkelijk te beheren
│       └── Beperkte logica mogelijkheden
│
├─► Complexe logica, meerdere condities
│   └─► GOOGLE ADS SCRIPTS
│       ├── JavaScript code
│       ├── Meer flexibiliteit
│       └── Externe data integratie mogelijk
│
├─► Real-time optimalisatie
│   └─► SMART BIDDING + RULES COMBO
│       ├── Laat Google AI bieden
│       └── Rules voor edge cases
│
└─► Multi-account management
    └─► MCC SCRIPTS
        ├── Cross-account automation
        └── Centrale monitoring
```

## Automated Rules Overzicht

### Wat Zijn Automated Rules?

```
GOOGLE ADS AUTOMATED RULES
══════════════════════════

DEFINITIE:
──────────
Automated rules zijn IF-THEN statements die Google Ads
automatisch uitvoert op basis van performance data.

IF [conditie is waar] THEN [voer actie uit]

VOORDELEN:
──────────
✓ Geen technische kennis nodig
✓ UI-based configuratie
✓ Betrouwbare uitvoering
✓ Email notificaties
✓ Audit trail

BEPERKINGEN:
────────────
✗ Beperkte conditie combinaties
✗ Geen custom calculaties
✗ Geen externe data bronnen
✗ Max 1 actie per rule
✗ Geen real-time uitvoering

WAAR TE VINDEN:
───────────────
Google Ads → Tools & Settings → Bulk Actions → Rules

RULE COMPONENTEN:
─────────────────
┌────────────────────────────────────────────────────────────┐
│ 1. APPLY TO: Wat wordt beïnvloed?                          │
│    ├── Campaigns                                            │
│    ├── Ad Groups                                            │
│    ├── Keywords                                             │
│    ├── Ads                                                  │
│    └── Extensions                                           │
├────────────────────────────────────────────────────────────┤
│ 2. ACTION: Wat moet er gebeuren?                           │
│    ├── Enable / Pause                                       │
│    ├── Change budget                                        │
│    ├── Change bid                                           │
│    ├── Send email                                           │
│    └── Change labels                                        │
├────────────────────────────────────────────────────────────┤
│ 3. CONDITIONS: Wanneer moet het gebeuren?                  │
│    ├── Performance metrics (CPA, CTR, etc.)                │
│    ├── Status condities                                     │
│    ├── Label condities                                      │
│    └── Budget condities                                     │
├────────────────────────────────────────────────────────────┤
│ 4. FREQUENCY: Hoe vaak controleren?                        │
│    ├── Hourly (elk uur)                                    │
│    ├── Daily (dagelijks)                                   │
│    ├── Weekly (wekelijks)                                  │
│    └── Monthly (maandelijks)                               │
└────────────────────────────────────────────────────────────┘
```

## Essential Automated Rules

### Budget Management Rules

```
BUDGET PROTECTION RULES
═══════════════════════

RULE 1: PAUSE CAMPAIGN BIJ BUDGET OVERSCHRIJDING
────────────────────────────────────────────────
Doel: Voorkom overspend op campagneniveau

Apply to: All enabled campaigns
Action: PAUSE campaign
Condition: Cost > [Maximum dagbudget]
           Date range: Same day
Frequency: Hourly

Voorbeeld:
├── Max budget: €500/dag
├── Condition: Cost > €475 (margin inbouwen)
└── Alert: Email bij elke uitvoering


RULE 2: BUDGET VERHOGEN BIJ GOEDE PERFORMANCE
─────────────────────────────────────────────
Doel: Schaal winning campaigns automatisch

Apply to: Enabled campaigns with label "Auto-Scale"
Action: INCREASE budget by 15%
Conditions:
├── CPA < €30 (jouw target CPA)
├── Conversions >= 5
├── Cost > €100 (significant spend)
Date range: Previous 7 days
Frequency: Weekly (Monday 8:00)
Max budget: €500/dag (limiet instellen)

Preview first! Controleer welke campagnes affected.


RULE 3: BUDGET VERLAGEN BIJ SLECHTE PERFORMANCE
────────────────────────────────────────────────
Doel: Limiteer spend op underperformers

Apply to: Enabled campaigns with label "Auto-Scale"
Action: DECREASE budget by 20%
Conditions:
├── CPA > €50 (boven target)
├── Cost > €100
├── Conversions > 0 (er is data)
Date range: Previous 7 days
Frequency: Weekly (Monday 8:00)
Min budget: €20/dag (niet te laag)


RULE 4: MONTHLY BUDGET PACING
─────────────────────────────
Doel: Voorkom maandelijkse overspend

Apply to: All enabled campaigns
Action: Send email notification
Conditions:
├── Cost > [Maandbudget * (dag/dagen_in_maand) * 1.1]
Date range: This month
Frequency: Daily (9:00)

Note: Bereken de verwachte spend ratio handmatig per dag.
```

### Bid Management Rules

```
BID ADJUSTMENT RULES
════════════════════

RULE 5: VERHOOG BID VOOR TOP PERFORMERS
───────────────────────────────────────
Doel: Meer volume voor winnende keywords

Apply to: Keywords with label "Auto-Bid"
Action: INCREASE bid by 10%
Conditions:
├── Status: Enabled
├── CPA < €25 (onder target)
├── Impressions > 100
├── Clicks >= 5
├── Avg Position < 3 (optioneel: top positie check)
Date range: Previous 14 days
Frequency: Weekly
Max CPC: €5.00 (cap instellen)


RULE 6: VERLAAG BID VOOR UNDERPERFORMERS
────────────────────────────────────────
Doel: Reduceer spend op slechte keywords

Apply to: Keywords with label "Auto-Bid"
Action: DECREASE bid by 15%
Conditions:
├── Status: Enabled
├── CPA > €40 (boven target)
├── Cost > €50
├── Conversions < 2
Date range: Previous 14 days
Frequency: Weekly
Min CPC: €0.50 (niet te laag voor visibility)


RULE 7: PAUSE KEYWORDS ZONDER CONVERSIES
────────────────────────────────────────
Doel: Stop spend op non-converters

Apply to: All enabled keywords
Action: PAUSE keyword
Conditions:
├── Cost > €100
├── Conversions = 0
Date range: Previous 30 days
Frequency: Weekly

⚠️ WAARSCHUWING: Preview altijd eerst!
   Check of er geen valuable awareness keywords gepausd worden.


RULE 8: REACTIVEER GEPAUSEERDE KEYWORDS (Seasonal)
──────────────────────────────────────────────────
Doel: Heractiveer keywords voor seizoensperiodes

Apply to: Paused keywords with label "Seasonal-Q4"
Action: ENABLE keyword
Conditions: None (activate all with label)
Frequency: One time / Manual trigger

Tip: Gebruik labels voor seizoensgebonden items:
├── "Seasonal-Q4" voor holiday season
├── "Seasonal-Summer" voor zomer
└── "Seasonal-BTS" voor back to school
```

### Performance Alert Rules

```
MONITORING & ALERT RULES
════════════════════════

RULE 9: CPA SPIKE ALERT
───────────────────────
Doel: Onmiddellijke notificatie bij CPA stijging

Apply to: All enabled campaigns
Action: Send email notification
Conditions:
├── CPA > €50 (jouw max acceptable CPA)
├── Conversions >= 3 (genoeg data)
├── Cost > €100
Date range: Previous 3 days
Frequency: Daily (9:00)


RULE 10: CTR DROP ALERT
───────────────────────
Doel: Detecteer mogelijke ad fatigue of issues

Apply to: All enabled ad groups
Action: Send email notification
Conditions:
├── CTR < 1% (onder benchmark)
├── Impressions > 500
Date range: Previous 7 days
Frequency: Weekly


RULE 11: QUALITY SCORE DROP ALERT
─────────────────────────────────
Doel: Monitor Quality Score dalingen

Apply to: Keywords with label "Monitor-QS"
Action: Send email notification
Conditions:
├── Quality Score < 5
├── Status: Enabled
├── Impressions > 100
Date range: Previous 30 days
Frequency: Weekly


RULE 12: ZERO IMPRESSIONS ALERT
───────────────────────────────
Doel: Detecteer campaigns zonder delivery

Apply to: All enabled campaigns
Action: Send email notification
Conditions:
├── Impressions = 0
├── Budget > €10
Date range: Yesterday
Frequency: Daily (10:00)


RULE 13: CONVERSION TRACKING ISSUE ALERT
────────────────────────────────────────
Doel: Detecteer mogelijke tracking problemen

Apply to: All enabled campaigns
Action: Send email notification
Conditions:
├── Clicks > 100
├── Conversions = 0
├── Historical conversion rate > 1% (verwacht conversies)
Date range: Yesterday
Frequency: Daily
```

### Scheduling Rules

```
SCHEDULING AUTOMATION
═════════════════════

RULE 14: WEEKDAY ONLY CAMPAIGNS
───────────────────────────────
Doel: Pauzeer campagnes in het weekend

RULE A - Pause Friday evening:
Apply to: Campaigns with label "Weekdays-Only"
Action: PAUSE campaign
Frequency: Weekly, Friday at 22:00

RULE B - Enable Monday morning:
Apply to: Paused campaigns with label "Weekdays-Only"
Action: ENABLE campaign
Frequency: Weekly, Monday at 06:00


RULE 15: BUSINESS HOURS ONLY
────────────────────────────
Doel: Alleen adverteren tijdens kantooruren

RULE A - Enable morning:
Apply to: Campaigns with label "Business-Hours"
Action: ENABLE campaign
Frequency: Daily (Weekdays), at 08:00

RULE B - Pause evening:
Apply to: Campaigns with label "Business-Hours"
Action: PAUSE campaign
Frequency: Daily (Weekdays), at 18:00


RULE 16: SEASONAL CAMPAIGN ACTIVATION
─────────────────────────────────────
Doel: Automatische activatie voor promotieperiodes

Enable Rule:
Apply to: Campaigns with label "BlackFriday2025"
Action: ENABLE campaign
Frequency: One time, specific date (bijv. 20 Nov 09:00)

Pause Rule:
Apply to: Campaigns with label "BlackFriday2025"
Action: PAUSE campaign
Frequency: One time, specific date (bijv. 2 Dec 23:00)


RULE 17: PAYDAY BUDGET BOOST
────────────────────────────
Doel: Verhoog budget rond betaaldagen (25e-5e)

Apply to: Campaigns with label "Payday-Boost"
Action: INCREASE budget by 30%
Frequency: Monthly, 24th at 06:00

Reset Rule:
Apply to: Campaigns with label "Payday-Boost"
Action: Set budget to [original value]
Frequency: Monthly, 6th at 06:00

Tip: Noteer originele budgets voor de reset.
```

## Advanced Rule Strategies

### Rule Combinations

```
LAYERED AUTOMATION STRATEGY
═══════════════════════════

TIER 1: PROTECTION RULES (Hoogste prioriteit)
──────────────────────────────────────────────
├── Budget overschrijding prevention
├── Zero conversion pauses (na €100+ spend)
└── Anomaly detection alerts

TIER 2: OPTIMIZATION RULES
──────────────────────────
├── Bid adjustments (weekly)
├── Budget scaling (weekly)
└── Performance-based pauses

TIER 3: SCHEDULING RULES
────────────────────────
├── Time-based enables/pauses
├── Day-of-week adjustments
└── Seasonal activations

TIER 4: MONITORING RULES
────────────────────────
├── Performance alerts
├── Tracking issue detection
└── Competitive alerts

EXECUTION ORDER:
────────────────
Protection > Optimization > Scheduling > Monitoring

Run protection rules eerst (hourly) zodat ze andere
rules kunnen overrulen indien nodig.
```

### Labels voor Rule Management

```
LABEL STRATEGY VOOR AUTOMATED RULES
═══════════════════════════════════

LABEL NAMING CONVENTION:
────────────────────────
[Category]-[Specifiek]

Categories:
├── Auto- : Automated rule target
├── Exclude- : Exclude from automation
├── Monitor- : Monitoring only
├── Seasonal- : Seizoensgebonden
└── Test- : A/B test items

VOORBEELDEN:
────────────
├── Auto-Scale         → Budget scaling rules
├── Auto-Bid           → Bid adjustment rules
├── Auto-Pause         → Auto-pause kandidaten
├── Exclude-Rules      → Nooit automatisch aanpassen
├── Monitor-QS         → Quality Score monitoring
├── Monitor-CPA        → CPA threshold monitoring
├── Seasonal-Q4        → Q4 / Holiday campaigns
├── Seasonal-Summer    → Zomercampagnes
├── Test-Creative      → Creative testing
└── Test-Bid           → Bid experiment

LABEL TOEPASSING:
─────────────────
Google Ads → Campaigns/Ad Groups/Keywords
→ Select items → Apply labels

Tip: Maak labels voordat je rules maakt.
     Rules kunnen alleen targeten op bestaande labels.
```

## Google Ads Script Equivalenten

### Wanneer Scripts vs Rules

```
RULES VS SCRIPTS DECISION GUIDE
═══════════════════════════════

USE AUTOMATED RULES WHEN:
─────────────────────────
✓ Simpele IF-THEN logica
✓ Single condition/action
✓ Standard metrics (CPA, CTR, etc.)
✓ Geen externe data nodig
✓ Snelle setup gewenst
✓ Non-technical team

USE SCRIPTS WHEN:
─────────────────
✓ Complexe berekeningen (bijv. ROAS thresholds)
✓ Meerdere conditions combineren
✓ Externe data integratie (spreadsheets, API)
✓ Cross-entity logic (campaign + ad group)
✓ Custom reporting
✓ MCC-level automation
✓ Geavanceerde alerting

HYBRID APPROACH:
────────────────
Rules voor: Simple, time-sensitive actions
Scripts voor: Complex logic, reporting
PMax/Smart bidding: Real-time optimization

VOORBEELD:
──────────
Automated Rule: Pause keyword if CPA > €50
Script: Analyze N-grams en stuur rapport met suggesties
Smart Bidding: Real-time bid optimization
```

### Script Templates voor Common Rules

```javascript
/**
 * Advanced Budget Protection Script
 *
 * Dit script biedt geavanceerde budget protection
 * die verder gaat dan automated rules.
 *
 * Features:
 * - Multi-campaign budget caps
 * - Rolling window analysis
 * - Slack/email alerts
 * - Automatic recovery
 *
 * Schedule: Hourly
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Account-level daily cap
  ACCOUNT_DAILY_CAP: 1000,  // €1000 per dag

  // Campaign-level caps (optional)
  CAMPAIGN_CAPS: {
    'Brand Campaign': 200,
    'Generic Campaign': 300
  },

  // Auto-pause or alert only
  AUTO_PAUSE: true,

  // Recovery: Re-enable next day
  AUTO_RECOVERY: true
};

function main() {
  var today = new Date();
  var todayString = Utilities.formatDate(today, AdsApp.currentAccount().getTimeZone(), 'yyyyMMdd');

  // Get total account spend today
  var accountStats = AdsApp.currentAccount().getStatsFor(todayString, todayString);
  var totalSpend = accountStats.getCost();

  Logger.log('Total spend today: €' + totalSpend.toFixed(2));

  // Check account-level cap
  if (totalSpend >= CONFIG.ACCOUNT_DAILY_CAP) {
    var message = 'Account daily cap reached: €' + totalSpend.toFixed(2) + ' / €' + CONFIG.ACCOUNT_DAILY_CAP;

    if (CONFIG.AUTO_PAUSE) {
      pauseAllCampaigns();
      message += '\nAll campaigns have been paused.';
    }

    sendAlert('Budget Cap Reached', message);
    return;
  }

  // Check campaign-level caps
  for (var campaignName in CONFIG.CAMPAIGN_CAPS) {
    var cap = CONFIG.CAMPAIGN_CAPS[campaignName];

    var campaigns = AdsApp.campaigns()
      .withCondition('Name = "' + campaignName + '"')
      .withCondition('Status = ENABLED')
      .get();

    while (campaigns.hasNext()) {
      var campaign = campaigns.next();
      var stats = campaign.getStatsFor(todayString, todayString);
      var spend = stats.getCost();

      if (spend >= cap) {
        var msg = campaignName + ' reached cap: €' + spend.toFixed(2) + ' / €' + cap;

        if (CONFIG.AUTO_PAUSE) {
          campaign.pause();
          // Add label for recovery
          campaign.applyLabel('AutoPaused-Budget');
          msg += ' - Campaign paused.';
        }

        sendAlert('Campaign Budget Cap', msg);
      }
    }
  }

  // Auto-recovery: Re-enable paused campaigns from yesterday
  if (CONFIG.AUTO_RECOVERY) {
    recoverPausedCampaigns();
  }
}

function pauseAllCampaigns() {
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    campaign.pause();
    campaign.applyLabel('AutoPaused-Budget');
  }
}

function recoverPausedCampaigns() {
  // Check if label exists
  var labelIterator = AdsApp.labels()
    .withCondition('Name = "AutoPaused-Budget"')
    .get();

  if (!labelIterator.hasNext()) return;

  var campaigns = AdsApp.campaigns()
    .withCondition('LabelNames CONTAINS_ANY ["AutoPaused-Budget"]')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    campaign.enable();
    campaign.removeLabel('AutoPaused-Budget');
    Logger.log('Re-enabled: ' + campaign.getName());
  }
}

function sendAlert(subject, body) {
  var fullSubject = '⚠️ ' + subject + ' - ' + AdsApp.currentAccount().getName();
  MailApp.sendEmail(CONFIG.EMAIL, fullSubject, body);
  Logger.log('Alert sent: ' + subject);
}
```

```javascript
/**
 * Multi-Condition Performance Rule Script
 *
 * Meer geavanceerd dan automated rules:
 * combineer meerdere condities met AND/OR logic.
 *
 * Schedule: Daily
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Complex rule: Pause if ALL conditions met
  PAUSE_CONDITIONS: {
    minCost: 100,           // Spend > €100
    maxConversions: 0,      // 0 conversions
    minImpressions: 500,    // Had enough impressions
    dateRange: 'LAST_14_DAYS'
  },

  // Alert if ANY condition met
  ALERT_CONDITIONS: [
    { metric: 'CPA', operator: '>', value: 50, dateRange: 'LAST_7_DAYS' },
    { metric: 'CTR', operator: '<', value: 0.01, dateRange: 'LAST_7_DAYS' },
    { metric: 'ConvRate', operator: '<', value: 0.005, dateRange: 'LAST_7_DAYS' }
  ],

  // Dry run mode
  DRY_RUN: true
};

function main() {
  var keywordsToPause = [];
  var alertItems = [];

  var keywords = AdsApp.keywords()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignStatus = ENABLED')
    .withCondition('AdGroupStatus = ENABLED')
    .get();

  while (keywords.hasNext()) {
    var keyword = keywords.next();
    var stats = keyword.getStatsFor(CONFIG.PAUSE_CONDITIONS.dateRange);

    var cost = stats.getCost();
    var conversions = stats.getConversions();
    var impressions = stats.getImpressions();
    var clicks = stats.getClicks();

    // Check pause conditions (ALL must be true)
    if (cost >= CONFIG.PAUSE_CONDITIONS.minCost &&
        conversions <= CONFIG.PAUSE_CONDITIONS.maxConversions &&
        impressions >= CONFIG.PAUSE_CONDITIONS.minImpressions) {

      keywordsToPause.push({
        text: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        cost: cost,
        impressions: impressions,
        keyword: keyword
      });
    }

    // Check alert conditions (ANY can trigger)
    var cpa = conversions > 0 ? cost / conversions : 0;
    var ctr = impressions > 0 ? clicks / impressions : 0;
    var convRate = clicks > 0 ? conversions / clicks : 0;

    for (var i = 0; i < CONFIG.ALERT_CONDITIONS.length; i++) {
      var condition = CONFIG.ALERT_CONDITIONS[i];
      var metricValue = 0;

      switch (condition.metric) {
        case 'CPA': metricValue = cpa; break;
        case 'CTR': metricValue = ctr; break;
        case 'ConvRate': metricValue = convRate; break;
      }

      var triggered = false;
      if (condition.operator === '>' && metricValue > condition.value) triggered = true;
      if (condition.operator === '<' && metricValue < condition.value && cost > 50) triggered = true;

      if (triggered) {
        alertItems.push({
          keyword: keyword.getText(),
          campaign: keyword.getCampaign().getName(),
          condition: condition.metric + ' ' + condition.operator + ' ' + condition.value,
          actualValue: metricValue
        });
        break; // One alert per keyword is enough
      }
    }
  }

  // Execute pauses
  if (keywordsToPause.length > 0) {
    for (var j = 0; j < keywordsToPause.length; j++) {
      if (!CONFIG.DRY_RUN) {
        keywordsToPause[j].keyword.pause();
      }
    }
  }

  // Send report
  if (keywordsToPause.length > 0 || alertItems.length > 0) {
    sendReport(keywordsToPause, alertItems);
  }

  Logger.log('Processed. To pause: ' + keywordsToPause.length + ', Alerts: ' + alertItems.length);
}

function sendReport(toPause, alerts) {
  var subject = '📊 Performance Rules Report - ' + AdsApp.currentAccount().getName();
  var dryRunNote = CONFIG.DRY_RUN ? '[DRY RUN] ' : '';

  var body = dryRunNote + 'Performance Rules Report\n';
  body += '========================\n\n';

  if (toPause.length > 0) {
    body += 'KEYWORDS TO PAUSE (' + toPause.length + '):\n';
    body += '───────────────────────────\n';
    for (var i = 0; i < Math.min(20, toPause.length); i++) {
      body += '• "' + toPause[i].text + '"\n';
      body += '  Campaign: ' + toPause[i].campaign + '\n';
      body += '  Spend: €' + toPause[i].cost.toFixed(2) + ', 0 conversions\n\n';
    }
  }

  if (alerts.length > 0) {
    body += '\nALERTS (' + alerts.length + '):\n';
    body += '─────────────────────\n';
    for (var j = 0; j < Math.min(20, alerts.length); j++) {
      body += '• "' + alerts[j].keyword + '"\n';
      body += '  Triggered: ' + alerts[j].condition + '\n';
      body += '  Actual: ' + alerts[j].actualValue.toFixed(4) + '\n\n';
    }
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Rule Management Best Practices

### Setup Checklist

```
AUTOMATED RULES SETUP CHECKLIST
═══════════════════════════════

VOOR ELKE RULE:
───────────────
□ Duidelijke naam (beschrijft actie + conditie)
□ Preview uitgevoerd en gecontroleerd
□ Email notificatie enabled
□ Correcte date range geselecteerd
□ Appropriate frequency gekozen
□ Labels toegepast waar nodig

NAMING CONVENTION:
──────────────────
[Actie]-[Object]-[Conditie]-[Frequentie]

Voorbeelden:
├── PAUSE-Keywords-NoCov100Spend-Weekly
├── ALERT-Campaigns-CPAOver50-Daily
├── BUDGET-Increase15-LowCPA-Weekly
├── ENABLE-Seasonal-BlackFriday-OneTime
└── BID-Decrease10-HighCPA-Weekly

DOCUMENTATIE:
─────────────
Maak een Google Sheet met:
├── Rule name
├── Purpose
├── Conditions
├── Action
├── Frequency
├── Last reviewed date
├── Owner

TESTING:
────────
1. Altijd PREVIEW voor activatie
2. Start met ALERT ONLY (geen actie)
3. Monitor 1-2 weken
4. Activeer actie na validatie
5. Review maandelijks
```

### Common Mistakes

```
VEELGEMAAKTE FOUTEN
═══════════════════

FOUT 1: Te agressieve thresholds
────────────────────────────────
✗ Pause bij eerste dag zonder conversies
✓ Wacht op voldoende data (€100+ spend)

FOUT 2: Geen maximum/minimum limieten
─────────────────────────────────────
✗ Verhoog bid 10% elke week (ongelimiteerd)
✓ Max CPC instellen op €5.00

FOUT 3: Verkeerde date range
────────────────────────────
✗ CPA check op "same day" (te weinig data)
✓ Gebruik 7-14 dagen voor betrouwbare metrics

FOUT 4: Geen preview voor activatie
───────────────────────────────────
✗ Activeer zonder te controleren welke items affected
✓ Altijd preview, screenshot results

FOUT 5: Conflicterende rules
────────────────────────────
✗ Rule A: Pause als CPA > 50
   Rule B: Enable als CPA < 60
   (Campaigns flippen continu aan/uit)
✓ Gebruik labels om conflicts te voorkomen
✓ Zorg voor duidelijke, niet-overlappende condities

FOUT 6: Geen recovery mechanisme
────────────────────────────────
✗ Automatisch pauzeren zonder re-enable logic
✓ Maak complementaire enable rules
✓ Gebruik labels voor tracking

FOUT 7: Over-automation
───────────────────────
✗ Rules voor alles, geen menselijke review
✓ Balans: Automation + periodieke manual review
```

### Monitoring & Maintenance

```
RULE MAINTENANCE SCHEDULE
═════════════════════════

DAGELIJKS:
──────────
□ Check email alerts
□ Review unexpected actions
□ Validate rule execution log

WEKELIJKS:
──────────
□ Review rule results
├── Hoeveel items affected?
├── Expected outcomes?
└── Any edge cases?

□ Check for conflicts
□ Adjust thresholds if needed

MAANDELIJKS:
────────────
□ Full rule audit
├── Zijn alle rules nog relevant?
├── Thresholds up to date?
└── Business goals veranderd?

□ Performance review
├── Impact op account performance
├── Time saved vs manual
└── Optimalisatie mogelijkheden

QUARTERLY:
──────────
□ Strategic review
├── Nieuwe automation opportunities
├── Rules die verwijderd kunnen worden
└── Script vs rule evaluatie

RULE AUDIT LOG:
───────────────
Google Ads → Tools → Change History
Filter: Automated rules
├── Wanneer uitgevoerd
├── Welke items affected
└── Wat was de actie
```

## Output: Automated Rules Template

```markdown
# Automated Rules Configuration Document

## Account Details
- **Account:** [Account naam]
- **Account ID:** [XXX-XXX-XXXX]
- **Rules Owner:** [Naam]
- **Last Review:** [Datum]

## Active Rules Overview

### Protection Rules
| Rule Name | Action | Condition | Frequency | Status |
|-----------|--------|-----------|-----------|--------|
| Budget-Cap-Pause | Pause campaign | Cost > €X | Hourly | Active |
| Zero-Conv-Pause | Pause keyword | Cost > €100, Conv = 0 | Weekly | Active |

### Optimization Rules
| Rule Name | Action | Condition | Frequency | Status |
|-----------|--------|-----------|-----------|--------|
| Bid-Increase-TopPerf | +10% bid | CPA < €X, Conv >= 5 | Weekly | Active |
| Bid-Decrease-LowPerf | -15% bid | CPA > €X | Weekly | Active |
| Budget-Scale-Winners | +15% budget | ROAS > X | Weekly | Active |

### Scheduling Rules
| Rule Name | Action | Condition | Frequency | Status |
|-----------|--------|-----------|-----------|--------|
| Weekday-Pause | Pause | Label: Weekdays-Only | Fri 22:00 | Active |
| Weekday-Enable | Enable | Label: Weekdays-Only | Mon 06:00 | Active |

### Alert Rules
| Rule Name | Alert Trigger | Frequency | Recipients |
|-----------|---------------|-----------|------------|
| CPA-Spike-Alert | CPA > €X | Daily | [emails] |
| CTR-Drop-Alert | CTR < 1% | Weekly | [emails] |
| Zero-Impr-Alert | Impr = 0 | Daily | [emails] |

## Labels in Use
| Label | Purpose | Applied To |
|-------|---------|-----------|
| Auto-Scale | Budget/bid automation | Campaigns |
| Auto-Bid | Bid adjustment automation | Keywords |
| Exclude-Rules | Never auto-modify | Various |
| Monitor-QS | QS monitoring | Keywords |

## Rule Dependencies
```
┌─────────────────────────────────────────┐
│ Protection Rules (Hourly)               │
│ ↓ Block optimization if budget cap hit │
├─────────────────────────────────────────┤
│ Optimization Rules (Weekly)             │
│ ↓ Adjust bids/budgets                   │
├─────────────────────────────────────────┤
│ Scheduling Rules (As scheduled)         │
│ ↓ Time-based enable/pause               │
├─────────────────────────────────────────┤
│ Alert Rules (Daily/Weekly)              │
│ → Notifications only                    │
└─────────────────────────────────────────┘
```

## Change Log
| Date | Rule | Change | Reason | By |
|------|------|--------|--------|-----|
| [Date] | [Rule name] | [What changed] | [Why] | [Name] |

## Notes
[Aanvullende opmerkingen over de automation setup]
```

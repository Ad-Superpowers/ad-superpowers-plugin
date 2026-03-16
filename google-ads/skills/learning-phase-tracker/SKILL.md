---
name: learning-phase-tracker
description: "Google Ads Smart Bidding Learning Phase tracker en optimizer. Gebruik voor: (1) Learning phase status monitoring, (2) Signalen en factoren die learning beïnvloeden, (3) Problemen oplossen met vastgelopen learning, (4) Learning phase duur voorspellen, (5) Best practices om learning te versnellen. Triggers: learning phase, learning limited, smart bidding learning, bid strategy learning, eligible, tcpa learning, troas learning, maximize conversions learning."
---

# Learning Phase Tracker

Complete gids voor het monitoren, begrijpen en optimaliseren van Google Ads Smart Bidding learning phases voor snellere en stabielere performance.

## Quick Decision Guide

```
LEARNING PHASE STATUS - WAT NU DOEN?
│
├─► STATUS: "Learning"
│   └─► WACHT EN OBSERVEER
│       ├── Normaal: 7-14 dagen
│       ├── GEEN wijzigingen maken
│       ├── Monitor dagelijks, niet ingrijpen
│       └── Verwacht fluctuaties in CPA/ROAS
│
├─► STATUS: "Learning (limited)"
│   └─► ACTIE VEREIST
│       ├── Check: Voldoende budget?
│       ├── Check: Voldoende conversies?
│       ├── Check: Tracking issues?
│       └── Zie: "Learning Limited Oplossen"
│
├─► STATUS: "Eligible"
│   └─► LEARNING VOLTOOID
│       ├── Nu kun je targets aanpassen
│       ├── Start met kleine wijzigingen (10%)
│       ├── Monitor performance
│       └── Optimaliseer indien stabiel
│
└─► STATUS: "Limited" (niet learning-gerelateerd)
    └─► ANDERE LIMITATIE
        ├── Budget limited?
        ├── Bid limited?
        ├── Target too restrictive?
        └── Zie: "Bid Status Problemen"
```

## Learning Phase Fundamentals

### Wat Is Learning Phase?

```
LEARNING PHASE UITLEG
═════════════════════

WAT GEBEURT ER:
├── Google's AI verzamelt data over jouw account
├── Analyseert welke signalen leiden tot conversies
├── Bouwt een prediction model
├── Bids worden dynamisch aangepast
└── Performance kan fluctueren

WAAROM HET NODIG IS:
├── Elk account is uniek
├── AI moet jouw specifieke patronen leren
├── Seizoenaliteit, audience, producten variëren
└── Generieke modellen zijn suboptimaal

DUUR VAN LEARNING:
────────────────────────────────────────
Typisch: 7-14 dagen (of ~50 conversies)

Kan langer duren bij:
├── Laag conversie volume
├── Inconsistente tracking
├── Onvoldoende budget
├── Zeer niche targeting
└── Nieuwe conversion actions

Kan korter zijn bij:
├── Hoog volume accounts
├── Consistent historisch patroon
├── Stabiele seizoenaliteit
└── Ervaring met vergelijkbare campaigns
```

### Learning Phase Signalen

```
SIGNALEN DIE SMART BIDDING GEBRUIKT
═══════════════════════════════════

REAL-TIME AUCTION SIGNALS:
├── Device (mobile, desktop, tablet)
├── Operating system
├── Browser
├── Location (geografisch, granular)
├── Time of day
├── Day of week
├── Search query (exact + intent)
└── Ad format/placement

HISTORICAL SIGNALS:
├── User's past behavior
├── Conversion patterns
├── Seasonal trends
├── Time-of-day performance
└── Device performance history

AUDIENCE SIGNALS:
├── Remarketing list membership
├── Similar audiences (indien actief)
├── Customer Match segments
├── Demographics (age, gender, income)
└── Affinities & in-market

CONTEXTUAL SIGNALS:
├── Ad relevance
├── Landing page quality
├── Ad position factors
├── Competitive auction dynamics
└── Query-ad match quality

⚠️ BELANGRIJK:
De AI leert welke COMBINATIES van signalen
leiden tot conversies in jouw specifieke situatie.
```

## Learning Phase Monitoring

### Status Controleren

```
WAAR LEARNING STATUS TE VINDEN
══════════════════════════════

LOCATIE 1: Campaign Level
─────────────────────────
Campaigns → Kolommen → Modify → Bid strategy
→ Voeg toe: "Bid strategy type" en "Bid strategy status"

LOCATIE 2: Bid Strategy Report
──────────────────────────────
Tools → Shared Library → Bid strategies
→ Zie "Status" kolom per strategy

LOCATIE 3: Recommendations Tab
──────────────────────────────
Recommendations → Scroll naar "Bidding"
→ Alerts over learning issues

STATUS INTERPRETATIE:
─────────────────────
┌─────────────────────┬─────────────────────────────────────────┐
│ Status              │ Betekenis                               │
├─────────────────────┼─────────────────────────────────────────┤
│ Learning            │ Actief aan het leren (7-14 dagen)       │
├─────────────────────┼─────────────────────────────────────────┤
│ Learning (limited)  │ Onvoldoende data om te leren            │
├─────────────────────┼─────────────────────────────────────────┤
│ Eligible            │ Learning voltooid, volledige            │
│                     │ optimalisatie actief                    │
├─────────────────────┼─────────────────────────────────────────┤
│ Misconfigured       │ Setup probleem (check conversion        │
│                     │ tracking)                               │
├─────────────────────┼─────────────────────────────────────────┤
│ Limited             │ Niet learning-gerelateerd (budget/bid)  │
└─────────────────────┴─────────────────────────────────────────┘
```

### Learning Duration Tracker

```
HOE LANG DUURT LEARNING?
════════════════════════

BASELINE VERWACHTINGEN:
──────────────────────
Nieuw account/campaign:
├── Minimaal: 7 dagen
├── Typisch: 10-14 dagen
├── Max (normaal): 21 dagen
└── Indicatie: ~50 conversies nodig

Bestaand account (wijziging):
├── Bid strategy switch: 7-14 dagen
├── Target aanpassing >20%: 7 dagen
├── Kleine target wijziging <10%: 3-5 dagen
└── Nieuwe conversion action: 14+ dagen

LEARNING DURATION CALCULATOR:
─────────────────────────────
Geschatte duur = 50 / (conversies per dag)

Voorbeeld:
├── 10 conv/dag → ~5 dagen (snel!)
├── 3 conv/dag → ~17 dagen (gemiddeld)
├── 1 conv/dag → ~50 dagen (lang)
└── 0.5 conv/dag → 100+ dagen (te lang)

⚠️ Als >21 dagen in learning:
├── Evalueer conversion volume
├── Check budget allocation
├── Overweeg higher-funnel conversie
└── Of ander bid strategy type
```

## Wat Reset Learning Phase?

### Major Resets (Volledige Herstart)

```
ACTIES DIE LEARNING VOLLEDIG RESETTEN
═════════════════════════════════════

🔴 VERMIJD DEZE TIJDENS LEARNING:
─────────────────────────────────

1. BID STRATEGY WIJZIGEN
   └── Van tCPA naar Max Conversions = RESET
   └── Van tROAS naar tCPA = RESET
   └── Portfolio naar individueel = RESET

2. TARGET GROTE AANPASSING (>20%)
   └── tCPA van €50 naar €40 = RESET
   └── tROAS van 400% naar 300% = RESET
   └── Uitzondering: Eerste target toevoegen

3. CONVERSION ACTION WIJZIGEN
   └── Andere primaire conversie = RESET
   └── Conversion value wijzigen = RESET
   └── Nieuwe conversion actie linken = RESET

4. CAMPAIGN PAUZEREN >7 DAGEN
   └── Langere pauze = learning data veroudert
   └── Heropening = quasi-nieuwe start

5. BUDGET DRASTISCH WIJZIGEN (>50%)
   └── Budget halveren = RESET
   └── Budget verdubbelen = Gedeeltelijke reset
```

### Minor Changes (Geen Reset)

```
VEILIGE ACTIES TIJDENS LEARNING
═══════════════════════════════

🟢 DEZE ACTIES ZIJN VEILIG:
───────────────────────────

TARGETING:
├── Keywords toevoegen (kleine batches)
├── Negative keywords toevoegen
├── Locatie uitbreiden
├── Device bid adjustments
└── Audience toevoegen (observatie)

ADS:
├── Nieuwe ads toevoegen
├── Ads pauzeren
├── RSA headlines/descriptions wijzigen
├── Extensions toevoegen/wijzigen
└── Ad copy optimaliseren

BUDGET:
├── Budget <20% verhogen
├── Budget <10% verlagen
└── Shared budget aanpassingen (klein)

LANDING PAGES:
├── Landing page URL wijzigen
├── Content updates
└── A/B test URL variants

⚠️ ALGEMENE REGEL:
Kleine, incrementele wijzigingen = OK
Grote, structurele wijzigingen = RESET
```

### Gray Zone Acties

```
ACTIES MET MOGELIJKE IMPACT
═══════════════════════════

🟡 VOORZICHTIG MEE OMGAAN:
──────────────────────────

1. BUDGET 20-30% WIJZIGEN
   └── Kan learning vertragen
   └── Meestal geen volledige reset
   └── Monitor nauwkeurig

2. TARGET 10-20% WIJZIGEN
   └── Kan korte "re-calibration" veroorzaken
   └── Niet altijd volledige reset
   └── Wait-and-see approach

3. VEEL KEYWORDS TEGELIJK TOEVOEGEN
   └── >50 keywords = kan learning verstoren
   └── Beter: batches van 10-20
   └── Monitor impressie share

4. NIEUWE AD GROUPS TOEVOEGEN
   └── 1-2 ad groups = geen probleem
   └── Grootschalige restructure = problematisch
   └── Test eerst klein

5. AUDIENCE TARGETING WIJZIGEN
   └── Observation naar targeting = impact
   └── Nieuwe audiences toevoegen = OK
   └── Audiences verwijderen = kleine impact
```

## Learning Limited Oplossen

### Diagnose

```
"LEARNING (LIMITED)" DIAGNOSE
═════════════════════════════

STAP 1: IDENTIFICEER OORZAAK
────────────────────────────
Hover over status voor details, of check:

MEEST VOORKOMENDE OORZAKEN:

1. ONVOLDOENDE CONVERSIES
   └── Symptoms: <50 conversies in 30 dagen
   └── Impact: AI kan geen patroon vinden
   └── Oplossing: Volume verhogen of funnel-up

2. BUDGET TE LAAG
   └── Symptoms: Budget limited tegelijk
   └── Impact: Niet genoeg auctions om te leren
   └── Oplossing: Budget verhogen of consolideren

3. TARGET TE RESTRICTIEF
   └── Symptoms: Zeer lage impressies
   └── Impact: Te weinig eligible auctions
   └── Oplossing: Target verruimen

4. TRACKING ISSUES
   └── Symptoms: Conversies fluctueren wild
   └── Impact: Onbetrouwbare data
   └── Oplossing: Tracking fixen eerst

5. SEASONALITY/VOLATILITEIT
   └── Symptoms: Grote dag-tot-dag variatie
   └── Impact: Geen consistent patroon
   └── Oplossing: Wachten of seasonality rules
```

### Oplossingen

```
LEARNING LIMITED OPLOSSINGEN
════════════════════════════

OPLOSSING 1: VERHOOG CONVERSION VOLUME
──────────────────────────────────────
Opties:
├── A) Verhoog budget → meer impressies → meer conversies
├── B) Verbreed targeting → meer reach
├── C) Gebruik "lighter" conversie (tijdelijk)
│   └── Form view ipv submit
│   └── Add-to-cart ipv purchase
│   └── Page engagement ipv lead
└── D) Combineer campaigns in portfolio

⚠️ Bij optie C: Zorg dat "echte" conversie wel getracked blijft
   voor later als primaire actie.

OPLOSSING 2: VERHOOG BUDGET
───────────────────────────
Berekening:
├── Target CPA × 10 = minimum daily budget
├── Voorbeeld: €50 CPA → €500/dag minimum

Of:
├── Combineer budgets van meerdere campaigns
├── Pauzeer underperforming campaigns
├── Reallocate naar learning campaigns

OPLOSSING 3: VERRUIM TARGET
───────────────────────────
Als tCPA te agressief:
├── Verhoog tCPA met 20-30%
├── Of switch naar Max Conversions (geen target)
├── Later: Geleidelijk tighten

Als tROAS te agressief:
├── Verlaag tROAS met 20-30%
├── Of switch naar Max Conversion Value
├── Later: Geleidelijk verhogen

OPLOSSING 4: CONSOLIDEER CAMPAIGNS
──────────────────────────────────
Probleem: Te veel kleine campaigns
Oplossing:
├── Combineer in minder campaigns
├── Of gebruik Portfolio bid strategy
├── Deel data over campaigns
└── Meer signalen voor AI

Voorbeeld:
├── 5 campaigns × 6 conv/maand = Learning limited
├── 1 campaign × 30 conv/maand = Betere learning
```

### Higher-Funnel Conversion Strategy

```
FUNNEL-UP STRATEGIE VOOR LEARNING
═════════════════════════════════

WANNEER GEBRUIKEN:
├── <50 primary conversions/maand
├── Structureel learning limited
├── Lange sales cycle

HOE HET WERKT:
──────────────

STAP 1: Identificeer Higher-Funnel Actie
┌────────────────────────────────────────────────────────────┐
│ Primary Conv    │ Higher-Funnel Optie      │ Volume x     │
├─────────────────┼──────────────────────────┼──────────────┤
│ Purchase        │ Add to cart              │ ~5x          │
│ Form submit     │ Form start / Page view   │ ~10x         │
│ Demo request    │ Pricing page view        │ ~20x         │
│ Phone call      │ Click-to-call            │ ~8x          │
│ Signup          │ Email capture            │ ~3x          │
└─────────────────┴──────────────────────────┴──────────────┘

STAP 2: Implementeer als Secondary Conversion
├── Conversion tracking toevoegen
├── Eerst als "secondary" (data verzamelen)
├── Check correlatie met primary conversie
└── Na 2-4 weken: switch als primary (voor bidding)

STAP 3: Monitor & Adjust
├── Learning zou moeten starten
├── Check dat primary conv niet daalt
├── Adjust bids voor nieuwe conversion rate
└── Overweeg value-based bidding met values

⚠️ BELANGRIJK:
Blijf primaire conversie tracken!
Switch terug zodra voldoende volume.
```

## Learning Phase Best Practices

### Pre-Launch Checklist

```
BEFORE LAUNCHING SMART BIDDING
══════════════════════════════

□ CONVERSION TRACKING VERIFIED
├── Test conversions gefired
├── Correct attribution window
├── Values correct (indien used)
└── Geen duplicate conversies

□ HISTORISCHE DATA AANWEZIG
├── Minimaal 30 dagen data
├── Liefst 50+ conversies in history
├── Consistent tracking gedurende periode
└── Geen grote gaps in data

□ BUDGET ADEQUAAT
├── Minimum: 10× target CPA per dag
├── Aanbevolen: 20× target CPA per dag
├── Buffer voor learning fluctuaties
└── 30 dagen budget commitment

□ REALISTIC TARGET INGESTELD
├── Target CPA: Historisch gemiddelde + 20%
├── Target ROAS: Historisch gemiddelde - 20%
├── NIET te agressief starten
└── Room to learn

□ STAKEHOLDERS GEÏNFORMEERD
├── Verwacht fluctuaties eerste 2 weken
├── Geen paniek bij CPA spike
├── Focus op trend, niet dagelijks
└── Review na 4 weken, niet eerder
```

### During Learning Protocol

```
TIJDENS LEARNING PHASE
══════════════════════

WEEK 1: HANDS-OFF
─────────────────
□ Dagelijkse monitoring (geen actie)
□ Log performance in spreadsheet
□ Verwacht: Hogere CPA, volatiliteit
□ NIET: Budget wijzigen, targets aanpassen

WEEK 2: OBSERVE PATTERNS
────────────────────────
□ Analyseer day-of-week trends
□ Check device performance
□ Noteer stabiel wordende metrics
□ Nog steeds: Geen grote wijzigingen

WEEK 3: EERSTE EVALUATIE
────────────────────────
□ Vergelijk met pre-learning baseline
□ Check learning status in UI
□ Als "Eligible": Kleine optimalisatie OK
□ Als "Learning": Nog wachten

WEEK 4: FORMELE REVIEW
──────────────────────
□ Full performance analysis
□ Learning voltooid? → Optimize
□ Nog learning? → Evaluate cause
□ Document learnings

MONITORING DASHBOARD:
─────────────────────
┌───────────────────────────────────────────────────────────┐
│ Metric          │ Pre-Learning │ Week 1 │ Week 2 │ Week 3│
├─────────────────┼──────────────┼────────┼────────┼───────┤
│ Conversions     │ baseline     │ -20%?  │ stable │ +10%? │
│ CPA             │ baseline     │ +30%?  │ -10%?  │ target│
│ Conv Rate       │ baseline     │ varies │ stable │ stable│
│ Impression Share│ baseline     │ varies │ varies │ stable│
└─────────────────┴──────────────┴────────┴────────┴───────┘
```

### Learning Acceleration Tactics

```
HOE LEARNING TE VERSNELLEN
══════════════════════════

TACTIEK 1: CONSERVATIVE TARGETS
───────────────────────────────
Start met ruimere targets:
├── tCPA: +30% van desired target
├── tROAS: -30% van desired target
├── Meer auctions = meer data = sneller leren
└── Tighten na learning complete

TACTIEK 2: ADEQUATE BUDGET
──────────────────────────
Budget formule:
├── Daily budget ≥ 15× target CPA
├── Of: Genoeg voor 15+ conversies/dag
├── Meer spend = sneller learnings
└── Investering in learning periode

TACTIEK 3: PORTFOLIO STRATEGIES
───────────────────────────────
Bundel campaigns:
├── Zelfde conversion goal
├── Shared learnings
├── Aggregate data
└── Snellere optimalisatie

TACTIEK 4: BROAD MATCH + SMART BIDDING
──────────────────────────────────────
Alleen tijdens learning:
├── Broad match = meer impressies
├── Smart bidding selecteert beste
├── Meer data voor AI
└── Later: Voeg negatives toe

TACTIEK 5: SEASONALITY ADJUSTMENTS
──────────────────────────────────
Bij bekend seasonal event:
├── Tools → Bid strategies → Advanced
├── Seasonality adjustment toevoegen
├── Informeert AI over verwachte change
└── Voorkomt onnodig "re-learning"
```

## Google Ads Script: Learning Phase Monitor

```javascript
/**
 * Learning Phase Monitor Script
 *
 * Monitort Smart Bidding learning phase status en stuurt alerts.
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Schedule: Dagelijks om 9:00
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Alert thresholds
  LEARNING_DAYS_WARNING: 14,  // Alert als >14 dagen in learning
  LEARNING_DAYS_CRITICAL: 21, // Critical alert

  // Performance monitoring tijdens learning
  CPA_SPIKE_THRESHOLD: 0.50,  // Alert bij 50% CPA spike
  CONV_DROP_THRESHOLD: 0.30   // Alert bij 30% conversie drop
};

function main() {
  var report = {
    learningCampaigns: [],
    limitedCampaigns: [],
    eligibleCampaigns: [],
    alerts: [],
    recommendations: []
  };

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var status = analyzeLearningStatus(campaign);

    if (status.isLearning) {
      report.learningCampaigns.push(status);

      if (status.estimatedDays > CONFIG.LEARNING_DAYS_WARNING) {
        report.alerts.push({
          campaign: status.name,
          type: status.estimatedDays > CONFIG.LEARNING_DAYS_CRITICAL ? 'CRITICAL' : 'WARNING',
          message: 'Learning phase duurt al ' + status.estimatedDays + ' dagen'
        });
      }
    } else if (status.isLimited) {
      report.limitedCampaigns.push(status);
      report.alerts.push({
        campaign: status.name,
        type: 'ACTION_REQUIRED',
        message: 'Learning Limited - actie vereist'
      });
    } else {
      report.eligibleCampaigns.push(status);
    }

    // Check performance changes during learning
    if (status.isLearning) {
      var perfAlerts = checkPerformanceDuringLearning(campaign);
      report.alerts = report.alerts.concat(perfAlerts);
    }
  }

  // Generate recommendations
  report.recommendations = generateLearningRecommendations(report);

  // Send report
  sendLearningReport(report);

  Logger.log('Learning Phase Monitor Complete');
  Logger.log('Campaigns in learning: ' + report.learningCampaigns.length);
  Logger.log('Campaigns limited: ' + report.limitedCampaigns.length);
  Logger.log('Alerts: ' + report.alerts.length);
}

function analyzeLearningStatus(campaign) {
  var name = campaign.getName();
  var bidStrategy = campaign.getBiddingStrategyType();

  // Get conversion stats
  var stats14d = campaign.getStatsFor('LAST_14_DAYS');
  var stats30d = campaign.getStatsFor('LAST_30_DAYS');

  var conv14d = stats14d.getConversions();
  var conv30d = stats30d.getConversions();

  // Estimate learning status based on conversion volume
  // Note: Actual status requires UI check, this is proxy
  var isLearning = conv30d < 50;
  var isLimited = conv30d < 30 && conv14d < 15;

  // Estimate days in learning
  var avgDailyConv = conv30d / 30;
  var estimatedDays = avgDailyConv > 0 ?
    Math.min(Math.ceil(50 / avgDailyConv), 60) : 60;

  return {
    name: name,
    bidStrategy: bidStrategy,
    conversions30d: conv30d,
    conversions14d: conv14d,
    avgDailyConv: avgDailyConv,
    isLearning: isLearning,
    isLimited: isLimited,
    estimatedDays: isLearning ? estimatedDays : 0,
    cost30d: stats30d.getCost()
  };
}

function checkPerformanceDuringLearning(campaign) {
  var alerts = [];
  var name = campaign.getName();

  var currentStats = campaign.getStatsFor('LAST_7_DAYS');
  var previousStats = campaign.getStatsFor('LAST_14_DAYS');

  // Current period
  var currentConv = currentStats.getConversions();
  var currentCost = currentStats.getCost();
  var currentCPA = currentConv > 0 ? currentCost / currentConv : 0;

  // Previous period (week before last week)
  var prevConv = previousStats.getConversions() - currentConv;
  var prevCost = previousStats.getCost() - currentCost;
  var prevCPA = prevConv > 0 ? prevCost / prevConv : 0;

  // Check CPA spike
  if (prevCPA > 0 && currentCPA > 0) {
    var cpaChange = (currentCPA - prevCPA) / prevCPA;
    if (cpaChange > CONFIG.CPA_SPIKE_THRESHOLD) {
      alerts.push({
        campaign: name,
        type: 'PERFORMANCE',
        message: 'CPA spike tijdens learning: ' +
                 (cpaChange * 100).toFixed(0) + '% stijging'
      });
    }
  }

  // Check conversion drop
  if (prevConv > 0) {
    var convChange = (prevConv - currentConv) / prevConv;
    if (convChange > CONFIG.CONV_DROP_THRESHOLD) {
      alerts.push({
        campaign: name,
        type: 'PERFORMANCE',
        message: 'Conversie drop tijdens learning: ' +
                 (convChange * 100).toFixed(0) + '% daling'
      });
    }
  }

  return alerts;
}

function generateLearningRecommendations(report) {
  var recs = [];

  // Limited campaigns
  if (report.limitedCampaigns.length > 0) {
    recs.push({
      priority: 'HIGH',
      action: 'Adresseer Learning Limited campaigns',
      detail: 'Overweeg: budget verhogen, target verruimen, of consolideren'
    });
  }

  // Long learning campaigns
  var longLearning = report.learningCampaigns.filter(function(c) {
    return c.estimatedDays > CONFIG.LEARNING_DAYS_WARNING;
  });

  if (longLearning.length > 0) {
    recs.push({
      priority: 'MEDIUM',
      action: longLearning.length + ' campaigns te lang in learning',
      detail: 'Evalueer conversion volumes en bid strategy keuze'
    });
  }

  // Low volume campaigns
  var lowVolume = report.learningCampaigns.filter(function(c) {
    return c.avgDailyConv < 2;
  });

  if (lowVolume.length > 0) {
    recs.push({
      priority: 'MEDIUM',
      action: lowVolume.length + ' campaigns met <2 conv/dag',
      detail: 'Overweeg Portfolio bid strategy of higher-funnel conversie'
    });
  }

  return recs;
}

function sendLearningReport(report) {
  var subject = 'Learning Phase Report - ' + AdsApp.currentAccount().getName();
  var body = 'Smart Bidding Learning Phase Report\n';
  body += '====================================\n\n';

  // Summary
  body += 'SUMMARY:\n';
  body += '• Campaigns in learning: ' + report.learningCampaigns.length + '\n';
  body += '• Campaigns limited: ' + report.limitedCampaigns.length + '\n';
  body += '• Campaigns eligible: ' + report.eligibleCampaigns.length + '\n';
  body += '• Alerts: ' + report.alerts.length + '\n\n';

  // Alerts
  if (report.alerts.length > 0) {
    body += 'ALERTS:\n';
    body += '────────\n';

    for (var i = 0; i < report.alerts.length; i++) {
      var alert = report.alerts[i];
      body += '[' + alert.type + '] ' + alert.campaign + '\n';
      body += '  ' + alert.message + '\n\n';
    }
  }

  // Learning campaigns detail
  if (report.learningCampaigns.length > 0) {
    body += 'CAMPAIGNS IN LEARNING:\n';
    body += '──────────────────────\n';

    for (var j = 0; j < report.learningCampaigns.length; j++) {
      var lc = report.learningCampaigns[j];
      body += '• ' + lc.name + '\n';
      body += '  Conv/30d: ' + lc.conversions30d.toFixed(0);
      body += ' | Avg/day: ' + lc.avgDailyConv.toFixed(1);
      body += ' | Est. days remaining: ' + lc.estimatedDays + '\n\n';
    }
  }

  // Limited campaigns
  if (report.limitedCampaigns.length > 0) {
    body += 'LEARNING LIMITED (Actie Vereist):\n';
    body += '─────────────────────────────────\n';

    for (var k = 0; k < report.limitedCampaigns.length; k++) {
      var ltd = report.limitedCampaigns[k];
      body += '• ' + ltd.name + '\n';
      body += '  Conv/30d: ' + ltd.conversions30d.toFixed(0);
      body += ' | Cost: €' + ltd.cost30d.toFixed(0) + '\n\n';
    }
  }

  // Recommendations
  if (report.recommendations.length > 0) {
    body += 'RECOMMENDATIONS:\n';
    body += '────────────────\n';

    for (var l = 0; l < report.recommendations.length; l++) {
      var rec = report.recommendations[l];
      body += '[' + rec.priority + '] ' + rec.action + '\n';
      body += '  → ' + rec.detail + '\n\n';
    }
  }

  body += '\n---\nGenerated by Learning Phase Monitor Script';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Output: Learning Phase Status Template

```markdown
# Learning Phase Status Report

## Campaign Overview
- **Campaign naam:** [Naam]
- **Bid strategy:** [tCPA/tROAS/Max Conv/etc.]
- **Learning status:** [Learning/Limited/Eligible]
- **Dagen in learning:** [X]

## Current Performance
| Metric | Baseline | Week 1 | Week 2 | Current |
|--------|----------|--------|--------|---------|
| Conversions | [X] | [X] | [X] | [X] |
| CPA | €[X] | €[X] | €[X] | €[X] |
| Conv Rate | [X]% | [X]% | [X]% | [X]% |
| Spend | €[X] | €[X] | €[X] | €[X] |

## Learning Analysis

### Data Volume Check
- Conversies afgelopen 30 dagen: [X] (nodig: 50+)
- Gemiddeld per dag: [X]
- Geschatte tijd tot eligible: [X] dagen

### Blocking Factors
- [ ] Budget te laag
- [ ] Target te restrictief
- [ ] Conversion tracking issues
- [ ] Onvoldoende impressies

## Aanbevelingen

### Als Status = "Learning"
- [ ] Wacht minimaal [X] dagen
- [ ] Geen grote wijzigingen
- [ ] Dagelijkse monitoring

### Als Status = "Learning (Limited)"
**Prioriteit actie:** [Beschrijf oplossing]

Opties:
1. [Optie 1 - bijv. budget verhogen]
2. [Optie 2 - bijv. target verruimen]
3. [Optie 3 - bijv. consolideren]

### Als Status = "Eligible"
- [ ] Evalueer performance vs targets
- [ ] Overweeg target tightening (max 10%)
- [ ] Begin optimalisatie cyclus

## Next Steps
1. [Actie 1 + deadline]
2. [Actie 2 + deadline]
3. [Actie 3 + deadline]

## Review Schedule
- Dagelijkse check: [Tijd]
- Wekelijkse deep-dive: [Dag]
- Formele evaluatie: [Datum]
```

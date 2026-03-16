---
name: bid-strategy-selector
description: "Google Ads Smart Bidding strategie advisor. Gebruik voor: (1) Maximize Conversions vs Target CPA vs Target ROAS kiezen, (2) Portfolio bid strategies opzetten, (3) Value-based bidding configuratie, (4) Learning phase management, (5) Bid strategy migration. Triggers: bid strategy, smart bidding, tCPA, tROAS, maximize conversions, maximize conversion value, portfolio bidding."
---

# Bid Strategy Selector

Complete gids voor het kiezen en implementeren van de juiste Google Ads Smart Bidding strategie op basis van doelen, data en account situatie.

## Quick Decision Tree

```
WELKE BID STRATEGY PAST BIJ JOU?
│
├─► NIEUW ACCOUNT / WEINIG DATA (<30 conversies/maand)
│   └─► MAXIMIZE CONVERSIONS (geen target)
│       └─► Doel: Data verzamelen, learning phase doorlopen
│
├─► LEAD GENERATION met bekende lead value
│   ├─► Consistent conversie volume (50+/maand)?
│   │   └─► JA → TARGET CPA
│   │   └─► NEE → MAXIMIZE CONVERSIONS
│   └─► Variabele lead waarden?
│       └─► JA → MAXIMIZE CONVERSION VALUE + tROAS
│
├─► E-COMMERCE met purchase tracking
│   ├─► Focus op volume (marktaandeel)?
│   │   └─► MAXIMIZE CONVERSION VALUE
│   ├─► Focus op profitability?
│   │   └─► TARGET ROAS
│   └─► Beide balanceren?
│       └─► MAXIMIZE CONVERSION VALUE + tROAS target
│
└─► MEERDERE CAMPAIGNS met zelfde doel
    └─► PORTFOLIO BID STRATEGY
        └─► Shared strategy over campaigns
```

## Smart Bidding Overzicht

```
SMART BIDDING VERGELIJKING
══════════════════════════

┌─────────────────────────┬───────────┬───────────┬─────────────────────┐
│ STRATEGY                │ CONTROL   │ DATA REQ  │ BEST FOR            │
├─────────────────────────┼───────────┼───────────┼─────────────────────┤
│ Maximize Conversions    │ Geen      │ Laag      │ Nieuwe accounts,    │
│ (zonder target)         │           │           │ data verzamelen     │
├─────────────────────────┼───────────┼───────────┼─────────────────────┤
│ Maximize Conversions    │ CPA cap   │ Medium    │ Lead gen met        │
│ + Target CPA            │           │ (50+/mnd) │ cost constraints    │
├─────────────────────────┼───────────┼───────────┼─────────────────────┤
│ Maximize Conv. Value    │ Geen      │ Laag      │ E-commerce volume,  │
│ (zonder target)         │           │           │ initial learning    │
├─────────────────────────┼───────────┼───────────┼─────────────────────┤
│ Maximize Conv. Value    │ ROAS      │ Medium    │ E-commerce profit,  │
│ + Target ROAS           │ target    │ (50+/mnd) │ scaling             │
├─────────────────────────┼───────────┼───────────┼─────────────────────┤
│ Manual CPC              │ Max CPC   │ Geen      │ Niche, B2B,         │
│ (Enhanced CPC opt.)     │ per kw    │           │ kleine accounts     │
└─────────────────────────┴───────────┴───────────┴─────────────────────┘
```

## Maximize Conversions

### Hoe Het Werkt

```
MAXIMIZE CONVERSIONS ENGINE
===========================

┌────────────────────────────────────────────────────────────────┐
│  GOOGLE AI OPTIMALISEERT VOOR:                                 │
│  Maximaal aantal conversies binnen je dagbudget                │
│                                                                │
│  SIGNALEN DIE WORDEN GEBRUIKT:                                 │
│  ├── Device, location, time of day                             │
│  ├── Browser, OS, demographics                                 │
│  ├── Search query en intent signals                            │
│  ├── Remarketing lists membership                              │
│  ├── Historical conversion patterns                            │
│  └── Real-time auction dynamics                                │
│                                                                │
│  JIJ BEPAALT:                                                  │
│  ├── Daily budget (spending limit)                             │
│  ├── Target CPA (optioneel, als constraint)                    │
│  └── Conversion actions (welke te optimaliseren)               │
└────────────────────────────────────────────────────────────────┘
```

### Wanneer Maximize Conversions Gebruiken

```
✅ GEBRUIK MAXIMIZE CONVERSIONS WANNEER:
────────────────────────────────────────
• Nieuw account met weinig historische data
• Eerste 2-4 weken van nieuwe campaign
• Lead generation focus (één type conversie)
• Budget belangrijker dan CPA efficiency
• Data verzamelen voor latere tCPA

❌ GEBRUIK NIET WANNEER:
─────────────────────────
• Strikte CPA vereisten (gebruik tCPA)
• E-commerce met purchase values (gebruik Max Conv Value)
• Heel laag budget (<€20/dag) - te weinig learnings
• Campaign met meerdere conversion types zonder primaire
```

### Maximize Conversions + Target CPA

```
TARGET CPA TOEVOEGEN
====================

WANNEER:
├── 50+ conversies in afgelopen 30 dagen
├── Stabiele performance (geen grote fluctuaties)
├── Bekende target CPA (break-even of doel)
└── Na succesvolle pure Maximize Conversions fase

TARGET CPA BEREKENEN:
─────────────────────
Break-even CPA (Lead Gen):
└── Lead Value × Conversion Rate to Sale

Voorbeeld:
├── Lead value (als sale): €500
├── Close rate: 10%
├── Break-even CPA: €500 × 0.10 = €50

Starting Target CPA:
├── Week 1-2: 120% van break-even (€60)
├── Week 3-4: 110% van break-even (€55)
├── Week 5+: 100% of tighter als stable

⚠️ NOOIT starten ONDER historisch gemiddelde CPA!
```

## Maximize Conversion Value

### Hoe Het Werkt

```
MAXIMIZE CONVERSION VALUE ENGINE
================================

┌────────────────────────────────────────────────────────────────┐
│  GOOGLE AI OPTIMALISEERT VOOR:                                 │
│  Maximale totale conversion value binnen je dagbudget          │
│                                                                │
│  VEREISTEN:                                                    │
│  ├── Conversion tracking met VALUE (purchase value)            │
│  ├── Accurate revenue/value data                               │
│  └── Consistent value tracking                                 │
│                                                                │
│  AI PRIORITEERT:                                               │
│  ├── Hoge waarde transacties boven lage                        │
│  ├── Users met hoge predicted value                            │
│  └── Queries die historisch hoge values opleveren              │
└────────────────────────────────────────────────────────────────┘
```

### Maximize Conversion Value + Target ROAS

```
TARGET ROAS TOEVOEGEN
=====================

WANNEER:
├── 50+ conversies met value in afgelopen 30 dagen
├── Consistent value tracking (geen gaps)
├── Bekende break-even of target ROAS
└── Na succesvolle pure Max Conv Value fase

TARGET ROAS BEREKENEN:
──────────────────────
Break-even ROAS = 1 / Profit Margin

Voorbeeld:
├── Profit margin: 40%
├── Break-even ROAS: 1 / 0.40 = 2.5 (250%)
├── Als je €100 spend, moet je €250 revenue genereren

Starting Target ROAS:
├── Week 1-2: 80% van break-even (200% als break-even 250%)
├── Week 3-4: 90% van break-even (225%)
├── Week 5+: 100% of tighter als stable

⚠️ Te agressieve ROAS target = geen delivery!
```

## Portfolio Bid Strategies

### Wat Zijn Portfolio Strategies?

```
PORTFOLIO BID STRATEGY
======================

= Eén bid strategy gedeeld over meerdere campaigns

VOORDELEN:
├── Meer data voor learning → betere optimalisatie
├── Centraal beheer van bids
├── Budget flexibility over campaigns
└── Betere performance bij kleine campaigns

BEPERKINGEN:
├── Alle campaigns moeten zelfde doel hebben
├── Shared learning kan suboptimaal zijn per campaign
└── Minder granular control
```

### Portfolio Strategy Setup

```
PORTFOLIO STRATEGY TYPES
========================

1. TARGET CPA PORTFOLIO
   └── Meerdere Search/Display campaigns, zelfde CPA doel
   └── Voorbeeld: Brand + Non-brand Search

2. TARGET ROAS PORTFOLIO
   └── E-commerce campaigns met zelfde margin target
   └── Voorbeeld: Shopping + Search + PMax

3. MAXIMIZE CONVERSIONS PORTFOLIO
   └── Data aggregeren voor snellere learning
   └── Voorbeeld: Nieuwe campaigns bundelen

4. TARGET IMPRESSION SHARE PORTFOLIO
   └── Brand visibility campaigns
   └── Voorbeeld: Branded Search campaigns

SETUP LOCATIE:
Tools & Settings → Shared Library → Bid Strategies
```

### Wanneer Portfolio Gebruiken

```
PORTFOLIO DECISION MATRIX
=========================

GEBRUIK PORTFOLIO WANNEER:
├── Meerdere campaigns met <50 conversies/maand elk
├── Campagnes hebben exact dezelfde KPI targets
├── Je wilt één centraal punt voor bid management
└── Kleine budgetten over meerdere campaigns

GEBRUIK INDIVIDUEEL WANNEER:
├── Campaigns hebben verschillende margin/CPA targets
├── Voldoende conversies per campaign (50+/maand)
├── Verschillende product types/audiences
└── Behoefte aan campaign-level bid adjustments
```

## Learning Phase Management

### Learning Phase Basics

```
LEARNING PHASE UITLEG
=====================

WAT:
├── Periode waarin Smart Bidding data verzamelt
├── Bids kunnen fluctueren
├── Performance kan tijdelijk slechter zijn
└── NIET ingrijpen tijdens deze fase

DUUR:
├── Typisch: 7-14 dagen
├── Requirement: ~50 conversies (of acties)
├── Kan langer bij weinig volume
└── Status zichtbaar in campaign UI

LEARNING PHASE STATUS:
├── "Learning" = Actief aan het leren
├── "Learning (limited)" = Onvoldoende data
├── "Eligible" = Learning complete
└── "Limited" = Andere issue (budget, etc.)
```

### Wat Reset Learning Phase?

```
ACTIES DIE LEARNING RESETTEN
============================

🔴 VERMIJD DEZE TIJDENS LEARNING:
─────────────────────────────────
• Bid strategy wijzigen
• Target CPA/ROAS aanpassen (>20%)
• Conversion action wijzigen
• Budget >20% verhogen of verlagen
• Campagne pauzeren >7 dagen

🟢 VEILIG TIJDENS LEARNING:
───────────────────────────
• Ads toevoegen of pauzeren
• Keywords toevoegen (small batches)
• Negatives toevoegen
• Budget <20% wijzigen
• Ad copy aanpassingen
```

### Learning Phase Troubleshooting

```
LEARNING PHASE ISSUES
=====================

PROBLEEM: "Learning (limited)" blijft hangen
─────────────────────────────────────────────
Oorzaak: Onvoldoende conversies
Oplossingen:
├── Budget verhogen
├── Broader targeting (meer volume)
├── Higher-funnel conversie actie (tijdelijk)
└── Wacht langer (soms nodig)

PROBLEEM: CPA explodeert tijdens learning
─────────────────────────────────────────
Dit is normaal! AI test grenzen.
Acties:
├── NIET paniekeren
├── Wacht minimaal 7-10 dagen
├── Monitor trend, niet dagelijkse CPA
└── Als >14 dagen slecht: evalueer targeting/budget

PROBLEEM: Learning duurt >3 weken
─────────────────────────────────
Mogelijke oorzaken:
├── Te weinig budget
├── Te nichey targeting
├── Slechte ad quality
└── Tracking issues
```

## Value-Based Bidding

### Value Rules (2025+)

```
VALUE RULES UITLEG
==================

WAT:
├── Pas conversion values dynamisch aan
├── Gebaseerd op user/context signals
├── AI biedt hoger voor high-value segments
└── Beschikbaar voor alle Smart Bidding strategies

BESCHIKBARE SIGNALEN:
├── Device (mobile, desktop, tablet)
├── Location (geografisch)
├── Audience (Customer Match, remarketing)
└── Time (planned voor toekomst)

VOORBEELD SETUP:
────────────────
Value Rule 1: High-Value Customers
├── Condition: Customer Match list = "VIP Customers"
├── Adjustment: +50% value
└── Effect: €100 purchase → €150 voor bidding

Value Rule 2: Low-Intent Location
├── Condition: Location = "Low converting region"
├── Adjustment: -30% value
└── Effect: €100 purchase → €70 voor bidding
```

### New Customer Acquisition

```
NEW CUSTOMER BIDDING (2025+)
============================

LOCATIE: Campaign Settings → Customer Acquisition

OPTIES:
├── Bid higher for new customers: +X% bid adjustment
├── Only bid for new customers: Exclude existing
└── No differentiation (default)

SETUP VEREISTEN:
├── Customer Match list van existing customers
├── Conversion tracking actief
└── Voldoende new vs returning data

AANBEVOLEN START:
├── +20% voor new customers
├── Monitor new vs returning ROAS
├── Adjust based on LTV data
└── E-commerce: Consider first-purchase margin
```

## Bid Strategy Migration

### Van Manual naar Smart Bidding

```
MANUAL → SMART BIDDING MIGRATION
================================

STAP 1: VOORBEREIDING (Week -2 tot -1)
──────────────────────────────────────
□ Conversion tracking verifiëren
□ Minimaal 30 conversies/maand
□ Baseline metrics documenteren
□ Budget bepalen (min €50/dag)

STAP 2: INITIAL SETUP (Week 1)
──────────────────────────────
□ Start met Maximize Conversions (geen target)
□ Verwacht fluctuaties
□ NIET ingrijpen

STAP 3: MONITORING (Week 2-3)
─────────────────────────────
□ Learning phase monitoren
□ Vergelijk met baseline
□ Nog steeds NIET ingrijpen

STAP 4: OPTIMIZATION (Week 4+)
──────────────────────────────
□ Evalueer performance vs manual
□ Voeg target toe indien stabiel
□ Start conservatief (120% van achieved)
```

### Strategy Switch Checklist

```
BID STRATEGY SWITCH PROTOCOL
============================

□ PRE-SWITCH:
├── Document huidige performance (7-day average)
├── Bereken target (CPA/ROAS)
├── Kies switching moment (niet tijdens peak)
└── Prepare stakeholders (tijdelijke fluctuaties)

□ DURING SWITCH:
├── Implement nieuwe strategy
├── Conservatieve target (120% van current)
├── Screen capture voor reference
└── Zet calendar reminder voor review

□ POST-SWITCH (Week 1-2):
├── Daily monitoring (maar geen changes)
├── Learning phase status checken
├── Compare week-over-week (niet day-over-day)
└── Noteer anomalieën

□ POST-SWITCH (Week 3+):
├── Formele performance review
├── Tighten targets indien stable (+10%)
├── Document learnings
└── Continue monitoring
```

## Campaign Type Specifieke Aanbevelingen

### Search Campaigns

```
SEARCH BID STRATEGY GUIDE
=========================

BRAND SEARCH:
├── Strategy: Maximize Conversions of Manual CPC
├── Reden: Hoge CTR, lage competitie
├── Target: Impression Share >90%
└── Let op: Niet overbidden, je wint toch

NON-BRAND SEARCH:
├── Nieuw: Maximize Conversions (2-3 weken)
├── Daarna: Target CPA/ROAS
├── Reden: Competitive, need efficiency
└── Let op: Broad match + Smart Bidding = powerful combo

DSA (Dynamic Search Ads):
├── Strategy: Maximize Conversions
├── Reden: Discovery, volume focus
├── Transitie naar tCPA als winnende queries bekend
└── Let op: Negative keywords management
```

### Shopping & PMax

```
SHOPPING / PMAX BID STRATEGY
============================

STANDARD SHOPPING (als nog gebruikt):
├── Start: Maximize Clicks (data verzamelen)
├── Transitie: Target ROAS na 50+ purchases
├── Let op: Product-level bidding via priorities

PERFORMANCE MAX:
├── E-commerce: Maximize Conversion Value + tROAS
├── Lead Gen: Maximize Conversions + tCPA
├── Nieuw: Zonder target (2-3 weken)
└── Let op: PMax heeft meer data nodig dan Search

ROAS TARGETS VOOR PMAX:
├── Conservative start: 200-300%
├── Moderate: 300-500%
├── Aggressive: 500%+
└── Adjust based on margin and goals
```

### Display & Video

```
DISPLAY / VIDEO BID STRATEGY
============================

DISPLAY CAMPAIGNS:
├── Remarketing: Maximize Conversions + tCPA
├── Prospecting: Maximize Conversions (volume focus)
├── Brand: Target CPM (als beschikbaar)
└── Let op: Langere learning door lager volume

VIDEO CAMPAIGNS:
├── Awareness: Target CPM of Maximize Impressions
├── Consideration: Target CPV (Cost-per-View)
├── Conversion: Maximize Conversions
└── Let op: Video ads converteren indirect

DEMAND GEN:
├── Strategy: Maximize Conversions of tCPA
├── Reden: Hybrid awareness/conversion
├── Let op: View-through conversions meewegen
```

## Performance Monitoring Script

```javascript
/**
 * Bid Strategy Performance Monitor
 *
 * Monitort Smart Bidding performance en learning phase status.
 *
 * Setup:
 * 1. Pas EMAIL aan
 * 2. Schedule dagelijks om 9:00
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',
  CPA_THRESHOLD: 0.25,     // Alert bij 25% CPA stijging
  ROAS_THRESHOLD: 0.20,    // Alert bij 20% ROAS daling
  LEARNING_DAYS_ALERT: 14  // Alert als learning >14 dagen
};

function main() {
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  var alerts = [];
  var learningCampaigns = [];

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var bidStrategy = campaign.getBiddingStrategyType();

    // Check learning phase (via status indicators)
    var status = checkCampaignStatus(campaign);
    if (status.isLearning) {
      learningCampaigns.push({
        name: campaign.getName(),
        strategy: bidStrategy,
        days: status.learningDays
      });
    }

    // Check performance changes
    var perfAlerts = checkPerformance(campaign);
    alerts = alerts.concat(perfAlerts);
  }

  // Send summary
  if (alerts.length > 0 || learningCampaigns.length > 0) {
    sendSummaryEmail(alerts, learningCampaigns);
  }

  Logger.log('Monitor complete. Alerts: ' + alerts.length);
  Logger.log('Campaigns in learning: ' + learningCampaigns.length);
}

function checkCampaignStatus(campaign) {
  // Note: Learning phase status niet direct via API
  // Dit is een proxy check
  var stats7d = campaign.getStatsFor('LAST_7_DAYS');
  var stats14d = campaign.getStatsFor('LAST_14_DAYS');

  var conv7d = stats7d.getConversions();
  var conv14d = stats14d.getConversions();

  // Als <50 conversies in 14 dagen, waarschijnlijk nog learning
  return {
    isLearning: conv14d < 50,
    learningDays: conv14d < 50 ? 14 : 0
  };
}

function checkPerformance(campaign) {
  var alerts = [];
  var name = campaign.getName();

  var currentStats = campaign.getStatsFor('LAST_7_DAYS');
  var previousStats = campaign.getStatsFor('LAST_14_DAYS');

  var currentCPA = currentStats.getConversions() > 0 ?
    currentStats.getCost() / currentStats.getConversions() : 0;

  // Calculate previous period CPA
  var prevConv = previousStats.getConversions() - currentStats.getConversions();
  var prevCost = previousStats.getCost() - currentStats.getCost();
  var previousCPA = prevConv > 0 ? prevCost / prevConv : 0;

  if (previousCPA > 0 && currentCPA > 0) {
    var change = (currentCPA - previousCPA) / previousCPA;
    if (change > CONFIG.CPA_THRESHOLD) {
      alerts.push({
        campaign: name,
        metric: 'CPA',
        previous: previousCPA.toFixed(2),
        current: currentCPA.toFixed(2),
        change: (change * 100).toFixed(1) + '%'
      });
    }
  }

  return alerts;
}

function sendSummaryEmail(alerts, learningCampaigns) {
  var subject = 'Smart Bidding Status - ' + AdsApp.currentAccount().getName();
  var body = 'Smart Bidding Daily Report\n';
  body += '===========================\n\n';

  if (learningCampaigns.length > 0) {
    body += 'CAMPAIGNS IN LEARNING:\n';
    for (var i = 0; i < learningCampaigns.length; i++) {
      var lc = learningCampaigns[i];
      body += '• ' + lc.name + ' (' + lc.strategy + ')\n';
    }
    body += '\n';
  }

  if (alerts.length > 0) {
    body += 'PERFORMANCE ALERTS:\n';
    for (var j = 0; j < alerts.length; j++) {
      var alert = alerts[j];
      body += '• ' + alert.campaign + ': ' + alert.metric + ' changed ';
      body += alert.previous + ' → ' + alert.current + ' (' + alert.change + ')\n';
    }
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Output: Bid Strategy Recommendation Template

```markdown
# Bid Strategy Recommendation

## Account Situatie
- **Account type:** [E-commerce / Lead Gen / Hybrid]
- **Monthly budget:** €[X]
- **Current conversions/month:** [X]
- **Current CPA/ROAS:** €[X] / [X]%
- **Primary goal:** [Volume / Efficiency / Profitability]

## Aanbevolen Strategy
**[STRATEGY NAAM]**

### Waarom Deze Strategy
1. [Reden 1 - gebaseerd op account situatie]
2. [Reden 2 - gebaseerd op goals]
3. [Reden 3 - gebaseerd op data availability]

### Implementatie Plan

**Week 1-2: Setup & Learning**
- Switch naar [strategy]
- Target: [Geen / €X / X%] (conservatief)
- Budget: €[X]/dag
- Actie: Alleen monitoren, geen changes

**Week 3-4: Evaluatie**
- Learning phase check
- Performance vs baseline
- Target adjustment: [Specificeer]

**Week 5+: Optimalisatie**
- Tighten target naar [X]
- Continue monitoring
- Evaluate scale opportunities

### Targets
- Primary: [CPA €X / ROAS X%]
- Secondary: [Conversions, Value, etc.]

### Verwachte Resultaten
- CPA change: [+/- X%]
- Volume change: [+/- X%]
- Learning phase duration: [X weken]

### Risico's & Mitigatie
- Risico: [Beschrijf]
- Mitigatie: [Plan]
```

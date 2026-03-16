---
name: attribution-model-advisor
description: "Google Ads Attribution Model advisor. Gebruik voor: (1) Data-Driven Attribution setup en evaluatie, (2) Cross-channel attribution analyse, (3) Attribution model vergelijking en selectie, (4) Conversion path analyse, (5) Multi-touch attribution strategie. Triggers: attribution, data-driven attribution, DDA, conversion paths, cross-channel, touchpoints, last click, first click, position based, time decay, attribution model."
---

# Attribution Model Advisor

Complete gids voor het kiezen, implementeren en evalueren van Google Ads attribution modellen met focus op Data-Driven Attribution (DDA) en cross-channel measurement.

## Quick Decision Guide

```
WELK ATTRIBUTION MODEL PAST BIJ JOU?
│
├─► VOLDOENDE DATA (600+ conversies/maand)
│   └─► DATA-DRIVEN ATTRIBUTION (DDA)
│       ├── Google's ML-based model
│       ├── Account-specifieke weging
│       └── Meest accurate voor jouw situatie
│
├─► MATIGE DATA (300-600 conversies/maand)
│   └─► TIME DECAY of POSITION BASED
│       ├── Time Decay: Focus op touchpoints dicht bij conversie
│       ├── Position Based: First/last touch + middle credits
│       └── Evalueer regelmatig voor DDA switch
│
├─► WEINIG DATA (<300 conversies/maand)
│   └─► LAST CLICK (default) of TIME DECAY
│       ├── Last Click: Simpel, maar onderwaardeert awareness
│       ├── Overweeg first click voor brand-focus
│       └── Bouw naar DDA toe
│
└─► SPECIFIEKE USE CASES
    ├─► Pure brand awareness → FIRST CLICK
    ├─► Direct response/e-com → LAST CLICK of TIME DECAY
    ├─► Complex B2B journey → POSITION BASED of DDA
    └─► Multi-channel mix → DATA-DRIVEN ATTRIBUTION
```

## Attribution Modellen Overzicht

### Model Vergelijking

```
ATTRIBUTION MODEL VERGELIJKING
══════════════════════════════

┌─────────────────────┬────────────┬────────────────────────────────────────┐
│ MODEL               │ DATA REQ   │ HOE HET WERKT                          │
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ Last Click          │ Geen       │ 100% credit naar laatste klik          │
│                     │            │ (default, simpel, maar beperkt)        │
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ First Click         │ Geen       │ 100% credit naar eerste klik           │
│                     │            │ (goed voor awareness meten)            │
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ Linear              │ Laag       │ Gelijke verdeling over alle touchpoints│
│                     │            │ (democratisch, maar weinig nuance)     │
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ Time Decay          │ Laag       │ Meer credit naar recente touchpoints   │
│                     │            │ (7-dagen half-life)                    │
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ Position Based      │ Medium     │ 40% first, 40% last, 20% middle        │
│                     │            │ (balanced awareness + conversion)      │
├─────────────────────┼────────────┼────────────────────────────────────────┤
│ Data-Driven (DDA)   │ Hoog       │ ML-based op jouw data                  │
│                     │ (600+/mnd) │ (meest accurate, Google aanbevolen)    │
└─────────────────────┴────────────┴────────────────────────────────────────┘
```

### Visual: Hoe Credits Worden Verdeeld

```
VOORBEELD: 4 TOUCHPOINTS VOOR CONVERSIE
═══════════════════════════════════════

Customer Journey:
Display Ad → Search (generic) → Search (brand) → Conversie
   [1]            [2]              [3]           [€100]

CREDIT VERDELING PER MODEL:

Last Click:
[1] €0 ────► [2] €0 ────► [3] €100 ────► Conversie
                              100%

First Click:
[1] €100 ───► [2] €0 ────► [3] €0 ────► Conversie
    100%

Linear:
[1] €33.33 ─► [2] €33.33 ─► [3] €33.33 ─► Conversie
    33.3%        33.3%         33.3%

Time Decay:
[1] €10.50 ─► [2] €24.50 ─► [3] €65 ────► Conversie
    10.5%        24.5%         65%

Position Based:
[1] €40 ────► [2] €20 ────► [3] €40 ────► Conversie
    40%          20%           40%

Data-Driven (voorbeeld):
[1] €28 ────► [2] €35 ────► [3] €37 ────► Conversie
    28%          35%           37%
    (gebaseerd op jouw account data)
```

## Data-Driven Attribution (DDA)

### Hoe DDA Werkt

```
DATA-DRIVEN ATTRIBUTION ENGINE
══════════════════════════════

MACHINE LEARNING APPROACH:
├── Analyseert alle conversion paths
├── Vergelijkt converting vs non-converting journeys
├── Berekent incrementele waarde per touchpoint
└── Past dynamisch aan op basis van nieuwe data

SIGNALEN DIE DDA GEBRUIKT:
├── Ad interactions (clicks, impressions)
├── Device type en cross-device behaviour
├── Time between interactions
├── Ad format en placement
├── Search query types
└── Customer segment signals

WANNEER CREDITS WORDEN VERDEELD:
├── Real-time bij elke conversie
├── Lookback window: 30-90 dagen (instelbaar)
├── Inclusief view-through conversions (indien enabled)
└── Cross-channel wanneer gelinkt (GA4)
```

### DDA Vereisten & Setup

```
DDA REQUIREMENTS CHECKLIST
══════════════════════════

MINIMUM VEREISTEN:
□ 600+ conversies per maand (per conversion action)
□ 15.000+ clicks per maand
□ 30 dagen historie met deze volumes
□ Conversion tracking correct geïmplementeerd

AANBEVOLEN VOOR OPTIMALE DDA:
□ 1000+ conversies per maand
□ Consistent tracking (geen gaps)
□ Cross-device tracking enabled
□ Enhanced conversions actief
□ Consent mode correct geconfigureerd

DDA ACTIVEREN:
1. Tools & Settings → Measurement → Conversions
2. Selecteer conversion action
3. Attribution model → "Data-driven"
4. Sla op

⚠️ BELANGRIJK:
├── DDA wordt per conversion action ingesteld
├── Niet alle actions hoeven DDA te gebruiken
├── Evalueer na 2-4 weken of data stabiel is
└── Fall-back naar Linear als data onvoldoende
```

### DDA Impact Analyseren

```
DDA vs LAST CLICK VERGELIJKING
══════════════════════════════

WAAR TE VINDEN:
Tools → Attribution → Model comparison

WAT JE ZIET:
┌─────────────────────────────────────────────────────────────┐
│ Campaign       │ Last Click │ Data-Driven │ Verschil       │
├────────────────┼────────────┼─────────────┼────────────────┤
│ Brand Search   │ 150 conv   │ 120 conv    │ -20% (↓)       │
│ Generic Search │ 80 conv    │ 95 conv     │ +19% (↑)       │
│ Display        │ 20 conv    │ 45 conv     │ +125% (↑)      │
│ YouTube        │ 10 conv    │ 35 conv     │ +250% (↑)      │
│ Shopping       │ 100 conv   │ 105 conv    │ +5%            │
└────────────────┴────────────┴─────────────┴────────────────┘

HOE TE INTERPRETEREN:
────────────────────
↑ Campaign krijgt MEER credit met DDA
  → Onderwaardering in Last Click
  → Overweeg budget verhoging

↓ Campaign krijgt MINDER credit met DDA
  → Overwaardering in Last Click
  → Heroverweeg budget allocatie

ACTIE BIJ SIGNIFICANTE VERSCHILLEN (>20%):
├── Analyseer conversion paths van die campaigns
├── Check assisted conversions
├── Pas budget allocatie aan op DDA waarden
└── Monitor voor 2-4 weken na wijziging
```

## Cross-Channel Attribution

### Google Ads + GA4 Integratie

```
CROSS-CHANNEL ATTRIBUTION SETUP
═══════════════════════════════

WAAROM CROSS-CHANNEL:
├── Google Ads ziet alleen Google touchpoints
├── GA4 ziet alle kanalen (organic, social, email, etc.)
├── Betere full-funnel attribution
└── Accuratere budget allocatie

SETUP STAPPEN:
──────────────
1. LINK GOOGLE ADS AAN GA4
   □ GA4 → Admin → Product Links → Google Ads
   □ Enable auto-tagging in Google Ads
   □ Importeer conversies naar Google Ads (optioneel)

2. CONFIGUREER ATTRIBUTION IN GA4
   □ Admin → Attribution Settings
   □ Reporting attribution model: Data-driven
   □ Lookback window: 90 dagen (of naar behoefte)
   □ Enable "Include Google signals data"

3. ANALYSEER CROSS-CHANNEL PATHS
   □ GA4 → Advertising → Attribution → Conversion paths
   □ Filter op verschillende channel groupings
   □ Vergelijk paid vs organic touchpoints

4. IMPORTEER GA4 CONVERSIONS (optioneel)
   □ Tools → Measurement → Conversions → Import
   □ Selecteer GA4 property
   □ Kies conversion events
   □ Let op: Andere attribution mogelijk dan native GA conversions
```

### Conversion Path Analyse

```
CONVERSION PATH ANALYSE
═══════════════════════

WAAR TE VINDEN (GA4):
Advertising → Attribution → Conversion paths

WAT JE ANALYSEERT:
──────────────────

1. TOP CONVERTING PATHS
   Paid Search → Organic → Direct → Conversie
   Display → Paid Search → Paid Search → Conversie

   → Identificeer typische customer journeys
   → Begrijp rol van elk kanaal

2. PATH LENGTH DISTRIBUTION
   ┌────────────────────────────────────────┐
   │ Touchpoints │ % Conversies │ Trend     │
   ├─────────────┼──────────────┼───────────┤
   │ 1           │ 35%          │ Direct    │
   │ 2-3         │ 40%          │ Short     │
   │ 4-6         │ 18%          │ Medium    │
   │ 7+          │ 7%           │ Complex   │
   └─────────────┴──────────────┴───────────┘

   → Langere paths = meer assisted value
   → Korte paths = sterke bottom-funnel

3. TIME TO CONVERSION
   ┌────────────────────────────────────────┐
   │ Dagen       │ % Conversies │ Type      │
   ├─────────────┼──────────────┼───────────┤
   │ Dag 0       │ 45%          │ Impulse   │
   │ 1-7 dagen   │ 30%          │ Short     │
   │ 8-30 dagen  │ 20%          │ Medium    │
   │ 30+ dagen   │ 5%           │ Long      │
   └─────────────┴──────────────┴───────────┘

   → Bepaalt lookback window keuze
   → Beïnvloedt remarketing strategie

4. ASSISTED VS LAST CLICK
   Per campaign/channel:
   ├── Assisted conversions (in pad, niet laatste)
   ├── Last click conversions (finale touch)
   └── Assisted/Last ratio

   Ratio > 1: Channel is "assister" (top-funnel)
   Ratio < 1: Channel is "closer" (bottom-funnel)
```

## Attribution Model Selectie

### Decision Framework

```
ATTRIBUTION MODEL SELECTION FRAMEWORK
═════════════════════════════════════

STAP 1: CHECK DATA VOLUMES
──────────────────────────
Conversies per maand:
├── <300 → Start met Last Click of Time Decay
├── 300-600 → Time Decay of Position Based
└── >600 → Data-Driven Attribution

STAP 2: ANALYSEER BUSINESS MODEL
────────────────────────────────
┌─────────────────────────┬──────────────────────────────────┐
│ Business Type           │ Aanbevolen Model                 │
├─────────────────────────┼──────────────────────────────────┤
│ Impulse e-commerce      │ Last Click of Time Decay         │
│ (<7 dagen decision)     │                                  │
├─────────────────────────┼──────────────────────────────────┤
│ Considered e-commerce   │ Position Based of DDA            │
│ (7-30 dagen decision)   │                                  │
├─────────────────────────┼──────────────────────────────────┤
│ B2B Lead Gen            │ Position Based of DDA            │
│ (lange sales cycle)     │                                  │
├─────────────────────────┼──────────────────────────────────┤
│ Brand-focused           │ First Click of Position Based    │
│ (awareness priority)    │                                  │
├─────────────────────────┼──────────────────────────────────┤
│ Multi-channel mature    │ Data-Driven Attribution          │
│ (veel kanalen actief)   │                                  │
└─────────────────────────┴──────────────────────────────────┘

STAP 3: EVALUEER HUIDIGE PERFORMANCE GAPS
─────────────────────────────────────────
Vragen om te beantwoorden:
□ Worden awareness campaigns onderwaareerd?
□ Krijgt brand search te veel credit?
□ Is er disconnect tussen ad spend en revenue?
□ Zijn bepaalde channels "onzichtbaar"?

Als JA op meerdere: Overweeg DDA of Position Based.
```

### Model Transitie Strategie

```
OVERSTAPPEN NAAR NIEUW ATTRIBUTION MODEL
════════════════════════════════════════

STAP 1: BASELINE DOCUMENTATIE (Week -1)
───────────────────────────────────────
□ Export huidige performance per campaign
□ Noteer conversion volumes per kanaal
□ Screenshot attribution reports
□ Documenteer huidige ROAS/CPA targets

STAP 2: MODEL VERGELIJKING (Week 0)
───────────────────────────────────
□ Tools → Attribution → Model Comparison
□ Vergelijk huidig model vs nieuw model
□ Identificeer campaigns met grote shifts
□ Bereken nieuwe targets:
  └── Nieuwe target = Oude target × (Nieuw/Oud ratio)

STAP 3: STAKEHOLDER COMMUNICATIE
────────────────────────────────
□ Leg uit waarom verandering
□ Toon verwachte impact per campaign
□ Manage verwachtingen (numbers zullen anders zijn)
□ Stel review moment in (4 weken)

STAP 4: IMPLEMENTATIE (Week 1)
──────────────────────────────
□ Wijzig attribution model in conversion settings
□ Update bidding targets (indien nodig)
□ Monitor eerste 7 dagen intensief
□ GEEN grote budget wijzigingen

STAP 5: EVALUATIE (Week 4)
──────────────────────────
□ Vergelijk pre vs post switch
□ Analyseer Smart Bidding performance
□ Check voor anomalieën
□ Fine-tune targets indien nodig

⚠️ BELANGRIJKE WAARSCHUWINGEN:
├── Attribution verandering = geen "echte" performance change
├── Smart Bidding past zich automatisch aan
├── Rapportages worden anders, niet beter/slechter
└── Geef het minimaal 4 weken
```

## Multi-Touch Attribution Strategie

### Assisted Conversions Analyse

```
ASSISTED CONVERSIONS ANALYSEREN
═══════════════════════════════

WAT ZIJN ASSISTED CONVERSIONS:
├── Touchpoints in conversion path die NIET laatste zijn
├── Tonen "ondersteunende" rol van campaigns
├── Cruciaal voor full-funnel budget allocation
└── Vaak onderwaareerd in Last Click

WAAR TE VINDEN:
Tools → Attribution → Top paths
Tools → Attribution → Assisted conversions

HOE TE GEBRUIKEN:
─────────────────

1. IDENTIFICEER "HIDDEN GEMS"
   Campaigns met:
   ├── Weinig last-click conversies
   ├── Veel assisted conversies
   └── Hoge assisted/last ratio

   → Deze campaigns zijn top-funnel initiators
   → Ondersteunen andere campaigns
   → Niet beoordelen op directe conversies

2. BEREKEN VOLLEDIGE WAARDE
   Total Value = Last Click Conv × Avg Value
                 + Assisted Conv × (Avg Value × Weight)

   Weight suggestie:
   ├── 0.3-0.5 voor awareness (Display, Video)
   ├── 0.5-0.7 voor consideration (Generic Search)
   └── 0.8-1.0 voor high-intent assisted

3. BUDGET ALLOCATIE
   ┌────────────────────────────────────────────────────┐
   │ Campaign Type    │ Eval Metric      │ Budget Role  │
   ├──────────────────┼──────────────────┼──────────────┤
   │ Display/Video    │ Assisted Conv    │ Top-funnel   │
   │ Generic Search   │ Assisted + Last  │ Mid-funnel   │
   │ Brand Search     │ Last Click       │ Bottom       │
   │ Shopping/PMax    │ Total Conv       │ Full-funnel  │
   └──────────────────┴──────────────────┴──────────────┘
```

### Attribution Windows

```
LOOKBACK WINDOW OPTIMALISATIE
═════════════════════════════

WAT IS LOOKBACK WINDOW:
├── Periode waarin touchpoints worden meegerekend
├── Click-through: 30 dagen default (1-90 mogelijk)
├── View-through: 1 dag default (1-30 mogelijk)
└── Engaged-view: 3 dagen default (video)

HOE JUISTE WINDOW TE BEPALEN:
─────────────────────────────

STAP 1: Analyseer Time to Conversion
GA4 → Advertising → Attribution → Conversion paths → Time to conversion

STAP 2: Bepaal Optimal Window
┌─────────────────────────────────────────────────────────┐
│ Als 90%+ conversies binnen X dagen → Window = X + buffer│
└─────────────────────────────────────────────────────────┘

TYPISCHE WINDOWS PER INDUSTRY:
─────────────────────────────
E-commerce (impuls):
├── Click-through: 7-14 dagen
├── View-through: 1 dag
└── Reden: Korte decision cycle

E-commerce (high-value):
├── Click-through: 30 dagen
├── View-through: 7 dagen
└── Reden: Meer research nodig

B2B Lead Gen:
├── Click-through: 60-90 dagen
├── View-through: 7-14 dagen
└── Reden: Lange sales cycle

Travel/Finance:
├── Click-through: 30-60 dagen
├── View-through: 7 dagen
└── Reden: Comparison shopping

INSTELLEN:
Tools → Measurement → Conversions → [Action] →
Edit settings → Lookback window
```

## Google Ads Script: Attribution Analyzer

```javascript
/**
 * Attribution Model Comparison Analyzer
 *
 * Analyseert verschil tussen Last Click en Data-Driven Attribution
 * voor budget allocatie optimalisatie.
 *
 * Let op: Dit script gebruikt Search Query Report data als proxy,
 * echte DDA data is alleen via UI beschikbaar.
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Schedule: Wekelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',
  DATE_RANGE: 'LAST_30_DAYS',

  // Threshold voor significante verschillen (20% = 0.20)
  SIGNIFICANCE_THRESHOLD: 0.20,

  // Minimum conversies voor analyse
  MIN_CONVERSIONS: 5
};

function main() {
  var report = {
    summary: {},
    campaigns: [],
    recommendations: []
  };

  // Analyseer campaign performance
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  var totalConversions = 0;
  var campaignData = [];

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var stats = campaign.getStatsFor(CONFIG.DATE_RANGE);
    var conversions = stats.getConversions();
    var cost = stats.getCost();
    var clicks = stats.getClicks();

    if (conversions >= CONFIG.MIN_CONVERSIONS) {
      var data = {
        name: campaign.getName(),
        type: getCampaignType(campaign.getName()),
        conversions: conversions,
        cost: cost,
        cpa: cost / conversions,
        clicks: clicks
      };

      // Schat assisted conversions (proxy via search terms)
      data.assistedRatio = estimateAssistedRatio(campaign);
      data.estimatedTotalValue = conversions * (1 + data.assistedRatio);

      campaignData.push(data);
      totalConversions += conversions;
    }
  }

  report.summary = {
    totalCampaigns: campaignData.length,
    totalConversions: totalConversions,
    ddaEligible: totalConversions >= 600
  };

  // Identificeer opportunities
  report.campaigns = campaignData.sort(function(a, b) {
    return b.assistedRatio - a.assistedRatio;
  });

  // Genereer aanbevelingen
  report.recommendations = generateRecommendations(report);

  sendReport(report);
  Logger.log('Attribution analysis complete');
}

function getCampaignType(name) {
  var nameLower = name.toLowerCase();
  if (nameLower.indexOf('brand') > -1) return 'Brand';
  if (nameLower.indexOf('display') > -1) return 'Display';
  if (nameLower.indexOf('video') > -1 || nameLower.indexOf('youtube') > -1) return 'Video';
  if (nameLower.indexOf('shopping') > -1 || nameLower.indexOf('pmax') > -1) return 'Shopping/PMax';
  return 'Generic Search';
}

function estimateAssistedRatio(campaign) {
  // Dit is een proxy - echte assisted data niet via API
  // Schatting op basis van campaign type
  var name = campaign.getName().toLowerCase();

  if (name.indexOf('display') > -1) return 0.8;
  if (name.indexOf('video') > -1 || name.indexOf('youtube') > -1) return 1.2;
  if (name.indexOf('brand') > -1) return 0.1;
  if (name.indexOf('shopping') > -1 || name.indexOf('pmax') > -1) return 0.3;
  return 0.4; // Generic search
}

function generateRecommendations(report) {
  var recs = [];

  // Check DDA eligibility
  if (!report.summary.ddaEligible) {
    recs.push({
      priority: 'INFO',
      action: 'Account heeft < 600 conversies/maand. DDA nog niet beschikbaar.',
      detail: 'Overweeg Time Decay of Position Based als alternatief.'
    });
  } else {
    recs.push({
      priority: 'HIGH',
      action: 'Account komt in aanmerking voor Data-Driven Attribution.',
      detail: 'Activeer DDA voor nauwkeurigere budget allocatie.'
    });
  }

  // Check voor hoge assisted ratio campaigns
  var highAssisted = report.campaigns.filter(function(c) {
    return c.assistedRatio > 0.5 && c.type !== 'Brand';
  });

  if (highAssisted.length > 0) {
    recs.push({
      priority: 'MEDIUM',
      action: highAssisted.length + ' campaigns worden mogelijk onderwaareerd met Last Click.',
      detail: 'Overweeg budget verhoging voor: ' +
              highAssisted.slice(0, 3).map(function(c) { return c.name; }).join(', ')
    });
  }

  return recs;
}

function sendReport(report) {
  var subject = 'Attribution Analysis - ' + AdsApp.currentAccount().getName();
  var body = 'Attribution Model Analysis Report\n';
  body += '=================================\n\n';

  body += 'SUMMARY:\n';
  body += '• Total campaigns analyzed: ' + report.summary.totalCampaigns + '\n';
  body += '• Total conversions: ' + report.summary.totalConversions + '\n';
  body += '• DDA eligible: ' + (report.summary.ddaEligible ? 'Yes' : 'No (need 600+)') + '\n\n';

  body += 'CAMPAIGN ANALYSIS (by estimated assisted value):\n';
  body += '────────────────────────────────────────────────\n';

  var topCampaigns = report.campaigns.slice(0, 10);
  for (var i = 0; i < topCampaigns.length; i++) {
    var c = topCampaigns[i];
    body += '• ' + c.name + '\n';
    body += '  Type: ' + c.type + ' | Conv: ' + c.conversions.toFixed(0);
    body += ' | Est. Assisted Ratio: ' + (c.assistedRatio * 100).toFixed(0) + '%\n';
  }

  body += '\nRECOMMENDATIONS:\n';
  body += '────────────────\n';

  for (var j = 0; j < report.recommendations.length; j++) {
    var rec = report.recommendations[j];
    body += '[' + rec.priority + '] ' + rec.action + '\n';
    body += '  → ' + rec.detail + '\n\n';
  }

  body += '\n---\nGenerated by Attribution Analyzer Script';
  body += '\nNote: Assisted ratios are estimates. Check UI for actual DDA data.';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Output: Attribution Model Recommendation Template

```markdown
# Attribution Model Recommendation

## Account Analyse
- **Monthly conversions:** [X]
- **Conversion types:** [Lead/Purchase/Multiple]
- **Current attribution model:** [Last Click/DDA/etc.]
- **Average path length:** [X touchpoints]
- **Average time to conversion:** [X dagen]

## Aanbevolen Attribution Model
**[MODEL NAAM]**

### Waarom Dit Model
1. [Reden 1 - gebaseerd op data volumes]
2. [Reden 2 - gebaseerd op business type]
3. [Reden 3 - gebaseerd op channel mix]

### Verwachte Impact per Campaign Type

| Campaign Type | Huidige Conv | Verwacht (nieuw model) | Verschil |
|---------------|--------------|------------------------|----------|
| Brand Search  | [X]          | [X]                    | [%]      |
| Generic Search| [X]          | [X]                    | [%]      |
| Display       | [X]          | [X]                    | [%]      |
| Shopping      | [X]          | [X]                    | [%]      |

### Implementatie Plan

**Week 1: Voorbereiding**
- Documenteer baseline metrics
- Bereken nieuwe ROAS/CPA targets
- Communiceer met stakeholders

**Week 2: Activatie**
- Wijzig attribution model in Google Ads
- Update conversion action settings
- Monitor dagelijks

**Week 3-4: Evaluatie**
- Vergelijk pre/post metrics
- Analyseer Smart Bidding impact
- Fine-tune targets

### Lookback Window Aanbeveling
- **Click-through:** [X] dagen
- **View-through:** [X] dagen
- **Engaged-view:** [X] dagen

### Cross-Channel Integratie
- [ ] GA4 linked aan Google Ads
- [ ] Import GA4 conversions (indien gewenst)
- [ ] Cross-device tracking enabled
- [ ] Enhanced conversions actief

### Monitoring Dashboard Setup
□ Model comparison report (weekly)
□ Path analysis review (monthly)
□ Assisted conversion tracking (ongoing)
□ Budget allocation review (quarterly)
```

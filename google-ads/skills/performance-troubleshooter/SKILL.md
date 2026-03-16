---
name: performance-troubleshooter
description: "Google Ads Performance Troubleshooter voor diagnose en oplossing van performance problemen. Gebruik voor: (1) CPA/ROAS degradatie analyseren, (2) Conversie drops onderzoeken, (3) Impression share dalingen oplossen, (4) Quality Score problemen fixen, (5) Budget en bidding issues troubleshooten. Triggers: performance drop, cpa stijging, roas daling, conversies gedaald, impressies gedaald, clicks gedaald, troubleshoot, diagnose, wat is er mis, probleem, degradatie."
---

# Performance Troubleshooter

Systematische gids voor het diagnosticeren en oplossen van Google Ads performance problemen met decision trees, root cause analyse en concrete oplossingen.

## Quick Diagnosis Guide

```
WELK PROBLEEM HEB JE?
│
├─► CONVERSIES GEDAALD
│   └─► Ga naar: "Conversie Drop Diagnose"
│
├─► CPA GESTEGEN / ROAS GEDAALD
│   └─► Ga naar: "Efficiency Degradatie Diagnose"
│
├─► IMPRESSIES / CLICKS GEDAALD
│   └─► Ga naar: "Volume Daling Diagnose"
│
├─► GEEN DELIVERY (0 impressies)
│   └─► Ga naar: "Delivery Problemen"
│
├─► QUALITY SCORE GEDAALD
│   └─► Ga naar: "Quality Score Troubleshoot"
│
└─► SMART BIDDING WERKT NIET
    └─► Ga naar: "Bidding Problemen"
```

## Conversie Drop Diagnose

### Decision Tree

```
CONVERSIES GEDAALD - DIAGNOSE
═════════════════════════════

START: Conversies zijn gedaald
│
├─► CHECK 1: Is tracking intact?
│   ├── Test conversie op website → Fired in Google Ads?
│   ├── Check Tag Assistant / Google Ads Conversions Report
│   └── Compare conversies in GA4 vs Google Ads
│       │
│       ├─► TRACKING BROKEN
│       │   └─► Fix: Check GTM, consent mode, tag status
│       │
│       └─► TRACKING OK → Ga naar Check 2
│
├─► CHECK 2: Zijn clicks gedaald?
│   ├── Compare clicks week-over-week
│   │
│   ├─► CLICKS GEDAALD
│   │   └─► Probleem is bovenstrooms (traffic)
│   │       └─► Ga naar "Volume Daling Diagnose"
│   │
│   └─► CLICKS STABIEL → Conversion Rate gedaald
│       └─► Ga naar Check 3
│
├─► CHECK 3: Is landing page veranderd?
│   ├── Check page speed (PageSpeed Insights)
│   ├── Check mobile experience
│   ├── Is form/checkout werkend?
│   │
│   ├─► LANDING PAGE ISSUE
│   │   └─► Fix: Rollback changes, fix bugs
│   │
│   └─► LANDING PAGE OK → Ga naar Check 4
│
├─► CHECK 4: Is traffic kwaliteit veranderd?
│   ├── Check search terms rapport
│   ├── Zijn er nieuwe query types?
│   ├── Check device/location shifts
│   │
│   ├─► TRAFFIC QUALITY ISSUE
│   │   └─► Fix: Negatives, targeting, bid adjustments
│   │
│   └─► TRAFFIC QUALITY OK → Ga naar Check 5
│
└─► CHECK 5: Externe factoren
    ├── Seizoenaliteit?
    ├── Competitor activiteit?
    ├── Market change?
    └─► Analyse en adapt strategy
```

### Conversie Tracking Verificatie

```
CONVERSIE TRACKING CHECK
════════════════════════

STAP 1: BASIC VERIFICATION
──────────────────────────
□ Google Ads → Tools → Conversions
□ Check "Recording status" per action
  ├── "Recording conversions" = OK
  ├── "No recent conversions" = Mogelijk issue
  └── "Tag inactive" = Probleem!

□ Conversions per dag grafiek bekijken
  └── Plotselinge drop = Tracking issue
  └── Geleidelijke daling = Andere oorzaak

STAP 2: TAG VERIFICATION
────────────────────────
Via Google Tag Assistant (Chrome Extension):
□ Laad conversion page
□ Check of conversie tag fired
□ Check of waarde correct is
□ Check consent mode status

Via Google Ads Tag Diagnostics:
□ Tools → Conversions → [Action] → Tag setup
□ Run diagnostics
□ Check website tag status

STAP 3: COMPARE SOURCES
───────────────────────
┌────────────────────────────────────────────────────────┐
│ Bron           │ Conversies │ Verschil vs GA4         │
├────────────────┼────────────┼─────────────────────────┤
│ Google Ads     │ [X]        │ Baseline                │
│ GA4 (Google)   │ [X]        │ Moet +/- gelijk zijn    │
│ CRM/Backend    │ [X]        │ Echte bron van waarheid │
└────────────────┴────────────┴─────────────────────────┘

Als grote discrepantie:
├── GA4 < Google Ads: Mogelijk duplicate tags
├── GA4 > Google Ads: Tracking niet volledig
└── CRM ≠ beide: Attribution/timing differences

STAP 4: CONSENT MODE CHECK
──────────────────────────
□ Is consent banner geïmplementeerd?
□ Wordt consent correct doorgegeven?
□ Zijn conversion modeling instellingen correct?
□ Check: "Consent mode" kolom in conversions

Consent Mode Impact:
├── Goed geconfigureerd: Google modeleert ~70-80%
├── Slecht geconfigureerd: Grote data gaps
└── Niet aanwezig: Potentiële compliance issues
```

## Efficiency Degradatie Diagnose

### CPA Gestegen

```
CPA GESTEGEN - ROOT CAUSE ANALYSE
═════════════════════════════════

MOGELIJKE OORZAKEN (in volgorde van waarschijnlijkheid):

1. COMPETITION INCREASED
───────────────────────
Symptomen:
├── Avg CPC gestegen
├── Impression share gedaald
├── Same queries, hogere kosten

Verificatie:
└── Auction Insights bekijken
    ├── Nieuwe competitors?
    ├── Overlap rate veranderd?
    └── Outranking share gedaald?

Oplossing:
├── Budget verhogen (als ROI positief blijft)
├── Focus op efficiency (neg keywords, targeting)
├── Differentiate (ad copy, landing page)
└── Explore andere channels

2. QUALITY SCORE GEDAALD
────────────────────────
Symptomen:
├── QS kolom toont daling
├── Hogere CPCs nodig voor zelfde positie
├── Expected CTR/Ad Relevance/LP experience gedaald

Verificatie:
└── Columns → Quality Score (historisch) bekijken

Oplossing:
└── Zie "Quality Score Troubleshoot" sectie

3. AUDIENCE/TRAFFIC SHIFT
─────────────────────────
Symptomen:
├── Andere demografics converteren
├── Device mix verschoven
├── Geografische shifts

Verificatie:
├── Segment by device/location/audience
└── Compare converters vs non-converters

Oplossing:
├── Bid adjustments per segment
├── Separate campaigns voor beste segments
└── Exclude underperforming segments

4. LANDING PAGE PERFORMANCE
───────────────────────────
Symptomen:
├── Bounce rate gestegen
├── Time on site gedaald
├── Form abandonment gestegen

Verificatie:
├── GA4 landing page report
├── User recordings (Hotjar/FullStory)
└── Page speed check

Oplossing:
├── Fix page speed issues
├── Improve mobile experience
├── Simplify conversion flow
└── A/B test landing page variants

5. SEASONALITY
──────────────
Symptomen:
├── Historisch dezelfde periode = slechter
├── Industry-wide trends
├── Holiday/event impact

Verificatie:
├── Year-over-year vergelijking
└── Industry benchmarks checken

Oplossing:
├── Adjust expectations
├── Seasonality adjustments in bidding
└── Prep for high season
```

### ROAS Gedaald

```
ROAS GEDAALD - DIAGNOSE
═══════════════════════

ROAS = Revenue / Ad Spend

ROAS gedaald kan komen door:
├── A) Zelfde revenue, hogere spend
├── B) Lagere revenue, zelfde spend
└── C) Combinatie

DIAGNOSE:

SCENARIO A: SPEND GESTEGEN
──────────────────────────
Check:
├── Budget automatisch verhoogd?
├── Bid strategy changed?
├── CPCs gestegen (competition)?

Oplossing:
├── Review budget settings
├── Check Smart Bidding targets
└── Analyse CPC trends

SCENARIO B: REVENUE GEDAALD
───────────────────────────
Check:
├── Average Order Value (AOV) gedaald?
├── Minder aankopen?
├── Product mix verschoven?

AOV gedaald:
├── Goedkopere producten gepromoot?
├── Discounting toegenomen?
├── Upsell/cross-sell niet werkend?

Minder aankopen:
├── Conversion rate check (zie eerder)
├── Cart abandonment gestegen?
├── Payment issues?

Oplossing:
├── Promote higher-margin products
├── Review promotional strategy
├── Check checkout flow
└── Value-based bidding inzetten

SCENARIO C: BOTH FACTORS
────────────────────────
Combinatie van bovenstaande - vaak bij:
├── Market downturn
├── Sterke competitor entry
├── Major algorithm change

Actie:
├── Full audit uitvoeren
├── Competitive analysis
└── Strategy heroverweging
```

## Volume Daling Diagnose

### Impressies Gedaald

```
IMPRESSIES GEDAALD - TROUBLESHOOT
═════════════════════════════════

CHECK 1: BUDGET & BIDDING
─────────────────────────
□ Budget limited status?
□ Bid too low voor posities?
□ Target CPA/ROAS te agressief?

Budget Limited:
├── Verhoog budget
├── Of: Prioriteer best performers
└── Of: Reduce targets om binnen budget te blijven

Bid Limited:
├── Verhoog bids/targets
├── Check search impression share (rank)
└── Improve Quality Score

CHECK 2: TARGETING CHANGES
──────────────────────────
□ Zijn keywords gepauzeerd?
□ Locatie targeting veranderd?
□ Device targeting veranderd?
□ Audience targeting (exclusions)?

Recent changes bekijken:
├── Change History in Google Ads
└── Rollback indien nodig

CHECK 3: ADS/KEYWORDS STATUS
────────────────────────────
□ Ads disapproved?
□ Keywords suspended?
□ Policy violations?

Check:
├── Ads → Status kolom
├── Keywords → Status kolom
└── Notifications/Emails

CHECK 4: SEARCH DEMAND
──────────────────────
□ Keyword Planner: search volume veranderd?
□ Seasonality effect?
□ Market trend shift?

Trend check:
├── Google Trends voor key terms
└── Year-over-year comparison

CHECK 5: AUCTION DYNAMICS
─────────────────────────
□ Auction Insights: nieuwe competitors?
□ CPCs gestegen (maar bids niet)?
□ Market consolidation?

IMPRESSION SHARE BREAKDOWN:
──────────────────────────
┌─────────────────────────────────────────────────────────┐
│ Metric                    │ Betekenis                   │
├───────────────────────────┼─────────────────────────────┤
│ Search Impression Share   │ % van eligible impressies   │
├───────────────────────────┼─────────────────────────────┤
│ Lost IS (Budget)          │ Gemist door budget          │
├───────────────────────────┼─────────────────────────────┤
│ Lost IS (Rank)            │ Gemist door lage Ad Rank    │
└───────────────────────────┴─────────────────────────────┘

Als Lost IS (Budget) hoog:
└── Verhoog budget of focus op efficiency

Als Lost IS (Rank) hoog:
└── Verbeter Quality Score of verhoog bids
```

### Clicks Gedaald (maar Impressies Stabiel)

```
CTR GEDAALD - DIAGNOSE
══════════════════════

SYMPTOOM: Impressies stabiel, clicks gedaald = CTR drop

CHECK 1: AD COPY/CREATIVE
─────────────────────────
□ Ads gewijzigd?
□ RSA assets in rotatie veranderd?
□ Ad strength gedaald?
□ Extensions verwijderd/gepauzeerd?

Verificatie:
├── Compare ad performance pre/post
├── Check RSA asset performance
└── Review extension status

Oplossing:
├── Revert ad changes
├── Add winning assets
├── Restore extensions
└── Test new variations

CHECK 2: SEARCH TERMS SHIFT
───────────────────────────
□ Andere queries triggering ads?
□ Broad match expansion?
□ Low-intent queries?

Verificatie:
├── Search Terms rapport
├── Compare top queries pre/post
└── Check query intent

Oplossing:
├── Add negative keywords
├── Adjust match types
└── Refine ad copy voor queries

CHECK 3: COMPETITOR ADS
───────────────────────
□ Competitors met betere offers?
□ Competitors met extensions jij niet hebt?
□ Competitors in hogere posities?

Verificatie:
├── Manual search checks
├── Auction Insights
└── SEMrush/SpyFu competitor analysis

Oplossing:
├── Improve ad USPs
├── Add missing extensions
├── Test promotional offers
└── Bid for better positions (test)

CHECK 4: AD POSITION
────────────────────
□ Average position gedaald?
□ Top of page rate gedaald?

Verificatie:
├── "Search top IS" metric
├── "Abs. top IS" metric
└── Average position trend

Correlatie:
├── Lower position = lower CTR (verwacht)
└── Focus op impression share vs position trade-off

CHECK 5: AUDIENCE FATIGUE
─────────────────────────
□ Retargeting audiences overexposed?
□ Frequency te hoog?
□ Display/Video ad fatigue?

Symptomen:
├── CTR daalt over tijd
├── Zelfde audience te lang bereikt
└── Creative "blind" geworden

Oplossing:
├── Refresh creatives
├── Expand audiences
├── Implement frequency capping
```

## Delivery Problemen

### Geen Impressies

```
0 IMPRESSIES - TROUBLESHOOT
═══════════════════════════

⚠️ URGENTIE: Geen spend = geen resultaten

STEP-BY-STEP DIAGNOSE:

1. CAMPAIGN STATUS
──────────────────
□ Campaign enabled?
□ Geen "Removed" status?
□ Start/end dates correct?
□ Budget > €0?

2. AD GROUP STATUS
──────────────────
□ Ad groups enabled?
□ Minimaal 1 active ad?
□ Minimaal 1 active keyword (Search)?

3. ADS STATUS
─────────────
□ Ads approved?
□ Geen "Policy violation"?
□ Geen "Under review" (te lang)?

Common disapprovals:
├── Trademark issues
├── Misleading content
├── Unavailable landing page
├── Prohibited content
└── Technical issues (redirects)

4. KEYWORDS STATUS
──────────────────
□ Keywords active?
□ Geen "Low search volume"?
□ Geen "Suspended"?
□ Bids niet €0?

5. TARGETING
────────────
□ Locations correct ingesteld?
□ Languages correct?
□ Schedule niet te restrictief?
□ Audiences niet exclusions-only?

6. BUDGET & BIDS
────────────────
□ Budget sufficient?
□ Bids sufficient voor markt?
□ Target CPA/ROAS niet te agressief?

7. BILLING
──────────
□ Payment method valid?
□ Geen account suspension?
□ Credit line beschikbaar?

QUICK FIX CHECKLIST:
───────────────────
If new campaign:
□ Wacht 24-48 uur voor initial approval
□ Check policy centre voor issues
□ Verify billing setup

If existing campaign suddenly stopped:
□ Check Change History voor recent changes
□ Check Notifications voor warnings
□ Review Billing for payment issues
```

## Quality Score Troubleshoot

### Diagnose

```
QUALITY SCORE ANALYSE
═════════════════════

QUALITY SCORE COMPONENTEN:
──────────────────────────
┌─────────────────────────────────────────────────────────┐
│ Component              │ Weight │ Wat het meet          │
├────────────────────────┼────────┼───────────────────────┤
│ Expected CTR           │ ~40%   │ Likelihood van click  │
├────────────────────────┼────────┼───────────────────────┤
│ Ad Relevance           │ ~20%   │ Match query↔ad copy   │
├────────────────────────┼────────┼───────────────────────┤
│ Landing Page Exp       │ ~40%   │ Page quality & match  │
└────────────────────────┴────────┴───────────────────────┘

HOE TE ANALYSEREN:
─────────────────
Columns toevoegen:
├── Quality Score
├── Quality Score (hist.)
├── Expected CTR
├── Expected CTR (hist.)
├── Ad Relevance
├── Ad Relevance (hist.)
├── Landing Page Exp
└── Landing Page Exp (hist.)

Filter op:
├── QS < 5 (priority fix)
├── High impressie keywords met lage QS
└── Keywords met QS daling vs vorige maand

STATUS INTERPRETATIE:
─────────────────────
"Below average" = Probleem, actie vereist
"Average" = OK, kan beter
"Above average" = Goed, behouden
```

### Oplossingen per Component

```
EXPECTED CTR - VERBETEREN
═════════════════════════

OORZAKEN LAGE EXPECTED CTR:
├── Ad copy niet compelling
├── Geen sterke CTA
├── Competitors hebben betere ads
└── Keyword-ad mismatch

OPLOSSINGEN:
────────────

1. AD COPY VERBETEREN
   □ Include keyword in headline 1
   □ Sterke, specifieke CTA
   □ USPs en differentiators
   □ Numbers en specifics (15% korting, 500+ reviews)

2. GEBRUIK ALLE AD ASSETS
   □ 15 headlines in RSA
   □ 4 descriptions
   □ Pin alleen strategisch
   □ Test variaties

3. EXTENSIONS TOEVOEGEN
   □ Sitelinks (min 4)
   □ Callouts (min 4)
   □ Structured snippets
   □ Call/location extensions

4. TEST & ITERATE
   □ A/B test ad variations
   □ Review top performing ads
   □ Pause underperformers
   □ Check RSA asset performance

─────────────────────────────────────────────────────────

AD RELEVANCE - VERBETEREN
═════════════════════════

OORZAKEN LAGE AD RELEVANCE:
├── Keywords niet in ad copy
├── Te brede ad groups
├── Generic ads voor specific keywords
└── Outdated ads

OPLOSSINGEN:
────────────

1. KEYWORD IN AD COPY
   □ Exact keyword in headline (waar mogelijk)
   □ Keyword in description
   □ Gebruik {KeyWord:Default} insertion

2. AD GROUP STRUCTUUR
   □ Tight theme ad groups (5-20 keywords)
   □ Ads specifiek voor ad group theme
   □ Overweeg SKAGs voor top performers
   └── (Single Keyword Ad Groups)

3. DYNAMIC KEYWORD INSERTION
   □ {KeyWord:Fallback}
   □ Alleen voor relevante positions
   □ Check voor awkward insertions

4. REFRESH AD COPY
   □ Verwijder outdated messaging
   □ Update voor huidige promoties
   □ Match current landing page

─────────────────────────────────────────────────────────

LANDING PAGE EXPERIENCE - VERBETEREN
════════════════════════════════════

OORZAKEN LAGE LANDING PAGE EXP:
├── Slow page load
├── Poor mobile experience
├── Content mismatch met ad
├── Difficult navigation
└── Missing trust signals

OPLOSSINGEN:
────────────

1. PAGE SPEED
   □ Target: <3 sec load time
   □ Use PageSpeed Insights
   □ Optimize images
   □ Minimize scripts
   □ Enable caching

2. MOBILE EXPERIENCE
   □ Responsive design
   □ Tap targets groot genoeg
   □ No horizontal scrolling
   □ Easy form filling

3. CONTENT RELEVANCE
   □ Headline matches ad
   □ Keyword in page title/H1
   □ Clear path to conversion
   □ No bait-and-switch

4. USER EXPERIENCE
   □ Clear navigation
   □ Trust signals (reviews, badges)
   □ Contact info visible
   □ Privacy policy linked

5. TECHNICAL SEO
   □ HTTPS required
   □ No broken links
   □ Proper meta tags
   □ Clean URL structure
```

## Bidding Problemen

### Smart Bidding Issues

```
SMART BIDDING TROUBLESHOOT
══════════════════════════

PROBLEEM 1: DELIVERY STOPS/DROPS
────────────────────────────────
Symptoom: Impressies plotseling gedaald

Oorzaken:
├── Target te agressief
├── Budget te laag
├── Competition increased
└── Tracking issue

Diagnose:
├── Check bid strategy status
├── Compare target vs actual CPA/ROAS
├── Check conversion tracking
└── Review auction insights

Oplossing:
├── Relax target (20%)
├── Increase budget
├── Switch naar "Maximize" (tijdelijk)
└── Fix tracking issues

PROBLEEM 2: CPA/ROAS WEG VAN TARGET
───────────────────────────────────
Symptoom: Actual ver boven/onder target

Oorzaken:
├── Unrealistic target
├── Market changed
├── Insufficient conversions
└── Learning phase

Diagnose:
├── Check historische CPA/ROAS
├── Vergelijk target vs market benchmarks
├── Check conversion volume
└── Check learning status

Oplossing:
├── Adjust target naar achievable
├── Use "Maximize" voor data collection
├── Increase volume (budget/targeting)
└── Wait for learning complete

PROBLEEM 3: ERRATIC PERFORMANCE
───────────────────────────────
Symptoom: Grote dag-tot-dag swings

Oorzaken:
├── Low conversion volume
├── Inconsistent demand
├── Budget limiting mid-day
└── Competitor auction dynamics

Diagnose:
├── Check daily conversions (need 15+)
├── Check budget utilization pattern
├── Review hourly performance
└── Compare to historical volatility

Oplossing:
├── Increase conversions (budget/targeting)
├── Portfolio bid strategy (aggregate)
├── Smooth budget pacing
└── Accept some volatility (normal)

PROBLEEM 4: NOT LEARNING
────────────────────────
Symptoom: "Learning Limited" blijft

Zie → "Learning Phase Tracker" skill
```

## Google Ads Script: Performance Alert System

```javascript
/**
 * Performance Troubleshoot Alert System
 *
 * Detecteert en rapporteert performance anomalieën.
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Schedule: Dagelijks om 8:00
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Lookback periods
  COMPARE_DAYS: 7,
  BASELINE_DAYS: 14,

  // Alert thresholds (percentage change)
  ALERTS: {
    // Critical alerts (immediate attention)
    CONVERSIONS_DROP_CRITICAL: -0.50,  // -50%
    SPEND_ZERO: true,                   // No spend
    TRACKING_BROKEN: true,              // 0 conversions

    // Warning alerts
    CPA_SPIKE: 0.30,            // +30%
    ROAS_DROP: -0.25,           // -25%
    CTR_DROP: -0.20,            // -20%
    IMPRESSIONS_DROP: -0.30,    // -30%
    CONVERSIONS_DROP: -0.25     // -25%
  },

  // Minimum data for alerts
  MIN_IMPRESSIONS: 100,
  MIN_CLICKS: 20,
  MIN_CONVERSIONS: 3
};

function main() {
  var report = {
    critical: [],
    warnings: [],
    info: [],
    summary: {}
  };

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  var campaignCount = 0;
  var alertCount = 0;

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var alerts = analyzeCampaignPerformance(campaign);

    report.critical = report.critical.concat(alerts.critical);
    report.warnings = report.warnings.concat(alerts.warnings);
    report.info = report.info.concat(alerts.info);

    alertCount += alerts.critical.length + alerts.warnings.length;
    campaignCount++;
  }

  report.summary = {
    campaignsAnalyzed: campaignCount,
    criticalAlerts: report.critical.length,
    warnings: report.warnings.length,
    timestamp: new Date().toISOString()
  };

  // Always send if critical alerts, otherwise only if warnings
  if (report.critical.length > 0 || report.warnings.length > 0) {
    sendAlertEmail(report);
  }

  Logger.log('Performance analysis complete');
  Logger.log('Campaigns: ' + campaignCount + ', Alerts: ' + alertCount);
}

function analyzeCampaignPerformance(campaign) {
  var name = campaign.getName();
  var alerts = { critical: [], warnings: [], info: [] };

  // Get stats for comparison periods
  var currentStats = campaign.getStatsFor('LAST_7_DAYS');
  var baselineStats = campaign.getStatsFor('LAST_14_DAYS');

  // Calculate current vs baseline
  var current = {
    impressions: currentStats.getImpressions(),
    clicks: currentStats.getClicks(),
    cost: currentStats.getCost(),
    conversions: currentStats.getConversions(),
    convValue: currentStats.getConversionValue()
  };

  // Baseline (previous period = last 14 days minus last 7 days)
  var baseline = {
    impressions: baselineStats.getImpressions() - current.impressions,
    clicks: baselineStats.getClicks() - current.clicks,
    cost: baselineStats.getCost() - current.cost,
    conversions: baselineStats.getConversions() - current.conversions,
    convValue: baselineStats.getConversionValue() - current.convValue
  };

  // Calculated metrics
  current.ctr = current.impressions > 0 ?
    current.clicks / current.impressions : 0;
  current.cpa = current.conversions > 0 ?
    current.cost / current.conversions : 0;
  current.roas = current.cost > 0 ?
    current.convValue / current.cost : 0;

  baseline.ctr = baseline.impressions > 0 ?
    baseline.clicks / baseline.impressions : 0;
  baseline.cpa = baseline.conversions > 0 ?
    baseline.cost / baseline.conversions : 0;
  baseline.roas = baseline.cost > 0 ?
    baseline.convValue / baseline.cost : 0;

  // CRITICAL ALERTS

  // Zero spend
  if (current.cost === 0 && baseline.cost > 0) {
    alerts.critical.push({
      campaign: name,
      type: 'NO_SPEND',
      message: 'Geen spend in afgelopen 7 dagen',
      baseline: '€' + baseline.cost.toFixed(2) + ' (vorige week)'
    });
  }

  // Tracking broken (had conversions, now 0)
  if (current.conversions === 0 && baseline.conversions > 3) {
    alerts.critical.push({
      campaign: name,
      type: 'TRACKING_ISSUE',
      message: '0 conversies terwijl vorige periode ' + baseline.conversions.toFixed(0) + ' had',
      action: 'Check conversion tracking'
    });
  }

  // Conversion drop critical
  if (baseline.conversions >= CONFIG.MIN_CONVERSIONS) {
    var convChange = (current.conversions - baseline.conversions) / baseline.conversions;
    if (convChange <= CONFIG.ALERTS.CONVERSIONS_DROP_CRITICAL) {
      alerts.critical.push({
        campaign: name,
        type: 'CONVERSION_CRASH',
        message: 'Conversies gedaald met ' + (convChange * 100).toFixed(0) + '%',
        current: current.conversions.toFixed(0),
        baseline: baseline.conversions.toFixed(0)
      });
    }
  }

  // WARNINGS

  // Skip if insufficient data
  if (baseline.impressions < CONFIG.MIN_IMPRESSIONS) {
    return alerts;
  }

  // CPA spike
  if (baseline.cpa > 0 && current.cpa > 0) {
    var cpaChange = (current.cpa - baseline.cpa) / baseline.cpa;
    if (cpaChange >= CONFIG.ALERTS.CPA_SPIKE) {
      alerts.warnings.push({
        campaign: name,
        type: 'CPA_SPIKE',
        message: 'CPA gestegen met ' + (cpaChange * 100).toFixed(0) + '%',
        current: '€' + current.cpa.toFixed(2),
        baseline: '€' + baseline.cpa.toFixed(2)
      });
    }
  }

  // ROAS drop
  if (baseline.roas > 0 && current.roas > 0) {
    var roasChange = (current.roas - baseline.roas) / baseline.roas;
    if (roasChange <= CONFIG.ALERTS.ROAS_DROP) {
      alerts.warnings.push({
        campaign: name,
        type: 'ROAS_DROP',
        message: 'ROAS gedaald met ' + (Math.abs(roasChange) * 100).toFixed(0) + '%',
        current: (current.roas * 100).toFixed(0) + '%',
        baseline: (baseline.roas * 100).toFixed(0) + '%'
      });
    }
  }

  // CTR drop
  if (baseline.ctr > 0) {
    var ctrChange = (current.ctr - baseline.ctr) / baseline.ctr;
    if (ctrChange <= CONFIG.ALERTS.CTR_DROP) {
      alerts.warnings.push({
        campaign: name,
        type: 'CTR_DROP',
        message: 'CTR gedaald met ' + (Math.abs(ctrChange) * 100).toFixed(0) + '%',
        current: (current.ctr * 100).toFixed(2) + '%',
        baseline: (baseline.ctr * 100).toFixed(2) + '%'
      });
    }
  }

  // Impressions drop
  var impChange = (current.impressions - baseline.impressions) / baseline.impressions;
  if (impChange <= CONFIG.ALERTS.IMPRESSIONS_DROP) {
    alerts.warnings.push({
      campaign: name,
      type: 'IMPRESSIONS_DROP',
      message: 'Impressies gedaald met ' + (Math.abs(impChange) * 100).toFixed(0) + '%',
      current: current.impressions,
      baseline: baseline.impressions
    });
  }

  return alerts;
}

function sendAlertEmail(report) {
  var subject = '[ALERT] Performance Issues - ' + AdsApp.currentAccount().getName();

  if (report.critical.length > 0) {
    subject = '[CRITICAL] ' + subject;
  }

  var body = 'Google Ads Performance Alert Report\n';
  body += '====================================\n';
  body += 'Generated: ' + new Date().toLocaleString() + '\n\n';

  body += 'SUMMARY:\n';
  body += '• Campaigns analyzed: ' + report.summary.campaignsAnalyzed + '\n';
  body += '• Critical alerts: ' + report.summary.criticalAlerts + '\n';
  body += '• Warnings: ' + report.summary.warnings + '\n\n';

  if (report.critical.length > 0) {
    body += '🚨 CRITICAL ALERTS (Immediate Action Required):\n';
    body += '───────────────────────────────────────────────\n';

    for (var i = 0; i < report.critical.length; i++) {
      var alert = report.critical[i];
      body += '• ' + alert.campaign + '\n';
      body += '  Issue: ' + alert.message + '\n';
      if (alert.current) body += '  Current: ' + alert.current + '\n';
      if (alert.baseline) body += '  Baseline: ' + alert.baseline + '\n';
      if (alert.action) body += '  Action: ' + alert.action + '\n';
      body += '\n';
    }
  }

  if (report.warnings.length > 0) {
    body += '⚠️ WARNINGS:\n';
    body += '────────────\n';

    for (var j = 0; j < report.warnings.length; j++) {
      var warning = report.warnings[j];
      body += '• ' + warning.campaign + '\n';
      body += '  ' + warning.message + '\n';
      body += '  Current: ' + warning.current + ' | Baseline: ' + warning.baseline + '\n\n';
    }
  }

  body += '\n---\nGenerated by Performance Troubleshoot Alert System';
  body += '\nRecommendation: Review campaigns in Google Ads UI for full diagnosis.';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Output: Troubleshooting Report Template

```markdown
# Performance Troubleshooting Report

## Issue Summary
- **Probleem gedetecteerd:** [Beschrijving]
- **Eerste signaal:** [Datum]
- **Impacted campaigns:** [Lijst]
- **Severity:** [Critical/Warning/Info]

## Symptomen
| Metric | Vorige Periode | Huidige Periode | Verandering |
|--------|----------------|-----------------|-------------|
| Impressies | [X] | [X] | [%] |
| Clicks | [X] | [X] | [%] |
| CTR | [X]% | [X]% | [%] |
| Conversies | [X] | [X] | [%] |
| CPA | €[X] | €[X] | [%] |
| ROAS | [X]% | [X]% | [%] |

## Root Cause Analyse

### Onderzochte Factoren
- [ ] Conversion tracking: [OK/Issue gevonden]
- [ ] Landing page: [OK/Issue gevonden]
- [ ] Ad copy/creatives: [OK/Issue gevonden]
- [ ] Bidding strategy: [OK/Issue gevonden]
- [ ] Budget: [OK/Issue gevonden]
- [ ] Competition: [Veranderd/Stabiel]
- [ ] Seasonality: [Ja/Nee]

### Geïdentificeerde Oorzaak
**[Beschrijf root cause]**

Evidence:
1. [Bewijs 1]
2. [Bewijs 2]
3. [Bewijs 3]

## Oplossingen

### Directe Acties (Nu)
1. [Actie 1]
2. [Actie 2]

### Korte Termijn (Deze Week)
1. [Actie 1]
2. [Actie 2]

### Lange Termijn (Preventie)
1. [Actie 1]
2. [Actie 2]

## Monitoring Plan
- Dagelijkse check: [Metrics om te monitoren]
- Wekelijkse review: [KPIs]
- Escalatie trigger: [Wanneer opnieuw escaleren]

## Lessons Learned
- [Learning 1]
- [Learning 2]
- [Preventieve maatregel voor toekomst]
```

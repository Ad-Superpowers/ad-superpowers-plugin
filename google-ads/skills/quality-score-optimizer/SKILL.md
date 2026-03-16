---
name: quality-score-optimizer
description: "Google Ads Quality Score optimalisatie gids. Gebruik voor: (1) Quality Score componenten analyse, (2) CTR verbetering strategieën, (3) Ad relevance optimalisatie, (4) Landing page experience verbetering, (5) QS diagnose en troubleshooting, (6) CPC reductie door QS. Triggers: quality score, qs, ctr, click through rate, ad relevance, landing page experience, average position, ad rank."
---

# Quality Score Optimizer

Complete gids voor het begrijpen en verbeteren van Google Ads Quality Score om lagere CPC's en betere ad posities te bereiken.

## Wat Is Quality Score?

```
QUALITY SCORE FUNDAMENTALS
══════════════════════════

Quality Score = Google's beoordeling van je ad kwaliteit
Score: 1-10 (10 = beste)

┌─────────────────────────────────────────────────────────────────┐
│  QUALITY SCORE COMPONENTEN (2025)                               │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  EXPECTED CTR                               ~39% weight   │ │
│  │  ├── Historische CTR van je ads                           │ │
│  │  ├── Voorspelde CTR voor dit keyword                      │ │
│  │  └── Vergeleken met competitors                           │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  AD RELEVANCE                               ~22% weight   │ │
│  │  ├── Match tussen keyword en ad copy                      │ │
│  │  ├── Semantische relevantie                               │ │
│  │  └── Intent alignment                                     │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  LANDING PAGE EXPERIENCE                    ~39% weight   │ │
│  │  ├── Relevantie van landing page                          │ │
│  │  ├── User experience (mobiel, snelheid)                   │ │
│  │  ├── Trust signals                                        │ │
│  │  └── Easy navigation                                      │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘

⚠️ BELANGRIJKE NUANCE:
Quality Score in UI is een HISTORISCHE metric.
Google gebruikt REAL-TIME quality signals in elke auction.
```

## Quality Score Impact

### QS en CPC Relatie

```
QUALITY SCORE IMPACT OP CPC
═══════════════════════════

FORMULE:
Ad Rank = Max CPC × Quality Score (simplified)
Actual CPC = (Ad Rank van advertiser onder je / Jouw QS) + €0.01

┌────────────────┬─────────────────┬──────────────────────────────┐
│ Quality Score  │ CPC Impact      │ Vergelijking (base QS=5)     │
├────────────────┼─────────────────┼──────────────────────────────┤
│ QS 10          │ -50% CPC        │ Betaal helft voor zelfde pos │
│ QS 8           │ -25% CPC        │ Significant voordeel         │
│ QS 7           │ -15% CPC        │ Klein voordeel               │
│ QS 5           │ Baseline        │ Gemiddeld                    │
│ QS 3           │ +35% CPC        │ Nadeel, inefficiënt          │
│ QS 1           │ +400% CPC       │ Niet concurrerend            │
└────────────────┴─────────────────┴──────────────────────────────┘

PRAKTISCH VOORBEELD:
────────────────────
Keyword: "hardloopschoenen kopen"
Market average CPC: €1.00

├── Met QS 10: Je betaalt ~€0.50
├── Met QS 7:  Je betaalt ~€0.85
├── Met QS 5:  Je betaalt ~€1.00 (baseline)
├── Met QS 3:  Je betaalt ~€1.35
└── Met QS 1:  Je betaalt ~€5.00 (vaak niet shown)

JAARLIJKSE IMPACT (€50k adspend):
─────────────────────────────────
QS 5 → QS 7: Bespaar ~€7,500/jaar
QS 5 → QS 8: Bespaar ~€12,500/jaar
QS 5 → QS 10: Bespaar ~€25,000/jaar
```

### QS Status Interpretation

```
COMPONENT STATUS UITLEG
═══════════════════════

ABOVE AVERAGE (Groen)
─────────────────────
✅ Je presteert beter dan meeste advertisers
✅ Geen directe actie nodig
✅ Focus op behouden

AVERAGE (Geel)
──────────────
⚠️ Je bent gemiddeld, ruimte voor verbetering
⚠️ Monitor en test verbeteringen
⚠️ Geen urgent probleem

BELOW AVERAGE (Rood)
────────────────────
❌ Je presteert slechter dan meeste advertisers
❌ Directe actie vereist
❌ Kost je geld en posities
```

## Expected CTR Optimalisatie

### CTR Verbetering Strategieën

```
CTR OPTIMALISATIE FRAMEWORK
═══════════════════════════

1. HEADLINE OPTIMALISATIE
─────────────────────────
HIGH-CTR HEADLINE FORMULAS:

□ Include Keyword (Direct Match)
├── Keyword: "hardloopschoenen dames"
├── Headline: "Hardloopschoenen Dames - Shop Nu"
└── Impact: +20-40% CTR

□ Numbers & Specifics
├── "50+ Modellen Hardloopschoenen"
├── "Vanaf €49,95"
├── "4.8★ Klantwaardering"
└── Impact: +15-30% CTR

□ Urgency/Scarcity
├── "Vandaag Nog Geleverd"
├── "Alleen Deze Week -30%"
├── "Laatste Stuks"
└── Impact: +10-25% CTR (gebruik spaarzaam)

□ Power Words
├── "Gratis Verzending"
├── "Officiële Dealer"
├── "100% Authentiek"
└── Impact: +10-20% CTR

2. DESCRIPTION OPTIMALISATIE
────────────────────────────
□ First 90 characters = meest zichtbaar
□ Include primary keyword
□ Clear CTA (Shop Nu, Bestel Direct)
□ Benefit-focused, niet feature-focused
□ Social proof (reviews, awards)

3. AD EXTENSIONS IMPACT
───────────────────────
Extensions verhogen visual footprint = hogere CTR

CTR IMPACT PER EXTENSION:
├── Sitelinks: +10-15%
├── Callouts: +5-10%
├── Structured Snippets: +5-8%
├── Call Extension: +5-10%
├── Location: +5-10%
└── Prijs Extension: +10-20%

ALLE EXTENSIONS GEBRUIKEN = Tot +30% CTR boost
```

### RSA Optimization voor CTR

```
RSA BEST PRACTICES VOOR CTR
═══════════════════════════

HEADLINES (15 max):
───────────────────
□ Headlines 1-3: Keyword-focused
├── "Hardloopschoenen Kopen"
├── "Premium Running Shoes"
└── "Officiële [Brand] Store"

□ Headlines 4-6: Benefit-focused
├── "Gratis Verzending Vanaf €50"
├── "Volgende Dag Geleverd"
└── "30 Dagen Retour"

□ Headlines 7-9: USP/Trust
├── "Al 15 Jaar Expert"
├── "4.8★ op Trustpilot"
└── "100% Authentiek"

□ Headlines 10-12: CTA-focused
├── "Shop Nu"
├── "Ontdek de Collectie"
└── "Bestel Vandaag Nog"

□ Headlines 13-15: Dynamic/Variatie
├── "Nieuw Binnen"
├── "[Season] Collectie"
└── Pinned headlines voor controle

DESCRIPTIONS (4 max):
─────────────────────
□ Description 1: Core value prop + keyword
□ Description 2: Social proof + benefits
□ Description 3: USPs + trust elements
□ Description 4: CTA + urgency

PIN STRATEGY:
─────────────
Position 1: Pin je beste CTR headline
Position 2: Pin keyword-focused headline
Position 3: Laat Google testen
```

## Ad Relevance Optimalisatie

### Keyword-Ad Alignment

```
AD RELEVANCE VERBETEREN
═══════════════════════

PROBLEEM: "Below Average" Ad Relevance

DIAGNOSE:
─────────
□ Bevat je ad copy het exact keyword?
□ Is de ad group te breed (te veel keywords)?
□ Match de intent van keyword en ad?

OPLOSSINGEN:
────────────

1. KEYWORD IN HEADLINES
───────────────────────
BAD: Ad Group "Running Shoes"
├── Keyword: hardloopschoenen kopen
└── Headline: "Sportschoenen Online" ❌

GOOD:
├── Keyword: hardloopschoenen kopen
└── Headline: "Hardloopschoenen Kopen - Shop Nu" ✅

2. KEYWORD INSERTION (Dynamic)
──────────────────────────────
Headline: {KeyWord:Hardloopschoenen} Online
├── Query "nike running shoes"
├── Shows: "Nike Running Shoes Online"
└── Fallback: "Hardloopschoenen Online"

⚠️ Pas op met:
├── Grammar issues
├── Competitor names
└── Rare long-tail queries

3. AD GROUP TIGHTENING
──────────────────────
BEFORE (Too broad):
Ad Group: Shoes
├── hardloopschoenen
├── wandelschoenen
├── sneakers
└── werkschoenen

AFTER (Focused):
Ad Group 1: Hardloopschoenen
├── hardloopschoenen
├── running shoes
└── hardloopschoenen kopen

Ad Group 2: Wandelschoenen
├── wandelschoenen
├── hiking shoes
└── wandelschoenen kopen

4. INTENT MATCHING
──────────────────
Keyword: "beste hardloopschoenen"
Intent: Comparison, research

BAD Ad Copy:
"Koop Nu Hardloopschoenen - Laagste Prijs"

GOOD Ad Copy:
"Top 10 Beste Hardloopschoenen 2025 - Vergelijk & Kies"
```

## Landing Page Experience

### Landing Page Optimalisatie Checklist

```
LANDING PAGE EXPERIENCE CHECKLIST
═════════════════════════════════

1. RELEVANCE (Content Match)
────────────────────────────
□ Keyword op landing page (H1, body text)
□ Ad promise = landing page delivery
□ Juiste product/service direct zichtbaar
□ Geen bait-and-switch

VOORBEELD:
├── Keyword: "nike air max heren"
├── Ad: "Nike Air Max Heren - Shop Nu"
├── LP BAD: Homepage met alle schoenen
└── LP GOOD: Gefilterde pagina Nike Air Max heren

2. PAGE SPEED (Core Web Vitals)
───────────────────────────────
□ LCP (Largest Contentful Paint): <2.5s
□ FID (First Input Delay): <100ms
□ CLS (Cumulative Layout Shift): <0.1

QUICK FIXES:
├── Compress images (WebP format)
├── Lazy loading voor below-fold images
├── Remove unused CSS/JS
├── Use CDN
└── Enable caching

3. MOBILE EXPERIENCE
────────────────────
□ Mobile-responsive design
□ Readable text (16px+ font)
□ Tap targets >48px
□ No horizontal scrolling
□ Fast mobile load (<3s)

4. TRUST & TRANSPARENCY
───────────────────────
□ Clear privacy policy (linked)
□ Secure connection (HTTPS)
□ Business info (adres, contact)
□ Reviews/testimonials visible
□ Return policy clear
□ Payment security badges

5. NAVIGATION & UX
──────────────────
□ Clear CTA above the fold
□ Easy navigation back/forward
□ No intrusive popups (especially mobile)
□ Form fields minimized
□ Guest checkout optie (e-commerce)
```

### Landing Page Speed Optimalisatie

```
PAGE SPEED VERBETEREN
═════════════════════

TESTING TOOLS:
──────────────
□ Google PageSpeed Insights
  https://pagespeed.web.dev/

□ Google Search Console
  Core Web Vitals report

□ GTmetrix
  https://gtmetrix.com/

□ WebPageTest
  https://webpagetest.org/

COMMON ISSUES & FIXES:
──────────────────────

ISSUE: Slow LCP (Largest Contentful Paint)
CAUSES:
├── Large hero image
├── Slow server response
└── Render-blocking resources
FIXES:
├── Preload hero image
├── Use CDN + caching
├── Defer non-critical JS
└── Inline critical CSS

ISSUE: High CLS (Layout Shift)
CAUSES:
├── Images without dimensions
├── Ads loading late
├── Dynamic content injection
FIXES:
├── Set width/height on images
├── Reserve space for ads
├── Use transform for animations
└── Skeleton loaders

ISSUE: Poor FID (First Input Delay)
CAUSES:
├── Heavy JavaScript execution
├── Third-party scripts
└── Large DOM
FIXES:
├── Code splitting
├── Defer third-party scripts
├── Reduce DOM size
└── Web workers for heavy tasks

QUICK WINS:
───────────
1. Compress images: 30-50% size reduction
2. Enable text compression (gzip/brotli)
3. Use browser caching
4. Remove unused code
5. Optimize fonts (subset, preload)
```

## Quality Score Diagnose

### QS Troubleshooting Workflow

```
QS DIAGNOSE FRAMEWORK
═════════════════════

STAP 1: IDENTIFICEER PROBLEEM KEYWORDS
──────────────────────────────────────
1. Keywords → Modify Columns
2. Add: Quality Score, Exp. CTR, Ad Rel., LP Exp.
3. Sort by QS (low to high)
4. Focus op keywords met spend en QS <5

STAP 2: ANALYSEER COMPONENTEN
─────────────────────────────
Per keyword, check welke component(en) "Below Average":

┌────────────────────┬───────────────────────────────────────┐
│ Below Average      │ Primaire Focus                        │
├────────────────────┼───────────────────────────────────────┤
│ Expected CTR       │ → Ad copy optimization                │
│                    │ → Extensions                          │
│                    │ → Ad testing                          │
├────────────────────┼───────────────────────────────────────┤
│ Ad Relevance       │ → Keyword-ad alignment                │
│                    │ → Ad group restructuring              │
│                    │ → Keyword insertion                   │
├────────────────────┼───────────────────────────────────────┤
│ Landing Page Exp.  │ → Page speed                          │
│                    │ → Content relevance                   │
│                    │ → Mobile experience                   │
├────────────────────┼───────────────────────────────────────┤
│ Multiple Below     │ → Major restructuring needed          │
│                    │ → Consider pausing keyword            │
└────────────────────┴───────────────────────────────────────┘

STAP 3: PRIORITEER ACTIES
─────────────────────────
Priority Matrix:

HIGH PRIORITY (Fix First):
├── High spend + Low QS
├── Core keywords met Below Average
└── Brand keywords met QS issues

MEDIUM PRIORITY:
├── Medium spend + Average components
├── Non-core keywords
└── Testing candidates

LOW PRIORITY:
├── Low spend keywords
├── Long-tail met weinig impressions
└── Already Average/Above Average
```

### QS Benchmarks per Industry

```
QUALITY SCORE BENCHMARKS
════════════════════════

GEMIDDELDE QS PER INDUSTRY:
───────────────────────────
├── E-commerce (Retail): 6-7
├── B2B Services: 5-6
├── Legal: 4-5
├── Finance/Insurance: 4-6
├── Healthcare: 5-6
├── Real Estate: 5-6
├── Travel: 5-7
└── Education: 6-7

DOELSTELLINGEN (Realistic):
───────────────────────────
├── Brand Keywords: QS 8-10
├── Core Non-brand: QS 6-8
├── Competitive Keywords: QS 5-7
├── Long-tail Keywords: QS 5-7
└── Account Average: QS 6+

⚠️ LET OP:
├── QS 10 op alle keywords = niet realistisch
├── Focus op keywords die er toe doen (spend)
├── QS is relative (jij vs competitors)
└── QS verbeteringen kosten tijd (weeks)
```

## Google Ads Script: Quality Score Monitor

```javascript
/**
 * Quality Score Monitor & Alert Script
 *
 * Features:
 * - Monitort QS changes over tijd
 * - Alert bij significant QS drops
 * - Weekly QS report
 * - Identificeert improvement opportunities
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Schedule: Dagelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Thresholds
  MIN_IMPRESSIONS: 100,           // Minimum impressions voor analyse
  QS_DROP_ALERT: 2,               // Alert bij QS drop van X punten
  LOW_QS_THRESHOLD: 5,            // Keywords met QS onder dit = priority

  // Spreadsheet voor historische tracking (optioneel)
  SPREADSHEET_URL: '',            // Laat leeg om over te slaan

  // Report frequency
  SEND_WEEKLY_REPORT: true,
  REPORT_DAY: 1                   // 1 = Monday
};

function main() {
  var today = new Date();
  var dayOfWeek = today.getDay();

  var report = analyzeQualityScores();

  // Daily alerts voor significant drops
  if (report.alerts.length > 0) {
    sendAlertEmail(report.alerts);
  }

  // Weekly report
  if (CONFIG.SEND_WEEKLY_REPORT && dayOfWeek === CONFIG.REPORT_DAY) {
    sendWeeklyReport(report);
  }

  // Log to spreadsheet
  if (CONFIG.SPREADSHEET_URL) {
    logToSpreadsheet(report);
  }
}

function analyzeQualityScores() {
  var report = {
    totalKeywords: 0,
    averageQS: 0,
    lowQSKeywords: [],
    belowAverageComponents: {
      expectedCtr: [],
      adRelevance: [],
      landingPageExperience: []
    },
    alerts: [],
    qsDistribution: {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
  };

  var totalQS = 0;
  var keywordsWithQS = 0;

  var keywords = AdsApp.keywords()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignStatus = ENABLED')
    .withCondition('AdGroupStatus = ENABLED')
    .withCondition('Impressions > ' + CONFIG.MIN_IMPRESSIONS)
    .forDateRange('LAST_30_DAYS')
    .get();

  while (keywords.hasNext()) {
    var keyword = keywords.next();
    var qs = keyword.getQualityScore();

    if (qs === null) continue;

    report.totalKeywords++;
    keywordsWithQS++;
    totalQS += qs;

    // QS Distribution
    report.qsDistribution[qs]++;

    // Low QS keywords
    if (qs < CONFIG.LOW_QS_THRESHOLD) {
      report.lowQSKeywords.push({
        keyword: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        adGroup: keyword.getAdGroup().getName(),
        qs: qs,
        expectedCtr: getStatusText(keyword.getExpectedCtr()),
        adRelevance: getStatusText(keyword.getAdRelevance()),
        landingPageExperience: getStatusText(keyword.getLandingPageExperience())
      });
    }

    // Below Average Components
    if (keyword.getExpectedCtr() === 'BELOW_AVERAGE') {
      report.belowAverageComponents.expectedCtr.push({
        keyword: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        qs: qs
      });
    }

    if (keyword.getAdRelevance() === 'BELOW_AVERAGE') {
      report.belowAverageComponents.adRelevance.push({
        keyword: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        qs: qs
      });
    }

    if (keyword.getLandingPageExperience() === 'BELOW_AVERAGE') {
      report.belowAverageComponents.landingPageExperience.push({
        keyword: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        qs: qs
      });
    }
  }

  report.averageQS = keywordsWithQS > 0 ?
    (totalQS / keywordsWithQS).toFixed(1) : 0;

  return report;
}

function getStatusText(status) {
  switch(status) {
    case 'ABOVE_AVERAGE': return 'Above Avg';
    case 'AVERAGE': return 'Average';
    case 'BELOW_AVERAGE': return 'Below Avg';
    default: return 'Unknown';
  }
}

function sendAlertEmail(alerts) {
  var subject = '⚠️ Quality Score Alert - ' + AdsApp.currentAccount().getName();
  var body = 'Quality Score Alerts\n';
  body += '====================\n\n';

  for (var i = 0; i < alerts.length; i++) {
    body += alerts[i] + '\n';
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}

function sendWeeklyReport(report) {
  var subject = 'Weekly Quality Score Report - ' + AdsApp.currentAccount().getName();
  var body = 'Quality Score Weekly Report\n';
  body += '===========================\n\n';

  body += 'SUMMARY:\n';
  body += '────────\n';
  body += 'Total Keywords Analyzed: ' + report.totalKeywords + '\n';
  body += 'Average Quality Score: ' + report.averageQS + '\n';
  body += 'Keywords with QS < ' + CONFIG.LOW_QS_THRESHOLD + ': ' +
          report.lowQSKeywords.length + '\n\n';

  body += 'QS DISTRIBUTION:\n';
  body += '────────────────\n';
  for (var qs = 10; qs >= 1; qs--) {
    var count = report.qsDistribution[qs];
    var bar = '';
    for (var j = 0; j < Math.min(count, 20); j++) bar += '█';
    body += 'QS ' + (qs < 10 ? ' ' : '') + qs + ': ' + bar + ' (' + count + ')\n';
  }
  body += '\n';

  body += 'BELOW AVERAGE COMPONENTS:\n';
  body += '─────────────────────────\n';
  body += 'Expected CTR: ' + report.belowAverageComponents.expectedCtr.length + ' keywords\n';
  body += 'Ad Relevance: ' + report.belowAverageComponents.adRelevance.length + ' keywords\n';
  body += 'Landing Page Exp: ' +
          report.belowAverageComponents.landingPageExperience.length + ' keywords\n\n';

  if (report.lowQSKeywords.length > 0) {
    body += 'TOP 10 LOW QS KEYWORDS:\n';
    body += '───────────────────────\n';
    var sorted = report.lowQSKeywords.sort(function(a, b) { return a.qs - b.qs; });
    for (var k = 0; k < Math.min(sorted.length, 10); k++) {
      var kw = sorted[k];
      body += '• ' + kw.keyword + ' (QS: ' + kw.qs + ')\n';
      body += '  Campaign: ' + kw.campaign + '\n';
      body += '  CTR: ' + kw.expectedCtr + ' | ';
      body += 'Ad Rel: ' + kw.adRelevance + ' | ';
      body += 'LP: ' + kw.landingPageExperience + '\n\n';
    }
  }

  body += '\n---\nGenerated by Quality Score Monitor Script';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
  Logger.log('Weekly report sent');
}

function logToSpreadsheet(report) {
  if (!CONFIG.SPREADSHEET_URL) return;

  try {
    var ss = SpreadsheetApp.openByUrl(CONFIG.SPREADSHEET_URL);
    var sheet = ss.getSheetByName('QS_History') ||
                ss.insertSheet('QS_History');

    var today = new Date();
    var row = [
      today,
      report.totalKeywords,
      report.averageQS,
      report.lowQSKeywords.length,
      report.belowAverageComponents.expectedCtr.length,
      report.belowAverageComponents.adRelevance.length,
      report.belowAverageComponents.landingPageExperience.length
    ];

    sheet.appendRow(row);
    Logger.log('Logged to spreadsheet');
  } catch (e) {
    Logger.log('Spreadsheet error: ' + e);
  }
}
```

## Output: Quality Score Improvement Plan

```markdown
# Quality Score Improvement Plan

## Account Status
- **Account:** [Account Name]
- **Date:** [Date]
- **Current Avg QS:** [X.X]
- **Target Avg QS:** [X.X]

## Priority Keywords Analysis

### Critical (QS 1-3)
| Keyword | Campaign | QS | Exp CTR | Ad Rel | LP Exp | Action |
|---------|----------|----|---------| -------|--------|--------|
| [kw]    | [camp]   | 2  | Below   | Below  | Avg    | Restructure |

### High Priority (QS 4-5)
| Keyword | Campaign | QS | Issue | Action |
|---------|----------|----|-------|--------|
| [kw]    | [camp]   | 4  | LP Exp Below | Speed optimization |

## Improvement Actions

### Expected CTR Improvements
- [ ] Rewrite headlines with keywords
- [ ] Add all relevant extensions
- [ ] Test new RSA variations
- [ ] Target CTR improvement: +[X]%

### Ad Relevance Improvements
- [ ] Restructure ad groups (max 15 kw/group)
- [ ] Add keyword insertion where appropriate
- [ ] Match keyword intent with ad copy
- [ ] Create dedicated ads per theme

### Landing Page Improvements
- [ ] Page speed optimization (target: <2.5s LCP)
- [ ] Mobile experience audit
- [ ] Add trust signals
- [ ] Ensure keyword presence on page

## Timeline
- Week 1-2: Ad copy & extension updates
- Week 3-4: Ad group restructuring
- Week 5-6: Landing page optimizations
- Week 7-8: Review & iterate

## Success Metrics
- Current Avg QS: [X.X] → Target: [X.X]
- Current CPC: €[X.XX] → Expected: €[X.XX] (-X%)
- Keywords Below Avg: [X] → Target: [X]
```

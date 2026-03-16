---
name: audience-strategy-planner
description: "Google Ads audience strategie en targeting planner. Gebruik voor: (1) Customer Match implementatie, (2) In-market en affinity audience selectie, (3) Similar/Lookalike audience setup, (4) Audience layering strategieën, (5) First-party data strategie, (6) B2B audience targeting. Triggers: audience, customer match, in-market, affinity, similar audiences, lookalike, first party data, targeting, segments, b2b targeting."
---

# Audience Strategy Planner

Complete gids voor het opzetten van een effectieve Google Ads audience strategie met first-party data, Google audiences en layering strategieën voor lead generation.

## Quick Decision Guide

```
WELKE AUDIENCE STRATEGIE PAST BIJ JOU?
│
├─► NIEUWE ACCOUNT / GEEN DATA
│   └─► START MET GOOGLE AUDIENCES
│       ├── In-market audiences
│       ├── Affinity audiences
│       └── Build first-party data over tijd
│
├─► BESTAANDE KLANTDATA
│   └─► CUSTOMER MATCH + SIMILAR
│       ├── Upload klantlijsten
│       ├── Maak similar audiences
│       └── Exclude existing customers (optioneel)
│
├─► WEBSITE MET TRAFFIC
│   └─► REMARKETING + GA4 AUDIENCES
│       ├── Website visitors
│       ├── Behavioral segments (GA4)
│       └── Funnel-based audiences
│
├─► B2B LEAD GENERATION
│   └─► LAYERED TARGETING
│       ├── In-market + Affinity combination
│       ├── Job function targeting
│       └── Company size/industry (via CRM match)
│
└─► FULL FUNNEL
    └─► COMBINED STRATEGY
        ├── Top: Affinity + Similar audiences
        ├── Middle: In-market + Website visitors
        └── Bottom: Converters + Customer Match
```

## Audience Types Overview

### Google Ads Audience Types

```
GOOGLE ADS AUDIENCE TYPES (2025)
════════════════════════════════

┌─────────────────────────────────────────────────────────────────┐
│ TYPE              │ BESCHRIJVING           │ USE CASE           │
├───────────────────┼────────────────────────┼────────────────────┤
│ FIRST-PARTY DATA                                                │
├───────────────────┼────────────────────────┼────────────────────┤
│ Customer Match    │ Jouw klantlijsten      │ Upsell, loyalty,   │
│                   │ (email, phone, address)│ exclusion          │
├───────────────────┼────────────────────────┼────────────────────┤
│ Website Visitors  │ Remarketing lists      │ Re-engage,         │
│                   │ (RLSA)                 │ cart recovery      │
├───────────────────┼────────────────────────┼────────────────────┤
│ App Users         │ Mobile app activity    │ App engagement     │
├───────────────────┼────────────────────────┼────────────────────┤
│ YouTube Users     │ Video interactions     │ Video remarketing  │
├───────────────────┼────────────────────────┼────────────────────┤
│ GA4 Audiences     │ Behavioral segments    │ Complex targeting  │
├───────────────────┼────────────────────────┼────────────────────┤
│ GOOGLE-PROVIDED DATA                                            │
├───────────────────┼────────────────────────┼────────────────────┤
│ In-market         │ Actively researching   │ High-intent        │
│                   │ products/services      │ prospecting        │
├───────────────────┼────────────────────────┼────────────────────┤
│ Affinity          │ Long-term interests    │ Brand awareness,   │
│                   │ & lifestyle            │ broad reach        │
├───────────────────┼────────────────────────┼────────────────────┤
│ Life Events       │ Major life changes     │ Timely targeting   │
│                   │ (moving, wedding)      │                    │
├───────────────────┼────────────────────────┼────────────────────┤
│ Detailed Demo     │ Age, gender, income,   │ Demographic        │
│                   │ parental status        │ targeting          │
├───────────────────┼────────────────────────┼────────────────────┤
│ Similar Audiences │ Lookalikes of your     │ Scale acquisition  │
│                   │ first-party lists      │ (limited in EU)    │
├───────────────────┼────────────────────────┼────────────────────┤
│ Custom Segments   │ Keywords, URLs,        │ Custom intent      │
│                   │ app interests          │ targeting          │
└───────────────────┴────────────────────────┴────────────────────┘

⚠️ SIMILAR AUDIENCES (EU):
├── Beperkt beschikbaar door privacy regelgeving
├── Vervangen door: Optimized Targeting, Smart Bidding signals
└── Check beschikbaarheid in jouw account
```

### Audience Sizing Guidelines

```
AUDIENCE SIZING GUIDELINES
══════════════════════════

MINIMUM SIZES PER NETWORK:
──────────────────────────
┌────────────────────┬───────────────────────────────────────────┐
│ Network            │ Minimum Size                              │
├────────────────────┼───────────────────────────────────────────┤
│ Search (RLSA)      │ 1,000 users                              │
│ Display            │ 100 users                                 │
│ YouTube            │ 1,000 users                              │
│ Gmail              │ 100 users                                 │
│ Customer Match     │ 1,000 matched users                      │
│ Similar Audiences  │ 500+ in source list                      │
└────────────────────┴───────────────────────────────────────────┘

OPTIMAL SIZES:
──────────────
□ Too small (<1,000): Limited reach, volatile performance
□ Optimal (10,000-100,000): Good reach, stable data
□ Very large (>1M): Good for broad campaigns, less specific

AUDIENCE MEMBERSHIP DURATION:
─────────────────────────────
Default settings en aanbevelingen:

┌────────────────────────────────────────────────────────────────┐
│ Audience Type      │ Default │ Aanbevolen (Lead Gen)          │
├────────────────────┼─────────┼────────────────────────────────┤
│ All Visitors       │ 30 days │ 30-90 days                     │
│ Cart Abandoners    │ 30 days │ 7-14 days (urgency)            │
│ Form Started       │ 30 days │ 14-30 days                     │
│ Converters         │ 540 days│ 180-365 days (voor exclusion)  │
│ High-value Custom. │ 540 days│ 365 days (upsell)              │
└────────────────────┴─────────┴────────────────────────────────┘
```

## Customer Match Setup

### Customer Match Implementatie

```
CUSTOMER MATCH SETUP GUIDE
══════════════════════════

VEREISTEN:
──────────
□ Google Ads account met goede history
□ $50,000+ lifetime spend (voor sommige features)
□ 90+ dagen account history
□ Good policy compliance record

DATA TYPES DIE JE KUNT UPLOADEN:
────────────────────────────────
□ Email addresses
□ Phone numbers (met country code)
□ Mailing addresses (first name, last name, country, zip)
□ Mobile device IDs

MATCH RATES:
────────────
┌────────────────────────────────────────────────────────────────┐
│ Data Combination        │ Expected Match Rate                 │
├─────────────────────────┼─────────────────────────────────────┤
│ Email only              │ 30-50%                              │
│ Email + Phone           │ 45-65%                              │
│ Email + Phone + Name    │ 55-75%                              │
│ All fields              │ 60-80%                              │
└─────────────────────────┴─────────────────────────────────────┘

STAP-VOOR-STAP SETUP:
─────────────────────

STAP 1: DATA PREPARATION
────────────────────────
Formatting requirements:

Email:
├── Lowercase
├── Remove whitespace
├── Format: john.doe@gmail.com

Phone:
├── Include country code
├── Format: +31612345678
├── Remove spaces, dashes, parentheses

Name:
├── Separate first/last name
├── Lowercase
├── Remove titles (Mr., Dr., etc.)

Address:
├── Country: ISO 2-letter code (NL, BE, DE)
├── Zip code: without spaces

STAP 2: CREATE CUSTOMER LIST
────────────────────────────
1. Tools → Audience Manager → Segments
2. "+ Segment" → "Customer list"
3. Name: "[Purpose]_CustomerMatch_[Date]"
   Bijv: "HighValue_Customers_2025Q1"

STAP 3: UPLOAD DATA
───────────────────
Option A: Manual upload (CSV)
├── Download template
├── Fill in data
├── Upload file

Option B: API upload
├── Use Google Ads API
├── Automate syncs van CRM
└── Real-time updates

STAP 4: SET MEMBERSHIP DURATION
───────────────────────────────
□ Default: Unlimited
□ Aanbevolen: 365-540 days
□ Match met je sales cycle

STAP 5: VERIFY MATCH RATE
─────────────────────────
□ Processing takes 24-48 hours
□ Check list size after processing
□ Target: >40% match rate
```

### Customer Match Strategieën

```
CUSTOMER MATCH USE CASES
════════════════════════

1. UPSELL/CROSS-SELL
────────────────────
Doel: Bestaande klanten nieuwe producten tonen

Segment: Active customers, last purchase >30 days
Targeting: Customer match (observation of targeting)
Messaging: New products, complementary services
Bid adjustment: +20-50%

2. RETENTION / WIN-BACK
───────────────────────
Doel: Inactieve klanten reactiveren

Segment: Churned customers (no purchase 90+ days)
Targeting: Customer match (targeting)
Messaging: "We miss you", special offers
Bid adjustment: +10-30%

3. EXCLUSION (ACQUISITION FOCUS)
────────────────────────────────
Doel: Alleen nieuwe klanten targeten

Segment: All customers
Targeting: Customer match → Exclude
Use: Prospecting campaigns only
Result: No wasted spend on existing customers

4. SIMILAR AUDIENCES (Scale)
────────────────────────────
Doel: Nieuwe klanten vinden die lijken op beste klanten

Base list: High-value customers
Create: Similar audience automatically
Targeting: Similar to high-value
Use: Prospecting campaigns

⚠️ EU: Similar audiences hebben beperkte beschikbaarheid

5. LOOKALIKE VIA PERFORMANCE MAX
────────────────────────────────
Doel: Scale met behulp van Customer Match signals

Setup:
├── Upload customer list als "Audience signal"
├── PMax gebruikt dit voor targeting optimization
└── Niet direct als targeting, maar als signal

SEGMENTATIE VOORBEELDEN:
────────────────────────
□ By purchase value: High (€500+), Medium (€100-500), Low (<€100)
□ By recency: Active (30d), Recent (90d), Lapsed (180d), Churned (365d+)
□ By product: Category A buyers, Category B buyers
□ By LTV: Top 20% customers, Next 30%, Bottom 50%
```

## In-Market & Affinity Audiences

### In-Market Audiences

```
IN-MARKET AUDIENCES STRATEGIE
═════════════════════════════

WAT ZIJN IN-MARKET AUDIENCES?
─────────────────────────────
Users die actief research doen en purchase intent tonen.
Google bepaalt dit op basis van:
├── Search queries
├── Websites bezocht
├── Content consumed
└── Recente gedrag

IN-MARKET CATEGORIES (Lead Gen relevant):
─────────────────────────────────────────

B2B SERVICES:
├── Business Services
│   ├── Accounting & Finance Services
│   ├── Advertising & Marketing Services
│   ├── Business Technology
│   ├── Corporate Event Planning
│   └── Office Supplies
├── Business Technology
│   ├── Enterprise Software
│   ├── CRM Software
│   ├── Cloud Storage
│   └── Cybersecurity
└── Financial Services
    ├── Business Loans
    ├── Insurance
    └── Merchant Services

B2C SERVICES:
├── Home Services
│   ├── Home Improvement
│   ├── Cleaning Services
│   ├── Moving & Relocation
│   └── Pest Control
├── Legal Services
├── Financial Services
│   ├── Personal Loans
│   ├── Insurance
│   └── Investment Services
└── Education
    ├── Post-Secondary Education
    └── Professional Training

HOE TE GEBRUIKEN:
─────────────────
SEARCH CAMPAIGNS:
├── Add als "Observation" eerst
├── Analyseer performance na 2-4 weken
├── Best performers → Bid adjustment +10-30%
├── Poor performers → Consider exclusion

DISPLAY/YOUTUBE CAMPAIGNS:
├── Kan als primary targeting
├── Combineer met andere audiences
└── Smaller scope = better quality
```

### Affinity Audiences

```
AFFINITY AUDIENCES STRATEGIE
════════════════════════════

WAT ZIJN AFFINITY AUDIENCES?
────────────────────────────
Users met langdurige interesses en lifestyle kenmerken.
Minder immediate intent, maar relevant voor branding.

AFFINITY CATEGORIES (Lead Gen relevant):
────────────────────────────────────────

BUSINESS PROFESSIONALS:
├── Business Professionals
├── Small Business Owners
├── Corporate Executives
└── IT Professionals

TECHNOPHILES:
├── Tech Enthusiasts
├── Social Media Enthusiasts
└── Mobile Enthusiasts

LIFESTYLE:
├── Green Living Enthusiasts
├── Luxury Shoppers
├── Value Shoppers
└── Home Decor Enthusiasts

HOE TE GEBRUIKEN:
─────────────────
□ Affinity = awareness fase
□ Combineer met In-market voor qualification
□ Use in Display/YouTube, minder relevant voor Search

CUSTOM AFFINITY (nu Custom Segments):
─────────────────────────────────────
Maak eigen affinity-style audiences:

1. Tools → Audience Manager → Custom Segments
2. "+ Custom segment"
3. Kies: "People with any of these interests or purchase intentions"
4. Voeg toe:
   ├── Keywords die je audience zou zoeken
   ├── URLs die ze zouden bezoeken
   └── Apps die ze zouden gebruiken
```

### Audience Layering

```
AUDIENCE LAYERING STRATEGIEËN
═════════════════════════════

WAT IS AUDIENCE LAYERING?
─────────────────────────
Meerdere audience types combineren om:
├── Precision te verhogen
├── Waste te verminderen
└── Relevantie te maximaliseren

LAYERING METHODES:
──────────────────

1. AND LOGIC (Narrowing)
────────────────────────
"Must match ALL conditions"

Voorbeeld:
├── In-market: Business Services
├── AND Affinity: Business Professionals
├── AND Demographics: Age 25-54

Result: Smaller, more qualified audience

2. OR LOGIC (Expanding)
───────────────────────
"Match ANY condition"

Voorbeeld:
├── In-market: CRM Software
├── OR In-market: Cloud Storage
├── OR In-market: Cybersecurity

Result: Larger audience, related interests

3. EXCLUSION LOGIC
──────────────────
"Match A but NOT B"

Voorbeeld:
├── Target: All website visitors
├── Exclude: Converters
├── Exclude: Customer Match list

Result: Prospecting only, no existing customers

LAYERING VOOR B2B LEAD GEN:
───────────────────────────
Campaign: B2B Software Leads

Layer 1 (Intent):
├── In-market: Enterprise Software
├── In-market: Cloud Services

Layer 2 (Decision maker):
├── Affinity: Business Professionals
├── Detailed Demo: Household income Top 10%

Layer 3 (Exclusion):
├── Exclude: Current customers
├── Exclude: Converters (last 90 days)

LAYERING VOOR LOCAL SERVICES:
─────────────────────────────
Campaign: Home Services (Renovatie)

Layer 1 (Intent):
├── In-market: Home Improvement
├── In-market: Kitchen & Bath Remodeling

Layer 2 (Life stage):
├── Life Events: Recently moved
├── Detailed Demo: Homeowners

Layer 3 (Geography):
├── Location targeting (radius)
└── Exclude: Renters (if possible via demo)
```

## Custom Segments

### Custom Segments Setup

```
CUSTOM SEGMENTS (Voorheen Custom Intent)
════════════════════════════════════════

WANNEER GEBRUIKEN:
──────────────────
□ Geen passende In-market/Affinity audience
□ Niche markt of product
□ Competitor targeting nodig
□ Zeer specifieke intent

CUSTOM SEGMENT TYPES:
─────────────────────

1. CUSTOM INTENT (Search-based)
───────────────────────────────
"People who searched for these terms"

Setup:
1. Audience Manager → Custom Segments → +
2. Name: "CS_[Purpose]_[Date]"
3. Type: "People who searched for any of these terms"
4. Add keywords:
   ├── Transactional queries
   ├── Problem-based queries
   ├── Competitor + alternative queries
   └── 10-50 keywords recommended

Voorbeeld (B2B CRM):
├── "beste crm software"
├── "crm voor mkb"
├── "salesforce alternatief"
├── "hubspot vs pipedrive"
└── "klantenbeheer software"

2. CUSTOM AFFINITY (Interest-based)
───────────────────────────────────
"People who have interests in..."

Setup:
1. Type: "People with any of these interests or purchase intentions"
2. Add:
   ├── Interest keywords
   ├── URLs of relevant websites
   └── Apps they might use

Voorbeeld (Marketing Professionals):
├── Keywords: digital marketing, content strategy
├── URLs: marketingweek.com, hubspot.com/blog
└── Apps: Hootsuite, Buffer, Sprout Social

3. COMPETITOR TARGETING
───────────────────────
Target users die competitor sites bezoeken

Setup:
1. Type: "People who browse types of websites"
2. Add competitor URLs:
   ├── competitor1.com
   ├── competitor2.com
   └── competitor3.com

⚠️ Dit target people WHO BROWSE SIMILAR SITES
   Niet exact die sites - Google's interpretation

BEST PRACTICES:
───────────────
□ Test segments met "Observation" eerst
□ Start breed, narrow down over tijd
□ Combineer met andere targeting
□ Min 10 keywords/URLs voor goede reach
□ Monitor weekly voor performance
```

## Audience Strategy voor Lead Gen

### Full-Funnel Audience Framework

```
FULL-FUNNEL AUDIENCE STRATEGY
═════════════════════════════

FUNNEL STAGE: AWARENESS (Top)
─────────────────────────────
Goal: Brand bekendheid, reach
Audiences:
├── Affinity audiences (breed)
├── Similar to customers
├── Custom segments (interest-based)
└── Life events

Campaigns: Display, YouTube, Discovery
Bidding: CPM, Maximize reach
Messaging: Brand story, pain points
Budget: 15-25% van total

FUNNEL STAGE: CONSIDERATION (Middle)
────────────────────────────────────
Goal: Engagement, interest
Audiences:
├── In-market audiences
├── Website visitors (all)
├── Video viewers (YouTube)
├── Custom intent segments
└── GA4 engaged users

Campaigns: Display, YouTube, Search (broad)
Bidding: Target CPA, Maximize conversions
Messaging: Benefits, social proof, education
Budget: 30-40% van total

FUNNEL STAGE: DECISION (Bottom)
───────────────────────────────
Goal: Conversie, leads
Audiences:
├── RLSA (high-intent pages)
├── Cart/form abandoners
├── Return visitors (3+ visits)
├── Customer Match (upsell)
└── GA4 predictive (likely to convert)

Campaigns: Search, Remarketing Display
Bidding: Target CPA, Maximize conversions
Messaging: CTA, urgency, offer
Budget: 35-45% van total

FUNNEL STAGE: LOYALTY (Post-conversion)
───────────────────────────────────────
Goal: Retention, referral
Audiences:
├── Customer Match (existing)
├── Converters (recent)
├── App users
└── Email subscribers

Campaigns: Display remarketing, YouTube
Bidding: Target ROAS
Messaging: Cross-sell, loyalty, referral
Budget: 5-10% van total

┌─────────────────────────────────────────────────────────────────┐
│                     FULL-FUNNEL VISUAL                          │
│                                                                  │
│     AWARENESS        Affinity, Similar, Life Events            │
│     ▼▼▼▼▼▼▼▼▼       Wide reach, brand building                 │
│                                                                  │
│     CONSIDERATION    In-market, Custom Intent                   │
│     ▼▼▼▼▼▼          Research phase, education                  │
│                                                                  │
│     DECISION         RLSA, Abandoners, High-intent             │
│     ▼▼▼             Convert intent to action                   │
│                                                                  │
│     LOYALTY          Customer Match, Converters                 │
│     ▼                Retain and grow value                      │
└─────────────────────────────────────────────────────────────────┘
```

### B2B Audience Strategy

```
B2B AUDIENCE TARGETING STRATEGY
═══════════════════════════════

CHALLENGE: B2B targeting is moeilijker
────────────────────────────────────
□ Geen "job title" targeting in Google Ads
□ Geen "company size" targeting
□ Langere sales cycles
□ Multiple decision makers

OPLOSSINGEN:
────────────

1. IN-MARKET + AFFINITY LAYERING
────────────────────────────────
Layer 1: In-market for B2B category
├── Business Services
├── Enterprise Software
└── Industry-specific

Layer 2: Affinity for decision makers
├── Business Professionals
├── Corporate Executives
└── IT Professionals

Layer 3: Demographics
├── Age: 25-54 (exclude juniors)
├── Household income: Top 30%
└── Parental: Exclude if needed

2. CUSTOMER MATCH (FIRMOGRAPHIC)
────────────────────────────────
Upload gesegmenteerde lijsten:

List 1: Enterprise accounts (1000+ employees)
List 2: Mid-market accounts (100-999 employees)
List 3: SMB accounts (<100 employees)

Create similar audiences van beste segment
Target/exclude gebaseerd op ideal customer

3. CUSTOM SEGMENTS (COMPETITOR/TOOL)
────────────────────────────────────
Target op basis van tool/competitor research:

Keywords:
├── "[competitor] pricing"
├── "[competitor] alternative"
├── "[competitor] vs [competitor]"
└── "[category] comparison"

URLs:
├── g2.com (B2B software reviews)
├── capterra.com
├── trustradius.com
└── Competitor websites

4. LINKEDIN → GOOGLE ADS WORKFLOW
─────────────────────────────────
LinkedIn biedt betere B2B targeting.
Maak customer match lijst van LinkedIn leads.

Flow:
1. LinkedIn campaign → Generate leads
2. Export leads (email, company)
3. Upload naar Google Ads Customer Match
4. Target similar audiences
5. Remarketing via Google Display
```

## Google Ads Script: Audience Performance Analyzer

```javascript
/**
 * Audience Performance Analyzer
 *
 * Analyseert performance van alle audiences
 * Genereert aanbevelingen voor bid adjustments
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Schedule: Wekelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Date range
  DATE_RANGE: 'LAST_30_DAYS',

  // Thresholds
  MIN_IMPRESSIONS: 1000,
  MIN_CLICKS: 50,
  PERFORMANCE_GOOD: 1.2,   // 20% beter dan campaign avg
  PERFORMANCE_POOR: 0.8,   // 20% slechter dan campaign avg

  // Bid adjustment recommendations
  GOOD_BID_ADJUSTMENT: 20,   // +20%
  POOR_BID_ADJUSTMENT: -20   // -20%
};

function main() {
  var report = {
    audiences: [],
    recommendations: [],
    topPerformers: [],
    underperformers: []
  };

  // Get campaign performance as baseline
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .forDateRange(CONFIG.DATE_RANGE)
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var campaignStats = campaign.getStatsFor(CONFIG.DATE_RANGE);
    var campaignCPA = calculateCPA(campaignStats);
    var campaignConvRate = calculateConvRate(campaignStats);

    // Get audience targeting
    var audienceTargeting = campaign.targeting().audiences().get();

    while (audienceTargeting.hasNext()) {
      var audience = audienceTargeting.next();
      var stats = audience.getStatsFor(CONFIG.DATE_RANGE);

      if (stats.getImpressions() < CONFIG.MIN_IMPRESSIONS) continue;

      var audienceCPA = calculateCPA(stats);
      var audienceConvRate = calculateConvRate(stats);

      var performance = campaignCPA > 0 ?
        campaignCPA / (audienceCPA || 9999) : 0;

      var audienceData = {
        campaign: campaign.getName(),
        name: audience.getName(),
        impressions: stats.getImpressions(),
        clicks: stats.getClicks(),
        conversions: stats.getConversions(),
        cost: stats.getCost(),
        cpa: audienceCPA,
        convRate: audienceConvRate,
        performance: performance,
        currentBidMod: audience.getBidModifier()
      };

      report.audiences.push(audienceData);

      // Categorize
      if (performance >= CONFIG.PERFORMANCE_GOOD &&
          stats.getClicks() >= CONFIG.MIN_CLICKS) {
        report.topPerformers.push(audienceData);

        if (audience.getBidModifier() < 1 + (CONFIG.GOOD_BID_ADJUSTMENT / 100)) {
          report.recommendations.push({
            campaign: campaign.getName(),
            audience: audience.getName(),
            action: 'INCREASE BID',
            current: Math.round((audience.getBidModifier() - 1) * 100) + '%',
            recommended: '+' + CONFIG.GOOD_BID_ADJUSTMENT + '%',
            reason: 'CPA ' + Math.round((1 - 1/performance) * 100) + '% beter dan campaign avg'
          });
        }
      } else if (performance <= CONFIG.PERFORMANCE_POOR &&
                 stats.getClicks() >= CONFIG.MIN_CLICKS) {
        report.underperformers.push(audienceData);

        report.recommendations.push({
          campaign: campaign.getName(),
          audience: audience.getName(),
          action: 'DECREASE BID or EXCLUDE',
          current: Math.round((audience.getBidModifier() - 1) * 100) + '%',
          recommended: CONFIG.POOR_BID_ADJUSTMENT + '%',
          reason: 'CPA ' + Math.round((1/performance - 1) * 100) + '% slechter dan campaign avg'
        });
      }
    }
  }

  // Generate and send report
  sendReport(report);
}

function calculateCPA(stats) {
  var conversions = stats.getConversions();
  return conversions > 0 ? stats.getCost() / conversions : 0;
}

function calculateConvRate(stats) {
  var clicks = stats.getClicks();
  return clicks > 0 ? (stats.getConversions() / clicks) * 100 : 0;
}

function sendReport(report) {
  var subject = 'Audience Performance Report - ' + AdsApp.currentAccount().getName();
  var body = 'Weekly Audience Performance Analysis\n';
  body += '=====================================\n\n';

  body += 'SUMMARY:\n';
  body += '────────\n';
  body += 'Total audiences analyzed: ' + report.audiences.length + '\n';
  body += 'Top performers: ' + report.topPerformers.length + '\n';
  body += 'Underperformers: ' + report.underperformers.length + '\n';
  body += 'Recommendations: ' + report.recommendations.length + '\n\n';

  if (report.topPerformers.length > 0) {
    body += 'TOP PERFORMERS:\n';
    body += '───────────────\n';
    for (var i = 0; i < Math.min(report.topPerformers.length, 5); i++) {
      var top = report.topPerformers[i];
      body += '• ' + top.name + '\n';
      body += '  Campaign: ' + top.campaign + '\n';
      body += '  Conversions: ' + top.conversions + ' | CPA: €' + top.cpa.toFixed(2) + '\n';
      body += '  Performance: ' + (top.performance * 100).toFixed(0) + '% of campaign avg\n\n';
    }
  }

  if (report.recommendations.length > 0) {
    body += 'RECOMMENDATIONS:\n';
    body += '────────────────\n';
    for (var j = 0; j < Math.min(report.recommendations.length, 10); j++) {
      var rec = report.recommendations[j];
      body += '• ' + rec.audience + '\n';
      body += '  Campaign: ' + rec.campaign + '\n';
      body += '  Action: ' + rec.action + '\n';
      body += '  Current bid adj: ' + rec.current + ' → Recommended: ' + rec.recommended + '\n';
      body += '  Reason: ' + rec.reason + '\n\n';
    }
  }

  body += '\n---\nGenerated by Audience Performance Analyzer';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
  Logger.log('Report sent to ' + CONFIG.EMAIL);
}
```

## Output: Audience Strategy Template

```markdown
# Audience Strategy Plan

## Business Context
- **Business type:** [B2B/B2C/Local Service]
- **Average deal value:** €[X]
- **Sales cycle length:** [days/weeks/months]
- **Current customer data:** [Yes/No, size]

## Audience Inventory

### First-Party Data Available
| Data Type | Size | Match Rate | Status |
|-----------|------|------------|--------|
| Customer emails | [X] | [X%] | Uploaded/Pending |
| Phone numbers | [X] | [X%] | Uploaded/Pending |
| Website visitors | [X] | N/A | Tag installed |
| GA4 audiences | [X] | N/A | Linked |

### Google Audiences Selected
| Audience Type | Specific Audience | Use Case |
|---------------|-------------------|----------|
| In-market | [category] | Consideration |
| Affinity | [category] | Awareness |
| Custom Segment | [name] | Intent targeting |

## Audience Layering Strategy

### Campaign: [Name]
**Funnel Stage:** [Awareness/Consideration/Decision]

**Targeting Layers:**
```
Layer 1 (Intent):
├── [Audience 1]
└── [Audience 2]

Layer 2 (Qualification):
├── [Audience 3]
└── [Demographics]

Layer 3 (Exclusions):
├── [Exclusion 1]
└── [Exclusion 2]
```

**Bid Adjustments:**
| Audience | Adjustment | Rationale |
|----------|------------|-----------|
| [Audience] | +20% | High performer |
| [Audience] | -15% | Lower quality |

## Implementation Checklist
- [ ] Customer Match lists uploaded
- [ ] In-market audiences added (observation)
- [ ] Custom segments created
- [ ] Exclusion lists configured
- [ ] GA4 audiences linked
- [ ] Bid adjustments set
- [ ] Performance tracking plan defined

## Measurement Plan
- [ ] Audience performance report scheduled
- [ ] Compare: Audience vs non-audience performance
- [ ] Track: Match rates over time
- [ ] Optimize: Weekly bid adjustments
```

---
name: audience-strategy-planner
description: |
  Google Ads audience strategy and targeting planner. Helps with Customer Match implementation, In-market and Affinity audience selection, Similar/Lookalike audience setup, audience layering strategies, first-party data strategy, and B2B audience targeting.
  Use when: audience, customer match, in-market, affinity, similar audiences, lookalike, first party data, targeting, segments, b2b targeting, audience layering, custom segments, remarketing audiences.
  Do NOT use for: remarketing list creation (use remarketing-list-builder), GA4 audience export (use ga4-integration-guide), bid strategy selection (use bid-strategy-selector).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "google_ads"
  phase: "fase-3-lead-generation"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---
# Audience Strategy Planner

Complete guide for setting up an effective Google Ads audience strategy with first-party data, Google audiences, and layering strategies for lead generation.
## Audience Types Overview

### Google Ads Audience Types

```
GOOGLE ADS AUDIENCE TYPES (2025)
════════════════════════════════

┌─────────────────────────────────────────────────────────────────┐
│ TYPE              │ DESCRIPTION            │ USE CASE           │
├───────────────────┼────────────────────────┼────────────────────┤
│ FIRST-PARTY DATA                                                │
├───────────────────┼────────────────────────┼────────────────────┤
│ Customer Match    │ Your customer lists    │ Upsell, loyalty,   │
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

WARNING — SIMILAR AUDIENCES (EU):
├── Limited availability due to privacy regulations
├── Replaced by: Optimized Targeting, Smart Bidding signals
└── Check availability in your account
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
Default settings and recommendations:

┌────────────────────────────────────────────────────────────────┐
│ Audience Type      │ Default │ Recommended (Lead Gen)          │
├────────────────────┼─────────┼────────────────────────────────┤
│ All Visitors       │ 30 days │ 30-90 days                     │
│ Cart Abandoners    │ 30 days │ 7-14 days (urgency)            │
│ Form Started       │ 30 days │ 14-30 days                     │
│ Converters         │ 540 days│ 180-365 days (for exclusion)   │
│ High-value Custom. │ 540 days│ 365 days (upsell)              │
└────────────────────┴─────────┴────────────────────────────────┘
```

## Customer Match Setup

### Customer Match Implementation

```
CUSTOMER MATCH SETUP GUIDE
══════════════════════════

REQUIREMENTS:
─────────────
□ Google Ads account with good history
□ $50,000+ lifetime spend (for some features)
□ 90+ days account history
□ Good policy compliance record

DATA TYPES YOU CAN UPLOAD:
──────────────────────────
□ Email addresses
□ Phone numbers (with country code)
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

STEP-BY-STEP SETUP:
───────────────────

STEP 1: DATA PREPARATION
─────────────────────────
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

STEP 2: CREATE CUSTOMER LIST
─────────────────────────────
1. Tools → Audience Manager → Segments
2. "+ Segment" → "Customer list"
3. Name: "[Purpose]_CustomerMatch_[Date]"
   E.g.: "HighValue_Customers_2025Q1"

STEP 3: UPLOAD DATA
───────────────────
Option A: Manual upload (CSV)
├── Download template
├── Fill in data
├── Upload file

Option B: API upload
├── Use Google Ads API
├── Automate syncs from CRM
└── Real-time updates

STEP 4: SET MEMBERSHIP DURATION
────────────────────────────────
□ Default: Unlimited
□ Recommended: 365-540 days
□ Match with your sales cycle

STEP 5: VERIFY MATCH RATE
──────────────────────────
□ Processing takes 24-48 hours
□ Check list size after processing
□ Target: >40% match rate
```

### Customer Match Strategies

```
CUSTOMER MATCH USE CASES
════════════════════════

1. UPSELL/CROSS-SELL
────────────────────
Goal: Show existing customers new products

Segment: Active customers, last purchase >30 days
Targeting: Customer match (observation or targeting)
Messaging: New products, complementary services
Bid adjustment: +20-50%

2. RETENTION / WIN-BACK
───────────────────────
Goal: Reactivate inactive customers

Segment: Churned customers (no purchase 90+ days)
Targeting: Customer match (targeting)
Messaging: "We miss you", special offers
Bid adjustment: +10-30%

3. EXCLUSION (ACQUISITION FOCUS)
────────────────────────────────
Goal: Target only new customers

Segment: All customers
Targeting: Customer match → Exclude
Use: Prospecting campaigns only
Result: No wasted spend on existing customers

4. SIMILAR AUDIENCES (Scale)
────────────────────────────
Goal: Find new customers who resemble your best customers

Base list: High-value customers
Create: Similar audience automatically
Targeting: Similar to high-value
Use: Prospecting campaigns

WARNING: Similar audiences have limited availability in the EU

5. LOOKALIKE VIA PERFORMANCE MAX
────────────────────────────────
Goal: Scale using Customer Match signals

Setup:
├── Upload customer list as "Audience signal"
├── PMax uses this for targeting optimization
└── Not direct targeting, but used as a signal

SEGMENTATION EXAMPLES:
──────────────────────
□ By purchase value: High ($500+), Medium ($100-500), Low (<$100)
□ By recency: Active (30d), Recent (90d), Lapsed (180d), Churned (365d+)
□ By product: Category A buyers, Category B buyers
□ By LTV: Top 20% customers, Next 30%, Bottom 50%
```

## In-Market & Affinity Audiences

### In-Market Audiences

```
IN-MARKET AUDIENCES STRATEGY
═════════════════════════════

WHAT ARE IN-MARKET AUDIENCES?
─────────────────────────────
Users who are actively researching and showing purchase intent.
Google determines this based on:
├── Search queries
├── Websites visited
├── Content consumed
└── Recent behavior

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

HOW TO USE:
───────────
SEARCH CAMPAIGNS:
├── Add as "Observation" first
├── Analyze performance after 2-4 weeks
├── Best performers → Bid adjustment +10-30%
├── Poor performers → Consider exclusion

DISPLAY/YOUTUBE CAMPAIGNS:
├── Can be used as primary targeting
├── Combine with other audiences
└── Smaller scope = better quality
```

### Affinity Audiences

```
AFFINITY AUDIENCES STRATEGY
════════════════════════════

WHAT ARE AFFINITY AUDIENCES?
────────────────────────────
Users with long-term interests and lifestyle characteristics.
Less immediate intent, but relevant for branding.

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

HOW TO USE:
───────────
□ Affinity = awareness stage
□ Combine with In-market for qualification
□ Use in Display/YouTube, less relevant for Search

CUSTOM AFFINITY (now Custom Segments):
──────────────────────────────────────
Create your own affinity-style audiences:

1. Tools → Audience Manager → Custom Segments
2. "+ Custom segment"
3. Choose: "People with any of these interests or purchase intentions"
4. Add:
   ├── Keywords your audience would search for
   ├── URLs they would visit
   └── Apps they would use
```

### Audience Layering

```
AUDIENCE LAYERING STRATEGIES
═════════════════════════════

WHAT IS AUDIENCE LAYERING?
──────────────────────────
Combining multiple audience types to:
├── Increase precision
├── Reduce waste
└── Maximize relevance

LAYERING METHODS:
─────────────────

1. AND LOGIC (Narrowing)
────────────────────────
"Must match ALL conditions"

Example:
├── In-market: Business Services
├── AND Affinity: Business Professionals
├── AND Demographics: Age 25-54

Result: Smaller, more qualified audience

2. OR LOGIC (Expanding)
───────────────────────
"Match ANY condition"

Example:
├── In-market: CRM Software
├── OR In-market: Cloud Storage
├── OR In-market: Cybersecurity

Result: Larger audience, related interests

3. EXCLUSION LOGIC
──────────────────
"Match A but NOT B"

Example:
├── Target: All website visitors
├── Exclude: Converters
├── Exclude: Customer Match list

Result: Prospecting only, no existing customers

LAYERING FOR B2B LEAD GEN:
──────────────────────────
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

LAYERING FOR LOCAL SERVICES:
────────────────────────────
Campaign: Home Services (Renovation)

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
CUSTOM SEGMENTS (Formerly Custom Intent)
════════════════════════════════════════

WHEN TO USE:
────────────
□ No suitable In-market/Affinity audience available
□ Niche market or product
□ Competitor targeting needed
□ Very specific intent

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

Example (B2B CRM):
├── "best crm software"
├── "crm for small business"
├── "salesforce alternative"
├── "hubspot vs pipedrive"
└── "customer management software"

2. CUSTOM AFFINITY (Interest-based)
───────────────────────────────────
"People who have interests in..."

Setup:
1. Type: "People with any of these interests or purchase intentions"
2. Add:
   ├── Interest keywords
   ├── URLs of relevant websites
   └── Apps they might use

Example (Marketing Professionals):
├── Keywords: digital marketing, content strategy
├── URLs: marketingweek.com, hubspot.com/blog
└── Apps: Hootsuite, Buffer, Sprout Social

3. COMPETITOR TARGETING
───────────────────────
Target users who visit competitor sites

Setup:
1. Type: "People who browse types of websites"
2. Add competitor URLs:
   ├── competitor1.com
   ├── competitor2.com
   └── competitor3.com

WARNING: This targets people WHO BROWSE SIMILAR SITES
   Not exactly those sites — Google's interpretation

BEST PRACTICES:
───────────────
□ Test segments with "Observation" first
□ Start broad, narrow down over time
□ Combine with other targeting
□ Minimum 10 keywords/URLs for good reach
□ Monitor weekly for performance
```

## Audience Strategy for Lead Gen

### Full-Funnel Audience Framework

```
FULL-FUNNEL AUDIENCE STRATEGY
═════════════════════════════

FUNNEL STAGE: AWARENESS (Top)
─────────────────────────────
Goal: Brand awareness, reach
Audiences:
├── Affinity audiences (broad)
├── Similar to customers
├── Custom segments (interest-based)
└── Life events

Campaigns: Display, YouTube, Discovery
Bidding: CPM, Maximize reach
Messaging: Brand story, pain points
Budget: 15-25% of total

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
Budget: 30-40% of total

FUNNEL STAGE: DECISION (Bottom)
───────────────────────────────
Goal: Conversion, leads
Audiences:
├── RLSA (high-intent pages)
├── Cart/form abandoners
├── Return visitors (3+ visits)
├── Customer Match (upsell)
└── GA4 predictive (likely to convert)

Campaigns: Search, Remarketing Display
Bidding: Target CPA, Maximize conversions
Messaging: CTA, urgency, offer
Budget: 35-45% of total

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
Budget: 5-10% of total

┌─────────────────────────────────────────────────────────────────┐
│                     FULL-FUNNEL VISUAL                          │
│                                                                 │
│     AWARENESS        Affinity, Similar, Life Events             │
│     ▼▼▼▼▼▼▼▼▼       Wide reach, brand building                │
│                                                                 │
│     CONSIDERATION    In-market, Custom Intent                   │
│     ▼▼▼▼▼▼          Research phase, education                  │
│                                                                 │
│     DECISION         RLSA, Abandoners, High-intent              │
│     ▼▼▼             Convert intent to action                    │
│                                                                 │
│     LOYALTY          Customer Match, Converters                 │
│     ▼                Retain and grow value                      │
└─────────────────────────────────────────────────────────────────┘
```

### B2B Audience Strategy

```
B2B AUDIENCE TARGETING STRATEGY
═══════════════════════════════

CHALLENGE: B2B targeting is harder
────────────────────────────────
□ No "job title" targeting in Google Ads
□ No "company size" targeting
□ Longer sales cycles
□ Multiple decision makers

SOLUTIONS:
──────────

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
Upload segmented lists:

List 1: Enterprise accounts (1000+ employees)
List 2: Mid-market accounts (100-999 employees)
List 3: SMB accounts (<100 employees)

Create similar audiences from best segment
Target/exclude based on ideal customer

3. CUSTOM SEGMENTS (COMPETITOR/TOOL)
────────────────────────────────────
Target based on tool/competitor research:

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
LinkedIn offers better B2B targeting.
Create customer match list from LinkedIn leads.

Flow:
1. LinkedIn campaign → Generate leads
2. Export leads (email, company)
3. Upload to Google Ads Customer Match
4. Target similar audiences
5. Remarketing via Google Display
```

## Google Ads Script: Audience Performance Analyzer

```javascript
/**
 * Audience Performance Analyzer
 *
 * Analyzes performance of all audiences
 * Generates recommendations for bid adjustments
 *
 * Setup:
 * 1. Update CONFIG
 * 2. Schedule: Weekly
 */

var CONFIG = {
  EMAIL: 'your@email.com',

  // Date range
  DATE_RANGE: 'LAST_30_DAYS',

  // Thresholds
  MIN_IMPRESSIONS: 1000,
  MIN_CLICKS: 50,
  PERFORMANCE_GOOD: 1.2,   // 20% better than campaign avg
  PERFORMANCE_POOR: 0.8,   // 20% worse than campaign avg

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
            reason: 'CPA ' + Math.round((1 - 1/performance) * 100) + '% better than campaign avg'
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
          reason: 'CPA ' + Math.round((1/performance - 1) * 100) + '% worse than campaign avg'
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
      body += '  Conversions: ' + top.conversions + ' | CPA: $' + top.cpa.toFixed(2) + '\n';
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
- **Average deal value:** $[X]
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

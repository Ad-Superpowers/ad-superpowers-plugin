---
name: remarketing-list-builder
description: |
  Google Ads remarketing list builder and RLSA strategy guide. Covers RLSA setup and strategy, dynamic remarketing implementation, audience sizing and segmentation, sequential remarketing, cross-device remarketing, and display remarketing campaigns.
  Use when: remarketing, rlsa, retargeting, dynamic remarketing, audience segments, website visitors, cart abandonment, display remarketing, sequential messaging, remarketing lists, cross-device.
  Do NOT use for: audience strategy planning (use audience-strategy-planner), GA4 audience export (use ga4-integration-guide), bid strategy selection (use bid-strategy-selector).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "google_ads"
  phase: "fase-3-lead-generation"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---
# Remarketing List Builder

Complete guide for setting up effective remarketing lists and RLSA strategies for lead generation with advanced segmentation and messaging sequences.



See [decision-trees.md](references/decision-trees.md) for details.



## Remarketing List Setup

### Google Ads Remarketing Tag

```
REMARKETING TAG IMPLEMENTATION
══════════════════════════════

OPTION 1: GOOGLE ADS TAG (Standalone)
──────────────────────────────────────
When: Only Google Ads remarketing needed

Setup:
1. Tools → Audience Manager → Audience sources
2. "Google Ads tag" → "Set up tag"
3. Choose:
   □ Only collect general site visit data (basic)
   □ Collect specific attributes (dynamic — for e-commerce)

4. Implement tag:
   <script async src="https://www.googletagmanager.com/gtag/js?id=AW-CONVERSION_ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'AW-CONVERSION_ID');
   </script>

OPTION 2: VIA GTM (Recommended)
────────────────────────────────
When: GTM already in use

Setup:
1. GTM → Tags → New
2. Tag Type: Google Ads Remarketing
3. Conversion ID: [from Google Ads]
4. Trigger: All Pages
5. Test & Publish

OPTION 3: VIA GA4 (Best for integration)
─────────────────────────────────────────
When: GA4 already linked to Google Ads

Setup:
1. GA4 linked with Google Ads
2. Create audiences in GA4
3. Auto-sync to Google Ads

Advantage:
├── One tag for everything
├── Richer audience definitions
└── Cross-device out of the box
```

### Basic Remarketing Lists

```
ESSENTIAL REMARKETING LISTS
════════════════════════════

1. ALL VISITORS
───────────────
Name: "All Visitors - 30 Days"
Condition: Any page visit
Duration: 30 days
Size minimum: 1,000 for Search, 100 for Display

Setup (Google Ads):
1. Audience Manager → Segments → "+"
2. Type: Website visitors
3. Segment members: "Visitors of a page"
4. Page URL: Contains "/" (all pages)
5. Membership duration: 30 days

2. HOMEPAGE VISITORS
────────────────────
Name: "Homepage Visitors - 30 Days"
Condition: Homepage visited
Duration: 30 days
Use: Broad awareness, brand recall

URL rule: URL exactly matches [homepage URL]

3. SERVICE/PRODUCT PAGE VISITORS
────────────────────────────────
Name: "Service Page Visitors - 30 Days"
Condition: Key service pages visited
Duration: 30 days
Use: Interest-based targeting

URL rule: URL contains "/services/" OR "/products/"

4. CONTACT/PRICING PAGE VISITORS
────────────────────────────────
Name: "High Intent Pages - 14 Days"
Condition: Contact, pricing, demo pages
Duration: 14 days (shorter = more intent)
Use: High-priority remarketing

URL rule: URL contains "/contact" OR "/pricing" OR "/demo"

5. CONVERTERS
─────────────
Name: "Converters - 180 Days"
Condition: Thank you / confirmation page
Duration: 180 days
Use: Exclusion, cross-sell, loyalty

URL rule: URL contains "/thank-you" OR "/confirmation"

LIST HIERARCHY:
───────────────
┌──────────────────────────────────────────────────────────────┐
│                    ALL VISITORS                               │
│    ┌────────────────────────────────────────────────────┐    │
│    │              SERVICE PAGE VISITORS                   │    │
│    │    ┌────────────────────────────────────────────┐   │    │
│    │    │         HIGH INTENT VISITORS                │   │    │
│    │    │    ┌────────────────────────────────────┐  │   │    │
│    │    │    │         CONVERTERS                  │  │   │    │
│    │    │    └────────────────────────────────────┘  │   │    │
│    │    └────────────────────────────────────────────┘   │    │
│    └────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

### Advanced Segmentation

```
ADVANCED REMARKETING SEGMENTS
═════════════════════════════

1. ENGAGEMENT-BASED SEGMENTS
─────────────────────────────

LOW ENGAGEMENT (Bounce):
Name: "Bouncers - 30 Days"
Condition (GA4): session_engaged = false
Duration: 30 days
Strategy: Don't target, or awareness only

MEDIUM ENGAGEMENT:
Name: "Engaged Visitors - 30 Days"
Condition (GA4): session_engaged = true AND pages > 2
Duration: 30 days
Strategy: Educational content, soft CTA

HIGH ENGAGEMENT:
Name: "High Engagement - 14 Days"
Condition (GA4): session_duration > 180 sec OR events > 5
Duration: 14 days
Strategy: Aggressive remarketing, strong CTA

2. RECENCY-BASED SEGMENTS
──────────────────────────
Segment by duration and combinations:

HOT LEADS (1-3 days):
├── Most likely to convert
├── Highest bids
└── Aggressive messaging

WARM LEADS (4-14 days):
├── Still interested
├── Medium bids
└── Reminder messaging

COLD LEADS (15-30 days):
├── Need re-engagement
├── Lower bids
└── Value proposition refresh

DORMANT (31-90 days):
├── Last chance
├── Lowest bids
└── Special offer/incentive

3. FUNNEL-BASED SEGMENTS
─────────────────────────

TOP FUNNEL:
Name: "Blog Readers - 30 Days"
Condition: Visited /blog/ pages
Strategy: Lead magnet, newsletter signup

MID FUNNEL:
Name: "Service Explorers - 21 Days"
Condition: Visited 2+ service pages
Strategy: Case studies, testimonials

BOTTOM FUNNEL:
Name: "Form Starters - 7 Days"
Condition: Started form but didn't complete
Strategy: Simplified form, phone CTA

4. FORM ABANDONMENT SEGMENTS
─────────────────────────────
Requires: Event tracking on form interactions

Name: "Form Abandoners - 7 Days"
Condition (GA4): form_start event WITHOUT form_submit event
Duration: 7 days
Strategy: "Still have a question?", direct contact options

Setup in GA4:
1. Create event: form_start (on focus first field)
2. Create event: form_submit (on form success)
3. Audience: form_start AND NOT form_submit (7 days)
```

## RLSA (Remarketing Lists for Search Ads)

### RLSA Strategy

```
RLSA STRATEGY
═════════════

WHAT IS RLSA?
─────────────
Remarketing Lists for Search Ads =
Apply your remarketing audiences to Search campaigns

ADVANTAGES:
───────────
□ Bid higher on return visitors (known intent)
□ Use broader match types (they already know you)
□ Personalized ad copy
□ Target competitor keywords (for return visitors)

RLSA IMPLEMENTATION MODES:
──────────────────────────

1. OBSERVATION (Bid Only)
──────────────────────────
= Monitor performance + bid adjustments
= Everyone can see ads
= RLSA users get bid boost

Setup:
1. Campaign → Audiences → "+"
2. Add audience
3. Targeting: "Observation"
4. Set bid adjustment: +10% to +50%

Use when:
□ You don't want to lose traffic
□ Testing RLSA value
□ Broad campaign goal

2. TARGETING (Target Only)
──────────────────────────
= Only RLSA users see these ads
= Exclusive targeting

Setup:
1. Campaign → Audiences → "+"
2. Add audience
3. Targeting: "Targeting"

Use when:
□ Competitor bidding (only for return visitors)
□ Broader keywords (less risk with known users)
□ Special RLSA-only campaigns

RLSA BID ADJUSTMENTS:
─────────────────────
┌────────────────────────────────────────────────────────────────┐
│ Audience Segment         │ Recommended Bid Adjustment         │
├──────────────────────────┼────────────────────────────────────┤
│ All visitors (30d)       │ +10% to +20%                       │
├──────────────────────────┼────────────────────────────────────┤
│ High-intent pages        │ +30% to +50%                       │
├──────────────────────────┼────────────────────────────────────┤
│ Cart/form abandoners     │ +40% to +70%                       │
├──────────────────────────┼────────────────────────────────────┤
│ Past converters (upsell) │ +20% to +40%                       │
├──────────────────────────┼────────────────────────────────────┤
│ Converters (exclude)     │ -100% (exclusion)                  │
└────────────────────────────────────────────────────────────────┘
```

### RLSA Campaign Structure

```
RLSA CAMPAIGN STRUCTURES
═════════════════════════

STRUCTURE 1: LAYERED BIDDING (Observation)
──────────────────────────────────────────

Campaign: Lead Gen - Search
├── Target: All users
├── Keywords: Phrase/Exact match
├── Audiences (Observation):
│   ├── All Visitors 30d: +15%
│   ├── Service Page Visitors: +30%
│   ├── High Intent Pages: +50%
│   └── Converters: -100% (exclude)
└── Budget: Normal

STRUCTURE 2: RLSA-ONLY CAMPAIGN (Targeting)
───────────────────────────────────────────

Campaign: RLSA - Broad Match Test
├── Target: RLSA users only
├── Keywords: Broad match (low risk with known users)
├── Audiences (Targeting):
│   └── High Intent Pages (14d)
├── Budget: Lower (smaller audience)
└── Use: Test broader keywords safely

Campaign: RLSA - Competitor Targeting
├── Target: RLSA users only
├── Keywords: Competitor brand names
├── Audiences (Targeting):
│   └── All Visitors (30d)
├── Messaging: "Come back to [Your Brand]"
└── Use: Win-back from competitor researchers

STRUCTURE 3: HYBRID (Best Practice)
────────────────────────────────────

Campaign 1: General Search (All users)
├── Standard targeting
├── RLSA as Observation
├── Bid adjustments per segment
└── Exclude converters

Campaign 2: RLSA High-Intent (RLSA only)
├── Target: High-intent visitors
├── Broader keywords OK
├── More aggressive bids
└── Personalized messaging

Campaign 3: RLSA Win-Back (RLSA only)
├── Target: 30-90 day old visitors
├── Competitor keywords
├── Re-engagement messaging
└── Special offers
```

## Display Remarketing

### Display Remarketing Setup

```
DISPLAY REMARKETING CAMPAIGN SETUP
═══════════════════════════════════

STEP 1: CAMPAIGN CREATION
──────────────────────────
1. + New Campaign → Leads
2. Campaign type: Display
3. Campaign subtype: Standard display

STEP 2: TARGETING
─────────────────
Audiences:
1. Add remarketing lists
2. Targeting: "Targeting" (not Observation)
3. Content targeting: Not recommended for remarketing
   → Remarketing works based on user, not content

WARNING — EXCLUSIONS ARE IMPORTANT:
├── Exclude converters (always)
├── Exclude recent contacts (if relevant)
└── Exclude branded traffic (if separate campaign)

STEP 3: BIDDING
───────────────
Recommended: Target CPA or Maximize Conversions
Reason: Remarketing often has higher conversion rates

Alternative: Manual CPC (more control)
Starting bid: 50-70% of Search CPC

STEP 4: ADS
────────────

RESPONSIVE DISPLAY ADS (Recommended):
├── Headlines (5): Mix of brand recall + CTA
├── Long headline (1): Value prop + CTA
├── Descriptions (5): Benefits, social proof
├── Images: 1200x628 (landscape), 1200x1200 (square)
├── Logo: 1200x1200
└── Video (optional): 30 sec YouTube video

IMAGE AD SIZES (Upload if custom):
├── 300x250 (Rectangle)
├── 728x90 (Leaderboard)
├── 160x600 (Wide Skyscraper)
├── 300x600 (Half Page)
└── 320x50 (Mobile Banner)

AD COPY FOR REMARKETING:
────────────────────────
Segment: General Visitors
├── Headline: "Still looking for [service]?"
├── Description: "Discover why 1000+ customers chose us"
└── CTA: "Get Free Consultation"

Segment: High-Intent (Pricing/Contact)
├── Headline: "Ready to get started?"
├── Description: "Contact us for a no-obligation quote"
└── CTA: "Call Now" or "Book Appointment"

Segment: Form Abandoners
├── Headline: "We haven't received your request yet"
├── Description: "Still have questions? We're happy to help."
└── CTA: "Complete Your Request"
```

### Sequential Remarketing

```
SEQUENTIAL REMARKETING (Messaging Sequence)
════════════════════════════════════════════

WHAT IS SEQUENTIAL REMARKETING?
───────────────────────────────
= Show different messages based on time since visit
= Tell a "story" across multiple touchpoints
= Gradual CTA escalation

SEQUENCE EXAMPLE (Lead Gen):
────────────────────────────

┌─────────────────────────────────────────────────────────────────┐
│ DAY 1-3: AWARENESS RECALL                                       │
│ ────────────────────────────────────────────────────────────── │
│ Audience: All Visitors (1-3 days)                               │
│ Message: Brand reminder, problem acknowledgment                 │
│ CTA: "Learn More" (soft)                                        │
│                                                                 │
│ Headline: "[Problem]? We have the solution."                    │
│ Description: "Discover how [Brand] helps with [benefit]"        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ DAY 4-7: EDUCATION                                              │
│ ────────────────────────────────────────────────────────────── │
│ Audience: Visitors (4-7 days) MINUS Recent Converters           │
│ Message: Social proof, case study, how it works                 │
│ CTA: "View Case Study" (medium)                                 │
│                                                                 │
│ Headline: "How [Customer] achieved [Result]"                    │
│ Description: "500+ companies preceded you. Read their story."   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ DAY 8-14: CONSIDERATION                                         │
│ ────────────────────────────────────────────────────────────── │
│ Audience: Visitors (8-14 days) MINUS Recent Converters          │
│ Message: Differentiation, why choose us                         │
│ CTA: "Compare Options" (medium-strong)                          │
│                                                                 │
│ Headline: "Why choose [Brand]?"                                 │
│ Description: "[USP 1]. [USP 2]. [USP 3]. Discover for yourself."│
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ DAY 15-30: CONVERSION PUSH                                      │
│ ────────────────────────────────────────────────────────────── │
│ Audience: Visitors (15-30 days) MINUS Recent Converters         │
│ Message: Urgency, offer, direct CTA                             │
│ CTA: "Start Now" or "Request Quote" (strong)                    │
│                                                                 │
│ Headline: "Last Chance: Free Consultation"                      │
│ Description: "Book your free consultation this week."           │
└─────────────────────────────────────────────────────────────────┘

SETUP IN GOOGLE ADS:
────────────────────
1. Create 4 audience lists with recency:
   ├── All Visitors 3 days
   ├── All Visitors 7 days
   ├── All Visitors 14 days
   └── All Visitors 30 days

2. Create 4 ad groups with exclusions:
   ├── AG1: Target 3d, Exclude: none
   ├── AG2: Target 7d, Exclude: 3d + Converters
   ├── AG3: Target 14d, Exclude: 7d + Converters
   └── AG4: Target 30d, Exclude: 14d + Converters

3. Different ads per ad group with sequence messaging
```

## Dynamic Remarketing

### Dynamic Remarketing Setup

```
DYNAMIC REMARKETING (E-commerce / Lead Gen)
════════════════════════════════════════════

WHAT IS DYNAMIC REMARKETING?
────────────────────────────
= Automatically show the right products/services
= Based on what the user viewed
= Personalized ads at scale

REQUIREMENTS:
─────────────
□ Google Merchant Center (e-commerce) OR
□ Business data feed (services)
□ Dynamic remarketing tag with parameters
□ Responsive display ads

SETUP FOR E-COMMERCE:
─────────────────────

1. MERCHANT CENTER FEED
───────────────────────
Ensure Merchant Center is active with:
├── Product feed up-to-date
├── All products approved
└── Linked to Google Ads

2. DYNAMIC REMARKETING TAG
──────────────────────────
Add product parameters to pages:

<script>
gtag('event', 'view_item', {
  'send_to': 'AW-CONVERSION_ID',
  'value': 29.99,
  'items': [{
    'id': 'SKU12345',
    'google_business_vertical': 'retail'
  }]
});
</script>

Events:
├── view_item: Product page view
├── add_to_cart: Added to cart
├── view_cart: Viewed cart
└── purchase: Completed purchase

3. DYNAMIC DISPLAY CAMPAIGN
────────────────────────────
1. New Campaign → Sales → Display
2. Campaign subtype: Display (standard)
3. Audiences: Website visitors (targeting)
4. Ads: Responsive display ads
5. Enable: "Add a data feed for personalized ads"

SETUP FOR SERVICES (Lead Gen):
──────────────────────────────

1. BUSINESS DATA FEED
─────────────────────
Create CSV with services:

ID,Item title,Final URL,Image URL,Item description,Price
service-1,"Website Development","https://site.com/websites","https://...",Description,from $999
service-2,"SEO Optimization","https://site.com/seo","https://...",Description,from $499

2. UPLOAD FEED
──────────────
1. Tools → Business data → +Data feed
2. Template: Custom
3. Upload CSV
4. Map fields

3. DYNAMIC TAG FOR SERVICES
────────────────────────────
<script>
gtag('event', 'page_view', {
  'send_to': 'AW-CONVERSION_ID',
  'dynx_itemid': 'service-1',
  'dynx_pagetype': 'offerdetail'
});
</script>

Page types:
├── home: Homepage
├── searchresults: Service overview
├── offerdetail: Specific service page
├── conversionintent: Contact/pricing page
└── conversion: Thank you page
```

## Cross-Device Remarketing

### Cross-Device Strategy

```
CROSS-DEVICE REMARKETING
═════════════════════════

HOW DOES CROSS-DEVICE WORK?
────────────────────────────
User visits site on mobile → later retargeted on desktop
Possible through:
├── Google signed-in users
├── GA4 User-ID tracking
└── Device graph estimation

MAXIMIZE CROSS-DEVICE TRACKING:
───────────────────────────────

1. GOOGLE SIGNALS (GA4)
───────────────────────
Setup:
1. GA4 → Admin → Data Settings → Data Collection
2. Enable "Google signals data collection"
3. Acknowledgment: Accept

Result:
├── Cross-device user journeys
├── Better remarketing matching
└── Demographics/interests data

2. USER-ID TRACKING (If user logs in)
──────────────────────────────────────
For sites with login:

<script>
gtag('config', 'G-XXXXXXX', {
  'user_id': 'USER_ID_HASH'
});
</script>

WARNING: Use hashed user ID, not plain text

3. SAME ACCOUNT LINKING
────────────────────────
Ensure all properties are linked:
├── GA4 ↔ Google Ads
├── YouTube ↔ Google Ads
├── Firebase ↔ Google Ads (apps)
└── All accounts in same organization

CROSS-DEVICE AUDIENCE STRATEGY:
───────────────────────────────

Multi-device user journey:
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  MOBILE (Discovery)          DESKTOP (Conversion)              │
│  ─────────────────          ─────────────────────              │
│                                                                │
│  1. User sees ad on mobile   4. Retarget on desktop            │
│  2. Visits site, browses     5. Recognition by Google          │
│  3. Leaves (no conversion)   6. Conversion!                    │
│                                                                │
│  ↓                                                             │
│  Remarketing list captures visit (cross-device enabled)        │
│                                                                │
└────────────────────────────────────────────────────────────────┘

DEVICE BID ADJUSTMENTS:
───────────────────────
Combine device bids with RLSA:

Remarketing visitors (RLSA):
├── Mobile: +20% (assist device)
├── Desktop: +30% (conversion device)
└── Tablet: +10%

Adjust based on data:
1. Segment by device in reports
2. Check conversion rate per device for RLSA
3. Adjust bids accordingly
```

## Google Ads Script: Remarketing List Health Check

```javascript
/**
 * Remarketing List Health Monitor
 *
 * Monitors:
 * - List sizes and growth
 * - List expirations
 * - Coverage vs campaigns
 *
 * Setup:
 * 1. Update CONFIG
 * 2. Schedule: Weekly
 */

var CONFIG = {
  EMAIL: 'your@email.com',

  // Thresholds
  MIN_LIST_SIZE_SEARCH: 1000,
  MIN_LIST_SIZE_DISPLAY: 100,
  GROWTH_WARNING_THRESHOLD: -0.10, // -10% = warning

  // Lists to monitor (names or partial names)
  CRITICAL_LISTS: [
    'All Visitors',
    'Converters',
    'High Intent'
  ]
};

function main() {
  var report = {
    lists: [],
    warnings: [],
    recommendations: []
  };

  var audienceIterator = AdsApp.userlists().get();

  while (audienceIterator.hasNext()) {
    var audience = audienceIterator.next();
    var name = audience.getName();
    var searchSize = audience.getSizeForSearch();
    var displaySize = audience.getSizeForDisplay();
    var type = audience.getType();

    var listData = {
      name: name,
      type: type,
      searchSize: formatSize(searchSize),
      displaySize: formatSize(displaySize),
      status: getListStatus(searchSize, displaySize),
      membershipLifespan: audience.getMembershipLifespan()
    };

    report.lists.push(listData);

    // Check for issues
    checkListHealth(listData, report);
  }

  // Check campaign coverage
  checkCampaignCoverage(report);

  // Send report
  sendReport(report);
}

function formatSize(size) {
  if (size === 0) return '0';
  if (size < 1000) return size.toString();
  if (size < 1000000) return Math.round(size / 1000) + 'k';
  return (size / 1000000).toFixed(1) + 'M';
}

function getListStatus(searchSize, displaySize) {
  if (searchSize >= CONFIG.MIN_LIST_SIZE_SEARCH) return 'OK';
  if (displaySize >= CONFIG.MIN_LIST_SIZE_DISPLAY) return 'Display Only';
  return 'Too Small';
}

function checkListHealth(listData, report) {
  // Check for critical lists
  for (var i = 0; i < CONFIG.CRITICAL_LISTS.length; i++) {
    var criticalName = CONFIG.CRITICAL_LISTS[i];
    if (listData.name.indexOf(criticalName) !== -1) {

      if (listData.status === 'Too Small') {
        report.warnings.push({
          type: 'CRITICAL_LIST_SMALL',
          list: listData.name,
          message: 'Critical list "' + listData.name + '" is too small for targeting'
        });
      }
    }
  }

  // Check for very short membership
  if (listData.membershipLifespan && listData.membershipLifespan < 7) {
    report.recommendations.push({
      type: 'SHORT_MEMBERSHIP',
      list: listData.name,
      message: 'List "' + listData.name + '" has very short membership (' +
               listData.membershipLifespan + ' days). Consider extending.'
    });
  }
}

function checkCampaignCoverage(report) {
  var campaignsWithRemarketing = 0;
  var campaignsWithoutRemarketing = 0;

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignType = SEARCH')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var audiences = campaign.targeting().audiences().get();

    if (audiences.hasNext()) {
      campaignsWithRemarketing++;
    } else {
      campaignsWithoutRemarketing++;
    }
  }

  if (campaignsWithoutRemarketing > 0) {
    report.recommendations.push({
      type: 'MISSING_RLSA',
      message: campaignsWithoutRemarketing + ' Search campaigns have no RLSA audiences. ' +
               'Consider adding remarketing lists for observation.'
    });
  }

  report.summary = {
    campaignsWithRLSA: campaignsWithRemarketing,
    campaignsWithoutRLSA: campaignsWithoutRemarketing
  };
}

function sendReport(report) {
  var subject = 'Remarketing Health Report - ' + AdsApp.currentAccount().getName();
  var body = 'Remarketing Lists Health Check\n';
  body += '===============================\n\n';

  body += 'SUMMARY:\n';
  body += '────────\n';
  body += 'Total lists: ' + report.lists.length + '\n';
  body += 'Campaigns with RLSA: ' + report.summary.campaignsWithRLSA + '\n';
  body += 'Campaigns without RLSA: ' + report.summary.campaignsWithoutRLSA + '\n\n';

  if (report.warnings.length > 0) {
    body += 'WARNINGS:\n';
    body += '─────────\n';
    for (var i = 0; i < report.warnings.length; i++) {
      body += '• ' + report.warnings[i].message + '\n';
    }
    body += '\n';
  }

  body += 'LIST STATUS:\n';
  body += '────────────\n';
  for (var j = 0; j < Math.min(report.lists.length, 15); j++) {
    var list = report.lists[j];
    var status = list.status === 'OK' ? '[OK]' :
                 list.status === 'Display Only' ? '[Display]' : '[Small]';
    body += status + ' ' + list.name + '\n';
    body += '  Search: ' + list.searchSize + ' | Display: ' + list.displaySize + '\n';
  }

  if (report.lists.length > 15) {
    body += '... and ' + (report.lists.length - 15) + ' more lists\n';
  }
  body += '\n';

  if (report.recommendations.length > 0) {
    body += 'RECOMMENDATIONS:\n';
    body += '────────────────\n';
    for (var k = 0; k < report.recommendations.length; k++) {
      body += '• ' + report.recommendations[k].message + '\n';
    }
  }

  body += '\n---\nGenerated by Remarketing Health Monitor';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
  Logger.log('Report sent to ' + CONFIG.EMAIL);
}
```

## Output: Remarketing Strategy Template

```markdown
# Remarketing Strategy Plan

## Account Context
- **Business type:** [B2B/B2C/Local Service]
- **Monthly website visitors:** [X]
- **Current conversion rate:** [X%]
- **Average time to conversion:** [X days]

## Remarketing Lists Inventory

### Required Lists
| List Name | Definition | Duration | Min Size | Priority |
|-----------|------------|----------|----------|----------|
| All Visitors | URL: / | 30 days | 1,000 | High |
| Service Pages | URL: /services/* | 30 days | 500 | High |
| High Intent | URL: /contact OR /pricing | 14 days | 200 | Critical |
| Form Abandoners | form_start NOT form_submit | 7 days | 100 | Critical |
| Converters | URL: /thank-you | 180 days | N/A | Exclusion |

### Segment Breakdown
| Segment | Definition | Campaign Use | Bid Adj |
|---------|------------|--------------|---------|
| Hot (1-3d) | Visitors 1-3 days | Display, RLSA | +50% |
| Warm (4-14d) | Visitors 4-14 days | Display, RLSA | +25% |
| Cold (15-30d) | Visitors 15-30 days | Display | +10% |

## RLSA Strategy

### Search Campaigns RLSA Setup
| Campaign | Audience | Mode | Bid Adjustment |
|----------|----------|------|----------------|
| Brand | All Visitors | Observation | +20% |
| Non-Brand | High Intent | Observation | +40% |
| Non-Brand | Converters | Observation | -100% |
| RLSA-Only | All Visitors | Targeting | N/A |

## Display Remarketing

### Campaign Structure
- **Campaign 1:** Standard Remarketing (All visitors excl converters)
- **Campaign 2:** High-Intent Remarketing (Pricing/contact visitors)
- **Campaign 3:** Sequential Remarketing (Tiered messaging)

### Sequential Messaging Plan
| Day Range | Message Theme | CTA |
|-----------|---------------|-----|
| 1-3 | Brand recall | Learn More |
| 4-7 | Social proof | See Case Studies |
| 8-14 | Differentiation | Compare Options |
| 15-30 | Urgency/Offer | Get Started |

## Implementation Checklist

### Phase 1: Tag Setup
- [ ] Remarketing tag implemented (all pages)
- [ ] Event tracking for key interactions
- [ ] Form abandonment tracking
- [ ] Conversion page tracking

### Phase 2: List Creation
- [ ] All Visitors list created
- [ ] High-intent pages list created
- [ ] Converters list created (for exclusion)
- [ ] Form abandoners list created
- [ ] Recency-based segments created

### Phase 3: RLSA
- [ ] RLSA audiences added to Search campaigns
- [ ] Bid adjustments configured
- [ ] Converter exclusion active
- [ ] 2-week observation period

### Phase 4: Display
- [ ] Display remarketing campaign created
- [ ] Responsive display ads uploaded
- [ ] Frequency cap set (3-5 per day)
- [ ] Sequential messaging configured

## Success Metrics
- [ ] List sizes meeting minimums
- [ ] RLSA performance vs non-RLSA
- [ ] Display remarketing ROAS
- [ ] Assisted conversions from remarketing
```

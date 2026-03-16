---
name: remarketing-list-builder
description: "Google Ads remarketing lijst builder en RLSA strategie gids. Gebruik voor: (1) RLSA setup en strategie, (2) Dynamic remarketing implementatie, (3) Audience sizing en segmentatie, (4) Sequential remarketing, (5) Cross-device remarketing, (6) Display remarketing campagnes. Triggers: remarketing, rlsa, retargeting, dynamic remarketing, audience segments, website visitors, cart abandonment, display remarketing, sequential messaging."
---

# Remarketing List Builder

Complete gids voor het opzetten van effectieve remarketing lijsten en RLSA strategieën voor lead generation met advanced segmentatie en messaging sequences.

## Quick Decision Guide

```
WELK REMARKETING TYPE PAST BIJ JOU?
│
├─► SEARCH CAMPAIGNS (RLSA)
│   └─► REMARKETING LISTS FOR SEARCH ADS
│       ├── Bid hoger op return visitors
│       ├── Gebruik bredere match types
│       └── Aangepaste messaging voor returners
│
├─► LEAD GEN / SERVICES
│   └─► STANDARD REMARKETING
│       ├── Display banners naar visitors
│       ├── Segmenteer op engagement level
│       └── Sequential messaging
│
├─► E-COMMERCE
│   └─► DYNAMIC REMARKETING
│       ├── Product-specifieke ads
│       ├── Cart abandonment focus
│       └── Cross-sell opportunities
│
├─► VIDEO ENGAGEMENT
│   └─► YOUTUBE REMARKETING
│       ├── Video viewers als audience
│       ├── Channel subscribers
│       └── Cross-platform remarketing
│
└─► ADVANCED / FULL FUNNEL
    └─► COMBINED STRATEGY
        ├── RLSA + Display + YouTube
        ├── Sequential messaging
        └── Exclusion laddering
```

## Remarketing List Setup

### Google Ads Remarketing Tag

```
REMARKETING TAG IMPLEMENTATIE
═════════════════════════════

OPTIE 1: GOOGLE ADS TAG (Standalone)
────────────────────────────────────
Wanneer: Alleen Google Ads remarketing nodig

Setup:
1. Tools → Audience Manager → Audience sources
2. "Google Ads tag" → "Set up tag"
3. Kies:
   □ Only collect general site visit data (basic)
   □ Collect specific attributes (dynamic - voor e-commerce)

4. Implementeer tag:
   <script async src="https://www.googletagmanager.com/gtag/js?id=AW-CONVERSION_ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'AW-CONVERSION_ID');
   </script>

OPTIE 2: VIA GTM (Aanbevolen)
─────────────────────────────
Wanneer: GTM al in gebruik

Setup:
1. GTM → Tags → New
2. Tag Type: Google Ads Remarketing
3. Conversion ID: [van Google Ads]
4. Trigger: All Pages
5. Test & Publish

OPTIE 3: VIA GA4 (Beste voor integratie)
────────────────────────────────────────
Wanneer: GA4 al gelinked aan Google Ads

Setup:
1. GA4 linked met Google Ads ✓
2. Audiences in GA4 maken
3. Auto-sync naar Google Ads

Voordeel:
├── Eén tag voor alles
├── Rijkere audience definitie
└── Cross-device out of the box
```

### Basic Remarketing Lists

```
ESSENTIËLE REMARKETING LISTS
════════════════════════════

1. ALL VISITORS
───────────────
Name: "All Visitors - 30 Days"
Condition: Any page visit
Duration: 30 dagen
Size minimum: 1,000 voor Search, 100 voor Display

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
Duration: 30 dagen
Use: Broad awareness, brand recall

URL rule: URL exactly matches [homepage URL]

3. SERVICE/PRODUCT PAGE VISITORS
────────────────────────────────
Name: "Service Page Visitors - 30 Days"
Condition: Key service pages visited
Duration: 30 dagen
Use: Interest-based targeting

URL rule: URL contains "/services/" OR "/diensten/"

4. CONTACT/PRICING PAGE VISITORS
────────────────────────────────
Name: "High Intent Pages - 14 Days"
Condition: Contact, pricing, demo pages
Duration: 14 dagen (korter = meer intent)
Use: High-priority remarketing

URL rule: URL contains "/contact" OR "/pricing" OR "/demo"

5. CONVERTERS
─────────────
Name: "Converters - 180 Days"
Condition: Thank you / confirmation page
Duration: 180 dagen
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
GEAVANCEERDE REMARKETING SEGMENTEN
══════════════════════════════════

1. ENGAGEMENT-BASED SEGMENTS
────────────────────────────

LOW ENGAGEMENT (Bounce):
Name: "Bouncers - 30 Days"
Condition (GA4): session_engaged = false
Duration: 30 dagen
Strategy: Don't target, of awareness only

MEDIUM ENGAGEMENT:
Name: "Engaged Visitors - 30 Days"
Condition (GA4): session_engaged = true AND pages > 2
Duration: 30 dagen
Strategy: Educational content, soft CTA

HIGH ENGAGEMENT:
Name: "High Engagement - 14 Days"
Condition (GA4): session_duration > 180 sec OR events > 5
Duration: 14 dagen
Strategy: Aggressive remarketing, strong CTA

2. RECENCY-BASED SEGMENTS
─────────────────────────
Segment door duration en combinaties:

HOT LEADS (1-3 dagen):
├── Most likely to convert
├── Highest bids
└── Aggressive messaging

WARM LEADS (4-14 dagen):
├── Still interested
├── Medium bids
└── Reminder messaging

COLD LEADS (15-30 dagen):
├── Need re-engagement
├── Lower bids
└── Value proposition refresh

DORMANT (31-90 dagen):
├── Last chance
├── Lowest bids
└── Special offer/incentive

3. FUNNEL-BASED SEGMENTS
────────────────────────

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
────────────────────────────
Vereist: Event tracking op form interactions

Name: "Form Abandoners - 7 Days"
Condition (GA4): form_start event WITHOUT form_submit event
Duration: 7 dagen
Strategy: "Nog een vraag?", directe contact opties

Setup in GA4:
1. Create event: form_start (on focus first field)
2. Create event: form_submit (on form success)
3. Audience: form_start AND NOT form_submit (7 days)
```

## RLSA (Remarketing Lists for Search Ads)

### RLSA Strategy

```
RLSA STRATEGIE
══════════════

WAT IS RLSA?
────────────
Remarketing Lists for Search Ads =
Je remarketing audiences toepassen op Search campaigns

VOORDELEN:
──────────
□ Bid hoger op return visitors (known intent)
□ Gebruik bredere match types (ze kennen je al)
□ Gepersonaliseerde ad copy
□ Target competitor keywords (voor return visitors)

RLSA IMPLEMENTATION MODES:
──────────────────────────

1. OBSERVATION (Bid Only)
─────────────────────────
= Monitor performance + bid adjustments
= Everyone can see ads
= RLSA users get bid boost

Setup:
1. Campaign → Audiences → "+"
2. Add audience
3. Targeting: "Observation"
4. Set bid adjustment: +10% to +50%

Use when:
□ Je wilt geen traffic verliezen
□ Testing RLSA value
□ Breed campagne doel

2. TARGETING (Target Only)
──────────────────────────
= Only RLSA users see these ads
= Exclusive targeting

Setup:
1. Campaign → Audiences → "+"
2. Add audience
3. Targeting: "Targeting"

Use when:
□ Competitor bidding (alleen voor return visitors)
□ Bredere keywords (minder risico met known users)
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
RLSA CAMPAIGN STRUCTUREN
════════════════════════

STRUCTUUR 1: LAYERED BIDDING (Observation)
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

STRUCTUUR 2: RLSA-ONLY CAMPAIGN (Targeting)
───────────────────────────────────────────

Campaign: RLSA - Broad Match Test
├── Target: RLSA users only
├── Keywords: Broad match (laag risico met known users)
├── Audiences (Targeting):
│   └── High Intent Pages (14d)
├── Budget: Lower (smaller audience)
└── Use: Test bredere keywords veilig

Campaign: RLSA - Competitor Targeting
├── Target: RLSA users only
├── Keywords: Competitor brand names
├── Audiences (Targeting):
│   └── All Visitors (30d)
├── Messaging: "Come back to [Your Brand]"
└── Use: Win-back van competitor researchers

STRUCTUUR 3: HYBRID (Best Practice)
───────────────────────────────────

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
DISPLAY REMARKETING CAMPAGNE SETUP
══════════════════════════════════

STAP 1: CAMPAIGN CREATION
─────────────────────────
1. + New Campaign → Leads
2. Campaign type: Display
3. Campaign subtype: Standard display

STAP 2: TARGETING
─────────────────
Audiences:
1. Add remarketing lists
2. Targeting: "Targeting" (niet Observation)
3. Content targeting: Afgeraden voor remarketing
   → Remarketing werkt op basis van user, niet content

⚠️ EXCLUSIONS BELANGRIJK:
├── Exclude converters (altijd)
├── Exclude recent contact (indien relevant)
└── Exclude branded traffic (indien aparte campaign)

STAP 3: BIDDING
───────────────
Recommended: Target CPA of Maximize Conversions
Reden: Remarketing heeft vaak hogere conv rates

Alternative: Manual CPC (meer controle)
Start bid: 50-70% van Search CPC

STAP 4: ADS
───────────

RESPONSIVE DISPLAY ADS (Aanbevolen):
├── Headlines (5): Mix van brand recall + CTA
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

AD COPY VOOR REMARKETING:
─────────────────────────
Segment: General Visitors
├── Headline: "Nog steeds op zoek naar [service]?"
├── Description: "Ontdek waarom 1000+ klanten voor ons kozen"
└── CTA: "Vraag Gratis Advies"

Segment: High-Intent (Pricing/Contact)
├── Headline: "Klaar om te starten?"
├── Description: "Neem contact op voor een vrijblijvende offerte"
└── CTA: "Bel Nu" of "Plan Afspraak"

Segment: Form Abandoners
├── Headline: "We hebben uw aanvraag nog niet ontvangen"
├── Description: "Heeft u nog vragen? Wij helpen graag verder."
└── CTA: "Maak Aanvraag Af"
```

### Sequential Remarketing

```
SEQUENTIAL REMARKETING (Messaging Sequence)
════════════════════════════════════════════

WAT IS SEQUENTIAL REMARKETING?
──────────────────────────────
= Verschillende boodschappen tonen gebaseerd op tijd sinds bezoek
= "Story" vertellen over meerdere touchpoints
= Graduele CTA escalatie

SEQUENCE VOORBEELD (Lead Gen):
──────────────────────────────

┌─────────────────────────────────────────────────────────────────┐
│ DAG 1-3: AWARENESS RECALL                                       │
│ ───────────────────────────────────────────────────────────────│
│ Audience: All Visitors (1-3 days)                               │
│ Message: Brand reminder, problem acknowledgment                 │
│ CTA: "Lees Meer" (soft)                                        │
│                                                                  │
│ Headline: "[Probleem]? Wij hebben de oplossing."               │
│ Description: "Ontdek hoe [Brand] helpt met [benefit]"          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ DAG 4-7: EDUCATION                                              │
│ ───────────────────────────────────────────────────────────────│
│ Audience: Visitors (4-7 days) MINUS Recent Converters          │
│ Message: Social proof, case study, how it works                │
│ CTA: "Bekijk Case Study" (medium)                              │
│                                                                  │
│ Headline: "Hoe [Klant] [Resultaat] bereikte"                   │
│ Description: "500+ bedrijven gingen u voor. Lees hun verhaal." │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ DAG 8-14: CONSIDERATION                                         │
│ ───────────────────────────────────────────────────────────────│
│ Audience: Visitors (8-14 days) MINUS Recent Converters         │
│ Message: Differentiation, why choose us                        │
│ CTA: "Vergelijk Opties" (medium-strong)                        │
│                                                                  │
│ Headline: "Waarom [Brand] kiezen?"                             │
│ Description: "[USP 1]. [USP 2]. [USP 3]. Ontdek het zelf."    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ DAG 15-30: CONVERSION PUSH                                      │
│ ───────────────────────────────────────────────────────────────│
│ Audience: Visitors (15-30 days) MINUS Recent Converters        │
│ Message: Urgency, offer, direct CTA                            │
│ CTA: "Start Nu" of "Vraag Offerte" (strong)                   │
│                                                                  │
│ Headline: "Laatste Kans: Gratis Consult"                       │
│ Description: "Plan deze week uw gratis adviesgesprek."         │
└─────────────────────────────────────────────────────────────────┘

SETUP IN GOOGLE ADS:
────────────────────
1. Maak 4 audience lists met recency:
   ├── All Visitors 3 days
   ├── All Visitors 7 days
   ├── All Visitors 14 days
   └── All Visitors 30 days

2. Maak 4 ad groups met exclusions:
   ├── AG1: Target 3d, Exclude: none
   ├── AG2: Target 7d, Exclude: 3d + Converters
   ├── AG3: Target 14d, Exclude: 7d + Converters
   └── AG4: Target 30d, Exclude: 14d + Converters

3. Verschillende ads per ad group met sequence messaging
```

## Dynamic Remarketing

### Dynamic Remarketing Setup

```
DYNAMIC REMARKETING (E-commerce / Lead Gen)
═══════════════════════════════════════════

WAT IS DYNAMIC REMARKETING?
───────────────────────────
= Automatisch de juiste producten/services tonen
= Gebaseerd op wat user bekeek
= Personalized ads at scale

VEREISTEN:
──────────
□ Google Merchant Center (e-commerce) OF
□ Business data feed (services)
□ Dynamic remarketing tag met parameters
□ Responsive display ads

SETUP VOOR E-COMMERCE:
──────────────────────

1. MERCHANT CENTER FEED
───────────────────────
Zorg dat Merchant Center actief is met:
├── Product feed up-to-date
├── All products approved
└── Linked aan Google Ads

2. DYNAMIC REMARKETING TAG
──────────────────────────
Voeg product parameters toe aan pages:

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
───────────────────────────
1. New Campaign → Sales → Display
2. Campaign subtype: Display (standard)
3. Audiences: Website visitors (targeting)
4. Ads: Responsive display ads
5. Enable: "Add a data feed for personalized ads"

SETUP VOOR SERVICES (Lead Gen):
───────────────────────────────

1. BUSINESS DATA FEED
─────────────────────
Create CSV met services:

ID,Item title,Final URL,Image URL,Item description,Price
service-1,"Website Ontwikkeling","https://site.nl/websites","https://...",Omschrijving,vanaf €999
service-2,"SEO Optimalisatie","https://site.nl/seo","https://...",Omschrijving,vanaf €499

2. UPLOAD FEED
──────────────
1. Tools → Business data → +Data feed
2. Template: Custom
3. Upload CSV
4. Map fields

3. DYNAMIC TAG VOOR SERVICES
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
════════════════════════

HOE WERKT CROSS-DEVICE?
───────────────────────
User bezoekt site op mobile → later retarget op desktop
Mogelijk door:
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

2. USER-ID TRACKING (Als user inlogt)
─────────────────────────────────────
Voor sites met login:

<script>
gtag('config', 'G-XXXXXXX', {
  'user_id': 'USER_ID_HASH'
});
</script>

⚠️ Use hashed user ID, niet plain text

3. SAME ACCOUNT LINKING
───────────────────────
Zorg dat alle properties gelinked zijn:
├── GA4 ↔ Google Ads
├── YouTube ↔ Google Ads
├── Firebase ↔ Google Ads (apps)
└── Alle accounts zelfde organization

CROSS-DEVICE AUDIENCE STRATEGIE:
────────────────────────────────

Multi-device user journey:
┌────────────────────────────────────────────────────────────────┐
│                                                                 │
│  MOBILE (Discovery)          DESKTOP (Conversion)              │
│  ─────────────────          ─────────────────────              │
│                                                                 │
│  1. User ziet ad op mobile   4. Retarget op desktop            │
│  2. Bezoekt site, browst     5. Herkenning door Google         │
│  3. Verlaat (geen conv)      6. Conversie!                     │
│                                                                 │
│  ↓                                                              │
│  Remarketing list captures visit (cross-device enabled)        │
│                                                                 │
└────────────────────────────────────────────────────────────────┘

DEVICE BID ADJUSTMENTS:
───────────────────────
Combineer device bids met RLSA:

Remarketing visitors (RLSA):
├── Mobile: +20% (assist device)
├── Desktop: +30% (conversion device)
└── Tablet: +10%

Adjust based on data:
1. Segment by device in reports
2. Check conv rate per device voor RLSA
3. Adjust bids accordingly
```

## Google Ads Script: Remarketing List Health Check

```javascript
/**
 * Remarketing List Health Monitor
 *
 * Monitort:
 * - List sizes en growth
 * - List expirations
 * - Coverage vs campaigns
 *
 * Setup:
 * 1. Pas CONFIG aan
 * 2. Schedule: Wekelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Thresholds
  MIN_LIST_SIZE_SEARCH: 1000,
  MIN_LIST_SIZE_DISPLAY: 100,
  GROWTH_WARNING_THRESHOLD: -0.10, // -10% = waarschuwing

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
    body += '⚠️ WARNINGS:\n';
    body += '────────────\n';
    for (var i = 0; i < report.warnings.length; i++) {
      body += '• ' + report.warnings[i].message + '\n';
    }
    body += '\n';
  }

  body += 'LIST STATUS:\n';
  body += '────────────\n';
  for (var j = 0; j < Math.min(report.lists.length, 15); j++) {
    var list = report.lists[j];
    var status = list.status === 'OK' ? '✓' :
                 list.status === 'Display Only' ? '◐' : '✗';
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

---
name: display-campaign-optimizer
description: "Google Display Network campagne optimalisatie. Gebruik voor: (1) Responsive Display Ads setup, (2) Display placement targeting, (3) Display audience strategie, (4) Banner formaten en specs, (5) Viewability optimalisatie, (6) Brand safety configuratie. Triggers: display, banner, gdn, responsive display, placements, display network, remarketing display, programmatic."
---

# Display Campaign Optimizer

Complete gids voor Google Display Network (GDN) campagnes - van Responsive Display Ads tot placement targeting en viewability optimalisatie.

## Quick Decision Guide

```
WELK TYPE DISPLAY CAMPAIGN HEB JE NODIG?
│
├─► Doel: Remarketing / Retargeting
│   └─► STANDARD DISPLAY - REMARKETING
│       ├── Website visitor audiences
│       ├── Cart abandoners, product viewers
│       ├── Bid strategy: tCPA of Maximize Conversions
│       └── Responsive Display Ads
│
├─► Doel: Brand Awareness
│   └─► STANDARD DISPLAY - PROSPECTING
│       ├── Affinity en Custom Audiences
│       ├── Topic/Placement targeting
│       ├── Bid strategy: vCPM (viewable impressions)
│       └── Uploaded image ads + Responsive
│
├─► Doel: Conversies / Lead Gen
│   └─► SMART DISPLAY (of PMax)
│       ├── Automated targeting
│       ├── Google AI optimalisatie
│       ├── Bid strategy: tCPA
│       └── Overweeg PMax als alternatief
│
├─► Doel: App Installs
│   └─► APP CAMPAIGNS (niet Display)
│       └── Dedicated app install campaigns
│
└─► Doel: Product verkoop (E-commerce)
    └─► PERFORMANCE MAX met feeds
        └── Display als onderdeel van PMax
```

## Display Network Overzicht

### Wat is het Google Display Network?

```
GOOGLE DISPLAY NETWORK (GDN)
════════════════════════════

BEREIK:
──────
├── 35+ miljoen websites en apps
├── 90%+ van internet gebruikers wereldwijd
├── YouTube, Gmail, Google Finance, etc.
└── Mobile apps via AdMob

INVENTORY TYPES:
────────────────
┌──────────────────────────────────────────────────────────────┐
│ GOOGLE OWNED PROPERTIES                                       │
│ ├── YouTube (non-video placements)                            │
│ ├── Gmail (Promotions tab)                                    │
│ ├── Google Finance                                            │
│ └── Blogger                                                   │
├──────────────────────────────────────────────────────────────┤
│ PARTNER WEBSITES                                              │
│ ├── News sites (Nu.nl, AD.nl, etc.)                           │
│ ├── Blogs en content sites                                    │
│ ├── Forums en communities                                     │
│ └── Niche websites                                            │
├──────────────────────────────────────────────────────────────┤
│ MOBILE APPS                                                   │
│ ├── Gaming apps                                               │
│ ├── Utility apps                                              │
│ └── Social/Entertainment apps                                 │
└──────────────────────────────────────────────────────────────┘

DISPLAY VS SEARCH:
──────────────────
┌─────────────┬─────────────────────┬─────────────────────┐
│ Aspect      │ Search              │ Display             │
├─────────────┼─────────────────────┼─────────────────────┤
│ User Intent │ Actief zoekend      │ Passief browsend    │
│ Format      │ Text-based          │ Visual (image/video)│
│ Targeting   │ Keywords            │ Audiences/Context   │
│ Funnel      │ Bottom (high intent)│ Top/Mid (awareness) │
│ CTR         │ 2-10%               │ 0.1-1%              │
│ CPC         │ Hoger               │ Lager               │
│ Volume      │ Beperkt door zoeken │ Veel hoger          │
└─────────────┴─────────────────────┴─────────────────────┘
```

## Responsive Display Ads (RDA)

### RDA Asset Requirements

```
RESPONSIVE DISPLAY AD SPECIFICATIONS
════════════════════════════════════

IMAGES (Verplicht):
───────────────────
┌───────────────┬────────────┬───────────────┬─────────────────┐
│ Type          │ Ratio      │ Minimum Size  │ Aanbevolen      │
├───────────────┼────────────┼───────────────┼─────────────────┤
│ Landscape     │ 1.91:1     │ 600x314       │ 1200x628        │
│ Square        │ 1:1        │ 300x300       │ 1200x1200       │
└───────────────┴────────────┴───────────────┴─────────────────┘

AANTALLEN:
├── Landscape: 1-5 images (upload 5 voor beste performance)
├── Square: 1-5 images (upload 5 voor beste performance)
├── Maximum file size: 5MB
└── Formats: JPG, PNG, GIF (static)

LOGO (Verplicht):
─────────────────
├── Square logo: 1:1 ratio (min 128x128, aanbevolen 1200x1200)
├── Landscape logo: 4:1 ratio (min 512x128, aanbevolen 1200x300)
├── Transparante achtergrond aanbevolen
└── Maximum file size: 5MB

HEADLINES:
──────────
├── Short Headlines: 1-5 (max 30 karakters elk)
├── Long Headline: 1 (max 90 karakters)
└── Mix van USPs, CTAs, en benefits

DESCRIPTIONS:
─────────────
├── Aantal: 1-5 descriptions
├── Lengte: Max 90 karakters elk
└── Varieer met features, benefits, social proof

BUSINESS NAME:
──────────────
├── Max 25 karakters
├── Officiële merknaam
└── Geen promoties

OPTIONAL:
─────────
├── Video: Tot 5 videos (YouTube links)
├── Call to Action: Selecteer uit preset opties
└── Custom colors: Match brand kleuren
```

### RDA Voorbeeld Combinaties

```
HOE RDA's WORDEN GEASSEMBLEERD
══════════════════════════════

Google combineert je assets automatisch in verschillende formaten:

NATIVE AD (In-feed):
┌─────────────────────────────────────────────────────────┐
│  ┌─────────┐  Short Headline                           │
│  │  LOGO   │  Description text here...                 │
│  └─────────┘                        [Shop Now]         │
└─────────────────────────────────────────────────────────┘

BANNER AD (Leaderboard 728x90):
┌─────────────────────────────────────────────────────────┐
│  ┌─────────────┐  Headline Text    ┌──────────────┐    │
│  │   IMAGE     │  Description...   │  [CTA BUTTON]│    │
│  └─────────────┘                   └──────────────┘    │
└─────────────────────────────────────────────────────────┘

LARGE RECTANGLE (336x280):
┌──────────────────────────────┐
│  ┌────────────────────────┐  │
│  │                        │  │
│  │        IMAGE           │  │
│  │                        │  │
│  └────────────────────────┘  │
│  Long Headline Here          │
│  Description text...         │
│  ┌────────────────┐          │
│  │   SHOP NOW     │   LOGO   │
│  └────────────────┘          │
└──────────────────────────────┘

INTERSTITIAL (Mobile):
┌────────────────────┐
│         ×          │
│  ┌──────────────┐  │
│  │              │  │
│  │    IMAGE     │  │
│  │              │  │
│  └──────────────┘  │
│  Headline          │
│  Description       │
│  ┌──────────────┐  │
│  │  [ACTION]    │  │
│  └──────────────┘  │
└────────────────────┘
```

## Uploaded Image Ads

### Banner Formaten

```
GOOGLE DISPLAY BANNER SIZES
═══════════════════════════

TOP PERFORMING SIZES (focus hierop):
────────────────────────────────────
┌─────────────────────┬────────────────┬────────────────────┐
│ Size                │ Name           │ Typical Placement  │
├─────────────────────┼────────────────┼────────────────────┤
│ 300x250             │ Medium Rect    │ In-content, sidebar│
│ 336x280             │ Large Rect     │ In-content         │
│ 728x90              │ Leaderboard    │ Header, footer     │
│ 300x600             │ Half Page      │ Sidebar            │
│ 320x50              │ Mobile Banner  │ Mobile header      │
│ 320x100             │ Large Mobile   │ Mobile             │
└─────────────────────┴────────────────┴────────────────────┘

VOLLEDIGE LIJST (voor maximum bereik):
──────────────────────────────────────
Desktop:
├── 300x250 (Medium Rectangle) ⭐
├── 336x280 (Large Rectangle) ⭐
├── 728x90 (Leaderboard) ⭐
├── 300x600 (Half Page) ⭐
├── 160x600 (Wide Skyscraper)
├── 970x90 (Large Leaderboard)
├── 970x250 (Billboard)
├── 468x60 (Banner)
└── 250x250 (Square)

Mobile:
├── 320x50 (Mobile Leaderboard) ⭐
├── 320x100 (Large Mobile Banner) ⭐
├── 300x250 (Medium Rectangle)
└── 336x280 (Large Rectangle)

AANBEVELING:
────────────
Minimaal uploaden: 300x250, 728x90, 320x50, 300x600
Optimaal: Alle sizes met ⭐ markering
Maximum reach: Alle sizes
```

### Banner Design Best Practices

```
DISPLAY BANNER DESIGN GUIDELINES
════════════════════════════════

VISUAL HIERARCHY:
─────────────────
1. Aandachtstrekker (image/product)
2. Headline (groot, leesbaar)
3. USP/Offer (kernboodschap)
4. CTA button (contrasterende kleur)
5. Logo (herkenning)

┌─────────────────────────────────────┐
│  1. AANDACHT                        │
│  ┌─────────────────────────────┐    │
│  │     PRODUCT / IMAGE         │    │
│  └─────────────────────────────┘    │
│                                     │
│  2. HEADLINE (kort & krachtig)      │
│                                     │
│  3. USP: Gratis verzending!         │
│                                     │
│  4. ┌────────────────┐   5. [LOGO]  │
│     │  SHOP NU  ▶    │              │
│     └────────────────┘              │
└─────────────────────────────────────┘

DO's:
─────
✓ Duidelijke call-to-action
✓ Contrasterende kleuren
✓ Leesbare tekst (min 10pt op klein formaat)
✓ Animatie max 30 seconden (GIF)
✓ Brand consistent
✓ Mobile-first design

DON'Ts:
───────
✗ Te veel tekst
✗ Flitsende of afleidende animaties
✗ Misleidende elementen (nep buttons)
✗ Lage kwaliteit images
✗ Te kleine tekst
✗ Geen CTA button

FILE SPECS:
───────────
├── Formats: GIF, JPG, PNG, HTML5
├── Max file size: 150KB
├── HTML5: Max 1MB met assets
├── Animation: Max 30 sec, dan freeze
└── Audio: Niet toegestaan
```

## Targeting Strategieën

### Audience Targeting

```
DISPLAY AUDIENCE TARGETING
══════════════════════════

LAYER 1: YOUR DATA (First-Party)
────────────────────────────────
Hoogste waarde, laagste volume

□ Website Remarketing
├── All Visitors: 30, 60, 90, 180 dagen
├── Category Viewers: Bezoekers van specifieke pagina's
├── Product Viewers: Dynamische remarketing
├── Cart Abandoners: Hoogste intent
└── Converters: Cross-sell / upsell

□ Customer Match
├── Email lists uploaden
├── Phone numbers
├── Lifetime value segments
└── Exclude bestaande klanten (prospecting)

□ YouTube Viewers
├── Video viewers
├── Channel subscribers
└── Video engagers (likes, comments)

LAYER 2: SIMILAR AUDIENCES
──────────────────────────
Gebaseerd op first-party data

□ Similar to Converters
├── Vergelijkbaar met kopers
└── Hoge conversie potentieel

□ Similar to Cart Abandoners
├── Hoge koopintentie signalen
└── Mid-funnel targeting

LAYER 3: IN-MARKET AUDIENCES
────────────────────────────
Actieve koopintentie

□ In-Market Categories
├── Selecteer relevante categorieën
├── Google's intent signalen
├── Laatste 7-14 dagen actief
└── Voorbeeld: "Laptops", "Running Shoes"

LAYER 4: AFFINITY AUDIENCES
───────────────────────────
Lifestyle en interesses

□ Affinity Categories
├── Bredere targeting
├── Long-term interests
├── Goed voor awareness
└── Voorbeeld: "Tech Enthusiasts", "Fashionistas"

LAYER 5: CUSTOM AUDIENCES
─────────────────────────
Zelf gedefinieerd

□ Custom Intent
├── Keyword-based: Mensen die zoeken naar [X]
├── URL-based: Bezoekers van competitor sites
└── App-based: Gebruikers van bepaalde apps

□ Custom Affinity
├── Bredere interesse targeting
├── Combine keywords + URLs + apps
└── Audience beschrijving meegeven
```

### Content Targeting

```
DISPLAY CONTENT TARGETING
═════════════════════════

TOPICS TARGETING:
─────────────────
□ Adverteer op sites over bepaalde onderwerpen
├── Broad categories: /Autos & Vehicles
├── Subcategories: /Autos/Classic Vehicles
├── Goed voor: Contextuele relevantie
└── Risico: Beperkt bereik, minder precise

PLACEMENT TARGETING:
────────────────────
□ Specifieke websites of apps
├── URL-level: www.example.com
├── Section-level: www.example.com/tech
├── App targeting: Specifieke apps
├── YouTube channels/videos
└── Goed voor: Premium placements, brand safety

KEYWORDS (Contextual):
──────────────────────
□ Pagina's met bepaalde keywords
├── Display keywords (niet Search keywords)
├── Content matching
├── Goed voor: Thematische targeting
└── Combine met audience voor betere resultaten

TARGETING COMBINATIES:
──────────────────────
┌─────────────────────────────────────────────────────────┐
│ TARGETING APPROACH                  │ RESULT             │
├─────────────────────────────────────┼────────────────────┤
│ Audience ONLY                       │ Breed, any site    │
│ Placement ONLY                      │ Beperkt, premium   │
│ Audience + Placement                │ Sweet spot         │
│ Audience + Topics                   │ Contextueel        │
│ Keywords + Audience                 │ Zeer specifiek     │
└─────────────────────────────────────┴────────────────────┘

AANBEVELING:
────────────
Remarketing: Audience only (volg gebruiker overal)
Prospecting: Audience + Topics/Keywords
Premium: Placement targeting + Audience
```

## Placements Beheer

### Placement Performance Analyse

```
PLACEMENTS OPTIMALISATIE
════════════════════════

WAAR VIND JE PLACEMENT DATA:
────────────────────────────
Google Ads → Campaigns → [Campaign] → Placements
├── Where ads showed: Automatische placements
└── Targeted: Jouw toegevoegde placements

PLACEMENT METRICS:
──────────────────
┌────────────────────┬─────────────────────────────────────┐
│ Metric             │ Wat te zoeken                       │
├────────────────────┼─────────────────────────────────────┤
│ Impressions        │ Volume per site                     │
│ CTR                │ Engagement kwaliteit                │
│ Conversions        │ Echte waarde                        │
│ Conv Rate          │ Site kwaliteit                      │
│ Cost/Conv          │ Efficiency                          │
│ Viewability        │ Zichtbaarheid (indien beschikbaar)  │
└────────────────────┴─────────────────────────────────────┘

EXCLUSION CRITERIA:
───────────────────
Exclude placements die:
├── Hoge impressies, geen conversies, hoge spend
├── Zeer lage CTR (<0.01%)
├── Irrelevante content (brand safety)
├── Mobile gaming apps (vaak accidental clicks)
└── Low quality / MFA sites

COMMON EXCLUSIONS:
──────────────────
□ App categories om te excluden:
├── Games (tenzij relevant)
├── Comics
├── Entertainment (vaak kids content)
└── Wallpapers/Screensavers

□ Site types om te excluden:
├── Parked domains
├── Error pages
├── Below the fold only
└── Sensitive content

EXCLUSION SETUP:
────────────────
1. Campaign → Settings → Additional Settings
2. Content exclusions
3. Placements → Exclusions tab
4. Upload exclusion list of add per site
```

### Placement Exclusion Script

```javascript
/**
 * Display Placement Analyzer
 *
 * Analyseert placements en identificeert
 * low performers voor exclusion.
 *
 * Features:
 * - High spend / no conversion detection
 * - CTR anomaly detection
 * - App placement analysis
 * - Automated exclusion suggestions
 *
 * Schedule: Wekelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Thresholds voor exclusion suggestie
  MIN_COST_FOR_ANALYSIS: 5,        // Min €5 spend
  MIN_IMPRESSIONS: 100,            // Min 100 impressions
  MAX_COST_NO_CONV: 50,            // €50+ spend, 0 conversions
  MIN_CTR: 0.0005,                 // CTR < 0.05%

  // Date range
  DATE_RANGE: 'LAST_30_DAYS',

  // Exclude mobile apps by default
  EXCLUDE_APPS: true
};

function main() {
  var displayCampaigns = AdsApp.campaigns()
    .withCondition('AdvertisingChannelType = DISPLAY')
    .withCondition('Status = ENABLED')
    .get();

  var placementsToExclude = [];
  var appsToExclude = [];

  while (displayCampaigns.hasNext()) {
    var campaign = displayCampaigns.next();

    // Analyze automatic placements
    var placementReport = campaign.targeting().placements()
      .forDateRange(CONFIG.DATE_RANGE)
      .get();

    while (placementReport.hasNext()) {
      var placement = placementReport.next();
      var stats = placement.getStatsFor(CONFIG.DATE_RANGE);

      var impressions = stats.getImpressions();
      var clicks = stats.getClicks();
      var cost = stats.getCost();
      var conversions = stats.getConversions();
      var url = placement.getUrl();

      if (impressions < CONFIG.MIN_IMPRESSIONS) continue;
      if (cost < CONFIG.MIN_COST_FOR_ANALYSIS) continue;

      var ctr = clicks / impressions;
      var shouldExclude = false;
      var reason = '';

      // High spend, no conversions
      if (cost > CONFIG.MAX_COST_NO_CONV && conversions === 0) {
        shouldExclude = true;
        reason = 'High spend (€' + cost.toFixed(2) + '), 0 conversions';
      }

      // Very low CTR
      if (ctr < CONFIG.MIN_CTR && impressions > 1000) {
        shouldExclude = true;
        reason = 'Very low CTR: ' + (ctr * 100).toFixed(3) + '%';
      }

      // Mobile app detection
      if (CONFIG.EXCLUDE_APPS && url.indexOf('mobileapp::') === 0) {
        appsToExclude.push({
          campaign: campaign.getName(),
          url: url,
          cost: cost,
          impressions: impressions,
          conversions: conversions
        });
      }

      if (shouldExclude) {
        placementsToExclude.push({
          campaign: campaign.getName(),
          url: url,
          cost: cost,
          impressions: impressions,
          clicks: clicks,
          ctr: ctr,
          conversions: conversions,
          reason: reason
        });
      }
    }
  }

  // Sort by cost
  placementsToExclude.sort(function(a, b) { return b.cost - a.cost; });
  appsToExclude.sort(function(a, b) { return b.cost - a.cost; });

  // Send report
  if (placementsToExclude.length > 0 || appsToExclude.length > 0) {
    sendPlacementReport(placementsToExclude, appsToExclude);
  }

  Logger.log('Placement analysis complete.');
  Logger.log('Placements to exclude: ' + placementsToExclude.length);
  Logger.log('Apps to exclude: ' + appsToExclude.length);
}

function sendPlacementReport(placements, apps) {
  var subject = '📍 Display Placement Analysis - ' + AdsApp.currentAccount().getName();

  var body = 'Display Placement Analysis Report\n';
  body += '=================================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Period: ' + CONFIG.DATE_RANGE + '\n\n';

  if (placements.length > 0) {
    body += '❌ PLACEMENTS TO EXCLUDE (' + placements.length + '):\n';
    body += '──────────────────────────────────────\n\n';

    var totalWaste = 0;
    for (var i = 0; i < Math.min(20, placements.length); i++) {
      var p = placements[i];
      totalWaste += p.cost;
      body += '• ' + truncateUrl(p.url, 50) + '\n';
      body += '  Campaign: ' + p.campaign + '\n';
      body += '  Spend: €' + p.cost.toFixed(2);
      body += ' | Impr: ' + p.impressions;
      body += ' | Conv: ' + p.conversions + '\n';
      body += '  Reason: ' + p.reason + '\n\n';
    }

    body += 'Total potential savings: €' + totalWaste.toFixed(2) + '\n\n';
  }

  if (apps.length > 0) {
    body += '📱 MOBILE APPS TO REVIEW (' + apps.length + '):\n';
    body += '────────────────────────────────────\n\n';

    var appSpend = 0;
    for (var j = 0; j < Math.min(10, apps.length); j++) {
      var app = apps[j];
      appSpend += app.cost;
      body += '• ' + app.url.replace('mobileapp::', '') + '\n';
      body += '  Spend: €' + app.cost.toFixed(2);
      body += ' | Conv: ' + app.conversions + '\n\n';
    }

    body += 'Total app spend: €' + appSpend.toFixed(2) + '\n';
    body += 'Consider excluding app categories in campaign settings.\n\n';
  }

  body += '\n---\nGenerated by Display Placement Analyzer';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}

function truncateUrl(url, maxLength) {
  if (url.length <= maxLength) return url;
  return url.substring(0, maxLength - 3) + '...';
}
```

## Bidding & Budget

### Bid Strategieën

```
DISPLAY BIDDING STRATEGIES
══════════════════════════

┌────────────────────────┬─────────────────────┬─────────────────────┐
│ Strategy               │ Best voor           │ Vereisten           │
├────────────────────────┼─────────────────────┼─────────────────────┤
│ Manual CPC             │ Volledige controle  │ Tijd voor optimize  │
│ Enhanced CPC           │ Assisted bidding    │ Conversion tracking │
│ Maximize Clicks        │ Traffic focus       │ Geen                │
│ Maximize Conversions   │ Lead gen/sales      │ Conv tracking       │
│ Target CPA             │ Efficiency focus    │ 15+ conv/maand      │
│ Target ROAS            │ E-commerce waarde   │ Conv value tracking │
│ Viewable CPM (vCPM)    │ Brand awareness     │ Geen                │
└────────────────────────┴─────────────────────┴─────────────────────┘

STRATEGIE SELECTIE:
───────────────────

REMARKETING CAMPAIGNS:
├── Start: Maximize Conversions
├── Na 15+ conv: Target CPA (20% boven gemiddelde)
└── Optimaliseer: CPA target verlagen per 10-15%

PROSPECTING CAMPAIGNS:
├── Awareness: vCPM (viewable impressions)
├── Traffic: Maximize Clicks
└── Conversions: Target CPA (hogere target dan remarketing)

BID ADJUSTMENTS:
────────────────
Device:
├── Mobile: -20% tot +20% afhankelijk van performance
├── Tablet: Vaak -10% tot -30%
└── Desktop: Baseline

Demographics:
├── Age: Adjust per segment
├── Gender: Adjust per segment
└── Household Income: Vooral B2B relevant

Schedule:
├── Peak uren: +10-20%
└── Nacht: -20-50% of exclude
```

### Budget Allocatie

```
DISPLAY BUDGET RICHTLIJNEN
══════════════════════════

MINIMUM BUDGETTEN:
──────────────────
├── Remarketing: €20/dag minimum
├── Prospecting: €30/dag minimum
├── Beide: €50/dag totaal aanbevolen
└── Schaling: Max 20% increase per week

BUDGET VERDELING:
─────────────────
Total Display Budget: 100%

Remarketing Focus:
├── Remarketing: 60-70%
├── Prospecting: 30-40%
└── Reden: Hogere ROI op remarketing

Awareness Focus:
├── Remarketing: 30-40%
├── Prospecting: 60-70%
└── Reden: Volume en bereik prioriteit

DISPLAY VS ANDERE KANALEN:
──────────────────────────
Total Digital Budget: 100%
├── Search: 50-60%
├── Display: 15-25%
├── Social: 15-25%
└── Video: 5-15%

REMARKETING BUDGET LOGIC:
─────────────────────────
Website Traffic/maand × Conv Rate × Target CPA = Max Budget

Voorbeeld:
100.000 bezoekers × 2% remarketing eligible × €50 tCPA
= 2.000 × €50 = €100.000 potential / maand
Realistische spend: €20.000-30.000/maand
```

## Brand Safety & Viewability

### Content Exclusions

```
BRAND SAFETY SETUP
══════════════════

CONTENT EXCLUSIONS (Campaign Level):
────────────────────────────────────
Settings → Additional Settings → Content Exclusions

□ Digital Content Labels:
├── DL-G: General audiences (veiligst)
├── DL-PG: Most audiences
├── DL-T: Teen and older
├── DL-MA: Mature audiences
└── Not yet labeled

□ Sensitive Content Categories:
├── Tragedy and conflict
├── Sensitive social issues
├── Sexually suggestive content
├── Profanity and rough language
└── Shocking content

AANBEVOLEN EXCLUSIONS:
──────────────────────
Conservative brands:
├── Exclude: DL-T, DL-MA, Not labeled
├── Exclude: All sensitive categories
└── Placement review: Wekelijks

Moderate brands:
├── Exclude: DL-MA, Not labeled
├── Exclude: Tragedy, Sexually suggestive, Shocking
└── Placement review: Maandelijks

PLACEMENT TYPE EXCLUSIONS:
──────────────────────────
□ Inventory types:
├── Standard inventory (default)
├── Expanded inventory (meer volume, minder controle)
└── Limited inventory (premium only, minder volume)

□ Content types:
├── Embedded videos
├── Live streaming videos
├── Games
└── In-apps (selectief)
```

### Viewability Optimalisatie

```
VIEWABILITY METRICS
═══════════════════

WAT IS VIEWABILITY?
───────────────────
Een ad is "viewable" als:
├── Display: 50%+ pixels zichtbaar voor 1+ seconde
└── Video: 50%+ pixels zichtbaar voor 2+ seconden

INDUSTRY BENCHMARKS:
────────────────────
├── Average viewability: 50-60%
├── Good viewability: 60-70%
├── Excellent viewability: 70%+
└── Premium inventory: 80%+

VIEWABILITY VERBETEREN:
───────────────────────

1. BID STRATEGY
   └── Gebruik vCPM (viewable CPM) voor awareness

2. PLACEMENT SELECTION
   ├── Above the fold placements
   ├── Premium publishers
   └── Exclude low viewability sites

3. AD SIZE SELECTION
   ├── 300x250: Hoge viewability (in-content)
   ├── 728x90: Medium (header, kan below fold zijn)
   ├── 300x600: Hoge viewability (sticky sidebar)
   └── 320x50: Variabel (mobile header)

4. EXCLUSIONS
   ├── Exclude sites met <40% viewability
   ├── Exclude embedded placements
   └── Exclude below-the-fold only inventory

VIEWABILITY REPORT OPZETTEN:
────────────────────────────
Reports → Predefined → Display
├── Add: Active View viewable impressions
├── Add: Active View measurable impressions
├── Add: Active View viewable rate
└── Segment by: Placement
```

## Display Campaign Optimalisatie

### Optimization Checklist

```
DISPLAY OPTIMIZATION WORKFLOW
═════════════════════════════

DAGELIJKS:
──────────
□ Budget pacing check
□ Grote afwijkingen in spend/impressions
□ Disapproved ads check

WEKELIJKS:
──────────
□ Placement performance review
├── Identify high-spend, low-conv placements
├── Add exclusions
└── Find new performing placements

□ Audience performance
├── CTR en Conv Rate per audience
├── Adjust bids per audience
└── Exclude underperformers

□ Asset performance (RDA)
├── Check asset ratings
├── Replace "Low" assets
└── Add nieuwe variaties

MAANDELIJKS:
────────────
□ Creative refresh
├── Nieuwe images/banners
├── Nieuwe headlines
└── Seasonal updates

□ Audience expansion/contraction
├── Test nieuwe segments
├── Remove non-performers
└── Lookalike audiences

□ Bidding review
├── CPA trends
├── Bid adjustment optimization
└── Strategy wijzigingen

QUARTERLY:
──────────
□ Full account audit
□ Strategie herziening
□ Budget reallocation
□ Nieuwe tests plannen
```

### Performance Benchmarks

```
DISPLAY BENCHMARKS (NL/BE)
══════════════════════════

REMARKETING:
────────────
├── CTR: 0.3-0.8%
├── CPC: €0.30-0.80
├── Conv Rate: 1.5-4%
├── CPA: 20-40% lager dan prospecting
└── ROAS: Typisch hoogste van display

PROSPECTING:
────────────
├── CTR: 0.05-0.2%
├── CPC: €0.15-0.50
├── Conv Rate: 0.2-1%
├── CPA: Hoger dan remarketing
└── Focus: Volume en awareness

PER INDUSTRIE:
──────────────
┌───────────────┬───────────┬───────────┬────────────┐
│ Industry      │ CTR       │ CPC       │ Conv Rate  │
├───────────────┼───────────┼───────────┼────────────┤
│ E-commerce    │ 0.15%     │ €0.35     │ 0.8%       │
│ B2B           │ 0.08%     │ €0.80     │ 0.5%       │
│ Finance       │ 0.10%     │ €0.90     │ 0.6%       │
│ Travel        │ 0.12%     │ €0.40     │ 0.4%       │
│ Retail        │ 0.20%     │ €0.30     │ 1.0%       │
└───────────────┴───────────┴───────────┴────────────┘
```

## Output: Display Campaign Template

```markdown
# Display Campaign Plan

## Campaign Overview
- **Adverteerder:** [Naam]
- **Type:** [Remarketing / Prospecting / Both]
- **Budget:** €[X]/dag
- **Looptijd:** [Start] - [Einde]

## Campaign Structure
| Campaign | Type | Audience | Budget/dag | Bid Strategy |
|----------|------|----------|------------|--------------|
| [Naam] | Remarketing | Website visitors | €[X] | tCPA |
| [Naam] | Prospecting | In-Market + Custom | €[X] | Max Conv |

## Audience Strategy
### Remarketing
- [ ] All visitors (30d, 60d, 90d)
- [ ] Product viewers
- [ ] Cart abandoners
- [ ] Past purchasers (exclude/cross-sell)

### Prospecting
- [ ] In-Market: [Categories]
- [ ] Custom Audiences: [Keywords/URLs]
- [ ] Similar Audiences: [Based on]

## Creative Assets
### Responsive Display Ads
| Asset Type | Quantity | Status |
|------------|----------|--------|
| Landscape Images (1.91:1) | x5 | |
| Square Images (1:1) | x5 | |
| Square Logo | x1 | |
| Headlines (30 char) | x5 | |
| Long Headline (90 char) | x1 | |
| Descriptions (90 char) | x5 | |

### Uploaded Banners (Optional)
| Size | Format | Status |
|------|--------|--------|
| 300x250 | JPG/PNG | |
| 728x90 | JPG/PNG | |
| 320x50 | JPG/PNG | |
| 300x600 | JPG/PNG | |

## Brand Safety
- [ ] Content exclusions configured
- [ ] Sensitive categories excluded
- [ ] Placement exclusion list uploaded
- [ ] Mobile app categories reviewed

## Success Metrics
| Metric | Remarketing Target | Prospecting Target |
|--------|-------------------|-------------------|
| CTR | >0.4% | >0.1% |
| CPC | <€0.50 | <€0.40 |
| Conv Rate | >2% | >0.5% |
| CPA | €[X] | €[X] |

## Optimization Schedule
- Week 1: Launch, monitor delivery
- Week 2: Placement review, first exclusions
- Week 3-4: Audience optimization
- Monthly: Creative refresh, full review
```

---
name: demand-gen-planner
description: |
  Demand Gen campaign strategy and optimization. Use for: (1) Demand Gen campaign setup, (2) Discovery ads strategy, (3) Gmail ads configuration, (4) Feed-based creatives, (5) YouTube Shorts advertising, (6) Visual storytelling campaigns.
  Do NOT use for: Search campaign setup (use search-campaign-builder), Performance Max optimization (use performance-max-optimizer), or YouTube video ads strategy (use youtube-ads-strategist).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "google_ads"
  phase: "fase-5-full-funnel-automation"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---
# Demand Gen Planner

Complete guide to Google Ads Demand Gen campaigns — the successor to Discovery campaigns for visual, mid-funnel advertising on YouTube, Discover, Gmail, and YouTube Shorts.



See [decision-trees.md](references/decision-trees.md) for details.



## What is Demand Gen?

### From Discovery to Demand Gen

```
DEMAND GEN EVOLUTION (2024+)
════════════════════════════

DISCOVERY ADS (2019-2023)     →     DEMAND GEN (2024+)
────────────────────────────────────────────────────────

Placements:                    Placements (expanded):
├── YouTube Home               ├── YouTube Home
├── Discover Feed              ├── YouTube Watch Next
├── Gmail Promotions           ├── YouTube Shorts ⭐ NEW
└── Gmail Social               ├── Discover Feed
                               ├── Gmail Promotions
Formats:                       └── Gmail Social
├── Single image
├── Carousel                   Formats (expanded):
└── Product feeds              ├── Single image
                               ├── Carousel
Bidding:                       ├── Video ads ⭐ NEW
├── tCPA                       ├── Product feeds
└── Maximize conversions       └── Mixed (image + video)

                               Bidding (expanded):
                               ├── tCPA
                               ├── Maximize conversions
                               ├── tROAS ⭐ NEW
                               ├── Maximize clicks
                               └── Maximize conversion value

                               Features (new):
                               ├── Lookalike segments
                               ├── A/B creative experiments
                               └── Enhanced audience tools
```

### Where Demand Gen Ads Appear

```
DEMAND GEN PLACEMENTS
═════════════════════

1. YOUTUBE HOME FEED
   ┌─────────────────────────────────────────────────┐
   │  [YouTube Logo]                    🔍  👤       │
   │  ─────────────────────────────────────────────  │
   │  ┌──────────────────┐  ┌──────────────────┐    │
   │  │    [SUGGESTED]   │  │    [SUGGESTED]   │    │
   │  └──────────────────┘  └──────────────────┘    │
   │  ┌──────────────────────────────────────────┐  │
   │  │           YOUR DEMAND GEN AD             │  │
   │  │    ┌─────────────────────────────────┐   │  │
   │  │    │                                 │   │  │
   │  │    │         IMAGE / VIDEO           │   │  │
   │  │    │                                 │   │  │
   │  │    └─────────────────────────────────┘   │  │
   │  │    Headline - Description              Ad│  │
   │  └──────────────────────────────────────────┘  │
   └─────────────────────────────────────────────────┘

2. YOUTUBE SHORTS
   ┌────────────────────┐
   │                    │
   │   YOUR VIDEO AD    │
   │   (9:16 format)    │
   │                    │
   │ ┌────────────────┐ │
   │ │  Shop Now  ▶  │ │
   │ └────────────────┘ │
   │                    │
   │    ❤️ 💬 ➡️ 🎵    │
   └────────────────────┘

3. DISCOVER FEED (Google App)
   ┌─────────────────────────────────────────────────┐
   │  ┌──────────────────────────────────────────┐  │
   │  │           NEWS ARTICLE                   │  │
   │  └──────────────────────────────────────────┘  │
   │  ┌──────────────────────────────────────────┐  │
   │  │           YOUR DEMAND GEN AD             │  │
   │  │    ┌─────────────────────────────────┐   │  │
   │  │    │      HIGH-QUALITY IMAGE         │   │  │
   │  │    │      (1200x628 or 1200x1200)    │   │  │
   │  │    └─────────────────────────────────┘   │  │
   │  │    Headline                            Ad│  │
   │  │    Brand Name                            │  │
   │  └──────────────────────────────────────────┘  │
   │  ┌──────────────────────────────────────────┐  │
   │  │           SUGGESTED CONTENT              │  │
   │  └──────────────────────────────────────────┘  │
   └─────────────────────────────────────────────────┘

4. GMAIL PROMOTIONS TAB
   ┌─────────────────────────────────────────────────┐
   │  ☆ Ad · Brand Name                              │
   │     Your compelling headline here               │
   │     Description text that entices...            │
   │  ─────────────────────────────────────────────  │
   │  [Expanded view shows full creative]            │
   └─────────────────────────────────────────────────┘
```

## Creative Asset Requirements

### Image Assets

```
DEMAND GEN IMAGE SPECIFICATIONS
═══════════════════════════════

REQUIRED IMAGES:
────────────────
┌───────────────┬────────────┬───────────────┬──────────────────┐
│ Type          │ Ratio      │ Minimum Size  │ Recommended      │
├───────────────┼────────────┼───────────────┼──────────────────┤
│ Landscape     │ 1.91:1     │ 600x314       │ 1200x628         │
│ Square        │ 1:1        │ 300x300       │ 1200x1200        │
│ Portrait      │ 4:5        │ 480x600       │ 960x1200         │
└───────────────┴────────────┴───────────────┴──────────────────┘

RECOMMENDED QUANTITIES:
├── Landscape: 3-5 variations
├── Square: 3-5 variations
├── Portrait: 1-3 variations
└── Total: 5-15 images per asset group

IMAGE BEST PRACTICES:
─────────────────────
□ No text on >20% of image area
□ Faces and people perform well
□ Bright, high-contrast colors
□ Product clearly visible
□ No blurry or low-quality images
□ Avoid overly "stock" looking photos
□ Mobile-first design (most views are mobile)

LOGO REQUIREMENTS:
──────────────────
├── Square logo: 1200x1200 (required)
├── Landscape logo: 1200x300 (optional)
└── Transparent background recommended
```

### Video Assets

```
DEMAND GEN VIDEO SPECIFICATIONS
═══════════════════════════════

REQUIRED ASPECT RATIOS:
───────────────────────
┌───────────────┬────────────┬────────────────────────────────┐
│ Placement     │ Ratio      │ Recommended                    │
├───────────────┼────────────┼────────────────────────────────┤
│ YouTube Feed  │ 16:9       │ 1920x1080 (landscape)          │
│ YouTube Feed  │ 1:1        │ 1080x1080 (square)             │
│ YouTube Shorts│ 9:16       │ 1080x1920 (vertical) ⭐        │
│ Discover      │ 1.91:1     │ 1200x628 (auto-plays)          │
└───────────────┴────────────┴────────────────────────────────┘

VIDEO LENGTH:
─────────────
├── Minimum: 5 seconds
├── Maximum: 60 seconds (Shorts), no max (Feed)
├── Recommended: 15-30 seconds
└── Shorts specific: 15-45 seconds

VIDEO BEST PRACTICES:
─────────────────────
□ Hook in the first 3 seconds
□ Brand visible within first 5 sec
□ Works without sound (add captions!)
□ Vertical video for Shorts
□ CTA both visual and verbal
□ Mobile-first design

VIDEO CONTENT IDEAS:
────────────────────
├── Product demos
├── Unboxing content
├── Before/After
├── User testimonials
├── Behind the scenes
└── Quick tutorials
```

### Text Assets

```
DEMAND GEN TEXT REQUIREMENTS
════════════════════════════

HEADLINES:
──────────
├── Quantity: 3-5 required (max 5)
├── Length: 1-40 characters
├── Best practices:
│   ├── Vary between short and long
│   ├── Include CTA in at least 1
│   ├── Use numbers/percentages
│   └── Test emotional vs rational

LONG HEADLINES:
───────────────
├── Quantity: 1-5 (recommended 3)
├── Length: 1-90 characters
├── Usage: Discovery and Gmail placements
└── More room for storytelling

DESCRIPTIONS:
─────────────
├── Quantity: 3-5 required
├── Length: 1-90 characters
├── Best practices:
│   ├── Unique selling points
│   ├── Call-to-action
│   ├── Urgency (where appropriate)
│   └── Social proof

BUSINESS NAME:
──────────────
├── Length: Max 25 characters
├── Consistency: Same as brand
└── No promotions in name

EXAMPLE ASSET SET:
──────────────────
Headlines:
├── "Shop the Summer Collection"         (27 chars)
├── "50% Off - This Weekend Only"        (29 chars)
├── "Free Shipping on Orders €50+"       (30 chars)
├── "Bestsellers Now on Sale"            (24 chars)
└── "New Arrivals: Limited Edition"      (29 chars)

Long Headlines:
├── "Discover the latest trends in sustainable fashion - Shop now at 50% off" (72 chars)
├── "From sporty to elegant: find your perfect look in our collection" (65 chars)
└── "Thousands of happy customers before you - Check our reviews" (59 chars)

Descriptions:
├── "Premium quality at affordable prices. Order today, delivered tomorrow." (70 chars)
├── "Sustainably produced in Europe. 30-day money-back guarantee." (60 chars)
├── "Join 50,000+ satisfied customers. Free returns." (48 chars)
└── "Exclusive designs you won't find anywhere else. Shop now!" (57 chars)
```

## Campaign Setup

### Step-by-Step Setup

```
DEMAND GEN CAMPAIGN SETUP
══════════════════════════

STEP 1: CREATE CAMPAIGN
────────────────────────
Google Ads → + New Campaign
├── Goal: Sales / Leads / Website Traffic
├── Campaign type: Demand Gen
└── Campaign name: [Brand] - Demand Gen - [Audience/Goal]

STEP 2: CAMPAIGN SETTINGS
──────────────────────────
□ Locations: [Your target locations]
□ Languages: [Target languages]
□ Bidding:
│ ├── New accounts: Maximize Conversions
│ ├── 50+ conv/month: Target CPA
│ └── E-commerce: Target ROAS
□ Budget: €[X]/day (min €30 recommended)

STEP 3: AUDIENCE TARGETING
───────────────────────────
□ Custom Segments (keywords + URLs)
□ Your Data (remarketing + customer match)
□ Interests & Demographics
□ Lookalike Segments (new in Demand Gen)
□ Optimized Targeting: On/Off

STEP 4: AD GROUPS & ADS
────────────────────────
□ Create ad group per audience segment
□ Upload assets:
│ ├── Images: Landscape + Square + Portrait
│ ├── Videos: Horizontal + Square + Vertical
│ ├── Logos: Square (required)
│ ├── Headlines: 5 items
│ ├── Long Headlines: 3 items
│ └── Descriptions: 5 items
□ Final URL: Landing page
□ Call to Action: Select appropriate CTA

STEP 5: PRODUCT FEEDS (Optional)
─────────────────────────────────
□ Link Merchant Center
□ Select product groups
□ Enable product cards in ads
```

### Audience Strategies

```
DEMAND GEN AUDIENCE TARGETING
═════════════════════════════

LAYER 1: YOUR DATA (First-Party)
─────────────────────────────────
Highest value, lowest volume

□ Customer Match
├── All Customers
├── High-Value Customers (top 20%)
├── Lapsed Customers (>6 months)
└── Newsletter Subscribers

□ Website Remarketing
├── All Visitors (180 days)
├── Product Viewers (90 days)
├── Cart Abandoners (30 days)
├── Past Purchasers (365 days)
└── Video Viewers (YouTube)

□ App Users
├── All App Users
├── In-App Purchasers
└── Lapsed App Users

LAYER 2: LOOKALIKE SEGMENTS ⭐ NEW
───────────────────────────────────
Based on your first-party data

□ Lookalike: Purchasers
├── Similarity: Narrow (2.5%) → Broad (10%)
└── Best for: Acquisition with conversion focus

□ Lookalike: High-Value Customers
├── Similarity: Narrow for quality
└── Best for: Premium acquisition

□ Lookalike: Engaged Visitors
├── Similarity: Broad for volume
└── Best for: Awareness expansion

LAYER 3: GOOGLE AUDIENCES
──────────────────────────
Medium value, high volume

□ In-Market Segments
├── Active purchase intent
├── Select 5-10 relevant categories
└── Combine with demographics

□ Affinity Audiences
├── Lifestyle and interests
├── Broader reach
└── Good for awareness

□ Life Events
├── Moving, Graduating, etc.
├── Small but high intent
└── Time-sensitive

LAYER 4: CUSTOM SEGMENTS
─────────────────────────
Self-defined

□ Keyword-based
├── People who search for [X]
├── Use Search query data
└── Competitor brand names

□ URL-based
├── Visitors of competitor sites
├── Industry publications
└── Review sites

OPTIMIZED TARGETING:
────────────────────
├── ON: Google finds additional converters
│   └── Good for scaling, less control
└── OFF: Strict targeting on your audiences
    └── Good for brand safety, less volume
```

## Lookalike Segments (New)

### Lookalike Setup

```
LOOKALIKE SEGMENTS IN DEMAND GEN
═════════════════════════════════

WHAT ARE LOOKALIKE SEGMENTS?
────────────────────────────
Google finds new users who resemble your
existing customers/visitors (comparable to
Meta Lookalike Audiences).

SEED AUDIENCES (Source):
────────────────────────
□ Customer Match lists (minimum 1000 users)
□ Website visitor lists (minimum 1000 users)
□ App user lists
□ YouTube engaged viewers

LOOKALIKE SETTINGS:
───────────────────
┌─────────────┬──────────────┬────────────────────┐
│ Setting     │ Reach        │ When to use        │
├─────────────┼──────────────┼────────────────────┤
│ Narrow      │ ~2.5%        │ High quality,      │
│             │              │ limited volume     │
├─────────────┼──────────────┼────────────────────┤
│ Balanced    │ ~5%          │ Good balance       │
│             │              │ (recommended start)│
├─────────────┼──────────────┼────────────────────┤
│ Broad       │ ~10%         │ Maximum volume,    │
│             │              │ lower precision    │
└─────────────┴──────────────┴────────────────────┘

BEST PRACTICES:
───────────────
├── Seed size: Minimum 1000, ideal 10,000+
├── Seed quality: Use converters, not all visitors
├── Start: Balanced, test Narrow for higher value
├── Segment: Create separate lookalikes for different seeds
└── Exclude: Always exclude existing customers

LOOKALIKE STRATEGY:
───────────────────
Campaign 1: Lookalike Purchasers (Narrow)
├── Highest quality new customers
├── tCPA: Base target
└── Budget: 40% of acquisition budget

Campaign 2: Lookalike Purchasers (Balanced)
├── Scale with quality
├── tCPA: +15% vs Narrow
└── Budget: 40% of acquisition budget

Campaign 3: Lookalike Engaged (Broad)
├── Volume and awareness
├── Maximize Clicks or lower tCPA
└── Budget: 20% of acquisition budget
```

## Bidding & Budget Strategies

### Bid Strategy Selection

```
DEMAND GEN BID STRATEGIES
═════════════════════════

┌──────────────────────┬─────────────────────┬─────────────────────┐
│ Strategy             │ When to use         │ Requirements        │
├──────────────────────┼─────────────────────┼─────────────────────┤
│ Maximize Conversions │ New campaigns,      │ Conversion tracking │
│                      │ <30 conv/month      │ active              │
├──────────────────────┼─────────────────────┼─────────────────────┤
│ Target CPA           │ 30+ conv/month,     │ Stable CPA          │
│                      │ lead gen focus      │ history             │
├──────────────────────┼─────────────────────┼─────────────────────┤
│ Maximize Conv Value  │ E-commerce, variable│ Conv value tracking │
│                      │ order values        │                     │
├──────────────────────┼─────────────────────┼─────────────────────┤
│ Target ROAS          │ E-commerce with     │ 50+ conv/month,     │
│                      │ value tracking      │ stable ROAS         │
├──────────────────────┼─────────────────────┼─────────────────────┤
│ Maximize Clicks      │ Awareness,          │ No specific         │
│                      │ traffic focus       │ requirements        │
└──────────────────────┴─────────────────────┴─────────────────────┘

BID STRATEGY EVOLUTION:
───────────────────────
Week 1-2: Maximize Conversions (gather data)
    ↓
Week 3-4: Evaluate performance
    ↓
≥30 conv → Switch to tCPA (start 20% above average)
    ↓
Optimize tCPA: -10% every 2 weeks if stable
```

### Budget Allocation

```
DEMAND GEN BUDGET GUIDELINES
═════════════════════════════

MINIMUM BUDGETS:
────────────────
├── Absolute minimum: €20/day
├── Recommended start: €50/day
├── Optimal for learning: €100/day
└── Scaling: €200+/day

BUDGET PER AUDIENCE TYPE:
─────────────────────────
┌────────────────────────┬────────────┬──────────────────────┐
│ Audience               │ Budget %   │ Expected CPA         │
├────────────────────────┼────────────┼──────────────────────┤
│ Remarketing            │ 30%        │ Lowest               │
│ Lookalike (Narrow)     │ 25%        │ Medium-Low           │
│ Lookalike (Balanced)   │ 25%        │ Medium               │
│ In-Market + Custom     │ 20%        │ Medium-High          │
└────────────────────────┴────────────┴──────────────────────┘

BUDGET VS SEARCH/PMAX:
──────────────────────
Total Digital Budget: 100%
├── Search: 40-50%
├── Performance Max: 30-40%
└── Demand Gen: 10-20%

If Demand Gen performs well:
├── Search: 35-40%
├── Performance Max: 30-35%
└── Demand Gen: 25-30%
```

## Performance Optimization

### Key Metrics

```
DEMAND GEN METRICS & BENCHMARKS
════════════════════════════════

PRIMARY METRICS:
────────────────
├── CTR (Click-Through Rate)
│   ├── Benchmark: 0.5-2.0%
│   ├── Gmail: 1.0-3.0%
│   └── YouTube/Discover: 0.3-1.5%
│
├── CPC (Cost Per Click)
│   ├── Benchmark: €0.30-1.00
│   ├── B2C: €0.20-0.60
│   └── B2B: €0.50-2.00
│
├── Conversion Rate
│   ├── Benchmark: 1-3%
│   ├── Remarketing: 3-8%
│   └── Prospecting: 0.5-2%
│
└── CPA / ROAS
    ├── Compare with Search/PMax
    ├── Demand Gen typically 10-30% higher CPA
    └── But brings incremental volume

SECONDARY METRICS:
──────────────────
├── Impressions: Reach indicator
├── Video Views: Engagement (video ads)
├── View Rate: Video completion %
└── Engagement Rate: Interactions/impressions

ASSET PERFORMANCE:
──────────────────
├── Best: Keep and create variations
├── Good: Monitor, no action needed
├── Low: Replace after 2-3 weeks
└── Pending: Wait for data
```

### Optimization Checklist

```
DEMAND GEN OPTIMIZATION WORKFLOW
═════════════════════════════════

WEEK 1: LAUNCH & MONITOR
─────────────────────────
□ Verify delivery (impressions coming in?)
□ Check asset status (all approved?)
□ Monitor budget pacing
□ No changes (learning phase)

WEEK 2: INITIAL ASSESSMENT
───────────────────────────
□ Review CTR per placement
□ Check CPC vs expectations
□ Identify underperforming assets
□ Minor bid adjustments only

WEEK 3-4: OPTIMIZATION
───────────────────────
□ Replace "Low" performing assets
□ Add new creative variations
□ Adjust bid targets (if needed)
□ Test new audiences

MONTHLY ROUTINE:
────────────────
□ Full asset performance review
□ Refresh 20-30% of creatives
□ Audience performance analysis
□ Budget reallocation
□ A/B test new concepts

OPTIMIZATION PRIORITY:
──────────────────────
1. Creative/Assets (biggest impact)
2. Audience targeting
3. Bid strategy
4. Budget allocation
5. Campaign structure
```



See [detailed-reference.md](references/detailed-reference.md) for details.



## Demand Gen vs Other Campaign Types

```
DEMAND GEN POSITIONING
═══════════════════════

┌─────────────────┬───────────────┬───────────────┬───────────────┐
│ Aspect          │ Search        │ Demand Gen    │ PMax          │
├─────────────────┼───────────────┼───────────────┼───────────────┤
│ User Intent     │ High (active) │ Medium        │ Mixed         │
│ Placements      │ Search only   │ YouTube,      │ All Google    │
│                 │               │ Discover,     │ properties    │
│                 │               │ Gmail         │               │
│ Creative        │ Text-based    │ Visual-first  │ Mixed         │
│ Control         │ High          │ Medium        │ Low           │
│ Best for        │ Bottom funnel │ Mid funnel    │ Full funnel   │
│ Typical CPA     │ Baseline      │ +10-30%       │ -10% to +10% │
└─────────────────┴───────────────┴───────────────┴───────────────┘

WHEN TO ADD DEMAND GEN:
───────────────────────
✓ Search is optimized (hitting targets)
✓ PMax running stable
✓ You have visually strong assets
✓ You want mid-funnel presence
✓ You have remarketing audiences
✗ Not if you don't have conversion tracking yet
✗ Not if Search isn't profitable yet
```

## Output: Demand Gen Campaign Template

```markdown
# Demand Gen Campaign Plan

## Campaign Overview
- **Advertiser:** [Name]
- **Campaign Goal:** [Awareness/Consideration/Conversions]
- **Budget:** €[X]/day
- **Duration:** [Start] - [End]

## Target Audiences
### Remarketing
- [ ] All visitors (180d)
- [ ] Product viewers (90d)
- [ ] Cart abandoners (30d)
- [ ] Past purchasers

### Lookalike Segments
- [ ] Lookalike: Purchasers (Balanced)
- [ ] Lookalike: High-Value Customers (Narrow)

### Google Audiences
- [ ] In-Market: [Categories]
- [ ] Custom Segment: [Keywords/URLs]

## Creative Assets
### Images Needed
- [ ] Landscape (1.91:1): x3 variations
- [ ] Square (1:1): x3 variations
- [ ] Portrait (4:5): x2 variations
- [ ] Logo square: 1200x1200

### Videos Needed
- [ ] Horizontal (16:9): x2 variations
- [ ] Square (1:1): x1 variation
- [ ] Vertical (9:16): x2 variations (Shorts)

### Text Assets
| Type | Asset 1 | Asset 2 | Asset 3 |
|------|---------|---------|---------|
| Headline | | | |
| Long Headline | | | |
| Description | | | |

## Bid Strategy
- **Initial:** Maximize Conversions
- **Target (after 30 conv):** tCPA €[X] / tROAS [X]%

## Success Metrics
| Metric | Target | Review Cadence |
|--------|--------|----------------|
| CTR | >0.8% | Weekly |
| CPA | <€[X] | Weekly |
| ROAS | >[X]x | Weekly |
| Conv Rate | >[X]% | Monthly |

## Optimization Schedule
- Week 1: Monitor, no changes
- Week 2: Asset performance review
- Week 3-4: Optimize underperformers
- Monthly: Creative refresh (20-30%)
```

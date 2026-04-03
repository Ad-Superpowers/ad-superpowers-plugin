---
name: pmax-asset-group-optimizer
description: |
  Optimizes Performance Max asset groups for structure, performance, audience signals, listing groups, search themes, and creative testing. Use when: asset group structure strategy, asset performance analysis, audience signals optimization, listing groups configuration, search themes setup, creative testing in PMax. Do NOT use for: standard Search/Display campaign setup (use search-campaign-builder), bid strategy selection (use learning-phase-tracker).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "google_ads"
  phase: "fase-5-full-funnel-automation"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---
# Performance Max Asset Group Optimizer

Complete guide for optimizing Performance Max asset groups — from structure and audience signals to creative testing and feed optimization.



See [decision-trees.md](references/decision-trees.md) for details.



## Asset Group Fundamentals

### What Is an Asset Group?

```
ASSET GROUP STRUCTURE
═════════════════════

┌─────────────────────────────────────────────────────────────────┐
│  PERFORMANCE MAX CAMPAIGN                                        │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  ASSET GROUP 1: "Winter Jackets"                          │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │  ASSETS                                             │  │  │
│  │  │  ├── Headlines (5-15)                               │  │  │
│  │  │  ├── Long Headlines (1-5)                           │  │  │
│  │  │  ├── Descriptions (2-5)                             │  │  │
│  │  │  ├── Images (3-20)                                  │  │  │
│  │  │  ├── Logos (1-5)                                    │  │  │
│  │  │  └── Videos (0-5)                                   │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │  AUDIENCE SIGNALS                                   │  │  │
│  │  │  ├── Custom Segments (keywords, URLs)               │  │  │
│  │  │  ├── Your Data (remarketing, customer match)        │  │  │
│  │  │  └── Google Audiences (in-market, affinity)         │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │  SEARCH THEMES (Optional)                           │  │  │
│  │  │  ├── "winter jacket women"                          │  │  │
│  │  │  ├── "warm jacket buy"                              │  │  │
│  │  │  └── "parka winter"                                 │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │  LISTING GROUP (E-commerce)                         │  │  │
│  │  │  └── Products: Category = Winter Jackets            │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │  FINAL URL                                          │  │  │
│  │  │  └── https://example.com/winter-jackets             │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  ASSET GROUP 2: "Rainwear"                                │  │
│  │  [Similar structure...]                                   │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Asset Group Strategy

```
ASSET GROUP STRUCTURING
═══════════════════════

OPTION 1: CATEGORY-BASED (Most common)
───────────────────────────────────────
├── AG: Women's Clothing
├── AG: Men's Clothing
├── AG: Children's Clothing
└── AG: Accessories

Advantages:
✓ Logical structure
✓ Relevant assets per category
✓ Clear performance per category

OPTION 2: MARGIN-BASED (Profit focus)
────────────────────────────────────
├── AG: High Margin Products (Custom Label)
├── AG: Standard Margin Products
└── AG: Clearance/Sale Items

Advantages:
✓ Budget toward profitable items
✓ Different bid targets per AG
✓ Focus on profitability

OPTION 3: FUNNEL-BASED (Customer journey)
────────────────────────────────────────
├── AG: New Customers (prospecting assets)
├── AG: Retargeting (remarketing focus)
└── AG: Cross-sell (existing customers)

Advantages:
✓ Messaging per funnel stage
✓ Audience signals aligned
✓ Clear performance per stage

OPTION 4: PERFORMANCE-BASED (Data-driven)
────────────────────────────────────────
├── AG: Top Performers (best ROAS)
├── AG: Potential Winners (testing)
└── AG: Long Tail (volume)

Advantages:
✓ Focus on proven winners
✓ Clear A/B testing structure
✓ Easy scaling decisions

HYBRID APPROACH (Recommended):
─────────────────────────────
├── AG: Bestsellers (top 20 products)
├── AG: Category A - High Margin
├── AG: Category B - Standard
├── AG: Category C - Standard
└── AG: Sale/Clearance
```

## Asset Performance Ratings

### Understanding Asset Ratings

```
ASSET PERFORMANCE RATINGS EXPLAINED
═══════════════════════════════════

RATING SYSTEM:
──────────────
┌─────────────┬─────────────────────────────────────────────────┐
│ Rating      │ Meaning                                         │
├─────────────┼─────────────────────────────────────────────────┤
│ Best        │ Top performer, outperforms other assets         │
│             │ → Keep running, create similar variations       │
├─────────────┼─────────────────────────────────────────────────┤
│ Good        │ Performs well, average or better                │
│             │ → Keep running, monitor for changes             │
├─────────────┼─────────────────────────────────────────────────┤
│ Low         │ Underperforms vs other assets                   │
│             │ → Replace after 30 days of consistent Low       │
├─────────────┼─────────────────────────────────────────────────┤
│ Pending     │ Not enough data for rating yet                  │
│             │ → Wait, no action needed                        │
└─────────────┴─────────────────────────────────────────────────┘

WHERE TO FIND:
──────────────
Campaign → Asset Groups → [Asset Group] → Asset Performance

IMPORTANT NOTES:
────────────────
⚠️ Ratings are RELATIVE within your asset group
   "Low" doesn't mean bad, just worse than others

⚠️ Keep at least 3-5 assets of each type
   Otherwise no comparison is possible

⚠️ Wait at least 2-3 weeks for reliable ratings
   Replacing too soon disrupts learning
```

### Asset Optimization Workflow

```
ASSET OPTIMIZATION CYCLE
════════════════════════

WEEK 1-2: LEARNING PHASE
────────────────────────
□ Upload all assets (maximum amounts)
□ Make no changes
□ Ratings still "Pending" or unstable
□ Focus on delivery and basics

WEEK 3-4: FIRST ANALYSIS
────────────────────────
□ Check asset ratings
□ Identify first "Low" performers
□ No removals yet
□ Note trends

WEEK 5-6: FIRST OPTIMIZATION
─────────────────────────────
□ Replace assets that are consistently "Low"
□ Add variations of "Best" assets
□ Test new concepts
□ Monitor impact

MONTHLY: ONGOING OPTIMIZATION
──────────────────────────────
□ Full asset review
□ Replace 20-30% of assets (refresh)
□ Seasonal updates
□ A/B test new concepts

REPLACEMENT RULES:
──────────────────
┌────────────────────────────────────────────────────────────────┐
│ Asset Rating │ Duration │ Action                              │
├──────────────┼──────────┼─────────────────────────────────────┤
│ Low          │ >30 days │ Replace                             │
│ Low          │ <30 days │ Monitor, don't replace yet          │
│ Good         │ Any      │ Keep, optionally test variations    │
│ Best         │ Any      │ Keep, create similar variations     │
│ Pending      │ Any      │ Wait for more data                  │
└──────────────┴──────────┴─────────────────────────────────────┘
```

## Asset Requirements & Best Practices

### Complete Asset Checklist

```
ASSET GROUP ASSET REQUIREMENTS
══════════════════════════════

HEADLINES (Required)
────────────────────
├── Minimum: 3 headlines
├── Recommended: 5-15 headlines
├── Maximum: 15 headlines
├── Length: Max 30 characters
└── Best practices:
    ├── Mix of USPs, CTAs, features
    ├── Include brand name in 1-2
    ├── Vary in length (short and long)
    ├── Test numbers/percentages
    └── No repetition

LONG HEADLINES (Required)
─────────────────────────
├── Minimum: 1 long headline
├── Recommended: 3-5 long headlines
├── Maximum: 5 long headlines
├── Length: Max 90 characters
└── Best practices:
    ├── Storytelling possible
    ├── More context than headlines
    ├── Include CTA
    └── Used in larger placements

DESCRIPTIONS (Required)
───────────────────────
├── Minimum: 2 descriptions
├── Recommended: 4-5 descriptions
├── Maximum: 5 descriptions
├── Length: Max 90 characters
└── Best practices:
    ├── First description = best hook
    ├── Vary: benefits, features, social proof
    ├── No repetition of headlines
    └── Include urgency where relevant

IMAGES (Required)
─────────────────
├── Minimum: 1 landscape + 1 square
├── Recommended: 3-5 of each type
├── Maximum: 20 images total
├── Formats:
│   ├── Landscape (1.91:1): 1200x628 recommended
│   ├── Square (1:1): 1200x1200 recommended
│   └── Portrait (4:5): 960x1200 recommended
└── Best practices:
    ├── Mix product shots and lifestyle
    ├── No text on >20% of image
    ├── High quality (no blur)
    ├── Faces perform well
    └── Mobile-first design

LOGOS (Required)
────────────────
├── Square logo (1:1): Min 128x128, recommended 1200x1200
├── Landscape logo (4:1): Min 512x128, recommended 1200x300
└── Transparent background recommended

VIDEOS (Optional but recommended)
─────────────────────────────────
├── Minimum: 0 (not required)
├── Recommended: 1-3 videos
├── Maximum: 5 videos
├── Formats:
│   ├── Landscape (16:9)
│   ├── Square (1:1)
│   └── Vertical (9:16) for Shorts
├── Length: 10 sec - 3 min (15-30 sec recommended)
└── Best practices:
    ├── Hook in first 3 seconds
    ├── Brand in first 5 seconds
    ├── Works without sound (subtitles!)
    └── CTA visual and verbal

⚠️ NO VIDEO UPLOAD = GOOGLE MAKES AUTO-VIDEO
   Google can automatically create videos from your images.
   This is often less effective than your own videos.
```

### Asset Variation Strategy

```
ASSET VARIATION BEST PRACTICES
══════════════════════════════

HEADLINE VARIATION:
───────────────────
Type 1: Brand Headlines
├── "[Brand] Official Store"
├── "Shop [Brand] Online"
└── "[Brand] - Since 2010"

Type 2: USP Headlines
├── "Free Shipping Above $50"
├── "100-Day Return Policy"
└── "Handmade in USA"

Type 3: Benefit Headlines
├── "Premium Quality"
├── "Sustainable Materials"
└── "Designed for Comfort"

Type 4: Action Headlines
├── "Shop Now & Save"
├── "Discover Our Collection"
└── "Get Yours Today"

Type 5: Offer Headlines
├── "Up to 50% Off"
├── "New Arrivals"
└── "Bestsellers Collection"

IMAGE VARIATION:
───────────────
Type 1: Product Only
├── Clean product shot
├── White background
└── Multiple angles

Type 2: Lifestyle
├── Product in use
├── Model wearing/using
└── Environment context

Type 3: Detail Shots
├── Close-up features
├── Material texture
└── Unique details

Type 4: Seasonal/Promotional
├── Sale imagery
├── Holiday themes
└── Limited edition visuals

VIDEO VARIATION:
───────────────
Type 1: Product Demo
├── How it works
├── Features showcase
└── Unboxing

Type 2: Testimonial
├── Customer reviews
├── Before/after
└── Social proof

Type 3: Brand Story
├── Company values
├── Behind the scenes
└── Founder story

Type 4: Quick Promo
├── Sale announcement
├── New arrivals
└── Limited offer
```

## Audience Signals Optimization

### Audience Signal Strategy

```
AUDIENCE SIGNALS IN PMAX
════════════════════════

⚠️ IMPORTANT NUANCE:
────────────────────────
Audience Signals = HINTS for Google AI
Audience Signals ≠ Targeting restrictions

Google WILL advertise beyond your signals if it
expects better results. Signals accelerate the
learning phase and provide direction.

SIGNAL TYPES:
─────────────
┌─────────────────────┬─────────────────────────────────────────┐
│ Signal Type         │ Best for                                │
├─────────────────────┼─────────────────────────────────────────┤
│ Custom Segments     │ Competitor targeting, niche interests   │
│ Your Data           │ Remarketing, Customer Match (strongest) │
│ Interests & Details │ Broad targeting, demographics           │
└─────────────────────┴─────────────────────────────────────────┘

SIGNAL PRIORITY (Strongest → Weakest):
──────────────────────────────────────
1. Your Data: Customer Match (converters)
2. Your Data: Website remarketing (high intent)
3. Custom Segments: Keywords (competitor/product)
4. Custom Segments: URLs (competitor sites)
5. In-Market Audiences
6. Affinity Audiences
7. Demographics
```

### Audience Signal Setup per Asset Group

```
AUDIENCE SIGNALS CONFIGURATION
══════════════════════════════

ASSET GROUP: BESTSELLERS
────────────────────────
Your Data:
├── Customer Match: All Purchasers
├── Remarketing: Product Viewers (90d)
└── Remarketing: Cart Abandoners (30d)

Custom Segments:
├── Keywords: [top product names], [category]
└── URLs: Competitor product pages

Interests:
├── In-Market: [Relevant category]
└── Affinity: [Relevant interest]

ASSET GROUP: PROSPECTING / NEW CUSTOMERS
────────────────────────────────────────
Your Data:
├── Similar: Lookalike Purchasers
└── EXCLUDE: Past purchasers (Customer Match)

Custom Segments:
├── Keywords: Generic product searches
└── URLs: Review sites, comparison sites

Interests:
├── In-Market: Broad category
└── Life Events: Relevant events (moving, etc.)

ASSET GROUP: HIGH-VALUE / PREMIUM
─────────────────────────────────
Your Data:
├── Customer Match: High-LTV Customers (top 20%)
├── Similar: Based on high-value customers
└── Remarketing: Premium product viewers

Custom Segments:
├── Keywords: Premium brand names
└── URLs: Luxury competitor sites

Interests:
├── Demographics: Household Income (top 10-20%)
└── In-Market: Premium subcategories
```



See [decision-trees.md](references/decision-trees.md) for details.



## Listing Groups (E-commerce)

### Listing Group Configuration

```
LISTING GROUPS FOR SHOPPING
════════════════════════════

WHAT ARE LISTING GROUPS:
────────────────────────
Listing Groups determine which products from your Merchant
Center feed belong to which Asset Group.

DEFAULT STRUCTURE:
──────────────────
Campaign: PMax
└── Asset Group: All Products
    └── Listing Group: All products (default)

SEGMENTED STRUCTURE:
────────────────────
Campaign: PMax
├── Asset Group: Winter Jackets
│   └── Listing Group: Category = Winter Jackets
│
├── Asset Group: Summer Jackets
│   └── Listing Group: Category = Summer Jackets
│
└── Asset Group: Accessories
    └── Listing Group: Category = Accessories

LISTING GROUP ATTRIBUTES:
─────────────────────────
├── Category (Google Product Category)
├── Brand
├── Condition (new, used, refurbished)
├── Item ID (specific products)
├── Product Type (custom hierarchy)
└── Custom Labels (0-4)

CUSTOM LABELS STRATEGY:
───────────────────────
Custom Label 0: Margin Level
├── High Margin
├── Medium Margin
└── Low Margin

Custom Label 1: Performance Tier
├── Bestseller
├── Rising Star
└── Long Tail

Custom Label 2: Seasonal
├── Spring
├── Summer
├── Fall
├── Winter

Custom Label 3: Promo Status
├── Full Price
├── On Sale
└── Clearance

Custom Label 4: Stock Level
├── In Stock
├── Low Stock
└── Pre-order
```

### Listing Group Optimization

```
LISTING GROUP OPTIMIZATION
══════════════════════════

STEP 1: ANALYSIS
─────────────────
Check product performance:
├── Campaigns → Products → Product Performance
├── Sort by Conversions, ROAS, Spend
└── Identify top 20% and bottom 20%

STEP 2: SEGMENTATION DECISION
──────────────────────────────
Top performers (top 20%):
├── Own asset group with higher budget
├── Specific assets (product images)
└── Premium audience signals

Mid performers (60%):
├── Category-based asset groups
├── Standard bid targets
└── Broad audience signals

Low performers (bottom 20%):
├── Evaluate: exclude or improve?
├── Check feed quality
├── Lower priority / budget

STEP 3: EXCLUSIONS
──────────────────
Products to exclude:
├── Out of stock (automatic via feed)
├── Low margin (below break-even)
├── Poor quality score in feed
├── Seasonally irrelevant
└── Competitive disadvantage (price too high)

HOW TO EXCLUDE:
───────────────
Asset Group → Listing Group → Subdivide
├── Select attribute
├── Choose values to EXCLUDE
└── Or use Custom Labels
```

## Search Themes Optimization

### Search Themes Strategy

```
SEARCH THEMES IN PMAX
═════════════════════

WHAT ARE SEARCH THEMES:
───────────────────────
Keywords you give PMax to help it understand
which search queries are relevant.

DIFFERENCE FROM SEARCH KEYWORDS:
────────────────────────────────
Search Campaign Keywords: Exact match/phrase targeting
PMax Search Themes: Hints for AI, no guarantee

HOW MANY SEARCH THEMES:
───────────────────────
├── Minimum: None (optional)
├── Recommended: 3-7 per asset group
├── Maximum: 25 per asset group
└── Too many = too broad, too few = missed opportunities

SEARCH THEMES TYPES:
────────────────────
Type 1: Branded
├── "[Brand name]"
├── "[Brand] + product"
└── Brand + category

Type 2: Generic Product
├── "[Product type]"
├── "[Category]"
└── "Buy [product]"

Type 3: Long-tail
├── "[Product] for [use case]"
├── "Best [product] 2025"
└── "[Product] comparison"

Type 4: Problem-solving
├── "How to fix [problem]"
├── "[Problem] solution"
└── "What helps with [issue]"
```

### Search Themes per Asset Group

```
SEARCH THEMES EXAMPLES
═══════════════════════

ASSET GROUP: WOMEN'S WINTER JACKETS
────────────────────────────────────
1. "winter jacket women"
2. "warm jacket buy"
3. "[brand] winter jackets"
4. "parka women winter"
5. "winter jacket waterproof"
6. "long winter jacket women"
7. "women's coat warm"

ASSET GROUP: RUNNING SHOES
──────────────────────────
1. "running shoes"
2. "best running shoes"
3. "[brand] running"
4. "best running shoes 2025"
5. "running shoes beginners"
6. "running shoes cushioning"

ASSET GROUP: B2B SOFTWARE
─────────────────────────
1. "crm software"
2. "customer management system"
3. "sales automation tool"
4. "[brand] crm"
5. "crm for small business"
6. "customer relationship software"

UPDATING SEARCH THEMES:
───────────────────────
Monthly:
├── Check Search Terms report
├── Identify new converting terms
├── Add high-performers
├── Remove non-performers
└── Monitor brand vs non-brand ratio
```



See [detailed-reference.md](references/detailed-reference.md) for details.



## Creative Testing in PMax

### A/B Testing Approach

```
CREATIVE TESTING IN PERFORMANCE MAX
═══════════════════════════════════

TESTING LIMITATIONS:
────────────────────
PMax has NO native A/B testing.
Google combines assets automatically.

WORKAROUNDS:
────────────

OPTION 1: SEQUENTIAL TESTING
───────────────────────────
Week 1-2: Asset Set A
Week 3-4: Asset Set B
Week 5-6: Analyze and pick winner

Drawbacks:
├── Timing effects (seasonality)
├── Slow
└── Not statistically pure

OPTION 2: SPLIT ASSET GROUPS
───────────────────────────
AG 1: Creative Concept A
├── All assets in one style
└── Specific messaging

AG 2: Creative Concept B
├── All assets in different style
└── Alternative messaging

Compare performance after 2-4 weeks.

Advantages:
✓ Parallel testing
✓ Better comparison
✓ Can test different audiences

Drawbacks:
├── Split budget
├── Possible audience overlap
└── More management

OPTION 3: CAMPAIGN EXPERIMENTS
─────────────────────────────
Google Ads Experiments (beta for PMax)
├── True A/B split
├── Statistically significant
└── Check availability in your account

OPTION 4: ASSET RATING MONITORING
────────────────────────────────
Upload multiple variations:
├── Track which get "Best" rating
├── Replace "Low" performers
└── Iteratively improve

This is not a true A/B test but still provides insights.
```

### Asset Refresh Strategy

```
ASSET REFRESH CADENCE
═════════════════════

WEEKLY:
───────
□ Check asset ratings
□ Minor copy updates if needed
□ Urgent fixes (disapprovals, errors)

MONTHLY:
────────
□ Full asset performance review
□ Replace "Low" performers (20-30%)
□ Add new variations
□ Test new concepts

QUARTERLY:
──────────
□ Complete creative refresh
□ New photo shoots/videos
□ Seasonal updates
□ Brand guideline updates

SEASONAL:
─────────
□ Pre-season: New seasonal assets
├── 2-3 weeks before season starts
├── Holiday themes
└── Sale/promo assets

□ In-season: Monitor and optimize
├── Weekly performance check
├── Quick wins implementation
└── Budget shift toward winners

□ Post-season: Cleanup
├── Remove seasonal assets
├── Archive for next year
└── Return to evergreen content
```

## Output: Asset Group Optimization Template

```markdown
# Asset Group Optimization Plan

## Campaign Overview
- **Campaign:** [Campaign name]
- **Account:** [Account name]
- **Analysis Date:** [Date]
- **Period Analyzed:** [Date range]

## Asset Group Structure

### Current Structure
| Asset Group | Products/Focus | Budget % | ROAS | Status |
|-------------|---------------|----------|------|--------|
| [AG 1] | [Products] | [%] | [X]x | [Status] |
| [AG 2] | [Products] | [%] | [X]x | [Status] |

### Recommended Structure
| Asset Group | Products/Focus | Recommended Budget % | Rationale |
|-------------|---------------|---------------------|-----------|
| [AG 1] | [Products] | [%] | [Why] |

## Asset Performance Review

### Headlines
| Headline | Rating | Action |
|----------|--------|--------|
| [Text] | Best | Keep |
| [Text] | Low | Replace with: [New] |

### Images
| Image Description | Rating | Action |
|-------------------|--------|--------|
| [Description] | Best | Keep, create variations |
| [Description] | Low | Replace |

### Videos
| Video | Rating | Action |
|-------|--------|--------|
| [Description] | [Rating] | [Action] |

## Audience Signals Review

### Current Signals
| Signal Type | Signal | Performance |
|-------------|--------|-------------|
| Your Data | [Signal] | [Performance] |
| Custom | [Signal] | [Performance] |

### Recommended Changes
- Add: [New signals]
- Remove: [Underperforming signals]
- Adjust: [Modifications]

## Search Themes Review

### Current Themes
| Theme | Relevance | Action |
|-------|-----------|--------|
| [Theme] | High | Keep |
| [Theme] | Low | Remove |

### New Themes to Add
- [Theme 1]
- [Theme 2]

## Listing Groups (E-commerce)

### Current Segmentation
| Listing Group | Products | Performance |
|---------------|----------|-------------|
| [LG 1] | [Count] | [ROAS] |

### Recommended Changes
- Split: [What to split]
- Exclude: [Products to exclude]
- Add: [New segments]

## Action Items

### Immediate (This Week)
- [ ] [Action item 1]
- [ ] [Action item 2]

### Short-term (Next 2 Weeks)
- [ ] [Action item 3]
- [ ] [Action item 4]

### Long-term (Next Month)
- [ ] [Action item 5]

## Success Metrics
| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| ROAS | [X]x | [Y]x | [Date] |
| CPA | $[X] | $[Y] | [Date] |
| Conv | [X] | [Y] | [Date] |

## Notes
[Additional notes]
```

---
name: meta-lookalike-strategy-planner
description: "This skill should be used when the user asks to \"create lookalike audiences\", \"optimize LAL percentages\", \"choose source audiences\", or mentions \"lookalike strategy\", \"LAL underperforming\", or \"Advantage+ audience signals\". Do NOT use for: audience overlap issues (use audience-overlap-detector), full-funnel design (use full-funnel-designer), campaign structure (use campaign-structure-advisor)."
---
# Lookalike Strategy Planner

## Overview

This skill helps create high-quality Lookalike Audiences by selecting the right source audiences, choosing optimal percentages, and applying advanced strategies for maximum performance.

> **2026 Context:** Meta recommends A/B testing Advantage+ audience for almost all campaign types, but not for retargeting ("About Advantage+ audience", Meta Business Help Center). Lookalikes remain useful as **audience suggestions** in those campaigns, and as audience controls where you need more targeting control. When you add a lookalike built from a website, app or customer list source to a new ad set, Meta turns on Advantage+ lookalike by default, so delivery can go beyond the percentage you chose ("About Advantage+ lookalike"). To keep the percentage as a limit, add the lookalike under "Further limit your audience" (or "Further limit the reach of your ads") and clear "Use as a suggestion" ("How to use custom or lookalike audiences"). In an Advantage+ sales campaign you can add a customer list custom audience as an audience suggestion instead of building separate lookalike ad sets. Since 19 May 2026 the Marketing API no longer allows creating, duplicating or updating legacy **Advantage+ shopping campaigns** (Marketing API changelog v25.0, 18 Feb 2026). New sales campaigns start in the Advantage+ setup; a sales campaign with Advantage+ audience, placements and budget on is what Meta calls an **Advantage+ sales campaign** ("About Advantage+ sales campaigns").

## Lookalike Fundamentals

### How Meta Lookalikes Work

```
┌─────────────────────────────────────────────────────────────────┐
│  LOOKALIKE CREATION PROCESS                                     │
│                                                                 │
│  1. SOURCE AUDIENCE (your data)                                 │
│     └── Minimum 100 people (Meta suggests 1,000-5,000)          │
│                                                                 │
│  2. META's SYSTEM uses source information such as:              │
│     ├── Demographics                                            │
│     ├── Interests                                               │
│     ├── Behaviors                                               │
│     └── (Meta's examples, not the full signal list)             │
│                                                                 │
│  3. LOOKALIKE OUTPUT                                            │
│     └── Top X% of people most similar to source                 │
│                                                                 │
│  Important: Source quality > Source size                         │
└─────────────────────────────────────────────────────────────────┘
```

Sources (Meta Business Help Center): "About lookalike audiences" and "Create a lookalike audience". People in the source audience are left out of the lookalike.

## Source Audience Ranking

Rules of thumb, not Meta figures: check them against the account's own history. Meta's own floor is 100 people in the source, and it suggests 1,000-5,000.

### Tier 1: Highest Quality (Recommended)

| Source Type | Min. Size | Why Effective |
|-------------|-----------|---------------|
| Purchasers (180d) | 500+ | Proven purchase intent |
| High-Value Customers (Top 20% LTV) | 200+ | Quality > quantity |
| Repeat Purchasers | 200+ | Loyalty signal |
| Subscribers (Email/SMS) | 1000+ | Active interest |

### Tier 2: Good Quality

| Source Type | Min. Size | Why Effective |
|-------------|-----------|---------------|
| Add to Cart (30d) | 500+ | High intent |
| Lead Form Completers | 300+ | Qualified interest |
| Checkout Initiators | 300+ | Near-purchasers |
| App Installers (Active) | 500+ | Engaged users |

### Tier 3: Usable but Less Specific

| Source Type | Min. Size | Why Effective |
|-------------|-----------|---------------|
| Website Visitors (30d) | 1000+ | Broad but relevant |
| Video Viewers 95% | 1000+ | High engagement |
| Page Engagers (90d) | 2000+ | Social interest |
| Content Viewers | 1000+ | Topic interest |

### Tier 4: Avoid as Source

```
DO NOT USE AS SOURCE:
├── All website visitors (too broad)
├── Video viewers <25% (low quality)
├── Page likes only (passive)
├── Very old data (>1 year)
└── Mixed audiences (purchasers + browsers)
```

## Percentage Selection Guide

Rules of thumb, not Meta figures: check them against the account's own history. The "Best for" lines and the decision tree below are our working rules.

### Percentage vs Reach Trade-off

```
LOOKALIKE PERCENTAGE SPECTRUM
=============================
Size = that % of the people in the ad set's locations.
Ads Manager shows the size estimate in the ad set.

1%  ████
    └── Most similar to source
    └── Best for: High-value products, limited budget

2%  ████████
    └── Good balance of quality/reach
    └── Best for: General prospecting

3%  ████████████
    └── Broader reach, still relevant
    └── Best for: Scalable campaigns

5%  ████████████████████
    └── Large reach, more variation
    └── Best for: Awareness, large budgets

10% ████████████████████████████████████████
    └── Very broad, limited similarity
    └── Best for: Maximum reach needed
```

Meta: you pick a percentage of the population of the location, smaller percentages match the source more closely, and new lookalikes take their location from the ad set, so their size estimate appears in the ad set, not in Audiences ("About lookalike audiences" and "Create a lookalike audience", cited above).

### Percentage Selection Decision Tree

```
START: Which percentage should I choose?
│
├─► Question 1: What is your daily budget per ad set?
│   ├── <$20/day → Use 1-2%
│   ├── $20-50/day → Use 2-3%
│   ├── $50-100/day → Use 3-5%
│   └── >$100/day → Use 5-10%
│
├─► Question 2: What is your product type?
│   ├── High-ticket (>$200) → Use 1-2%
│   ├── Mid-range ($50-200) → Use 2-4%
│   └── Low-ticket (<$50) → Use 3-6%
│
├─► Question 3: What is your campaign goal?
│   ├── Pure performance/ROAS → Use 1-2%
│   ├── Balanced growth → Use 2-4%
│   └── Scale/volume → Use 4-6%
│
└─► RESULT: Choose percentage based on overlap
```

## Advanced Lookalike Strategies

Rules of thumb, not Meta figures: check them against the account's own history. The budget splits and thresholds below are our working rules.

### Strategy 1: Value-Based Lookalikes

```
STEPS:
1. Export buyers with a value per customer (LTV, order value)
2. Upload them as a customer list with a customer value column
3. Create a lookalike from that customer value custom audience

SETUP IN META:
├── Audiences → Create audience → Custom audience → Customer list
├── Customer value prompt: "Yes", then pick the value column
├── Import & create
└── Create audience → Lookalike audience → pick this source

RESULT: LAL looks for people similar to your valuable customers
```

Sources: "Create a customer value custom audience" and "Create a value-based lookalike audience", Meta Business Help Center.

### Strategy 2: Layered Lookalikes

```
GOAL: Maximum reach without overlap

SETUP (create the three ranges as one lookalike set):
├── Ad Set 1: LAL 0-1% (most valuable)
│   └── Budget: 40% of LAL budget
│
├── Ad Set 2: LAL 1-3%
│   └── No exclusion needed: the set's ranges do not overlap
│   └── Budget: 35% of LAL budget
│
└── Ad Set 3: LAL 3-5%
    └── No exclusion needed: the set's ranges do not overlap
    └── Budget: 25% of LAL budget

BENEFIT: Test which layer performs best
CAUTION: With Advantage+ lookalike on (the default), delivery can
go beyond each range; add each lookalike as an audience control
to keep the layers apart.
```

Meta: lookalikes created as a set are non-overlapping, so you don't have to exclude the more or less similar ones ("Create lookalike audience sets to optimize your bids").

### Strategy 3: Multi-Source Lookalikes

```
GOAL: Reach different customer segments

SETUP:
├── LAL 2%: Purchasers (all buyers)
├── LAL 2%: High-AOV Customers (>$150 orders)
├── LAL 2%: Repeat Purchasers (2+ orders)
├── LAL 2%: Email Engagers (opens/clicks)
└── LAL 2%: Video Completers (95% viewed)

IMPORTANT: Check overlap between these LALs!
Measure it (Audiences → Actions → Show audience overlap),
then use exclusions if needed
```

### Strategy 4: Stacked Lookalikes

```
GOAL: Combine multiple high-intent sources

SETUP:
1. Create Super Source Audience:
   ├── Purchasers (180d) +
   ├── Repeat Purchasers +
   ├── High-Value Customers +
   └── Active Email Subscribers

2. Create LAL from combined audience

BENEFIT: Larger source = more data for algorithm
DRAWBACK: Can "dilute" signal if sources are too diverse
```

## Lookalike Troubleshooting

Rules of thumb, not Meta figures: check them against the account's own history.

### Problem: LAL performs worse than Interest audiences

```
POSSIBLE CAUSES:
├── Source audience too small (<500)
├── Source audience too old (>180 days)
├── Source contains low-quality users
├── LAL percentage too broad for budget
└── Learning phase not completed

SOLUTIONS:
├── Upgrade to Tier 1 source (purchasers)
├── Refresh source with recent data
├── Filter source to high-value only
├── Lower percentage (e.g., 3% → 1%)
└── Increase budget or consolidate ad sets
```

### Problem: LAL has insufficient reach

```
POSSIBLE CAUSES:
├── Percentage too low for market
├── Too many exclusions active
├── Geographic targeting too narrow
└── Source too specific

SOLUTIONS:
├── Increase percentage (e.g., 1% → 3%)
├── Review and reduce exclusions
├── Expand geo targeting
└── Combine multiple sources
```

### Problem: LAL audience not growing

```
LOOKALIKE REFRESH CYCLE:
├── Meta refreshes LALs automatically (see "Last Updated"
│   on the audience); Meta does not publish the interval
├── Source audience must keep growing
└── Stagnation = source audience is stagnating

ACTION:
├── Check if source audience is still receiving events
├── Verify pixel/CAPI is working correctly
└── Consider a broader event as source
```

## Lookalike Creation Template

### When user asks for a LAL strategy:

Rules of thumb, not Meta figures: check them against the account's own history.

```
LOOKALIKE STRATEGY TEMPLATE
============================

ACCOUNT INFO:
├── Monthly budget: [AMOUNT]
├── Current purchasers: [COUNT]
├── Product type: [TYPE]
└── Average order value: [AOV]

RECOMMENDED LOOKALIKES:

PRIMARY LAL (best chance of conversion):
├── Source: [Purchasers 180d / High-Value]
├── Percentage: [1-2%]
├── Estimated size: [XXX,XXX]
└── Budget allocation: 40-50%

SECONDARY LAL (scale potential):
├── Source: [Add to Cart / Leads]
├── Percentage: [2-3%]
├── Estimated size: [XXX,XXX]
└── Budget allocation: 30-35%

TERTIARY LAL (reach/awareness):
├── Source: [Engagers / Video Viewers]
├── Percentage: [3-5%]
├── Estimated size: [XXX,XXX]
└── Budget allocation: 15-25%

EXCLUSIONS SETUP:
├── All LALs: Exclude purchasers (30d)
├── Secondary: Exclude Primary LAL
└── Tertiary: Exclude Primary + Secondary
```

## Source Audience Optimization

### Checklist for Best Source Quality

Only the source size line is Meta's; the rest are rules of thumb, not Meta figures: check them against the account's own history.

```
SOURCE AUDIENCE CHECKLIST:

□ At least 100 people in source (Meta suggests 1,000-5,000)
□ Data is recent (last 180 days)
□ Based on conversion events (not pageviews)
□ Geographically relevant to target market
□ Contains no test/spam accounts
□ Value-based if available
□ Single intent (not mixed)
```

## Example Interaction

**User**: "I want to set up lookalike audiences but don't know which source to use. I have about 2,000 purchasers in the last 6 months."

**Claude response**:

"With 2,000 purchasers in 6 months, your source is inside the 1,000-5,000 range Meta suggests for lookalike sources. Here is my recommended strategy:

**Primary Lookalike (highest priority):**
- Source: Purchasers (180 days)
- Percentage: 1-2%
- Why: You have enough data for a strong signal

**Also consider a Value-Based LAL:**
- Source: Top 20% customers by order value
- Percentage: 1%
- Why: Meta looks for people similar to your higher-value customers

**Questions to optimize further:**
1. Can you export your customers with their order value or LTV? (Meta builds value-based lookalikes from a customer list with a value column.)
2. How many repeat purchasers do you have (2+ orders)?
3. What is your daily budget for prospecting?

With that info I can fine-tune the percentages and build out a layered strategy!"

## MCP Tool Usage

### Pull existing custom audiences to select the best LAL source:

```python
# List custom audiences to identify your highest-quality source options
meta_query(
    account_id="act_XXXXXXXXX",
    entity_type="customaudiences"
)
# Default fields: id, name, approximate_count_lower_bound,
# approximate_count_upper_bound, subtype, description, time_created,
# time_updated, delivery_status, operation_status, data_source.
# 50 audiences per page by default; for more, pass pagination_url=<paging.next>.
# When more than 50 audiences come back, format="auto" keeps only id and name: pass format="full".

# See which audiences the active ad sets use (targeting.custom_audiences)
meta_query(
    account_id="act_XXXXXXXXX",
    entity_type="adsets",
    effective_status=["ACTIVE"],
    fields=["id", "name", "targeting", "optimization_goal"]
)
```

Rules of thumb, not Meta figures: check them against the account's own history. Look for audiences whose `approximate_count_lower_bound` is at least 1,000 and whose `time_updated` is recent. Purchaser audiences (a customer list of buyers, or a website audience built on the Purchase event) are usually the better LAL sources. Skip sources below 300 people or not updated in the last 180 days. Meta's floor is 100 people and it suggests 1,000-5,000.

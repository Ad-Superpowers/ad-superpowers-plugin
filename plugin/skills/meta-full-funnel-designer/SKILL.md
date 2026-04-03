---
name: full-funnel-designer
description: |
  Designs complete full-funnel Meta Ads strategies with optimized campaign structures for every stage of the customer journey. Use when: setting up a full funnel, allocating budget across funnel stages, or optimizing an existing funnel.
  Do NOT use for: campaign structure details (use campaign-structure-advisor), audience overlap issues (use audience-overlap-detector), bid strategy selection (use bid-strategy-selector).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "meta"
  phase: "fase-3-audience-creative"
compatibility: "Requires AdSuperpowers MCP server with Meta Ads connection"
---
# Full-Funnel Designer

## Overview

This skill helps design complete full-funnel advertising strategies for Meta Ads, including budget allocation, audience targeting per stage, and creative alignment with the customer journey.

## Funnel Framework

### The 3 Funnel Stages

```
┌─────────────────────────────────────────────────────────────────┐
│  TOFU (Top of Funnel) - AWARENESS                               │
│  ├── Goal: Reach & brand awareness                              │
│  ├── Budget: 20-30% of total                                    │
│  ├── Audiences: Broad, Lookalikes 3-10%, Interest-based         │
│  ├── Objectives: Reach, Video Views, Brand Awareness            │
│  ├── Creatives: Educational, entertaining, brand story          │
│  └── KPIs: CPM, Reach, Video ThruPlay, Frequency                │
├─────────────────────────────────────────────────────────────────┤
│  MOFU (Middle of Funnel) - CONSIDERATION                        │
│  ├── Goal: Engagement & interest building                       │
│  ├── Budget: 30-40% of total                                    │
│  ├── Audiences: Engagers, Video viewers, Website visitors       │
│  ├── Objectives: Traffic, Engagement, Lead Generation           │
│  ├── Creatives: Product demos, testimonials, comparisons        │
│  └── KPIs: CTR, CPC, Landing page views, Time on site           │
├─────────────────────────────────────────────────────────────────┤
│  BOFU (Bottom of Funnel) - CONVERSION                           │
│  ├── Goal: Conversions & sales                                  │
│  ├── Budget: 30-50% of total                                    │
│  ├── Audiences: Add to cart, High-intent visitors, Customers    │
│  ├── Objectives: Conversions, Catalog Sales                     │
│  ├── Creatives: Urgency, offers, social proof, retargeting      │
│  └── KPIs: CPA, ROAS, Conversion rate, AOV                      │
└─────────────────────────────────────────────────────────────────┘
```

## Budget Allocation Calculator

### Ask the user:

1. **What is your total monthly budget?**
2. **What is your current situation?**
   - New brand (low awareness) → More TOFU
   - Established brand (high traffic) → More BOFU
   - Growing brand (balance needed) → Balanced distribution

### Budget Distribution Models

#### Model A: New Brand / Awareness Focus
```
TOFU: 40% │████████████████████
MOFU: 35% │█████████████████▌
BOFU: 25% │████████████▌
```

#### Model B: Balanced / Growth Focus
```
TOFU: 25% │████████████▌
MOFU: 35% │█████████████████▌
BOFU: 40% │████████████████████
```

#### Model C: Established Brand / Performance Focus
```
TOFU: 15% │███████▌
MOFU: 25% │████████████▌
BOFU: 60% │██████████████████████████████
```

## Audience Mapping per Stage

### TOFU Audiences (Cold)

| Audience Type | Description | Expected CPM |
|---------------|-------------|--------------|
| Broad | Demographics + geo only | $3-8 |
| Interest Stacking | 3-5 related interests | $5-10 |
| Lookalike 6-10% | Broad lookalike of purchasers | $4-8 |
| Video Viewers LAL | Lookalike of 95% video viewers | $5-9 |

### MOFU Audiences (Warm)

| Audience Type | Description | Window |
|---------------|-------------|--------|
| Video Viewers | 50%, 75%, 95% watched | 30-60 days |
| Page Engagers | Likes, comments, shares | 30-90 days |
| Website Visitors | All visitors (excl. converters) | 30-60 days |
| Blog Readers | Specific content pages | 30-60 days |
| IG/FB Engagers | Profile visitors, post engagers | 30-90 days |

### BOFU Audiences (Hot)

| Audience Type | Description | Window |
|---------------|-------------|--------|
| Add to Cart | Product added, not purchased | 7-14 days |
| View Content | Product page viewed | 7-14 days |
| Initiate Checkout | Checkout started, not completed | 3-7 days |
| Past Purchasers | Cross-sell/upsell | 30-180 days |
| High-Value Customers | Top 20% LTV | 180-365 days |

## Creative Strategy per Stage

### TOFU Creative Formats

```
Recommended formats:
├── Video (15-30 sec) - Hook within 3 seconds
├── Carousel - Storytelling or educational
├── Reels - Native, entertaining content
└── Collection - Brand discovery

Content types:
├── Educational ("Did you know...")
├── Entertainment (Relatable content)
├── Brand story (Values, mission)
└── User generated (Authentic)
```

### MOFU Creative Formats

```
Recommended formats:
├── Video (30-60 sec) - Product demos
├── Carousel - Feature highlights
├── Lead ads - Gated content
└── Instant Experience - Immersive storytelling

Content types:
├── Product demonstrations
├── Customer testimonials
├── How-to guides
├── Comparison content
└── Behind the scenes
```

### BOFU Creative Formats

```
Recommended formats:
├── DPA (Dynamic Product Ads)
├── Carousel - Retargeting viewed products
├── Single image - Strong CTA
└── Collection - Product catalog

Content types:
├── Urgency ("Last chance", "Almost sold out")
├── Social proof (Reviews, ratings)
├── Special offers (Discount, free shipping)
├── Abandoned cart reminders
└── Limited time deals
```

## Full-Funnel Campaign Template

### When the user asks to set up a funnel:

```
CAMPAIGN STRUCTURE TEMPLATE
===========================

Budget: [TOTAL BUDGET]

TOFU CAMPAIGN - Awareness
   ├── Name: [BRAND]_TOFU_Awareness_[MONTH]
   ├── Objective: Reach / Video Views
   ├── Budget: [X]% = $[AMOUNT]
   ├── Audiences:
   │   ├── Ad Set 1: Broad (18-65, [COUNTRY])
   │   ├── Ad Set 2: Interest Stack ([INTERESTS])
   │   └── Ad Set 3: LAL 6-10% Purchasers
   └── Creatives:
       ├── Video 1: Brand story (15 sec)
       ├── Video 2: Educational hook
       └── Carousel: Value proposition

MOFU CAMPAIGN - Consideration
   ├── Name: [BRAND]_MOFU_Consideration_[MONTH]
   ├── Objective: Traffic / Engagement
   ├── Budget: [X]% = $[AMOUNT]
   ├── Audiences:
   │   ├── Ad Set 1: Video Viewers 50%+ (30d)
   │   ├── Ad Set 2: Page Engagers (60d)
   │   └── Ad Set 3: Website Visitors (30d)
   └── Creatives:
       ├── Video 1: Product demo
       ├── Carousel: Features & benefits
       └── Testimonial: Customer story

BOFU CAMPAIGN - Conversion
   ├── Name: [BRAND]_BOFU_Conversion_[MONTH]
   ├── Objective: Conversions / Sales
   ├── Budget: [X]% = $[AMOUNT]
   ├── Audiences:
   │   ├── Ad Set 1: Add to Cart (14d)
   │   ├── Ad Set 2: View Content (7d)
   │   └── Ad Set 3: Past Purchasers (90d)
   └── Creatives:
       ├── DPA: Viewed products
       ├── Single image: Urgency offer
       └── Carousel: Social proof
```

## Frequency & Overlap Management

### Frequency Guidelines per Stage

| Stage | Max Frequency/Week | Action When Exceeded |
|-------|---------------------|----------------------|
| TOFU | 2-3x | Expand audience |
| MOFU | 3-4x | Refresh creatives |
| BOFU | 5-7x | Add exclusions |

### Audience Exclusions Setup

```
TOFU exclusions:
└── Exclude: MOFU + BOFU audiences

MOFU exclusions:
├── Exclude: Purchasers (30d)
└── Exclude: Add to Cart (7d)

BOFU exclusions:
└── Exclude: Purchasers (7d) or converters
```

## Funnel Diagnosis Framework

### When the funnel is underperforming:

```
PROBLEM: Low awareness/reach
├── Check: Is TOFU budget sufficient? (min 20%)
├── Check: Are audiences too narrow?
└── Action: Target broader, more video content

PROBLEM: High TOFU metrics, low MOFU engagement
├── Check: Does MOFU content align with TOFU messaging?
├── Check: Are retargeting windows correct?
└── Action: Align content, extend windows

PROBLEM: Good engagement, few conversions
├── Check: Is the landing page optimized?
├── Check: Are BOFU offers compelling enough?
└── Action: A/B test offers, add urgency

PROBLEM: High CPA in BOFU
├── Check: Is the audience too small (audience exhaustion)?
├── Check: Is frequency too high?
└── Action: Strengthen TOFU/MOFU, refresh creatives
```

## Example Interaction

**User**: "I want to set up a full funnel for my e-commerce store. Budget is $5,000/month."

**Claude response**:

"I'll help you with a complete full-funnel strategy. First, a few questions:

1. **What do you sell?** (product category)
2. **Is your brand already established or are you starting fresh?**
3. **Do you have existing pixel data/audiences?**
4. **What is your average order value (AOV)?**

Based on $5,000/month and an average scenario, I'd suggest:

| Stage | Budget | Goal |
|-------|--------|------|
| TOFU | $1,250 (25%) | Reach new people |
| MOFU | $1,750 (35%) | Build interest |
| BOFU | $2,000 (40%) | Drive conversions |

Would you like me to build out the complete campaign structure with audiences and creative suggestions?"

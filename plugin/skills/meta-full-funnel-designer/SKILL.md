---
name: meta-full-funnel-designer
description: "This skill should be used when the user asks to \"design a full funnel\", \"allocate budget across funnel stages\", \"optimize TOFU/MOFU/BOFU\", or mentions \"full-funnel strategy\", \"customer journey campaigns\", or \"funnel budget split\". Do NOT use for: campaign structure details (use campaign-structure-advisor), audience overlap issues (use audience-overlap-detector), bid strategy selection (use bid-strategy-selector)."
---
# Full-Funnel Designer

## Overview

This skill helps design complete full-funnel advertising strategies for Meta Ads, including budget allocation, audience targeting per stage, and creative alignment with the customer journey.

## 2026 Context: ASC and Andromeda

> **Advantage+ Sales Campaigns (ASC):** For e-commerce advertisers, a sales campaign with Advantage+ audience, placements and budget on is what Meta calls an Advantage+ sales campaign; Meta then manages budget, audience and placement ("About Advantage+ sales campaigns", Meta Business Help Center). Since 19 May 2026 the Marketing API no longer allows creating, duplicating or updating legacy "Advantage+ shopping campaigns" (Marketing API changelog v25.0, 18 Feb 2026). For accounts spending >€5k/month on conversions, consider running ASC alongside or instead of manual TOFU/MOFU/BOFU segmentation. Rules of thumb, not Meta figures: check them against the account's own history (the €5k threshold is ours).

> **Andromeda Engine:** Andromeda is Meta's ad retrieval system: the first stage of delivery, which narrows tens of millions of candidate ads to a few thousand before ranking (Meta Engineering, 2 Dec 2024, https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/).

> **Attribution (Jan 2026 change):** Since 12 January 2026 the Ads Insights API no longer returns the 7-day view and 28-day view attribution windows; 1-day click, 7-day click, 28-day click, 1-day engaged view and 1-day view remain ("Ads Insights API Metric Availability Updates", Meta for Developers, 16 Oct 2025). In Ads Manager, the standard attribution setting offers click-through of 1 or 7 days, view-through of 1 day and engage-through of 1 day ("About attribution models and attribution settings", Meta Business Help Center). If older reports or BOFU ROAS targets used 7-day or 28-day view, compare like with like: the same sales counted over shorter windows give lower totals.

## Funnel Framework

### The 3 Funnel Stages

```
┌─────────────────────────────────────────────────────────────────┐
│  TOFU (Top of Funnel) - AWARENESS                               │
│  ├── Goal: Reach & brand awareness                              │
│  ├── Budget: 20-30% of total                                    │
│  ├── Audiences: Broad, Lookalikes 3-10%, Interest-based         │
│  ├── Objectives: Awareness; Engagement for video views          │
│  ├── Creatives: Educational, entertaining, brand story          │
│  └── KPIs: CPM, Reach, Video ThruPlay (Ads Manager), Frequency  │
├─────────────────────────────────────────────────────────────────┤
│  MOFU (Middle of Funnel) - CONSIDERATION                        │
│  ├── Goal: Engagement & interest building                       │
│  ├── Budget: 30-40% of total                                    │
│  ├── Audiences: Engagers, Video viewers, Website visitors       │
│  ├── Objectives: Traffic, Engagement, Leads                     │
│  ├── Creatives: Product demos, testimonials, comparisons        │
│  └── KPIs: CTR, CPC, Landing page views, Time on site           │
├─────────────────────────────────────────────────────────────────┤
│  BOFU (Bottom of Funnel) - CONVERSION                           │
│  ├── Goal: Conversions & sales                                  │
│  ├── Budget: 30-50% of total                                    │
│  ├── Audiences: Add to cart, High-intent visitors, Customers    │
│  ├── Objective: Sales (incl. Advantage+ catalog ads)            │
│  ├── Creatives: Urgency, offers, social proof, retargeting      │
│  └── KPIs: CPA, ROAS, Conversion rate, AOV                      │
└─────────────────────────────────────────────────────────────────┘
```

The budget shares and lookalike ranges in this framework are rules of thumb, not Meta figures: check them against the account's own history. The objective names are Meta's: Awareness, Traffic, Engagement, Leads, App promotion and Sales replaced the older objectives (Reach, Video Views, Brand Awareness, Conversions), and since Marketing API v21.0 (2 Oct 2024) new ad sets and ads can no longer use the older ones (Marketing API changelog v21.0). Meta's API guides create video-view campaigns with the Engagement objective (OUTCOME_ENGAGEMENT), and our meta_create tool accepts only the six OUTCOME_* objectives.

## Budget Allocation Calculator

### Ask the user:

1. **What is your total monthly budget?**
2. **What is your current situation?**
   - New brand (low awareness) → More TOFU
   - Established brand (high traffic) → More BOFU
   - Growing brand (balance needed) → Balanced distribution

### Budget Distribution Models

Rules of thumb, not Meta figures: check them against the account's own history.

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

The windows and ranges below are rules of thumb, not Meta figures: check them against the account's own history.

### TOFU Audiences (Cold)

| Audience Type | Description | Expected CPM |
|---------------|-------------|--------------|
| Broad | Demographics + geo only | [from account history] |
| Interest Stacking | 3-5 related interests | [from account history] |
| Lookalike 6-10% | Broad lookalike of purchasers | [from account history] |
| Video Viewers LAL | Lookalike of 95% video viewers | [from account history] |

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

Video lengths and the 3-second hook are rules of thumb, not Meta figures: check them against the account's own history.

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
├── Advantage+ Catalog Ads (Dynamic Product Ads)
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
   ├── Objective: Awareness / Engagement (video views)
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
   ├── Objective: Sales
   ├── Budget: [X]% = $[AMOUNT]
   ├── Audiences:
   │   ├── Ad Set 1: Add to Cart (14d)
   │   ├── Ad Set 2: View Content (7d)
   │   └── Ad Set 3: Past Purchasers (90d)
   └── Creatives:
       ├── Advantage+ Catalog Ads: Viewed products
       ├── Single image: Urgency offer
       └── Carousel: Social proof
```

## Frequency & Overlap Management

### Frequency Guidelines per Stage

Rules of thumb, not Meta figures: check them against the account's own history.

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

Rules of thumb, not Meta figures: check them against the account's own history.

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

## MCP Tool Usage

### Audit an existing funnel before designing a new one:

```python
# Get campaign-level performance to map current funnel state
meta_get_insights(
    account_id="act_XXXXXXXXX",
    level="campaign",
    date_preset="last_30d",
    fields=["impressions", "reach", "spend", "actions", "cost_per_action_type"]
)
```

This shows spend and results per campaign. `meta_get_insights` returns one page of rows: if the response has `paging.next`, fetch the rest with `meta_query(account_id, "campaigns", pagination_url=<paging.next>)`. Map each campaign to a funnel stage by its objective (read it with `meta_query(account_id, "campaigns", fields=["name", "objective"])`) to see which stage is underfunded or over-invested before recommending changes.

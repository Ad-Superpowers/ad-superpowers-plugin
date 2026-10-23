---
name: meta-ad-copy-generator
description: "This skill should be used when the user asks to \"write ad copy\", \"generate headlines\", \"create primary text\", or mentions \"Meta ad copy\", \"ad descriptions\", or \"hook formulas for ads\". Do NOT use for: video scripts (use video-script-writer), creative brainstorming (use creative-diversification-generator), A/B test design (use ab-test-planner)."
---
# Ad Copy Generator

## Overview

This skill writes ad copy for Meta Ads using common copywriting frameworks, psychological triggers and Meta's placement specs.

## Meta Ads Copy Structure

### Anatomy of a Meta Ad

```
┌─────────────────────────────────────────────────────────────────┐
│  META AD COPY COMPONENTS                                        │
│                                                                 │
│  PRIMARY TEXT (Meta's Ads Guide, per placement)                 │
│  └── 50-150 characters (Facebook Feed), 125 (Instagram Feed,    │
│      Stories), 44 (Instagram Reels)                             │
│                                                                 │
│  HEADLINE (Meta's Ads Guide, per placement)                     │
│  └── 27 characters (Facebook Feed), 40 (Instagram Feed images,  │
│      Facebook Stories)                                          │
│                                                                 │
│  DESCRIPTION (optional)                                         │
│  └── The Ads Guide gives no recommended length for Feed         │
│                                                                 │
│  CTA BUTTON (fixed menu)                                        │
│  └── Shop Now, Learn More, Sign Up, etc.                       │
└─────────────────────────────────────────────────────────────────┘
```

Lengths are recommendations from Meta's Ads Guide (checked 10 Oct 2026, https://www.facebook.com/business/ads-guide/update), not hard limits; see Optimal Lengths below.

## Hook Formulas (First Sentence)

### The 3-Second Rule

```
The first sentence determines whether people stop scrolling.
```

### Top 10 Hook Frameworks

| # | Framework | Example |
|---|-----------|---------|
| 1 | **Problem + Solution** | "Tired of [problem]? Here's the solution." |
| 2 | **Shocking Statistic** | "[A real, sourced percentage] of [audience] make this mistake..." |
| 3 | **Ask a Question** | "Did you know that [surprising fact]?" |
| 4 | **Direct Address** | "This is for you if you [situation]..." |
| 5 | **Social Proof** | "[Real number] people already joined..." |
| 6 | **Urgency** | "Today only: [offer]" |
| 7 | **Curiosity Gap** | "The secret behind [desired result]..." |
| 8 | **Before/After** | "From [negative] to [positive] in [time]" |
| 9 | **Contrarian** | "Forget everything you knew about [topic]" |
| 10 | **Specific Result** | "[Exact result] in [exact time]" |

## Copywriting Frameworks

### PAS Framework (Problem-Agitate-Solve)

```
STRUCTURE:
P - Problem: Name the problem
A - Agitate: Make the problem bigger/more painful
S - Solve: Present your solution

EXAMPLE:
"Getting headaches from Excel spreadsheets again? [PROBLEM]
It costs you hours every week and you keep making mistakes. [AGITATE]
With [Product] you automate everything in [real, measured time]. [SOLVE]"
```

### AIDA Framework (Attention-Interest-Desire-Action)

```
STRUCTURE:
A - Attention: Grab attention with hook
I - Interest: Build interest with benefits
D - Desire: Create desire with results
A - Action: Call to action

EXAMPLE:
"Stop wasting money on ineffective ads. [ATTENTION]
Our AI analyzes [real number] data points per campaign. [INTEREST]
Customers see [a real, sourced result]. [DESIRE]
Start your free trial → [ACTION]"
```

### BAB Framework (Before-After-Bridge)

```
STRUCTURE:
B - Before: Current situation (pain)
A - After: Desired situation (pleasure)
B - Bridge: Your product as the bridge

EXAMPLE:
"You work 60 hours a week and barely see your family. [BEFORE]
Imagine: same revenue, but [real, measured number] fewer hours of work. [AFTER]
[Product] automates your workflows so you get your time back. [BRIDGE]"
```

### 4U Framework

```
STRUCTURE:
- Useful: Is it useful?
- Urgent: Is there urgency?
- Unique: Is it unique?
- Ultra-specific: Is it specific?

EXAMPLE:
"Save [real, measured hours] per week [USEFUL] - [only if true: this week only N% off] [URGENT].
[Only if true: the only tool that combines AI + human review] [UNIQUE].
[Real number] companies increased their conversion by [real, measured %] [ULTRA-SPECIFIC]."
```

## Copy per Funnel Stage

The CTA lines name Meta call-to-action button types; not every type is available for every campaign objective ('Ad Creative Link Data Call To Action', Marketing API reference).

### TOFU Copy (Awareness)

```
GOAL: Educate, spark interest, build problem awareness
TONE: Informative, curiosity-building, low barrier
CTA: Learn More, Watch Video, See More

EXAMPLE:
"Did you know [a real, sourced percentage] of marketers struggle with [problem]?

In this video we explain why this happens and
what you can do about it. No sales pitch, just value.

Watch the video"
```

### MOFU Copy (Consideration)

```
GOAL: Build trust, show benefits, differentiate
TONE: Helpful, expert, social proof
CTA: Sign Up, Download, Subscribe, Learn More

EXAMPLE:
"Over [real number] marketers already use [Product] to
optimize their Meta Ads.

- [Real, measured CPA result]
- [Real, measured reporting time saved]
- Automatic optimizations

Try 14 days free - no credit card required."
```

### BOFU Copy (Conversion)

```
GOAL: Push conversion, create urgency, remove objections
TONE: Direct, urgent, results-oriented
CTA: Shop Now, Buy Now, Get Offer, Order Now

EXAMPLE:
"You've looked at [Product] before.

This is your sign:
25% off - today only
Free shipping
30-day return policy

More than [real number] 5-star reviews.
Order now"
```

## Copy Variation Templates

### When user asks for ad copy:

**Ask first:**
1. What is the product/service?
2. Who is the target audience?
3. Which funnel stage? (TOFU/MOFU/BOFU)
4. What is the unique benefit?
5. Is there a specific offer?

**Then deliver:**

```
AD COPY SET - [PRODUCT/SERVICE]
================================

VARIATION 1: Problem-Solution
─────────────────────────────
Primary Text:
[Hook with problem]

[Problem explanation 1-2 sentences]

[Present solution]

[Social proof or result]

[CTA]

Headline: [Short, benefit-focused]
Description: [Supporting info]
CTA Button: [Relevant CTA]

─────────────────────────────

VARIATION 2: Social Proof Lead
─────────────────────────────
Primary Text:
[Hook with social proof/statistic]

[What others achieved]

[How you can too]

[Urgency or offer]

Headline: [Result-focused]
Description: [Trust element]
CTA Button: [Relevant CTA]

─────────────────────────────

VARIATION 3: Direct Offer
─────────────────────────────
Primary Text:
[Hook with offer]

[Key benefits bullets]
- Benefit 1
- Benefit 2
- Benefit 3

[Urgency]

Headline: [Offer + benefit]
Description: [Scarcity/trust]
CTA Button: [Shop Now/Get Offer]
```

## Psychological Triggers

### Triggers to use in copy:

```
SCARCITY
├── "Only [real stock count] left in stock"
├── "Last day of the sale"
└── "Limited edition"

SOCIAL PROOF
├── "[Real number]+ satisfied customers"
├── "[Real rating]/5 ([real review count] reviews)"
└── "As seen in [well-known media]"

AUTHORITY
├── "[Named expert or body, if real]"
├── "[Award name, if real]"
└── "[Real number]+ years of experience"

RECIPROCITY
├── "Free [valuable content]"
├── "No credit card required"
└── "No-obligation consultation"

LOSS AVERSION
├── "Don't miss this"
├── "Prevent yourself from..."
└── "Stop losing money on..."

CURIOSITY
├── "The secret behind..."
├── "What nobody tells you about..."
└── "The surprising reason why..."
```

## Platform-Specific Tips

### Facebook vs Instagram vs Threads vs Meta Audience Network

Rules of thumb, not Meta figures: check them against the account's own history. Only the character counts, the Threads note and the Audience Network placements come from the Meta pages cited below the block.

```
FACEBOOK:
├── Longer copy can work (test!)
├── More context & detail allowed
└── Emojis work, but keep subtle

INSTAGRAM:
├── Shorter = better (visual first)
├── Emoji-friendly
├── Lifestyle & aspirational tone
└── Under 125 characters ideal

THREADS:
├── Conversational, community-first tone
├── Shorter copy — feels like a post
├── Avoid hard-sell language
└── No CTA button in the feed: tapping the headline opens the link

STORIES/REELS:
├── Ads Guide: 44 characters (Instagram Reels), 125 (Stories)
├── Native, casual tone
├── Emojis as visual elements
└── Urgency works well

META AUDIENCE NETWORK:
├── Works with same copy as Feed
├── Native, banner, interstitial and rewarded video placements
└── Often excluded in manual placement tests
```

Threads: 'Extend Meta Campaigns With Ads in Threads', Meta for Business, https://www.facebook.com/business/ads/threads. Placements and lengths: Meta's Ads Guide, https://www.facebook.com/business/ads-guide/update.

## Character Limits & Best Practices

### Optimal Lengths

| Component | Facebook Feed | Instagram Feed | Instagram Reels |
|-----------|---------------|----------------|-----------------|
| Primary Text | 50-150 | 125 | 44 |
| Headline | 27 | 40 (image ads) | not listed |
| Description | not listed | not listed | not listed |

Recommended character counts from Meta's Ads Guide (image and video ad specs per placement, checked 10 Oct 2026: https://www.facebook.com/business/ads-guide/update). Stories: 125 characters of primary text, and a 40-character headline on Facebook Stories. The guide gives recommendations, not hard limits, and the figures change: check the page for the placement you buy.

### Formatting Tips

Rules of thumb, not Meta figures: check them against the account's own history.

```
DO:
├── Use line breaks for readability
├── Bullets/emoji for scannable lists
├── One clear CTA per ad
├── Test short vs long versions
└── Use numbers (specific > vague)

DON'T:
├── ALL CAPS (except 1 word for emphasis)
├── Too many emojis (max 3-5)
├── Clickbait that doesn't deliver
├── Multiple CTAs in one ad
└── Jargon your audience doesn't know
```

## A/B Test Suggestions

### What to test in copy:

```
TEST PRIORITY:
1. Hook/first sentence
2. Headline
3. CTA button choice
4. Length (short vs long)
5. Tone (formal vs casual)
6. With/without emojis
7. With/without social proof
8. With/without price
```

## Example Interaction

**User**: "I need ad copy for my online Spanish course. Target audience is adults 25-45 who want to get by in Spanish on holiday. It's a 12-week program for €297."

**Claude response**:

"I'll create 3 copy variations for your Spanish course:

---

**VARIATION 1: Problem-Agitate-Solve**

*Primary Text:*
Tried language apps but still freeze when someone speaks Spanish to you?

You're not alone. [A real, sourced figure, or drop this line.]

In my 12-week program you'll learn:
- Order, ask for directions and make small talk
- Practice in short daily sessions
- Phrases you will actually use

[Real number] students already joined. Your turn?

*Headline:* Spanish for your next holiday
*Description:* 12-week program
*CTA:* Learn More

---

**VARIATION 2: Transformation Focus**

*Primary Text:*
From pointing at the menu to ordering in Spanish

[Real student's name and result, shared with permission.]

'[Real quote from that student]'

Discover how the 12-week program can help you →

*Headline:* Your transformation starts here
*Description:* Start today
*CTA:* Sign Up

---

**VARIATION 3: Direct Offer**

*Primary Text:*
12 weeks of Spanish for your next trip

- Personalized lesson plans
- Short daily lessons
- Weekly coaching calls
- Community of [real number] learners

Limited time: €297 (normally [real previous price])
+ Free bonus week included

*Headline:* Start your 12-week transformation
*Description:* [Only if true: Limited availability]
*CTA:* Get Offer

---

Want me to create more variations with a different angle?"

## MCP Tool Usage

### Pull top-performing ad copy to inform new variations:

```python
# Retrieve existing ad performance to identify winning copy patterns
meta_get_insights(
    account_id="act_XXXXXXXXX",
    level="ad",
    date_preset="last_30d",
    fields=["impressions", "ctr", "spend", "actions", "cost_per_action_type"]
)

# Then pull the actual creative text from top performers
meta_get_creatives(
    account_id="act_XXXXXXXXX",
    scope="account",
    date_preset="last_30d",
    sort_by="ctr"
)
```

Use these to analyze which hooks, benefit statements, and CTAs are currently winning before generating new copy variants.

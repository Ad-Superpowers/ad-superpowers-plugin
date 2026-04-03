---
description: Comprehensive competitive analysis combining deep research with ad platform data. Includes competitor profiling, positioning maps, spend estimation, creative analysis, and strategic recommendations. Integrates Google Ads auction insights and Meta Ad Library research. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Competitive Intelligence & Ad Strategy Analysis

Conduct comprehensive competitive analysis for [specify company_name] in the [specify industry] industry.

## Overview

This workflow combines external research, ad library analysis, and optional platform data to create a complete competitive intelligence report. Helps agencies understand the competitive landscape for strategic planning and client pitches.

## Parameters
- Company: [specify company_name]
- Industry: [specify industry]
- Known Competitors: To be discovered
- Google Ads Customer ID: [specify google_ads_customer_id]
- Competitive Focus: general
- Include Ad Library Research: {{ include_ad_library_research | default(true) }}

---

## PHASE 1: Competitor Discovery & Research

### Research Prompts

Use these prompts to discover and research competitors. If web search tools are available (Exa, native search), execute them directly. Otherwise, provide as structured research prompts.

**Prompt 1 - Competitor Discovery:**
```
Find the top 5-10 competitors for [specify company_name] in [specify industry]:
- Direct competitors (same product/service, same market)
- Indirect competitors (different product, same need)
- Emerging competitors (startups, new entrants)

For each competitor, identify:
- Company name and website
- Headquarters and markets served
- Estimated company size (employees, revenue)
- Primary product/service offerings
- Year founded
- Funding status (if applicable)
```


**Known Competitors to Analyze:**
[specify known_competitors]


**Prompt 2 - Competitive Positioning Research:**
```
Research competitive positioning for [specify company_name]'s top competitors in [specify industry]:

For each competitor:
- Unique value proposition
- Target audience/segments
- Pricing strategy (premium/mid-market/budget)
- Key messaging themes
- Brand positioning (innovative/reliable/affordable/etc.)
- Distribution channels
- Recent strategic moves (last 6 months)
```

**Prompt 3 - Competitor Digital Presence:**
```
Analyze digital presence of [specify company_name]'s competitors:
- Website traffic estimates (SimilarWeb if available)
- Social media following (Meta, LinkedIn, TikTok)
- Content marketing approach
- SEO visibility for key terms
- Review ratings (G2, Trustpilot, Google)
- App store presence (if applicable)
```

---

## PHASE 2: Ad Library Research


### Meta Ad Library Research

**Manual Research Instructions:**
Visit [Meta Ad Library](https://www.facebook.com/ads/library/) and search for each competitor.

**For Each Competitor, Document:**

| Competitor | Active Ads | Ad Types | Key Themes | Start Date |
|------------|-----------|----------|------------|------------|
| [Name] | [Count] | [Video/Image/Carousel] | [Main messages] | [Earliest ad] |

**Analysis Questions:**
1. How many ads are they running? (Scale indicator)
2. What ad formats dominate? (Video = higher investment)
3. What are the main messaging themes?
4. What CTAs do they use?
5. What landing pages do they drive to?
6. How often do they refresh creative?
7. Are they running any seasonal/promotional campaigns?

**Creative Pattern Analysis:**
```
For top 3 competitors, analyze:
- Visual style (lifestyle/product/testimonial/UGC)
- Color palette and branding consistency
- Video length distribution (if video ads)
- Headline patterns and copywriting style
- Offer structure (discount/free trial/demo/etc.)
- Social proof usage (reviews, numbers, logos)
```

### LinkedIn Ad Analysis (B2B)
For B2B competitors, check LinkedIn's ad transparency:
- Go to competitor's LinkedIn page → Posts → Ads
- Document: Ad formats, messaging, content offers

### TikTok Creative Center
Visit [TikTok Creative Center](https://ads.tiktok.com/business/creativecenter/inspiration/topads)
- Search for competitors or industry keywords
- Analyze top-performing ad formats and hooks


---

## PHASE 3: Platform-Specific Competitive Data


### Google Ads Auction Insights

Run auction insights analysis to understand competitive position:

```
google_ads_run_gaql(
    customer_id="[specify google_ads_customer_id]",
    query="""
        SELECT
            campaign.name,
            auction_insight.domain,
            metrics.auction_insight_search_impression_share,
            metrics.auction_insight_search_top_impression_share,
            metrics.auction_insight_search_absolute_top_impression_share,
            metrics.auction_insight_search_outranking_share,
            metrics.auction_insight_search_overlap_rate,
            metrics.auction_insight_search_position_above_rate
        FROM auction_insight
        WHERE segments.date DURING LAST_30_DAYS
        ORDER BY metrics.auction_insight_search_impression_share DESC
        LIMIT 20
    """
)
```

**Auction Insights Interpretation:**
| Metric | What It Means | Good Benchmark |
|--------|--------------|----------------|
| Impression Share | How often you appear vs. competitors | >50% for brand, >15% for generic |
| Top of Page Rate | Above organic results | >70% for brand terms |
| Abs Top Rate | Very first position | >50% for brand terms |
| Overlap Rate | How often competitor appears with you | Monitor high overlaps |
| Position Above Rate | Competitor above you when both show | <50% = you're winning |
| Outranking Share | You rank higher or show when they don't | Higher = better position |


### Google Ads Insights (Manual Research)

Without connected Google Ads, use these research methods:

**Keyword Research:**
```
google_ads_run_keyword_planner(
    customer_id="YOUR_CUSTOMER_ID",
    keywords=["[specify industry] related keywords"],
    page_url="competitor website URL"
)
```

**Manual Competitive Indicators:**
- Search for industry keywords and note which competitors appear
- Document ad copy patterns and offers
- Note landing page strategies


### Estimated Competitor Ad Spend

**Spend Estimation Framework:**

Method 1 - Platform Clues:
- Meta Ad Library active ads count × €50-200/day = rough estimate
- LinkedIn ads visible × €100-300/day = rough estimate
- Google Ads visibility in auction insights → impression share indicates relative spend

Method 2 - Industry Benchmarks:
| Company Size | Typical Monthly Ad Budget |
|--------------|---------------------------|
| Startup (<20 employees) | €1,000 - €10,000 |
| SMB (20-100 employees) | €10,000 - €50,000 |
| Mid-market (100-500 employees) | €50,000 - €200,000 |
| Enterprise (500+ employees) | €200,000+ |

Method 3 - Digital Presence Correlation:
- Website traffic (SimilarWeb) × industry CPM/CPC × estimated paid % = rough spend

**Output: Competitor Spend Estimates**
| Competitor | Est. Monthly Spend | Confidence | Primary Channels |
|------------|-------------------|------------|------------------|
| [Competitor 1] | €XX,XXX | High/Med/Low | [Channels] |
| [Competitor 2] | €XX,XXX | High/Med/Low | [Channels] |

---

## PHASE 4: Competitive Analysis Frameworks

### 4.1 Positioning Map

Create a 2x2 positioning map based on the most relevant dimensions for [specify industry]:

**Common Positioning Axes:**
- Price (Low ↔ Premium)
- Quality/Features (Basic ↔ Advanced)
- Target Market (SMB ↔ Enterprise)
- Approach (Traditional ↔ Innovative)
- Focus (Generalist ↔ Specialist)

```
                        [Dimension 2 - High]
                              │
              Quadrant 1      │      Quadrant 2
           (Low/High)        │      (High/High)
                              │
                              │
  [Dimension 1 - Low] ────────┼──────── [Dimension 1 - High]
                              │
                              │
              Quadrant 3      │      Quadrant 4
           (Low/Low)         │      (High/Low)
                              │
                        [Dimension 2 - Low]
```

**Place each competitor and [specify company_name] on the map.**

### 4.2 Competitive Threat Scoring

| Competitor | Market Share | Ad Aggressiveness | Brand Strength | Innovation | **Threat Score** |
|------------|-------------|-------------------|----------------|------------|------------------|
| [Name] | /10 | /10 | /10 | /10 | /40 |

**Scoring Guide:**
- Market Share: Estimated share of target market (1=tiny, 10=dominant)
- Ad Aggressiveness: Volume and frequency of advertising (1=minimal, 10=saturating)
- Brand Strength: Recognition and reputation (1=unknown, 10=household name)
- Innovation: Product/service innovation pace (1=stagnant, 10=cutting-edge)

### 4.3 Competitive SWOT per Competitor

For top 3 competitors:

**[Competitor Name] SWOT:**
| Strengths | Weaknesses |
|-----------|------------|
| • [Strength 1] | • [Weakness 1] |
| • [Strength 2] | • [Weakness 2] |

| Opportunities | Threats |
|---------------|---------|
| • [Opportunity for them] | • [Threat to them] |

---

## Output Format

```
================================================================================
                    COMPETITIVE INTELLIGENCE REPORT
                    [specify company_name] - [specify industry]
                    Generated: [Date]
================================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Competitive Landscape Overview:**
[2-3 sentence summary of the competitive environment, key players, and market dynamics]

**[specify company_name]'s Competitive Position:**
[Assessment of current position: leader/challenger/niche player/new entrant]

**Top 3 Competitive Threats:**
1. 🔴 [Competitor] - [Why they're a threat] - Threat Level: [High/Medium]
2. 🟡 [Competitor] - [Why they're a threat] - Threat Level: [Medium]
3. 🟡 [Competitor] - [Why they're a threat] - Threat Level: [Medium/Low]

**Key Opportunities Identified:**
1. [Opportunity 1 - gap in competitor coverage]
2. [Opportunity 2 - underserved segment]
3. [Opportunity 3 - messaging/positioning opportunity]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👥 COMPETITOR PROFILES
──────────────────────

### Competitor 1: [Name]

| Attribute | Details |
|-----------|---------|
| Website | [URL] |
| Founded | [Year] |
| Size | [Employees / Revenue] |
| Funding | [Stage / Amount] |
| Headquarters | [Location] |
| Markets | [Geographic focus] |

**Products/Services:**
- [Product 1]: [Brief description]
- [Product 2]: [Brief description]

**Target Audience:** [Primary customer segments]

**Positioning:** [How they position themselves]

**Unique Value Proposition:** "[Their main value prop]"

**Strengths:**
• [Strength 1]
• [Strength 2]
• [Strength 3]

**Weaknesses:**
• [Weakness 1]
• [Weakness 2]

**Recent Moves:**
- [Recent news/development 1]
- [Recent news/development 2]

---

### Competitor 2: [Name]
[Repeat format]

---

### Competitor 3: [Name]
[Repeat format]

📊 COMPETITIVE POSITIONING MAP
─────────────────────────────

[Describe the positioning map with axes and placements]

**Axes Used:**
- X-axis: [Dimension 1] (Low → High)
- Y-axis: [Dimension 2] (Low → High)

**Positioning:**
| Company | X Position | Y Position | Quadrant |
|---------|-----------|-----------|----------|
| [specify company_name] | [Low/Mid/High] | [Low/Mid/High] | [Description] |
| [Competitor 1] | [Low/Mid/High] | [Low/Mid/High] | [Description] |
| [Competitor 2] | [Low/Mid/High] | [Low/Mid/High] | [Description] |

**White Space Opportunities:**
- [Quadrant/position with no or few competitors]
- [Underserved positioning option]

📢 ADVERTISING STRATEGY ANALYSIS
─────────────────────────────────

### Ad Presence Overview

| Competitor | Meta Ads | Google Ads | LinkedIn | TikTok | Est. Monthly Spend |
|------------|----------|------------|----------|--------|-------------------|
| [Comp 1] | XX active | [Visible/Not] | [Y/N] | [Y/N] | €XX,XXX |
| [Comp 2] | XX active | [Visible/Not] | [Y/N] | [Y/N] | €XX,XXX |
| [Comp 3] | XX active | [Visible/Not] | [Y/N] | [Y/N] | €XX,XXX |
| **[specify company_name]** | XX active | [Visible/Not] | [Y/N] | [Y/N] | €XX,XXX |

### Creative Strategy Breakdown

**Meta Ads Creative Patterns:**
| Competitor | Primary Format | Visual Style | Key Messages | CTAs |
|------------|---------------|--------------|--------------|------|
| [Comp 1] | [Video/Image/Carousel] | [Style] | [Theme] | [CTA] |
| [Comp 2] | [Video/Image/Carousel] | [Style] | [Theme] | [CTA] |

**Top Performing Creative Themes (Industry-Wide):**
1. [Theme 1] - Used by [Competitors]
2. [Theme 2] - Used by [Competitors]
3. [Theme 3] - Underutilized opportunity

**Landing Page Strategy:**
| Competitor | Primary LP Type | Key Elements | Conversion Focus |
|------------|----------------|--------------|------------------|
| [Comp 1] | [Type] | [Elements] | [Focus] |
| [Comp 2] | [Type] | [Elements] | [Focus] |


### Google Ads Auction Insights

**Your Competitive Position:**
| Metric | Your Score | Industry Benchmark | Status |
|--------|-----------|-------------------|--------|
| Search Impression Share | XX% | XX% | [Good/Improve] |
| Top of Page Rate | XX% | XX% | [Good/Improve] |
| Absolute Top Rate | XX% | XX% | [Good/Improve] |
| Avg. Outranking Share | XX% | - | - |

**Top Search Competitors:**
| Competitor | Overlap Rate | Position Above | Outranking | Threat Level |
|------------|-------------|----------------|------------|--------------|
| [Domain 1] | XX% | XX% | XX% | [High/Med/Low] |
| [Domain 2] | XX% | XX% | XX% | [High/Med/Low] |
| [Domain 3] | XX% | XX% | XX% | [High/Med/Low] |

**Interpretation:**
- Your strongest position: [Where you win]
- Greatest competitive pressure: [Where you lose]
- Budget implication: [What this means for spend]


⚔️ COMPETITIVE THREAT MATRIX
────────────────────────────

| Competitor | Market Share | Ad Aggressiveness | Brand Strength | Innovation | **Total /40** | Trend |
|------------|-------------|-------------------|----------------|------------|--------------|-------|
| [Comp 1] | X/10 | X/10 | X/10 | X/10 | **XX** | ↑↓→ |
| [Comp 2] | X/10 | X/10 | X/10 | X/10 | **XX** | ↑↓→ |
| [Comp 3] | X/10 | X/10 | X/10 | X/10 | **XX** | ↑↓→ |

**Threat Level Guide:**
- 30-40: Critical threat - monitor closely, prepare defensive strategy
- 20-29: Significant threat - track regularly, develop counter-positioning
- 10-19: Moderate threat - periodic monitoring sufficient
- <10: Low threat - awareness only

💡 STRATEGIC RECOMMENDATIONS
────────────────────────────

### Defensive Priorities

**1. [Recommendation Title]**
- Threat: [What competitor threat this addresses]
- Action: [Specific action to take]
- Channels: [Which ad platforms]
- Investment: [Budget implication]
- Timeline: [When to implement]

**2. [Recommendation Title]**
- Threat: [What competitor threat this addresses]
- Action: [Specific action to take]

### Offensive Opportunities

**1. [Opportunity Title]**
- Gap: [Market/messaging gap identified]
- Competitors missing: [Who isn't addressing this]
- Target audience: [Who would respond]
- Recommended approach: [How to capitalize]
- Est. investment: [Budget range]

**2. [Opportunity Title]**
- Gap: [Market/messaging gap identified]
- Recommended approach: [How to capitalize]

### Messaging Differentiation

**Competitor Messaging Themes:**
| Competitor | Primary Message | Secondary Message |
|------------|----------------|-------------------|
| [Comp 1] | "[Message]" | "[Message]" |
| [Comp 2] | "[Message]" | "[Message]" |

**[specify company_name] Differentiation Opportunities:**
| Angle | Why It Works | Competitors Not Using |
|-------|-------------|----------------------|
| [Angle 1] | [Rationale] | [Which competitors] |
| [Angle 2] | [Rationale] | [Which competitors] |

**Suggested Positioning Statement:**
"For [target audience] who [need/pain point], [specify company_name] is the [category] that [key differentiator]. Unlike [competitors], we [unique benefit]."

📊 BUDGET BENCHMARKING
──────────────────────

**Industry Ad Spend Benchmarks ([specify industry]):**
| Company Stage | Monthly Ad Budget | % of Revenue |
|---------------|-------------------|--------------|
| Startup | €5,000 - €20,000 | 15-25% |
| Growth | €20,000 - €100,000 | 10-20% |
| Established | €100,000+ | 5-15% |

**Competitive Spend Analysis:**
- Total competitor monthly spend (estimated): €XXX,XXX
- [specify company_name]'s current spend: €XX,XXX (XX% of competitors)
- Share of voice estimate: XX%

**Budget Recommendations:**
| Scenario | Monthly Budget | Expected SOV | Competitive Position |
|----------|---------------|--------------|---------------------|
| Maintain | €XX,XXX | XX% | Current position |
| Grow | €XX,XXX | XX% | Match top competitor |
| Dominate | €XX,XXX | XX% | Market leader position |

📋 NEXT STEPS & MONITORING
──────────────────────────

**Immediate Actions (This Week):**
1. [ ] [Action 1]
2. [ ] [Action 2]
3. [ ] [Action 3]

**Monthly Monitoring Checklist:**
- [ ] Check Meta Ad Library for new competitor ads
- [ ] Review auction insights (if Google Ads connected)
- [ ] Update competitor spend estimates
- [ ] Track competitor landing page changes
- [ ] Monitor competitor news and announcements

**Quarterly Deep Dive:**
- [ ] Full positioning map update
- [ ] Threat matrix reassessment
- [ ] Strategy effectiveness review

💡 SUGGESTED WORKFLOWS TO RUN NEXT
───────────────────────────────────
Based on this competitive analysis, consider:
- [ ] Cross-Platform Comparison (understand your own performance baseline)
- [ ] Landing Page Analyzer (compare your LPs to competitors)
- [ ] Buyer Persona Builder (define target audiences based on competitive gaps)
- [ ] Market Sizing (quantify the opportunity in underserved segments)
```

---

## Competitive Focus Deep Dives

{% if competitive_focus == "ad_creative" %}
### Deep Dive: Ad Creative Analysis

For each competitor, document:

**Video Ads:**
| Competitor | Video Count | Avg Length | Hook Style | CTA Style |
|------------|------------|-----------|-----------|----------|
| [Comp] | XX | XX sec | [Type] | [Type] |

**Hook Types to Analyze:**
- Question hook: "Are you struggling with...?"
- Statistic hook: "87% of companies..."
- Problem hook: "Tired of...?"
- Benefit hook: "Get [result] in [time]"
- Testimonial hook: "How [customer] achieved..."

**Image Ads:**
| Competitor | Image Count | Visual Style | Text Overlay |
|------------|------------|-------------|--------------|
| [Comp] | XX | [Style] | [Y/N] |

**Creative Testing Patterns:**
- How many variants per concept?
- Creative refresh frequency?
- Seasonal vs evergreen ratio?


{% if competitive_focus == "pricing" %}
### Deep Dive: Pricing Strategy

| Competitor | Pricing Model | Entry Price | Mid Tier | Enterprise |
|------------|--------------|------------|---------|-----------|
| [Comp 1] | [Model] | €XX/mo | €XX/mo | Custom |
| [Comp 2] | [Model] | €XX/mo | €XX/mo | Custom |

**Pricing Model Types:**
- Per seat/user
- Usage-based
- Flat rate
- Freemium
- Free trial + paid

**Price Anchoring Analysis:**
- Who is the price leader?
- Who positions as premium?
- Who competes on value?


{% if competitive_focus == "messaging" %}
### Deep Dive: Messaging Analysis

**Taglines & Headlines:**
| Competitor | Primary Tagline | Key Headlines |
|------------|----------------|---------------|
| [Comp] | "[Tagline]" | "[Headlines used in ads]" |

**Benefit Claims:**
| Competitor | Primary Benefit | Proof Points |
|------------|----------------|--------------|
| [Comp] | "[Benefit]" | [How they prove it] |

**Emotional vs Rational Appeals:**
| Competitor | Primary Appeal | Examples |
|------------|---------------|----------|
| [Comp] | [Emotional/Rational/Both] | [Examples] |

**Message Testing Opportunities:**
- Underutilized emotional angles
- Proof points competitors miss
- Audience segments not addressed
---
description: AI-powered channel selection advisor that matches campaign objectives with optimal platform mix. Analyzes audience fit, platform strengths, funnel stage requirements, and budget constraints to recommend the ideal channel strategy. Includes budget allocation suggestions and expected performance benchmarks per channel. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Strategic Channel Selection & Media Mix Planning

Create a comprehensive channel strategy recommendation for [specify company_name].

## Overview

This workflow guides strategic decisions about which advertising platforms to use, how to allocate budget across channels, and what to expect from each platform based on campaign objectives and audience characteristics.

## Parameters
- Company: [specify company_name]
- Industry: [specify industry]
- Primary Objective: [specify primary_objective]
- Monthly Budget: €10,000
- Target Audience: To be analyzed
- Geographic Focus: Netherlands / Europe
- Current Channels: [specify existing_channels]
- Product Type: [specify product_type]
- Sales Cycle: [specify sales_cycle]

---

## PHASE 1: Campaign Objective Analysis

### Objective Classification

**Primary Objective: [specify primary_objective]**

{% if primary_objective == "awareness" %}
#### Awareness Objective Profile
- **Goal**: Maximize reach and brand visibility
- **Key Metrics**: Reach, Impressions, CPM, Brand Lift
- **Funnel Stage**: Top of Funnel (TOFU)
- **Recommended Channels**: Meta (broad reach), TikTok (viral potential), Google Display, YouTube
- **Budget Efficiency**: Lower CPM channels, broad targeting

{% elif primary_objective == "consideration" %}
#### Consideration Objective Profile
- **Goal**: Drive engagement and intent signals
- **Key Metrics**: Clicks, CTR, Video Views, Engagement Rate, Site Traffic
- **Funnel Stage**: Middle of Funnel (MOFU)
- **Recommended Channels**: Meta (engagement), Google Search (intent), LinkedIn (B2B research), TikTok (engagement)
- **Budget Efficiency**: Balance reach and engagement quality

{% elif primary_objective == "conversion" %}
#### Conversion Objective Profile
- **Goal**: Drive purchases, leads, or signups
- **Key Metrics**: Conversions, CPA, ROAS, Conversion Rate
- **Funnel Stage**: Bottom of Funnel (BOFU)
- **Recommended Channels**: Google Search (high intent), Meta (retargeting), LinkedIn (B2B leads)
- **Budget Efficiency**: Performance-based, focus on ROAS/CPA targets

{% elif primary_objective == "lead_generation" %}
#### Lead Generation Objective Profile
- **Goal**: Capture qualified leads for sales pipeline
- **Key Metrics**: Leads, CPL, Lead Quality Score, SQL Rate
- **Funnel Stage**: Middle-to-Bottom Funnel
- **Recommended Channels**: LinkedIn (B2B), Meta Lead Ads, Google Search
- **Budget Efficiency**: CPL optimization, quality over volume

{% elif primary_objective == "app_install" %}
#### App Install Objective Profile
- **Goal**: Drive mobile app downloads
- **Key Metrics**: Installs, CPI, Day 1/7/30 Retention, ARPU
- **Funnel Stage**: Acquisition
- **Recommended Channels**: Meta (app installs), TikTok (app installs), Google App Campaigns
- **Budget Efficiency**: CPI targets, post-install engagement


#### Full-Funnel Objective Profile
- **Goal**: Balanced approach across awareness, consideration, and conversion
- **Key Metrics**: Blended ROAS, incrementality, brand + performance mix
- **Funnel Stage**: All stages
- **Recommended Channels**: Multi-platform presence
- **Budget Efficiency**: 60/20/20 or 70/20/10 split (awareness/consideration/conversion)


---

## PHASE 2: Audience-Channel Fit Analysis

### Target Audience Profile

**Audience Description:** Analyze based on industry and product type

{% if product_type == "b2b_saas" or product_type == "b2b_services" %}
### B2B Audience Channel Fit

| Platform | Audience Fit | Why |
|----------|-------------|-----|
| **LinkedIn** | ⭐⭐⭐⭐⭐ Excellent | Best B2B targeting (job title, company, industry), professional intent |
| **Google Search** | ⭐⭐⭐⭐⭐ Excellent | Captures active research intent, keyword targeting |
| **Meta (Facebook/IG)** | ⭐⭐⭐ Good | Large reach, but B2B targeting less precise |
| **TikTok** | ⭐⭐ Limited | Growing B2B presence but primarily B2C platform |
| **Google Display** | ⭐⭐⭐ Good | Retargeting and account-based targeting |

**B2B Channel Recommendation:** LinkedIn + Google Search as primary, Meta for retargeting

{% elif product_type == "d2c_ecommerce" or product_type == "b2c_product" %}
### D2C/E-commerce Audience Channel Fit

| Platform | Audience Fit | Why |
|----------|-------------|-----|
| **Meta (Facebook/IG)** | ⭐⭐⭐⭐⭐ Excellent | Visual products, shopping features, broad reach |
| **TikTok** | ⭐⭐⭐⭐⭐ Excellent | Viral discovery, TikTok Shop, younger demos |
| **Google Search** | ⭐⭐⭐⭐ Very Good | Captures search intent, Shopping campaigns |
| **Google Shopping** | ⭐⭐⭐⭐⭐ Excellent | High purchase intent, product visibility |
| **LinkedIn** | ⭐ Poor | Not suited for consumer products |

**E-commerce Channel Recommendation:** Meta + Google Shopping as primary, TikTok for discovery

{% elif product_type == "local_business" %}
### Local Business Audience Channel Fit

| Platform | Audience Fit | Why |
|----------|-------------|-----|
| **Google Search** | ⭐⭐⭐⭐⭐ Excellent | "Near me" searches, local intent |
| **Meta (Facebook/IG)** | ⭐⭐⭐⭐ Very Good | Local targeting, community engagement |
| **Google Local/Maps** | ⭐⭐⭐⭐⭐ Excellent | Direct to business location |
| **TikTok** | ⭐⭐⭐ Good | Local discovery, especially for food/entertainment |
| **LinkedIn** | ⭐⭐ Limited | Only for B2B local services |

**Local Business Channel Recommendation:** Google Search/Local + Meta for awareness


### General Audience Channel Fit Analysis

Analyze audience fit based on:

| Factor | Meta | Google Search | LinkedIn | TikTok |
|--------|------|--------------|----------|--------|
| Age 18-24 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Age 25-34 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Age 35-54 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Age 55+ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐ |
| B2B Decision Makers | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Consumers | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Visual Products | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Services | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |


### Geographic Considerations (Netherlands / Europe)

| Platform | Netherlands / Europe Reach | Notes |
|----------|---------------------------|-------|
| Meta | ~10M users (NL), 400M+ (EU) | Strong in all EU markets |
| Google | ~95% search market share | Dominant search platform |
| LinkedIn | ~9M users (NL), 300M+ (EMEA) | Strong B2B coverage |
| TikTok | ~4M users (NL), growing fast | Especially strong <35 demographics |

---

## PHASE 3: Platform Strengths & Weaknesses

### Platform Capability Matrix

| Capability | Meta | Google Search | Google Display | LinkedIn | TikTok |
|------------|------|--------------|----------------|----------|--------|
| **Awareness** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Consideration** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Conversion** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **B2B Targeting** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **B2C Targeting** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Retargeting** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Video Ads** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ (YouTube) | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Shopping/E-com** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐⭐⭐ |
| **Lead Gen** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Brand Building** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Attribution** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

### Platform-Specific Strengths

**Meta (Facebook/Instagram):**
- Best for: Visual products, broad audiences, lookalike audiences
- Minimum budget: €1,000/month (meaningful learning)
- Learning phase: ~50 conversions/week per ad set
- Creative needs: High (creative fatigue in 10-14 days)

**Google Search:**
- Best for: High-intent keywords, bottom-funnel, competitive industries
- Minimum budget: €500/month for testing, €2,000+ for competitive verticals
- Learning phase: Continuous optimization
- Creative needs: Low (text ads), ad extensions important

**LinkedIn:**
- Best for: B2B, professional services, high-ticket items
- Minimum budget: €2,000/month (high CPCs)
- Learning phase: Slower, smaller audiences
- Creative needs: Medium (professional content)

**TikTok:**
- Best for: Brand awareness, younger demographics, viral content
- Minimum budget: €1,000/month
- Learning phase: Faster creative fatigue (4x Meta)
- Creative needs: Very high (native content, frequent refresh)

---

## PHASE 4: Budget Allocation Framework

### Monthly Budget: €10,000

{% if primary_objective == "awareness" %}
### Recommended Allocation: Awareness Focus

| Channel | Allocation | Budget | Rationale |
|---------|-----------|--------|-----------|
| **Meta** | 40% | €{{ (monthly_budget | default(10000) | float * 0.4) | round | int }} | Broad reach, cost-efficient CPM |
| **TikTok** | 30% | €{{ (monthly_budget | default(10000) | float * 0.3) | round | int }} | Viral potential, younger audiences |
| **Google Display/YouTube** | 20% | €{{ (monthly_budget | default(10000) | float * 0.2) | round | int }} | Video reach, brand safety |
| **LinkedIn** | 10% | €{{ (monthly_budget | default(10000) | float * 0.1) | round | int }} | Professional awareness (if B2B element) |

{% elif primary_objective == "consideration" %}
### Recommended Allocation: Consideration Focus

| Channel | Allocation | Budget | Rationale |
|---------|-----------|--------|-----------|
| **Meta** | 35% | €{{ (monthly_budget | default(10000) | float * 0.35) | round | int }} | Engagement, video views, traffic |
| **Google Search** | 30% | €{{ (monthly_budget | default(10000) | float * 0.3) | round | int }} | Research-phase keywords |
| **TikTok** | 20% | €{{ (monthly_budget | default(10000) | float * 0.2) | round | int }} | Engagement and consideration content |
| **LinkedIn** | 15% | €{{ (monthly_budget | default(10000) | float * 0.15) | round | int }} | Content engagement (B2B) |

{% elif primary_objective == "conversion" or primary_objective == "lead_generation" %}
### Recommended Allocation: Conversion/Lead Gen Focus

| Channel | Allocation | Budget | Rationale |
|---------|-----------|--------|-----------|
| **Google Search** | 40% | €{{ (monthly_budget | default(10000) | float * 0.4) | round | int }} | Highest intent, proven conversion |
| **Meta** | 35% | €{{ (monthly_budget | default(10000) | float * 0.35) | round | int }} | Retargeting, lookalikes, lead ads |
{% if product_type == "b2b_saas" or product_type == "b2b_services" %}| **LinkedIn** | 20% | €{{ (monthly_budget | default(10000) | float * 0.2) | round | int }} | B2B leads, professional targeting |
| **TikTok** | 5% | €{{ (monthly_budget | default(10000) | float * 0.05) | round | int }} | Testing/brand (optional) |
| **TikTok** | 15% | €{{ (monthly_budget | default(10000) | float * 0.15) | round | int }} | Conversion campaigns, Shop |
| **LinkedIn** | 10% | €{{ (monthly_budget | default(10000) | float * 0.1) | round | int }} | If any B2B component |



### Recommended Allocation: Full-Funnel (Balanced)

| Channel | Allocation | Budget | Rationale |
|---------|-----------|--------|-----------|
| **Meta** | 35% | €{{ (monthly_budget | default(10000) | float * 0.35) | round | int }} | Versatile, all funnel stages |
| **Google Search** | 30% | €{{ (monthly_budget | default(10000) | float * 0.3) | round | int }} | Intent capture, conversion |
| **TikTok** | 20% | €{{ (monthly_budget | default(10000) | float * 0.2) | round | int }} | Awareness, discovery |
| **LinkedIn** | 15% | €{{ (monthly_budget | default(10000) | float * 0.15) | round | int }} | B2B component |


### Budget Thresholds by Channel

| Channel | Minimum Viable | Recommended | Optimal |
|---------|---------------|-------------|---------|
| Meta | €1,000/mo | €3,000/mo | €10,000+/mo |
| Google Search | €500/mo | €2,000/mo | €5,000+/mo |
| LinkedIn | €2,000/mo | €5,000/mo | €15,000+/mo |
| TikTok | €1,000/mo | €3,000/mo | €10,000+/mo |

⚠️ **Budget Warning:**
{% if monthly_budget | default(10000) | float < 3000 %}
With a budget under €3,000/month, focus on **1-2 channels maximum** to achieve meaningful results. Spreading too thin leads to insufficient learning data.
{% elif monthly_budget | default(10000) | float < 5000 %}
With a budget of €3,000-€5,000/month, limit to **2-3 channels** and prioritize based on your primary objective.
{% elif monthly_budget | default(10000) | float < 10000 %}
With a budget of €5,000-€10,000/month, you can test **3-4 channels** but should still prioritize.

With a budget of €10,000+/month, a **full multi-channel strategy** is viable with proper allocation.


---

## PHASE 5: Expected Performance Benchmarks

### [specify industry] Industry Benchmarks

| Metric | Meta | Google Search | LinkedIn | TikTok |
|--------|------|--------------|----------|--------|
| **CPM** | €8-15 | €15-40 | €30-60 | €5-12 |
| **CPC** | €0.50-2.00 | €1.00-5.00 | €3.00-8.00 | €0.30-1.50 |
| **CTR** | 1.0-2.0% | 2.0-5.0% | 0.4-0.8% | 1.0-3.0% |
| **Conversion Rate** | 2-5% | 3-8% | 2-6% | 1-3% |
| **CPL (B2B)** | €30-80 | €40-100 | €50-150 | €40-100 |
| **CPA (E-com)** | €15-50 | €20-60 | N/A | €15-45 |
| **ROAS (E-com)** | 3-6x | 4-8x | N/A | 2-5x |

### Expected Results for €10,000/month

Based on the recommended allocation:

{% if primary_objective == "awareness" %}
| Channel | Budget | Expected Reach | Expected CPM |
|---------|--------|----------------|--------------|
| Meta | €{{ (monthly_budget | default(10000) | float * 0.4) | round | int }} | {{ ((monthly_budget | default(10000) | float * 0.4) / 10 * 1000) | round | int | string }}+ | €8-12 |
| TikTok | €{{ (monthly_budget | default(10000) | float * 0.3) | round | int }} | {{ ((monthly_budget | default(10000) | float * 0.3) / 8 * 1000) | round | int | string }}+ | €5-10 |
| Display/YouTube | €{{ (monthly_budget | default(10000) | float * 0.2) | round | int }} | {{ ((monthly_budget | default(10000) | float * 0.2) / 15 * 1000) | round | int | string }}+ | €10-20 |

{% elif primary_objective == "conversion" or primary_objective == "lead_generation" %}
| Channel | Budget | Expected Leads/Conv. | Expected CPA/CPL |
|---------|--------|---------------------|------------------|
| Google Search | €{{ (monthly_budget | default(10000) | float * 0.4) | round | int }} | {{ ((monthly_budget | default(10000) | float * 0.4) / 50) | round | int }}-{{ ((monthly_budget | default(10000) | float * 0.4) / 30) | round | int }} | €30-50 |
| Meta | €{{ (monthly_budget | default(10000) | float * 0.35) | round | int }} | {{ ((monthly_budget | default(10000) | float * 0.35) / 45) | round | int }}-{{ ((monthly_budget | default(10000) | float * 0.35) / 25) | round | int }} | €25-45 |
| LinkedIn/TikTok | €{{ (monthly_budget | default(10000) | float * 0.25) | round | int }} | {{ ((monthly_budget | default(10000) | float * 0.25) / 80) | round | int }}-{{ ((monthly_budget | default(10000) | float * 0.25) / 40) | round | int }} | €40-80 |


| Channel | Budget | Primary Metric | Expected Range |
|---------|--------|----------------|----------------|
| Meta | €{{ (monthly_budget | default(10000) | float * 0.35) | round | int }} | Blended | 3-5x ROAS |
| Google Search | €{{ (monthly_budget | default(10000) | float * 0.3) | round | int }} | Conversions | 4-6x ROAS |
| TikTok | €{{ (monthly_budget | default(10000) | float * 0.2) | round | int }} | Reach + Conv. | 2-4x ROAS |
| LinkedIn | €{{ (monthly_budget | default(10000) | float * 0.15) | round | int }} | Leads | €50-100 CPL |


---

## Output Format

```
================================================================================
                    CHANNEL STRATEGY RECOMMENDATION
                    [specify company_name] - [specify industry]
                    Objective: [specify primary_objective]
                    Budget: €10,000/month
================================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Recommended Channel Mix:**
[Summarize the top 2-3 channels and why they fit this situation]

**Budget Allocation:**
| Channel | Allocation | Monthly Budget |
|---------|-----------|----------------|
| [Primary Channel] | XX% | €X,XXX |
| [Secondary Channel] | XX% | €X,XXX |
| [Tertiary Channel] | XX% | €X,XXX |

**Key Insight:**
[One-sentence strategic insight about the recommended approach]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 CHANNEL RECOMMENDATIONS BY PRIORITY
─────────────────────────────────────

### Priority 1: [Channel Name] ⭐
**Allocation:** XX% (€X,XXX/month)

**Why This Channel:**
- [Reason 1 related to objective]
- [Reason 2 related to audience]
- [Reason 3 related to platform strength]

**Campaign Types to Run:**
- [Campaign type 1]
- [Campaign type 2]

**Expected Results:**
- [Metric 1]: [Expected range]
- [Metric 2]: [Expected range]

**Success Criteria:**
- [KPI target 1]
- [KPI target 2]

---

### Priority 2: [Channel Name]
[Repeat format]

---

### Priority 3: [Channel Name]
[Repeat format]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 EXPECTED PERFORMANCE SUMMARY
───────────────────────────────

| Channel | Monthly Spend | Expected Output | Efficiency Metric |
|---------|--------------|-----------------|-------------------|
| [Ch 1] | €X,XXX | [Output] | [CPA/ROAS/CPM] |
| [Ch 2] | €X,XXX | [Output] | [CPA/ROAS/CPM] |
| [Ch 3] | €X,XXX | [Output] | [CPA/ROAS/CPM] |
| **Total** | **€X,XXX** | **[Total output]** | **[Blended metric]** |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ CHANNELS NOT RECOMMENDED (AND WHY)
─────────────────────────────────────

| Channel | Reason Not Recommended |
|---------|----------------------|
| [Channel] | [Specific reason - audience mismatch, budget constraint, objective mismatch] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 IMPLEMENTATION ROADMAP
─────────────────────────

**Week 1-2: Launch Phase**
- [ ] Set up tracking (pixels, conversion events)
- [ ] Create initial campaigns on priority channels
- [ ] Establish baseline metrics

**Week 3-4: Optimization Phase**
- [ ] Review initial performance data
- [ ] Adjust bids and budgets
- [ ] Test creative variations

**Month 2: Scale Phase**
- [ ] Double down on winning channels
- [ ] Reduce or pause underperformers
- [ ] Consider adding secondary channels

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 SUGGESTED NEXT WORKFLOWS
────────────────────────────

Based on this channel strategy, consider running:
- [ ] **Budget Allocation Planner** - Detailed scenario planning for budget distribution
- [ ] **Performance Forecaster** - Project expected results with confidence intervals
- [ ] **Buyer Persona Builder** - Deep dive on target audience for each channel
- [ ] **Competitive Landscape Analyzer** - Understand competitor channel presence
```

---

## Additional Considerations

### Seasonality Impact on Channel Selection

| Season/Event | Impact on Meta | Impact on Google | Impact on LinkedIn | Impact on TikTok |
|--------------|---------------|-----------------|-------------------|-----------------|
| Q4 (Holiday) | CPM +30-50% | CPC +20-40% | Minimal | CPM +20-30% |
| Q1 (New Year) | CPM -10-20% | CPC stable | CPC +10-20% | CPM stable |
| Summer | CPM -5-15% | CPC -5-10% | CPC -10-20% | Engagement ↑ |
| Black Friday | CPM +50-100% | CPC +30-50% | Minimal | CPM +30-50% |


### Sales Cycle Consideration: [specify sales_cycle]

{% if sales_cycle == "short" or sales_cycle == "impulse" %}
**Short/Impulse Sales Cycle:**
- Focus on conversion-oriented channels (Google Search, Meta retargeting)
- Shorter attribution windows (7-14 days)
- Heavier bottom-funnel investment
{% elif sales_cycle == "long" or sales_cycle == "considered" %}
**Long/Considered Sales Cycle:**
- Multi-touch attribution required
- Upper-funnel investment important (awareness builds pipeline)
- LinkedIn particularly valuable for B2B
- Expect 30-90 day conversion windows
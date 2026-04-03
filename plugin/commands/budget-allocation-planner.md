---
description: Forward-looking budget planning with scenario modeling (conservative/realistic/aggressive). Integrates market sizing data, competitive share of voice analysis, and platform-specific budget thresholds. Outputs optimal budget distribution across channels with confidence levels and expected ROI ranges. Different from budget-pacing-monitor which tracks actual spend vs. budget. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Strategic Budget Planning & Scenario Modeling

Develop comprehensive budget allocation plan for [specify company_name] with scenario analysis.

## Overview

This workflow creates a strategic budget plan with three scenarios (conservative, realistic, aggressive) that accounts for market opportunity, competitive landscape, and platform-specific requirements. Different from tracking workflows - this is forward-planning, not monitoring.

## Parameters
- Company: [specify company_name]
- Industry: [specify industry]
- Planning Period: Q1 2026
- Total Available Budget: €30,000
- Primary Objective: growth
- Current Monthly Performance: [specify current_performance]
- Addressable Market Size: [specify market_size]
- Estimated Competitor Spend: [specify competitor_spend]
- Historical ROAS: [specify historical_roas]
- Target CPA: [specify target_cpa]

---

## PHASE 1: Budget Context Analysis

### Available Budget Assessment

**Total Planning Budget:** €30,000
**Planning Period:** Q1 2026

{% set monthly_budget = (total_budget | default(30000) | float / 3) %}

**Monthly Budget Available:** €{{ monthly_budget | round | int }}

### Budget Classification

| Budget Level | Monthly Range | Strategy Focus |
|--------------|---------------|----------------|
| **Startup/Test** | €1,000 - €5,000 | Single channel focus, validate product-market fit |
| **Growth** | €5,000 - €20,000 | 2-3 channels, scaling winners |
| **Scale** | €20,000 - €100,000 | Multi-channel, market expansion |
| **Enterprise** | €100,000+ | Full-funnel, brand + performance |

{% if monthly_budget < 5000 %}
**Your Category:** Startup/Test Phase
- Recommendation: Focus on 1-2 channels maximum
- Priority: Validation over scale
{% elif monthly_budget < 20000 %}
**Your Category:** Growth Phase
- Recommendation: Test 2-3 channels, double down on winners
- Priority: Efficient scaling
{% elif monthly_budget < 100000 %}
**Your Category:** Scale Phase
- Recommendation: Multi-channel strategy with clear attribution
- Priority: Market share growth

**Your Category:** Enterprise Phase
- Recommendation: Full-funnel with brand investment
- Priority: Sustainable competitive advantage


---

## PHASE 2: Market Opportunity Sizing


### Provided Market Context
**Addressable Market:** [specify market_size]

### Market Sizing Research Required

**Research Prompts for Market Sizing:**

```
Research market size for [specify industry] in Netherlands / Europe:
1. Total Addressable Market (TAM) for the industry
2. Serviceable Addressable Market (SAM) for [specify company_name]'s specific segment
3. Number of potential customers/businesses in target segment
4. Average customer value / transaction size
5. Industry growth rate (2024-2026)
```

**Quick Market Estimation Framework:**

| Approach | Formula | Notes |
|----------|---------|-------|
| Top-Down | Total Market × Your Segment % | Start with industry reports |
| Bottom-Up | Customers × Avg Value × Frequency | More accurate for specific niches |
| Competitor-Based | Total Competitor Revenue × (1/Market Share) | If competitor data available |


### Share of Voice Analysis

**SOV-SOM Rule (Ehrenberg-Bass):**
- To **maintain** market share: SOV should equal SOM
- To **grow** market share: SOV should exceed SOM by 5-15 percentage points
- Each 10pp of Excess SOV (ESOV) typically yields ~0.5% market share growth/year


**Competitive Context:**
Estimated competitor spend: [specify competitor_spend]

| Scenario | Your Budget | Est. Market Total | Your SOV |
|----------|-------------|-------------------|----------|
| Conservative | €{{ (monthly_budget * 0.7) | round | int }} | [specify competitor_spend] + your spend | Calculate % |
| Realistic | €{{ monthly_budget | round | int }} | [specify competitor_spend] + your spend | Calculate % |
| Aggressive | €{{ (monthly_budget * 1.3) | round | int }} | [specify competitor_spend] + your spend | Calculate % |

**Estimate Competitor Spend:**

| Industry Benchmark | Typical Monthly Ad Spend |
|-------------------|-------------------------|
| Local SMB | €1,000 - €10,000 |
| Regional Business | €10,000 - €50,000 |
| National Brand | €50,000 - €250,000 |
| Enterprise | €250,000+ |

Use the **Competitive Landscape Analyzer** workflow to estimate competitor spend if unknown.


---

## PHASE 3: Three-Scenario Budget Modeling

### Scenario Definitions

| Scenario | Budget Modifier | Risk Profile | Expected Outcome |
|----------|-----------------|--------------|------------------|
| **Conservative** | 70% of budget | Low risk | Maintain current position, steady growth |
| **Realistic** | 100% of budget | Medium risk | Achieve target growth objectives |
| **Aggressive** | 130% of budget | Higher risk | Accelerated growth, market share gain |

---

### SCENARIO A: Conservative (70% Budget)

**Monthly Budget:** €{{ (monthly_budget * 0.7) | round | int }}
**Quarterly Total:** €{{ (total_budget | default(30000) | float * 0.7) | round | int }}

#### Channel Allocation (Conservative)

| Channel | Allocation | Monthly Budget | Rationale |
|---------|-----------|----------------|-----------|
| **Google Search** | 50% | €{{ (monthly_budget * 0.7 * 0.5) | round | int }} | Highest intent, proven ROI |
| **Meta Retargeting** | 30% | €{{ (monthly_budget * 0.7 * 0.3) | round | int }} | Capture warm audiences only |
| **Brand Protection** | 20% | €{{ (monthly_budget * 0.7 * 0.2) | round | int }} | Defend brand terms |

**Focus Areas:**
- Bottom-funnel only (high-intent converters)
- Existing audiences and retargeting
- Proven keywords and audiences
- No new channel testing

**Expected Outcomes (Conservative):**
| Metric | Expected Range | Confidence |
|--------|---------------|------------|
| ROAS | 3-4x | High (85%) |
| Conversions | Maintain current | High |
| Market Share | Flat to +1% | Medium |
| Risk Level | Low | - |

---

### SCENARIO B: Realistic (100% Budget)

**Monthly Budget:** €{{ monthly_budget | round | int }}
**Quarterly Total:** €{{ total_budget | default(30000) | float | round | int }}

#### Channel Allocation (Realistic)

{% if primary_objective == "growth" or primary_objective == "conversion" %}
| Channel | Allocation | Monthly Budget | Rationale |
|---------|-----------|----------------|-----------|
| **Google Search** | 35% | €{{ (monthly_budget * 0.35) | round | int }} | Core performance driver |
| **Meta** | 30% | €{{ (monthly_budget * 0.30) | round | int }} | Prospecting + retargeting mix |
| **Google Shopping/PMax** | 20% | €{{ (monthly_budget * 0.20) | round | int }} | Product visibility (if e-comm) |
| **LinkedIn/TikTok** | 15% | €{{ (monthly_budget * 0.15) | round | int }} | Channel testing / B2B focus |

{% elif primary_objective == "awareness" %}
| Channel | Allocation | Monthly Budget | Rationale |
|---------|-----------|----------------|-----------|
| **Meta** | 40% | €{{ (monthly_budget * 0.40) | round | int }} | Broad reach, video |
| **TikTok** | 25% | €{{ (monthly_budget * 0.25) | round | int }} | Viral potential |
| **YouTube/Display** | 20% | €{{ (monthly_budget * 0.20) | round | int }} | Video reach |
| **Google Search** | 15% | €{{ (monthly_budget * 0.15) | round | int }} | Brand capture |


| Channel | Allocation | Monthly Budget | Rationale |
|---------|-----------|----------------|-----------|
| **Google Search** | 35% | €{{ (monthly_budget * 0.35) | round | int }} | Intent capture |
| **Meta** | 35% | €{{ (monthly_budget * 0.35) | round | int }} | Full-funnel |
| **LinkedIn** | 20% | €{{ (monthly_budget * 0.20) | round | int }} | B2B targeting |
| **Testing** | 10% | €{{ (monthly_budget * 0.10) | round | int }} | New channel tests |


**Focus Areas:**
- Balanced prospecting and retargeting (70/30)
- Core channels + selective testing
- Creative testing budget included
- Some audience expansion

**Expected Outcomes (Realistic):**
| Metric | Expected Range | Confidence |
|--------|---------------|------------|
| ROAS | 2.5-4x | Medium (70%) |
| Conversions | +20-40% growth | Medium |
| Market Share | +2-5% | Medium |
| Risk Level | Medium | - |

---

### SCENARIO C: Aggressive (130% Budget)

**Monthly Budget:** €{{ (monthly_budget * 1.3) | round | int }}
**Quarterly Total:** €{{ (total_budget | default(30000) | float * 1.3) | round | int }}

#### Channel Allocation (Aggressive)

| Channel | Allocation | Monthly Budget | Rationale |
|---------|-----------|----------------|-----------|
| **Meta** | 30% | €{{ (monthly_budget * 1.3 * 0.30) | round | int }} | Scale prospecting, broad reach |
| **Google Search** | 25% | €{{ (monthly_budget * 1.3 * 0.25) | round | int }} | Expand keyword coverage |
| **TikTok** | 20% | €{{ (monthly_budget * 1.3 * 0.20) | round | int }} | New audience acquisition |
| **LinkedIn** | 15% | €{{ (monthly_budget * 1.3 * 0.15) | round | int }} | B2B market capture |
| **YouTube/Display** | 10% | €{{ (monthly_budget * 1.3 * 0.10) | round | int }} | Brand awareness push |

**Focus Areas:**
- Heavy prospecting (80/20 vs retargeting)
- Multi-channel presence
- Aggressive audience expansion
- Higher-funnel investment
- Market share capture priority

**Expected Outcomes (Aggressive):**
| Metric | Expected Range | Confidence |
|--------|---------------|------------|
| ROAS | 2-3x (lower efficiency) | Lower (55%) |
| Conversions | +50-100% growth | Medium |
| Market Share | +5-10% | Medium-Low |
| Risk Level | Higher | - |

**Warning:** Aggressive scenario may temporarily reduce ROAS as you invest in upper-funnel activities. This is expected and strategic if market share growth is the priority.

---

## PHASE 4: Platform-Specific Budget Thresholds

### Minimum Viable Budgets by Channel

| Channel | Minimum | Why |
|---------|---------|-----|
| **Google Search** | €500/mo | Need volume for algorithm learning |
| **Meta (Facebook/IG)** | €1,000/mo | Learning phase needs ~50 conv/week |
| **LinkedIn** | €2,000/mo | High CPCs require minimum scale |
| **TikTok** | €1,000/mo | Creative testing needs budget |
| **Google Display/YouTube** | €1,500/mo | CPM-based, need reach |

### Recommended Budgets for Meaningful Impact

| Channel | Recommended | Sweet Spot |
|---------|-------------|------------|
| **Google Search** | €2,000-5,000/mo | €5,000-15,000/mo |
| **Meta** | €3,000-8,000/mo | €8,000-25,000/mo |
| **LinkedIn** | €5,000-10,000/mo | €10,000-30,000/mo |
| **TikTok** | €3,000-8,000/mo | €8,000-20,000/mo |

### Budget Constraint Analysis

{% if monthly_budget < 3000 %}
⚠️ **Budget Alert:** At €{{ monthly_budget | round | int }}/month, focus on **ONE channel only**.

**Recommendation:** Start with Google Search (highest intent) or Meta (best reach per €).
{% elif monthly_budget < 5000 %}
⚠️ **Budget Alert:** At €{{ monthly_budget | round | int }}/month, limit to **2 channels maximum**.

**Recommendation:** Google Search + Meta retargeting only.
{% elif monthly_budget < 10000 %}
**Budget Level:** Suitable for **2-3 channels** with focused allocation.

**Recommendation:** Primary channel gets 50%, secondary 30%, testing 20%.

✅ **Budget Level:** Sufficient for **multi-channel strategy** with proper diversification.

**Recommendation:** Allocate to 3-4 channels with clear role for each.


---

## PHASE 5: Quarterly Phasing Plan

### Month-over-Month Budget Phasing

**Recommended Phasing Strategy:**

| Month | % of Quarterly Budget | Focus |
|-------|----------------------|-------|
| Month 1 | 30% | Testing, learning, baseline |
| Month 2 | 35% | Optimization, scale winners |
| Month 3 | 35% | Full scale, capture opportunity |

### Q1 2026 Budget Calendar

#### Realistic Scenario Phasing

| Month | Total Budget | Google | Meta | Other Channels |
|-------|-------------|--------|------|----------------|
| Month 1 | €{{ (total_budget | default(30000) | float * 0.30) | round | int }} | €{{ (total_budget | default(30000) | float * 0.30 * 0.35) | round | int }} | €{{ (total_budget | default(30000) | float * 0.30 * 0.30) | round | int }} | €{{ (total_budget | default(30000) | float * 0.30 * 0.35) | round | int }} |
| Month 2 | €{{ (total_budget | default(30000) | float * 0.35) | round | int }} | €{{ (total_budget | default(30000) | float * 0.35 * 0.35) | round | int }} | €{{ (total_budget | default(30000) | float * 0.35 * 0.30) | round | int }} | €{{ (total_budget | default(30000) | float * 0.35 * 0.35) | round | int }} |
| Month 3 | €{{ (total_budget | default(30000) | float * 0.35) | round | int }} | €{{ (total_budget | default(30000) | float * 0.35 * 0.35) | round | int }} | €{{ (total_budget | default(30000) | float * 0.35 * 0.30) | round | int }} | €{{ (total_budget | default(30000) | float * 0.35 * 0.35) | round | int }} |

### Budget Flexibility Rules

| Trigger | Action |
|---------|--------|
| Channel ROAS > 150% of target | Increase allocation by 20% from underperformers |
| Channel ROAS < 50% of target | Reduce allocation by 30%, redistribute |
| New opportunity identified | Use 10% reserve for testing |
| Seasonal peak approaching | Increase by 20-30% during peak |

---

## Output Format

```
================================================================================
                    BUDGET ALLOCATION PLAN
                    [specify company_name] - Q1 2026
                    Total Budget: €30,000
================================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Recommended Scenario:** [Conservative/Realistic/Aggressive]

**Budget Overview:**
| Period | Budget | Key Focus |
|--------|--------|-----------|
| Q1 2026 | €30,000 | [Primary objective] |

**Channel Mix Summary:**
| Channel | Monthly Budget | Role |
|---------|---------------|------|
| [Primary] | €X,XXX | [Role] |
| [Secondary] | €X,XXX | [Role] |
| [Tertiary] | €X,XXX | [Role] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 SCENARIO COMPARISON
─────────────────────

| Metric | Conservative | Realistic | Aggressive |
|--------|-------------|-----------|------------|
| **Quarterly Budget** | €XX,XXX | €XX,XXX | €XX,XXX |
| **Expected ROAS** | X.Xx | X.Xx | X.Xx |
| **Expected Conv.** | XXX | XXX | XXX |
| **Market Share Impact** | +X% | +X% | +X% |
| **Risk Level** | Low | Medium | High |
| **Confidence** | 85% | 70% | 55% |

**Recommendation Rationale:**
[Explain why you recommend a specific scenario based on company context]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 DETAILED BUDGET BREAKDOWN ([Selected Scenario])
──────────────────────────────────────────────────

### Channel-by-Channel Allocation

**[Channel 1 Name]**
- Monthly Budget: €X,XXX (XX%)
- Role: [Primary conversion / Prospecting / Brand / etc.]
- Campaign Types: [Search / Shopping / Display / etc.]
- Target KPIs: [ROAS X.Xx / CPA €XX / CPL €XX]
- Confidence Level: [High/Medium/Low]

**[Channel 2 Name]**
[Repeat format]

**[Channel 3 Name]**
[Repeat format]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 MONTHLY PHASING
──────────────────

| Month | Total | Google | Meta | LinkedIn | TikTok | Focus |
|-------|-------|--------|------|----------|--------|-------|
| M1 | €X,XXX | €X,XXX | €X,XXX | €X,XXX | €X,XXX | Testing |
| M2 | €X,XXX | €X,XXX | €X,XXX | €X,XXX | €X,XXX | Optimize |
| M3 | €X,XXX | €X,XXX | €X,XXX | €X,XXX | €X,XXX | Scale |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 EXPECTED RETURNS
───────────────────

**ROI Projections (Q1 2026):**

| Scenario | Investment | Expected Revenue | ROAS | Net Return |
|----------|-----------|-----------------|------|------------|
| Conservative | €XX,XXX | €XX,XXX | X.Xx | €XX,XXX |
| Realistic | €XX,XXX | €XX,XXX | X.Xx | €XX,XXX |
| Aggressive | €XX,XXX | €XX,XXX | X.Xx | €XX,XXX |

**Break-Even Analysis:**
- Break-even ROAS: X.Xx (assuming XX% margin)
- Minimum conversions needed: XXX
- Daily conversion target: X.X

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ RISKS & MITIGATIONS
──────────────────────

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | Medium | High | [Mitigation strategy] |
| [Risk 2] | Low | Medium | [Mitigation strategy] |
| [Risk 3] | Medium | Medium | [Mitigation strategy] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 REALLOCATION TRIGGERS
────────────────────────

**When to Shift Budget:**

| Trigger | From | To | Amount |
|---------|------|-----|--------|
| ROAS > 5x sustained | Any | Scale that channel | +25% |
| ROAS < 1.5x for 2 weeks | That channel | Best performer | -30% |
| CPL > 2x target | LinkedIn/TikTok | Google/Meta | -50% |
| Seasonal peak | Even split | Top performers | +30% overall |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 NEXT STEPS
─────────────

1. [ ] Approve budget scenario (Conservative/Realistic/Aggressive)
2. [ ] Set up tracking and attribution model
3. [ ] Create campaign structure per channel
4. [ ] Establish baseline metrics
5. [ ] Schedule weekly budget review checkpoints

**Suggested Follow-up Workflows:**
- [ ] **Performance Forecaster** - Detailed projections with confidence intervals
- [ ] **Budget Pacing Monitor** - Track actual vs. planned spend (weekly)
- [ ] **Channel Strategy Advisor** - Refine channel selection based on data
```

---

## Appendix: Budget Planning Checklist

### Pre-Planning Checklist

- [ ] Historical performance data gathered (last 3-6 months)
- [ ] Current ROAS/CPA baselines documented
- [ ] Target KPIs defined (ROAS, CPA, CPL targets)
- [ ] Market size research completed
- [ ] Competitor spend estimated
- [ ] Seasonal factors identified
- [ ] Attribution model agreed upon

### Budget Approval Checklist

- [ ] Scenario analysis completed
- [ ] Stakeholder alignment on risk level
- [ ] Monthly phasing approved
- [ ] Reallocation rules documented
- [ ] Review cadence established (weekly/monthly)
- [ ] Success metrics defined
---
name: linkedin-bid-strategy-selector
description: "LinkedIn Ads bid strategy advisor voor het kiezen van de optimale biedstrategie. Gebruik voor: (1) Maximum Delivery vs Manual Bidding vs Cost Cap kiezen, (2) CPC vs CPM vs CPL optimalisatie, (3) Budget pacing advies, (4) Bid optimization troubleshooting, (5) High CPL diagnosis. Triggers: linkedin bidding, bid strategy, cost cap, manual bid, maximum delivery, CPC too high, CPL high, delivery issues."
---

# LinkedIn Bid Strategy Selector

Advisor voor het selecteren van de optimale LinkedIn Ads biedstrategie op basis van doelen, budget en account situatie.

## Quick Selection Guide

```
WAT IS JE PRIMAIRE DOEL?
│
├─► Maximaal volume & reach
│   └─► MAXIMUM DELIVERY
│       (Laat LinkedIn optimaliseren)
│
├─► CPL/CPA onder controle houden
│   └─► COST CAP
│       (Target cost met flexibility)
│
└─► Volledige controle over kosten
    └─► MANUAL BIDDING
        (Fixed max bid per result)
```

## Bid Strategy Overview

```
LINKEDIN BID STRATEGIES VERGELIJKING
====================================

Strategy         │ Control │ Risk │ Best For          │ Min. Budget
─────────────────┼─────────┼──────┼───────────────────┼────────────
Maximum Delivery │ Geen    │ Laag │ Beginners, volume │ €25/dag
Cost Cap         │ Target  │ Med  │ CPL constraints   │ €50/dag
Manual Bidding   │ Exact   │ Hoog │ Competitive auctions│ €100/dag

OBJECTIVE COMPATIBILITY:

                │ Max Del │ Cost Cap │ Manual
────────────────┼─────────┼──────────┼────────
Brand Awareness │   ✓     │    -     │   ✓
Website Visits  │   ✓     │    ✓     │   ✓
Engagement      │   ✓     │    ✓     │   ✓
Video Views     │   ✓     │    ✓     │   ✓
Lead Generation │   ✓     │    ✓     │   ✓
Conversions     │   ✓     │    ✓     │   ✓
Job Applicants  │   ✓     │    -     │   ✓
```

## Maximum Delivery (Automated Bidding)

### Hoe Het Werkt
LinkedIn optimaliseert automatisch je bids om zoveel mogelijk resultaten te krijgen binnen je budget. Geen controle over CPC/CPL.

### Wanneer Gebruiken
- Nieuwe accounts met weinig benchmark data
- Brand awareness campaigns
- Snelle learning phase doorlopen
- Onzeker over realistische bid ranges
- Budget volledig uitgeven is prioriteit

### Wanneer NIET Gebruiken
- Strikte CPL vereisten
- Competitive niches waar kosten kunnen exploderen
- Wanneer je al benchmark data hebt

### Setup
```
Campaign Settings:
├── Objective: [Based on goal]
├── Bid type: Maximum Delivery
├── Daily budget: Minimum €25/dag
├── Schedule: Continuous of custom
└── Pacing: Standard (aanbevolen)

Expected Behavior:
├── Day 1-3: Learning, CPC/CPL fluctuates
├── Day 4-7: Stabilisatie
├── Week 2+: Consistent delivery
└── CPL: Typically 10-30% above market benchmark
```

### Verwachtingen
```
MAXIMUM DELIVERY PERFORMANCE
============================

Positief:
├── Budget wordt volledig besteed
├── Maximum reach/impressions
├── Snelle data verzameling
└── Weinig management nodig

Negatief:
├── Geen CPL/CPC controle
├── Kan duur zijn in competitive niches
├── CPA variatie dag-tot-dag
└── Minder geschikt voor strikte ROI targets
```

## Cost Cap

### Hoe Het Werkt
Stel een target CPL/CPA in. LinkedIn probeert gemiddeld rond dit bedrag te blijven, maar kan tijdelijk over/onder gaan.

### Wanneer Gebruiken
- Bekende target CPL uit historische data
- Lead generation met vastgestelde lead value
- Scaling terwijl efficiency bewaakt
- B2B met voorspelbare sales cycles

### Wanneer NIET Gebruiken
- Geen benchmark CPL beschikbaar
- Target te ambitieus (delivery stopt)
- Nieuwe accounts zonder data

### Cost Cap Berekening

```
COST CAP BEPALEN
================

Stap 1: Bepaal je Lead Value
├── Enterprise SaaS: Lead Value = ACV × Close Rate × 0.5
│   Voorbeeld: €50k × 5% × 0.5 = €1,250 lead value
│
├── SMB SaaS: Lead Value = ACV × Close Rate
│   Voorbeeld: €5k × 10% = €500 lead value
│
└── Services: Lead Value = Avg Deal × Close Rate
    Voorbeeld: €10k × 15% = €1,500 lead value

Stap 2: Bereken Break-Even CPL
├── Formula: Lead Value × Target CAC Efficiency
├── Efficiency factor: 0.10-0.20 (aggressive) to 0.30-0.40 (conservative)
│
├── Voorbeeld Enterprise:
│   €1,250 × 0.20 = €250 break-even CPL
│
└── Voorbeeld SMB:
    €500 × 0.15 = €75 break-even CPL

Stap 3: Set Cost Cap
├── Start: 1.2x break-even CPL (learning room)
├── Week 2: Tighten to 1.1x
├── Week 3+: Target break-even
└── Never: Start onder historisch gemiddelde
```

### Setup Best Practices

```
Cost Cap Implementation:
├── Calculate break-even CPL: €[X]
├── Start Cost Cap: €[X × 1.2]
├── Daily Budget: Minimum €50/dag
├── Audience Size: >50,000 recommended
└── Creative Rotation: 3-5 variants

Optimization Timeline:
├── Week 1: Monitor, don't adjust
├── Week 2: Tighten cap 10% if CPL stable
├── Week 3: Fine-tune based on SQL rate
└── Ongoing: Adjust seasonally
```

### Troubleshooting

```
COST CAP ISSUES
===============

Issue: Geen/Low Delivery
├── Oorzaak: Cap te laag
├── Check: Vergelijk met benchmark CPL
├── Fix: Verhoog cap 15-25%
└── Alternative: Switch to Maximum Delivery temporarily

Issue: CPL boven Cap
├── Oorzaak: Learning phase of high competition
├── Check: Is het consistent of incidenteel?
├── Fix: Wacht 5-7 dagen, verhoog cap 10%
└── Alternative: Expand audience size

Issue: Inconsistente Delivery
├── Oorzaak: Audience te klein of cap te tight
├── Check: Audience size (>50k?)
├── Fix: Broaden targeting of loosen cap
└── Alternative: Split in multiple campaigns
```

## Manual Bidding

### Hoe Het Werkt
Je stelt een exact maximum bid per click/impression/lead in. LinkedIn biedt nooit meer, zelfs als dit delivery kost.

### Wanneer Gebruiken
- Competitive niches (Finance, SaaS, Enterprise)
- Ervaren advertisers met veel data
- Strikte marge vereisten
- Auction dynamics goed begrepen
- A/B testing different bid levels

### Wanneer NIET Gebruiken
- Beginners
- Weinig conversie volume
- Onbekende bid ranges

### Manual Bid Bepalen

```
MANUAL BID STRATEGIE
====================

Voor CPC Campaigns:
├── Research: Check LinkedIn suggested bid range
├── Start: Mid-range of suggestions
├── Test: Run 3 ad sets with low/mid/high bids
├── Evaluate: Na 1000+ impressions per variant
└── Optimize: Focus budget op best performing bid

Suggested Bid Interpretation:
├── "€5.00 - €8.00" = Low competition
├── "€8.00 - €12.00" = Medium competition
├── "€12.00 - €20.00" = High competition
└── ">€20.00" = Very competitive (Finance, C-suite)

Bid Positioning Strategy:
├── Volume focus: Bid in top 25% of range
├── Efficiency focus: Bid in bottom 50% of range
├── Balanced: Bid at median
└── Testing: Run parallel at different levels
```

### Bid Optimization Process

```
MANUAL BID OPTIMIZATION WORKFLOW
================================

Week 1: Discovery
├── Set 3 bid levels: -20%, baseline, +20%
├── Equal budget across ad sets
├── Track: Impressions, clicks, conversions
└── Minimum: 1000 impressions per variant

Week 2: Analysis
├── Compare CPC, CTR, conversion rate
├── Calculate effective CPL per bid level
├── Identify sweet spot
└── Document: Bid vs Performance curve

Week 3: Optimization
├── Consolidate budget to winning bid level
├── Fine-tune: Test ±10% variations
├── Scale: Increase budget 20%
└── Monitor: Daily performance checks

Ongoing:
├── Adjust for seasonality
├── React to competition changes
├── Refresh bids monthly
└── Test new ranges quarterly
```

## Bid Strategy by Campaign Objective

### Lead Generation Campaigns

```
LEAD GEN BID STRATEGY SELECTION
===============================

Budget <€50/dag
└─► Maximum Delivery
    ├── Reason: Need volume for learning
    └── Expectation: CPL will be higher

Budget €50-150/dag
└─► Cost Cap (recommended)
    ├── Start: Benchmark CPL × 1.2
    ├── Target: Benchmark CPL
    └── Reason: Balance volume & efficiency

Budget >€150/dag
└─► Manual Bidding OR Cost Cap
    ├── Manual: If competitive niche
    ├── Cost Cap: If stable market
    └── Test: Run both parallel

Lead Gen Forms vs Website Conversions:
├── Forms: Typically 20-30% lower CPL
├── Website: Higher quality, higher CPL
└── Bid: Adjust expectations accordingly
```

### Website Visits / Traffic

```
TRAFFIC CAMPAIGN BIDDING
========================

Goal: Maximum Clicks
└─► Maximum Delivery + CPC billing
    ├── Benefit: Optimize for clicks
    └── Risk: Quality may vary

Goal: Quality Traffic
└─► Manual CPC Bidding
    ├── Set: Target CPC × 0.9
    ├── Benefit: Cost control
    └── Risk: Lower volume

Recommended CPC Ranges by Industry:
├── Technology: €4-8
├── Finance: €6-12
├── Healthcare: €4-8
├── Education: €3-6
├── Professional Services: €4-7
└── General B2B: €3-6
```

### Brand Awareness / Video Views

```
AWARENESS CAMPAIGN BIDDING
==========================

Objective: Reach
└─► Maximum Delivery
    ├── Billing: CPM
    ├── Benefit: Maximum exposure
    └── Target CPM: €30-60

Objective: Video Views
└─► Manual CPV OR Maximum Delivery
    ├── CPV target: €0.05-0.15
    ├── View threshold: 50%+ completion
    └── Benchmark: 25% view rate = good
```

## Budget & Pacing Strategy

### Budget Allocation Framework

```
LINKEDIN BUDGET ALLOCATION
==========================

Total Monthly Budget: €[X]
│
├── Lead Generation: 50-60%
│   ├── Lead Gen Forms: 60%
│   └── Website Conversions: 40%
│
├── Retargeting: 20-30%
│   ├── Website visitors: 50%
│   ├── Video viewers: 25%
│   └── Form abandoners: 25%
│
├── Brand Awareness: 10-20%
│   ├── Thought leadership: 60%
│   └── Video content: 40%
│
└── Testing: 5-10%
    └── New creatives & audiences
```

### Pacing Options

```
PACING STRATEGY
===============

Standard Pacing (Recommended):
├── Budget spread evenly across day
├── Benefit: Consistent delivery
├── Best for: Lead gen, conversions
└── Use when: You want steady performance

Accelerated Pacing:
├── Spend budget as fast as possible
├── Benefit: Quick results, testing
├── Risk: May exhaust budget early
├── Use when: Time-sensitive campaigns

Budget Flight Recommendations:
├── Short campaigns (<7 days): Accelerated
├── Standard campaigns (7-30 days): Standard
├── Always-on: Standard
└── Peak periods: Increase budget, keep standard pacing
```

### Scaling Protocols

```
SCALING LINKEDIN CAMPAIGNS
==========================

Safe Scaling Rules:
├── Maximum increase: 25% per 5-7 dagen
├── Never: >50% in één keer (triggers learning)
├── Monitor: CPL na elke increase
├── Trigger: CPL stable + SQL rate acceptable
└── Stop: Als CPL >25% stijgt na increase

Scaling Example:
├── Week 1: €100/dag (baseline)
├── Week 2: €125/dag (+25%)
├── Week 3: €156/dag (+25%)
├── Week 4: €195/dag (+25%)
├── Week 5: €244/dag (+25%)
└── Result: 2.5x scale in 5 weeks

Horizontal Scaling:
├── Duplicate winning campaign
├── Change one variable:
│   ├── New audience segment
│   ├── New creative set
│   └── New geography
├── Run parallel
└── Consolidate after 14 days
```

## High CPL Diagnosis & Resolution

```
CPL TE HOOG - DIAGNOSE
======================

Check 1: Benchmark Alignment
├── Compare to industry benchmark
├── Finance CPL €90-120 is normal
├── SaaS CPL €80-120 is normal
└── If within range: Expectations issue

Check 2: Audience Size
├── <20,000: Significantly higher CPL expected
├── 20-50,000: Moderately higher CPL
├── 50-200,000: Optimal range
└── >200,000: May be too broad

Check 3: Targeting Precision
├── Too narrow: High CPM, high CPL
├── Too broad: Low relevance, high CPL
└── Sweet spot: Qualified audience, reasonable size

Check 4: Creative Performance
├── CTR <0.4%: Creative issue
├── CTR 0.4-0.6%: Normal
├── CTR >0.6%: Strong creative
└── Low CTR = High CPC = High CPL

Check 5: Form Friction
├── Many fields (>5): Lower CVR, higher CPL
├── Custom questions: May filter but increase CPL
└── Test: Reduce fields, measure SQL impact

RESOLUTION MATRIX:

If CPL High + CTR Low → Creative refresh needed
If CPL High + CTR Good → Audience/targeting issue
If CPL High + CVR Low → Form optimization needed
If CPL High + All Good → Market rate, accept or narrow targeting
```

## Scenario-Based Recommendations

### Scenario 1: New Account Launch

```
NEW ACCOUNT - 4 WEEK PLAN
=========================

Week 1-2:
├── Strategy: Maximum Delivery
├── Budget: €50-75/dag
├── Goal: 30+ conversions for learning
├── Focus: Gather benchmark data
└── Expected CPL: 20-30% above market

Week 3:
├── Strategy: Transition to Cost Cap
├── Cost Cap: Achieved CPL × 1.1
├── Budget: Maintain €50-75/dag
├── Goal: Validate efficiency
└── Monitor: Delivery consistency

Week 4+:
├── Strategy: Cost Cap (tightened)
├── Cost Cap: Target benchmark
├── Budget: Scale if CPL stable
├── Goal: Sustainable acquisition
└── Optimize: Creative testing
```

### Scenario 2: Scaling Profitable Campaign

```
SCALING SCENARIO
================

Current State:
├── Spend: €75/dag
├── CPL: €85 (target: €100)
├── SQL Rate: 22% (good)
└── Goal: Scale to €200/dag

Scaling Plan:
├── Week 1: €75 → €95 (+27%)
│   └── Monitor: CPL should stay <€95
│
├── Week 2: €95 → €120 (+26%)
│   └── Monitor: Add new creative variants
│
├── Week 3: €120 → €150 (+25%)
│   └── Monitor: Test audience expansion
│
├── Week 4: €150 → €200 (+33%)
│   └── Monitor: Review SQL rate stability
│
└── Contingency:
    ├── If CPL >€100: Pause scaling
    ├── If CPL >€110: Reduce budget 15%
    └── If SQL rate drops: Tighten targeting
```

### Scenario 3: High-Competition Niche (Finance/Enterprise SaaS)

```
COMPETITIVE NICHE STRATEGY
==========================

Strategy: Manual Bidding + Premium Positioning

Setup:
├── Research: Check suggested bid range
├── Bid: Top 30% of range (win auctions)
├── Budget: €100+/dag (sufficient volume)
├── Audience: Tight, qualified targeting
└── Creative: Premium, thought leadership

Bid Strategy:
├── Start: €12-15 CPC (Finance)
├── Week 1: Evaluate win rate
├── Adjust: If <60% impression share, increase bid
├── Optimize: Test bid levels ±20%
└── Target: 70%+ impression share on target audience

Cost Management:
├── Accept higher CPC for better audience
├── Focus on: SQL rate, not just CPL
├── Calculate: Cost per SQL, not just cost per lead
└── Expectation: CPL €100-150 acceptable if SQL rate >25%
```

## Output: Strategy Recommendation Template

```markdown
# LinkedIn Bid Strategy Recommendation

## Current Situation
- Daily/Monthly budget: €[X]
- Industry: [sector]
- Target audience size: [X]
- Current CPL/CPC: [metric] (if available)
- Primary goal: [volume/efficiency/quality]

## Recommended Strategy
**[Maximum Delivery / Cost Cap / Manual Bidding]**

### Why This Strategy
- [Reason 1 based on budget]
- [Reason 2 based on goal]
- [Reason 3 based on experience level]

### Implementation
1. Campaign Setup: [specifics]
2. Bid Configuration: [details]
3. Budget Allocation: [breakdown]

### Targets
- Primary: CPL €[X] / CPC €[Y]
- Secondary: CTR [X]%, CVR [Y]%
- Quality: SQL Rate [X]%

### Timeline
- Week 1: [Learning/baseline]
- Week 2: [Optimization]
- Week 3+: [Scaling/maintenance]

### Success Criteria
- CPL within [X]% of target
- Delivery consistent (>90% budget spend)
- SQL rate maintains [X]%+
```

## Voorbeeld Interactie

**Gebruiker**: "Ik heb €100/dag budget voor LinkedIn lead gen in de SaaS sector. Wat is de beste bidding strategie?"

**Claude response**:

"Voor je situatie (€100/dag, SaaS, lead generation) adviseer ik:

**Aanbevolen Strategy: Cost Cap**

### Waarom Cost Cap?

1. **Budget is voldoende** - €100/dag geeft LinkedIn genoeg ruimte om te optimaliseren
2. **SaaS heeft benchmark data** - We kunnen een realistisch target CPL bepalen
3. **Balans volume & efficiency** - Cost Cap voorkomt runaway costs

### Implementation

**Stap 1: Bepaal je Cost Cap**
```
SaaS Benchmark CPL: €80-120
Start Cost Cap: €120 (1.2x industry baseline)
Week 2 target: €100
Week 3+ target: €85-90
```

**Stap 2: Campaign Setup**
- Objective: Lead Generation
- Bid type: Cost Cap
- Cost Cap: €120
- Daily budget: €100
- Audience: >50,000 mensen

**Stap 3: Optimization Timeline**
| Week | Action | Target CPL |
|------|--------|------------|
| 1 | Monitor, don't touch | €120 |
| 2 | Tighten cap 15% | €100 |
| 3 | Fine-tune based on SQL | €90 |
| 4+ | Scale if stable | €85-90 |

### Verwachte Resultaten
- Leads per week: ~8-12 (afhankelijk van niche)
- Expected CPL: €85-100 na optimalisatie
- SQL rate target: 15-25%

### Red Flags om te monitoren
- Delivery <80% budget? → Verhoog cap
- CPL >€140 na week 2? → Check creative/targeting
- CTR <0.4%? → Refresh creatives

Wil je dat ik je Cost Cap berekening valideer op basis van je specifieke deal size en close rate?"

---
name: bid-strategy-selector
description: |
  Selects optimal Meta Ads bid strategy (Lowest Cost, Cost Cap, Bid Cap, ROAS Goal) based on goals, budget, and account maturity. Use when: choosing bid strategy, comparing cost cap vs bid cap, budget allocation, scaling strategy, value rules setup.
  Do NOT use for: Google Ads bidding (use google-bid-strategy-selector), campaign structure decisions (use campaign-structure-advisor), creative testing (use creative-diversification-generator).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "meta"
  phase: "fase-1-foundation"
compatibility: "Requires AdSuperpowers MCP server with Meta Ads connection"
---
# Bid Strategy Selector

Advisor for selecting the optimal Meta Ads bid strategy based on goals, budget, and account situation.

## Quick Selection Guide

```
WHAT IS YOUR PRIMARY GOAL?
│
├─► Maximum volume (leads/sales)
│   └─► LOWEST COST (Highest Volume)
│
├─► Keep CPA under control
│   └─► COST CAP
│
├─► Strict margin requirements
│   └─► BID CAP
│
└─► Profitability focus (e-commerce)
    └─► ROAS GOAL (Minimum ROAS)
```

## Bid Strategy Overview

| Strategy | Control | Risk | Best For | Min. Data |
|----------|---------|------|----------|-----------|
| **Lowest Cost** | None | Low | Beginners, volume | Little |
| **Cost Cap** | CPA target | Medium | CPA constraints | 50+ conv/week |
| **Bid Cap** | Max bid | High | Competitive niches | 100+ conv/week |
| **ROAS Goal** | Min ROAS | Medium | Profitability | 50+ conv/week + CAPI |

## Lowest Cost (Highest Volume)

### How It Works
Meta gets as many results as possible within your budget, without a CPA limit.

### When to Use
- New accounts with little historical data
- Learning phase (first 2-4 weeks)
- Volume more important than efficiency
- Unsure about realistic CPA targets
- Brand awareness campaigns

### When NOT to Use
- Strict CPA requirements
- Limited budget with margin pressure
- Competitive auctions where CPA can spike

### Setup
```
Campaign Settings:
├── Budget optimization: CBO or ABO
├── Bid strategy: Highest Volume
├── No cost controls: Leave empty
└── Conversion goal: Select optimization event
```

### Expectations
- CPA fluctuates day-to-day
- AI optimizes for volume, not efficiency
- Best baseline for new campaigns

## Cost Cap

### How It Works
Meta keeps average CPA around your target. May temporarily exceed but balances over time.

### When to Use
- Known target CPA (from historical data)
- Lead gen with fixed lead value
- E-commerce with known break-even CPA
- Scaling while monitoring efficiency

### When NOT to Use
- No idea of realistic CPA
- Cap set too low (delivery stops)
- New accounts without benchmarks

### Setup Best Practices
```
Cost Cap Calculation:
├── Break-even CPA: [AOV x Margin] or [Lead Value x Conv Rate]
├── Starting point: 1.2x break-even (room for learning)
├── After 1-2 weeks: Tighten to 1.0-1.1x
└── Never: Start below historical average

Example E-commerce:
- AOV: €80
- Margin: 40%
- Break-even CPA: €80 x 0.40 = €32
- Starting Cost Cap: €38 (1.2x)
- Target Cost Cap: €32-35
```

### Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| No delivery | Cap too low | Increase 10-20% |
| CPA above cap | Learning phase | Wait 3-5 days |
| Unstable delivery | Cap too tight | Increase to 1.1x target |

## Bid Cap

### How It Works
Set maximum bid per auction. Meta never bids more, even if it costs conversions.

### When to Use
- Competitive niches (finance, real estate, SaaS)
- Strict margin requirements
- Predictable costs are crucial
- Experienced advertisers with lots of data

### When NOT to Use
- Beginners (too complex)
- Low conversion volume
- Unknown auction dynamics

### Setup Strategy
```
Determining Bid Cap:
├── Start: 1.5x your average CPA
├── Week 1: Monitor delivery and CPA
├── Week 2: Lower 10% if delivery is stable
├── Repeat: Until sweet spot found
└── Minimum: Never below historical lowest CPA

Example:
- Historical CPA: €25
- Starting Bid Cap: €37.50
- Week 2: €33.75
- Week 3: €30
- Sweet spot: €28-30
```

### Pro Tips
- Test multiple bid caps in parallel across different ad sets
- Seasonal adjustment: Increase 20-30% in Q4/peak periods
- Monitor frequency: High frequency + low delivery = bid too low

## ROAS Goal (Minimum ROAS)

### How It Works
Meta optimizes for minimum return per euro of ad spend.

### When to Use
- E-commerce with variable product values
- Profitability more important than volume
- Sufficient conversion volume (50+/week)
- Strong CAPI implementation

### When NOT to Use
- Lead generation (no direct revenue)
- Inconsistent product values
- Weak tracking setup

### Setup Requirements
```
Prerequisites:
├── CAPI active with purchase value
├── Event Match Quality >7
├── Product catalog with accurate prices
├── 50+ purchases per week
└── 28+ days of conversion data

Calculating ROAS Target:
├── Break-even ROAS: 1 / Profit Margin
├── Example: 40% margin → 1/0.40 = 2.5x break-even
├── Starting target: 80% of break-even (2.0x)
├── Scale up: Tighten toward break-even + buffer
└── Aggressive: 1.2x break-even for growth
```

### Value Rules (2025 Enhancement)

Value Rules let you adjust bids based on predicted ROAS per segment:

```
Value Rule Setup:
├── Segment: High-value customers
│   ├── Criteria: Previous purchasers, high AOV
│   └── Bid adjustment: +30%
│
├── Segment: Low-value segments
│   ├── Criteria: Certain geos, devices
│   └── Bid adjustment: -20%
│
└── Formula: Bid = BaseBid x (Predicted ROAS / Target ROAS)
```

## Budget & Scaling Strategy

### Budget Allocation Framework

```
Total Monthly Budget: €[X]
│
├── Prospecting (TOF): 60-70%
│   ├── Advantage+ Sales: 70% of TOF
│   └── Manual testing: 30% of TOF
│
├── Retargeting (MOF/BOF): 20-30%
│   ├── Website visitors: 60%
│   └── Engagement: 40%
│
└── Creative Testing: 5-15%
    └── New concepts validation
```

### Scaling Rules

**Vertical Scaling (Increasing Budget)**
```
Safe scaling protocol:
├── Maximum increase: 20% per 3-4 days
├── Never: >50% at once
├── Monitor: CPA after each increase
├── Trigger: ROAS >target AND stable 5+ days
└── Stop: If CPA rises >20% after increase
```

**Horizontal Scaling (New Ad Sets)**
```
Horizontal expansion:
├── Duplicate winning ad set
├── Change ONE variable:
│   ├── New audience segment
│   ├── New creative set
│   └── New geo/placement
├── Run in parallel with original
└── Consolidate winners after 7-14 days
```

### Peak Period Strategy

```
Peak Period Planning (Black Friday, etc.):
├── 2 weeks before peak:
│   ├── Increase budgets 30-50%
│   ├── Loosen bid constraints 20%
│   └── Test new creatives
│
├── Peak week:
│   ├── Allocate 50-60% monthly budget
│   ├── Monitor hourly
│   └── Ready for quick scaling
│
└── Post-peak:
    ├── Reduce budgets gradually
    ├── Tighten bids
    └── Continue retargeting
```

## Scenario-Based Recommendations

### Scenario 1: New Account Launch

```
Week 1-2:
├── Strategy: Lowest Cost
├── Budget: €50-100/day minimum
├── Goal: Exit learning phase
└── KPI: 50+ conversions

Week 3-4:
├── Strategy: Cost Cap (1.2x achieved CPA)
├── Evaluate: Is CPA sustainable?
├── Adjust: Tighten cap 10% weekly
└── Scale: If ROAS >break-even

Week 5+:
├── Strategy: Maintain Cost Cap or switch to ROAS Goal
├── Focus: Scaling winners
└── Testing: 10-15% budget for new concepts
```

### Scenario 2: Scaling Profitable Campaign

```
Current: ROAS 4x, spending €500/day
Target: Scale to €2000/day

Approach:
├── Week 1: €500 → €600 (+20%)
├── Week 2: €600 → €750 (+25%)
├── Week 3: €750 → €950 (+27%)
├── Week 4: €950 → €1200 (+26%)
├── Week 5: €1200 → €1500 (+25%)
├── Week 6: €1500 → €2000 (+33%)
└── Total: 6 weeks for 4x scale

Safety checks per week:
- ROAS drop >20%? Pause scaling
- CPA spike >30%? Reduce budget 10%
- Frequency >4? Refresh creatives
```

### Scenario 3: Competitive Niche (Finance/Insurance)

```
Strategy: Bid Cap + Value Rules

Setup:
├── Research: Competitor bid ranges
├── Start: Premium bid cap (top 25% range)
├── Value Rules:
│   ├── High-intent keywords: +40%
│   └── Low-quality signals: -30%
├── Focus: Quality over volume
└── Tracking: Lead-to-customer rate

Optimization:
├── Weekly bid adjustments
├── Heavy creative testing (10+ variations)
├── Audience refinement
└── Landing page A/B testing
```

## Bid Strategy Migration Checklist

When switching strategies:

```
Pre-Migration:
□ Document current performance (7-day average)
□ Calculate new target (CPA/ROAS)
□ Prepare for learning phase reset

Migration:
□ Implement new strategy
□ Set conservative targets (1.2x current)
□ Allow 3-5 days learning

Post-Migration:
□ Compare week-over-week
□ Tighten targets if stable
□ Document learnings
```

## Output: Strategy Recommendation Template

```markdown
# Bid Strategy Recommendation

## Current Situation
- Monthly budget: €[X]
- Current CPA/ROAS: [metric]
- Conversion volume: [X]/week
- Primary goal: [volume/efficiency/profitability]

## Recommended Strategy
**[Strategy Name]**

### Why This Strategy
[2-3 bullets explaining rationale]

### Implementation
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Targets
- [Primary metric]: [target]
- [Secondary metric]: [target]

### Timeline
- Week 1: [actions]
- Week 2: [actions]
- Week 3+: [ongoing optimization]

### Success Criteria
- [Metric 1] achieves [target]
- Learning phase exits within [X] days
- Stable delivery maintained
```

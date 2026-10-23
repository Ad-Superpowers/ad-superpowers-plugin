---
name: meta-bid-strategy-selector
description: "This skill should be used when the user asks to \"choose a bid strategy\", \"compare cost cap vs bid cap\", \"set up value rules\", or mentions \"Meta bid strategy\", \"ROAS goal bidding\", or \"scaling bid approach\". Do NOT use for: Google Ads bidding (use google-bid-strategy-selector), campaign structure decisions (use campaign-structure-advisor), creative testing (use creative-diversification-generator)."
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
| **Cost Cap** | CPA target | Medium | CPA constraints | 50-100+ conv/week |
| **Bid Cap** | Max bid | High | Competitive niches | 100+ conv/week |
| **ROAS Goal** | Min ROAS | Medium | Profitability | 50-100+ conv/week + CAPI |

For its goal-based strategies, cost per result goal (Cost Cap here) and ROAS goal, Meta says goal-based bidding works best with 50 to 100 or more conversions per week ("About bid strategies", Meta Business Help Center, undated, checked 2026-10-10). The other columns and the Bid Cap figure are rules of thumb, not Meta figures: check them against the account's own history.

## Lowest Cost (Highest Volume)

### How It Works
Meta gets as many results as possible within your budget, without a CPA limit.

### When to Use
- New accounts with little historical data
- The learning phase of a new campaign
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
├── Budget optimization: Advantage Campaign Budget or Ad Set Budget
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
In Ads Manager, Cost Cap is called "Cost per result goal" (API `COST_CAP`; "About bid strategies", Meta Business Help Center). Meta aims for the most results while trying to keep the average cost per result at your cap. Meta does not guarantee the cap: costs can rise, and the ad set may not spend its full budget once it hits the cap ("Bid Strategy", Marketing API).

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

The multipliers, percentages and day counts in this section and in Troubleshooting below are rules of thumb, not Meta figures: check them against the account's own history. Meta's own pointer: if you set the cap from the ad set's cost per optimization event, wait until it has about 50 optimization events since its last significant edit (Meta Business Help Center, "Last Significant Edit", undated, checked 2026-10-10).

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
Set a maximum bid across auctions. Meta raises its bid as needed but never above the cap, even if that costs results, and the ad set may not spend its full budget. The bid is not the cost per result you see in reporting ("Bid Strategy", Marketing API).

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

The multipliers and percentages in this section and in Pro Tips below are rules of thumb, not Meta figures: check them against the account's own history.

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
Meta optimizes for purchase value and aims to keep the return on ad spend at or above the floor you set. It needs value optimization (`optimization_goal` VALUE) and an account that is eligible for value optimization; a floor set too high can lead to under-delivery ("Bid Strategy", Marketing API).

### When to Use
- E-commerce with variable product values
- Profitability more important than volume
- Sufficient conversion volume (Meta says goal-based bidding works best with 50 to 100 or more conversions a week: "About bid strategies")
- Strong CAPI implementation

### When NOT to Use
- Lead generation (no direct revenue)
- Inconsistent product values
- Weak tracking setup

### Setup Requirements

Meta requires value optimization, an eligible account and purchase values sent back to Meta ("Bid Strategy", Marketing API); a new business can be refused at first (see "How this maps to our MCP tools today" below). The list below adds our own prerequisites. The Event Match Quality line follows Meta's Conversions API docs, which call a "Good" or "Great" rating in Events Manager optimal ("Monitor Your Conversions API Gateway Setup", updated Feb 2, 2025) and recommend aiming for a score of 6.0 or higher where possible ("Verifying Your Setup", updated Nov 24, 2025; both checked 2026-10-10). The purchase line follows Meta's 50 to 100 or more weekly conversions for goal-based bidding (see When to Use); the days and ROAS target steps are rules of thumb, not Meta figures: check them against the account's own history.

```
Prerequisites:
├── CAPI active with purchase value
├── Event Match Quality 6.0 or higher where possible (Meta's recommendation)
├── 50-100+ purchases per week
└── 28+ days of conversion data

Calculating ROAS Target:
├── Break-even ROAS: 1 / Profit Margin
├── Example: 40% margin → 1/0.40 = 2.5x break-even
├── Starting target: 80% of break-even (2.0x)
├── Scale up: Tighten toward break-even + buffer
└── Aggressive: 1.2x break-even for growth
```

### Value Rules

Value rules tell Meta how much more or less a result from a segment is worth to you, and Meta adjusts its bids for that segment. Criteria: age, gender, location, OS, device platform, audience labels and select placements. Limits: up to 10 rules per rule set, 6 rule sets per ad account, an increase of 1-1000% or a decrease of 1-90%. They apply to ad sets on `LOWEST_COST_WITHOUT_CAP` or `COST_CAP`, with some exceptions ("Value Rules", Marketing API). Our MCP tools cannot create or change value rules.

```
Value Rule Setup (example values):
├── Segment: higher-value buyers
│   ├── Criteria: e.g. age 35-44 in one region
│   └── Value adjustment: +30%
│
├── Segment: lower-value segment
│   ├── Criteria: e.g. one device platform
│   └── Value adjustment: -20%
│
└── Meta bids up or down for people who match a rule
```

## Budget & Scaling Strategy

Rules of thumb, not Meta figures: check them against the account's own history. This covers the budget shares, step sizes and day counts in this section.

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
├── Maximum increase: about 20% per 3-4 days (rule of thumb)
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

Rules of thumb, not Meta figures: check them against the account's own history.

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
│   (ROAS Goal needs optimization_goal VALUE; read the
│   migration checklist below before you switch)
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
Strategy: Bid Cap (value rules need Highest Volume or Cost Cap)

Setup:
├── Research: the account's own CPA and lead-to-customer history
├── Start: a bid cap from that history (see Bid Cap above)
├── Value Rules: only after a switch to Cost Cap; criteria are
│   age, gender, location, OS, device platform, audience
│   labels and placements, not keywords
├── Focus: Quality over volume
└── Tracking: Lead-to-customer rate

Optimization:
├── Weekly bid adjustments
├── Heavy creative testing (many variations)
├── Audience refinement
└── Landing page A/B testing
```

## Bid Strategy Migration Checklist

When switching strategies:

Under an Advantage campaign budget, Meta documents switching a campaign between `COST_CAP` and `LOWEST_COST_WITH_BID_CAP`; a campaign created with `LOWEST_COST_WITH_MIN_ROAS` cannot currently switch to another bid strategy ("Advantage Campaign Budget", Marketing API). To move away from ROAS Goal, plan a new campaign; a move to ROAS Goal also needs ad sets with `optimization_goal` VALUE. Meta counts a bid strategy change as a significant edit, which restarts learning, and under an Advantage campaign budget a campaign-level switch can send several ad sets back into learning ("Significant edits and learning phase", Meta Business Help Center, undated, checked 2026-10-10). The 1.2x target and the day counts below are rules of thumb, not Meta figures: check them against the account's own history.

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

## How this maps to our MCP tools today

The strategy names above map to these API values, and `meta_create` has defaults worth knowing before you set anything:

| This guide's name | API `bid_strategy` value | Needs a number? |
|-------------------|--------------------------|-----------------|
| Lowest Cost (Highest Volume) | `LOWEST_COST_WITHOUT_CAP` | no |
| Cost Cap (Ads Manager: "Cost per result goal") | `COST_CAP` | `bid_amount` (ad set) |
| Bid Cap | `LOWEST_COST_WITH_BID_CAP` | `bid_amount` (ad set) |
| ROAS Goal | `LOWEST_COST_WITH_MIN_ROAS` | `roas_floor` (ad set, with `bid_strategy="LOWEST_COST_WITH_MIN_ROAS"` and `optimization_goal="VALUE"` on the same ad set; under CBO also set the strategy on the campaign) |

- **`meta_create` defaults a new campaign to `LOWEST_COST_WITHOUT_CAP`.** You only pass `bid_strategy` to override it, and that default is why ad sets do not need a `bid_amount`.
- **`meta_create` takes `budget_mode`:** `"CBO"` (the default) puts the budget on the campaign; `"ABO"` leaves the campaign without a budget and each ad set sets its own. The cap/target strategies put their `bid_amount` (or `roas_floor`) on the **ad set**. Under CBO the ad sets inherit the campaign's bid strategy, so set a non-default strategy on the campaign as well.
- **Minimum ROAS can be refused for a new business.** On a test account Meta rejected `LOWEST_COST_WITH_MIN_ROAS` with: "Ad accounts owned by a new business can use minimum ROAS for ad delivery after several weeks of following our policies. If you don't want to wait, verify your business." (Meta API error, seen 2026-10-10). Until then, use another strategy or verify the business.
- For the full launch sequence (campaign → ad set → ads), `use ad-launch-playbook`.

## MCP: Check Current Bid Strategy & Performance

```python
# Pull campaign-level bid strategy and spend for active campaigns
# format="full" keeps bid_strategy; above 30 campaigns the default "auto" format compacts the list and drops it
meta_query(account_id="act_XXXXX", entity_type="campaigns", effective_status=["ACTIVE"], fields=["id","name","bid_strategy","daily_budget","status"], format="full")

# Pull ad set performance to evaluate current CPA vs target
meta_get_insights(account_id="act_XXXXX", level="adset", date_preset="last_7d", fields=["cost_per_action_type","spend","actions","impressions","ctr"])
# meta_get_insights returns one page; if the result has paging.next, fetch the rest with
# meta_query(account_id="act_XXXXX", entity_type="ads", pagination_url=<paging.next>)
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

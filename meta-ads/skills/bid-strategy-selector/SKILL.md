---
name: bid-strategy-selector
description: "Meta Ads bid strategy advisor voor het kiezen van de optimale biedstrategie. Gebruik voor: (1) Lowest Cost vs Cost Cap vs Bid Cap vs ROAS Goal kiezen, (2) Budget allocatie advies, (3) Scaling strategie planning, (4) Value Rules setup, (5) Bid optimization troubleshooting. Triggers: bid strategy, bidding, cost cap, bid cap, ROAS goal, lowest cost, budget, scaling, value rules."
---

# Bid Strategy Selector

Advisor voor het selecteren van de optimale Meta Ads biedstrategie op basis van doelen, budget en account situatie.

## Quick Selection Guide

```
WAT IS JE PRIMAIRE DOEL?
│
├─► Maximaal volume (leads/sales)
│   └─► LOWEST COST (Highest Volume)
│
├─► CPA onder controle houden
│   └─► COST CAP
│
├─► Strikte marge vereisten
│   └─► BID CAP
│
└─► Profitability focus (e-commerce)
    └─► ROAS GOAL (Minimum ROAS)
```

## Bid Strategy Overview

| Strategy | Control | Risk | Best For | Min. Data |
|----------|---------|------|----------|-----------|
| **Lowest Cost** | Geen | Laag | Beginners, volume | Weinig |
| **Cost Cap** | CPA target | Medium | CPA constraints | 50+ conv/week |
| **Bid Cap** | Max bid | Hoog | Competitive niches | 100+ conv/week |
| **ROAS Goal** | Min ROAS | Medium | Profitability | 50+ conv/week + CAPI |

## Lowest Cost (Highest Volume)

### Hoe Het Werkt
Meta krijgt zoveel mogelijk resultaten binnen je budget, zonder CPA limiet.

### Wanneer Gebruiken
- Nieuwe accounts met weinig historische data
- Learning phase (eerste 2-4 weken)
- Volume belangrijker dan efficiency
- Onzeker over realistische CPA targets
- Brand awareness campaigns

### Wanneer NIET Gebruiken
- Strikte CPA vereisten
- Beperkt budget met marge-druk
- Competitive auctions waar CPA kan exploderen

### Setup
```
Campaign Settings:
├── Budget optimization: CBO of ABO
├── Bid strategy: Highest Volume
├── No cost controls: Laat leeg
└── Conversion goal: Selecteer optimization event
```

### Verwachtingen
- CPA fluctueert dag-tot-dag
- AI optimaliseert voor volume, niet efficiency
- Beste baseline voor nieuwe campaigns

## Cost Cap

### Hoe Het Werkt
Meta houdt gemiddelde CPA rond je target. Mag tijdelijk overschrijden maar balanceert over tijd.

### Wanneer Gebruiken
- Bekende target CPA (uit historische data)
- Lead gen met vaste lead value
- E-commerce met bekende break-even CPA
- Scaling terwijl je efficiency bewaakt

### Wanneer NIET Gebruiken
- Geen idee van realistische CPA
- Te lage cap (delivery stopt)
- Nieuwe accounts zonder benchmarks

### Setup Best Practices
```
Cost Cap Berekening:
├── Break-even CPA: [AOV × Margin] of [Lead Value × Conv Rate]
├── Startpunt: 1.2x break-even (ruimte voor learning)
├── Na 1-2 weken: Tighten naar 1.0-1.1x
└── Never: Onder historisch gemiddelde starten

Voorbeeld E-commerce:
- AOV: €80
- Margin: 40%
- Break-even CPA: €80 × 0.40 = €32
- Start Cost Cap: €38 (1.2x)
- Target Cost Cap: €32-35
```

### Troubleshooting

| Issue | Oorzaak | Oplossing |
|-------|---------|-----------|
| Geen delivery | Cap te laag | Verhoog 10-20% |
| CPA boven cap | Learning phase | Wacht 3-5 dagen |
| Unstable delivery | Cap te tight | Verhoog naar 1.1x target |

## Bid Cap

### Hoe Het Werkt
Stel maximum bid per auction. Meta biedt nooit meer, ook als het conversies kost.

### Wanneer Gebruiken
- Competitive niches (finance, real estate, SaaS)
- Strikte marge vereisten
- Voorspelbare kosten cruciaal
- Ervaren advertisers met veel data

### Wanneer NIET Gebruiken
- Beginners (te complex)
- Weinig conversie volume
- Onbekende auction dynamics

### Setup Strategie
```
Bid Cap Bepalen:
├── Start: 1.5x je gemiddelde CPA
├── Week 1: Monitor delivery en CPA
├── Week 2: Verlaag 10% als delivery stabiel
├── Repeat: Tot sweet spot gevonden
└── Minimum: Nooit onder historisch laagste CPA

Voorbeeld:
- Historisch CPA: €25
- Start Bid Cap: €37.50
- Week 2: €33.75
- Week 3: €30
- Sweet spot: €28-30
```

### Pro Tips
- Test meerdere bid caps parallel in verschillende ad sets
- Seasonal adjustment: Verhoog 20-30% in Q4/peak periods
- Monitor frequency: Hoge frequency + lage delivery = bid te laag

## ROAS Goal (Minimum ROAS)

### Hoe Het Werkt
Meta optimaliseert voor minimale return per euro adspend.

### Wanneer Gebruiken
- E-commerce met variabele product values
- Profitability belangrijker dan volume
- Voldoende conversie volume (50+/week)
- Strong CAPI implementation

### Wanneer NIET Gebruiken
- Lead generation (geen directe revenue)
- Inconsistente product values
- Zwakke tracking setup

### Setup Requirements
```
Prerequisites:
├── CAPI actief met purchase value
├── Event Match Quality >7
├── Product catalog met accurate prijzen
├── 50+ purchases per week
└── 28+ dagen conversion data

ROAS Target Berekenen:
├── Break-even ROAS: 1 / Profit Margin
├── Voorbeeld: 40% margin → 1/0.40 = 2.5x break-even
├── Start target: 80% van break-even (2.0x)
├── Scale up: Tighten naar break-even + buffer
└── Aggressive: 1.2x break-even voor growth
```

### Value Rules (2025 Enhancement)

Value Rules laten je bids aanpassen op predicted ROAS per segment:

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
└── Formula: Bid = BaseBid × (Predicted ROAS / Target ROAS)
```

## Budget & Scaling Strategy

### Budget Allocation Framework

```
Total Monthly Budget: €[X]
│
├── Prospecting (TOF): 60-70%
│   ├── Advantage+ Sales: 70% van TOF
│   └── Manual testing: 30% van TOF
│
├── Retargeting (MOF/BOF): 20-30%
│   ├── Website visitors: 60%
│   └── Engagement: 40%
│
└── Creative Testing: 5-15%
    └── New concepts validation
```

### Scaling Rules

**Vertical Scaling (Budget Verhogen)**
```
Safe scaling protocol:
├── Maximum increase: 20% per 3-4 dagen
├── Never: >50% in één keer
├── Monitor: CPA na elke increase
├── Trigger: ROAS >target én stable 5+ dagen
└── Stop: Als CPA >20% stijgt na increase
```

**Horizontal Scaling (Nieuwe Ad Sets)**
```
Horizontal expansion:
├── Dupliceer winning ad set
├── Change ONE variable:
│   ├── New audience segment
│   ├── New creative set
│   └── New geo/placement
├── Run parallel met original
└── Consolidate winners na 7-14 dagen
```

### Peak Period Strategy

```
Peak Period Planning (Black Friday, etc.):
├── 2 weken voor peak:
│   ├── Increase budgets 30-50%
│   ├── Loosen bid constraints 20%
│   └── Test new creatives
│
├── Peak week:
│   ├── Allocate 50-60% monthly budget
│   ├── Monitor hourly
│   └── Ready voor quick scaling
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
├── Budget: €50-100/dag minimum
├── Goal: Exit learning phase
└── KPI: 50+ conversions

Week 3-4:
├── Strategy: Cost Cap (1.2x achieved CPA)
├── Evaluate: Is CPA sustainable?
├── Adjust: Tighten cap 10% weekly
└── Scale: If ROAS >break-even

Week 5+:
├── Strategy: Maintain Cost Cap of switch naar ROAS Goal
├── Focus: Scaling winners
└── Testing: 10-15% budget voor new concepts
```

### Scenario 2: Scaling Profitable Campaign

```
Current: ROAS 4x, spending €500/dag
Target: Scale naar €2000/dag

Approach:
├── Week 1: €500 → €600 (+20%)
├── Week 2: €600 → €750 (+25%)
├── Week 3: €750 → €950 (+27%)
├── Week 4: €950 → €1200 (+26%)
├── Week 5: €1200 → €1500 (+25%)
├── Week 6: €1500 → €2000 (+33%)
└── Total: 6 weken voor 4x scale

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

Bij het switchen van strategy:

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

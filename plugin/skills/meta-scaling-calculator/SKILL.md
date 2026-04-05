---
name: scaling-calculator
description: |
  This skill should be used when the user asks to "scale a campaign", "calculate budget increments",
  "plan a scaling timeline", or mentions "scaling without losing performance",
  "Meta Ads scaling strategy", or "budget increase risk". Do NOT use for: bid strategy
  selection (use bid-strategy-selector), budget allocation across funnel
  (use full-funnel-designer), performance diagnostics (use performance-troubleshooter).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "meta"
  phase: "fase-5-advanced"
compatibility: "Requires AdSuperpowers MCP server with Meta Ads connection"
---
# Scaling Calculator

## Overview

This skill helps calculate optimal scaling strategies for Meta Ads, including budget increases, timelines, and risk assessment to maintain performance during growth.

## Scaling Fundamentals

### Why Scaling Is Difficult

```
┌─────────────────────────────────────────────────────────────────┐
│  THE SCALING DILEMMA                                            │
│                                                                 │
│  Scaling too fast:                                              │
│  ├── Learning phase reset                                       │
│  ├── CPA spike from algorithm adjustments                       │
│  ├── Audience exhaustion                                        │
│  └── Budget waste                                               │
│                                                                 │
│  Scaling too slow:                                              │
│  ├── Missed revenue opportunity                                 │
│  ├── Competitor gains ground                                    │
│  ├── Seasonal opportunities missed                              │
│  └── Inefficient growth                                         │
│                                                                 │
│  Sweet spot: 15-20% budget increase per 3-4 days               │
│              as long as performance stays stable                │
└─────────────────────────────────────────────────────────────────┘
```

### The 20% Rule

```
META'S RECOMMENDED SCALING:
==========================

Budget increases up to 20% do NOT trigger a learning phase reset.

Example:
├── Day 1: $50/day
├── Day 4: $60/day (+20%)
├── Day 7: $72/day (+20%)
├── Day 10: $86/day (+20%)
└── Day 13: $103/day (+20%)

After 2 weeks: Budget doubled without learning phase reset!
```

## Scaling Readiness Check

### Pre-Scaling Checklist

```
BEFORE YOU SCALE - VALIDATE:
==============================

□ PERFORMANCE STABILITY
├── CPA stable last 7 days? (variation <15%)
├── Sufficient conversions? (>50 per week)
├── Positive ROAS above target?
└── Ready if: All 3 checks positive

□ AUDIENCE HEADROOM
├── Current frequency <2.5?
├── Audience size >10x daily budget?
├── Reach still has growth potential?
└── Ready if: All 3 checks positive

□ CREATIVE STRENGTH
├── CTR stable or rising?
├── At least 3-5 active creatives?
├── No creative fatigue signals?
└── Ready if: All 3 checks positive

□ TECHNICAL READINESS
├── Pixel/CAPI working correctly?
├── No delivery issues?
├── Budget cap not reached?
└── Ready if: All 3 checks positive

SCALING GO/NO-GO:
├── 12/12 checks: GO - Scale aggressively
├── 9-11 checks: CAUTIOUS - Scale conservatively
├── 6-8 checks: PREPARE - Fix issues first
└── <6 checks: NO-GO - Do not scale
```

## Scaling Calculator

### Vertical Scaling (Budget Increase)

```
BUDGET SCALING CALCULATOR
=========================

INPUT:
├── Current daily budget: $[X]
├── Target daily budget: $[Y]
├── Current CPA: $[Z]
├── Max acceptable CPA: $[W]

CALCULATION:
├── Budget multiplier: Y / X = [M]x
├── Estimated scaling period: log(M) / log(1.2) x 3 days
├── CPA buffer: (W - Z) / Z x 100 = [B]%
└── Risk level: [Low/Medium/High]

EXAMPLE:
Current: $100/day → Target: $500/day

Scaling timeline (20% increments):
├── Week 1: $100 → $120 → $144
├── Week 2: $173 → $207 → $249
├── Week 3: $299 → $358 → $430
└── Week 4: $516 - Target reached!

Total period: ~3-4 weeks for 5x scale
```

### Horizontal Scaling (More Ad Sets)

```
HORIZONTAL SCALING CALCULATOR
=============================

INPUT:
├── Current winning audiences: [COUNT]
├── New audiences to test: [LIST]
├── Budget per test ad set: $[X]
├── Test period: [Y] days

CALCULATION:
├── Total test budget: audiences x budget x days
├── Minimum conversions for conclusion: 50 per ad set
├── Test duration: 50 / (daily conversions estimate)

STRUCTURE:
Original Campaign (proven):
├── Ad Set 1 (winning): $100/day
├── Ad Set 2 (winning): $80/day
└── Ad Set 3 (winning): $60/day

Test Campaign (experimental):
├── Ad Set 4 (new LAL): $30/day
├── Ad Set 5 (new interest): $30/day
└── Ad Set 6 (new geo): $30/day

Rule: Test budget = max 30% of total
```

## Scaling Scenarios

### Scenario 1: Conservative Scale (Low Risk)

```
CONSERVATIVE SCALING PLAN
=========================

Situation: Stable performance, want to maintain

Budget increases: 15% per 4 days
Timeline: Slow but steady
Risk: Low

WEEK 1:
├── Day 1-4: $100/day (baseline)
└── Day 5-7: $115/day (+15%)

WEEK 2:
├── Day 8-11: $132/day (+15%)
└── Day 12-14: $152/day (+15%)

WEEK 3:
├── Day 15-18: $175/day (+15%)
└── Day 19-21: $201/day (+15%)

RESULT: 2x budget in 3 weeks
Expected CPA impact: +5-10%
```

### Scenario 2: Moderate Scale (Medium Risk)

```
MODERATE SCALING PLAN
=====================

Situation: Good performance, room to push

Budget increases: 20% per 3 days
Timeline: Balanced
Risk: Medium

WEEK 1:
├── Day 1-3: $100/day
├── Day 4-6: $120/day (+20%)
└── Day 7: $144/day (+20%)

WEEK 2:
├── Day 8-10: $173/day (+20%)
├── Day 11-13: $207/day (+20%)
└── Day 14: $249/day (+20%)

RESULT: 2.5x budget in 2 weeks
Expected CPA impact: +10-20%
```

### Scenario 3: Aggressive Scale (High Risk)

```
AGGRESSIVE SCALING PLAN
=======================

Situation: Hot product, seasonal urgency

Budget increases: 30-50% per 2-3 days
Timeline: Fast
Risk: High

ONLY USE WHEN:
├── CPA well under target (>30% margin)
├── Proven large audiences
├── Lots of creative variation
└── Willing to accept CPA spike

WEEK 1:
├── Day 1-2: $100/day
├── Day 3-4: $150/day (+50%)
├── Day 5-6: $225/day (+50%)
└── Day 7: $337/day (+50%)

RESULT: 3.4x budget in 1 week
Expected CPA impact: +20-40% (temporary)

FALLBACK PLAN:
If CPA >target + 30%:
└── Reduce budget by 20%
└── Stabilize for 3-4 days
└── Try again with 20% steps
```

## Scaling Decision Tree

```
SCALING DECISION FLOWCHART
==========================

START: Do you want to scale?
│
├─► Question 1: CPA under target?
│   ├── YES → Continue
│   └── NO → STOP, optimize first
│
├─► Question 2: >50 conversions/week?
│   ├── YES → Continue
│   └── NO → STOP, collect more data
│
├─► Question 3: Frequency <2.5?
│   ├── YES → Continue
│   └── NO → Horizontal scale (new audiences)
│
├─► Question 4: CPA margin vs target?
│   ├── >30% under → Aggressive scale possible
│   ├── 15-30% under → Moderate scale
│   └── <15% under → Conservative scale
│
└─► Question 5: How much time?
    ├── <1 week → Aggressive (accept risk)
    ├── 2-3 weeks → Moderate
    └── 4+ weeks → Conservative
```

## Scaling Monitoring Dashboard

### Metrics to Track During Scale

```
DAILY SCALING MONITOR
=====================

Day │ Budget │ Spend │ Conv │  CPA  │ ROAS │ Freq │ Status
────┼────────┼───────┼──────┼───────┼──────┼──────┼────────
 1  │ $100   │ $98   │  8   │ $12.25│ 3.2x │ 1.2  │ green
 2  │ $100   │ $100  │  9   │ $11.11│ 3.5x │ 1.3  │ green
 3  │ $100   │ $99   │  7   │ $14.14│ 2.8x │ 1.4  │ green
 4  │ $120   │ $118  │  8   │ $14.75│ 2.7x │ 1.5  │ green Scale
 5  │ $120   │ $120  │  7   │ $17.14│ 2.3x │ 1.6  │ yellow
 6  │ $120   │ $119  │  9   │ $13.22│ 3.0x │ 1.7  │ green
 7  │ $144   │ $142  │ 10   │ $14.20│ 2.8x │ 1.8  │ green Scale

ALERT TRIGGERS:
├── yellow Warning: CPA +15% vs baseline
├── red Stop: CPA +30% vs baseline or >target
├── red Stop: Frequency >3.0
└── red Stop: CTR drops >20%
```

## Scaling Formulas

### Budget Scaling Formula

```
OPTIMAL DAILY BUDGET CALCULATOR
===============================

Formula for max daily budget per ad set:

Max Budget = (Target CPA x Weekly Conv Goal) / 7

Example:
├── Target CPA: $20
├── Weekly conversions goal: 100
├── Max budget: ($20 x 100) / 7 = $286/day

CHECK: Audience headroom
├── Audience size: 500,000
├── Daily reach at $286: ~15,000 (3%)
└── Headroom: Plenty of room
```

### Scale Timeline Calculator

```
TIMELINE CALCULATOR
===================

From $[A] to $[B] with [X]% steps:

Formula:
Days = (log(B/A) / log(1 + X/100)) x step_interval

Example: $100 → $500, 20% steps, every 3 days
Days = (log(5) / log(1.2)) x 3
Days = (1.61 / 0.18) x 3
Days = 8.9 x 3 = ~27 days

QUICK REFERENCE TABLE:
──────────────────────────────────────────
Multiplier │ 15% steps   │ 20% steps
──────────────────────────────────────────
    2x     │   16 days   │   12 days
    3x     │   25 days   │   19 days
    5x     │   37 days   │   27 days
   10x     │   53 days   │   39 days
──────────────────────────────────────────
```

## Scaling Strategy Templates

### Template: Scale Plan Generator

```
SCALING PLAN - [ACCOUNT/CAMPAIGN]
=================================

CURRENT SITUATION:
├── Daily budget: $[X]
├── CPA: $[Y] (target: $[Z])
├── CPA margin: (Y-Z)/Z x 100 = [M]%
├── Weekly conversions: [N]
└── Frequency: [F]

SCALING GOAL:
├── Target budget: $[TARGET]
├── Multiplier: [TARGET/X]x
└── Deadline: [DATE]

RECOMMENDED APPROACH:
[Conservative/Moderate/Aggressive]

SCALING TIMELINE:

Week 1:
├── [Day]: $[budget] → Actions: [...]
├── [Day]: $[budget] → Check: [...]
└── [Day]: $[budget] → Evaluate: [...]

Week 2:
├── [Day]: $[budget] → Actions: [...]
[etc...]

STOP CONDITIONS:
├── CPA > $[threshold]
├── Frequency > [X]
├── CTR drops below [X]%
└── ROAS < [X]

SUCCESS METRICS:
├── Target reached within [X] days
├── CPA stays under $[X]
└── No learning phase resets
```

## MCP Tool Integration

### Validating Scaling Readiness with Live Data

Before building a scale plan, always verify the pre-scaling checklist with real account data:

```
1. Performance stability check (last 7 days):
→ meta_get_insights(account_id="...", level="adset", date_preset="last_7d", fields=["cost_per_action_type","spend","impressions","reach","frequency"])

2. Learning phase status:
→ meta_get_insights(account_id="...", level="adset", date_preset="last_3d", fields=["spend","impressions","actions"])

3. Check current frequency (audience headroom):
→ meta_get_insights(account_id="...", level="adset", date_preset="last_14d", fields=["frequency","reach","impressions"])
```

Use the results to fill in the scaling readiness checklist before committing to a timeline.

## Example Interaction

**User**: "My campaign is doing well at $100/day and $15 CPA (target is $20). I want to scale to $500/day. How do I do that best?"

**Claude response**:

"Good news - you have 25% CPA margin, that gives room to scale! Here is your plan:

---

**SCALING ASSESSMENT:**

| Metric | Value | Status |
|--------|-------|--------|
| CPA margin | 25% under target | Good |
| Scale multiplier | 5x | Medium |
| Recommended approach | Moderate | OK |

---

**RECOMMENDED TIMELINE (20% steps, ~4 weeks):**

```
Week 1:
├── Day 1-3: $100/day (baseline)
├── Day 4-6: $120/day (+20%)
└── Day 7: $144/day (+20%)

Week 2:
├── Day 8-10: $173/day (+20%)
├── Day 11-13: $207/day (+20%)
└── Day 14: $249/day (+20%)

Week 3:
├── Day 15-17: $299/day (+20%)
├── Day 18-20: $358/day (+20%)
└── Day 21: $430/day (+20%)

Week 4:
├── Day 22-24: $516/day - Target reached!
└── Day 25+: Stabilize
```

---

**MONITORING:**
Stop and stabilize if:
- CPA > $18 (more than 20% increase)
- Frequency > 2.5
- CTR drops >15%

**TIP:** Consider launching a test campaign with new audiences in parallel for horizontal scale. With Advantage+ Audience (2026 recommended approach), Meta handles audience expansion automatically — so horizontal scale via new ad sets is less critical than it used to be when using Advantage+ campaigns.

**MONITOR DAILY with MCP:**
```
meta_get_insights(account_id="...", level="adset", date_preset="today", fields=["spend","cost_per_action_type","frequency","impressions"])
```

Would you like a detailed day-by-day tracking sheet?"

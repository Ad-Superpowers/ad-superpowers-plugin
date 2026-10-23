---
name: meta-scaling-calculator
description: "This skill should be used when the user asks to \"scale a campaign\", \"calculate budget increments\", \"plan a scaling timeline\", or mentions \"scaling without losing performance\", \"Meta Ads scaling strategy\", or \"budget increase risk\". Do NOT use for: bid strategy selection (use bid-strategy-selector), budget allocation across funnel (use full-funnel-designer), performance diagnostics (use performance-troubleshooter)."
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
│  Rule of thumb, not a Meta figure: 15-20% budget increase per   │
│  3-4 days, as long as performance stays stable                  │
└─────────────────────────────────────────────────────────────────┘
```

### The 20% Rule

```
OUR SCALING RULE OF THUMB:
==========================

Rules of thumb, not Meta figures: check them against the account's own history.

Raise the budget by at most 20% per step, then wait about 3 days.
Meta gives no percentage. It says a budget change may or may not be a
significant edit, depending on the magnitude of the change: $100 to $101
is not likely to restart learning, $100 to $1000 may. Small steps make
a restart less likely, not impossible.

Example:
├── Day 1: $50/day
├── Day 4: $60/day (+20%)
├── Day 7: $72/day (+20%)
├── Day 10: $86/day (+20%)
└── Day 13: $103/day (+20%)

After about 2 weeks: budget doubled in steps of 20% or less.
```

Source: Meta Business Help Center, "Significant edits and learning phase" (page undated; checked 2026-10-10). With Advantage+
campaign budget, a campaign budget change might put several ad sets back into learning. In Ad Superpowers,
`meta_update` refuses a budget change of more than 20% unless you pass `acknowledge_learning_reset=True`.
That 20% is the tool's own guard, not a Meta rule.

## Scaling Readiness Check

### Pre-Scaling Checklist

```
BEFORE YOU SCALE - VALIDATE:
==============================

Rules of thumb, not Meta figures: check them against the account's own history.

□ PERFORMANCE STABILITY
├── CPA stable last 7 days? (variation <15%)
├── Sufficient conversions? (>50 per week)
├── Positive ROAS above target?
└── Ready if: All 3 checks positive

□ AUDIENCE HEADROOM
├── Current frequency <2.5?
├── Audience large enough for the higher budget?
├── Reach still has growth potential?
└── Ready if: All 3 checks positive

□ CREATIVE STRENGTH
├── CTR stable or rising?
├── Active ads are genuinely different concepts, not cosmetic variants of one?
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

The 50-per-week check follows Meta's learning phase figure: an ad set usually exits learning after about 50
results in the week after its last significant edit (Meta Business Help Center, "About the learning phase", checked 2026-10-10).

## Scaling Calculator

Rules of thumb, not Meta figures: check them against the account's own history. This covers the step sizes,
waiting days, test budget share and minimum conversions below.

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
├── CPA margin: (W - Z) / W x 100 = [B]%
└── Risk level: [Low/Medium/High]

EXAMPLE:
Current: $100/day → Target: $500/day

Scaling timeline (20% steps, one step every 3 days):
├── Days 1-9:   $100 → $120 → $144
├── Days 10-18: $173 → $207 → $249
├── Days 19-27: $299 → $358 → $430
└── Day 28:     $516 - Target reached!

Total period: about 4 weeks for 5x scale
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

Rules of thumb, not Meta figures: check them against the account's own history. The CPA impact of a step
differs per account, so estimate it only from the account's own past budget changes.

### Scenario 1: Conservative Scale (Low Risk)

```
CONSERVATIVE SCALING PLAN
=========================

Situation: Stable performance, want to maintain

Budget increases: 15% every 3-4 days (twice a week)
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
Expected CPA impact: [from this account's history]
```

### Scenario 2: Moderate Scale (Medium Risk)

```
MODERATE SCALING PLAN
=====================

Situation: Good performance, room to push

Budget increases: 20% per 3 days
Timeline: Balanced
Risk: Medium

SCHEDULE:
├── Day 1-3: $100/day
├── Day 4-6: $120/day (+20%)
├── Day 7-9: $144/day (+20%)
├── Day 10-12: $172/day (+20%)
├── Day 13-15: $206/day (+20%)
└── Day 16-18: $247/day (+20%)
(amounts rounded down, so no step is above 20%)

RESULT: 2.5x budget in about 2.5 weeks
Expected CPA impact: [from this account's history]
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
Expected CPA impact: [from this account's history]
Steps this large may restart learning (Meta: it depends on the
magnitude of the change), and meta_update needs
acknowledge_learning_reset=True for any step above 20%.

FALLBACK PLAN:
If CPA >target + 30%:
└── Reduce budget by 20%
└── Stabilize for 3-4 days
└── Try again with 20% steps
```

## Scaling Decision Tree

Rules of thumb, not Meta figures: check them against the account's own history.

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
 4  │ $120   │ $118  │  9   │ $13.11│ 3.0x │ 1.5  │ green Scale
 5  │ $120   │ $120  │  8   │ $15.00│ 2.6x │ 1.6  │ yellow
 6  │ $120   │ $119  │  9   │ $13.22│ 3.0x │ 1.7  │ green
 7  │ $144   │ $142  │ 10   │ $14.20│ 2.8x │ 1.8  │ green Scale

Baseline CPA (days 1-3): $297 / 24 conversions = $12.38

ALERT TRIGGERS (rules of thumb, not Meta figures: check them against the account's own history):
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

QUICK REFERENCE TABLE (one step every 3 days, rounded up):
──────────────────────────────────────────
Multiplier │ 15% steps   │ 20% steps
──────────────────────────────────────────
    2x     │   15 days   │   12 days
    3x     │   24 days   │   21 days
    5x     │   36 days   │   27 days
   10x     │   51 days   │   39 days
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
├── CPA margin: (Z-Y)/Z x 100 = [M]%
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

2. Learning phase status (insights do not report it; Meta returns it for active ad sets only,
   not for ad sets with dynamic creative, and not every ad account gets it):
→ meta_query(account_id="...", entity_type="adsets", effective_status=["ACTIVE"], fields=["id","name","learning_stage_info"], format="full")
  learning_stage_info.status: LEARNING, SUCCESS (exited) or FAIL (not enough results to exit)

3. Check current frequency (audience headroom):
→ meta_get_insights(account_id="...", level="adset", date_preset="last_14d", fields=["frequency","reach","impressions"])

meta_get_insights returns one page of rows: while a response has paging.next, fetch the next page with
meta_query(account_id="...", entity_type="adsets", pagination_url=<paging.next>) and add its rows.

Note for later budget changes (this readiness check makes none): meta_update takes amounts in
cents (under CBO, change the campaign, not the ad set) and refuses a change of more than 20% from
the current budget unless you pass acknowledge_learning_reset=True. That 20% is Ad Superpowers'
own guard, not a Meta rule.
```

Use the results to fill in the scaling readiness checklist before committing to a timeline. The learning stage
field is described in the Marketing API reference, "Ad Campaign Learning Stage Info"
(checked 2026-10-10).

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
├── Day 1-3: $100/day (baseline)
├── Day 4-6: $120/day (+20%)
├── Day 7-9: $144/day (+20%)
├── Day 10-12: $173/day (+20%)
├── Day 13-15: $207/day (+20%)
├── Day 16-18: $249/day (+20%)
├── Day 19-21: $299/day (+20%)
├── Day 22-24: $358/day (+20%)
├── Day 25-27: $430/day (+20%)
└── Day 28+: $516/day - Target reached, then stabilize
```

---

**MONITORING:**
Stop and stabilize if (rules of thumb, not Meta figures: check them against the account's own history):
- CPA > $18 (more than 20% increase)
- Frequency > 2.5
- CTR drops >15%

**TIP:** Consider launching a test campaign with new audiences in parallel for horizontal scale. If your ad sets use Advantage+ audience, Meta's delivery can already reach people beyond your audience inputs, so check first whether a separate audience adds anything. Meta recommends A/B testing Advantage+ audience for almost all campaign types, but not for retargeting (Meta Business Help Center, "About Advantage+ audience", checked 2026-10-10).

**MONITOR DAILY with MCP:**
```
meta_get_insights(account_id="...", level="adset", date_preset="today", fields=["spend","cost_per_action_type","frequency","impressions"])
```

Would you like a detailed day-by-day tracking sheet?"

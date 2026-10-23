---
name: meta-learning-phase-tracker
description: "This skill should be used when the user asks to \"check learning phase status\", \"predict edit impact\", \"exit learning phase faster\", or mentions \"learning phase\", \"significant edit reset\", or \"ad set health check\". Do NOT use for: campaign structure decisions (use campaign-structure-advisor), performance troubleshooting (use performance-troubleshooter), bid strategy selection (use bid-strategy-selector)."
---
# Learning Phase Tracker

Analyzer for Meta Ads learning phase management. Predicts edit impact and advises on optimal timing for changes.

## Learning Phase Basics

### What Is Learning Phase?

A period during which Meta's algorithm learns who to target and how to bid. Ad sets show "Learning" status until sufficient data has been collected.

### Exit Criteria

```
Meta Business Help Center (sources below): about 50
optimization events in the week after the ad set's last
significant edit. An ad set that is unlikely to get there
shows "Learning limited".

Meta's API can also report a dynamic learning phase per
ad set: learning_stage_info carries dynamic_lp_status,
dynamic_lp_conversions_threshold and
dynamic_lp_days_threshold. When they are filled, read
the threshold there instead of assuming 50 in 7 days.

Practical rule of thumb: plan for about 50 optimization
events per ad set per week.
```

Sources: Meta Business Help Center, "About learning limited" and "Last Significant Edit", both undated, checked 2026-10-10; Marketing API reference, "Ad Campaign Learning Stage Info".

### Learning Phase Statuses

| Status | Meaning | Action |
|--------|---------|--------|
| **Learning** | Algorithm is collecting data | Don't change, wait |
| **Active** | Exited, optimization is stable | Monitor and optimize |
| **Learning Limited** | Insufficient events | Increase budget or use broader targeting |

## Edit Impact Matrix

### Significant Edits (Trigger Learning Reset)

| Edit Type | Impact | Learning Reset? |
|-----------|--------|-----------------|
| Budget >20% increase | High | Depends on size |
| Budget >20% decrease | High | Depends on size |
| Audience change | High | Yes |
| New creative | High | Yes |
| Adding a new ad to the ad set | High | Yes |
| Copy or URL change on an ad | Medium | Yes (a creative change) |
| Optimization goal change | High | Yes |
| Bid strategy change | High | Yes |
| Placement change | Medium | Often yes |
| Pausing the ad set for 7 days or longer | High | Yes (on unpause) |

### Non-Significant Edits (Usually Safe)

| Edit Type | Impact | Learning Reset? |
|-----------|--------|-----------------|
| Budget <20% change | Low | Usually no |
| Ad name change | None | No |
| Campaign name change | None | No |

### What Meta Says About Edits

Meta lists these significant edits, which put the ad set back into the learning phase: any change to targeting, ad creative or the optimization event; adding a new ad to the ad set; pausing the ad set for 7 days or longer (it re-enters learning when you unpause it); and changing the bid strategy. A change to the ad set spending limit, to the bid control, cost per result goal or ROAS goal amount, or to the budget amount may or may not be significant, depending on its size, and Meta publishes no percentage. Under Advantage+ campaign budget, changing the campaign's bid strategy or budget can send several ad sets back into learning ("Significant edits and learning phase", Meta Business Help Center, undated, checked 2026-10-10). Meta's "Last Significant Edit" column shows when the last one happened; through the API, read `last_sig_edit_ts` in the ad set's `learning_stage_info`. The 20% budget lines in this skill, the impact levels, the placement row and the budget zones below are rules of thumb, not Meta figures: check them against the account's own history.

## Budget Change Impact Calculator

### Safe Budget Increase Zones

```
Current Daily Budget: €[X]
Learning Phase Status: [Learning/Active/Limited]

SAFE ZONE (Reset Unlikely):
├── Increase: Up to 20% (€[X x 1.2])
└── Decrease: Up to 20% (€[X x 0.8])

YELLOW ZONE (Possible Reset):
├── Increase: 20-50% (€[X x 1.2] - €[X x 1.5])
└── Decrease: 20-50%
└── Recommendation: Do in 2 steps over 3-4 days

RED ZONE (Likely Reset):
├── Increase: >50%
└── Decrease: >50%
└── Recommendation: Duplicate ad set with new budget
```

### Budget Change Decision Tree

```
Want to increase budget?
│
├─► <20% increase
│   └─► Safe, implement directly
│
├─► 20-50% increase
│   ├─► Ad set in Learning?
│   │   └─► Wait until Active, then increase
│   └─► Ad set Active?
│       └─► Do in 2 steps, 3-4 days apart
│
└─► >50% increase
    └─► Duplicate ad set with new budget
        └─► Keep original running as backup
```

## Learning Phase Exit Strategies

### Quick Exit Tactics

Meta suggests the same levers for an ad set that is Learning limited: a higher budget or bid/cost control, a broader audience, combined ad sets, or a more frequent optimization event such as add to cart instead of purchase ("About learning limited", Meta Business Help Center). The budget formula is our arithmetic for about 50 events a week, a rule of thumb, not a Meta figure.

```
Tactic 1: Budget Boost
├── Daily budget of about CPA x 50 / 7 (room for ~50 events a week)
├── Example: CPA €20 → €1,000/week ≈ €143/day
└── After exit: Scale back to desired level (a large cut can restart learning)

Tactic 2: Broader Targeting
├── Use Advantage+ Audience
├── Remove interest restrictions
├── Expand age ranges
└── More conversion opportunities = faster learning

Tactic 3: Higher-Funnel Event
├── Temporarily optimize for AddToCart instead of Purchase
├── More events = faster learning
├── After exit: Switch back to Purchase (a new significant edit: learning restarts)
└── Note: May affect traffic quality

Tactic 4: Consolidation
├── Merge small ad sets
├── Combine budgets
├── One strong ad set > multiple weak ones
└── Aggregated data = faster learning
```

### Learning Limited Solutions

```
Diagnosis: Why Learning Limited?
│
├─► Budget too low
│   └─► Increase to €[CPA x 50 / 7] per day
│
├─► Audience too small
│   └─► Broader targeting or merge audiences
│
├─► Too few distinct concepts
│   └─► Add a genuinely different concept (look-alike ads count as one)
│
├─► Event too rare
│   └─► Switch to higher-funnel event
│
└─► Competition too high
    └─► Increase budget or adjust bid strategy
```

## Edit Timing Best Practices

Rules of thumb, not Meta figures: check them against the account's own history.

### When to Make Changes

```
BEST TIMING:
├── Beginning of the week (Monday/Tuesday)
│   └─► Gives algorithm weekdays to learn
│
├── After stable 5-7 days of performance
│   └─► Baseline data available for comparison
│
└── NOT during:
    ├── Learning phase (wait for exit)
    ├── Weekend (less data)
    ├── Peak periods (Black Friday, etc.)
    └── Right after previous change (<3 days)
```

### Batch Edits Strategy

```
Multiple edits needed?
│
├─► Option 1: Batch all edits together
│   ├── Advantage: One learning reset instead of multiple
│   └─► Use when: Major refresh/overhaul
│
└─► Option 2: Staggered edits
    ├── Advantage: Isolate impact per change
    ├── Wait 3-5 days between edits
    └─► Use when: Testing hypotheses
```

## Ad Set Health Check

Rules of thumb, not Meta figures: check them against the account's own history. Only the 50-per-week line follows Meta's learning-phase rule.

### Quick Health Assessment

```
AD SET HEALTH CHECK

□ Learning Phase Status: [Learning/Active/Limited]
□ Days in current status: [X]
□ Conversions last 7 days: [X]
□ Daily budget: €[X]
□ Estimated CPA: €[X]
□ Frequency: [X]
□ CTR: [X]%
□ Delivery status: [Active/Limited/Off]

HEALTH SCORE:
├── Green (Healthy): Active + 50+ conv/week + Frequency <4
├── Yellow (Watch): Learning >7 days OR 25-50 conv/week
└── Red (Action needed): Limited OR <25 conv/week OR Frequency >5
```

### Recommended Actions by Status

```
STATUS: Learning (Normal)
├── Days in learning: <7
├── Action: Wait, don't make changes
└── Check again: After 7 days

STATUS: Learning (Extended)
├── Days in learning: >7
├── Action: Evaluate budget/audience/event
└── Consider: Tactic 1-4 from Exit Strategies

STATUS: Learning Limited
├── Action: Immediate intervention
├── Primary: Increase budget
├── Secondary: Broader audience
└── Tertiary: Higher-funnel event

STATUS: Active (Healthy)
├── Action: Monitor, no changes needed
├── Optimize: Test new creatives (add, don't replace; adding ads restarts learning)
└── Scale: 20% budget increase if performance is stable

STATUS: Active (Declining)
├── Symptoms: Rising CPA, falling ROAS
├── Diagnose: Creative fatigue? Audience saturation?
├── Action: Refresh creatives, expand audience
└── Avoid: Major restructuring (resets learning)
```

## Edit Impact Simulator

### Input Template

```
CURRENT AD SET:
- Daily budget: €[X]
- Learning status: [Learning/Active/Limited]
- Days in status: [X]
- Conv. last 7 days: [X]
- Current CPA: €[X]

PROPOSED CHANGE:
- Change type: [budget/audience/creative/bid/event]
- Change details: [specifics]
```

### Output Template

```
EDIT IMPACT ANALYSIS

Proposed Change: [description]

RISK ASSESSMENT:
├── Learning Reset Risk: [Low/Medium/High]
├── Performance Impact: [Minimal/Moderate/Significant]
└── Recovery Time: [X] days

RECOMMENDATION:
[Proceed/Proceed with caution/Delay/Alternative approach]

ALTERNATIVE APPROACH (if risky):
[Safer alternative to achieve same goal]

TIMING ADVICE:
[When to implement if proceeding]

POST-CHANGE MONITORING:
- Day 1-3: [what to monitor]
- Day 4-7: [evaluation criteria]
- Action triggers: [when to intervene]
```

## MCP: Check Learning Phase Status

```python
# Get learning phase status for active ad sets (one page of up to `limit`, default 50;
# if the result has paging.next, pass it as pagination_url to get the rest)
# learning_stage_info: status (LEARNING | SUCCESS | FAIL), conversions, last_sig_edit_ts and,
# where Meta applies them, the dynamic_lp_* thresholds. Meta returns it only for active ad sets,
# not for dynamic creative ad sets, and not for every ad account.
meta_query(account_id="act_XXXXX", entity_type="adsets", effective_status=["ACTIVE"], fields=["id","name","status","daily_budget","optimization_goal","bid_strategy","learning_stage_info"])
```

Edits through `meta_update`: changing an ad set's targeting, optimization_goal, bid_strategy, bid_amount, roas_floor or promoted_object, or a campaign or ad set budget by more than 20%, is refused until you pass `acknowledge_learning_reset=True`. That 20% is the tool's own guard, not a Meta rule.

## Common Scenarios

Rules of thumb, not Meta figures: check them against the account's own history.

### Scenario 1: Doubling Budget

```
Situation: Ad set performing well, want to 2x budget
Risk: High (>50% increase)

Recommendation:
1. Duplicate ad set with 2x budget
2. Keep original running on current budget
3. After 7 days: Evaluate which performs better
4. Pause the underperformer
```

### Scenario 2: Creative Refresh

```
Situation: CTR declining, want to replace all ads
Risk: High (replacing or adding ads restarts learning)

Recommendation:
1. Add new ads to existing ad set (don't replace): adding an
   ad also restarts learning (Meta: "Significant edits and
   learning phase"), but the proven ads keep running
2. Let algorithm test new vs old
3. Pause underperformers after 5-7 days
4. Avoid full creative swap
```

### Scenario 3: Audience Change

```
Situation: Want to add interest targeting
Risk: High (audience change = reset)

Recommendation:
1. Create new ad set with new audience
2. Keep original running in parallel
3. Compare performance after 7-14 days
4. Scale winner, pause loser
```

### Scenario 4: Stuck in Learning

```
Situation: 14 days in Learning, no progress
Diagnosis: Budget €30/day, CPA €25, 8 conv/week

Recommendation:
1. Increase budget toward €179/day (€25 CPA x 50 / 7); a first step to €90/day buys about 25 conv/week
2. OR switch to AddToCart event temporarily
3. OR merge with other ad sets
4. After exit: Optimize back to desired setup
```

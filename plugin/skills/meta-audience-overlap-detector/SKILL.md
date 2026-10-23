---
name: meta-audience-overlap-detector
description: "This skill should be used when the user asks to \"detect audience overlap\", \"consolidate audiences\", \"set up exclusion strategies\", or mentions \"audience overlap\", \"self-bidding\", or \"internal auction competition\". Do NOT use for: campaign structure advice (use campaign-structure-advisor), lookalike strategy (use lookalike-strategy-planner), full-funnel design (use full-funnel-designer)."
---
# Audience Overlap Detector

## Overview

This skill helps identify audience overlap in Meta Ads accounts and fix the poor delivery it can cause. Your ad sets do not bid against each other: when ad sets from the same advertiser would enter the same auction, Meta enters only the one with the best performance history and holds the others back, so those can under-deliver ("About overlapping audiences", Meta Business Help Center). It provides frameworks for overlap analysis and solution strategies.

## Why Overlap Is Problematic

```
┌─────────────────────────────────────────────────────────────────┐
│  AUCTION DYNAMICS WITH OVERLAP                                   │
│                                                                 │
│  User "Anna" is in:                                             │
│  ├── Ad Set A: Interest "Fitness"                               │
│  ├── Ad Set B: Lookalike 1% Purchasers                          │
│  └── Ad Set C: Website Visitors 30d                             │
│                                                                 │
│  Result:                                                        │
│  ├── Meta enters only one of these ad sets in the auction:      │
│  │   the one with the best performance history                  │
│  ├── The others are held back and can under-deliver             │
│  └── Learning phase takes longer (split data)                   │
└─────────────────────────────────────────────────────────────────┘
```

Source for the first two results: "About overlapping audiences" (cited above). The learning-phase line is our reading of Meta's advice to combine similar ad sets so their learning combines ("About the learning phase").

## Overlap Check Method

### Step 1: Audience Overlap Tool (Meta)

```
Location: Ads Manager → Audiences → Select 2 to 5 audiences →
          Actions → Show audience overlap

Meta's notes on the tool:
├── Useful only for audiences of at least 10,000 Accounts Center accounts
└── "% overlap of selected audience" is relative to the selected
    audience: A vs B and B vs A give different percentages

Interpretation (rules of thumb, see below):
├── <10% overlap: Acceptable, no action needed
├── 10-30% overlap: Monitor, consider exclusions
├── 30-50% overlap: Problematic, consolidate or exclude
└── >50% overlap: Critical, merge audiences
```

Source for the location and notes: "About overlapping audiences", Meta Business Help Center. The interpretation bands are ours. Rules of thumb, not Meta figures: check them against the account's own history.

### Step 2: Create Overlap Matrix

Ask the user to share their audiences, and create a matrix:

```
AUDIENCE OVERLAP MATRIX (example values)
=======================

              │ Broad │ LAL 1% │ LAL 3% │ Interest │ Retarg │
──────────────┼───────┼────────┼────────┼──────────┼────────┤
Broad         │   -   │  15%   │  25%   │   35%    │   5%   │
LAL 1%        │  15%  │   -    │  70%   │   20%    │  10%   │
LAL 3%        │  25%  │  70%   │   -    │   30%    │  15%   │
Interest      │  35%  │  20%   │  30%   │    -     │   8%   │
Retargeting   │   5%  │  10%   │  15%   │    8%    │   -    │

Critical: LAL 1% <> LAL 3% = 70% overlap
Warning: Broad <> Interest = 35% overlap
```

Fill the matrix one row at a time, with the row's audience as the selected audience in Meta's tool. Meta's percentage is relative to the selected audience, so in real data the two halves of the matrix will not mirror each other.

## Overlap Scenarios & Solutions

### Scenario 1: Lookalike Overlap

**Problem**: LAL 1%, LAL 2%, LAL 3% running simultaneously

```
CURRENT SITUATION:
├── Ad Set 1: LAL 1% Purchasers
├── Ad Set 2: LAL 2% Purchasers
└── Ad Set 3: LAL 3% Purchasers

OVERLAP: high; from one source, the 1% audience is part of
the 2% and 3% audiences (measure it with the tool in Step 1)

SOLUTION A - Layered Lookalikes (create as one lookalike set;
Meta makes the ranges non-overlapping, so no exclusions needed):
├── Ad Set 1: LAL 0-1%
├── Ad Set 2: LAL 1-3%
└── Ad Set 3: LAL 3-5%
CAUTION: With Advantage+ lookalike on (the default), delivery can
go beyond each range; add each lookalike as an audience control
to keep the layers apart.

SOLUTION B - Consolidation:
└── Ad Set 1: LAL 0-3% (single audience)

SOLUTION C - Source Differentiation:
├── Ad Set 1: LAL 1% from Purchasers
├── Ad Set 2: LAL 1% from High-Value Customers
└── Ad Set 3: LAL 1% from Email Subscribers
```

Sources: a lookalike ratio is the top X% most similar people ("Lookalike audiences", Marketing API); lookalikes created as a set do not overlap ("Create lookalike audience sets to optimize your bids"); Advantage+ lookalike is on by default for new, duplicated and draft ad sets that use lookalikes from website, app or customer list sources ("About Advantage+ lookalike"); a lookalike added as an audience control limits who sees the ads ("How to use custom or lookalike audiences").

### Scenario 2: Interest vs Lookalike Overlap

**Problem**: Interest audiences overlap with lookalikes

```
CURRENT SITUATION:
├── Ad Set 1: Interest "Luxury Fashion"
└── Ad Set 2: LAL 2% Purchasers (luxury items)

OVERLAP: [measure it with the tool in Step 1]

SOLUTION A - Interest Exclusion:
├── Ad Set 1: Interest "Luxury Fashion"
│   └── EXCLUDE: LAL 2% Purchasers
└── Ad Set 2: LAL 2% Purchasers

SOLUTION B - Broad Audience:
└── Ad Set 1: Advantage+ Audience
    └── Suggestion: Interest "Luxury Fashion"
    (Let algorithm optimize)
```

### Scenario 3: Retargeting Overlap

**Problem**: Multiple retargeting audiences overlap

```
CURRENT SITUATION:
├── Ad Set 1: All Website Visitors (30d)
├── Ad Set 2: Product Page Viewers (30d)
└── Ad Set 3: Add to Cart (14d)

OVERLAP: Product viewers AND ATC are also in "All visitors"

SOLUTION - Funnel Exclusions:
├── Ad Set 1: All Visitors (30d)
│   └── EXCLUDE: Product Viewers + ATC
├── Ad Set 2: Product Viewers (30d)
│   └── EXCLUDE: ATC
└── Ad Set 3: Add to Cart (14d)
    └── EXCLUDE: Purchasers (7d)
```

## Exclusion Strategy Framework

Rules of thumb, not Meta figures: check them against the account's own history.

### Vertical Exclusions (Funnel-based)

```
TOFU CAMPAIGN
├── Target: Broad/Cold audiences
└── Exclude: All warm + hot audiences

MOFU CAMPAIGN
├── Target: Engagers, video viewers
└── Exclude: High-intent (ATC, IC) + purchasers

BOFU CAMPAIGN
├── Target: ATC, View Content, IC
└── Exclude: Recent purchasers (7-14d)
```

### Horizontal Exclusions (Within the same stage)

```
When you have multiple ad sets in one campaign:

Ad Set A: Interest Stack 1
Ad Set B: Interest Stack 2
└── These cannot exclude each other: only custom audiences
    can be excluded, not interests. Instead:
    ├── Merge the stacks into one ad set, or
    └── Use one Advantage+ audience ad set with both stacks
        as suggestions

Ad sets that target custom audiences (visitors, engagers,
lists) can still exclude each other's audiences.

OR use Advantage+ campaign budget (one budget on the campaign).
With our tools: meta_create(account_id, "campaign", name,
objective=..., special_ad_categories=[], daily_budget=...);
budget_mode="CBO" is the default. Meta then shifts budget
between the ad sets. Overlapping ad sets still don't compete
in one auction: Meta enters only one.

NOTE: Keep manual exclusions for funnel separation (TOFU/MOFU/BOFU),
also with Advantage+ Audience enabled (custom audience exclusions
stay a hard audience control there).
```

Sources: "Removal of Detailed Targeting Exclusions", Meta for Developers, 21 Jan 2025 (custom audience exclusions remain); Meta's Advantage campaign budget guide sets the budget on the campaign; "About Audience controls and Audience suggestions in Advantage+ audience".

## Account Audit Checklist

### Ask the user for this info:

```
OVERLAP AUDIT QUESTIONNAIRE
============================

1. AUDIENCE INVENTORY
   □ How many active audiences do you have?
   □ Which types? (LAL, Interest, Custom, Saved)
   □ Which windows do you use for retargeting?

2. CAMPAIGN STRUCTURE
   □ How many campaigns are running simultaneously?
   □ Do multiple campaigns use the same audiences?
   □ Do you have exclusions set up?

3. SIGNS OF OVERLAP
   □ Fluctuating delivery between ad sets?
   □ Ad sets spending well below their budgets?
   □ Ad sets stuck in learning phase?
   □ Inconsistent results with equal budgets?
```

## Overlap Diagnosis Decision Tree

Rules of thumb, not Meta figures: check them against the account's own history.

```
START: Suspected overlap
│
├─► Check 1: Are you using LAL 1%, 2%, 3% simultaneously?
│   ├── YES → Consolidate, or layer them as one lookalike set
│   └── NO → Go to Check 2
│
├─► Check 2: Are interest + LAL audiences running simultaneously?
│   ├── YES → Check overlap %, exclude if >20%
│   └── NO → Go to Check 3
│
├─► Check 3: Do you have retargeting audiences without exclusions?
│   ├── YES → Implement funnel-based exclusions
│   └── NO → Go to Check 4
│
├─► Check 4: Are multiple campaigns running on the same audiences?
│   ├── YES → Consolidate campaigns or split audiences
│   └── NO → Overlap is probably not the problem
│
└─► RESULT: Implement recommended exclusion strategy
```

## Audience Consolidation Guide

### When to Consolidate?

Rules of thumb, not Meta figures: check them against the account's own history.

| Situation | Action |
|----------|--------|
| 2+ ad sets with >50% overlap | Merge into 1 ad set |
| LAL 1% + LAL 2% + LAL 3% | Use LAL 0-3% or layer |
| 5+ interest ad sets | Consolidate to 2-3 stacks |
| Multiple retargeting windows | Use longest window + exclusions |

### Consolidation Template

```
FROM (fragmented):
├── Campaign 1
│   ├── Ad Set: LAL 1% - €20/day
│   ├── Ad Set: LAL 2% - €20/day
│   └── Ad Set: LAL 3% - €20/day
└── Total: €60/day, lots of overlap

TO (consolidated):
├── Campaign 1
│   ├── Ad Set: LAL 0-2% - €40/day
│   └── Ad Set: LAL 2-5% - €20/day (same lookalike set as 0-2%)
└── Total: €60/day, minimal overlap if both are audience controls
```

## Performance Impact Monitoring

### Metrics to track after overlap fix:

Rules of thumb, not Meta figures: check them against the account's own history. Fill in the account's own values; no fix guarantees a CPM change.

```
BEFORE/AFTER COMPARISON
========================

Metric              │ Before Fix │ After Fix │ Goal
────────────────────┼────────────┼───────────┼─────────
CPM                 │  [value]   │  [value]  │ vs history
Frequency (7d)      │  [value]   │  [value]  │ ↓ to <3
Delivery Stability  │  Volatile  │  Stable   │ Consistent
Learning Phase Exit │   Slow     │  Faster   │ <7 days
Budget Spend Rate   │  Uneven    │   Even    │ Consistent
```

Meta: an ad set usually exits the learning phase after about 50 results in the week after its last significant edit ("About the learning phase").

## Example Interaction

**User**: "My CPMs have risen enormously in recent weeks and some ad sets are barely getting delivery. Could it be overlap?"

**Claude response**:

"The delivery drop fits audience overlap: Meta holds back overlapping ad sets in the auction. The CPM rise can have other causes, so let's check both:

**Can you tell me:**
1. Which audiences are currently running?
2. Have you recently added new ad sets?
3. Are you using multiple Lookalike percentages (1%, 2%, 3%)?
4. Do you have exclusions set up between your ad sets?

**Typical signs of overlap:**
- Delivery shifting between ad sets with similar audiences
- Some ad sets getting no delivery
- Ad sets stuck in learning phase for a long time
- Inconsistent costs between similar ad sets

Share your account ID and I'll list your audiences and active ad sets to see where they overlap."

## MCP Tool Usage

### Step 1: List custom audiences to find IDs

```python
meta_query(
    account_id="act_XXXXXXXXX",
    entity_type="customaudiences"
)
```

### Step 2: Get overlap between any 2+ audiences

```python
meta_query(
    account_id="act_XXXXXXXXX",
    entity_type="audienceoverlap",
    entity_id="AUDIENCE_ID_1,AUDIENCE_ID_2"
)
```

This call uses an overlap endpoint that Meta's public Marketing API does not document, and in our own test it returned Meta error #100 for valid audience IDs. If it returns an error, do not retry: compare the audiences with the Ads Manager tool from Step 1 (up to 5 at a time) and ask the user for the numbers.

### Step 3: List active ad sets to see which audiences are in use

```python
meta_query(
    account_id="act_XXXXXXXXX",
    entity_type="adsets",
    effective_status=["ACTIVE"],
    fields=["name", "targeting", "status", "daily_budget"]
)
```

Cross-reference the audience IDs in `targeting.custom_audiences` across ad sets to spot duplicates, then use the overlap numbers (from Step 2, or from the Ads Manager tool) to quantify the issue.

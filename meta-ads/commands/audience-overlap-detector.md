---
description: Detect audience overlap issues in Meta campaigns. Find where you're competing against yourself and wasting budget. (requires Pro subscription)
---

> **Platforms:** meta
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Audience Overlap Detector

Detect and resolve audience overlap in Meta Ads campaigns.

## Why Overlap Matters
- Overlapping audiences compete in the same auction
- Drives up CPMs and wastes budget
- Causes attribution confusion
- Leads to audience fatigue faster

## Instructions

### 1. Map All Audiences
For each active ad set, document:
- Targeting criteria (interests, behaviors, demographics)
- Custom audiences used
- Lookalike audiences
- Exclusions applied

### 2. Identify Overlap

**Direct Overlap:**
- Same custom audience in multiple ad sets
- Similar lookalikes (1%, 2%, 3% of same seed)
- Identical interest/behavior targeting

**Indirect Overlap:**
- Broad targeting competing with specific
- Retargeting without proper exclusions
- Lookalikes overlapping with custom audiences

### 3. Output Format

```
================================================================================
                         AUDIENCE OVERLAP DETECTOR
                    Account: [Name] | Active Ad Sets: [X]
================================================================================

OVERLAP SUMMARY:
----------------
- High overlap pairs detected: [X]
- Medium overlap pairs: [X]
- Estimated budget waste: €XXX/month

HIGH OVERLAP PAIRS (Action Required):
-------------------------------------
Pair 1:
- Ad Set A: [Name] | Audience: [Description]
- Ad Set B: [Name] | Audience: [Description]
- Estimated Overlap: XX%
- Combined Spend: €X,XXX
- Impact: [Higher CPMs, attribution issues]
- Fix: [Specific recommendation]

Pair 2:
[Continue for each high-overlap pair]

LOOKALIKE STACKING ISSUES:
--------------------------
| Seed Audience     | 1% LAL | 2% LAL | 3% LAL | Issue                    |
|-------------------|--------|--------|--------|--------------------------|
| [Purchasers]      | Active | Active | Active | 1% contained in 2% & 3%  |

Recommendation: Use 1% only, or split: 1%, 2-3%, 3-5%

EXCLUSION GAPS:
---------------
| Ad Set           | Missing Exclusion        | Impact              |
|------------------|--------------------------|---------------------|
| [Prospecting]    | Not excluding purchasers | Wasting on converters|
| [LAL Campaign]   | Not excluding CRM list   | Targeting existing   |

RECOMMENDED RESTRUCTURE:
------------------------
1. [Specific restructure suggestion]
2. [Exclusion to implement]
3. [Audience consolidation opportunity]

PROPER EXCLUSION HIERARCHY:
---------------------------
Prospecting campaigns should exclude:
- All purchasers (180 days)
- All leads (90 days)
- Website visitors (if retargeting separate)

Retargeting campaigns should exclude:
- Recent purchasers (based on purchase cycle)
- Already converted leads (if lead gen)
```
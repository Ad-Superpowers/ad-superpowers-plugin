---
name: performance-troubleshooter
description: |
  Diagnoses and resolves Google Ads performance problems using decision trees and root cause analysis. Use when: CPA/ROAS degradation, conversion drops, impression share declines, Quality Score problems, budget and bidding issues. Do NOT use for: full account audits (use account-auditor), keyword strategy planning (use keyword-strategy-planner).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "google_ads"
  phase: "fase-4-measurement-attribution"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---
# Performance Troubleshooter

Systematic guide for diagnosing and resolving Google Ads performance problems with decision trees, root cause analysis, and concrete solutions.

## Quick Diagnosis Guide

```
WHAT PROBLEM DO YOU HAVE?
│
├─► CONVERSIONS DROPPED
│   └─► Go to: "Conversion Drop Diagnosis"
│
├─► CPA INCREASED / ROAS DECREASED
│   └─► Go to: "Efficiency Degradation Diagnosis"
│
├─► IMPRESSIONS / CLICKS DROPPED
│   └─► Go to: "Volume Decline Diagnosis"
│
├─► NO DELIVERY (0 impressions)
│   └─► Go to: "Delivery Problems"
│
├─► QUALITY SCORE DROPPED
│   └─► Go to: "Quality Score Troubleshoot"
│
└─► SMART BIDDING NOT WORKING
    └─► Go to: "Bidding Problems"
```



See [decision-trees.md](references/decision-trees.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.



## Output: Troubleshooting Report Template

```markdown
# Performance Troubleshooting Report

## Issue Summary
- **Problem detected:** [Description]
- **First signal:** [Date]
- **Impacted campaigns:** [List]
- **Severity:** [Critical/Warning/Info]

## Symptoms
| Metric | Previous Period | Current Period | Change |
|--------|----------------|----------------|--------|
| Impressions | [X] | [X] | [%] |
| Clicks | [X] | [X] | [%] |
| CTR | [X]% | [X]% | [%] |
| Conversions | [X] | [X] | [%] |
| CPA | [X] | [X] | [%] |
| ROAS | [X]% | [X]% | [%] |

## Root Cause Analysis

### Investigated Factors
- [ ] Conversion tracking: [OK/Issue found]
- [ ] Landing page: [OK/Issue found]
- [ ] Ad copy/creatives: [OK/Issue found]
- [ ] Bidding strategy: [OK/Issue found]
- [ ] Budget: [OK/Issue found]
- [ ] Competition: [Changed/Stable]
- [ ] Seasonality: [Yes/No]

### Identified Cause
**[Describe root cause]**

Evidence:
1. [Evidence 1]
2. [Evidence 2]
3. [Evidence 3]

## Solutions

### Immediate Actions (Now)
1. [Action 1]
2. [Action 2]

### Short Term (This Week)
1. [Action 1]
2. [Action 2]

### Long Term (Prevention)
1. [Action 1]
2. [Action 2]

## Monitoring Plan
- Daily check: [Metrics to monitor]
- Weekly review: [KPIs]
- Escalation trigger: [When to escalate again]

## Lessons Learned
- [Learning 1]
- [Learning 2]
- [Preventive measure for the future]
```

---
description: Get a 0-100 health score for each account with prioritized issue list and quick win recommendations. Perfect for managing large portfolios. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Account Health Scoring

Calculate health scores and prioritize accounts needing attention.

## Scoring Methodology

### Health Score Components (0-100)
| Component | Weight | Scoring Criteria |
|-----------|--------|------------------|
| Performance vs Target | 30% | ROAS/CPA within target = 30, deviation reduces score |
| Budget Efficiency | 20% | Proper pacing = 20, over/underspend reduces |
| Account Structure | 15% | Clean structure = 15, issues reduce |
| Creative Health | 15% | Fresh creatives = 15, fatigue reduces |
| Trend Direction | 20% | Improving = 20, stable = 15, declining = 5 |

### Score Interpretation
| Score | Status | Action |
|-------|--------|--------|
| 80-100 | Excellent | Maintain, consider scaling |
| 60-79 | Good | Minor optimizations needed |
| 40-59 | Needs Attention | Prioritize for review |
| 0-39 | Critical | Immediate action required |

## Instructions

### 1. Calculate Component Scores

For each account:
```python
score = 0

# Performance (30 points)
if actual_kpi meets target:
    score += 30
else:
    deviation = abs(actual - target) / target
    score += max(0, 30 - (deviation * 100))

# Budget efficiency (20 points)
pacing_accuracy = 1 - abs(actual_pacing - 1.0)
score += pacing_accuracy * 20

# Structure (15 points) - check for:
# - Proper campaign organization
# - No overlapping audiences
# - Correct tracking setup
score += structure_score

# Creative health (15 points)
# - No fatigued creatives = 15
# - Some fatigue = 10
# - High fatigue = 5
score += creative_score

# Trend (20 points)
if week_over_week_improvement:
    score += 20
elif stable:
    score += 15
else:
    score += 5
```

### 2. Output Format

```
================================================================================
                         ACCOUNT HEALTH SCORES
                    Portfolio: [X] Accounts | Average Score: [XX]
================================================================================

HEALTH SCORE RANKINGS:
----------------------
| Rank | Account          | Score | Status    | Top Issue              |
|------|------------------|-------|-----------|------------------------|
| 1    | [Best Account]   | 92    | Excellent | None                   |
| 2    | [Account B]      | 78    | Good      | Creative refresh needed|
| ...  | ...              | ...   | ...       | ...                    |
| X    | [Worst Account]  | 34    | Critical  | Conversion drop -45%   |

CRITICAL ACCOUNTS (Score <40):
------------------------------
Account: [Name] | Score: [XX]
Issues:
1. [Issue] - Impact: [XX points lost]
2. [Issue] - Impact: [XX points lost]
Quick Wins:
- [Specific action that could improve score by X points]
- [Specific action that could improve score by X points]

NEEDS ATTENTION (Score 40-59):
------------------------------
[Similar format]

PORTFOLIO INSIGHTS:
-------------------
- Average health score trend: [improving/stable/declining]
- Most common issue across accounts: [Issue]
- Estimated revenue impact of fixing critical issues: €XXX
```
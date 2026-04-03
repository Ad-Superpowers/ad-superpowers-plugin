---
description: Compare two campaigns, time periods, or campaign types head-to-head. Includes statistical significance indicators for A/B tests. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Campaign Battle Report

Compare two campaigns or time periods side-by-side.

## Comparison Type: ab_test

## Instructions

### 1. Gather Comparison Data

**For A/B Test:**
- Campaign A metrics (control)
- Campaign B metrics (variant)
- Same time period, same audience split

**For Period Comparison:**
- Period 1 metrics (baseline)
- Period 2 metrics (comparison)
- Same campaigns, different dates

**For Campaign Type Comparison:**
- Campaign Type A metrics (e.g., PMax)
- Campaign Type B metrics (e.g., Standard Shopping)

### 2. Statistical Significance (for A/B tests)

```python
# Simplified significance check
# For proper testing, use chi-squared or z-test

sample_a = conversions_a
sample_b = conversions_b
rate_a = conversions_a / clicks_a
rate_b = conversions_b / clicks_b

relative_lift = (rate_b - rate_a) / rate_a * 100

# Rough significance threshold
if sample_a > 100 and sample_b > 100:
    if abs(relative_lift) > 10:
        significance = "Likely Significant"
    else:
        significance = "Not Significant - Need more data"
else:
    significance = "Insufficient sample size"
```

### 3. Output Format

```
================================================================================
                         CAMPAIGN BATTLE REPORT
                    A/B Test Analysis
================================================================================

CONTESTANTS:
------------
A: [Campaign/Period A Name]
B: [Campaign/Period B Name]
Period: [Date Range]

HEAD-TO-HEAD COMPARISON:
------------------------
| Metric          | A              | B              | Difference  | Winner |
|-----------------|----------------|----------------|-------------|--------|
| Spend           | €X,XXX         | €X,XXX         | +/-XX%      | A/B    |
| Impressions     | XXX,XXX        | XXX,XXX        | +/-XX%      | A/B    |
| Clicks          | X,XXX          | X,XXX          | +/-XX%      | A/B    |
| CTR             | X.XX%          | X.XX%          | +/-XX%      | A/B    |
| Conversions     | XXX            | XXX            | +/-XX%      | A/B    |
| Conv. Rate      | X.XX%          | X.XX%          | +/-XX%      | A/B    |
| CPA             | €XX.XX         | €XX.XX         | +/-XX%      | A/B    |
| ROAS            | X.XXx          | X.XXx          | +/-XX%      | A/B    |

WINNER DECLARATION:
-------------------
WINNER: [A or B]

Primary KPI ([CPA/ROAS/CVR]): [Winner] outperformed by XX%
Statistical Significance: [Significant / Not Significant / Need More Data]
Confidence Level: [High / Medium / Low]

KEY INSIGHTS:
-------------
1. [Main takeaway from comparison]
2. [Secondary insight]
3. [Unexpected finding]

RECOMMENDED ACTIONS:
--------------------
Based on this comparison:
1. [Action item #1]
2. [Action item #2]
3. [Action item #3]

CAVEATS:
--------
- [Any data quality issues]
- [External factors to consider]
- [Minimum sample size recommendations]
```
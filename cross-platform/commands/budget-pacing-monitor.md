---
description: Real-time budget tracking with end-of-month projections. Prevent overspend and underspend surprises with velocity anomaly detection.
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** free
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Budget Pacing Monitor

Monitor budget pacing across all connected ad accounts.

## Instructions

### 1. Gather Budget Data
For each account/campaign, retrieve:
- Monthly budget (or daily budget * days in month)
- Spend to date this month
- Days elapsed / days remaining in month

### 2. Calculate Pacing Metrics

```python
# Pacing calculation logic
ideal_daily_spend = monthly_budget / days_in_month
actual_daily_spend = spend_to_date / days_elapsed
pacing_ratio = actual_daily_spend / ideal_daily_spend
projected_spend = actual_daily_spend * days_in_month

# Status assignment
if 0.95 <= pacing_ratio <= 1.05:
    status = "GREEN - On Track"
elif 0.85 <= pacing_ratio < 0.95 or 1.05 < pacing_ratio <= 1.15:
    status = "AMBER - Watch"
else:
    status = "RED - Alert"
```

### 3. Output Format

```
================================================================================
                         BUDGET PACING MONITOR
                    Month: [Current Month] | Day [X] of [Y]
================================================================================

SUMMARY:
- Total Monthly Budget: €XXX,XXX
- Spent to Date: €XX,XXX (XX%)
- Projected End-of-Month: €XXX,XXX
- Variance: +/-€X,XXX (+/-XX%)

--------------------------------------------------------------------------------
| Account/Campaign | Budget    | Spent     | Pacing | Projected | Status      |
--------------------------------------------------------------------------------
| [Name]           | €XX,XXX   | €X,XXX    | XX%    | €XX,XXX   | GREEN/AMBER/RED |
--------------------------------------------------------------------------------

RED ALERTS (Immediate Action Required):
---------------------------------------
* [Account]: Projected overspend of €X,XXX (+XX%)
  - Current daily spend: €XXX vs ideal €XXX
  - Recommendation: [Specific action]

* [Account]: Projected underspend of €X,XXX (-XX%)
  - Current daily spend: €XXX vs ideal €XXX
  - Recommendation: [Specific action]

AMBER WARNINGS:
---------------
* [Account]: Slight pacing deviation (XX%)
  - Monitor through [date]
  - Consider: [Adjustment suggestion]

VELOCITY ANOMALIES:
-------------------
* [Account]: Unusual spend velocity detected
  - Today's spend rate: XX% higher/lower than 7-day average
  - Potential cause: [Suggestion]
```

### 4. Critical Alerts

Flag immediately if:
- Projected overspend >{{ alert_threshold | default(10) }}% before month end
- Projected underspend >{{ alert_threshold | default(15) }}% before month end
- Daily spend >150% or <50% of average (velocity anomaly)
- Budget exhaustion projected before month end
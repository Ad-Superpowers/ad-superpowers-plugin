---
description: Automatically detect unusual performance shifts across all accounts with severity levels, budget impact estimation, vertical seasonality context, and action urgency indicators. Catches issues before they become expensive problems. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Anomaly Detective

Scan all accounts for unusual performance anomalies with **budget impact estimation** and **vertical seasonality context**.

## Severity Levels

| Level | Criteria | Action Urgency | Budget Impact |
|-------|----------|----------------|---------------|
| 🔴 CRITICAL | >200% deviation OR conversion tracking down | ACT NOW (0-4h) | >€500/day at risk |
| 🟠 HIGH | >100% deviation OR core metric collapse | ACT TODAY (4-24h) | €100-500/day at risk |
| 🟡 MEDIUM | >50% deviation | MONITOR (24-48h) | €50-100/day at risk |
| 🟢 LOW | >25% deviation | REVIEW (this week) | <€50/day at risk |

## Detection Logic

### Statistical Approach
- Compare today/recent period vs. rolling 7-day average (same day of week when possible)
- Minimum threshold: 20 impressions to avoid noise
- Severity scoring based on spend impact AND deviation percentage

### Alert Thresholds (Sensitivity: medium)
| Alert Type | LOW | MEDIUM | HIGH | Severity |
|------------|-----|--------|------|----------|
| Spend Spike | >200% | >150% | >120% | By impact |
| Conversion Drop | >50% | >30% | >20% | 🔴/🟠/🟡 |
| CPC Anomaly | >40% | >25% | >15% | 🟡/🟢 |
| Impression Loss | >60% | >40% | >25% | 🟠/🟡 |
| CTR Drop | >35% | >20% | >15% | 🟡/🟢 |

## CRITICAL: Vertical Seasonality Patterns

Before flagging an anomaly, check if it matches expected seasonal patterns:

### Travel & Hospitality
| Period | Pattern | Don't Flag If... |
|--------|---------|------------------|
| Jul-Aug | +40-80% spend/conversions | Summer peak - NORMAL |
| Jan | -30-50% dip | Post-holiday slow - NORMAL |
| Mar-Apr | +20-30% recovery | Spring break booking - NORMAL |
| Dec 15-25 | -40% conversions | Holiday pause - NORMAL |

### E-commerce / Retail
| Period | Pattern | Don't Flag If... |
|--------|---------|------------------|
| Nov (BFCM) | +100-300% spike | Black Friday/Cyber Monday - NORMAL |
| Dec 1-20 | +50-100% | Holiday shopping - NORMAL |
| Dec 26-Jan 15 | +30% (returns/gift cards) | Post-holiday surge - NORMAL |
| Jan 15-Feb | -40-60% dip | Post-holiday slow - NORMAL |

### Education / Training
| Period | Pattern | Don't Flag If... |
|--------|---------|------------------|
| Aug-Sep | +60-100% | Back-to-school/enrollment - NORMAL |
| Jan-Feb | +30-50% | Spring enrollment - NORMAL |
| Jun-Jul | -40-60% | Summer break - NORMAL |
| Dec | -30% | Semester end - NORMAL |

### B2B / SaaS
| Period | Pattern | Don't Flag If... |
|--------|---------|------------------|
| Q1 (Jan-Mar) | +30-50% | New budget cycle - NORMAL |
| Q4 (Oct-Dec) | +40-60% | Use-it-or-lose-it budgets - NORMAL |
| Aug | -30-40% | Summer slowdown - NORMAL |
| Dec 20-Jan 5 | -50-70% | Holiday shutdown - NORMAL |

### Healthcare / Wellness
| Period | Pattern | Don't Flag If... |
|--------|---------|------------------|
| Jan | +50-100% | New Year resolutions - NORMAL |
| Sep | +20-30% | Back-to-routine - NORMAL |
| Dec | -20-30% | Holiday pause - NORMAL |

## Instructions

### 1. Gather Time-Series Data
For each account/campaign:
- Pull daily data for last 14 days
- Calculate 7-day rolling averages (same day of week)
- Compare current period to baseline
- Calculate daily spend for budget impact estimation

### 2. Detect Anomalies with Budget Impact

```python
def detect_anomaly(current, baseline, threshold, daily_spend):
    change = (current - baseline) / baseline * 100

    # Calculate budget impact
    if "spend" in metric_type:
        daily_impact = abs(current - baseline)
    elif "conversion" in metric_type:
        daily_impact = abs(change) * daily_spend * 0.01  # Rough CPA impact
    else:
        daily_impact = daily_spend * abs(change) * 0.005  # Efficiency impact

    # Determine severity
    if abs(change) > threshold * 2 or daily_impact > 500:
        severity = "CRITICAL"
        urgency = "ACT NOW (0-4h)"
    elif abs(change) > threshold * 1.5 or daily_impact > 100:
        severity = "HIGH"
        urgency = "ACT TODAY (4-24h)"
    elif abs(change) > threshold:
        severity = "MEDIUM"
        urgency = "MONITOR (24-48h)"
    else:
        severity = "LOW"
        urgency = "REVIEW (this week)"

    return {
        "detected": True,
        "change": change,
        "severity": severity,
        "urgency": urgency,
        "daily_impact": daily_impact,
        "weekly_impact": daily_impact * 7
    }
```

### 3. Seasonality Check

For each detected anomaly:
```python
def check_seasonality(anomaly, vertical, current_date):
    # Check against vertical patterns
    patterns = VERTICAL_PATTERNS[vertical]

    for pattern in patterns:
        if pattern.matches(current_date, anomaly.direction):
            return {
                "is_seasonal": True,
                "confidence": pattern.confidence,
                "expected_range": pattern.expected_range,
                "message": f"This appears to be typical {vertical} seasonality"
            }

    return {"is_seasonal": False}
```

### 4. Root Cause Analysis

For each anomaly, check:
- ✅ Is this expected seasonality for the vertical?
- Did budget change?
- Were ads paused/activated?
- Did bidding strategy change?
- Is there a platform-wide issue?
- Day-of-week effects?

### 5. Output Format

```
================================================================================
                         ANOMALY DETECTIVE
                    Scan Period: Last 24-48 Hours
                    Sensitivity: medium
================================================================================

EXECUTIVE SUMMARY:
------------------
Total Anomalies: [X]
- 🔴 CRITICAL: [X] (€XXX/day at risk)
- 🟠 HIGH: [X] (€XXX/day at risk)
- 🟡 MEDIUM: [X] (€XXX/day at risk)
- 🟢 LOW: [X] (€XXX/day at risk)

💰 TOTAL DAILY BUDGET IMPACT: €XXX - €XXX
📅 TOTAL WEEKLY IMPACT IF UNADDRESSED: €X,XXX - €X,XXX

🔴 CRITICAL - ACT NOW (0-4 hours):
----------------------------------
Account: [Name] | Platform: [Meta/Google/etc.]
* SPEND SPIKE: +175% vs 7-day average
  - Today: €1,245 | Average: €452
  - 💰 Daily Impact: €793/day overspend
  - ⏱️ Action Urgency: ACT NOW - 4 hours max
  - 🔍 Root Cause: [Auto-generated suggestion]
  - ✅ Recommended Action: [Specific step]
  - 📋 Checklist: [ ] Check bid caps [ ] Review budgets [ ] Pause if needed

Account: [Name] | Platform: [Meta/Google/etc.]
* CONVERSION TRACKING DOWN: 0 conversions in 24h
  - Normal: 45 conversions/day
  - 💰 Daily Impact: €2,250 revenue at risk (at €50 CPA)
  - ⏱️ Action Urgency: ACT NOW - 4 hours max
  - 🔍 Probable Cause: Pixel/tag issue, payment system, or website down
  - ✅ Recommended Action: Check tracking immediately
  - 📋 Checklist:
    [ ] Test pixel/tag in browser dev tools
    [ ] Verify landing page loading
    [ ] Check checkout/payment flow
    [ ] Review platform conversion settings

🟠 HIGH - ACT TODAY (4-24 hours):
---------------------------------
Account: [Name]
* CONVERSION DROP: -45% vs baseline
  - Today: 12 conversions | Average: 22
  - 💰 Daily Impact: €150-300 revenue loss
  - ⏱️ Action Urgency: ACT TODAY - 24 hours
  - 📅 Seasonality Check: [❌ NOT seasonal / ✅ May be seasonal]
  - 🔍 Probable Cause: [Analysis]
  - ✅ Recommended Action: [Step]

🟡 MEDIUM - MONITOR (24-48 hours):
----------------------------------
Account: [Name]
* CPC SPIKE: +28% vs baseline
  - Today: €2.45 | Average: €1.91
  - 💰 Daily Impact: ~€54/day (at current volume)
  - ⏱️ Action Urgency: MONITOR - 48 hours
  - 📅 Seasonality Check: ✅ Possible Q1 B2B budget flush
  - 🔍 Analysis: [Context]
  - ✅ Recommendation: Monitor for 48h before action

🟢 LOW - REVIEW THIS WEEK:
--------------------------
* [Account]: CTR down 18% - within normal variance, no action needed

📅 SEASONALITY CONTEXT:
-----------------------
Current Date: [Date]
Detected Vertical Patterns:

⚠️ SEASONAL ALERTS (Don't Panic!):
| Account | Anomaly | Seasonal? | Confidence | Expected Range |
|---------|---------|-----------|------------|----------------|
| [Travel Co] | +45% spend | ✅ YES | HIGH | Jul travel peak normal |
| [E-comm] | +120% conv | ✅ YES | HIGH | BFCM expected |
| [SaaS] | -35% leads | ❓ MAYBE | MEDIUM | Aug B2B slowdown possible |

TRUE ANOMALIES (Investigate!):
| Account | Anomaly | Seasonal? | Reason |
|---------|---------|-----------|--------|
| [Retail] | -60% conv | ❌ NO | Not aligned with any pattern |

INVESTIGATION CHECKLISTS:
-------------------------
For conversion drops, verify:
[ ] Conversion tracking firing correctly (check browser dev tools)
[ ] Landing page loading properly (test in incognito)
[ ] No checkout/form issues (test full flow)
[ ] Payment processing working (check payment provider status)
[ ] No ad disapprovals (check platform notifications)

For spend spikes, verify:
[ ] Budget caps in place
[ ] Bid strategy settings correct
[ ] No bid limit changes
[ ] Audience expansion not enabled unintentionally

✅ NO ANOMALIES DETECTED:
-------------------------
[List of accounts with stable performance - GREEN status]
```
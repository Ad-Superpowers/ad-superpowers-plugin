---
description: Predicts future campaign performance using historical platform data, seasonality patterns, and trend analysis. Uses Monte Carlo-style uncertainty modeling to provide confidence intervals for projected spend, conversions, and ROAS. Helps set realistic expectations and plan for multiple scenarios. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# AI-Powered Performance Forecasting

Generate performance forecasts with confidence intervals for [specify company_name].

## Overview

This workflow analyzes historical performance data to project future results with uncertainty ranges. Uses industry benchmarks, seasonality factors, and trend analysis to create realistic forecasts with confidence intervals rather than single-point estimates.

## Parameters
- Company: [specify company_name]
- Industry: [specify industry]
- Forecast Period: Next 90 days
- Planned Monthly Budget: €10,000
- Meta Account ID: [specify meta_account_id]
- Google Ads Customer ID: [specify google_ads_customer_id]
- GA4 Property ID: [specify ga4_property_id]
- Historical Data Period: [specify historical_days] days

---

## PHASE 1: Historical Data Collection

### Required Data Points

To generate accurate forecasts, collect the following from connected platforms:


#### Meta Ads Historical Data
```
meta_get_insights(
    account_id="[specify meta_account_id]",
    date_preset="last_90d",
    level="account",
    fields=["spend", "impressions", "clicks", "conversions", "purchase_roas"]
)
```

**Also collect daily breakdown:**
```
meta_get_insights(
    account_id="[specify meta_account_id]",
    date_preset="last_90d",
    time_increment="1",
    level="account"
)
```



#### Google Ads Historical Data
```
google_ads_run_gaql(
    customer_id="[specify google_ads_customer_id]",
    query="""
        SELECT
            segments.date,
            metrics.cost_micros,
            metrics.impressions,
            metrics.clicks,
            metrics.conversions,
            metrics.conversions_value
        FROM customer
        WHERE segments.date DURING LAST_90_DAYS
        ORDER BY segments.date
    """
)
```



#### GA4 Conversion Data
```
ga4_run_report(
    property_id="[specify ga4_property_id]",
    start_date="90daysAgo",
    end_date="yesterday",
    metrics=["sessions", "conversions", "totalRevenue"],
    dimensions=["date", "sessionDefaultChannelGroup"]
)
```


### Manual Data Input (if platforms not connected)

If platform data is not available, provide historical metrics:

| Metric | Last 30 Days | Last 60 Days | Last 90 Days |
|--------|-------------|-------------|--------------|
| **Total Spend** | €____ | €____ | €____ |
| **Conversions** | ____ | ____ | ____ |
| **Revenue** | €____ | €____ | €____ |
| **ROAS** | ____x | ____x | ____x |
| **Avg CPA** | €____ | €____ | €____ |
| **Avg CTR** | ___% | ___% | ___% |

---

## PHASE 2: Trend Analysis

### Performance Trend Identification

**Calculate Key Trends:**

| Metric | 90-Day Trend | 30-Day Trend | Direction |
|--------|-------------|-------------|-----------|
| Spend Efficiency | [Calculate from data] | [Calculate] | ↑↓→ |
| Conversion Rate | [Calculate from data] | [Calculate] | ↑↓→ |
| ROAS | [Calculate from data] | [Calculate] | ↑↓→ |
| CPM | [Calculate from data] | [Calculate] | ↑↓→ |
| CPC | [Calculate from data] | [Calculate] | ↑↓→ |

### Trend Direction Classification

| Trend Category | Definition | Forecast Impact |
|----------------|------------|-----------------|
| **Strong Uptrend** | +15% or more | Apply +10% to base forecast |
| **Moderate Uptrend** | +5% to +15% | Apply +5% to base forecast |
| **Stable** | -5% to +5% | Use base forecast |
| **Moderate Downtrend** | -5% to -15% | Apply -5% to base forecast |
| **Strong Downtrend** | -15% or worse | Apply -10% to base forecast |

### Platform-Specific Trend Factors

| Factor | Meta Impact | Google Impact | LinkedIn Impact | TikTok Impact |
|--------|------------|--------------|-----------------|---------------|
| **Algorithm changes** | Medium | Low | Low | High |
| **Privacy changes** | High | Medium | Low | Medium |
| **Auction pressure** | Medium | High | Medium | Medium |
| **Creative fatigue rate** | High | Low | Low | Very High |

---

## PHASE 3: Seasonality Analysis

### [specify industry] Seasonality Factors

**Monthly Performance Multipliers:**

| Month | Typical Index | Notes |
|-------|--------------|-------|
| January | 0.85 | Post-holiday lull |
| February | 0.90 | Recovery begins |
| March | 0.95 | Spring ramp-up |
| April | 1.00 | Baseline |
| May | 1.00 | Baseline |
| June | 0.95 | Early summer dip |
| July | 0.90 | Summer slowdown |
| August | 0.85 | Peak vacation |
| September | 1.05 | Back-to-business |
| October | 1.10 | Pre-holiday ramp |
| November | 1.25 | Black Friday/sales |
| December | 1.15 | Holiday peak (early) then drop |

**Index interpretation:** 1.00 = baseline, 0.90 = 10% below normal, 1.20 = 20% above normal

### Forecast Period Seasonality: Next 90 days

Based on current date and forecast period, apply these adjustments:

| Month in Forecast | Seasonality Index | Adjusted Multiplier |
|-------------------|------------------|---------------------|
| Month 1 | [From table] | [Index × Trend factor] |
| Month 2 | [From table] | [Index × Trend factor] |
| Month 3 | [From table] | [Index × Trend factor] |

### Special Events Impact

| Event | Expected Dates | CPM Impact | Conversion Impact |
|-------|---------------|------------|-------------------|
| Black Friday | Late November | +50-100% | +30-50% |
| Cyber Monday | After Black Friday | +40-80% | +25-40% |
| Christmas | December 1-24 | +30-60% | +20-40% |
| January Sales | January 1-14 | +20-40% | +15-25% |
| Summer Sales | June-July | +10-20% | +10-15% |

---

## PHASE 4: Monte Carlo-Style Uncertainty Modeling

### Confidence Interval Framework

Instead of single-point forecasts, we model uncertainty with confidence intervals:

**Confidence Levels:**
- **90% Confidence:** Very likely range (conservative)
- **70% Confidence:** Likely range (realistic)
- **50% Confidence:** Central estimate (optimistic)

### Variable Distribution Assumptions

| Metric | Distribution | Low (10th %ile) | Base (50th) | High (90th %ile) |
|--------|-------------|-----------------|-------------|------------------|
| **CPM** | Normal | Base × 0.80 | Historical avg | Base × 1.30 |
| **CTR** | Normal | Base × 0.85 | Historical avg | Base × 1.15 |
| **CVR** | Log-normal | Base × 0.70 | Historical avg | Base × 1.40 |
| **CPA** | Log-normal | Base × 0.75 | Historical avg | Base × 1.50 |
| **ROAS** | Log-normal | Base × 0.60 | Historical avg | Base × 1.50 |

### Uncertainty Factors by Platform

| Platform | Forecast Uncertainty | Why |
|----------|---------------------|-----|
| **Google Search** | Low (±15%) | Stable, intent-based |
| **Meta** | Medium (±25%) | Algorithm variability, creative dependency |
| **LinkedIn** | Medium (±20%) | Smaller audiences, B2B volatility |
| **TikTok** | High (±35%) | Rapid creative fatigue, trend-dependent |

---

## PHASE 5: Forecast Generation

### Planned Budget for Forecast Period

**Monthly Budget:** €10,000
**Forecast Period:** Next 90 days (3 months)
**Total Forecast Budget:** €{{ (monthly_budget | default(10000) | float * 3) | round | int }}

### Base Forecast Calculation

Using historical data + seasonality + trend adjustments:

```
Base Conversions = (Historical Daily Conversions × Days in Period) × Seasonality Index × Trend Factor
Base ROAS = Historical ROAS × Trend Factor × (1 - Platform Uncertainty)
Base Revenue = Budget × Base ROAS
```

### Forecasted Performance Ranges

#### Conversions Forecast

| Timeframe | Pessimistic (10th) | Expected (50th) | Optimistic (90th) | Confidence |
|-----------|-------------------|-----------------|-------------------|------------|
| Month 1 | [Calculate] | [Calculate] | [Calculate] | ±25% |
| Month 2 | [Calculate] | [Calculate] | [Calculate] | ±20% |
| Month 3 | [Calculate] | [Calculate] | [Calculate] | ±20% |
| **Total** | **[Sum]** | **[Sum]** | **[Sum]** | - |

#### ROAS Forecast

| Timeframe | Pessimistic (10th) | Expected (50th) | Optimistic (90th) | Confidence |
|-----------|-------------------|-----------------|-------------------|------------|
| Month 1 | [Base × 0.70] | [Base] | [Base × 1.30] | ±30% |
| Month 2 | [Base × 0.75] | [Base] | [Base × 1.25] | ±25% |
| Month 3 | [Base × 0.75] | [Base] | [Base × 1.25] | ±25% |

#### Revenue Forecast

| Timeframe | Budget | Pessimistic Rev | Expected Rev | Optimistic Rev |
|-----------|--------|----------------|--------------|----------------|
| Month 1 | €{{ monthly_budget | default(10000) | round | int }} | €[Budget × Low ROAS] | €[Budget × Base ROAS] | €[Budget × High ROAS] |
| Month 2 | €{{ monthly_budget | default(10000) | round | int }} | €[Calculate] | €[Calculate] | €[Calculate] |
| Month 3 | €{{ monthly_budget | default(10000) | round | int }} | €[Calculate] | €[Calculate] | €[Calculate] |

---

## PHASE 6: Scenario Analysis

### Scenario 1: Base Case (Most Likely)

**Assumptions:**
- Current trends continue
- No major platform changes
- Consistent budget allocation
- Normal seasonality

**Projected Outcomes:**

| Metric | Month 1 | Month 2 | Month 3 | Total |
|--------|---------|---------|---------|-------|
| Spend | €{{ monthly_budget | default(10000) | round | int }} | €{{ monthly_budget | default(10000) | round | int }} | €{{ monthly_budget | default(10000) | round | int }} | €{{ (monthly_budget | default(10000) | float * 3) | round | int }} |
| Conversions | [Base] | [Base] | [Base] | [Sum] |
| ROAS | [Base]x | [Base]x | [Base]x | [Avg]x |
| Revenue | [Calculate] | [Calculate] | [Calculate] | [Sum] |

**Probability:** 60%

### Scenario 2: Upside Case (Optimistic)

**Assumptions:**
- Creative testing succeeds (new winners)
- Algorithm favorability improves
- Strong seasonal performance
- Efficient scaling

**Projected Outcomes:**

| Metric | Month 1 | Month 2 | Month 3 | Total |
|--------|---------|---------|---------|-------|
| Conversions | [Base × 1.2] | [Base × 1.3] | [Base × 1.3] | [Sum] |
| ROAS | [Base × 1.2]x | [Base × 1.3]x | [Base × 1.3]x | [Weighted avg]x |
| Revenue | [Calculate] | [Calculate] | [Calculate] | [Sum] |

**Probability:** 25%

### Scenario 3: Downside Case (Pessimistic)

**Assumptions:**
- Creative fatigue accelerates
- CPM inflation continues
- Conversion rates decline
- Competitive pressure increases

**Projected Outcomes:**

| Metric | Month 1 | Month 2 | Month 3 | Total |
|--------|---------|---------|---------|-------|
| Conversions | [Base × 0.8] | [Base × 0.75] | [Base × 0.7] | [Sum] |
| ROAS | [Base × 0.7]x | [Base × 0.65]x | [Base × 0.6]x | [Weighted avg]x |
| Revenue | [Calculate] | [Calculate] | [Calculate] | [Sum] |

**Probability:** 15%

---

## Output Format

```
================================================================================
                    PERFORMANCE FORECAST
                    [specify company_name] - Next 90 Days
                    Budget: €{{ (monthly_budget | default(10000) | float * 3) | round | int }} total
================================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Forecast Overview:**
Based on [X days] of historical data, [platform data sources], seasonality patterns,
and uncertainty modeling, here are projected outcomes for the next 90 days:

**Key Projections (Expected Case):**
| Metric | Projection | Confidence Range |
|--------|------------|------------------|
| Total Spend | €{{ (monthly_budget | default(10000) | float * 3) | round | int }} | Fixed (planned) |
| Conversions | [Expected] | [Low] - [High] (70% CI) |
| Revenue | €[Expected] | €[Low] - €[High] (70% CI) |
| Blended ROAS | [Expected]x | [Low]x - [High]x (70% CI) |
| Avg CPA | €[Expected] | €[Low] - €[High] (70% CI) |

**Forecast Confidence:** [High/Medium/Low] based on data quality and platform variability.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 MONTHLY FORECAST BREAKDOWN
─────────────────────────────

### Month 1: [Month Name]

| Metric | Pessimistic | Expected | Optimistic |
|--------|------------|----------|------------|
| Budget | €X,XXX | €X,XXX | €X,XXX |
| Conversions | XXX | XXX | XXX |
| ROAS | X.Xx | X.Xx | X.Xx |
| Revenue | €X,XXX | €X,XXX | €X,XXX |
| CPA | €XX | €XX | €XX |

**Seasonality Factor:** [X.XX] ([Description])
**Key Considerations:** [Month-specific notes]

---

### Month 2: [Month Name]
[Repeat format]

---

### Month 3: [Month Name]
[Repeat format]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 CONFIDENCE INTERVAL VISUALIZATION
────────────────────────────────────

**ROAS Forecast Range:**

```
Month 1: [Low]x ████████████████████████████ [High]x
                      ▲ Expected: [X.X]x

Month 2: [Low]x ██████████████████████████ [High]x
                    ▲ Expected: [X.X]x

Month 3: [Low]x ████████████████████████ [High]x
                  ▲ Expected: [X.X]x
```

**Conversion Forecast Range:**

```
Month 1: [Low] ████████████████████████████ [High]
                    ▲ Expected: [XXX]

Month 2: [Low] ██████████████████████████ [High]
                  ▲ Expected: [XXX]

Month 3: [Low] ████████████████████████ [High]
                ▲ Expected: [XXX]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 SCENARIO SUMMARY
───────────────────

| Scenario | Probability | Total Conv. | Total Revenue | ROAS |
|----------|------------|-------------|---------------|------|
| **Downside** | 15% | [Low] | €[Low] | [Low]x |
| **Base Case** | 60% | [Expected] | €[Expected] | [Exp]x |
| **Upside** | 25% | [High] | €[High] | [High]x |

**Expected Value Calculation:**
EV(Conversions) = (0.15 × [Low]) + (0.60 × [Expected]) + (0.25 × [High]) = [EV]
EV(Revenue) = (0.15 × €[Low]) + (0.60 × €[Expected]) + (0.25 × €[High]) = €[EV]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 SEASONALITY IMPACT
─────────────────────

| Month | Seasonality Index | Impact Description |
|-------|------------------|-------------------|
| [Month 1] | [X.XX] | [Above/Below average - reason] |
| [Month 2] | [X.XX] | [Above/Below average - reason] |
| [Month 3] | [X.XX] | [Above/Below average - reason] |

**Seasonal Recommendations:**
- [Month with high index]: [Increase budget / expect better performance]
- [Month with low index]: [Plan for efficiency / reduce expectations]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ FORECAST RISKS & SENSITIVITIES
─────────────────────────────────

### Key Risk Factors

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| CPM inflation > 20% | Medium | -15% ROAS | Budget flexibility, creative refresh |
| Creative fatigue | High | -20% CVR | Weekly creative pipeline |
| Platform algorithm change | Low | ±25% variance | Diversify platforms |
| Competitive pressure | Medium | -10% ROAS | Monitor auction insights |
| Conversion tracking issues | Low | Measurement gap | Regular QA checks |

### Sensitivity Analysis

**Impact of 10% CPM Increase:**
- Conversions: [New projection] (-X% from base)
- ROAS: [New projection] (-X% from base)

**Impact of 10% CVR Improvement:**
- Conversions: [New projection] (+X% from base)
- ROAS: [New projection] (+X% from base)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ FORECAST CONFIDENCE ASSESSMENT
─────────────────────────────────

**Overall Confidence Level:** [High / Medium / Low]

| Factor | Score | Notes |
|--------|-------|-------|
| Historical data quality | [1-5] | [Notes on data completeness] |
| Trend stability | [1-5] | [Notes on trend consistency] |
| Platform predictability | [1-5] | [Notes on platform variance] |
| Seasonal alignment | [1-5] | [Notes on seasonal patterns] |
| External factors | [1-5] | [Notes on market conditions] |

**Average Score:** [X.X/5]

**Recommendation:** [Interpret confidence and suggest buffer/contingency]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 RECOMMENDATIONS
──────────────────

**Based on this forecast:**

1. **Budget Planning:**
   - [Recommendation based on forecast ranges]
   - Build [X%] contingency for downside scenario

2. **Performance Targets:**
   - Set targets at [Expected Case] level
   - Trigger optimization reviews if hitting [Downside] range

3. **Monitoring Cadence:**
   - Weekly: Check pacing vs. forecast
   - Bi-weekly: Compare actuals to confidence intervals
   - Monthly: Full forecast refresh

4. **Suggested Next Workflows:**
   - [ ] **Budget Pacing Monitor** - Track actual vs. forecasted spend
   - [ ] **Weekly Performance Pulse** - Regular performance check-ins
   - [ ] **Anomaly Detector** - Alert when outside confidence intervals
```

---

## Forecast Methodology Notes

### Data Requirements for Accurate Forecasting

| Data Type | Minimum | Recommended | Impact on Accuracy |
|-----------|---------|-------------|-------------------|
| Historical days | 30 | 90+ | ±20% accuracy improvement |
| Daily granularity | Yes | Yes | Critical for trend detection |
| Platform breakdown | 1 platform | All active | Better attribution |
| Conversion data | Basic | With value | Enables ROAS forecasting |

### Forecast Accuracy Expectations

| Forecast Horizon | Expected Accuracy | Confidence |
|------------------|------------------|------------|
| 30 days | ±15-20% | High |
| 60 days | ±20-30% | Medium |
| 90 days | ±25-35% | Medium |
| 180 days | ±35-50% | Low |

### When to Refresh Forecasts

- **Weekly:** If actuals deviate >15% from forecast
- **Monthly:** Standard refresh cadence
- **Immediately:** After major platform changes, algorithm updates, or budget changes
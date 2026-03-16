---
description: Design rigorous incrementality tests to measure true advertising impact. Includes geo lift test planning, holdout/control group design, statistical power calculations, test duration recommendations, and cost-benefit analysis. Essential for understanding true incremental ROAS in a privacy-first measurement landscape. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Incrementality Test Designer

Design a rigorous incrementality test to measure the **true causal impact** of your advertising.

## Why Incrementality Testing Matters (2026)

In a privacy-first world, traditional attribution is increasingly unreliable:
- iOS signal loss: 40-60% of conversions untracked on Meta
- Cookie deprecation: Cross-site tracking severely limited
- Platform modeling: 50-65% of reported conversions are "modeled" (estimated)
- Channel overlap: Same user credited by multiple platforms

**Incrementality testing answers the only question that matters:**
"What additional revenue did this advertising create that wouldn't have happened anyway?"

---

## Test Parameters

**Test Focus:**
- Platform to test: Not specified
- Campaign type: All campaigns
- Current monthly spend: €X,XXX
- Geographic scope: Netherlands
- Business type: E-commerce

---

## Instructions

### 1. Determine Test Type

**Choose the Right Test for Your Situation:**

| Test Type | Best For | Min Budget | Min Duration | Confidence |
|-----------|----------|-----------|--------------|------------|
| **Geo Lift** | Any channel, any size | €5K/month | 4-6 weeks | High |
| **Conversion Lift (Meta)** | Meta only | €2K/month | 2-4 weeks | Medium-High |
| **Brand Lift (Google)** | Brand awareness | €5K+ | 2 weeks | High |
| **Holdout Test** | Retargeting | €3K/month | 3-4 weeks | Medium |
| **Ghost Bids** | Display/Video | €10K/month | 4 weeks | High |
| **Full MMM** | All channels | €100K+/month | 8-12 weeks | Highest |

**Tool Usage:**
First, gather current performance data:
- Meta: `meta_get_insights(account_id, date_preset="last_90d", level="campaign")`
- Google: `google_ads_run_gaql(customer_id, query="SELECT campaign.name, metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions FROM campaign WHERE segments.date DURING LAST_90_DAYS")`
- GA4: `ga4_run_report(property_id, start_date, end_date, metrics=["conversions", "totalRevenue"], dimensions=["source", "medium"])`

### 2. Output Format

```
================================================================================
                    INCREMENTALITY TEST DESIGN
                    Platform: [Platform]
================================================================================

📊 TEST RECOMMENDATION
─────────────────────

**Recommended Test Type:** [Geo Lift / Conversion Lift / Holdout / etc.]

**Why This Test:**
- [Reason 1 based on spend level]
- [Reason 2 based on platform]
- [Reason 3 based on geography]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🗺️ GEO LIFT TEST DESIGN
────────────────────────

**Test vs Control Region Selection:**

| Factor | Test Regions | Control Regions |
|--------|-------------|-----------------|
| Population | [50% of target] | [50% of target] |
| Historical similarity | Must match within 15% | Baseline |
| Economic indicators | Similar GDP/income | Similar GDP/income |
| Suggested regions | [List 3-5 regions] | [List 3-5 regions] |

**For Netherlands:** Consider these geo splits:
| Option | Test Regions | Control Regions | Balance Score |
|--------|-------------|-----------------|---------------|
| North/South | Noord-Holland, Zuid-Holland, Utrecht | Noord-Brabant, Gelderland, Limburg | 85% |
| East/West | Overijssel, Gelderland, Flevoland | Noord-Holland, Zuid-Holland | 78% |
| Randstad/Rest | Amsterdam, Rotterdam, Den Haag | All other provinces | 72% |

**For Germany:** Consider these geo splits:
| Option | Test Regions | Control Regions | Balance Score |
|--------|-------------|-----------------|---------------|
| North/South | NRW, Niedersachsen, Hamburg | Bavaria, Baden-Württemberg, Hessen | 88% |
| East/West | Former DDR states | Former West states | 65% |

**Recommended Split:** [Specific recommendation with reasoning]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📐 STATISTICAL POWER CALCULATION
────────────────────────────────

**Minimum Detectable Effect (MDE):**

Your test needs enough conversions to detect a meaningful difference.

| Current Metrics | Value |
|-----------------|-------|
| Monthly conversions | [From data] |
| Monthly revenue | [From data] |
| Current ROAS | [Calculated] |

**Power Analysis:**

| Confidence Level | MDE You Can Detect | Required Sample (Conversions) |
|------------------|-------------------|-------------------------------|
| 80% confidence | ±30% | ~200 per group |
| 90% confidence | ±20% | ~400 per group |
| 95% confidence | ±15% | ~800 per group |

**For your spend level (€X,XXX/month):**

| Metric | Your Value | Required for 80% Power | Gap |
|--------|-----------|----------------------|-----|
| Monthly conversions | [X] | 400 (200 per group) | [+/-X] |
| Test duration needed | [Calculate] | [X weeks] | - |

**Interpretation:**
- [ ] Sufficient data for reliable test (400+ monthly conversions)
- [ ] Marginal data - extend test duration or reduce MDE target
- [ ] Insufficient data - consider platform conversion lift instead

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ TEST DURATION RECOMMENDATION
───────────────────────────────

**Minimum Test Duration:** [X weeks]

| Factor | Impact on Duration |
|--------|-------------------|
| Conversion volume | [High/Med/Low volume] → [Shorter/Longer] |
| Purchase cycle | [X days avg] → Add [X days] buffer |
| Seasonality | [Season] → [Adjust for/Avoid] |
| Day-of-week effects | Account for [X] full weeks |

**Recommended Schedule:**

| Phase | Duration | Dates | Activities |
|-------|----------|-------|------------|
| Pre-test baseline | 2 weeks | [Date range] | Measure both regions |
| Test period | 4-6 weeks | [Date range] | Ads ON in test, OFF in control |
| Post-test cooldown | 1 week | [Date range] | Measure lag effects |
| Analysis | 1 week | [Date range] | Statistical analysis |

**Total Timeline:** [X weeks]

**Avoid Testing During:**
- Black Friday / Cyber Monday (Nov 20 - Dec 5)
- Christmas period (Dec 15 - Jan 5)
- Major sports events in your market
- Your own promotional periods

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 COST-BENEFIT ANALYSIS
────────────────────────

**Cost of Testing:**

| Cost Type | Amount | Notes |
|-----------|--------|-------|
| Lost revenue (control) | €[X,XXX] | Estimated 50% of normal revenue in control |
| Media spend (unchanged) | €[X,XXX] | Or reduced if scaling back for test |
| Analysis time | [X hours] | Internal or agency cost |
| **Total Test Cost** | **€[X,XXX]** | |

**Potential Benefit:**

| Scenario | Annual Impact |
|----------|---------------|
| If 20% of spend is non-incremental | Save €[X,XXX]/year |
| If 30% of spend is non-incremental | Save €[X,XXX]/year |
| If spend is 80%+ incremental | Validate/increase budget |

**ROI of Testing:**

```
Test Cost: €[X,XXX]
Potential Annual Savings: €[X,XXX] - €[X,XXX]
ROI Breakeven: [X weeks] of optimized spend
```

**Recommendation:** [Worth testing / Defer testing / Alternative approach]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 HOLDOUT TEST DESIGN (For Retargeting)
────────────────────────────────────────

If testing retargeting incrementality specifically:

**Holdout Structure:**

| Group | Size | Treatment |
|-------|------|-----------|
| Control (Holdout) | 10-20% of audience | No retargeting ads |
| Test | 80-90% of audience | Normal retargeting |

**Platform-Specific Setup:**

**Meta Conversion Lift:**
1. Go to Experiments in Ads Manager
2. Create A/B test with holdout
3. Meta handles randomization and measurement
4. Results in 2-4 weeks

**Google Conversion Lift:**
1. Contact Google rep for conversion lift study
2. Requires minimum spend threshold
3. Google manages holdout and measurement

**Manual Holdout (Any Platform):**
1. Split audience randomly (use user ID hash)
2. Exclude control group from all retargeting
3. Track conversions in both groups
4. Calculate lift manually

**Expected Retargeting Incrementality Benchmarks:**

| Retargeting Type | Expected Incrementality |
|------------------|------------------------|
| Cart abandoners (1-3 days) | 40-60% incremental |
| Cart abandoners (7+ days) | 60-80% incremental |
| Website visitors (generic) | 20-40% incremental |
| Past purchasers | 15-30% incremental |
| Dynamic product ads | 35-55% incremental |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 TEST EXECUTION CHECKLIST
───────────────────────────

**Pre-Test (Week -2 to 0):**
- [ ] Define test and control regions/audiences
- [ ] Set up tracking in both groups
- [ ] Document baseline metrics for both groups
- [ ] Ensure groups are statistically similar (<15% variance)
- [ ] Create suppression lists for control group
- [ ] Brief team on test protocol

**During Test (Week 1-4-6):**
- [ ] Monitor both groups daily (but don't optimize!)
- [ ] Document any external factors (weather, news, etc.)
- [ ] Keep all other marketing activities consistent
- [ ] Track weekly KPIs for both groups
- [ ] Flag any contamination issues immediately

**Post-Test (Week 6+):**
- [ ] Allow 7-day cooldown for lag conversions
- [ ] Calculate lift: (Test - Control) / Control
- [ ] Assess statistical significance (p < 0.05)
- [ ] Document learnings and confidence level
- [ ] Plan next test or budget reallocation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 EXPECTED RESULTS FRAMEWORK
─────────────────────────────

**How to Interpret Your Results:**

| Incrementality Rate | What It Means | Action |
|--------------------|---------------|--------|
| **80-100%** | Highly incremental | Scale aggressively |
| **60-80%** | Mostly incremental | Maintain/optimize |
| **40-60%** | Partially incremental | Review targeting, creative |
| **20-40%** | Low incrementality | Reduce spend, shift budget |
| **<20%** | Mostly cannibalization | Pause or radically restructure |

**Adjusting ROAS for Incrementality:**

```
Reported ROAS: [X.X]x
Measured Incrementality: [XX]%
Incremental ROAS (iROAS): [X.X]x × [XX]% = [X.X]x

Your TRUE return per € is [X.X]x, not [X.X]x
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 NEXT STEPS
─────────────

1. **Before testing:** Run Cross-Platform Comparison to establish baseline
2. **After testing:** Update budget allocation based on iROAS
3. **Ongoing:** Retest every 6-12 months (incrementality changes over time)
4. **Advanced:** Consider full MMM for holistic view

**Suggested Follow-Up Workflows:**
- [ ] Cross-Platform Comparison (with incrementality data)
- [ ] Budget Allocation Planner (with iROAS inputs)
- [ ] Performance Forecaster (adjusted for incrementality)
```

---

## Incrementality Testing Best Practices

### Common Pitfalls to Avoid

| Pitfall | Impact | Prevention |
|---------|--------|-----------|
| Test too short | Inconclusive results | Minimum 4 weeks |
| Unbalanced groups | Biased results | Pre-match on historical KPIs |
| Contamination | Invalid results | Strict geo/audience separation |
| Testing during promos | Noise in data | Avoid sale periods |
| Optimizing during test | Invalidates test | Freeze all settings |

### When NOT to Run Incrementality Tests

- Less than €5K/month spend (use platform lift studies instead)
- During peak season (data too noisy)
- Recent major changes (need stable baseline)
- Fewer than 100 monthly conversions (insufficient data)

### Building a Testing Calendar

| Quarter | Test Focus | Channel | Notes |
|---------|-----------|---------|-------|
| Q1 | [Prospecting] | [Meta] | Post-holiday baseline |
| Q2 | [Retargeting] | [Google] | Pre-summer |
| Q3 | [Brand] | [TikTok] | Before Q4 ramp |
| Q4 | Skip testing | - | Peak season data too valuable |
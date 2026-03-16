---
description: Compare advertising performance across Meta, Google, LinkedIn, and TikTok with attribution reconciliation, incrementality analysis, and competitive context. Includes expected discrepancy ranges, 'which number to trust' guidance, iROAS framework (incremental ROAS estimates by platform), MMM-lite recommendations, privacy-adjusted confidence framework, specific € budget reallocation recommendations, reach/frequency analysis, EU vs US benchmarks, and optional competitive position analysis via Google Ads auction insights. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Cross-Platform Performance Comparison

Compare performance across all connected advertising platforms **with attribution reconciliation guidance and competitive context**.


## Competitive Context Parameters
- Google Ads Customer ID: Not provided - competitive insights limited
- Include Competitor Analysis: [specify include_competitor_context]


## CRITICAL: Attribution Discrepancies Are Normal

Different platforms will report different conversion numbers - this is expected!

### Expected Discrepancy Ranges (vs GA4 as baseline)
| Platform Comparison | Expected Difference | Primary Cause |
|--------------------|--------------------| --------------|
| Meta vs GA4 | Meta +15-30% higher | View-through + modeled conversions |
| Google Ads vs GA4 | Google +10-25% higher | Enhanced Conversions + modeling |
| TikTok vs GA4 | TikTok +20-40% higher | VTA attribution (30% of conversions) |
| LinkedIn vs GA4 | LinkedIn +15-35% higher | Long B2B cycles, cross-device |

### EU vs US Context (Privacy Impact)
| Metric | EU | US | Delta |
|--------|----|----|-------|
| Cookie consent opt-in | ~50% | ~78% (Meta) | -28pp signal loss |
| CTR impact | -2.1% | Baseline | GDPR effect |
| Conversion rate impact | -5.4% | Baseline | Signal loss |
| Meta CPA | +15% | Baseline | Privacy premium |
| Google CPC | +14-29% | Baseline | Market maturity |

**For EU advertisers:** Expect 20-35% higher attribution discrepancies due to GDPR consent rates.

### When to Investigate (>35% discrepancy)
- [ ] Check pixel/tag firing correctly
- [ ] Verify server-side tracking (CAPI) setup
- [ ] Confirm event ID deduplication
- [ ] Check UTM parameter consistency
- [ ] Verify Consent Mode V2 implementation (CRITICAL for EU)

## Instructions

### 1. Gather Platform Data
For each connected platform (last 30 days):
- Total spend, impressions, clicks, conversions
- Revenue (if e-commerce)
- **Reach and frequency** (for brand awareness analysis)
- Calculate: CTR, CPC, CPM, CPA, ROAS

**Tool Usage:**
- Meta: `meta_get_insights(account_id, date_preset="[specify date_range]", fields=["spend", "impressions", "reach", "frequency", "clicks", "actions", "action_values", "cpm", "cpc", "ctr", "purchase_roas"])`
- Google Ads: `google_ads_run_gaql(customer_id, query="SELECT campaign.name, metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions FROM campaign WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.cost_micros DESC")`
- TikTok: `tiktok_get_report(start_date, end_date, level="campaign", metrics=["spend", "impressions", "reach", "frequency", "clicks", "conversions"])`
- LinkedIn: `linkedin_get_analytics(account_id, start_date, end_date, fields=["impressions", "clicks", "costInLocalCurrency", "externalWebsiteConversions"])`
- GA4: `ga4_run_report(property_id, metrics=["conversions", "totalRevenue"])`

### 2. Attribution Reconciliation Analysis

Compare platform-reported conversions to GA4:
```
ATTRIBUTION DISCREPANCY CHECK:
| Platform | Platform Convs | GA4 Convs | Variance | Expected? |
|----------|----------------|-----------|----------|-----------|
| Meta     | [X]            | [Y]       | +XX%     | ✅ <30% OK |
| Google   | [X]            | [Y]       | +XX%     | ✅ <25% OK |
| TikTok   | [X]            | [Y]       | +XX%     | ✅ <40% OK |
| LinkedIn | [X]            | [Y]       | +XX%     | ✅ <35% OK |
```

**If variance exceeds expected range:** Flag for technical investigation.

### 3. Output Format

```
================================================================================
                    CROSS-PLATFORM PERFORMANCE COMPARISON
                    Period: Last 30 Days
================================================================================

ATTRIBUTION CONTEXT:
-------------------
⚠️ Each platform uses different attribution windows:
- Meta: 7-day click, 1-day view (default)
- Google Ads: Data-driven attribution (or last-click)
- TikTok: 7-day click, 1-day view
- LinkedIn: 30-day click, 7-day view (longest for B2B)
- GA4: Cross-channel DDA (typically underreports by 18-35%)

🇪🇺 EU Privacy Impact Note:
- EU consent rates ~50% (vs 78% US on Meta)
- Expect 20-35% additional signal loss in EU markets
- Server-side tracking (CAPI) recovers ~70% of lost signals

PLATFORM OVERVIEW (Platform-Reported):
--------------------------------------
| Platform    | Spend     | % Budget | Convs | CPA      | ROAS   | Efficiency |
|-------------|-----------|----------|-------|----------|--------|------------|
| Meta        | €XX,XXX   | XX%      | XXX   | €XX.XX   | X.XXx  | [ranking]  |
| Google Ads  | €XX,XXX   | XX%      | XXX   | €XX.XX   | X.XXx  | [ranking]  |
| LinkedIn    | €XX,XXX   | XX%      | XXX   | €XX.XX   | X.XXx  | [ranking]  |
| TikTok      | €XX,XXX   | XX%      | XXX   | €XX.XX   | X.XXx  | [ranking]  |
| TOTAL       | €XX,XXX   | 100%     | X,XXX | €XX.XX   | X.XXx  | -          |

REACH & FREQUENCY ANALYSIS (Brand Awareness):
---------------------------------------------
| Platform    | Reach      | Frequency | CPM     | Cost per 1K Reach |
|-------------|------------|-----------|---------|-------------------|
| Meta        | X,XXX,XXX  | X.X/week  | €X.XX   | €X.XX             |
| Google (Display) | X,XXX,XXX | X.X/week | €X.XX | €X.XX            |
| TikTok      | X,XXX,XXX  | X.X/week  | €X.XX   | €X.XX             |
| LinkedIn    | XXX,XXX    | X.X/week  | €XX.XX  | €XX.XX            |

📊 Brand vs Performance Budget Split Guidance:
- Pure e-commerce: 20% awareness / 80% performance
- FMCG/CPG: 60% awareness / 40% performance
- B2B SaaS: 30% awareness / 70% performance
- Current split: [Calculate from reach vs conversion campaigns]

ATTRIBUTION RECONCILIATION:
---------------------------
| Platform | Platform Convs | GA4 Convs | Variance | Status |
|----------|----------------|-----------|----------|--------|
| Meta     | [X]            | [Y]       | +XX%     | [Normal/Investigate] |
| Google   | [X]            | [Y]       | +XX%     | [Normal/Investigate] |
| TikTok   | [X]            | [Y]       | +XX%     | [Normal/Investigate] |
| LinkedIn | [X]            | [Y]       | +XX%     | [Normal/Investigate] |

WHICH NUMBER TO TRUST:
----------------------
📊 Use Case Decision Framework:

| Use Case | Which Data to Use | Why |
|----------|-------------------|-----|
| Optimizing single platform | Platform's own data | Algorithm optimizes on its signals |
| Cross-channel budget allocation | GA4 (adjust +25-35%) | Consistent attribution |
| Reporting to stakeholders | GA4 as truth + context | Consistency builds trust |
| Strategic planning | Consider MMM | Accounts for upper-funnel |

EFFICIENCY RANKING (by ROAS):
------------------------------------------------------------------
1. [Platform] - [Score] - [Why it's performing well]
2. [Platform] - [Score] - [Key strength]
3. [Platform] - [Score] - [Opportunity for improvement]
4. [Platform] - [Score] - [Area of concern]

BUDGET REALLOCATION RECOMMENDATIONS:
------------------------------------
💰 SPECIFIC € RECOMMENDATIONS (with confidence intervals):

| Platform   | Current €  | Recommended € | Change €   | Confidence |
|------------|------------|---------------|------------|------------|
| Meta       | €X,XXX     | €X,XXX        | +/-€X,XXX  | [High/Med] |
| Google Ads | €X,XXX     | €X,XXX        | +/-€X,XXX  | [High/Med] |
| LinkedIn   | €X,XXX     | €X,XXX        | +/-€X,XXX  | [High/Med] |
| TikTok     | €X,XXX     | €X,XXX        | +/-€X,XXX  | [High/Med] |
| TOTAL      | €XX,XXX    | €XX,XXX       | (same)     | -          |

**Confidence Level Guide:**
- HIGH: Strong data (1000+ conversions), clear performance difference (>25%)
- MEDIUM: Moderate data (100-999 conversions), moderate difference (10-25%)
- LOW: Limited data (<100 conversions), small difference (<10%) - wait for more data

📈 EXPECTED IMPACT:
| Action | Monthly € Impact | Confidence Interval |
|--------|------------------|---------------------|
| Shift €X,XXX from [A] to [B] | +€X,XXX - €X,XXX | 70% confidence |
| Reduce [C] by €X,XXX | Save €X,XXX (reinvest) | 85% confidence |
| Scale [D] by €X,XXX | +€X,XXX - €X,XXX | 65% confidence |

**Total Expected Improvement:** +€X,XXX - €X,XXX/month (at current ROAS levels)

REALLOCATION CAVEATS:
- Meta ROAS appears lower due to VTA undercount in GA4 (adjust +20%)
- LinkedIn ROI may be undervalued due to long B2B cycles (30-day attribution)
- TikTok upper-funnel contribution often uncredited (consider awareness value)
- EU markets: Factor in €X,XXX privacy premium (GDPR signal loss)

EU MARKET ADJUSTMENT (if applicable):
-------------------------------------
| Factor | Impact on Budget Decision |
|--------|---------------------------|
| Lower consent rates | Underreported conversions on Meta/TikTok |
| Higher CPCs | Google Ads +14-29% vs US benchmarks |
| B2B premium | LinkedIn CPM +20% YoY (DDMA 2025) |
| Recommendation | Weight server-side tracked channels higher |

CROSS-PLATFORM INSIGHTS:
------------------------
- Attribution window impact: [Analysis]
- Privacy impact estimate: [iOS 14+ signal loss by platform]
- EU consent impact: [If applicable - additional ~20% signal loss]
- Recommended validation: [Geo holdout test or MMM]


📊 INCREMENTAL ROAS (iROAS) FRAMEWORK:
--------------------------------------
Traditional ROAS measures total revenue/spend, but iROAS measures only the INCREMENTAL
revenue that wouldn't have happened without advertising.

### Why iROAS Matters
| Metric | What It Measures | Typical Overstatement |
|--------|------------------|----------------------|
| Platform ROAS | All attributed revenue / spend | 15-40% over-attributed |
| GA4 ROAS | Last-click attributed revenue / spend | 10-25% over-attributed |
| **iROAS** | Incremental revenue / spend | True causal impact |

### Platform-Specific Incrementality Estimates
Based on industry benchmarks and lift studies:

| Platform | Typical ROAS | Est. Incrementality Rate | Est. iROAS |
|----------|-------------|-------------------------|------------|
| Meta Retargeting | 8-15x | 30-50% | 2.4-7.5x |
| Meta Prospecting | 3-6x | 60-80% | 1.8-4.8x |
| Google Brand | 10-30x | 10-30% | 1-9x |
| Google Generic | 4-8x | 70-90% | 2.8-7.2x |
| TikTok | 3-6x | 65-85% | 2-5.1x |
| LinkedIn | 2-4x | 75-90% | 1.5-3.6x |

⚠️ **Key Insight**: Retargeting and brand search show HIGH ROAS but LOW incrementality
because users would likely convert anyway.

### Adjusted Performance Ranking (by Estimated iROAS):
| Platform | Reported ROAS | Est. iROAS | True Efficiency Rank |
|----------|--------------|------------|---------------------|
| [Platform] | X.Xx | X.Xx | #1 |
| [Platform] | X.Xx | X.Xx | #2 |
| [Platform] | X.Xx | X.Xx | #3 |
| [Platform] | X.Xx | X.Xx | #4 |

### Budget Reallocation with iROAS Lens:
| Current Allocation | Recommendation | Reason |
|-------------------|----------------|--------|
| High retargeting spend | Reduce 20-30% | Low incrementality despite high ROAS |
| Low prospecting spend | Increase 15-25% | Higher incrementality, feeds retargeting pool |
| Brand search heavy | Test reduced spend | Often low incrementality |
| Generic search | Maintain/increase | High intent + high incrementality |



🎯 MMM-LITE RECOMMENDATIONS:
----------------------------
Marketing Mix Modeling (MMM) provides the gold standard for understanding true channel
value, but isn't always practical. Here's when to consider each approach:

### When to Use Each Measurement Method

| Situation | Recommended Method | Why |
|-----------|-------------------|-----|
| <€5K/month spend | Platform reporting + GA4 | Insufficient data for testing |
| €5-25K/month | Geo lift tests (1-2 per quarter) | Affordable, actionable |
| €25-100K/month | Regular lift tests + simple MMM | Enough data for modeling |
| €100K+/month | Full MMM + continuous testing | ROI justifies investment |

### DIY MMM-Lite Approach (€25K+/month)
For advertisers not ready for full MMM, these proxies can help:

**1. Simple Spend-Conversion Correlation:**
```
Weekly data: [spend_week_1, spend_week_2, ...] vs [conversions_week_1, ...]
Look for: Correlation > 0.6 suggests channel is working
```

**2. Saturation Check (Diminishing Returns):**
| Spend Level | Conv/€ | Status |
|-------------|--------|--------|
| €0-5K | X.XX | Baseline efficiency |
| €5-10K | X.XX | Slight decrease = normal |
| €10-15K | X.XX | 15%+ decrease = nearing saturation |
| €15K+ | X.XX | Heavy decrease = oversaturated |

**3. Lag Effect Analysis:**
```
Check: Do conversions increase 3-7 days AFTER spend increases?
If yes: Consideration-phase impact (good for awareness channels)
```

### Quick Incrementality Test Options

| Test Type | Cost | Time | Confidence | Best For |
|-----------|------|------|------------|----------|
| Geo Holdout | Low | 4-6 weeks | Medium | Single channel test |
| Conversion Lift (Meta) | Free | 2-4 weeks | Medium-High | Meta campaigns |
| Brand Lift (Google) | €5K+ | 2 weeks | High | Brand awareness |
| Ghost Ads (Research) | Medium | 4 weeks | High | Display/video |
| Full MMM | €15K+ | 8-12 weeks | Highest | Full picture |

### Recommended Next Step for Validation:
Based on your spend level and data maturity:
- **Recommendation:** [Geo holdout test / Meta conversion lift / Simple correlation analysis]
- **Focus on:** [Channel with largest spend but uncertain incrementality]
- **Timeline:** [X weeks to results]



📈 ENHANCED CONFIDENCE FRAMEWORK:
---------------------------------
Every recommendation comes with uncertainty. Here's a privacy-adjusted confidence assessment:

### Data Quality Assessment
| Platform | Signal Quality | Modeling % | Privacy Impact | Overall Confidence |
|----------|---------------|------------|----------------|-------------------|
| Meta | [High/Med/Low] | ~55% modeled | iOS/GDPR: -XX% | [High/Med/Low] |
| Google | [High/Med/Low] | ~35% modeled | Privacy Sandbox | [High/Med/Low] |
| TikTok | [High/Med/Low] | ~60% modeled | Heavy iOS impact | [High/Med/Low] |
| LinkedIn | [High/Med/Low] | ~45% modeled | B2B cookieless | [High/Med/Low] |

### Confidence Adjustments for Recommendations

| Recommendation | Base Confidence | Privacy Adjustment | Final Confidence |
|---------------|-----------------|-------------------|------------------|
| Shift €X to [Platform] | High | -1 level if EU-heavy | [High/Med/Low] |
| Reduce [Platform] | Med | No adjustment | [Med] |
| Scale [Platform] | Low | -1 level for iOS users | [Low] |

### Privacy-First Measurement Stack Status
- [ ] Server-side tracking (CAPI/Enhanced Conversions): [Yes/No/Partial]
- [ ] Consent Mode V2: [Implemented/Not/Partial]
- [ ] First-party data integration: [Active/Planned/None]
- [ ] Conversion API deduplication: [Configured/Not]

**Signal Recovery Estimate:**
| Current Setup | Signal Loss | With Improvements | Potential Recovery |
|---------------|-------------|-------------------|-------------------|
| Client-only | ~40-60% | + Server-side | Recover ~70% |
| Basic server | ~20-35% | + Consent Mode V2 | Recover ~85% |
| Full stack | ~10-15% | Optimized | Near-full signal |

### Recommended Actions for Better Confidence:
1. [Highest impact: e.g., Implement CAPI for Meta]
2. [Second priority: e.g., Enable Enhanced Conversions for Google]
3. [Third: e.g., Set up Consent Mode V2]



⚔️ COMPETITIVE CONTEXT:
-----------------------
Understanding your performance requires competitive context. Your metrics don't exist
in isolation - they're relative to what competitors are achieving in the same auctions.


### Google Ads Competitive Position

Run auction insights to understand your competitive standing:

```
google_ads_run_gaql(
    customer_id="[specify google_ads_customer_id]",
    query="""
        SELECT
            campaign.name,
            auction_insight.domain,
            metrics.auction_insight_search_impression_share,
            metrics.auction_insight_search_top_impression_share,
            metrics.auction_insight_search_absolute_top_impression_share,
            metrics.auction_insight_search_outranking_share,
            metrics.auction_insight_search_overlap_rate,
            metrics.auction_insight_search_position_above_rate
        FROM auction_insight
        WHERE segments.date DURING LAST_30_DAYS
        ORDER BY metrics.auction_insight_search_impression_share DESC
        LIMIT 15
    """
)
```

**Auction Insights Analysis:**

| Competitor Domain | Overlap Rate | Position Above | Outranking | Threat Level |
|-------------------|-------------|----------------|------------|--------------|
| [domain1.com]     | XX%         | XX%            | XX%        | High/Med/Low |
| [domain2.com]     | XX%         | XX%            | XX%        | High/Med/Low |
| [domain3.com]     | XX%         | XX%            | XX%        | High/Med/Low |

**Your Competitive Position:**
| Metric | Your Score | Industry Benchmark | Status |
|--------|-----------|-------------------|--------|
| Search Impression Share | XX% | 20-40% | [Good/Needs Improvement] |
| Top of Page Rate | XX% | 60-80% | [Good/Needs Improvement] |
| Absolute Top Rate | XX% | 30-50% | [Good/Needs Improvement] |

**Interpretation:**
- **Impression Share <20%**: Significant budget or Quality Score gap vs competitors
- **Position Above >60%**: Competitors consistently outbidding you
- **Outranking <40%**: Need to improve bids, Quality Score, or budget

### Competitive Context (Limited)

Without Google Ads Customer ID, competitive insights are limited.
To enable full competitive analysis, provide google_ads_customer_id parameter.

**Available Competitive Signals:**
- Meta: Compare your CPM/CPC to industry benchmarks
- LinkedIn: Compare your CPL to industry benchmarks (see B2B Lead Quality Analyzer)
- TikTok: Compare your engagement rates to creative center benchmarks


### Share of Voice Estimation

**Estimating Your SOV by Platform:**

| Platform | Your Spend | Est. Market Spend | Est. SOV | Target SOV |
|----------|-----------|-------------------|----------|------------|
| Meta | €XX,XXX | €X,XXX,XXX | X.X% | [Based on SOM target] |
| Google | €XX,XXX | €X,XXX,XXX | X.X% | [Based on SOM target] |
| LinkedIn | €X,XXX | €XXX,XXX | X.X% | [Based on SOM target] |
| TikTok | €X,XXX | €X,XXX,XXX | X.X% | [Based on SOM target] |

**SOV Strategy Guidance:**
- To maintain market share: SOV ≈ Market Share
- To grow market share: SOV should exceed Market Share by 5-15 points
- For each 10 points of Excess SOV, expect ~0.5% market share growth/year

### Competitive Performance Benchmarking

**Your Metrics vs Industry Benchmarks:**

| Metric | Your Performance | Industry Benchmark | Delta |
|--------|-----------------|-------------------|-------|
| Meta CPM | €XX | €5-15 (B2C), €15-40 (B2B) | [+/-XX%] |
| Meta CTR | X.X% | 0.9% (avg) | [+/-XX%] |
| Google CPC | €X.XX | €0.50-3.00 (avg) | [+/-XX%] |
| LinkedIn CPL | €XX | €50-150 (B2B) | [+/-XX%] |
| TikTok CPM | €XX | €8-15 (avg) | [+/-XX%] |

**Competitive Gap Analysis:**
- **Outperforming benchmarks:** [List platforms where you beat industry]
- **Underperforming benchmarks:** [List platforms where improvement needed]
- **Implication:** [What this means for budget allocation]

### Competitive Recommendations

Based on competitive analysis:

1. **[Defensive Action]**
   - If competitors are gaining impression share on brand terms, consider...
   - If SOV is below market share, consider increasing budget by...

2. **[Offensive Opportunity]**
   - Where competitors show weakness (low overlap, poor position)
   - Underserved channels where you can gain SOV efficiently


NEXT STEPS:
-----------
1. [Highest confidence reallocation action]
2. [Second priority action]
3. [Validation/testing recommendation]

4. [Competitive action - based on auction insights/SOV analysis]

```
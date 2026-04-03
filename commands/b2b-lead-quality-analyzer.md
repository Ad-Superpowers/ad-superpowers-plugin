---
description: Analyze lead quality across platforms with LinkedIn-specific benchmarks. Compare CPL by industry, MQL/SQL rates, Lead Gen Forms vs Landing Pages, and LTV:CAC framework for B2B. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# B2B Lead Quality Analyzer

Deep analysis of B2B lead generation with **LinkedIn-specific benchmarks** and quality metrics.

## LinkedIn B2B Benchmarks (Industry-Specific)

### CPL Benchmarks by Industry
| Industry | Poor | Average | Good | Excellent |
|----------|------|---------|------|-----------|
| Finance & Insurance | >€120 | €90-120 | €60-90 | <€60 |
| SaaS / Software | >€120 | €80-120 | €50-80 | <€50 |
| Professional Services | >€100 | €70-100 | €45-70 | <€45 |
| Healthcare | >€150 | €100-150 | €70-100 | <€70 |
| Manufacturing | >€130 | €90-130 | €60-90 | <€60 |
| Education | >€80 | €60-80 | €40-60 | <€40 |
| Marketing / Agencies | >€120 | €80-120 | €50-80 | <€50 |

**CPL Context by Deal Size:**
- Enterprise deals (€50k+ ACV): CPL €150-300+ acceptable
- Mid-market (€10-50k ACV): CPL €80-150 target
- SMB deals (€5k ACV): CPL <€50 target
- Freemium SaaS: CPL <€30 ideal

### Lead Quality Benchmarks (LinkedIn-Specific)
| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| MQL to SQL Rate | <10% | 10-20% | 20-35% | >35% |
| SQL to Opportunity | <20% | 20-35% | 35-50% | >50% |
| Opportunity to Close | <15% | 15-25% | 25-40% | >40% |
| Lead Gen Form SQL Rate | <8% | 8-15% | 15-25% | >25% |
| Landing Page SQL Rate | <15% | 15-30% | 30-45% | >45% |

### Lead Gen Forms vs Landing Pages
| Metric | Lead Gen Forms | Landing Pages |
|--------|----------------|---------------|
| Conversion Rate | 10-13% | 4-6% |
| Cost per Lead | 15-25% lower | Higher |
| SQL Rate (quality) | 20-40% lower | Higher |
| Mobile Experience | Excellent | Variable |

**When to Use:**
- Lead Gen Forms: Volume-focused, TOFU/MOFU content, mobile audience
- Landing Pages: Quality-focused, BOFU demos, complex qualification needed

## Instructions

### 1. Gather Lead Data
**LinkedIn:** Use `linkedin_get_analytics(account_id, start_date, end_date)` for lead metrics
**Google:** Use `google_ads_run_gaql(customer_id, query="SELECT campaign.name, metrics.conversions, metrics.cost_per_conversion FROM campaign WHERE campaign.advertising_channel_type = 'SEARCH' AND segments.date DURING LAST_30_DAYS")` for lead campaigns
**Meta:** Use `meta_get_insights(account_id, fields=["actions"])` for lead events

From CRM/Marketing Automation (if available):
- MQL conversion rates by source
- SQL progression
- Pipeline value attributed

### 2. Calculate Quality Metrics

```python
# Quality-adjusted CPL (the metric that matters)
quality_cpl = total_spend / mql_count  # Cost per MQL, not just CPL

# LinkedIn-specific efficiency
# LinkedIn CPC is 3-5x higher than Meta/Google, but quality compensates
platform_efficiency = sql_rate * (1 / quality_cpl)  # Higher = better

# LTV:CAC Ratio (B2B ROI standard)
ltv = avg_contract_value * customer_lifespan_years * gross_margin
cac = total_spend / customers_acquired
ltv_cac_ratio = ltv / cac
# Target: 3:1 - 5:1 is healthy, >7:1 may indicate underinvestment
```

### 3. Output Format

```
================================================================================
                         B2B LEAD QUALITY ANALYZER
                    Period: Last 30 Days
                    Industry: SaaS / Software
================================================================================

LEAD FUNNEL OVERVIEW:
---------------------
| Stage           | Volume  | Rate      | Benchmark | Status    |
|-----------------|---------|-----------|-----------|-----------|
| Total Leads     | XXX     | -         | -         | -         |
| MQLs            | XX      | XX%       | 31%       | [🟢🟡🔴]   |
| SQLs            | XX      | XX% of MQL| 20-35%    | [🟢🟡🔴]   |
| Opportunities   | XX      | XX% of SQL| 35-50%    | [🟢🟡🔴]   |

B2B SALES CYCLE CONTEXT:
- Avg LinkedIn-sourced cycle: 200+ days
- Multi-touch attribution: 6-12 touches average
- Don't judge CPL without SQL rate data!

LINKEDIN-SPECIFIC METRICS:
--------------------------
| Metric | Your Value | Industry Benchmark | Status |
|--------|------------|-------------------|--------|
| CPL | €XX | €[specify industry_cpl_benchmark] | [🟢🟡🔴] |
| CPC | €XX | €4-7 (B2B avg) | [🟢🟡🔴] |
| CTR | X.XX% | 0.35-0.55% (Sponsored Content) | [🟢🟡🔴] |
| Form CVR | XX% | 6-10% (Lead Gen Forms) | [🟢🟡🔴] |
| SQL Rate | XX% | 10-20% (average) | [🟢🟡🔴] |
| Cost/SQL | €XXX | €[specify industry_cpl_benchmark] / SQL rate | [🟢🟡🔴] |

LEAD GEN FORMS vs LANDING PAGES:
--------------------------------
| Source | Leads | CPL | SQL Rate | Cost/SQL | Recommendation |
|--------|-------|-----|----------|----------|----------------|
| Lead Gen Forms | XX | €XX | XX% | €XXX | [Volume/Quality tradeoff] |
| Landing Pages | XX | €XX | XX% | €XXX | [Volume/Quality tradeoff] |

PLATFORM QUALITY COMPARISON:
----------------------------
| Platform  | Leads | CPL    | SQL Rate | Cost/SQL | Quality Score |
|-----------|-------|--------|----------|----------|---------------|
| LinkedIn  | XX    | €XX.XX | XX%      | €XXX     | [1-10]        |
| Google    | XX    | €XX.XX | XX%      | €XXX     | [1-10]        |
| Meta      | XX    | €XX.XX | XX%      | €XXX     | [1-10]        |

Note: LinkedIn CPC is 3-5x higher than Meta/Google, but B2B audience quality often compensates.

LTV:CAC ANALYSIS:
-----------------
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Avg Contract Value | €XX,XXX | - | - |
| Customer Lifespan | X years | - | - |
| Estimated LTV | €XX,XXX | - | - |
| CAC (from ads) | €X,XXX | - | - |
| LTV:CAC Ratio | X:1 | 3:1 - 5:1 | [🟢🟡🔴] |

Interpretation:
- <1:1 = Loss-making
- 1:1 - 3:1 = Break-even to marginal
- 3:1 - 5:1 = Healthy (target range)
- 5:1 - 7:1 = Excellent
- >7:1 = Potentially under-investing in growth

RECOMMENDATIONS:
----------------
Budget Reallocation:
- LinkedIn: [Increase/Decrease/Maintain] - [Reason based on SQL rate]
- Google: [Increase/Decrease/Maintain] - [Reason]
- Meta: [Increase/Decrease/Maintain] - [Reason]

Quality Improvements:
1. [Add 1-2 qualifying questions to Lead Gen Forms if SQL rate <15%]
2. [Test Landing Pages for BOFU campaigns if quality is priority]
3. [Speed-to-lead: Respond <1hr for 53% conv rate vs 17% at 24hr+]

Lead Gen Form Optimization:
- Current fields: [X]
- Recommendation: [Add/Remove] [Field] to improve SQL rate
- Expected impact: [+X% SQL rate] or [+X% volume]
```
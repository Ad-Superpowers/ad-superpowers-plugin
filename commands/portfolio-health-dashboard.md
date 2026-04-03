---
description: Get a traffic-light overview of all your ad accounts in under 5 minutes. Uses platform-specific thresholds: TikTok (faster fatigue), LinkedIn (B2B CPL benchmarks), Meta/Google (standard metrics).
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** free
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Portfolio Health Dashboard

Generate a comprehensive health check for all connected ad accounts for the last 7 days.

## Instructions

### 1. Gather Account Data Per Platform

**Tool Usage:**
- Meta: `meta_get_insights(account_id, date_preset="[specify period]", level="account")`
- Google Ads: `google_ads_run_gaql(customer_id, query="SELECT campaign.name, metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions FROM campaign WHERE segments.date DURING LAST_30_DAYS ORDER BY metrics.cost_micros DESC")`
- TikTok: `tiktok_get_report(start_date, end_date, level="campaign")`
- LinkedIn: `linkedin_get_analytics(account_id, start_date, end_date)`

Retrieve for each:
- Account-level spend and budget data
- Primary KPIs (ROAS for e-commerce, CPA/CPL for lead gen)
- Week-over-week or period-over-period changes

### 2. Apply Platform-Specific Traffic Light Status

**IMPORTANT:** Different platforms have different healthy thresholds!

#### Universal Thresholds (All Platforms)
| Metric | Green | Amber | Red |
|--------|-------|-------|-----|
| Daily spend vs. budget | 90-110% | 80-90% or 110-120% | <80% or >120% |
| Monthly pacing | Within 5% of ideal | 5-15% deviation | >15% deviation |
| CPA vs. target | Within 10% | +10-25% | +25%+ |
| ROAS vs. target | At or above target | -10-20% | -20%+ |

#### Meta Ads Specific
| Metric | Green | Amber | Red |
|--------|-------|-------|-----|
| CTR (Feed) | >1.5% | 1.0-1.5% | <1.0% |
| Frequency (Prospecting) | <3/week | 3-4/week | >4/week |
| Frequency (Retargeting) | <5/week | 5-6/week | >6/week |
| Creative age | <10 days | 10-14 days | >14 days |
| CPM vs 7-day avg | Within 15% | 15-25% deviation | >25% deviation |

#### Google Ads Specific
| Metric | Green | Amber | Red |
|--------|-------|-------|-----|
| CTR (Search) | >3% | 2-3% | <2% |
| CTR (Display) | >0.5% | 0.3-0.5% | <0.3% |
| Quality Score (avg) | >7 | 5-7 | <5 |
| Impression Share | >70% | 50-70% | <50% |
| IS Lost (Budget) | <10% | 10-20% | >20% |

#### TikTok Ads Specific (4x Faster Fatigue!)
| Metric | Green | Amber | Red |
|--------|-------|-------|-----|
| CTR | >1.5% | 1.0-1.5% | <1.0% |
| 2-Second View Rate | >50% | 30-50% | <30% |
| Frequency (Prospecting) | <4/week | 4-5/week | >5/week |
| Creative age | <5 days | 5-7 days | >7 days |
| CPM vs baseline | Within 20% | 20-40% increase | >40% increase |

#### LinkedIn Ads Specific (B2B Benchmarks)
| Metric | Green | Amber | Red |
|--------|-------|-------|-----|
| CTR (Sponsored Content) | >0.55% | 0.35-0.55% | <0.35% |
| CPL (SaaS) | <€80 | €80-120 | >€120 |
| CPL (Finance) | <€90 | €90-120 | >€120 |
| CPL (Professional Services) | <€70 | €70-100 | >€100 |
| Lead Gen Form CVR | >10% | 6-10% | <6% |
| Frequency | <4/week | 4-6/week | >6/week |
| Creative age | <30 days | 30-45 days | >45 days |

#### Critical Alerts (Immediate Action Required)
| Alert | Threshold | Platform |
|-------|-----------|----------|
| Conversion tracking down | 0 conversions in 24+ hours | All |
| Mass ad disapprovals | >10% of active ads | All |
| Impression share loss (budget) | >20% sustained | Google |
| Spend velocity anomaly | 200%+ of normal rate | All |
| TikTok creative cliff | CTR drop >25% in 3 days | TikTok |
| LinkedIn CPL spike | >50% above industry benchmark | LinkedIn |

### 3. Output Format

```
================================================================================
                         PORTFOLIO HEALTH CHECK
                    Period: Last 7 Days vs Previous Period
================================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 TL;DR (Executive Summary)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1-2 sentence plain English summary. Example:]
"Your ads are mostly on track. One account needs attention: [Account] on TikTok
has declining performance that's costing you ~€XX/day in wasted spend."

or if all healthy:
"All accounts are performing well this week. You can focus on growth, not fixes."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 #1 PRIORITY - If You Do ONE Thing This Week:
───────────────────────────────────────────────
[Single most impactful action in plain language. Example:]
"Refresh your TikTok creatives in [Account Name].
Your current ads are tired (they've been running 12 days - TikTok ads need
refreshing every 5-7 days). This is likely costing you €50-100/day extra."

If all healthy: "No urgent actions needed. Consider testing new creatives."
───────────────────────────────────────────────

QUICK OVERVIEW: X accounts | Y healthy | Z need attention | W urgent

| Platform | Status | Quick Take |
|----------|--------|------------|
| Meta     | 🟢/🟡/🔴 | [Plain language: "Running smoothly" / "Watch your costs" / "Needs work"] |
| Google   | 🟢/🟡/🔴 | [Plain language description] |
| TikTok   | 🟢/🟡/🔴 | [Plain language description] |
| LinkedIn | 🟢/🟡/🔴 | [Plain language description] |

DETAILED ACCOUNT STATUS:
--------------------------------------------------------------------------------
| Account          | Platform | Budget Used | Results vs Goal | Health |
--------------------------------------------------------------------------------
| [Account Name]   | Meta     | €XX/€XX     | [Above/On/Below] target | 🟢🟡🔴 |
| [Account Name]   | TikTok   | €XX/€XX     | [Above/On/Below] target | 🟢🟡🔴 |
| [Account Name]   | LinkedIn | €XX/€XX     | [Above/On/Below] target | 🟢🟡🔴 |
| [Account Name]   | Google   | €XX/€XX     | [Above/On/Below] target | 🟢🟡🔴 |
--------------------------------------------------------------------------------

⚠️ WHAT TO KNOW (Plain Language Alerts):
-----------------------------------------
TIKTOK: Your TikTok ads are getting stale. People have seen them too many times.
  → What this means: You're paying more for fewer clicks.
  → Fix: Upload 3-5 new videos/images this week.

LINKEDIN: Your cost per lead is high compared to other [industry] companies.
  → What this means: You might be targeting too narrowly.
  → Fix: Try broader job titles or company sizes.

GOOGLE: You're missing out on customers because your budget runs out.
  → What this means: ~XX% of potential customers can't see your ads.
  → Fix: Increase daily budget or focus on best-performing campaigns.

META: People are seeing your ads too often (frequency is high).
  → What this means: Ad fatigue is starting - effectiveness dropping.
  → Fix: Add new creative variations or expand your audience.

🔴 URGENT - Fix This Week:
--------------------------
* [Account] on TikTok: Ads are underperforming
  - Problem: Your click rate dropped 28% in 3 days (ads are stale)
  - Impact: ~€XX/day in wasted spend
  - Fix: Upload 3+ new creatives today

* [Account] on LinkedIn: Leads are too expensive
  - Problem: Paying €XX per lead (industry average is €XX)
  - Impact: ~€XX/month over budget
  - Fix: Test Lead Gen Forms instead of website forms

🟡 KEEP AN EYE ON:
------------------
* [Account] on Meta: Getting close to ad fatigue
  - Current: People see your ads 3.2x/week (limit is 4x)
  - Action: Prepare new creatives just in case

🟢 ALL GOOD:
------------
* X accounts running smoothly
* [Brief note on what's working well]
```

### 4. Prioritization
List issues by:
1. Platform urgency (TikTok issues first - faster fatigue)
2. Spend impact (highest spend accounts)
3. Severity (Red before Amber)
4. Actionability (quick fixes first)
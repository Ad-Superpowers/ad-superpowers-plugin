---
description: Quick weekly summary with platform-specific insights. Includes TL;DR, top wins, concerns, and platform-appropriate benchmarks (TikTok creative health, LinkedIn CPL vs industry, etc.).
---

> **Platforms:** meta, google_ads, linkedin, tiktok
> **Tier:** free
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Weekly Performance Pulse

Generate a quick weekly performance summary for all connected accounts.

## Instructions

### 1. Gather This Week's Data (Platform-Specific Tool Calls)

**Meta Ads:**
```
meta_get_insights(
    account_id=account_id,
    date_preset="last_7d",
    level="account",
    fields=["spend", "impressions", "clicks", "actions", "action_values", "cpm", "cpc", "ctr", "purchase_roas"]
)
```

**Google Ads:**
```
google_ads_run_gaql(
    customer_id=customer_id,
    date_range="LAST_7_DAYS"
)
```

**TikTok Ads:**
```
tiktok_get_report(
    start_date="7 days ago",
    end_date="today",
    level="campaign",
    metrics=["spend", "impressions", "clicks", "conversions", "cpc", "cpm", "ctr", "conversion_rate"]
)
```

**LinkedIn Ads:**
```
linkedin_get_analytics(
    account_id=account_id,
    start_date="7 days ago",
    end_date="today",
    time_granularity="ALL",
    fields=["impressions", "clicks", "costInLocalCurrency", "externalWebsiteConversions"]
)
```

### 2. Compare to Previous Week
Calculate week-over-week changes for all metrics.

### 3. Platform-Specific Quick Health Checks

Include in analysis:

**TikTok (check first - fastest fatigue):**
- Creative age: Any ads >5 days? Flag for refresh
- CTR trend over 3 days: Declining >15%? Fatigue signal
- Hook performance: 2-second view rate (target >50%)

**Meta:**
- Frequency: Prospecting >3/week? Monitor closely
- Creative age: Any ads >14 days? Plan refresh

**LinkedIn (B2B context):**
- CPL vs industry benchmark (SaaS: €80-120, Finance: €90-120)
- Long sales cycles - don't judge too quickly

**Google Ads:**
- Quality Score changes
- Impression share trends

### 4. Output Format

```
================================================================================
📊 Weekly Performance Pulse - Your Ad Portfolio
   Week of [Date Range]
================================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 TL;DR (Copy-Paste Ready for Slack/Email)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1-2 sentence plain English summary - max 280 characters]
Example: "Good week: +15% more sales from ads. One thing to fix: TikTok ads are
getting stale (refresh needed). LinkedIn leads cost €X - that's healthy."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 IF YOU DO ONE THING THIS WEEK:
─────────────────────────────────
[Single most impactful action in plain language]
Example: "Refresh your TikTok creatives - they're 8 days old (TikTok ads work
best when refreshed every 5-7 days). This could save you €XX-XX/week."

If all good: "No urgent actions. Consider testing new ad creative."
─────────────────────────────────

📈 THE NUMBERS (Plain English)
──────────────────────────────
Spent this week: €X,XXX (vs €X,XXX last week = [up/down] X%)
Results: XXX conversions ([up/down] X% vs last week)
Cost per result: €XX ([better/worse] than last week's €XX)
Return on ad spend: €X.XX back for every €1 spent ([up/down])

PLATFORM QUICK VIEW:
| Platform  | Spent   | Results | How It's Going    | vs Last Week |
|-----------|---------|---------|-------------------|--------------|
| Meta      | €X,XXX  | XXX     | [Great/OK/Needs work] | +/-XX%   |
| Google    | €X,XXX  | XXX     | [Great/OK/Needs work] | +/-XX%   |
| TikTok    | €X,XXX  | XXX     | [Great/OK/Needs work] | +/-XX%   |
| LinkedIn  | €X,XXX  | XX      | [Great/OK/Needs work] | +/-XX%   |

⚠️ THINGS TO KNOW THIS WEEK:
────────────────────────────
[Only show if relevant - plain language explanations]

TIKTOK: Your ads are [X] days old. On TikTok, ads get stale fast (5-7 days).
  → Impact: You're probably paying more than needed for each result.
  → Fix: Upload 3-5 new video/image ads this week.

LINKEDIN: Your cost per lead (€XX) compares to the [industry] average of €XX.
  → What this means: [Good - you're efficient] / [High - room to improve]
  → If high: Try Lead Gen Forms instead of sending people to your website.

META: People are seeing your ads [X] times per week.
  → Impact: Above [3] means they might be ignoring them (ad fatigue).
  → Fix: Add new creative variations or show to new audiences.

GOOGLE: You're reaching [X]% of people searching for your keywords.
  → What this means: [Great] / [You're missing [100-X]% of potential customers]
  → If low: Consider increasing budget on best-performing campaigns.

🎉 THIS WEEK'S WINS (What Went Well):
─────────────────────────────────────
1. [Specific win with numbers, plain language]
   Example: "Meta ads: 20% more sales than last week - new creative is working!"
2. [Specific win]
3. [Specific win]

⚠️ THINGS TO IMPROVE:
────────────────────
1. [Platform]: [Plain language issue] - Fix: [specific action]
2. [Platform]: [Plain language issue] - Fix: [specific action]
3. [Platform]: [Plain language issue] - Fix: [specific action]

📋 THIS WEEK'S TO-DO LIST:
─────────────────────────
Priority order (do first one first!):
□ [Most important action - usually TikTok if ads are old]
□ [Second action]
□ [Third action]
□ [Nice to have if time allows]

─────────────────────────────────────────────────────────────────────────────
📧 SHARE THIS SUMMARY
For Slack/Teams: Copy the TL;DR section above
For email: Copy the whole "THE NUMBERS" section
─────────────────────────────────────────────────────────────────────────────
```

### 5. Highlight Significant Changes
- Flag any metric change >10% with clear indicator
- Platform-specific context (TikTok changes matter more - faster fatigue)
- Keep recommendations actionable and specific
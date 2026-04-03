---
description: Analyze Google Ads auction insights to understand competitive landscape. See who you're competing against and where you're winning or losing. (requires Pro subscription)
---

> **Platforms:** google_ads
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Competitive Auction Insights

Analyze competitive landscape using Google Ads auction insights.

## Instructions

### 1. Gather Auction Data
From Google Ads, retrieve auction insights for:
- Top campaigns by spend
- Brand campaigns
- Top converting campaigns

Key metrics:
- Impression share
- Overlap rate
- Position above rate
- Top of page rate
- Outranking share

### 2. Analyze Competitive Position

```
Competitive Strength Score =
  (Impression Share * 0.3) +
  (Top of Page Rate * 0.3) +
  (Outranking Share * 0.4)
```

### 3. Output Format

```
================================================================================
                         COMPETITIVE AUCTION INSIGHTS
                    Account: [Name] | Period: Last 30 Days
================================================================================

YOUR COMPETITIVE POSITION:
--------------------------
| Metric                | Your Score | Industry Avg | Status    |
|-----------------------|------------|--------------|-----------|
| Search Impression Share | XX%       | XX%          | Good/Poor |
| Top of Page Rate      | XX%        | XX%          | Good/Poor |
| Absolute Top Rate     | XX%        | XX%          | Good/Poor |
| Outranking Share (avg)| XX%        | -            | -         |

TOP COMPETITORS:
----------------
| Competitor            | Overlap | Position Above | Outranking | Threat Level |
|-----------------------|---------|----------------|------------|--------------|
| [Competitor 1]        | XX%     | XX%            | XX%        | High         |
| [Competitor 2]        | XX%     | XX%            | XX%        | Medium       |
| [Competitor 3]        | XX%     | XX%            | XX%        | Low          |

COMPETITOR DEEP DIVE:
---------------------
[Top Competitor Name]:
- Overlaps with you XX% of the time
- Appears above you XX% of the time
- You outrank them XX% of the time
- Trend: [Getting more/less aggressive]
- Strategy insight: [Based on their behavior]

CAMPAIGN-LEVEL COMPETITIVE ANALYSIS:
------------------------------------
Brand Campaigns:
- Your impression share: XX%
- Top competitor: [Name] at XX%
- Risk: [Assessment]

Non-Brand Campaigns:
- Your impression share: XX%
- Losing to: [Competitors taking share]
- Opportunity: [Where to gain ground]

RECOMMENDATIONS:
----------------
Defensive Priorities:
1. [Protect brand terms from [competitor]]
2. [Improve position on [high-value keywords]]

Offensive Opportunities:
1. [Competitor weakness to exploit]
2. [Market gap identified]

Budget Implications:
- To gain 10% more impression share: Estimated +€X,XXX/month
- To match top competitor's share: Estimated +€X,XXX/month
```
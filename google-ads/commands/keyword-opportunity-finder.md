---
description: Discover new keyword opportunities in Google Ads. Analyze search terms, find gaps, and get bid recommendations. (requires Pro subscription)
---

> **Platforms:** google_ads
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Keyword Opportunity Finder

Discover keyword opportunities in Google Ads campaigns.

## Instructions

### 1. Analyze Current Keywords
Pull keyword performance data:
- Active keywords with metrics
- Quality scores
- Impression share data
- Search term reports

### 2. Identify Opportunities

**High-Value Opportunities:**
- Search terms with conversions not yet added as keywords
- Keywords with high impression share loss (budget)
- Low QS keywords with good conversion rates (improve landing page)
- Competitor terms worth bidding on

**Negative Keyword Opportunities:**
- Irrelevant search terms wasting budget
- High-spend, zero-conversion terms
- Brand misspellings to exclude

### 3. Output Format

```
================================================================================
                         KEYWORD OPPORTUNITY FINDER
                    Account: [Name] | Period: Last 30 Days
================================================================================

SEARCH TERM GOLD MINES:
-----------------------
These search terms converted but aren't keywords yet:

| Search Term              | Clicks | Conv | Conv Rate | Cost  | Recommended Match |
|--------------------------|--------|------|-----------|-------|-------------------|
| [converting search term] | XX     | X    | X.X%      | €XXX  | Exact/Phrase      |

Potential impact: +XX conversions/month if added

IMPRESSION SHARE OPPORTUNITIES:
-------------------------------
Keywords losing impression share to budget:

| Keyword                  | IS Lost (Budget) | Avg CPC | Conv | Recommendation      |
|--------------------------|------------------|---------|------|---------------------|
| [high-value keyword]     | XX%              | €X.XX   | XX   | Increase bid/budget |

Estimated opportunity: €X,XXX additional revenue if captured

QUALITY SCORE IMPROVEMENTS:
---------------------------
Keywords with low QS but good conversion rates:

| Keyword                  | QS  | Conv Rate | Issue           | Fix                 |
|--------------------------|-----|-----------|-----------------|---------------------|
| [low QS keyword]         | 4   | 5.2%      | Landing page    | [specific fix]      |

Estimated CPC savings: XX% if QS improved to 7+

NEGATIVE KEYWORD RECOMMENDATIONS:
---------------------------------
Irrelevant search terms to exclude:

| Search Term              | Clicks | Spend | Conv | Action          |
|--------------------------|--------|-------|------|-----------------|
| [irrelevant term]        | XX     | €XXX  | 0    | Add as negative |

Estimated monthly savings: €XXX

NEW KEYWORD IDEAS:
------------------
Based on top performers and search trends:

| Keyword Idea             | Est. Volume | Est. CPC | Competition | Relevance |
|--------------------------|-------------|----------|-------------|-----------|
| [new keyword]            | X,XXX       | €X.XX    | Med         | High      |

ACTION SUMMARY:
---------------
1. Add [X] converting search terms as keywords
2. Exclude [X] irrelevant terms
3. Increase budget/bids for [X] high-opportunity keywords
4. Improve landing pages for [X] low-QS keywords
```
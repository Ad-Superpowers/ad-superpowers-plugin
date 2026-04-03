---
description: Comprehensive client research combining deep research with optional ad account analysis. Gathers company intel, competitive landscape, and advertising history in one structured workflow. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Client Discovery & Intelligence Gathering

Conduct comprehensive client research to build a complete profile for [specify company_name].

## Overview

This workflow combines external research with optional ad platform data to create a structured Client Profile Report. Works with or without connected ad accounts.

## Parameters
- Company: [specify company_name]
- Website: Not provided
- Industry: To be determined
- Research Depth: standard

---

## PHASE 1: Company Intelligence Research

### Research Prompts

Use these prompts to gather company intelligence. If you have access to web search tools (Exa, native search), execute them directly. Otherwise, provide these as structured research prompts.

**Prompt 1 - Company Overview:**
```
Research [specify company_name]:
- Business model and revenue streams
- Products/services offered
- Target market and customer segments
- Company size (employees, revenue if public)
- Founding date and key milestones
- Leadership team
- Recent news (last 6 months)
- Funding history (if startup/private)
```

**Prompt 2 - Digital Presence Analysis:**
```
Analyze [specify company_name]'s digital presence:
- Website traffic estimates (SimilarWeb, if available)
- Social media presence and follower counts
- Content marketing strategy
- SEO visibility and top keywords
- Tech stack (BuiltWith, Wappalyzer insights)
- Customer reviews and sentiment
```

**Prompt 3 - Competitive Landscape:**
```
Identify [specify company_name]'s competitive landscape:
- Top 3-5 direct competitors
- Market positioning vs competitors
- Unique value proposition
- Pricing strategy comparison
- Competitive advantages and weaknesses
```


### Website Analysis

If crawling tools are available, analyze: [specify company_website]

Extract:
- Value proposition (homepage hero section)
- Products/services structure
- Target audience signals (language, imagery)
- Trust signals (testimonials, certifications, press)
- Conversion points (CTAs, forms, pricing)
- Content themes and messaging


---

## PHASE 2: Ad Platform Intelligence (If Connected)

{% if research_depth in ["standard", "comprehensive"] %}
### Check Connected Platforms

For each connected platform, gather historical performance data:

**Meta Ads:**
```
meta_get_insights(
    account_id=account_id,
    date_preset="last_90d",
    level="account",
    fields=["spend", "impressions", "clicks", "actions", "action_values", "purchase_roas"]
)

meta_query(
    account_id=account_id,
    entity_type="campaigns",
    effective_status=["ACTIVE", "PAUSED"]
)
```

**Google Ads:**
```
google_ads_run_gaql(
    customer_id=customer_id,
    date_range="LAST_90_DAYS"
)
```

**LinkedIn Ads:**
```
linkedin_get_analytics(
    account_id=account_id,
    start_date="90 days ago",
    end_date="today",
    time_granularity="MONTHLY"
)
```

**TikTok Ads:**
```
tiktok_get_report(
    start_date="90 days ago",
    end_date="today",
    level="campaign"
)
```

**GA4 (for traffic context):**
```
ga4_get_traffic_sources(
    property_id=property_id,
    start_date="90 days ago",
    end_date="today"
)
```


---

## PHASE 3: Synthesis & Client Profile Report

### Output Format

```
================================================================================
                    CLIENT DISCOVERY REPORT
                    [specify company_name]
                    Generated: [Date]
================================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[2-3 sentence summary of the company, its market position, and key opportunity
areas for advertising. Write as if briefing a new account manager.]

Example: "[specify company_name] is a [business type] targeting [audience]. They have
[strong/moderate/limited] digital presence with [X] monthly visitors. Key
opportunity: [main advertising opportunity based on research]."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 COMPANY SNAPSHOT
────────────────────
| Attribute           | Details                                    |
|---------------------|--------------------------------------------|
| Industry            | [Industry/vertical]                        |
| Business Model      | [B2B/B2C/D2C/Marketplace/SaaS/etc.]       |
| Company Size        | [Employees] employees                      |
| Revenue             | [If public/available]                      |
| Founded             | [Year]                                     |
| Headquarters        | [Location]                                 |
| Website             | [URL]   |

🎯 TARGET MARKET
────────────────
Primary Audience:
- Demographics: [Age, gender, location]
- Psychographics: [Interests, values, lifestyle]
- B2B specifics: [Industry, company size, job titles]

Secondary Audiences:
1. [Audience segment 1]
2. [Audience segment 2]

💰 PRODUCTS & SERVICES
─────────────────────
| Offering           | Price Point    | Target Segment    |
|--------------------|----------------|-------------------|
| [Product 1]        | €/$ XX         | [Segment]         |
| [Product 2]        | €/$ XX         | [Segment]         |
| [Service 1]        | €/$ XX/month   | [Segment]         |

Average Order Value (estimated): €/$ XXX
Customer Lifetime Value (estimated): €/$ X,XXX

⚔️ COMPETITIVE LANDSCAPE
────────────────────────
| Competitor      | Strength              | Weakness              | Ad Activity |
|-----------------|----------------------|----------------------|-------------|
| [Competitor 1]  | [Key strength]       | [Key weakness]       | [High/Med/Low] |
| [Competitor 2]  | [Key strength]       | [Key weakness]       | [High/Med/Low] |
| [Competitor 3]  | [Key strength]       | [Key weakness]       | [High/Med/Low] |

Competitive Position:
[specify company_name] differentiates through [unique value proposition].
Main competitive threats: [key threats]
Opportunity gaps: [underserved areas competitors miss]

🌐 DIGITAL PRESENCE SCORE
─────────────────────────
| Channel          | Presence    | Quality     | Opportunity |
|------------------|-------------|-------------|-------------|
| Website          | [1-10]      | [Notes]     | [High/Med/Low] |
| SEO              | [1-10]      | [Notes]     | [High/Med/Low] |
| Social (Meta)    | [1-10]      | [X followers] | [High/Med/Low] |
| Social (LinkedIn)| [1-10]      | [X followers] | [High/Med/Low] |
| Social (TikTok)  | [1-10]      | [X followers] | [High/Med/Low] |
| Content/Blog     | [1-10]      | [Notes]     | [High/Med/Low] |
| Email Marketing  | [1-10]      | [Notes]     | [High/Med/Low] |

Overall Digital Maturity: [Beginner/Developing/Established/Advanced]

📈 ADVERTISING HISTORY (If Platform Data Available)
────────────────────────────────────────────────────
| Platform     | 90-Day Spend | Key Metrics              | Status    |
|--------------|--------------|--------------------------|-----------|
| Meta Ads     | €XX,XXX      | ROAS: X.X, CPA: €XX     | [Active/Paused] |
| Google Ads   | €XX,XXX      | Conv: XXX, CPA: €XX     | [Active/Paused] |
| LinkedIn     | €X,XXX       | Leads: XX, CPL: €XX     | [Active/Paused] |
| TikTok       | €X,XXX       | ROAS: X.X               | [Active/Paused] |

Historical Performance Summary:
- Best performing platform: [Platform] (why)
- Highest potential platform: [Platform] (why)
- Current strategy: [Describe current approach]

🔑 KEY INSIGHTS & OPPORTUNITIES
────────────────────────────────
1. **[Insight 1 Title]**
   [Detailed observation with data point]
   → Opportunity: [Specific advertising opportunity]

2. **[Insight 2 Title]**
   [Detailed observation with data point]
   → Opportunity: [Specific advertising opportunity]

3. **[Insight 3 Title]**
   [Detailed observation with data point]
   → Opportunity: [Specific advertising opportunity]

⚠️ RISKS & CONSIDERATIONS
─────────────────────────
- [Risk 1]: [Description and mitigation]
- [Risk 2]: [Description and mitigation]
- [Risk 3]: [Description and mitigation]

📋 RECOMMENDED NEXT STEPS
─────────────────────────
1. **Immediate**: [First priority action]
2. **This Week**: [Second priority action]
3. **This Month**: [Longer-term action]

💡 SUGGESTED WORKFLOWS TO RUN NEXT
───────────────────────────────────
Based on this discovery, consider running:
- [ ] Market Sizing (if budget planning needed)
- [ ] Buyer Persona Builder (if audience unclear)
- [ ] Landing Page Analyzer (if conversion focus)
- [ ] Competitive Landscape Analyzer (if competitive intel needed)
```

---

## Research Depth Guidelines

**Quick (5-10 minutes):**
- Basic company overview only
- No competitor analysis
- No platform data
- Use for initial scoping

**Standard (15-30 minutes):**
- Full company research
- Top 3 competitors
- Available platform data
- Use for most new clients

**Comprehensive (45-60 minutes):**
- Deep company analysis
- Full competitive landscape (5+ competitors)
- Historical platform data with trend analysis
- Website audit
- Use for high-value prospects or pitches
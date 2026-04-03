---
description: Generate detailed buyer personas combining research with optional platform audience data. Creates 2-4 actionable personas with platform-specific targeting recommendations. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# AI-Powered Buyer Persona Builder

Generate detailed buyer personas for [specify company_name] in [specify industry].

## Overview

Create {{ num_personas | default(3) }} data-driven buyer personas combining research with optional platform audience insights. Each persona includes demographics, psychographics, pain points, and platform-specific targeting recommendations.

## Parameters
- Company: [specify company_name]
- Industry: [specify industry]
- Product Type: b2c_product
- Number of Personas: {{ num_personas | default(3) }}
- Existing Customer Description: Not provided

- GA4 Property: [specify ga4_property_id]


---

## PHASE 1: Audience Research

### Research Prompts

**Prompt 1 - Industry Buyer Research:**
```
Research typical buyers in [specify industry]:
- Demographics (age, gender, income, education, location)
- Job titles and roles (if B2B)
- Common pain points and challenges
- Buying motivations and triggers
- Decision-making process
- Information sources they trust
- Objections and barriers to purchase
```

**Prompt 2 - Competitor Audience Analysis:**
```
Analyze who competitors in [specify industry] are targeting:
- Target demographics from their advertising
- Messaging themes and appeals
- Audience segments they focus on
- Gaps or underserved segments
```

{% if product_type == "b2b_saas" or product_type == "b2b_services" %}
**Prompt 3 - B2B Buying Committee:**
```
For [specify industry] B2B purchases, identify:
- Decision makers (titles, responsibilities)
- Influencers in the buying process
- End users vs buyers
- Budget holders
- Typical buying committee size
- Sales cycle length
```


---

## PHASE 2: Platform Data Enrichment (If Connected)


### GA4 Audience Insights
```
ga4_run_report(
    property_id="[specify ga4_property_id]",
    start_date="90 days ago",
    end_date="today",
    metrics=["activeUsers", "sessions", "conversions"],
    dimensions=["userAgeBracket", "userGender", "country", "deviceCategory"]
)

ga4_get_traffic_sources(
    property_id="[specify ga4_property_id]",
    start_date="90 days ago",
    end_date="today"
)
```


### Meta Audience Insights (If Connected)
```
meta_get_insights(
    account_id=account_id,
    date_preset="last_90d",
    level="account",
    breakdowns=["age", "gender", "country"]
)
```

### LinkedIn Demographics (If Connected)
```
linkedin_get_analytics with demographic breakdowns for:
- Job function
- Seniority
- Industry
- Company size
```

---

## PHASE 3: Persona Generation

### Persona Framework

For each persona, develop:

1. **Identity**
   - Name (realistic, memorable)
   - Photo description (for visualization)
   - One-line summary

2. **Demographics**
   - Age range
   - Gender
   - Location
   - Income/budget level
   - Education
   - Family status (B2C) / Job title (B2B)

3. **Psychographics**
   - Values and beliefs
   - Lifestyle
   - Personality traits
   - Interests and hobbies

4. **Goals & Pain Points**
   - Primary goals
   - Key challenges
   - Frustrations
   - Desired outcomes

5. **Buying Behavior**
   - Decision drivers
   - Information sources
   - Objections
   - Buying triggers

6. **Platform Behavior**
   - Preferred social platforms
   - Content consumption habits
   - Device preferences
   - Best times to reach

7. **Targeting Recommendations**
   - Meta targeting parameters
   - Google Ads audiences
   - LinkedIn targeting (if B2B)
   - TikTok targeting (if relevant)

---

## Output Format

```
================================================================================
                    BUYER PERSONA REPORT
                    [specify company_name] | [specify industry]
================================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Based on research and {{ "platform data" if ga4_property_id else "industry analysis" }},
we've identified {{ num_personas | default(3) }} key buyer personas for [specify company_name].
Primary persona: [Name] ([X]% of ideal customers)
Secondary personas: [Names]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 PERSONA OVERVIEW
────────────────────

| Persona | Segment | Est. % of Market | Priority | Best Platform |
|---------|---------|------------------|----------|---------------|
| [Name 1] | [Segment] | [XX]% | Primary | [Platform] |
| [Name 2] | [Segment] | [XX]% | Secondary | [Platform] |
| [Name 3] | [Segment] | [XX]% | Tertiary | [Platform] |

================================================================================
                    PERSONA 1: [PERSONA NAME]
                    "[One-line description/quote]"
================================================================================

🎭 IDENTITY
───────────
**Name:** [Realistic first name]
**Archetype:** [e.g., "The Busy Professional", "The Value Seeker"]
**Summary:** [One sentence describing this persona]

📋 DEMOGRAPHICS
───────────────
| Attribute | Details |
|-----------|---------|
| Age | [XX-XX years] |
| Gender | [Distribution or primary] |
| Location | [Geographic focus] |
| Income | EUR [XX,XXX - XX,XXX] |
| Education | [Level] |
| {% if product_type in ["b2b_saas", "b2b_services"] %}Job Title | [Title]Family Status | [Status] |
| {% if product_type in ["b2b_saas", "b2b_services"] %}Company Size | [Size range]Living Situation | [Details] |

🧠 PSYCHOGRAPHICS
─────────────────
**Values:**
- [Value 1]
- [Value 2]
- [Value 3]

**Personality:**
- [Trait 1]
- [Trait 2]

**Interests & Hobbies:**
- [Interest 1]
- [Interest 2]
- [Interest 3]

**Media Consumption:**
- Platforms: [Primary platforms]
- Content types: [Preferred content]
- Influencers/brands they follow: [Examples]

🎯 GOALS & PAIN POINTS
──────────────────────

**Primary Goals:**
1. [Goal 1 - specific and actionable]
2. [Goal 2]
3. [Goal 3]

**Key Pain Points:**
1. 😤 [Pain point 1 - emotional language]
   *"[Quote that represents this frustration]"*
2. 😤 [Pain point 2]
3. 😤 [Pain point 3]

**Desired Outcomes:**
- [What success looks like for them]
- [How they measure success]

💳 BUYING BEHAVIOR
──────────────────

**Decision Drivers (Ranked):**
1. [Primary driver - e.g., price, quality, convenience]
2. [Secondary driver]
3. [Tertiary driver]

**Information Sources:**
- Discovery: [How they find products]
- Research: [Where they validate]
- Trust signals: [What builds confidence]

**Common Objections:**
- "[Objection 1]" → Counter: [How to address]
- "[Objection 2]" → Counter: [How to address]

**Buying Triggers:**
- [Trigger 1 - e.g., seasonal, life event, pain threshold]
- [Trigger 2]

**Budget & Timing:**
- Budget range: EUR [XX - XX]
- Decision timeline: [X days/weeks]
- Purchase frequency: [One-time/Recurring]

📱 PLATFORM BEHAVIOR
────────────────────

| Platform | Usage | Best Content | Best Time |
|----------|-------|--------------|-----------|
| Facebook | [High/Med/Low] | [Type] | [Time] |
| Instagram | [High/Med/Low] | [Type] | [Time] |
| LinkedIn | [High/Med/Low] | [Type] | [Time] |
| TikTok | [High/Med/Low] | [Type] | [Time] |
| Google | [Search behavior] | [Keywords] | [Intent] |
| YouTube | [High/Med/Low] | [Type] | [Time] |

**Device Preferences:**
- Primary: [Mobile/Desktop]
- Shopping behavior: [Device patterns]

🎯 TARGETING RECOMMENDATIONS
────────────────────────────

### Meta Ads (Facebook/Instagram)

**Demographics:**
- Age: [XX-XX]
- Gender: [Selection]
- Locations: [Specific locations]

**Detailed Targeting:**
- Interests: [Interest 1], [Interest 2], [Interest 3]
- Behaviors: [Behavior 1], [Behavior 2]
- Life events: [If relevant]

**Custom Audiences:**
- Website visitors: [Specific pages]
- Engagement: [Video viewers, page engagers]
- Lookalike: Based on [source]

**Placements:**
- Recommended: [Feed, Stories, Reels]
- Avoid: [If any]

### Google Ads

**Search Campaigns:**
- High-intent keywords: [Keyword 1], [Keyword 2]
- Informational keywords: [Keyword 1], [Keyword 2]
- Negative keywords: [Exclusions]

**Audience Segments:**
- In-market: [Relevant segments]
- Affinity: [Relevant segments]
- Custom intent: [Keywords/URLs]

**Display/YouTube:**
- Topics: [Relevant topics]
- Placements: [Specific sites/channels]

{% if product_type in ["b2b_saas", "b2b_services"] %}
### LinkedIn Ads

**Job Targeting:**
- Job titles: [Title 1], [Title 2], [Title 3]
- Job functions: [Function 1], [Function 2]
- Seniority: [Level]

**Company Targeting:**
- Industries: [Industry 1], [Industry 2]
- Company size: [Range]
- Company growth: [If relevant]

**Skills & Interests:**
- Skills: [Skill 1], [Skill 2]
- Groups: [Relevant groups]


### TikTok Ads

**Targeting:**
- Age: [XX-XX]
- Interests: [Category 1], [Category 2]
- Behaviors: [Behavior 1]

**Content Strategy:**
- Hook style: [What grabs their attention]
- Content themes: [What resonates]
- Creator style: [UGC/Polished/Educational]

📝 MESSAGING GUIDELINES
───────────────────────

**Value Proposition for This Persona:**
"[Tailored value prop that speaks to their specific pain points]"

**Key Messages:**
1. [Message addressing primary pain point]
2. [Message addressing goal]
3. [Message addressing objection]

**Tone of Voice:**
- [Descriptor 1] - [Example phrase]
- [Descriptor 2] - [Example phrase]

**Words/Phrases That Resonate:**
✅ [Word 1], [Word 2], [Word 3]

**Words/Phrases to Avoid:**
❌ [Word 1], [Word 2]

**Ad Copy Examples:**

*Headline:*
"[Example headline targeting this persona]"

*Primary text:*
"[Example ad copy - 2-3 sentences]"

*CTA:*
[Recommended CTA for this persona]

================================================================================
[REPEAT STRUCTURE FOR PERSONA 2, 3, etc.]
================================================================================

📊 PERSONA COMPARISON MATRIX
────────────────────────────

| Attribute | Persona 1 | Persona 2 | Persona 3 |
|-----------|-----------|-----------|-----------|
| Age | [Range] | [Range] | [Range] |
| Primary Platform | [Platform] | [Platform] | [Platform] |
| Main Pain Point | [Pain] | [Pain] | [Pain] |
| Price Sensitivity | [High/Med/Low] | [H/M/L] | [H/M/L] |
| Decision Speed | [Fast/Medium/Slow] | [F/M/S] | [F/M/S] |
| Best Ad Format | [Format] | [Format] | [Format] |
| Estimated CAC | [specify currency] [XX] | [specify currency] [XX] | [specify currency] [XX] |

🎯 CAMPAIGN STRUCTURE RECOMMENDATIONS
─────────────────────────────────────

**Recommended Campaign Setup:**

1. **Prospecting - Persona 1 (Primary)**
   - Budget allocation: [XX]%
   - Platforms: [Platforms]
   - Objective: [Objective]

2. **Prospecting - Persona 2**
   - Budget allocation: [XX]%
   - Platforms: [Platforms]
   - Objective: [Objective]

3. **Prospecting - Persona 3**
   - Budget allocation: [XX]%
   - Platforms: [Platforms]
   - Objective: [Objective]

**A/B Testing Priority:**
1. [Test messaging for Persona 1 vs 2]
2. [Test creative style for Persona X]
3. [Test platform allocation]

📋 DATA SOURCES & CONFIDENCE
────────────────────────────

| Data Point | Source | Confidence |
|------------|--------|------------|
| Demographics | [Source] | [High/Med/Low] |
| Psychographics | [Source] | [High/Med/Low] |
| Platform behavior | [Source] | [High/Med/Low] |
| Buying behavior | [Source] | [High/Med/Low] |

**Validation Recommendations:**
- [ ] Run creative tests per persona
- [ ] Track conversion rates by targeting
- [ ] Survey customers to validate assumptions
- [ ] Review in 90 days with performance data
```

---

## Product Type Considerations

### B2C Product
- Focus on lifestyle, values, emotional drivers
- Include family/household context
- Emphasize price sensitivity and purchase triggers

### B2B SaaS
- Focus on job responsibilities and KPIs
- Include buying committee dynamics
- Emphasize ROI and business outcomes

### D2C E-commerce
- Focus on shopping behavior and preferences
- Include brand loyalty and switching triggers
- Emphasize convenience and experience

### B2B Services
- Focus on business challenges and expertise needs
- Include trust and credibility factors
- Emphasize relationship and support expectations
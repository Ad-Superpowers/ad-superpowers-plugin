---
description: Comprehensive landing page analysis combining page crawling, GA4 performance data, and CRO best practices. Identifies conversion opportunities and provides actionable recommendations. (requires Pro subscription)
---

> **Platforms:** meta, google_ads, linkedin, tiktok, google_analytics
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# CRO & Landing Page Quality Assessment

Analyze the landing page at [specify landing_page_url] for conversion optimization.

## Overview

This workflow evaluates landing page quality across multiple dimensions: message match, value proposition, trust signals, UX, and technical performance. Combines page analysis with optional GA4 data for data-driven recommendations.

## Parameters
- Landing Page URL: [specify landing_page_url]
- Campaign Objective: [specify campaign_objective]
- Target Audience: Not specified
- Ad Copy: Not provided
- Industry: General

- GA4 Property: [specify ga4_property_id]


---

## PHASE 1: Page Crawl & Analysis

### Page Content Extraction

If crawling tools are available, extract from [specify landing_page_url]:

```
1. Hero Section
   - Headline (H1)
   - Subheadline
   - Hero image/video
   - Primary CTA

2. Value Proposition
   - Key benefits listed
   - Unique selling points
   - Problem/solution framing

3. Trust Signals
   - Customer logos
   - Testimonials/reviews
   - Certifications/badges
   - Press mentions
   - Social proof (user counts, etc.)

4. Content Structure
   - Number of sections
   - Content hierarchy
   - Reading flow

5. Conversion Elements
   - CTA buttons (text, placement, count)
   - Forms (fields, length)
   - Pricing information
   - Risk reducers (guarantees, trials)

6. Technical Elements
   - Meta title and description
   - Mobile responsiveness indicators
   - Page load indicators
   - Tracking pixels detected
```

### Manual Analysis Prompts (If No Crawl Tools)

**Prompt 1 - Page Analysis:**
```
Visit [specify landing_page_url] and analyze:
- What is the main headline?
- What is the primary call-to-action?
- How many form fields are there?
- What trust signals are present?
- Is the page mobile-friendly?
- How clear is the value proposition?
```

---

## PHASE 2: GA4 Performance Data (If Available)


### Landing Page Performance
```
ga4_run_report(
    property_id="[specify ga4_property_id]",
    start_date="30 days ago",
    end_date="today",
    metrics=["sessions", "conversions", "bounceRate", "averageSessionDuration"],
    dimensions=["landingPage"],
    limit=100
)
```

### Traffic Sources to This Page
```
ga4_run_report(
    property_id="[specify ga4_property_id]",
    start_date="30 days ago",
    end_date="today",
    metrics=["sessions", "conversions"],
    dimensions=["sessionSource", "sessionMedium"],
    # Filter for this landing page if possible
)
```

### Device Performance
```
ga4_run_report(
    property_id="[specify ga4_property_id]",
    start_date="30 days ago",
    end_date="today",
    metrics=["sessions", "conversions", "bounceRate"],
    dimensions=["deviceCategory"]
)
```


---

## PHASE 3: CRO Assessment Framework

### Scoring Categories (100 Points Total)

| Category | Weight | Focus Areas |
|----------|--------|-------------|
| Message Match | 20 pts | Ad ↔ page alignment |
| Value Proposition | 20 pts | Clarity, differentiation |
| Trust & Credibility | 15 pts | Social proof, authority |
| CTA Effectiveness | 15 pts | Clarity, placement, urgency |
| Form Optimization | 10 pts | Length, friction |
| Mobile Experience | 10 pts | Responsiveness, UX |
| Technical Performance | 10 pts | Speed, tracking |

### Evaluation Criteria

**Message Match (20 points)**
- Headline matches ad promise: 0-8 pts
- Visual continuity from ad: 0-6 pts
- Offer consistency: 0-6 pts

**Value Proposition (20 points)**
- Clear within 5 seconds: 0-8 pts
- Unique vs competitors: 0-6 pts
- Benefit-focused (not feature-focused): 0-6 pts

**Trust & Credibility (15 points)**
- Customer testimonials: 0-4 pts
- Logos/social proof: 0-4 pts
- Certifications/guarantees: 0-4 pts
- Contact information visible: 0-3 pts

**CTA Effectiveness (15 points)**
- Clear action verb: 0-4 pts
- Visible above fold: 0-4 pts
- Value-focused text (not "Submit"): 0-4 pts
- Contrasting color: 0-3 pts

**Form Optimization (10 points)**
- Appropriate field count: 0-4 pts
- Clear labels: 0-3 pts
- Error handling: 0-3 pts

**Mobile Experience (10 points)**
- Responsive layout: 0-4 pts
- Touch-friendly CTAs: 0-3 pts
- Readable text: 0-3 pts

**Technical Performance (10 points)**
- Load speed: 0-4 pts
- Tracking implementation: 0-3 pts
- No broken elements: 0-3 pts

---

## Output Format

```
================================================================================
                    LANDING PAGE ANALYSIS
                    [specify landing_page_url]
================================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Overall Conversion Score: [XX]/100** [🟢 Good / 🟡 Needs Work / 🔴 Critical Issues]

[2-3 sentence summary of the page's conversion potential and main opportunities]

**Top 3 Issues to Fix:**
1. 🔴 [Critical issue] - Est. impact: +[X]% conversion rate
2. 🟡 [Important issue] - Est. impact: +[X]% conversion rate
3. 🟡 [Secondary issue] - Est. impact: +[X]% conversion rate

**Quick Wins (< 1 hour to fix):**
- [Quick win 1]
- [Quick win 2]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 CONVERSION SCORECARD
───────────────────────

| Category | Score | Status | Priority Fix |
|----------|-------|--------|--------------|
| Message Match | [XX]/20 | 🟢🟡🔴 | [Yes/No] |
| Value Proposition | [XX]/20 | 🟢🟡🔴 | [Yes/No] |
| Trust & Credibility | [XX]/15 | 🟢🟡🔴 | [Yes/No] |
| CTA Effectiveness | [XX]/15 | 🟢🟡🔴 | [Yes/No] |
| Form Optimization | [XX]/10 | 🟢🟡🔴 | [Yes/No] |
| Mobile Experience | [XX]/10 | 🟢🟡🔴 | [Yes/No] |
| Technical Performance | [XX]/10 | 🟢🟡🔴 | [Yes/No] |
| **TOTAL** | **[XX]/100** | | |

Score interpretation:
- 80-100: Excellent - minor optimizations only
- 60-79: Good - some improvements needed
- 40-59: Needs work - significant issues
- Below 40: Critical - major overhaul needed


🎯 MESSAGE MATCH ANALYSIS
─────────────────────────

**Ad Copy Provided:**
"[specify ad_copy]"

**Landing Page Headline:**
"[Extracted headline]"

**Match Assessment:**

| Element | Ad | Landing Page | Match? |
|---------|----|--------------| -------|
| Main promise | [Ad promise] | [Page promise] | ✅/❌ |
| Key benefit | [Ad benefit] | [Page benefit] | ✅/❌ |
| Tone/voice | [Ad tone] | [Page tone] | ✅/❌ |
| Visual style | [If known] | [Page style] | ✅/❌ |
| Offer | [Ad offer] | [Page offer] | ✅/❌ |

**Message Match Score: [X]/20**

Issues found:
- [Issue 1 - e.g., "Headline doesn't match ad promise"]
- [Issue 2]

Recommendations:
- [Recommendation 1]
- [Recommendation 2]


💎 VALUE PROPOSITION ASSESSMENT
───────────────────────────────

**Current Value Proposition:**
"[Extracted or summarized value prop]"

**5-Second Test:** [Pass/Fail]
Can a visitor understand what you offer and why it matters within 5 seconds?

**Value Proposition Checklist:**

| Element | Present? | Quality | Notes |
|---------|----------|---------|-------|
| What you offer | ✅/❌ | [1-5] | [Notes] |
| Who it's for | ✅/❌ | [1-5] | [Notes] |
| Key benefit | ✅/❌ | [1-5] | [Notes] |
| Differentiation | ✅/❌ | [1-5] | [Notes] |
| Proof/credibility | ✅/❌ | [1-5] | [Notes] |

**Value Proposition Score: [X]/20**

**Recommended Value Proposition Format:**
```
For [target audience] who [have this problem],
[Product] is a [category] that [key benefit].
Unlike [competitors], we [unique differentiator].
```

**Suggested Rewrite:**
"[Improved value proposition based on analysis]"

🤝 TRUST & CREDIBILITY AUDIT
────────────────────────────

**Trust Signals Found:**

| Signal Type | Present? | Details | Impact |
|-------------|----------|---------|--------|
| Customer testimonials | ✅/❌ | [Count, quality] | High |
| Customer logos | ✅/❌ | [Count, recognizable?] | High |
| Review ratings | ✅/❌ | [Platform, score] | High |
| Case studies | ✅/❌ | [Count] | Medium |
| Certifications | ✅/❌ | [Which ones] | Medium |
| Press/media mentions | ✅/❌ | [Sources] | Medium |
| Money-back guarantee | ✅/❌ | [Terms] | High |
| Security badges | ✅/❌ | [Which ones] | Medium |
| Contact information | ✅/❌ | [Phone/email/address] | Medium |
| Privacy policy | ✅/❌ | [Linked?] | Low |

**Trust Score: [X]/15**

**Missing High-Impact Trust Elements:**
1. [Missing element 1] - Add this for +[X]% trust
2. [Missing element 2]

**Recommendations:**
- [Specific trust element to add]
- [Where to place it]

🔘 CTA ANALYSIS
───────────────

**Primary CTA:**
- Text: "[CTA text]"
- Location: [Above/below fold]
- Color: [Color] - [Contrasts/doesn't contrast]
- Size: [Appropriate/too small/too large]

**CTA Checklist:**

| Element | Current | Best Practice | Fix? |
|---------|---------|--------------|------|
| Action verb | [Yes/No] | Clear action verb | [Y/N] |
| Benefit-focused | [Yes/No] | Value, not "Submit" | [Y/N] |
| Above fold | [Yes/No] | Visible without scroll | [Y/N] |
| Contrasting color | [Yes/No] | Stands out from page | [Y/N] |
| Appropriate size | [Yes/No] | Large enough to notice | [Y/N] |
| Repeated | [Yes/No] | Multiple on long pages | [Y/N] |
| Urgency/scarcity | [Yes/No] | Optional but effective | [Y/N] |

**CTA Score: [X]/15**

**Better CTA Options for [specify campaign_objective]:**

| Current | Suggested Alternative | Why Better |
|---------|----------------------|------------|
| "[Current CTA]" | "[Option 1]" | [Reason] |
| | "[Option 2]" | [Reason] |
| | "[Option 3]" | [Reason] |

📝 FORM ANALYSIS
────────────────

**Form Details:**
- Number of fields: [X]
- Required fields: [X]
- Form location: [Above/below fold]
- Submit button text: "[Text]"

**Field-by-Field Assessment:**

| Field | Necessary? | Friction Level | Recommendation |
|-------|------------|----------------|----------------|
| [Field 1] | ✅/❌ | Low/Med/High | [Keep/Remove/Move] |
| [Field 2] | ✅/❌ | Low/Med/High | [Keep/Remove/Move] |
| [Field 3] | ✅/❌ | Low/Med/High | [Keep/Remove/Move] |

**Form Score: [X]/10**

**Benchmark: Form Fields by Objective**

| Objective | Optimal Fields | Your Fields | Status |
|-----------|---------------|-------------|--------|
| [specify campaign_objective] | [X] | [Y] | [Over/Under/Good] |

**Lead Gen:** 3-5 fields (name, email, phone, company, role)
**Purchase:** Minimal (checkout optimized)
**Signup:** 2-3 fields (email, password, name)
**Download:** 2-3 fields (email, name, company)

**Form Optimization Recommendations:**
1. [Recommendation 1]
2. [Recommendation 2]

📱 MOBILE EXPERIENCE
────────────────────

**Mobile Assessment:**

| Element | Status | Notes |
|---------|--------|-------|
| Responsive layout | ✅/❌ | [Notes] |
| Touch-friendly buttons | ✅/❌ | [Min 44x44px] |
| Readable text | ✅/❌ | [Min 16px] |
| No horizontal scroll | ✅/❌ | [Notes] |
| Form usability | ✅/❌ | [Notes] |
| Image optimization | ✅/❌ | [Notes] |
| CTA visibility | ✅/❌ | [Notes] |

**Mobile Score: [X]/10**


**GA4 Mobile vs Desktop:**

| Device | Sessions | Conversion Rate | Bounce Rate |
|--------|----------|-----------------|-------------|
| Desktop | [X] | [X]% | [X]% |
| Mobile | [X] | [X]% | [X]% |
| Tablet | [X] | [X]% | [X]% |

**Mobile Gap Analysis:**
[If mobile conversion < desktop, explain why and what to fix]


⚡ TECHNICAL PERFORMANCE
────────────────────────

**Performance Indicators:**

| Metric | Status | Target | Notes |
|--------|--------|--------|-------|
| Page load (est.) | [Fast/Slow] | <3 seconds | [Notes] |
| Meta pixel | ✅/❌ | Required | [Detected?] |
| Google tag | ✅/❌ | Required | [Detected?] |
| LinkedIn Insight | ✅/❌ | If using LinkedIn | [Detected?] |
| TikTok pixel | ✅/❌ | If using TikTok | [Detected?] |
| SSL certificate | ✅/❌ | Required | [https?] |

**Technical Score: [X]/10**


📈 GA4 PERFORMANCE DATA
───────────────────────

**Landing Page Performance (Last 30 Days):**

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Sessions | [X] | - | - |
| Conversion Rate | [X]% | [specify industry]: [X]% | 🟢🟡🔴 |
| Bounce Rate | [X]% | <40% ideal | 🟢🟡🔴 |
| Avg. Session Duration | [X]s | >60s ideal | 🟢🟡🔴 |
| Pages/Session | [X] | - | - |

**Traffic Source Performance:**

| Source | Sessions | Conv. Rate | Notes |
|--------|----------|------------|-------|
| [Source 1] | [X] | [X]% | [Best/Worst] |
| [Source 2] | [X] | [X]% | |
| [Source 3] | [X] | [X]% | |

**Key Insight:** [Observation about which traffic converts best/worst and why]


📋 PRIORITIZED RECOMMENDATIONS
──────────────────────────────

### 🔴 Critical (Fix This Week)

**1. [Issue Title]**
- Problem: [Specific problem]
- Impact: Estimated +[X-X]% conversion rate improvement
- Effort: [Low/Medium/High]
- How to fix: [Step-by-step instructions]

**2. [Issue Title]**
- Problem: [Specific problem]
- Impact: Estimated +[X-X]% conversion rate improvement
- Effort: [Low/Medium/High]
- How to fix: [Step-by-step instructions]

### 🟡 Important (Fix This Month)

**3. [Issue Title]**
- Problem: [Specific problem]
- Impact: Estimated +[X-X]% conversion rate improvement
- Effort: [Low/Medium/High]
- How to fix: [Step-by-step instructions]

**4. [Issue Title]**
- Problem: [Specific problem]
- Impact: Estimated +[X-X]% conversion rate improvement

### 🟢 Nice to Have (Backlog)

**5. [Enhancement]**
- Benefit: [Expected benefit]
- Effort: [Low/Medium/High]

**6. [Enhancement]**
- Benefit: [Expected benefit]

📊 A/B TEST SUGGESTIONS
───────────────────────

Based on this analysis, prioritized tests to run:

| Test | Hypothesis | Priority | Expected Lift |
|------|------------|----------|---------------|
| [Test 1] | If we [change], then [outcome] because [reason] | High | +[X]% |
| [Test 2] | If we [change], then [outcome] because [reason] | Medium | +[X]% |
| [Test 3] | If we [change], then [outcome] because [reason] | Medium | +[X]% |

📈 PROJECTED IMPACT
───────────────────

If all critical recommendations are implemented:

| Metric | Current | Projected | Improvement |
|--------|---------|-----------|-------------|
| Conversion Rate | [X]% | [X]% | +[X]% |
| Cost per Conversion | €[X] | €[X] | -[X]% |
| Monthly Conversions* | [X] | [X] | +[X] |

*Based on current traffic levels

**ROI of Optimization:**
At current ad spend of €[X]/month, a [X]% conversion improvement =
€[X] additional revenue / [X] additional leads per month
```

---

## Industry Benchmarks

### Landing Page Conversion Rates by Objective

| Objective | Poor | Average | Good | Excellent |
|-----------|------|---------|------|-----------|
| Lead Gen (B2B) | <2% | 2-5% | 5-10% | >10% |
| Lead Gen (B2C) | <3% | 3-8% | 8-15% | >15% |
| E-commerce | <1% | 1-3% | 3-5% | >5% |
| SaaS Signup | <2% | 2-5% | 5-10% | >10% |
| App Download | <5% | 5-15% | 15-25% | >25% |

### Bounce Rate Benchmarks

| Page Type | Poor | Average | Good |
|-----------|------|---------|------|
| Landing Page | >70% | 40-70% | <40% |
| Homepage | >60% | 40-60% | <40% |
| Blog Post | >80% | 60-80% | <60% |
---
name: linkedin-performance-troubleshooter
description: "This skill should be used when the user asks to \"fix LinkedIn ad performance\", \"diagnose high LinkedIn CPL\", \"fix LinkedIn ads not spending\", or mentions \"LinkedIn low engagement\", \"LinkedIn performance drop\", or \"reduce LinkedIn ad costs\". Do NOT use for: LinkedIn bid strategy selection (use linkedin-bid-strategy-selector), LinkedIn lead gen form optimization (use linkedin-lead-gen-optimizer), or LinkedIn benchmark lookups (use linkedin-benchmark-database)."
---
# LinkedIn Ads Performance Troubleshooter

## Purpose

Diagnose and fix common LinkedIn Ads performance problems. LinkedIn has the highest CPC ($3-8+) and CPL ($60-150) of any major ad platform, requiring specialized troubleshooting because generic advice doesn't work for LinkedIn's unique auction dynamics and B2B audience.

## When to Use This Skill

Invoke when user mentions:
- **High costs:** "Why is my LinkedIn CPL so high?"
- **Delivery issues:** "My LinkedIn ads aren't spending/delivering"
- **Low engagement:** "Engagement is low despite high impressions"
- **Cost reduction:** "How do I reduce my LinkedIn ad costs?"
- **Performance drops:** "Why did my LinkedIn performance suddenly drop?"

## Quick Diagnostic Framework

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LINKEDIN ADS TROUBLESHOOTING                              │
│                         START HERE                                           │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                    What's the main problem?
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
    HIGH CPL                  LOW DELIVERY               LOW ENGAGEMENT
    (Cost per lead           (Spending <50%             (CTR <0.4%)
    above benchmark)          of budget)                      │
        │                           │                           │
        ▼                           ▼                           ▼
   Go to SECTION A           Go to SECTION B           Go to SECTION C
```

## Section A: High CPL Troubleshooting

### Diagnostic Checklist

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HIGH CPL DIAGNOSIS                                        │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                    Check 1: AUDIENCE SIZE
                                    │
            ┌───────────────────────┴───────────────────────────┐
            │                                                   │
            ▼                                                   ▼
    AUDIENCE < 50,000                                  AUDIENCE > 50,000
    ─────────────────                                  ─────────────────
            │                                                   │
            ▼                                                   ▼
    Too narrow!                                        Check 2: BID STRATEGY
    Action: Remove 1-2 filters                                  │
    Impact: -20-40% CPL typically               ┌───────────────┴───────────────┐
                                                │                               │
                                                ▼                               ▼
                                        MANUAL BIDDING               AUTOMATED BIDDING
                                                │                               │
                                                ▼                               ▼
                                        Likely too low                Check 3: FORM vs LP
                                        Action: Switch to                       │
                                        automated or increase cap       ┌───────┴───────┐
                                                                        ▼               ▼
                                                                    USING FORMS    USING LP
                                                                        │               │
                                                                        ▼               ▼
                                                                Check 4: CREATIVE   Higher CPL
                                                                FATIGUE            expected
                                                                (CTR declining?)   (better quality)
```

### High CPL Solutions

| Check | Issue | Action | Expected Impact |
|-------|-------|--------|-----------------|
| Audience size | <50,000 members | Broaden targeting - remove 1-2 filters | -20-40% CPL |
| Bid strategy | Manual bidding too low | Switch to automated or increase cap | -10-25% CPL |
| Forms vs LP | Using landing pages | Test Lead Gen Forms for volume | -30-50% CPL (but lower quality) |
| Creative fatigue | CTR declining over 2+ weeks | Rotate creatives | -10-20% CPL |

## Section B: Low Delivery Troubleshooting

Start with Step 1 under MCP Tool Usage: read serving_diagnosis before applying
the audience, budget, bid and overlap checks below.

### Diagnostic Checklist

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LOW DELIVERY DIAGNOSIS                                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                    Check 1: AUDIENCE SIZE
                                    │
            ┌───────────────────────┴───────────────────────────┐
            │                                                   │
            ▼                                                   ▼
    AUDIENCE < 300,000                                 AUDIENCE > 300,000
    (planning guideline, not a minimum)                            │
            │                                                   │
            ▼                                                   ▼
    Check actual audience count.                             Check 2: BUDGET
    Action: Use Message Ads                                    │
    for <50K audiences, or                    ┌───────────────┴───────────────┐
    expand targeting                          │                               │
                                              ▼                               ▼
                                      BUDGET < $50/day              BUDGET > $50/day
                                              │                               │
                                              ▼                               ▼
                                      May be too low                Check 3: BID CAPS
                                      Action: Increase to                      │
                                      $100+/day for                    ┌───────┴───────┐
                                      consistent delivery              │               │
                                                                       ▼               ▼
                                                               BID CAP SET      NO BID CAP
                                                                       │               │
                                                                       ▼               ▼
                                                               Likely below    Check 4: TARGETING
                                                               competitive     OVERLAP
                                                               threshold              │
                                                               Action: Remove          ▼
                                                               cap or +20-30%   Overlapping
                                                                               audiences?
                                                                               Action:
                                                                               Consolidate or
                                                                               use exclusions
```

### Low Delivery Solutions

| Check | Issue | Action | Notes |
|-------|-------|--------|-------|
| Audience size | Low estimated audience | Check audience_count before proposing broader targeting | Rounded count; zero may mean fewer than 300 members |
| Budget | <$50/day | Increase to $100+/day for consistent delivery | $25 minimum, $100 recommended |
| Bid caps | Below competitive threshold | Remove cap or increase by 20-30% | Benchmark CPC: $5-8 for most B2B |
| Targeting overlap | Overlapping audiences competing | Consolidate or use exclusions | Prevents self-competition |

## Section C: Low Engagement Troubleshooting

### Diagnostic Checklist

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LOW ENGAGEMENT DIAGNOSIS                                  │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                    Check 1: CREATIVE RELEVANCE
                                    │
            ┌───────────────────────┴───────────────────────────┐
            │                                                   │
            ▼                                                   ▼
    GENERIC MESSAGING                                  PERSONALIZED MESSAGING
    ─────────────────                                  ───────────────────────
            │                                                   │
            ▼                                                   ▼
    Low relevance to audience                         Check 2: AD FORMAT
    Action: Personalize to job                                 │
    function/industry                         ┌───────────────┴───────────────┐
    Impact: +50-100% CTR                      │               │               │
                                              ▼               ▼               ▼
                                          SINGLE          VIDEO          NEW IMAGE
                                          IMAGE              │               │
                                              │               ▼               │
                                              │    Good engagement,          │
                                              │    lower CTR                 │
                                              │               │               │
                                              ▼               ▼               ▼
                                        Check 3: CTA ALIGNMENT
                                                              │
                                              ┌───────────────┴───────────────┐
                                              │                               │
                                              ▼                               ▼
                                        CTA MATCHES                    CTA MISMATCH
                                        FUNNEL STAGE                   ───────────
                                              │                               │
                                              ▼                               ▼
                                        Check 4:                       Fix CTA:
                                        MOBILE EXPERIENCE              Top-funnel: Learn More
                                                                       Bottom-funnel: Request Demo
```

### Low Engagement Solutions

| Check | Issue | Action | Expected Impact |
|-------|-------|--------|-----------------|
| Creative relevance | Generic messaging | Personalize to job function/industry | +50-100% CTR |
| Ad format | Not testing video | Test video (higher engagement, lower CTR) | +20-30% engagement |
| CTA alignment | CTA doesn't match funnel stage | Top: Learn More, Download; Bottom: Request Demo | +10-20% CTR |
| Mobile experience | Poor mobile LP | Optimize LP for mobile (50%+ traffic) | +15-25% CVR |

## Red Flag Thresholds

### CPL Thresholds

| Status | Threshold |
|--------|-----------|
| Good | At or below industry benchmark |
| Warning | >1.5x industry benchmark |
| Critical | >2x industry benchmark |

### CTR Thresholds

| Status | CTR |
|--------|-----|
| Good | >0.50% |
| Warning | 0.40-0.50% |
| Critical | <0.40% |
| Severe | <0.25% |

### Delivery Thresholds

| Status | % of Budget Spent |
|--------|-------------------|
| Good | >80% |
| Warning | 50-80% |
| Critical | <50% |

### Frequency Thresholds

Use these only with advertiser-supplied frequency from Campaign Manager. The
creative analytics tools do not provide frequency.

| Status | Frequency/Week |
|--------|----------------|
| Good | <3x |
| Warning | 3-5x |
| Critical | >5x |

### Conversion Rate Thresholds

| Status | Form Completion Rate |
|--------|---------------------|
| Excellent | >60% |
| Good | 40-60% |
| Warning | 30-40% |
| Critical | <30% |

## Quick Wins Checklist

### Immediate Actions (Do Today)

- [ ] Switch to automated bidding (if using manual)
- [ ] Expand audience by removing 1 targeting criteria
- [ ] Add video creative to ad mix
- [ ] Check mobile landing page speed (<3 seconds)

### This Week

- [ ] A/B test headline variations
- [ ] Plan a warm-audience test in Campaign Manager; segment creation is unavailable here
- [ ] Review form field count (optimal: 5-7)
- [ ] Analyze best performing demographics

### Next Sprint

- [ ] Implement lead scoring
- [ ] Set up conversion tracking refinement
- [ ] Build the company list in Campaign Manager, then read matched audience readiness
- [ ] Create funnel-stage segmented campaigns

## Industry Benchmarks

### CPC by Industry

| Industry | CPC Range |
|----------|-----------|
| Finance | $3-5 |
| SaaS | $6-8+ |
| Healthcare | $4-6 |
| Education | $3-4 |
| Marketing | $5-7 |

### CPM Range

$30-50 across most B2B industries

### CTR by Format

| Format | Average CTR |
|--------|-------------|
| Sponsored Content | 0.50-0.60% |
| Video | 0.40% |
| Message Ads (InMail) | 3%+ |

### Form Completion Rate

| Rating | Rate |
|--------|------|
| Good | 40-60% |
| Excellent | >60% |

## New Format Opportunities for Performance Recovery

Test a new single-image or video variant against the current creative. Match the
offer and CTA to the audience before restructuring campaigns. Carousel ads (2-10 image cards in a CAROUSEL campaign) and, where the server has document ads enabled, document ads (a PDF uploaded with `linkedin_upload`, in a BRAND_AWARENESS or ENGAGEMENT campaign with format SPONSORED_UPDATE_NATIVE_DOCUMENT) can be created as a DRAFT through `linkedin_manage(action="create_inline")`.

## Predictive Audiences for CPL Improvement

If high CPL persists after audience broadening, test **Predictive Audiences** in Campaign Manager:

- **Requirement:** 300+ conversions or contacts as seed audience
- **Expected impact:** ~21% lower CPL vs standard interest/attribute targeting
- **Setup:** Campaign Manager → Audiences → Predictive → Upload seed or use conversion event
- **Note:** Needs Matched Audiences enabled (Company/Contact list upload or Insight Tag)

## MCP Tool Usage

Use these steps with the cost, delivery and engagement frameworks above. Replace
placeholders with the selected account, campaign and inclusive reporting dates.
Benchmark ranges are planning context, not automatic reasons to change campaigns.

### Step 1: Delivery holds before bids

**Data you need:** Account and campaign IDs, raw serving statuses, creative review
status, diagnosis codes and their levels.

```python
linkedin_query(account_id="<account_id>", entity_type="serving_diagnosis",
               campaign_id="<campaign_id>")
linkedin_query(account_id="<account_id>", entity_type="campaigns",
               entity_id="<campaign_id>", format="full")
```

Start here whenever delivery is low. Follow each returned reason and remedy before
changing bids or targeting. Narrow to a campaign if the summary is truncated.
A future start date calls for waiting; a stopped parent calls for a status review.
A creative under review cannot be paused: LinkedIn returns 400 until its review is
APPROVED. Activate only when ready to serve and the advertiser approves launch.

### Step 2: Audience and campaign settings

**Data you need:** The campaign's complete targetingCriteria, budget, currency,
bid settings and schedule. Assign the returned targetingCriteria to `criteria`.

```python
linkedin_query(account_id="<account_id>", entity_type="audience_count",
               targeting_criteria=criteria)
```

Audience count is a rounded estimate, not reach. Zero can mean fewer than 300
members. The planning audience sizes above are not platform minimums. Use the bid
strategy skill for bid_suggestions and supply_forecast after holds are understood.

### Step 3: Cost and engagement breakdowns

**Data you need:** Equal current and previous date windows, impressions, clicks,
spend, native form leads and website conversions for the affected campaign.

```python
linkedin_get_analytics(
    account_id="<account_id>", level="campaign", entity_id="<campaign_id>",
    start_date="<start_date>", end_date="<end_date>", time_granularity="ALL",
    pivots=["CAMPAIGN", "CREATIVE"],
    fields=["impressions", "clicks", "costInLocalCurrency", "oneClickLeads",
            "externalWebsiteConversions", "totalEngagements"])
linkedin_get_analytics(
    account_id="<account_id>", level="campaign", entity_id="<campaign_id>",
    start_date="<start_date>", end_date="<end_date>", time_granularity="ALL",
    pivot="MEMBER_JOB_FUNCTION", fields=["impressions", "clicks", "costInLocalCurrency"])
```

Repeat for the preceding equal window. Calculate rates from summed counts;
keep missing values unknown. Demographics are approximate and delayed. Use one
`pivot` for demographics or `pivots` for statistics, never both. Report native
form CPL separately from website conversion cost.

### Step 4: Inspect the ad and assess fatigue

**Data you need:** Creative URN, desktop/mobile presentation, two comparable
periods and the creative's impression counts in each.

```python
linkedin_query(account_id="<account_id>", entity_type="ad_preview",
               entity_id="urn:li:sponsoredCreative:<creative_id>")
linkedin_get_creatives_with_images(
    account_id="<account_id>", campaign_id="<campaign_id>",
    start_date="<start_date>", end_date="<end_date>",
    compare_previous_period=True, include_images=True, limit=20)
```

Check both desktop and mobile previews; preview links expire after about three
hours. In our testing, LinkedIn's preview returned UNSUPPORTED_CREATIVE_TYPE for a lead gen creative, and LinkedIn documents no preview for lead gen.
If ad_preview fails for one, use a preview in Campaign Manager. A preview does not establish approval or delivery.
Fatigue requires a relative CTR drop of at least 25%, at least 1,000 impressions
in each period, and no account-wide CTR drop of at least 25%. It is a heuristic.
If comparison periods are not exact, or previous data is unavailable, report the
comparison as inconclusive. This tool does not measure frequency.

## Platform-Specific Troubleshooting

### Common LinkedIn Issues

| Problem | Check | Solution |
|---------|-------|----------|
| High CPL | Audience size | Broaden targeting, test automated bidding |
| Low engagement | Creative relevance | Test video, improve personalization |
| Delivery issues | serving_diagnosis | Resolve the returned hold before evaluating bids |
| Form completion low | Read lead_forms | Test field changes in Campaign Manager |
| Sudden performance drop | Period comparison and fatigue | Separate creative decline from account-wide change |

### LinkedIn-Specific Optimization Levers

Audience creation and edits to published forms below require Campaign Manager. These are
strategy options, not additional Ad Superpowers write capabilities.

| Lever | When to Use | Impact |
|-------|-------------|--------|
| Audience Expansion | When delivery is limited | +20-50% reach, monitor quality |
| Enhanced Bidding | After manual testing phase | More efficient spend |
| Website Retargeting | Always for bottom-funnel | +30-50% CVR |
| Matched Audiences | When you have CRM data | +40-60% CTR |

## Output Template

When troubleshooting LinkedIn performance, provide:

```
## LinkedIn Performance Diagnosis

### Problem Type: [High CPL / Low Delivery / Low Engagement / Multiple]

### Severity: [Warning / Critical]

### Root Cause Hypothesis
Based on the data, the most likely cause is: [specific cause]

### Metrics vs Benchmarks

| Metric | Current | Benchmark | Status |
|--------|---------|-----------|--------|
| CPL | $X | $Y | [status] |
| CTR | X% | 0.50% | [status] |
| Delivery | X% | 80%+ | [status] |
| Frequency | X/week | <3/week | [status] |

### Recommendations

**Immediate Fixes (Do Now):**
1. [Action 1 with expected impact]
2. [Action 2 with expected impact]

**Testing Suggestions:**
1. [Test recommendation]
2. [Test recommendation]

**Budget Optimization:**
- [Recommendation based on analysis]

### Timeline for Results
- Quick wins: [1-2 weeks]
- Full optimization: [4-6 weeks]
```

## Emergency Response: Performance Crashed

### Step 1: Check External Factors

**Data you need:** serving_diagnosis from MCP Step 1 and account notices in Campaign Manager.

- [ ] LinkedIn platform outage? (check status.linkedin.com)
- [ ] Tracking broken? (verify LinkedIn Insight Tag)
- [ ] Payment issue? (check billing)

### Step 2: Check for Changes

**Data you need:** The campaign read from MCP Step 1 and advertiser change history; the read is a current snapshot, not an edit log.

- [ ] Did anyone edit the campaign?
- [ ] Did a scheduled change take effect?
- [ ] Did bid strategy switch?

### Step 3: Compare to Previous Period

**Data you need:** The two analytics windows and fatigue comparison from MCP Steps 3 and 4.

- [ ] Is this across all campaigns or just one?
- [ ] All audiences or specific segments?
- [ ] Gradual decline or sudden drop?

### Step 4: Don't Panic-Edit

**Data you need:** Confirmed holds, reporting completeness and the advertiser's approved remedy.

- Wait 24-48 hours before major changes
- Verify data is correct before reacting
- Document what you observe

---

*Based on 2025-2026 LinkedIn Ads research. LinkedIn is the highest-cost ad platform - specialized troubleshooting is essential for ROI.*

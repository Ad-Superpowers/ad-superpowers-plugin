---
name: linkedin-lead-gen-optimizer
description: "This skill should be used when the user asks to \"optimize LinkedIn Lead Gen Forms\", \"compare Lead Gen Forms vs landing pages\", \"improve LinkedIn lead quality\", \"reduce LinkedIn CPL\", or mentions \"LinkedIn form conversion rate\" or \"B2B lead quality tradeoff\". Do NOT use for: LinkedIn bid strategy questions (use linkedin-bid-strategy-selector), LinkedIn benchmark lookups (use linkedin-benchmark-database), or LinkedIn learning phase questions (use linkedin-learning-phase-tracker)."
---
# LinkedIn Lead Gen Form Optimizer

## Purpose

Help B2B advertisers optimize the quality vs quantity tradeoff on LinkedIn. Lead Gen Forms have 13% CVR vs 4% for landing pages, but SQL rates are 20-40% lower. This skill helps determine when to use forms vs landing pages and how to improve lead quality.

## The Core Tradeoff

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LINKEDIN LEAD GEN: QUALITY vs QUANTITY                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  LEAD GEN FORMS                          LANDING PAGES                       │
│  ──────────────                          ─────────────                       │
│                                                                              │
│  CVR: ~13% average                       CVR: ~4-6% average                  │
│  SQL Rate: 20-40% LOWER                  SQL Rate: HIGHER                    │
│  CPL: Lower (more volume)                CPL: Higher (better quality)        │
│                                                                              │
│  Best for:                               Best for:                           │
│  ├─ Volume over quality                  ├─ Quality over volume              │
│  ├─ Mobile-heavy audience (60%+)         ├─ Complex qualification needed     │
│  ├─ Top-of-funnel (ebooks, whitepapers)  ├─ Product demos, trials            │
│  ├─ Quick campaign launch                ├─ Desktop-heavy audience           │
│  └─ Limited LP resources                 └─ A/B testing capability           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## When to Use This Skill

Invoke when user mentions:
- **Strategy questions:** "Should I use Lead Gen Forms or landing pages?"
- **Quality concerns:** "How do I improve lead quality from LinkedIn forms?"
- **Benchmarking:** "What's a good CPL for my industry?"
- **Cost reduction:** "How do I reduce CPL without hurting quality?"
- **Switching:** "When should I switch from forms to landing pages?"

## Decision Framework: Forms vs Landing Pages

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LEAD GEN FORMS vs LANDING PAGES                           │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    What's your primary goal?
                                    │
            ┌───────────────────────┼───────────────────────────┐
            │                       │                           │
            ▼                       ▼                           ▼
       VOLUME                  BALANCED                    QUALITY
   (MQLs, awareness)       (MQLs that convert)        (SQLs, pipeline)
            │                       │                           │
            ▼                       ▼                           ▼
    USE LEAD GEN FORMS       HYBRID STRATEGY            USE LANDING PAGES
    + qualifying questions                              or Forms + heavy
                                    │                   qualification
                                    ▼
                    ┌───────────────────────────────────┐
                    │        HYBRID STRATEGY            │
                    ├───────────────────────────────────┤
                    │ 1. Capture leads via forms        │
                    │ 2. Create retargeting audience    │
                    │ 3. Serve LP ads to warm audience  │
                    │ 4. Measure SQL rate from each     │
                    └───────────────────────────────────┘
```

### Lead Gen Forms Better When:

| Scenario | Why |
|----------|-----|
| Volume is priority (early funnel) | Higher CVR (13% vs 4%) |
| Mobile-heavy audience (60%+ mobile) | Auto-fill works great on mobile |
| Top-of-funnel content (ebooks, whitepapers) | Low commitment ask |
| Average CPL target > €100 | More cost-efficient for volume |
| Quick campaign launch needed | No LP development required |
| Limited landing page resources | Built-in form functionality |

### Landing Pages Better When:

| Scenario | Why |
|----------|-----|
| Lead quality is critical (sales-ready) | Higher SQL rates |
| Complex qualification needed | Can have more fields/questions |
| Product demos or trials (high-intent) | Better for bottom-funnel |
| Desktop-heavy audience | Better form experience |
| Detailed tracking needed | Full analytics capability |
| A/B testing capability required | More flexibility |

## Quality Improvement Tactics

Read lead_forms first. Ad Superpowers can create a DRAFT form and edit it while it is
DRAFT; changes to a published form and warm-audience setup happen in Campaign Manager.
No retargeting segment tool is available.

### 1. Add Qualifying Questions

**Impact:** +40% SQL rate, +5-15% CPL

Add custom questions that filter out low-intent leads:

| Question | Purpose |
|----------|---------|
| "Budget range" | Filters by ability to pay |
| "Timeline to purchase" | Filters by urgency |
| "Company size" | Filters by fit |
| "Decision-making role" | Filters by authority |

**Best practice:** 5-7 total fields for optimal completion rate.

### 2. Retarget Warm Audiences

**Impact:** +30-50% SQL rate, same CPL

Audiences to retarget:
- Website visitors (last 30-90 days)
- Page engagers (likes, comments, shares)
- Video viewers (50%+ watched)
- Previous form openers (non-submitters)

### 3. Optimize Form Fields

| Do | Don't |
|----|-------|
| Add custom questions that qualify intent | Keep generic fields that auto-fill incorrectly |
| Limit to 5-7 fields total | Ask for unnecessary info |
| Make key qualifiers required | Make everything required |
| Test different field orders | Set and forget |

## CPL Reduction Tactics

### Audience Optimization

| Tactic | Expected Impact |
|--------|-----------------|
| Broaden targeting tiers (avoid hyper-narrow) | -20-40% CPL |
| Test job function vs job title targeting | Variable |
| Expand to adjacent industries | -10-20% CPL |
| Use LinkedIn Audience Expansion | -15-25% CPL |

### Bidding Strategy

| Tactic | When to Use |
|--------|-------------|
| Switch to automated bidding | When starting or scaling |
| Set realistic CPC caps ($5-8 for most) | After gathering data |
| Test enhanced CPC vs manual | Optimization phase |

### Creative Refresh

| Tactic | Expected Impact |
|--------|-----------------|
| Rotate creatives every 2 weeks | Maintains performance |
| Test video vs image | Video often 20% lower CPM |
| Test a single-image variant for each offer | Compare qualified lead cost |

## Industry Benchmarks

### CPL by Industry

| Industry | Average CPL | Good CPL |
|----------|-------------|----------|
| Finance & Insurance | $90-120 | <$90 |
| Education | $60-70 | <$55 |
| Healthcare | $100-150 | <$95 |
| SaaS/Software | $100+ | <$90 |
| Marketing & Agencies | $100 | <$85 |

### CTR Benchmarks

| Ad Format | Average CTR | Good CTR |
|-----------|-------------|----------|
| Sponsored Content | 0.50-0.60% | >0.65% |
| Video Ads | 0.40% | >0.50% |
| Lead Gen Forms | 0.50% | >0.60% |
| Message Ads (InMail) | 3%+ | >4% |

### Form Completion Rate

| Rating | Completion Rate |
|--------|-----------------|
| Excellent | >60% |
| Good | 40-60% |
| Needs Improvement | <40% |

### CVR Comparison

| Method | Average CVR | SQL Rate |
|--------|-------------|----------|
| Lead Gen Forms | ~13% | 20-40% lower |
| Landing Pages | 4-6% | Baseline |
| Hybrid (Forms + LP retarget) | Combined ~8% | Near LP rates |

## Red Flag Thresholds

| Metric | Warning | Critical |
|--------|---------|----------|
| CPL | >1.5x industry benchmark | >2x industry benchmark |
| Form completion rate | <40% | <30% |
| SQL rate | <20% | <10% |
| CTR | <0.40% | <0.25% |

## A/B Testing Recommendations

### Test 1: Forms vs Landing Pages

Run parallel campaigns:
- Campaign A: Lead Gen Forms
- Campaign B: Landing Page
- Measure: CVR, CPL, and **SQL rate** (critical!)

### Test 2: Form Field Variations

Test form configurations:
- Version A: 4 fields (basic)
- Version B: 6 fields (with qualifiers)
- Version C: 8 fields (heavy qualification)
- Measure: Completion rate AND SQL rate

### Test 3: Qualifying Questions

Test specific qualifiers:
- Control: No custom questions
- Test: With budget/timeline questions
- Measure: SQL rate difference

## Output Template

When optimizing LinkedIn lead gen, provide:

```
## LinkedIn Lead Gen Analysis

### Current Strategy
- Method: [Lead Gen Forms / Landing Pages / Hybrid]
- CPL: $X (vs $Y industry benchmark)
- Form Completion Rate: X%
- Estimated SQL Rate: X%

### Performance vs Benchmarks

| Metric | Current | Benchmark | Status |
|--------|---------|-----------|--------|
| CPL | $X | $Y | [Good/Warning/Critical] |
| CTR | X% | 0.50% | [Good/Warning/Critical] |
| Completion Rate | X% | 50% | [Good/Warning/Critical] |
| SQL Rate | X% | 30%+ | [Good/Warning/Critical] |

### Strategy Recommendation

**Recommended: [Forms / Landing Pages / Hybrid]**

Reason: [Based on goals, audience, and current performance]

### Quality Improvement Actions
1. [Specific action with expected impact]
2. [Specific action with expected impact]
3. [Specific action with expected impact]

### CPL Reduction Tactics
1. [Specific tactic]
2. [Specific tactic]

### A/B Tests to Run
1. [Test recommendation with hypothesis]
2. [Test recommendation with hypothesis]
```

## New Format Opportunities for Lead Gen

Use a single-image or video creative with an attachable published Lead Gen Form.
Test the offer, copy and image while keeping the form stable. Lead gen document ads are not available; lead gen carousels are not available.

## Predictive Audiences for Lead Quality

**Predictive Audiences** are an audience option in Campaign Manager; evaluate them against your existing targeting:

- Require a seed of 300+ contacts or conversion events
- Deliver ~21% lower CPL vs standard targeting (LinkedIn internal data)
- Combine with qualifying questions on forms to maintain SQL rate
- Best seeds: CRM contact upload of closed-won customers, or Insight Tag conversion events

To enable: Campaign Manager → Audiences → Predictive Audiences. Requires Matched Audiences (contact upload or Insight Tag).

## MCP Tool Usage

Ad Superpowers can draft a form with linkedin_manage (object_type="lead_form",
create or update while the form is DRAFT; ask the advertiser for their privacy
policy URL). Publish it in Campaign Manager, then attach it. Ad Superpowers reads
forms and creates supported lead gen creatives; it cannot publish or archive forms,
edit a published form, export submitted leads, or create retargeting segments.
Make changes to published forms and audience setup in Campaign Manager. Obtain lead quality data from the advertiser's CRM.

### Step 1: Inspect the campaign and form

**Data you need:** Campaign ID, form ID, account ownership, form state and review.

```python
linkedin_query(account_id="<account_id>", entity_type="campaigns",
               entity_id="<campaign_id>", format="full")
linkedin_query(account_id="<account_id>", entity_type="lead_forms", start=0, count=100)
linkedin_query(account_id="<account_id>", entity_type="lead_forms",
               entity_id="urn:li:adForm:<form_id>")
```

Paginate form lists using start/count. Do not pass campaign_id or status to
lead_forms. Inspect state, reviewInfo and content; this reads forms, not leads.
For attachment the form must be PUBLISHED, belong to the same account and have
reviewInfo.reviewStatus other than REJECTED or AUTO_REJECTED. Unreadable forms
cannot be used. Publish or correct the form in Campaign Manager first.
The campaign must have objectiveType LEAD_GENERATION and offsiteDeliveryEnabled
must not be true. Inline creation requires type SPONSORED_UPDATES with format
STANDARD_UPDATE for image or SINGLE_VIDEO for video.

### Step 2: Measure volume and form friction

**Data you need:** Inclusive dates, spend, form opens, native form leads and
website conversions, with CRM qualification data kept separate.

```python
linkedin_get_analytics(
    account_id="<account_id>", level="campaign", entity_id="<campaign_id>",
    start_date="<start_date>", end_date="<end_date>", time_granularity="ALL",
    fields=["costInLocalCurrency", "clicks", "impressions",
            "externalWebsiteConversions", "oneClickLeads", "oneClickLeadFormOpens"])
```

Form completion = oneClickLeads / oneClickLeadFormOpens. Native form CPL = spend /
oneClickLeads. Keep missing values and zero denominators unknown. Repeat for an
equal previous window. Use the existing forms-versus-landing-pages framework,
but compare SQL rates using CRM outcomes rather than inferring quality from CPL.

### Step 3: Attach a published form to a draft creative

**Data you need:** Advertiser-approved copy, campaign and form URNs, and an
AVAILABLE image or video owned by the account's organization and associated with
the account. Replace every placeholder before executing this write.

```python
linkedin_manage(
    ad_account_id="<account_id>", object_type="creative", action="create_inline",
    payload={"campaign": "urn:li:sponsoredCampaign:<campaign_id>",
             "name": "<approved_creative_name>", "commentary": "<approved_copy>",
             "content": {"media": {"id": "urn:li:image:<image_id>",
                                    "title": "<approved_media_title>"}},
             "leadgenCallToAction": {"destination": "urn:li:adForm:<form_id>",
                                     "label": "LEARN_MORE"}})
```

Use exactly one click target. Do not combine leadgenCallToAction with
contentLandingPage or contentCallToActionLabel. Do not pass entity_id or
confirm_launch to create_inline, or override author, account, status or distribution
inside the payload. The creative lands DRAFT, but its post is PUBLIC/PUBLISHED
with feedDistribution=NONE. No feed distribution does not mean a private post.
The form is read uncached before submission. Record form_state,
form_review_status and leadgen_call_to_action from the result.

If using an existing staged upload, confirm readiness separately:

```python
linkedin_upload(ad_account_id="<account_id>", stage_id="<stage_id>",
                asset_name="<exact_staged_filename>", action="status")
```

Use the asset only when ready_for_use is true. An accepted upload alone does not
establish readiness. This status call cannot stage, upload or repair a missing asset.
Do not retry an ambiguous create or upload; inspect existing results first.

### Step 4: Review, then activate deliberately

**Data you need:** Full creative URN, current review and serving reasons, form
readiness and explicit advertiser approval to start serving.

```python
linkedin_query(account_id="<account_id>", entity_type="creatives",
               campaign_id="<campaign_id>", format="full")
linkedin_query(account_id="<account_id>", entity_type="serving_diagnosis",
               campaign_id="<campaign_id>", entity_id="urn:li:sponsoredCreative:<creative_id>")
```

Inspect the form and creative in Campaign Manager. In our testing, LinkedIn's preview returned UNSUPPORTED_CREATIVE_TYPE for a lead gen creative, and LinkedIn documents no preview for lead gen.
If ad_preview fails, use Campaign Manager's preview.
A DRAFT without review may report review_pending_activation; DRAFT is not approval.
Activate only when ready to serve and approved by the advertiser:

```python
linkedin_manage(
    ad_account_id="<account_id>", object_type="creative", action="status",
    entity_id="urn:li:sponsoredCreative:<creative_id>", target_status="ACTIVE",
    confirm_launch=True, payload={})
```

Leaving DRAFT for ACTIVE, PAUSED or ARCHIVED freezes the form destination and
rechecks form eligibility. Reactivation rechecks it too; pausing or archiving an
already live creative is not blocked by that form check. A creative under review
cannot be paused: LinkedIn returns 400 until review is APPROVED. Do not activate
a draft merely to test it. Use the creative URN for status, update and delete.
Read serving_diagnosis again after a confirmed status change; success is not proof
of serving. If the parent campaign group is DRAFT, resolve its state before the
campaign can change status.

## Hybrid Strategy Playbook

This framework requires audience setup in Campaign Manager and advertiser-supplied
CRM outcomes. Ad Superpowers does not export leads or create retargeting segments.

### When to Use Hybrid

Use hybrid when:
- Volume and quality are both needed
- Budget allows for two campaign tracks
- Retargeting audiences can be built in Campaign Manager
- Time horizon is 30+ days

### Implementation Steps

1. **Phase 1: Form Capture (Week 1-2)**
   - Run Lead Gen Form campaigns
   - Capture high volume leads
   - Build retargeting audiences in Campaign Manager

2. **Phase 2: Build Audiences in Campaign Manager (Week 2-3)**
   - Form openers (non-submitters)
   - Form submitters (for exclusion or upsell)
   - Website visitors from form traffic

3. **Phase 3: Landing Page Retarget (Week 3+)**
   - Target warm audiences with LP campaigns
   - Higher-intent offer (demo, trial)
   - Measure blended SQL rate

4. **Measurement**
   - Track leads by source (Form vs LP)
   - Measure SQL rate for each path
   - Calculate blended CPL and SQL rate
   - Optimize budget allocation

### Expected Results

| Metric | Forms Only | Hybrid |
|--------|------------|--------|
| CVR | 13% | ~8% blended |
| CPL | Lower | Moderate |
| SQL Rate | 20-40% lower | Near LP levels |
| Total SQLs | Lower | Higher |

---

*Based on 2025-2026 LinkedIn Ads research (LinkedIn Marketing Solutions Blog 2025, B2BHouse 2025 LinkedIn Benchmarks). CPL benchmarks in USD. Lead Gen Forms offer volume; Landing Pages offer quality. Hybrid approach often delivers the best blended results.*

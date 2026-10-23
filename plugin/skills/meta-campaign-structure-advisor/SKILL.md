---
name: meta-campaign-structure-advisor
description: "This skill should be used when the user asks to \"set up campaign structure\", \"audit account structure\", \"organize ad sets\", or mentions \"Meta account structure\", \"creative testing framework\", or \"4-tier funnel\". Do NOT use for: bid strategy selection (use bid-strategy-selector), creative brainstorming (use creative-diversification-generator), full-funnel design across platforms (use full-funnel-designer)."
---
# Meta Ads Campaign Structure Advisor

Framework for setting up and optimizing Meta Ads account structures using the 4-tier funnel methodology. It draws on Meta's Performance 5 practices (simplify accounts, automation, diverse creative, data quality, results validation: "Performance Marketing on Meta", Meta for Business, https://www.facebook.com/business/ads/performance-marketing, undated, checked 2026-10-10). The 4-tier structure and its numbers are our working model, not Meta's.

> **Advantage+ API change (checked 2026-10-10):** Marketing API v24.0 (October 8, 2025) introduced one unified Advantage+ campaign structure. A sales campaign is in the Advantage+ state when its three automation levers (budget, audience, placement) are on; the read-only field `advantage_state_info` shows each lever. Since v24.0 (October 8, 2025), legacy Advantage+ shopping campaigns (created with `smart_promotion_type`) and Advantage+ app campaigns can no longer be created, duplicated or updated in versioned calls; since May 19, 2026 this applies to all API versions (v25.0 changelog). The legacy existing-customer budget cap (`existing_customer_budget_percentage`) is not available for new Advantage+ campaigns. Sources: Marketing API changelog, Version 25.0 and Version 24.0; "Advantage+ Campaigns". In this framework an Advantage+ sales campaign is the SCALE tier. **Threads:** the Threads feed is an ad placement, and campaigns created in Ads Manager are opted in by default ("Extend Meta Campaigns With Ads in Threads", Meta for Business, https://www.facebook.com/business/ads/threads); in API targeting, `threads_stream` needs Instagram `stream` in the same ad set.

## Core Principle

**Diversify concepts, not cosmetic variations.** Meta's guidance ('Demystifying creative diversification', Meta for Business, 16 Dec 2025, https://www.facebook.com/business/news/demystifying-creative-diversification) says ads that look or feel alike are treated as variations of the same creative and share learnings. It recommends ads that are truly different in look, feel, storyline and message, and ads that speak to different audience motivations or use cases. It gives no number. Creative diversification and systematic testing are the levers this framework works on.

**Simplify the structure.** Working rule: prefer a few consolidated campaigns over a fragmented structure (see the 4-tier model below).

## How this maps to our MCP tools today

Before applying the structures below, know what `meta_create` actually does today:

- **Choose the budget mode when you create the campaign.** `meta_create(entity_type="campaign")` takes `budget_mode`: `"CBO"` (the default) needs `daily_budget` or `lifetime_budget` (in cents) on the campaign; `"ABO"` takes no campaign budget, and each ad set then sets its own `daily_budget` or `lifetime_budget`. The TEST tier below uses ABO.
- **Pass `special_ad_categories` on every campaign create.** Meta rejects the call without it ("(#100) The parameter special_ad_categories is required"); pass `[]` when no special ad category applies.
- **Under CBO, ad sets must not carry their own budget** — omit it; they share the campaign budget.
- The funnel below is the strategy; for the click-by-click create sequence (campaign → ad set → ads), `use ad-launch-playbook`.

## 4-Tier Funnel Structure

| Tier | Campaign Type | Budget | Goal |
|------|---------------|--------|------|
| **SCALE** | Advantage+ Sales (ASC) | 60-70% | Scale proven winners |
| **TEST** | Manual Sales (ABO) | 10-20% | Identify new winners |
| **RETARGET** | Manual Sales | 15-25% | Convert warm traffic |
| **RETAIN** | Manual Sales | 5-10% | Maximize customer LTV |

Rules of thumb, not Meta figures: check them against the account's own history. This covers the budget shares and audience windows in this section.

### SCALE Campaign (ASC) - 60-70% budget
- **Targeting:** 100% Broad (Advantage+ Audience)
- **Creatives:** Only validated winners - no new tests here
- **Goal:** Maximum scale with proven performers

### TEST Campaign (Prospecting) - 10-20% budget
- **Broad Pack [date]** - Contains a batch of new creatives for testing
- **Broad Pack [date]** - New batch of creatives (weekly/biweekly)
- **Interest #1 Winners** - Receives graduated winners for interest targeting
- **Interest #2 Winners** - Receives graduated winners for other interests
- **Goal:** Systematically test new creatives and identify winners

### RETARGET Campaign - 15-25% budget
- **14 Day FB/IG Engagers** - Social engagement retargeting
- **30 Day Website Visitors** - Site visitor retargeting
- **90 Day ATC/IC** - Add to Cart / Initiate Checkout retargeting
- **Goal:** Convert warm traffic with high purchase intent

### RETAIN Campaign - 5-10% budget
- **All Time Purchasers** - Upsell/Cross-sell messaging (build it from a customer list: a pixel-based website custom audience only keeps people for a limited retention window, "Website Custom Audiences", Marketing API)
- **180 Day Purchasers** - Replenishment/New Products messaging
- **Goal:** Reactivate existing customers and increase LTV

---

## Creative Flow: How Ads Move Through the System

This is the exact flow of how creatives are tested, evaluated, and graduated.

### Step 1: New Creatives Start in TEST

All new creatives begin in the **TEST campaign**, specifically in a **Broad Pack ad set**:

```
New creative made
         ↓
    TEST Campaign
         ↓
  Broad Pack [date]
    (Ad Set with ABO)
```

**Why Broad Pack?**
- Broad targeting gives the algorithm maximum freedom to find the best audience
- ABO (Ad Set Budget Optimization) gives the Broad Pack ad set its own budget
- Date in name makes tracking creative batches simple

### Step 2: Evaluation Against Winner Criteria

After sufficient spend and time, each creative is evaluated:

```
Creative in Broad Pack
         ↓
  Spend >= minimum threshold?
  (MAX(3x CPA, 3x AOV); see Winner Criteria)
         ↓
    NO → Keep testing OR kill if underperforming
    YES → Evaluate performance
         ↓
  ROAS >= threshold AND conversions >= minimum?
         ↓
    NO → Kill or keep testing
    YES → WINNER! Go to Step 3
```

### Step 3: Winner Graduation (Three Destinations)

**Important:** A winner goes to MULTIPLE destinations simultaneously, not just one.

When a creative reaches winner status, it is copied to:

**Destination A: SCALE Campaign (ASC)**
```
Winner Creative
      ↓
 SCALE Campaign (ASC)
      ↓
 100% Broad Ad Set
 (alongside other winners)
```
- Creative is added to the ASC campaign
- Runs with 100% broad targeting on Advantage Campaign Budget
- Receives the largest share of budget (60-70%)

**Destination B: Interest #1 Winners Ad Set**
```
Winner Creative
      ↓
  TEST Campaign
      ↓
Interest #1 Winners
   (Ad Set)
```
- Same creative, but now with interest targeting
- Tests whether the winner also performs with specific interest audiences
- Provides diversification alongside pure broad scaling

**Destination C: Interest #2 Winners Ad Set**
```
Winner Creative
      ↓
  TEST Campaign
      ↓
Interest #2 Winners
   (Ad Set)
```
- Same creative with different interest targeting
- Multiple interest ad sets possible depending on product/market

### Complete Flow Summary

```
[NEW CREATIVE]
        │
        ▼
┌───────────────────┐
│   TEST Campaign   │
│                   │
│  Broad Pack [date]│ ◄── Starting point for all new creatives
│    (ABO budget)   │
└────────┬──────────┘
         │
         ▼
   [EVALUATION]
   Meets winner criteria?
         │
    ┌────┴────┐
    │         │
   NO        YES
    │         │
    ▼         ▼
  [KILL]   [WINNER]
    or        │
 [KEEP       │
 TESTING]    ├──────────────────────────────────────┐
             │                                      │
             ▼                                      ▼
┌────────────────────────┐          ┌───────────────────────────┐
│    SCALE Campaign      │          │      TEST Campaign        │
│         (ASC)          │          │                           │
│                        │          │  ┌─────────────────────┐  │
│  ┌──────────────────┐  │          │  │ Interest #1 Winners │  │
│  │   100% Broad     │  │          │  └─────────────────────┘  │
│  │   (all winners)  │  │          │  ┌─────────────────────┐  │
│  └──────────────────┘  │          │  │ Interest #2 Winners │  │
│                        │          │  └─────────────────────┘  │
│  Budget: 60-70%        │          │                           │
│  Goal: Maximum scale   │          │  Goal: Interest targeting │
└────────────────────────┘          │        with winners       │
                                    └───────────────────────────┘
```

### Flow Rules Summary

| Rule | Description |
|------|-------------|
| New creatives → Broad Pack | All new creatives start in TEST campaign, Broad Pack ad set |
| Winner = multi-destination | Winners go to SCALE (ASC) AND Interest Winners ad sets |
| No new tests in SCALE | SCALE campaign contains only proven winners, no experiments |
| Interest Winners ≠ new tests | Interest Winners ad sets contain graduated winners, not new creatives |
| Retarget/Retain = separate creatives | These campaigns use specific messaging, not the same test creatives |

### When Does a Creative NOT Advance?

A creative is paused (killed) and does not advance when (rules of thumb for this framework, not Meta figures: check them against the account's own history):

1. **No conversions after 2-3x CPA spend** → Pause immediately
2. **ROAS < 50% of target after significant spend** → Pause
3. **CTR < 0.5% with €100+ spend** → Pause or iterate
4. **Hook rate clearly below the account's own history after 10,000+ impressions** → Creative problem, iterate

### Practical Example

```
Scenario: E-commerce brand, AOV €80, Target ROAS 4x, Target CPA €20
Winner bar (Medium AOV): spend >= MAX(3 x €20, 3 x €80) = €240,
5-8 purchases, ROAS >= 3x

Week 1:
- Launch Broad Pack 2025-01-15 with Creative A, B, C, D
- The Broad Pack ad set has its own budget (ABO)

Week 3-4 (after €240+ spend per creative; C was stopped early):
- Creative A: €260 spend, 16 purchases, €1,600 revenue → ROAS 6.15x ✓
- Creative B: €280 spend, 8 purchases, €640 revenue → ROAS 2.29x (below threshold)
- Creative C: €55 spend, 0 purchases → KILL (in week 2)
- Creative D: €240 spend, 12 purchases, €1,120 revenue → ROAS 4.67x ✓

Actions:
- Creative A → Copy to SCALE + Interest #1 Winners + Interest #2 Winners
- Creative B → Keep testing (ROAS positive but below 3x threshold)
- Creative C → Pause (no conversions after 2.75x CPA)
- Creative D → Copy to SCALE + Interest #1 Winners + Interest #2 Winners
```

## Campaign Settings per Tier

Budget steps, frequency levels, test durations and audience windows in this section are rules of thumb, not Meta figures: check them against the account's own history. The existing-customer and ad-limit rows are Meta facts with their sources.

### SCALE - Advantage+ Sales Campaign (ASC)

| Setting | Value |
|---------|-------|
| Campaign Type | Advantage+ Sales Campaign |
| Budget Type | Advantage Campaign Budget (formerly CBO) |
| Targeting | 100% Broad (Advantage+ Audience) |
| Existing Customer Cap | Not available on new Advantage+ campaigns (legacy Advantage+ shopping field `existing_customer_budget_percentage`; "Advantage+ Campaigns", Marketing API); that guide replicates the cap with two ad sets, one that includes an existing-customer custom audience under a spending limit and one that excludes it |
| Creatives | Only validated winners |
| Max ads | 50 non-archived ads per ad set (Ad Set reference, Marketing API) |

**Scaling rules:**
- Increase budget in steps of about 20%, a few days apart (rule of thumb, not a Meta figure)
- Monitor frequency: >3.0 = creative fatigue risk
- Add new winners, don't immediately pause old ones

### TEST - Prospecting Campaign

| Setting | Value |
|---------|-------|
| Campaign Type | Manual Sales Campaign |
| Budget Type | ABO (Ad Set Budget Optimization) |
| Targeting | Broad (Broad Packs) + Interest (Winners) |
| Structure | A batch of new creatives per Broad Pack ad set |
| Test duration | Minimum 5-7 days |

**Broad Pack naming:**
```
Ad Set: "Broad Pack [YYYY-MM-DD]"
├── Creative #1: [Format]_[Concept]_[Hook]_V1
├── Creative #2: [Format]_[Concept]_[Hook]_V2
├── Creative #3: [Format]_[Concept]_[Hook]_V3
└── Creative #4: [Format]_[Concept]_[Hook]_V4
```

### RETARGET - Retargeting Campaign

| Audience | Window | Creative Approach |
|----------|--------|-------------------|
| FB/IG Engagers | 14 days | Social proof, testimonials |
| Website Visitors | 30 days | Product benefits, urgency |
| ATC/IC | 90 days | Abandoned cart, discount offers |

**Retargeting creative types:**
- Evergreen content (always relevant)
- Objection handlers (FAQ, guarantees)
- Sales/discount promotions
- Low barrier offers (free shipping, samples)
- Product-specific retargeting (Advantage+ Catalog Ads)

### RETAIN - Retention Campaign

| Audience | Creative Approach |
|----------|-------------------|
| All Time Purchasers | Cross-sell, new collections, VIP offers |
| 180 Day Purchasers | Replenishment, loyalty rewards, referral |

**Retention creative types:**
- Subscription/membership upsells
- Bundle offers
- Exclusive early access
- Referral programs

## Winner Criteria Framework

The thresholds below are rules of thumb for this framework, not Meta figures: check them against the account's own history.

### Step 1: Determine Client Parameters

**Always ask the user first:**
1. What is the average order value (AOV)?
2. What is the target CPA or ROAS?
3. What is the business model? (e-commerce low/high AOV, lead gen)
4. How much budget is available for testing?

### Step 2: Calculate Winner Thresholds

**Formula for E-commerce:**
```
Minimum Spend = MAX(3 x Target CPA, 3 x AOV)
Minimum Conversions = Depends on AOV tier (see table)
ROAS Threshold = Depends on business model (see table)
```

**Winner Criteria per Business Model:**

| Business Model | Min. Conversions | Min. Spend | ROAS Threshold |
|----------------|-----------------|------------|----------------|
| Low AOV (<€50) | 8-10 purchases | 3x CPA or ~€200-400 | >=4x ROAS |
| Medium AOV (€50-200) | 5-8 purchases | 3x CPA or ~€300-600 | >=3x ROAS |
| High AOV (>€200) | 3-5 purchases | 3x CPA or ~€500-1000 | >=2.5x ROAS |
| Lead Generation | 10-15 leads | 3x CPL or ~€200-500 | Lead Quality Score |

**Example calculation (Medium AOV):**
```
AOV = €100
Target CPA = €25
Target ROAS = 4x (€100/€25)

Winner Criteria:
- Minimum spend: MAX(3 x €25, 3 x €100) = €300
- Minimum conversions: 5-8 purchases
- ROAS threshold: >=3x (conservative) or >=4x (target)
```

### Step 3: Early Performance Signals (Video)

**Evaluate after 24-48 hours and 10,000+ impressions:**

| Metric | Benchmark | Action if Below |
|--------|-----------|-----------------|
| Hook Rate | 3-second views (`video_view` in `actions`) / impressions; compare with the account's own history | Iterate first 3 seconds |
| Hold Rate | `video_p50_watched_actions` / 3-second views (our proxy: ThruPlay is not available in `meta_get_insights`); compare with the account's own history | Check pacing and narrative |
| CTR | >=1% (target: 2%+) | Test other hooks/angles |
| CPC | <= account average | Monitor, don't pause yet |

### Step 4: Kill Criteria

**Pause creative when:**
- No conversions after 2-3x target CPA spend
- ROAS <50% of target after 5+ days
- CTR <0.5% with significant spend (>€100)
- Frequency >3.0 with declining performance
- Hook rate clearly below the account's own history after 10,000+ impressions

## Creative Velocity Guidelines

Rules of thumb for this framework, not Meta figures.

**How many new creatives per month?**

| Monthly Ad Spend | New Creatives | Structure |
|-----------------|---------------|-----------|
| €0-10k | 1-2 per month | Test on-demand at fatigue |
| €10-25k | 3-4 per month | Weekly iteration cycle |
| €25-50k | 4-8 per month | 1-2 per week |
| €50-100k | 8-16 per month | 2-4 per week |
| €100k+ | 15-50+ per month | Dedicated creative team |

**Creative production breakdown:**
- ~50% iterations on proven concepts
- ~30% new concepts within proven formats
- ~20% experimental new formats/angles

**Win rate expectations:**
- Track the account's own win rate (winners / creatives tested, per batch) and plan creative volume from it

## Budget Allocation Templates

Rules of thumb, not Meta figures: check them against the account's own history.

### Template A: Growth Focus (Recommended)
```
SCALE (ASC):     60%
TEST:            20%
RETARGET:        15%
RETAIN:           5%
```

### Template B: Efficiency Focus
```
SCALE (ASC):     50%
TEST:            15%
RETARGET:        25%
RETAIN:          10%
```

### Template C: New Account / Launch
```
SCALE (ASC):     40%  (or 0% until first winners)
TEST:            40%
RETARGET:        15%
RETAIN:           5%
```

## Account Audit Checklist

### Identifying Red Flags

Rules of thumb, not Meta figures: check them against the account's own history. The exception is the 50-per-week line, which follows Meta's learning-phase rule: an ad set shows "Learning limited" when it is unlikely to get about 50 optimization events in the week after its last significant edit (Meta Business Help Center, "About learning limited", undated, checked 2026-10-10).

| Red Flag | Impact | Action |
|----------|--------|--------|
| >5 active campaigns | Data fragmentation | Consolidate to 4-tier model |
| Ad sets <50 conv/week | Learning Limited | Merge or increase budget |
| >50% budget in learning | Inefficiency | Consolidate, increase budgets |
| No dedicated test campaign | No pipeline | Implement TEST tier |
| Retargeting >30% budget | Over-investment | Reduce, focus on prospecting |
| Frequency >4 on scale | Creative fatigue | Refresh creatives, add new |

### Audit Questions

1. **Structure:** How many active campaigns? (Ideal: 2-4; a rule of thumb for this 4-tier model)
2. **Learning:** What share of spend goes to ad sets in the learning phase? (Meta's Performance 5 page, https://www.facebook.com/business/ads/performance-marketing, links keeping under 20% of spend in the learning phase to a lower cost per purchase.) Separately, how many ad sets show Learning limited?
3. **Testing:** Is there a dedicated test campaign? (Must: Yes)
4. **Winners:** How are winners identified and scaled?
5. **Creative velocity:** How many new creatives per month?
6. **Attribution:** Is the Conversions API set up, with an Event Match Quality rating of Good or Great? (Meta's Conversions API docs call a "Good" or "Great" rating optimal: "Monitor Your Conversions API Gateway Setup", updated Feb 2, 2025; they also recommend aiming for a score of 6.0 or higher where possible: "Verifying Your Setup", updated Nov 24, 2025; both checked 2026-10-10.)

### MCP: Pull Account Structure for Audit

```python
# Get active campaigns with delivery status and budget
# format="full" keeps every requested field; above 30 campaigns the default "auto" format compacts the list
meta_query(account_id="act_XXXXX", entity_type="campaigns", effective_status=["ACTIVE"], fields=["id","name","status","daily_budget","lifetime_budget","objective","buying_type"], format="full")

# Get active ad sets in the account (learning status, audience info); add parent_id=<campaign_id> for one campaign
# learning_stage_info.status is LEARNING, SUCCESS or FAIL; Meta returns it only for active ad sets
meta_query(account_id="act_XXXXX", entity_type="adsets", effective_status=["ACTIVE"], fields=["id","name","status","daily_budget","targeting","optimization_goal","learning_stage_info"])
```

## Naming Convention

**Campaign Level:**
```
[Tier]_[Objective]_[BudgetType]_[Geo]
```
Example: `SCALE_SALES_ACB_NL` or `TEST_SALES_ASB_EU`

**Ad Set Level:**
```
[Tier]_[AudienceType]_[Date/Detail]
```
Example: `TEST_BROAD_2025-01-15` or `RT_WV30D_ALLPLC`

**Ad Level:**
```
[Format]_[Concept]_[Hook]_[Version]
```
Example: `VID_UGC_PROBLEM_V2` or `IMG_LIFESTYLE_BENEFIT_V1`

### Code Legend

| Code | Meaning |
|------|---------|
| SCALE | Scaling campaign (ASC) |
| TEST | Testing campaign |
| RT | Retargeting |
| RET | Retention |
| BROAD | Advantage+ Audience / Broad |
| INT | Interest targeting |
| LAL | Lookalike Audience |
| WV | Website Visitors |
| ENG | Engagers (FB/IG) |
| ATC | Add to Cart |
| IC | Initiate Checkout |
| PURCH | Purchasers |
| VID | Video |
| IMG | Static Image |
| CAR | Carousel |
| UGC | User Generated Content |

## Implementation Plan

### Week 1: Audit & Setup
1. Audit current account structure
2. Define winner criteria with client
3. Set up 4-tier campaign structure
4. Implement naming conventions

### Week 2: Testing Launch
1. Launch first Broad Pack with a batch of new creatives
2. Set up tracking and reporting dashboard
3. Monitor early signals (hook rate, CTR)

### Week 3-4: Optimize & Scale
1. Evaluate creatives against winner criteria
2. Graduate winners to SCALE/Interest
3. Kill underperformers
4. Launch new test batch

### Ongoing: Maintain Velocity
1. Weekly creative refresh cycle
2. Monthly structure audit
3. Quarterly winner criteria review

## Output Template: Account Restructuring Plan

```markdown
# Account Restructuring Plan: [Client Name]

## Current Situation
- Campaigns: [count]
- Ad Sets: [count]
- % in Learning Limited: [%]
- Primary issues: [list]

## Winner Criteria (Client-Specific)
- AOV: €[X]
- Target CPA: €[X]
- Target ROAS: [X]x
- Min. spend for winner: €[X]
- Min. conversions for winner: [X]

## Proposed 4-Tier Structure

### SCALE - ASC Campaign
- Budget: €[X]/day ([%] of total)
- Creatives: [current winners]

### TEST - Prospecting Campaign
- Budget: €[X]/day ([%] of total)
- First Broad Pack: [date]
- Creatives to test: [list]

### RETARGET Campaign
- Budget: €[X]/day ([%] of total)
- Audiences: [list with windows]

### RETAIN Campaign
- Budget: €[X]/day ([%] of total)
- Focus: [upsell/cross-sell strategy]

## Migration Timeline
- Week 1: [actions]
- Week 2: [actions]
- Week 3-4: [actions]

## Expected Impact
Estimate only from this account's own data and state the assumptions; otherwise write "not estimated".
- CPA: [current value] → [estimate, if supported]
- ROAS: [current value] → [estimate, if supported]
- Share of ad sets in Learning Limited: [current %] → [estimate, if supported]
```

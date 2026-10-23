---
name: meta-creative-fatigue-analyzer
description: "This skill should be used when the user asks to \"detect creative fatigue\", \"analyze frequency vs CTR\", \"plan a creative refresh\", or mentions \"Meta ad fatigue\", \"declining CTR on Facebook\", or \"frequency thresholds\"."
---
# Meta Ads Creative Fatigue Analyzer

## Purpose

Detect and prevent creative fatigue on Meta Ads (Facebook/Instagram). Help advertisers understand when performance drops are due to creative fatigue vs other factors, and provide actionable recommendations for refresh timing and strategies.

## When to Use This Skill

Invoke when user mentions:
- **CTR questions:** "Is my CTR declining due to high frequency?"
- **Refresh timing:** "When should I refresh my Meta creatives?"
- **Frequency concerns:** "What frequency is too high for conversion campaigns?"
- **Audience vs creative:** "Should I expand my audience or refresh creatives?"
- **Prevention:** "How do I prevent Meta creative fatigue proactively?"
- **Diagnosis:** "Is my campaign fatigued or is there another issue?"

## Key Questions This Skill Answers

Rules of thumb, not Meta figures: check them against the account's own history.

### Q1: Is my CTR dropping due to high frequency?

**Analysis Framework:**
1. Calculate CTR trend over time
2. Correlate with frequency increase
3. Check if CTR decline matches frequency curve

**Answer:** If frequency >3-4 for conversion campaigns AND CTR declining >10% week-over-week, creative fatigue is likely the cause.

### Q2: When should I refresh my creatives?

| Scenario | Refresh Every |
|----------|--------------|
| Standard budget, broad audience | 10-14 days |
| High budget, small audience | 5-7 days |
| High budget, large audience | 14-21 days |
| Low budget | 14-21 days |

### Q3: What frequency is too high?

| Campaign Type | Max Frequency/Week |
|--------------|-------------------|
| Conversion | 3-4/week |
| Consideration | 4-5/week |
| Awareness | 6-8/week |

### Q4: Should I expand audience or refresh creative?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AUDIENCE vs CREATIVE DECISION                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    What's happening with your metrics?
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
FREQUENCY HIGH              FREQUENCY NORMAL            REACH EXHAUSTED
+ CTR DECLINING             + CTR DECLINING             (can't reach more)
        │                           │                           │
        ▼                           ▼                           ▼
REFRESH CREATIVE            TEST NEW AUDIENCE          EXPAND AUDIENCE
(Primary issue)             (Targeting issue)          (Audience issue)
        │                           │                           │
        └───────────────────────────┼───────────────────────────┘
                                    │
                                    ▼
                          BOTH ISSUES?
                    Refresh creative + expand audience
```

## Fatigue Detection Algorithm

### Step 1: Pull Creative Performance Data

```
→ meta_get_creatives(account_id="act_XXXXXXXXX", scope="account", date_preset="last_14d", sort_by="spend")
```
This returns up to 10 ads by default (at most 25), ranked by spend, taken from the first 100 ad rows of the period, with their copy and their impressions, clicks, spend, CTR and CPC. It returns no dates: for an ad's age, take its `created_time` from `meta_query(account_id, "ads")`; for its first delivery in the window, take its first day with impressions in the Step 2 rows.

### Step 2: Pull Daily Frequency & CTR Trends

```
→ meta_get_insights(account_id="act_XXXXXXXXX", level="ad", date_preset="last_14d", time_increment="1", fields=["impressions", "reach", "frequency", "ctr", "cpm", "spend", "actions"])
```
Daily `time_increment="1"` is essential — plot CTR over time and correlate with frequency curve. This is the core fatigue detection signal.

Each daily row's `frequency` covers that day only (Meta: the average number of times each person saw the ad in the row's period). For the weekly frequency in Step 3, run the same call with `date_preset="last_7d"` and `time_increment="all_days"`.

### Step 3: Score Against Thresholds

Rules of thumb, not Meta figures: check them against the account's own history.

| Signal | Warning | Critical |
|--------|---------|----------|
| **CTR decline** | >10-15% over 7 days | >20% over 7 days |
| **CPM rise** | >20-30% over 14 days | >40% over 14 days |
| **Frequency** | >3/week (conversion) | >5/week (any type) |
| **Days active** | >10 days | >14 days |
| **Platform alert** | "Creative Limited" | "Creative Fatigue" warning |

### Step 4: Check Creative Diversity

Count genuinely different concepts, not ad objects: ads that share a concept with cosmetic changes count as one. Meta's guidance ('Demystifying creative diversification', Meta for Business, 16 Dec 2025, https://www.facebook.com/business/news/demystifying-creative-diversification) says ads that look or feel alike are treated as variations of the same creative and share learnings. It recommends ads that are truly different in look, feel, storyline and message, and ads that speak to different audience motivations or use cases. It gives no number.

```
Group the Step 2 rows by adset_id (level="ad" rows include ad_id, adset_id and campaign_id).
Use every row: while a response has paging.next, fetch the next page with
  meta_query(account_id, "ads", pagination_url=<paging.next>) and add its rows.
  Then sum each ad's daily rows before counting ads or ranking them by spend.
Ads with delivery: ads with impressions in the window (this includes ads paused since).
Distinct concepts: group those ads by concept, using the copy and creative details from
  meta_get_creatives (Step 1 covers the top-spend ads; scope="campaign" with the
  campaign_id and limit=50 returns up to 50 ads of one campaign; match on ad_id).
Top-3 spend share: spend of the 3 highest-spend ads divided by the ad set's spend.
```

Report per ad set: ads with delivery, distinct concepts, and the spend share of the top 3 ads. These are descriptive, not targets.

### Combined Signal (Critical)

When you see ALL THREE:
- Frequency high
- CTR declining
- CPM rising

**Action:** Refresh immediately - fatigue confirmed.

### Fatigue Timeline (Meta)

Rules of thumb, not Meta figures: check them against the account's own history. Only the learning phase is Meta's own term: Meta says an ad set usually leaves it after about 50 results in the week after its last significant edit, and advises waiting to edit until then ('About the learning phase', Meta Business Help Center).

| Phase | Days | What's Happening | Action |
|-------|------|------------------|--------|
| **Learning** | 1-7 | Algorithm optimizing | Don't touch |
| **Peak** | 7-10 | Best performance window | Monitor closely |
| **Early decline** | 10-14 | Fatigue signs appearing | Prepare refresh |
| **Fatigue** | 14+ | Performance degrading | Refresh or kill |

### CTR & CPM Patterns

Rules of thumb, not Meta figures: check them against the account's own history.

```
META ADS FATIGUE PATTERNS
──────────────────────────

CTR Pattern: Linear, gradual descent
├─ Predictable curve
└─ Watch for acceleration

CPM Pattern: Gradual incline
├─ Read it together with the CTR trend
└─ May spike suddenly at fatigue point
```

## Fatigue Detection Decision Tree

Rules of thumb, not Meta figures: check them against the account's own history.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IS MY META CREATIVE FATIGUED?                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                         Check Platform Alerts
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
           "CREATIVE LIMITED"               NO PLATFORM ALERT
           or "CREATIVE FATIGUE"                    │
                    │                               │
                    ▼                               ▼
           WARNING / CRITICAL             Check Frequency by Campaign Type
           Add a new, different ad                  │
                                    ┌───────────────┼───────────────┐
                                    ▼               ▼               ▼
                               CONVERSION       CONSIDER.       AWARENESS
                               >3-4/week?       >4-5/week?      >6-8/week?
                                    │               │               │
                                    ▼               ▼               ▼
                               ┌────┴────┐     ┌────┴────┐     ┌────┴────┐
                               YES    NO       YES    NO       YES    NO
                                │      │        │      │        │      │
                                ▼      ▼        ▼      ▼        ▼      ▼
                            Check   Likely   Check   Likely   Check   Likely
                            CTR    not      CTR    not       CTR    not
                            trend  fatigue  trend  fatigue   trend  fatigue
```

## Refresh vs Kill Decision Framework

Rules of thumb, not Meta figures: check them against the account's own history.

### Refresh Actions (Minor Tweaks)

These tweaks make variations of the same creative (Meta treats look-alike ads as one creative), so they do not add diversity. If the concept itself is fatigued, replace it with a genuinely different concept (Step 4).

When CTR or CPM reaches the Step 3 warning level:

1. **Change headline or primary text** - quick win
2. **Swap CTA button** - Learn More vs Shop Now
3. **Adjust image cropping** - new focal point
4. **Add text overlay** - reinforces message
5. **Change color scheme** - fresh look, same concept

### Kill Criteria (Pause Immediately)

- CTR falls >30% below campaign average
- CPA >2x baseline for 48 hours

A "Creative limited" or "Creative fatigue" status alone is not a reason to pause: Meta recommends adding a new, materially different ad and notes that keeping the original ad active may maximize results (see Platform Signals). For negative feedback, watch quality ranking: Meta replaced the relevance score with ad relevance diagnostics, and quality ranking reflects feedback such as people hiding the ad (see Quality Ranking Components).

## Prevention Strategies

Rules of thumb, not Meta figures: check them against the account's own history.

### Creative Rotation Schedule

| Scenario | Refresh Every |
|----------|--------------|
| Standard budget, broad audience | 10-14 days |
| High budget, small audience | 5-7 days |
| High budget, large audience | 14-21 days |
| Low budget | 14-21 days |

### Content Mix for Longevity

```
META CREATIVE MIX (RULE OF THUMB)
──────────────────────────────────

UGC Content: 40%
└─ Best for: Authenticity, social proof

Polished Content: 40%
├─ Brand consistency
├─ Professional look
└─ Best for: Brand campaigns, premium products

Dynamic Creative: 20%
├─ Combines the images and headlines you upload into variations
├─ Not a split test: Meta reports the variations in aggregate
└─ Meta says it may be unavailable for new sales or app promotion
   ad sets in Ads Manager since June 2024
```

Dynamic creative facts: 'About dynamic creative in Meta Ads Manager', Meta Business Help Center.

### Andromeda (Meta's Ad Retrieval System)

Andromeda is Meta's ad retrieval system: the first stage of delivery, which narrows tens of millions of candidate ads to a few thousand before ranking (Meta Engineering, 2 Dec 2024, https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/). For creative diversity, use the Step 4 check rather than an ad count.

### Variation Types to Prepare

1. **Different headline angles** (benefit, feature, social proof)
2. **Different imagery** (lifestyle, product, UGC)
3. **Different formats** (single image, carousel, video)
4. **Different CTAs** (Learn More, Shop Now, Sign Up)

## Platform Signals (Meta-Specific)

### Understanding Meta's Alerts

| Signal | What It Means | Action |
|--------|--------------|--------|
| **Creative Limited** | Delivery column status: people have seen the ad many times and its cost per result is above your past ads, but less than twice as much | Add a new, materially different ad; consider a wider audience |
| **Creative Fatigue** | Delivery column status: the same, with cost per result at twice your past ads or more | Add a new, materially different ad; consider a wider audience |
| **Learning Limited** | The ad set is unlikely to get about 50 optimization events in the week after its last significant edit | Different issue: combine ad sets, widen the audience, raise budget or bid, or choose a more frequent optimization event |

Definitions and actions are Meta's ('About creative fatigue recommendations in Meta Ads Manager'; 'About learning limited'; both Meta Business Help Center). Meta notes that keeping the original ad active instead of pausing it may maximize results. It offers the creative fatigue feature only for ad sets with one creative, and not with Advantage+ catalog ads, dynamic creative or Advantage+ app campaigns, so a missing status does not rule out fatigue.

### Quality Ranking Components

Monitor these for early fatigue signals (Meta's ad relevance diagnostics; each ranks as Above average, Average or Below average):
- **Quality Ranking:** perceived quality compared with ads competing for the same audience; Meta measures it with signals such as feedback from people viewing or hiding the ad
- **Engagement Rate Ranking:** expected engagement rate compared with ads competing for the same audience
- **Conversion Rate Ranking:** expected conversion rate compared with ads that have the same optimization goal and compete for the same audience

Meta does not show them for ads with fewer than 500 impressions, and says to use them to diagnose ads that miss their goals, not to optimize ads that already meet them ('About ad relevance diagnostics'; 'How to use ad relevance diagnostics'; 'About quality ranking'; all Meta Business Help Center). Read them per ad with `meta_get_insights(account_id="act_XXXXXXXXX", level="ad", fields=["quality_ranking", "engagement_rate_ranking", "conversion_rate_ranking"])`.

## Recovery Playbook

Rules of thumb, not Meta figures: check them against the account's own history.

### When Creative is Fatigued

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    META FATIGUE RECOVERY                                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                First: Try NEW CREATIVE
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
            WORKS                         DOESN'T WORK
                    │                               │
                    ▼                               ▼
             Continue with                Second: AUDIENCE EXPANSION
             new creative                 (Add 10-20% new audience)
                                                   │
                                    ┌───────────────┴───────────────┐
                                    │                               │
                                    ▼                               ▼
                            WORKS                           STILL STRUGGLING
                                                                   │
                                    │                               ▼
                                    ▼                  Third: COMBINED APPROACH
                             Scale up               New creative + 10-20% audience
                                                    + budget reallocation
```

### Budget Reallocation Strategy

- When creative ages >14 days: Shift 20-30% to new ad sets
- Reserve 20% for evergreen performers
- Test 10% on new creative concepts weekly

## Benchmarks

Rules of thumb, not Meta figures: check them against the account's own history.

### Frequency Thresholds by Campaign Type

| Campaign Type | Safe | Warning | Critical |
|--------------|------|---------|----------|
| Conversion | <3/week | 3-4/week | >4/week |
| Consideration | <4/week | 4-5/week | >5/week |
| Awareness | <6/week | 6-8/week | >8/week |

### CTR & CPM Warning Signs

| Metric | Warning Threshold | Critical Threshold |
|--------|-------------------|-------------------|
| CTR decline | >10% week-over-week | >20% week-over-week |
| CPM rise | >20% over 14 days | >40% over 14 days |

### Creative Lifespan by Type

Measure lifespan in the account instead of assuming a typical figure: per creative type (for example UGC and polished), count the days from launch until the Step 3 CTR or CPM warning is reached.

## Differentiating Fatigue from Other Issues

Rules of thumb, not Meta figures: check them against the account's own history.

### Not Fatigue - Different Problems

| Symptom | Likely Cause | Solution |
|---------|-------------|----------|
| "Learning Limited" | Budget too low or audience too narrow | Consolidate ad sets or raise budget |
| CTR normal but conversions down | Landing page or tracking issue | Check LP and pixel |
| Sudden performance drop (1 day) | External factor or algorithm change | Wait 24-48h before acting |
| High CPM but stable CTR | Competition increased | Accept or improve bid |

### Is It Fatigue? Checklist

- [ ] Frequency exceeds threshold for campaign type
- [ ] CTR declining over 7+ days (not just 1-2 days)
- [ ] CPM rising gradually (not sudden spike)
- [ ] Days active approaching or exceeding 14
- [ ] No recent significant changes to campaign
- [ ] No external factors (seasonality, competition)

## Output Template

When diagnosing Meta creative fatigue, provide:

```
## Meta Creative Fatigue Analysis

### Fatigue Score: X/10
(10 = severe fatigue)

**Components:**
- Frequency: [score] - [current] vs [threshold for campaign type]
- CTR trend: [score] - [% change over 7 days]
- CPM trend: [score] - [% change over 14 days]
- Days active: [score] - [days] vs 14 day threshold

### Status: [Healthy / Warning / Critical]

### Platform Signals
- Creative Limited: [Yes/No]
- Creative Fatigue Warning: [Yes/No]
- Learning Limited: [Yes/No - if yes, different issue]

### Diagnosis
- Fatigue detected: [Yes/No/Likely]
- Primary indicator: [which metric is driving diagnosis]
- Days until refresh needed: [estimate]

### Recommendations

**Refresh or Continue:** [decision]

**If Refresh:**
1. [Specific action 1]
2. [Specific action 2]

**Creative Suggestions:**
- [Based on current creative type]

**Audience Recommendation:**
- [Expand/Maintain/Test new]

**Testing Ideas:**
- [A/B test suggestion]
```

## Monitoring Checklist

### Daily Checks (High-Spend Campaigns)
- [ ] Frequency by ad set
- [ ] CTR trend (last 3 days)
- [ ] CPM trend (last 3 days)
- [ ] Platform alerts (Creative Limited, etc.)

### Weekly Checks
- [ ] Calculate fatigue score per creative
- [ ] Identify refresh candidates
- [ ] Review creative diversity per ad set (Step 4)
- [ ] Plan next week's refreshes
- [ ] Compare UGC vs polished performance

### Bi-Weekly Review
- [ ] Average creative lifespan analysis
- [ ] Frequency threshold validation
- [ ] Budget allocation vs creative performance
- [ ] Learnings documentation

---

*Sources: Meta for Business, 'Demystifying creative diversification' (16 Dec 2025), Meta Engineering on Andromeda (2 Dec 2024), and the Meta Business Help Center pages on creative fatigue, the learning phase, learning limited, ad relevance diagnostics and dynamic creative (checked 10 Oct 2026), each cited by title above. The frequency, CTR, CPM, CPA, budget and timing thresholds in this skill are rules of thumb, not Meta guidance: check them against the account's own history. Plan for 2-week refresh cycles with monitoring.*

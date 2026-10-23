---
name: meta-workflow-optimizer
description: "This skill should be used when the user asks to \"optimize my Meta Ads workflow\", \"create a daily checklist\", \"build SOPs for ad management\", or mentions \"Meta Ads workflow\", \"weekly review process\", or \"campaign management routine\". Do NOT use for: automated rules setup (use automated-rules-builder), campaign structure (use campaign-structure-advisor), performance diagnostics (use performance-troubleshooter)."
---
# Workflow Optimizer

## Overview

This skill helps set up streamlined workflows for Meta Ads management, including daily routines, weekly reviews, monthly audits, and efficient processes for campaign setup and optimization.

## Workflow Framework

### Time Allocation Model

```
┌─────────────────────────────────────────────────────────────────┐
│  EXAMPLE TIME ALLOCATION FOR A META ADS MANAGER                 │
│                                                                 │
│  DAILY (30-60 min)                                              │
│  ├── Performance check: 15 min                                  │
│  ├── Quick optimizations: 15 min                                │
│  └── Issue resolution: 15 min                                   │
│                                                                 │
│  WEEKLY (2-3 hours)                                             │
│  ├── Deep dive analysis: 45 min                                 │
│  ├── Creative review: 30 min                                    │
│  ├── Reporting: 30 min                                          │
│  └── Planning & testing: 45 min                                 │
│                                                                 │
│  MONTHLY (4-6 hours)                                            │
│  ├── Account audit: 2 hours                                     │
│  ├── Strategy review: 1 hour                                    │
│  ├── Budget planning: 1 hour                                    │
│  └── Competitor analysis: 1 hour                                │
└─────────────────────────────────────────────────────────────────┘
```

Rules of thumb, not Meta figures: check them against the account's own history. This covers the time budgets and thresholds throughout this skill.

## Daily Workflow

### Morning Check Routine (15 min)

```
DAILY CHECKLIST - 09:00
========================

□ SPEND CHECK (2 min)
├── Is spend on pace? (not too fast/slow)
├── Check budget alerts
└── Anomalies in spend pattern?

□ PERFORMANCE SNAPSHOT (5 min)
├── CPA vs target (green/yellow/red)
├── ROAS vs target
├── Top 3 & bottom 3 ad sets
└── Conversion volume vs yesterday

□ DELIVERY CHECK (3 min)
├── Are all campaigns active?
├── Ad sets in learning phase
├── Rejected ads?
└── Budget caps reached?

□ QUICK ACTIONS (5 min)
├── Pause clear losers
├── Make note for later investigation
└── Flag urgent issues
```

### Quick Optimization Actions

```
QUICK DAILY ACTIONS
====================

IF CPA > Target + 30%:
├── Check: Is this 1 day or a trend (3+ days)?
├── Check: Enough conversions for a conclusion?
└── Action: Pause or reduce budget

IF CPA < Target - 20%:
├── Check: Is audience not exhausted?
├── Check: Can it be scaled?
└── Action: Consider budget +20%

IF Ad Set in Learning:
├── Check: Make no changes
├── Check: On track for about 50 results in the week after the last
│   significant edit?
└── Action: Monitor, do not adjust

IF Rejected Ad:
├── Check: Which policy violation?
├── Action: Fix and resubmit
└── Escalate: If incorrect, appeal
```

Rules of thumb, not Meta figures: check them against the account's own history. The learning phase figure is Meta's: an ad set usually exits learning after about 50 results in the week after its last significant edit ("About the learning phase", Meta Business Help Center).

## Weekly Workflow

### Weekly Review Process (2-3 hours)

```
WEEKLY REVIEW - [FIXED DAY]
============================

BLOCK 1: DATA ANALYSIS (45 min)
─────────────────────────────
□ Export performance data (last 7 days)
□ Compare with previous week
□ Compare with targets
□ Identify trends

ANALYSIS QUESTIONS:
├── Which campaigns are overperforming? Why?
├── Which campaigns are underperforming? Why?
├── Are there audience exhaustion signals?
├── How is new creative performing?
└── Which placements deliver best ROAS?

BLOCK 2: CREATIVE REVIEW (30 min)
────────────────────────────────
□ Review ad performance metrics
□ Identify creative fatigue (CTR trend)
□ Plan new creative needs
□ Create brief for new assets

CREATIVE CHECKLIST:
├── Which ads have been running >3 weeks?
├── Which CTRs are declining?
├── Which hooks work best?
├── Which formats perform (video/static/carousel)?
└── How many active ads per ad set?

BLOCK 3: REPORTING (30 min)
──────────────────────────
□ Update performance dashboard
□ Write weekly summary
□ Highlight wins & learnings
□ Share with stakeholders

BLOCK 4: PLANNING (45 min)
─────────────────────────
□ Plan tests for next week
□ Budget reallocation if needed
□ Creative production pipeline update
□ Calendar check for events/promos
```

### Weekly Metrics Dashboard

```
WEEKLY KPI TRACKER
==================

METRIC          │ TARGET │ THIS WEEK │ LAST WEEK │ TREND
────────────────┼────────┼───────────┼───────────┼──────
Spend           │ $X     │           │           │
Impressions     │ X      │           │           │
Clicks          │ X      │           │           │
CTR             │ X%     │           │           │
Conversions     │ X      │           │           │
CPA             │ $X     │           │           │
ROAS            │ Xx     │           │           │
Frequency       │ X      │           │           │

TOP PERFORMERS:
1. [Campaign/Ad Set] - [Metric]
2. [Campaign/Ad Set] - [Metric]
3. [Campaign/Ad Set] - [Metric]

UNDERPERFORMERS:
1. [Campaign/Ad Set] - [Issue]
2. [Campaign/Ad Set] - [Issue]
3. [Campaign/Ad Set] - [Issue]

ACTIONS FOR NEXT WEEK:
□ [Action 1]
□ [Action 2]
□ [Action 3]
```

## Monthly Workflow

### Monthly Audit Checklist

```
MONTHLY ACCOUNT AUDIT
======================

□ ACCOUNT HEALTH (30 min)
├── Pixel/CAPI status check
├── Event tracking validation
├── Catalog sync status
├── Audience sizes trend
└── Billing/payment status

□ CAMPAIGN STRUCTURE (30 min)
├── Too many/few campaigns?
├── Ad set consolidation needed?
├── Naming conventions consistent?
├── Old campaigns cleanup
└── Test campaigns evaluation

□ AUDIENCE AUDIT (30 min)
├── Custom audiences up-to-date?
├── Lookalike audiences still active? (With Advantage+ audience, a lookalike works as an audience suggestion)
├── Advantage+ Audience enabled on prospecting ad sets?
├── Audience overlap check
├── Exclusions correct?
└── New audience ideas

□ CREATIVE AUDIT (30 min)
├── Clean up creative library
├── Performance per creative type
├── Document top hooks
├── Creative refresh schedule
└── Archive A/B test results

□ BUDGET & BIDDING (20 min)
├── Budget efficiency per campaign
├── Bid strategy effectiveness
├── Dayparting opportunities?
├── Seasonality planning
└── Next month budget planning

□ COMPETITIVE REVIEW (20 min)
├── Ad Library competitor check
├── New messaging/offers?
├── Creative trends in market
└── Identify opportunities
```

Sources for the audience lines: "Meta Advantage+ features" describes Advantage+ lookalike as using a lookalike audience as a suggestion; "About Advantage+ audience" does not recommend Advantage+ audience for retargeting.

### Monthly Strategy Review

```
MONTHLY STRATEGY REVIEW
========================

1. PERFORMANCE VS GOALS
├── Did we hit targets?
├── Where did we fall short?
├── What external factors played a role?
└── How realistic were the targets?

2. LEARNINGS DOCUMENTATION
├── Top 3 learnings this month
├── What worked unexpectedly well?
├── What worked unexpectedly poorly?
└── Hypotheses for next month

3. STRATEGY ADJUSTMENTS
├── Should we adjust funnel balance?
├── Are there new audiences to test?
├── Does creative strategy need to change?
└── Budget reallocation needed?

4. NEXT MONTH PLANNING
├── Key priorities (max 3)
├── Tests to run
├── Creative production needs
└── Important dates/events
```

## Campaign Setup Workflow

### New Campaign Launch Checklist

```
CAMPAIGN LAUNCH CHECKLIST
=========================

PRE-LAUNCH (1-2 days before)
───────────────────────────
□ Campaign objective confirmed
□ Budget defined (daily/lifetime)
□ Target audience created
□ Creative assets approved
□ Landing page live and tested
□ Tracking verified (pixel events)
□ UTM parameters correct
□ Naming convention applied

SETUP CHECKLIST
───────────────
□ Campaign level:
  ├── Correct objective
  ├── Budget strategy (Campaign budget vs Ad set budget)
  ├── A/B test setup if needed
  └── Campaign budget set

□ Ad Set level:
  ├── Audience targeting correct
  ├── Placements configured
  ├── Optimization goal correct
  ├── Budget (if ABO)
  ├── Schedule set
  └── Bid strategy chosen

□ Ad level:
  ├── Creative correctly uploaded
  ├── Primary text filled in
  ├── Headline filled in
  ├── CTA button correct
  ├── URL correct + UTMs
  └── Preview on all placements

LAUNCH DAY
──────────
□ Final review in preview mode
□ Publish campaign
□ Verify delivery start
□ Note launch time for reporting
□ Set calendar reminder for 24h check

POST-LAUNCH (24-48 hours)
────────────────────────
□ Delivery check (impressions coming in)
□ No policy rejections
□ CTR in expected range
□ Conversion tracking works
□ Learning phase started
```

## Efficiency Tools & Templates

### Naming Convention Template

```
NAMING CONVENTION SYSTEM
=========================

CAMPAIGN LEVEL:
[Brand]_[Objective]_[Funnel]_[Geo]_[MMYY]

Example: Acme_Conv_BOFU_US_0124

AD SET LEVEL:
[Audience Type]_[Audience Detail]_[Placement]

Example: LAL_1pct_Purchasers_AllPlace

AD LEVEL:
[Creative Type]_[Format]_[Version]_[Hook Type]

Example: UGC_Video_v2_ProblemHook

FULL EXAMPLE:
Campaign: Acme_Conv_BOFU_US_0124
└── Ad Set: LAL_1pct_Purchasers_AllPlace
    └── Ad: UGC_Video_v2_ProblemHook
```

### Quick Templates

```
PERFORMANCE UPDATE TEMPLATE (Slack/Email)
=========================================

**Daily Performance Update - [DATE]**

**Spend:** $X (X% of daily target)
**Conversions:** X
**CPA:** $X (target: $X) [green/yellow/red]
**ROAS:** Xx (target: Xx) [green/yellow/red]

**Highlights:**
- [Positive highlight]
- [Positive highlight]

**Watch items:**
- [Concern if any]

**Actions taken:**
- [Action if any]

---

CREATIVE REQUEST TEMPLATE
=========================

**Creative Brief - [CAMPAIGN]**

**Deadline:** [DATE]
**Platform:** [FB/IG/Both]
**Format:** [Static/Video/Carousel]
**Dimensions:** [1:1/4:5/9:16]

**Objective:** [Awareness/Conversion]
**Target Audience:** [Description]
**Key Message:** [1 sentence]
**CTA:** [Desired action]

**Requirements:**
- [Specific requirement 1]
- [Specific requirement 2]

**References:**
- [Link to inspiration]

**Deliverables:**
- [ ] [Format 1]
- [ ] [Format 2]
```

## Automation Opportunities

### Tasks to Automate

```
AUTOMATION PRIORITY
====================

HIGH PRIORITY:
├── Automated rules for budget protection
├── Performance alerts (Slack/Email)
├── Automated reporting
└── Ad scheduling (dayparting)

MEDIUM PRIORITY:
├── Creative performance tracking spreadsheet
├── Competitor ad monitoring
├── Audience refresh reminders
└── A/B test result logging

NICE TO HAVE:
├── AI-powered copy suggestions
├── Automated creative rotation
├── Predictive budget allocation
└── Cross-platform reporting
```

### Tools Ecosystem

```
RECOMMENDED TOOL STACK
======================

NATIVE (Free):
├── Meta Ads Manager (management)
├── Meta Business Suite (scheduling)
├── Automated Rules (optimization)
└── Ads Reporting (dashboards)

ESSENTIALS (Budget-friendly):
├── Google Sheets (tracking/reporting)
├── Slack (alerts & communication)
├── Notion/Asana (project management)
└── Canva (quick creative edits)

ADVANCED (Scale):
├── Triple Whale / Northbeam (attribution)
├── Motion (creative analytics)
├── Foreplay (creative research)
└── Supermetrics (reporting automation)
```

## MCP Tool Integration

### Automating the Daily Check

Replace manual Ads Manager browsing with direct data pulls:

```
DAILY CHECK (with MCP):

1. Performance snapshot (ad sets with delivery today):
→ meta_get_insights(account_id="...", fields=["spend","cost_per_action_type","purchase_roas","impressions","frequency"], date_preset="today", level="adset")

2. Weekly trend (top/bottom performers):
→ meta_get_insights(account_id="...", fields=["spend","cost_per_action_type","purchase_roas"], date_preset="last_7d", level="campaign")

3. Creative health check (by default: up to 10 ads ranked by spend over
   the last 30 days, taken from the first 100 ad rows):
→ meta_get_creatives(account_id="...", scope="account")

4. Delivery check (what is not running, and why):
→ meta_query(account_id="...", entity_type="ads", effective_status=["WITH_ISSUES","DISAPPROVED"], fields=["name","effective_status","issues_info","ad_review_feedback"])
→ meta_query(account_id="...", entity_type="adsets", effective_status=["ACTIVE"], fields=["name","effective_status","learning_stage_info","issues_info"])
→ meta_query(account_id="...", entity_type="account", fields=["account_status","disable_reason","spend_cap","amount_spent"])
```

How to read the delivery check: `ad_review_feedback` names the policy behind a rejected ad, and `issues_info` gives the delivery error. In `learning_stage_info`, `LEARNING` means wait, and `FAIL` (Ads Manager shows "Learning limited") means the ad set gets too few results for its budget and audience. For the account, read `account_status` first: 1 is active, 2 is disabled, and a disabled account carries a non-zero `disable_reason`. A `spend_cap` of `"0"` means no limit. A positive `spend_cap` stops all delivery once `amount_spent` reaches it, so when the two are close, raise or reset the cap before it runs out. Meta leaves an empty field out, so a missing `issues_info` means no issues.

`meta_get_insights` returns one page: while a response has `paging.next`, fetch the next page with `meta_query(account_id, "adsets", pagination_url=<paging.next>)` and add its rows. Then compare the results with the targets in the Morning Check Routine above.

## Example Interaction

**User**: "I spend way too much time managing my Meta Ads accounts. How can I work more efficiently?"

**Claude response**:

"Let's optimize your workflow. Here is a streamlined system:

---

**FIRST STEPS:**

1. **Set up Automated Rules** (about 30 min to set up)
```
- CPA > Target x 1.3 → Pause ad set
- CPA < Target x 0.8 → Notification to scale
- Frequency > 3.5 → Creative refresh alert
```
Rules of thumb, not Meta figures: check them against the account's own history. Under a campaign budget, Meta does not allow cost-based rules that pause ad sets or only notify, so put the CPA rules on the campaign (see automated-rules-builder).

2. **Fixed Time Blocks** (Structure)
```
- 09:00-09:15: Daily check (no longer!)
- [Fixed day] 10:00-12:00: Weekly deep dive
- [1st Monday]: Monthly audit
```

3. **Build a Dashboard** (20 min setup)
```
One view with only what you actually need:
- Spend vs target
- CPA trend (7 days)
- Top/bottom performers
```

---

**EFFICIENCY CHECKLIST:**

Which of these do you currently do manually?
- [ ] Check all ads individually daily
- [ ] Manually adjust budgets
- [ ] Copy performance data to sheets
- [ ] Create the same report weekly

For each one you check off, I'll suggest a way to automate or shorten it.

---

**What is your biggest time waster right now?**
I'll focus on that first."

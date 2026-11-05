---
name: linkedin-pacing-check
description: "Use when the user asks for a LinkedIn pacing check, why LinkedIn spends above the daily budget, whether a LinkedIn budget will run out early, or why LinkedIn is underspending. Do NOT use for: choosing a bid strategy, a full weekly performance review, or changing budget and bid guardrails."
---
# LinkedIn Pacing Check

Explain observed spend against campaign budgets and the remaining schedule.
Daily spend above the daily budget can be normal LinkedIn pacing.
It is a reason to inspect the full budget and schedule, not proof of a billing error.
This analysis reads data; it does not enforce a spending ceiling or change a budget.

## Step 1: Choose the account and window

**Data you need:** Selected account, affected campaign if known, reporting dates
and whether the advertiser is concerned about overdelivery or underdelivery.
The default is the last 14 days ending yesterday UTC.
Use completed days for the primary review; label a partial current day separately.

```python
linkedin_get_analytics(
    account_id="<account_id>", level="account", analysis="pacing")
```

The account view reads the first 100 ACTIVE campaigns.
It is a bounded review, not a complete historical inventory of every campaign.
A paused campaign or one outside those first 100 can be absent.
For a named campaign, bind the read directly:

```python
linkedin_get_analytics(
    account_id="<account_id>", level="campaign", entity_id="<campaign_id>",
    analysis="pacing", start_date="<start_date>", end_date="<end_date>")
```

Use an inclusive window of at most 92 days.
Do not combine explicit dates with date_range.
Pacing supports account or campaign level, not campaign_group.
Omit pivot, pivots, fields and target_companies.
Pacing uses fixed CAMPAIGN/DAILY data and its own spend fields.
LinkedIn caps analytics at 15,000 rows without pagination.

## Step 2: Verify the budget being compared

**Data you need:** Campaign dailyBudget, totalBudget, currency, runSchedule,
status, pacingStrategy when present, and the parent campaign group.

```python
linkedin_query(account_id="<account_id>", entity_type="campaigns",
               entity_id="<campaign_id>", format="full")
linkedin_query(account_id="<account_id>", entity_type="campaign_groups",
               entity_id="<campaign_group_id>", format="full")
```

Identify whether the campaign has a daily budget, a total budget or both.
Do not use a parent group's total budget as though it were the campaign daily budget.
Daily budgets reset at midnight UTC.
A daily budget with a fixed schedule also needs a full-flight budget review.
PacingStrategy may be absent, including with smart budget groups.
An absent strategy is unknown; do not fill it with an assumed default.

These reads show current settings, not historical budget edits.
Ask for advertiser change history if the budget changed inside the reporting window.
A comparison with today's budget can misrepresent a day that used a different budget.
Keep Money amounts and their currency together.
Do not compare a EUR spend amount with a USD budget.

## Step 3: Read observed days and flags

**Data you need:** Daily spend rows, budget ratios, days with usable spend data,
average_daily_spend, flags and currency warnings.

Only days with observed spend contribute to average_daily_spend.
Missing days remain null, not invented zeros.
An empty result can mean no activity or no read access.
Today's RUNNABLE status cannot prove historical delivery on missing days.

| Observation or flag | What it establishes | Next action |
|---------------------|---------------------|-------------|
| Daily spend above the daily budget | Observed overdelivery relative to the compared budget | Inspect the full schedule and current LinkedIn guidance |
| OVER_150_PERCENT_DAY | A diagnostic threshold in the tool was crossed | Review budget history and the flagged day; it is not a universal billing rule |
| UNDERDELIVERING | Average spend is below 50% with at least seven observed spend days | Read serving holds before proposing bid changes |
| NO_SPEND_IN_WINDOW | No spend was observed in the response | Check access, reporting coverage and serving state |
| NO_DAILY_BUDGET | There is no daily budget for a ratio | Review total budget and schedule instead |
| CURRENCY_MISMATCH | Available budget and report currencies disagree | Resolve the currency difference before interpreting ratios |
| Missing daily rows | The tool lacks evidence for those days | Report incomplete coverage |
| No warning flag | No implemented threshold was crossed in this bounded view | Still inspect totals, schedule and missing data |

Flags are diagnostic aids, not advertiser-approved thresholds or automatic actions.
The report fields cannot independently verify an unknown reporting currency.
Do not sum only known days and call the result complete if other days are missing.

## Step 4: Explain spend above the daily budget

**Data you need:** Observed spend, the daily budget used for the comparison,
current campaign schedule, budget history and LinkedIn's current help guidance.

Use this explanation:

> Daily spend above the daily budget can be normal LinkedIn pacing. Review the
> full schedule and budget, then check LinkedIn Help, "Daily budgets", for the
> current guidance that applies to this campaign.

Do not present a fixed percentage as LinkedIn's rule.
A repeated ratio on one account is an observation, not a platform guarantee.
The tool's named flag also does not establish a universal allowed overspend percentage.
A supply forecast is an estimate and does not define a billable spending limit.

For each flagged day, show the spend amount, compared daily budget and ratio.
Label a ratio as measured for those inputs.
Explain whether the campaign's budget changed during the period.
If historical budgets are unavailable, state that the ratio uses the current snapshot.
Do not declare the charge invalid from the ratio alone.

If the advertiser needs an absolute spending boundary, explain that Ad Superpowers checks budget and bid writes for large steps, high amounts and LinkedIn pricing, requiring explicit confirmation where needed. It refuses budgets above its currency limits unless strictly decreasing, but does not cap actual spend or guard schedule-only changes. Present a proposed budget or schedule decision
for approval; do not claim this analysis will stop spend automatically.

## Step 5: Interpret projected exhaustion

**Data you need:** totalBudget, runSchedule.end, usable observed spend, currency
agreement, remaining_budget_upper_bound and projection_note.

The projection subtracts spend in the selected window from totalBudget.
It floors that result at zero and treats it as an upper bound on remaining budget.
It does not read spend before the selected window.
Actual remaining budget may therefore be lower.

The tool compares that upper bound with average daily spend multiplied by the
time remaining from now until the exclusive schedule end.
projected_to_exhaust_before_end is true only when projected spend strictly exceeds
the upper bound. Otherwise the projection is null, meaning unknown, not false.

| Projection result | How to report it |
|-------------------|------------------|
| true | Current average spend suggests exhaustion before the scheduled end, even using the remaining-budget upper bound |
| null with missing totalBudget | A total-budget exhaustion estimate is unavailable |
| null with missing schedule end | There is no end date against which to evaluate exhaustion |
| null with missing spend or currency mismatch | Data is insufficient for the projection |
| null with usable inputs | Early exhaustion is not established; earlier spend can still reduce the remaining budget |

Read projection_note in the response rather than guessing why a projection is null.
Do not convert this estimate into a promise of the day the budget will run out.
Averages can change when delivery, audience or bids change.

## Step 6: Diagnose low delivery separately

**Data you need:** Campaign ID and current serving reasons for the campaign and creatives.

```python
linkedin_query(account_id="<account_id>", entity_type="serving_diagnosis",
               campaign_id="<campaign_id>")
```

A future start hold suggests waiting.
A total budget hold calls for a budget review with the advertiser.
A campaign or campaign-group status hold calls for checking parent state.
A review hold calls for checking LinkedIn's review status.
An account or billing hold needs the notices in Campaign Manager.

Follow the returned exact reason and remedy before proposing a higher bid.
If the diagnosis is truncated, narrow it to the affected campaign.
If there are no holds, use bid suggestions, audience sizing and a supply forecast
through the bid strategy skill to investigate the next possible constraint.
Do not treat a missing day as historical proof of any current hold.

## Step 7: Report and decide

**Data you need:** Complete-day window, campaign coverage, spend ratios,
projection caveats, exact holds and the advertiser's actual budget constraint.

Return a compact table:

| Campaign | Observed days | Window spend | Daily budget | Flags | Projection | Next action |
|----------|---------------|--------------|--------------|-------|------------|-------------|
| <campaign_name> | <observed_days> | <amount_currency> | <amount_or_missing> | <flags> | <true_or_unknown> | <one_action> |

Keep these qualifications next to the result:

- Account coverage is limited to the first 100 ACTIVE campaigns unless narrowed.
- Analytics has a provider row cap and missing days are unknown.
- Budget settings are current snapshots, not a history of budget changes.
- Remaining budget is an upper bound because pre-window spend is not read.
- Spend above the daily budget is not, by itself, evidence of a billing error.

Recommend waiting, a tracking/access check, a serving remedy or a budget review
based on the evidence. Do not change budgets or statuses during a pacing check.
If the advertiser approves a change separately, read back the affected settings
and repeat the relevant pacing or serving read to verify the result.

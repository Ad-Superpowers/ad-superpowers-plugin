---
name: linkedin-weekly-review
description: "Use when the user asks for a LinkedIn weekly review, a week-over-week LinkedIn performance report, or to review LinkedIn account, campaign group, campaign and creative results together. Do NOT use for: diagnosing a single ad that cannot run, a pacing-only check, or general benchmark research."
---
# LinkedIn Weekly Review

Review account totals first, then campaign groups, campaigns and creatives.
Compare equal periods before recommending changes.
Finish with the main change, its evidence and a short list of proposed actions.
This workflow reads performance; it does not change campaign settings.

## Step 1: Set comparable periods and read the account

**Data you need:** Selected account, reporting currency, primary outcome,
seven complete current days and the immediately preceding seven days.
Use inclusive dates and exclude an unfinished day from the comparison.
Ask the advertiser to define the primary outcome: native form leads, website
conversions, clicks or another metric available in the returned data.

```python
linkedin_list_ad_accounts(account_id="<account_id>", format="full")
linkedin_get_analytics(
    account_id="<account_id>", level="account",
    start_date="<current_start_date>", end_date="<current_end_date>",
    time_granularity="ALL",
    fields=["impressions", "clicks", "costInLocalCurrency",
            "oneClickLeads", "externalWebsiteConversions"])
linkedin_get_analytics(
    account_id="<account_id>", level="account",
    start_date="<previous_start_date>", end_date="<previous_end_date>",
    time_granularity="ALL",
    fields=["impressions", "clicks", "costInLocalCurrency",
            "oneClickLeads", "externalWebsiteConversions"])
```

Replace the placeholders with equal adjacent windows before calling.
Do not combine date_range with start_date or end_date.
Retain requested dates, provider reporting dates and any warnings.
Rounded or missing provider dates weaken the comparison even if requested dates match.
Empty analytics can mean no activity or no read access; do not report it as zero.

Compute CTR as clicks divided by impressions and CPC as spend divided by clicks.
Compute CPM as spend divided by impressions times 1,000.
Keep native form CPL separate from cost per website conversion.
Use sums of additive metrics to compute rates, never the average of row-level rates.
A missing metric or zero denominator leaves the rate unavailable.
Relative change is unavailable when the previous value is zero or absent.

## Step 2: Find which campaign groups explain the change

**Data you need:** Group IDs and names, group totals for both periods, and their
contribution to account spend and results.

```python
linkedin_query(account_id="<account_id>", entity_type="campaign_groups", format="full")
linkedin_get_analytics(
    account_id="<account_id>", level="campaign_group",
    start_date="<current_start_date>", end_date="<current_end_date>",
    time_granularity="ALL",
    fields=["impressions", "clicks", "costInLocalCurrency", "oneClickLeads"])
```

Without entity_id, campaign_group level breaks down the account's groups.
Repeat the analytics call with the previous window and identical fields.
Compare each group's absolute spend and result changes as well as percentage changes.
A small group can have a large percentage change with little effect on the account.
Do not add account totals and group totals together: they are different views of the same spend.

To inspect one group and its campaigns:

```python
linkedin_get_analytics(
    account_id="<account_id>", level="campaign_group", entity_id="<campaign_group_id>",
    start_date="<current_start_date>", end_date="<current_end_date>",
    time_granularity="ALL", pivots=["CAMPAIGN_GROUP", "CAMPAIGN"],
    fields=["impressions", "clicks", "costInLocalCurrency", "oneClickLeads"])
```

Repeat for the previous period before judging winners and losers.
Match returned pivotValues to entity IDs; preserve unknown IDs rather than guessing names.

## Step 3: Inspect the campaigns behind each material change

**Data you need:** Campaign ID, objective, status, budget, targeting and totals
for the same two windows.

```python
linkedin_query(account_id="<account_id>", entity_type="campaigns",
               entity_id="<campaign_id>", format="full")
linkedin_get_analytics(
    account_id="<account_id>", level="campaign", entity_id="<campaign_id>",
    start_date="<current_start_date>", end_date="<current_end_date>",
    time_granularity="DAILY",
    fields=["impressions", "clicks", "costInLocalCurrency",
            "oneClickLeads", "externalWebsiteConversions"])
```

Campaign level always needs entity_id.
Repeat for the previous period to locate when the change began.
Keep campaign objectives separate when comparing cost per result.
Current campaign settings are a snapshot, not an audit log of last week's edits.
Use advertiser change history to explain budget, audience or offer changes.

If observed delivery fell, inspect holds before blaming bids:

```python
linkedin_query(account_id="<account_id>", entity_type="serving_diagnosis",
               campaign_id="<campaign_id>")
```

A present hold explains current serving eligibility, not every historical missing day.
If budget utilization is the question, use a separate analysis="pacing" request.
Do not add pacing analysis to the pivot or demographic calls below.

## Step 4: Check audience and placement mix

**Data you need:** One demographic dimension or up to three non-demographic
statistics dimensions, matching periods and suitable metrics.

```python
linkedin_get_analytics(
    account_id="<account_id>", level="campaign", entity_id="<campaign_id>",
    start_date="<current_start_date>", end_date="<current_end_date>",
    time_granularity="ALL", pivot="MEMBER_JOB_FUNCTION",
    fields=["impressions", "clicks", "costInLocalCurrency"], limit=100)
linkedin_get_analytics(
    account_id="<account_id>", level="campaign", entity_id="<campaign_id>",
    start_date="<current_start_date>", end_date="<current_end_date>",
    time_granularity="ALL", pivots=["CAMPAIGN", "SERVING_LOCATION"],
    fields=["impressions", "clicks", "costInLocalCurrency"])
```

Repeat the relevant call for the previous period.
Use pivot for a single MEMBER_* demographic dimension.
Use pivots for one to three non-demographic dimensions, never MEMBER_* values.
Do not supply pivot and pivots together.
For company-level ABM use MEMBER_COMPANY and verified target_companies.
Demographics are approximate, privacy-filtered and delayed by 12-24 hours.
Prefer ALL granularity rather than summing daily demographic noise.
A missing company or job function row does not prove zero delivery.

Avoid conversion and reach metrics with IMPRESSION_DEVICE_TYPE.
Analytics responses are capped at 15,000 rows without pagination.
Demographic display limits can truncate rows; report the returned coverage.
A change in audience or placement mix can explain a CTR change without creative wear.

## Step 5: Compare creatives and inspect fatigue

**Data you need:** Campaign creatives, current performance and an exact comparison
with the immediately preceding equal-length period.

```python
linkedin_get_analytics(
    account_id="<account_id>", level="campaign", entity_id="<campaign_id>",
    start_date="<current_start_date>", end_date="<current_end_date>",
    time_granularity="ALL", pivots=["CAMPAIGN", "CREATIVE"],
    fields=["impressions", "clicks", "costInLocalCurrency", "oneClickLeads"])
linkedin_get_creatives_with_images(
    account_id="<account_id>", campaign_id="<campaign_id>",
    start_date="<current_start_date>", end_date="<current_end_date>",
    compare_previous_period=True, include_images=True, limit=20)
```

Repeat the creative-pivot analytics call for the previous dates to compare native leads.
The creative comparison tool calculates its previous window automatically.
Its fatigue signal uses CTR, not lead completion or frequency.
Read the reason alongside fatigue_signal and the returned period boundaries.

Fatigue requires all of these conditions:

- CTR fell at least 25% relative to the previous period.
- Both periods have at least 1,000 impressions for that creative.
- Account-wide CTR did not also fall at least 25%.
- The provider periods are exactly equal, adjacent and complete for the comparison.

The account baseline includes analytics rows beyond the display limit and campaign filter.
It is still subject to LinkedIn's provider row cap.
A signal is a review prompt, not proof that the creative caused the decline.
If account-wide CTR also falls, investigate mix, auction or timing before rotating ads.
If periods are inexact, fatigue_signal is null; do not turn null into false.
If the previous read fails, report current performance and an unavailable comparison.

## Step 6: Choose the next action

**Data you need:** Account-to-creative findings, comparable periods, hold reasons
and advertiser-provided lead quality outcomes where available.

| Finding | Interpretation | Proposed next action |
|---------|----------------|----------------------|
| Spend rose and cost per result stayed stable | More volume at similar efficiency | Check lead quality before proposing scale |
| One group accounts for most lost results | The change is concentrated | Inspect its campaigns before changing the account |
| Low delivery with a hold | Eligibility is blocking delivery | Follow the exact hold remedy |
| One creative has a valid fatigue signal | Creative wear is plausible | Propose a controlled image or copy test |
| Account-wide CTR also fell | The fatigue condition is not met | Review targeting, placements and timing |
| Native form CPL improved, SQL rate fell | Cheap leads may be less useful | Review CRM qualification with sales |
| Missing dates, metrics or access | The comparison is incomplete | State what cannot be concluded |

Rank proposed actions by measured contribution to the account change.
Do not pause or activate creatives as part of this read-only review.

## Report to the advertiser

- Current and previous dates, currency, primary outcome and data limitations.
- Account spend, results, CTR and cost per result with absolute and relative changes.
- Campaign group and campaign contributions to the change.
- Creative findings with fatigue reasons and impression counts in both periods.
- Up to three proposed actions, each tied to evidence and an owner.

Distinguish observed results from hypotheses and advertiser-supplied CRM outcomes.
Keep unresolved data gaps visible in the recommendation.

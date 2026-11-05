---
name: linkedin-ad-not-running
description: "Use when the user asks why is my LinkedIn ad not running, why a LinkedIn campaign has no delivery, or to explain LinkedIn serving holds or an ad stuck in review. Do NOT use for: cost benchmarking, choosing a bid strategy after holds are resolved, or a recurring weekly performance review."
---
# LinkedIn Ad Not Running

Find the reason an ad cannot serve before changing its budget, bid or audience.
Return the exact provider reason, the affected level and one next action per reason.
A read does not authorize a campaign change.

## Step 1: Read serving diagnosis

**Data you need:** Selected account, affected campaign ID and, if known, creative URN.
Use the campaign ID when the advertiser names a particular campaign.

```python
linkedin_query(
    account_id="<account_id>", entity_type="serving_diagnosis",
    campaign_id="<campaign_id>")
```

For a specific creative, narrow the same read:

```python
linkedin_query(
    account_id="<account_id>", entity_type="serving_diagnosis",
    campaign_id="<campaign_id>",
    entity_id="urn:li:sponsoredCreative:<creative_id>")
```

If no campaign is identified, include stopped and draft campaigns explicitly:

```python
linkedin_query(
    account_id="<account_id>", entity_type="serving_diagnosis",
    status=["ACTIVE", "PAUSED", "DRAFT"])
```

The unfiltered account read defaults to ACTIVE campaigns.
Status filters the campaign list, not a keyed campaign or the creative list.
Do not add format, targeting inputs or non-default start/count to diagnosis.
It reads at most 100 campaigns and 100 creatives.
If summary.truncated is true, narrow by campaign_id and label the account view incomplete.

Keep raw servingStatuses, servingHoldReasons and review alongside diagnosis.
For each diagnosis retain code, source, layer, level, meaning and remedy.
An unknown code stays unknown; do not translate it into a guessed billing problem.
A campaign and its creative can have several simultaneous blockers.
Resolve the parent blocker as well as the creative blocker.

## Step 2: Match each reason to a remedy

**Data you need:** The returned diagnosis codes and affected entity levels.
The table gives one next action per known serving or processing reason.
For policy rejection details, use the exact returned reason and remedy.

| Reason | One next action | Where or permission |
|--------|-----------------|---------------------|
| STOPPED | Review the entity's intended status and whether it should resume | Approval before a status write |
| CAMPAIGN_STOPPED | Review whether the parent campaign should resume | Approval before a campaign status write |
| UNDER_REVIEW | Check the review status and wait for LinkedIn's decision | Campaign Manager |
| PENDING | Check the pending review | Campaign Manager |
| REJECTED | Correct the rejection cause before submitting a revised creative | Advertiser approval |
| NEEDS_REVIEW | Read the review details | Campaign Manager |
| REFERRED_CONTENT_QUALITY_HOLD | Inspect the content quality notice | Campaign Manager |
| FORM_HOLD | Read the attached form's state and review | lead_forms read below |
| PROCESSING | Read the recorded media processing status | Upload status read below |
| PROCESSING_FAILED | Inspect the failure before proposing a replacement asset | Approval for a replacement upload |
| JOB_POSTING_ON_HOLD | Inspect the promoted job's hold | Campaign Manager |
| JOB_POSTING_INVALID | Inspect the promoted job's validity | Campaign Manager |
| ACCOUNT_TOTAL_BUDGET_HOLD | Review the account's total budget | Campaign Manager; approval to change |
| ACCOUNT_END_DATE_HOLD | Review whether the account end date should extend | Campaign Manager; approval to change |
| CAMPAIGN_START_DATE_HOLD | Wait until the scheduled start | No write needed |
| CAMPAIGN_END_DATE_HOLD | Propose an appropriate schedule extension | Approval before a schedule write |
| CAMPAIGN_TOTAL_BUDGET_HOLD | Review whether to raise the campaign's total budget | Approval before a budget write |
| CAMPAIGN_AUDIENCE_COUNT_HOLD | Size the full targeting criteria before proposing broader targeting | audience_count read below |
| CAMPAIGN_GROUP_START_DATE_HOLD | Wait until the group's scheduled start | No write needed |
| CAMPAIGN_GROUP_END_DATE_HOLD | Review whether the group end date should extend | Approval before a schedule write |
| CAMPAIGN_GROUP_TOTAL_BUDGET_HOLD | Review the group's total budget | Approval before a budget write |
| CAMPAIGN_GROUP_STATUS_HOLD | Review whether the parent group's status should change | Approval before a status write |
| ACCOUNT_SERVING_HOLD | Read account notices; the API does not identify the underlying cause | Campaign Manager |
| BILLING_HOLD | Read billing notices | Campaign Manager |
| MISSING_PRIVACY_POLICY | Ensure the privacy-policy page contains the actual statement | Advertiser's website |
| NONFUNCTIONAL_SITE | Make the landing page load successfully | Advertiser's website |
| NON_MATCHING_LANGUAGES | Match the ad and landing-page language | Advertiser approval |
| Other rejection code | Follow its returned remedy and LinkedIn Advertising Policies | Campaign Manager and advertiser |
| Unknown code | Preserve the code and inspect the account notice | Campaign Manager |

A remedy_is_write flag means a write is one possible remedy.
It does not mean every remedy requires a write: waiting for a future start needs none.
Never clear a budget hold by automatically raising the budget.

## Step 3: Gather evidence for the selected remedy

**Data you need:** Campaign settings, parent group ID, and whichever form,
audience or staged media is named by the diagnosis.

```python
linkedin_query(account_id="<account_id>", entity_type="campaigns",
               entity_id="<campaign_id>", format="full")
linkedin_query(account_id="<account_id>", entity_type="campaign_groups",
               entity_id="<campaign_group_id>", format="full")
```

For a form hold, get the attached form ID from the creative and read it:

```python
linkedin_query(account_id="<account_id>", entity_type="creatives",
               entity_id="urn:li:sponsoredCreative:<creative_id>", format="full")
linkedin_query(account_id="<account_id>", entity_type="lead_forms",
               entity_id="urn:li:adForm:<form_id>")
```

Draft the form with linkedin_manage (object_type="lead_form", DRAFT only) or in
Campaign Manager; publish it in Campaign Manager, then attach it.
Publishing, archiving and editing a published form are unavailable through Ad Superpowers.
The form must be PUBLISHED in the same account, without REJECTED or AUTO_REJECTED review.
The campaign must use LEAD_GENERATION, with offsiteDeliveryEnabled not true.
For a new supported image/video creative, attach with create_inline and leadgenCallToAction.
Leaving DRAFT freezes the form destination and rechecks its eligibility.
Reactivation also rechecks the form.

For an audience hold, assign the campaign's complete targetingCriteria to `criteria`:

```python
linkedin_query(account_id="<account_id>", entity_type="audience_count",
               targeting_criteria=criteria)
```

Audience count is rounded; zero may mean fewer than 300 members.
A count is not a reach forecast or proof that the campaign will serve.

For a recorded staged asset, inspect processing without uploading again:

```python
linkedin_upload(ad_account_id="<account_id>", stage_id="<stage_id>",
                asset_name="<exact_staged_filename>", action="status")
```

Use media only after ready_for_use is true.
If the stage is unknown or an upload outcome is ambiguous, do not restage automatically.

## Step 4: Inspect desktop and mobile presentation

**Data you need:** Creative URN and a fresh preview for each returned placement.

```python
linkedin_query(account_id="<account_id>", entity_type="ad_preview",
               entity_id="urn:li:sponsoredCreative:<creative_id>")
```

Inspect both desktop and mobile previews for copy, image and CTA alignment.
The preview iframe expires after about three hours; fetch it again when needed.
In our testing, LinkedIn's preview returned UNSUPPORTED_CREATIVE_TYPE for a lead gen creative, and LinkedIn documents no preview for lead gen.
If ad_preview fails for a lead gen creative, suggest a preview in Campaign Manager.
An unsupported preview does not prove that the creative is invalid or rejected.
A preview is not a policy approval or a delivery guarantee.

## Step 5: Apply only the approved remedy

**Data you need:** Advertiser approval, the exact entity and intended status,
current review, parent state and readiness to serve.

A creative under review cannot be paused: LinkedIn returns 400 until review is APPROVED.
Do not retry the same pause while review is pending.
DRAFT creatives without review can report review_pending_activation=true.
That does not establish approval; activate only when the ad is ready to serve.
Do not activate it simply to test whether a pause will work.

Use a full creative URN for status, update or delete.
After approval, an activation uses this separate call:

```python
linkedin_manage(
    ad_account_id="<account_id>", object_type="creative", action="status",
    entity_id="urn:li:sponsoredCreative:<creative_id>",
    target_status="ACTIVE", confirm_launch=True, payload={})
```

Do not put status or intendedStatus in payload.
A campaign cannot change status while its parent campaign group is DRAFT.
Review the group first; changing it can affect more than the selected campaign.
An existing approval must cover the actual entity and change before executing it.
Form, billing and account-level remedies belong in Campaign Manager.

## Step 6: Verify and report

**Data you need:** A fresh diagnosis after a confirmed remedy and any remaining holds.

```python
linkedin_query(account_id="<account_id>", entity_type="serving_diagnosis",
               campaign_id="<campaign_id>")
```

A successful status write does not prove the ad is serving.
Check isServing, review, raw holds and the remaining diagnosis together.
If the view is truncated or unreadable, state that verification is incomplete.
If no holds remain but delivery is low, continue with bid and audience planning.
Do not diagnose creative fatigue from an ad that has no usable delivery data.

Report these items to the advertiser:

- Affected campaign or creative and its current state.
- Each exact hold code, its level and one remedy.
- Which remedies were reads or waiting, and which changes were approved.
- What the follow-up diagnosis confirmed.
- Remaining blockers and who should resolve them.

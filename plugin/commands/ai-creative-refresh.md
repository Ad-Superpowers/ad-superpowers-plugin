---
description: "End-to-end creative refresh pipeline: analyze ad performance, detect fatigue, build a creative brief from your top performers, then upload and deploy a new image you provide (existing Meta image_hash, authorized private local staging, or direct public HTTPS URL). Image generation happens outside the app. Bring your own image from Photoshop, Canva, Midjourney, Gemini, or anywhere."
disable-model-invocation: true
---

> **Platforms:** meta
> Included in trial and paid plans. Your existing quota and permissions still apply.
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Creative Refresh

End-to-end creative refresh pipeline: analyze performance → detect fatigue → build a creative brief from top performers → upload your new image → deploy as a paused ad for review.

**Image generation is intentionally NOT part of this workflow.** Use whatever image tool you prefer (Photoshop, Canva, Midjourney, ChatGPT/Gemini in your client, etc.) — this workflow handles everything around the image: the analysis, the brief that tells you what to make, the upload, and the deployment.

**Requirements:**
- Connected Meta Ads account
- A new image you want to deploy (after Step 5):
  - **Existing asset:** reuse an image_hash from the selected ad account.
  - **Local image:** JPEG/PNG up to **20 MB (20,000,000 bytes)** and 16 megapixels, using private staging when your workspace currently has upload access to the selected Meta account and your client has file access and HTTP upload. Tool discovery alone does not establish access.
  - **Public URL:** an approved, direct HTTPS image URL. A Drive/Dropbox sharing page is not necessarily a downloadable file. Existing source validation and limits apply.
  - **No file/HTTP access:** use an already approved direct URL or manually upload in Ads Manager, then discover the account-library hash. Do not require public hosting of private files.

## OUTPUT FORMAT

### CREATIVE AUDIT SUMMARY
| Metric | Value |
|--------|-------|
| Account | {account name} |
| Campaign | {campaign name} |
| Active Ads | {count} |
| Fatigued Ads | {count} |
| Top Performer | {ad name} (CTR: X%, ROAS: Y) |
| Avg Creative Age | {days} days |

### TOP PERFORMERS (Reference for the Creative Brief)
| Ad Name | CTR | CPC | ROAS | Impressions | Days Active | Image Style |
|---------|-----|-----|------|-------------|-------------|-------------|

### FATIGUED ADS (Need Refresh)
| Ad Name | Frequency | CTR Decline | CPM Change | Days Active | Fatigue Score |
|---------|-----------|-------------|------------|-------------|---------------|

### CREATIVE BRIEF (For You to Execute Externally)
- **Visual style:** {derived from top performer}
- **Subject / focal point:** {derived}
- **Color palette:** {derived}
- **Composition / framing:** {derived}
- **Lighting:** {derived}
- **Aspect ratio:** 4:5
- **Variations to produce:** 2
- **Negative cues (avoid):** {derived}

### UPLOAD + DEPLOYMENT STATUS
| Image | Source | image_hash | Ad Name | Ad Set | Status | Ad ID |
|-------|--------|------------|---------|--------|--------|-------|

## EXECUTION STEPS

### Step 1: Discover Account
```
meta_list_ad_accounts()
```
Let the user select their account
> Conditional: if account_id
 or use account `[specify account_id]`.

### Step 2: Creative Audit
Fetch current creatives with performance data:
```
meta_get_creatives(account_id="FROM_STEP_1", scope="campaign"
> Conditional: if campaign_id
, campaign_id="[specify campaign_id]")
```

Then get insights for trend analysis:
```
meta_get_insights(account_id="FROM_STEP_1", date_preset="last_14d", level="ad", fields=["ad_name","impressions","reach","frequency","clicks","ctr","cpm","cpc","spend","actions"])
```

Also get the previous period for comparison:
```
meta_get_insights(account_id="FROM_STEP_1", level="ad", fields=["ad_name","frequency","ctr","cpm"], time_range={"since":"21_DAYS_AGO","until":"8_DAYS_AGO"})
```

### Step 3: Fatigue Detection
Apply Meta fatigue thresholds:
| Indicator | Warning | Critical |
|-----------|---------|----------|
| Frequency | >4/week | >6/week |
| CTR Decline (WoW) | >15% | >20% |
| CPM Increase (WoW) | >25% | >40% |
| Days Active | >14 days | >21 days |

Score each ad (100-point scale):
- Frequency above threshold: +30 points
- CTR decline: +25 points
- CPM increase: +25 points
- Creative age: +20 points

Score >=50 = HIGH FATIGUE | 30-49 = WARNING | <30 = HEALTHY

### Step 4: Analyze Top Performers
From the creative audit, identify the winning elements of the best-performing ads (highest CTR + ROAS):
- **Visual style:** Product photo, lifestyle, UGC, flat lay
- **Color palette:** Dominant colors, contrast level
- **Composition:** Layout, subject placement, background
- **Lighting:** Natural, studio, dramatic, soft
- **Mood / emotion:** Confident, calm, urgent, aspirational

### Step 5: Output the Creative Brief
Synthesize Step 4 into a structured creative brief in the OUTPUT FORMAT above. **Stop here and present the brief to the user.** The user will use this brief externally (in their image tool of choice) to produce 2 new image(s).

Wait for the user to provide an image, a destination-account image_hash, or an approved direct HTTPS image URL. Generation is an external/client function; do not claim that every AI client can read local files or perform HTTP uploads.

### Step 6: Prepare the Approved Media
Follow `media-upload-guide` for the full input and retry procedure. Confirm the selected workspace/account and existing upload authorization.

- Reuse an existing image_hash in that account without uploading again.
- For a local JPEG/PNG with a capable client and current workspace/account upload access: calculate size/SHA-256 locally, call `assets_stage(platform="meta", account_id="FROM_STEP_1", asset_type="image", filename=..., content_type=..., size_bytes=..., sha256_expected=...)`, PUT the original bytes with the returned URL/headers from the client, then call `meta_upload_image(account_id="FROM_STEP_1", stage_id=..., name=...)`. Keep the returned image_hash for Step 7. Do not send base64 through the conversation for this route or save the upload capability in a manifest.
- Explain that original bytes, including embedded metadata, pass through AdSuperpowers and temporary private Storage to Meta. Keep the original; this is not a library or backup. Only this byte transfer bypasses the MCP payload, not files already given to the AI client.
- For an approved direct HTTPS URL use `meta_upload_image(account_id="FROM_STEP_1", image_url=...)`, then use its image_hash in Step 7. The existing `meta_create_ad(image_url=...)` route is also available when the combined upload/ad write is authorized.
- Preserve workspace, original connection, account and immutable finalization name. On a lost PUT response, try finalizing the existing stage. On `finalization_retryable`, follow retry_after using the same stage/name. On `outcome_unknown`, stop and inspect the account library; never blindly upload or restage.
- For batches use the guide's small window and secret-free local manifest. Fifty new staged images normally cost 100 successful MCP calls, excluding checks, replays and ad creation; PUT costs zero. Ordinary plan limits apply.
- Video and other platforms follow their existing guides; do not pass stage_id to unsupported tools.

### Step 7: Deploy to Meta (Approved Only)
For each approved image_hash from Step 6:
```
meta_create_ad(
    account_id="FROM_STEP_1",
    adset_id="FROM_USER",
    image_hash="FROM_STEP_6",
    headline="FROM_USER",
    body="FROM_USER",
    link_url="FROM_USER",
    cta_type="LEARN_MORE",
    status="PAUSED"
)
```

Ads are created as PAUSED for final review. Activation through `meta_update()` requires a separate explicit instruction; never enable spend implicitly.

## EDGE CASES
- **No fatigued ads:** Confirm healthy status. Still offer a proactive refresh if any ad is >10 days old.
- **User has no image yet:** Stop at Step 5 with the creative brief. Resume from Step 6 once they have a usable image source.
- **User only has a local image:** Use private staging when current workspace/account upload access permits it and the client supports file/HTTP access; otherwise use the manual account-library route. See media-upload-guide.
- **Image is not PNG/JPEG:** Ask the user to convert (Meta only accepts standard image formats).
- **Image transfer fails (Step 6):** surface the structured `assets_stage` or `meta_upload_image` error and its retry hint. Check the selected account, source requirements and upload permissions. Stop on `outcome_unknown`; inspect the existing stage and destination before any new write. Ad-creation errors belong to Step 7.
- **No ad sets available:** Help the user identify the right ad set via `meta_query`.
- **All ads performing well:** Suggest A/B testing the new creative against the current winners rather than replacing them.
---
name: meta-media-upload-guide
description: "This skill should be used when the user asks to \"upload a video to Meta\", \"upload an image to Meta\", \"push a local file into Meta media library\", \"use a Canva / Google Drive / Dropbox asset for an ad\", \"Meta says it can't upload my local file\", \"how do I get an image_hash\", \"bulk upload creatives\", or mentions \"image_url vs image_hash\", \"video_url vs video_id\", \"Meta Media Library\", \"Zakelijke media\", or \"Meta asset hosting\". Covers the complete decision tree from a file on disk to a usable Meta asset. Do NOT use for: ad copy (use ad-copy-generator), video scripts (use video-script-writer), creative strategy (use creative-diversification-generator), CAPI / pixel setup (use capi-implementation-guide)."
---
# Meta Media Upload Guide

Requires the Ad Superpowers MCP server with a Meta Ads connection.

The single source of truth for getting creative assets into Meta Ads when using Ad Superpowers' MCP tools. It answers the question **"why won't Claude upload my local file?"**.

## Choose the upload route

Reuse an existing destination-account `image_hash` or `video_id` first (PATH B).
For a **local JPEG/PNG up to 20 MB (20,000,000 bytes)**, prefer **private staging** when `assets_stage`
is available (PATH C). The client needs file access and HTTP upload (for example a local shell); the remote MCP
server cannot open a client path or an attachment in another application. Client
support must be tested, not inferred from a product name. Use a connected Meta
account that your workspace is currently allowed to modify. Tool discovery alone
does not establish upload access; do not change rollout settings yourself.

An already public, direct HTTPS media URL remains supported (PATH A). For
`meta_upload_image(image_url=...)`, Ad Superpowers downloads the image and uploads
it to Meta. Do not publish private client files merely to obtain a URL.

Legacy `meta_upload_image(image_data=...)` remains available with the existing
4 MiB raw-byte limit. Around **50 KB is a practical context warning**, not an
additional enforced limit. Avoid sending ordinary creative-sized base64 strings
through the conversation. If staging or local shell access is unavailable, use
an approved existing URL or manual Ads Manager upload and library discovery.
For a local MP4 up to **500 MB (500,000,000 bytes)**, follow the private staging
route in PATH D. Preserve IDs and outcomes from earlier attempts: a later
successful upload does not resolve an old uncertain attempt. Never repeat or
restage an uncertain upload automatically. An existing approved asset, an
already approved URL or authorized manual Ads Manager upload remains an option.

For a folder, use the bounded staged workflow below when available. Manual
Ads Manager drag/drop remains an alternative, especially when Meta must be the
only remote store. Uploading media does not authorize creating or activating ads.

**Filename hints reduce friction on every path.** Use consistent aspect-ratio suffixes when you name files (`_1x1`, `_9x16`, `_4x5`, `_16x9`, `_1.91x1`) so Claude can match the right asset to the right placement automatically after upload. See "Filename-based aspect ratio matching" below.

## PATH A — You already have a URL

Simplest case. The URL must be:

- **Publicly reachable HTTPS** (open an incognito browser window to verify — no auth wall, no VPN)
- **Direct link to the media file itself**, not a viewer page (for Google Drive / Dropbox, see PATH D hosting rules)
- **Format**: Meta's Ads Guide recommends JPG or PNG for images and MP4, MOV or GIF for video, and says other types are supported
- **Size constraints** (Meta Ads Guide, Facebook Feed): video 1 second to 241 minutes, at least 120 x 120 pixels, up to 4 GB; image up to 30 MB and at least 600 pixels wide. Other placements differ, for example Instagram Feed video runs up to 60 minutes. Source: https://www.facebook.com/business/ads-guide/update (read 10 October 2026).
- **Temporary URLs work** while they are still valid when the tool runs: for an image, Ad Superpowers downloads the file during the call; for a video, Meta fetches it from the URL. An expiring link such as a presigned S3 URL is fine on those terms.

Commands:

```python
# Image ad
meta_create_ad(
    account_id="act_...",
    adset_id="...",
    headline="...", body="...", link_url="https://...",
    image_url="https://your-host/image.jpg",
)

# Video ad (one call: upload, wait for processing, create; see the note below)
meta_create_ad(
    account_id="act_...",
    adset_id="...",
    headline="...", body="...", link_url="https://...",
    video_url="https://your-host/video.mp4",
)

# Pre-upload a video (decouple from ad creation)
meta_upload_video(account_id="act_...", video_url="https://...", title="Spring Launch v3")
# → returns {video_id: "12345...", status: "processing"}
# Then poll until it is ready:
meta_get_video_status(video_id="12345...")
# → status: "ready" → now usable in meta_create_ad(video_id="12345...")
```

If the video is still processing when `meta_create_ad`'s own wait ends, it
returns `error="video_still_processing"` with the `video_id` (if the call itself
times out first, there is no such response: use the `video_id` from the upload). Poll
`meta_get_video_status` until the status is `ready`, then retry with
`video_id` instead of `video_url`.

## PATH B — Reuse an existing library asset

If your asset is already in Meta's library (uploaded via an earlier ad, bulk-dropped in Ads Manager, or pushed via `meta_upload_video`), just reuse its handle. No re-upload.

**Find existing assets:**

```python
# Images in this ad account's library. format="full" keeps every field;
# with the default format="auto", more than 50 rows shrink to id + name only.
meta_query(account_id="act_...", entity_type="adimages", limit=100, format="full")
# Returns rows under "data" with: hash, name, width, height, aspect_ratio_bucket,
# created_time, url_128 (thumbnail), permalink_url, status, creatives[]

# Videos
meta_query(account_id="act_...", entity_type="advideos", limit=50)
# Returns items with: id, title, source, picture, length, format, aspect_ratio_bucket

# Filter by date: only assets uploaded since 17 April
meta_query(account_id="act_...", entity_type="adimages", since="2026-04-17")
```

`since` / `until` filter the returned page on the Ad Superpowers side (Meta's
adimages edge takes no date filter), so for a large library raise `limit` or
follow `paging.next` with `meta_query(..., pagination_url=<paging.next>)`. Pages
fetched with `pagination_url` come back raw: no date filter and no
`aspect_ratio_bucket`, so filter and compute ratios yourself.

**Filter by placement using `aspect_ratio_bucket`:**

| Bucket | Placement use case |
|--------|-------------------|
| `9:16` | Stories and Reels (Meta's recommended ratio there) |
| `4:5` | Facebook Feed and Instagram Feed images (Meta's recommended ratio there) |
| `1:1` | Marketplace (recommended); also listed for the feeds, Stories, Reels and search |
| `16:9` | In-stream video (with 1:1) |
| `1.91:1` | Right column; also listed for the feeds and search |

These follow Meta's placement table; see "Placement → ratio mapping" below for the source.

```python
# Pick an asset for Stories (format="full" puts every row, with its hash, under "data")
result = await meta_query(account_id, "adimages", format="full")
stories_assets = [i for i in result["data"] if i.get("aspect_ratio_bucket") == "9:16"]
hash_to_use = stories_assets[0]["hash"]

# Use in ad
meta_create_ad(..., image_hash=hash_to_use)
```

**Gotcha:** `image_hash` is scoped to the ad account. You cannot reuse a hash from account A in account B. Each account needs its own copy.

## PATH C — Local JPEG/PNG with private staging (preferred)

Image generation is an external/client function, not an MCP upload capability.
For video use PATH D; for another platform use its own guide and inputs.
A stage is bound to its platform, account and media type. The byte transfer bypasses the MCP payload, but
metadata and files already given to an AI client may still be in its context.

At first use explain that original media, including embedded metadata, passes
through Ad Superpowers and temporary private storage at its provider before
uploading to the chosen Meta account. This does not need a new confirmation per
file when the user has already authorized the upload. Preserve their original.

1. Compute bytecount and SHA-256 locally, printing only metadata (for example
   `wc -c < hero.jpg` and `sha256sum hero.jpg`). Do not print or base64 the file.
2. Call `assets_stage(platform="meta", account_id="act_...", asset_type="image",
   filename="hero.jpg", content_type="image/jpeg", size_bytes=...,
   sha256_expected="<local SHA-256>")`. PNG uses `image/png`. This route supports
   up to 20 MB (20,000,000 bytes) and 16 megapixels; provider/placement limits
   can be stricter, and the returned stage policy is authoritative.
3. Send the file with the returned method, URL and headers from the local client.
   Keep the capability in memory. If using curl, supply its URL and returned
   headers through `--config -` on stdin and the file through `--data-binary
   @hero.jpg`; never interpolate the capability into argv, shell history or a
   generated script. Do not enable verbose/trace logging or redirects.

   Treat the URL as a credential: no shared logs or committed manifests
   containing it. Only the local HTTP client opens `hero.jpg`; never pass a
   `file_path` to MCP. No temporary public/signed read URL is involved.
4. On HTTP 201 call `meta_upload_image(account_id="act_...", stage_id="stg_...",
   name="hero_1x1")`. Supply exactly one of `stage_id`, `image_data`, `image_url`.
   Compare returned SHA-256 with the local hash; store the resulting image_hash.
   A separate, authorized ad-creation call can use that hash.

The upload URL expires after 10 minutes and permits one admitted attempt.
`finalize_before` is 24 hours from reservation; the 10-minute URL expiry does
not expire an already ready stage. Persisted results can replay until
`result_expires_at` (30 days). Source objects are scheduled for deletion after
success/failure/expiry, normally on a 15-minute cleanup cadence. Physical deletion
may lag during an outage; this is not a guaranteed physical retention deadline.
Replay rechecks current org/account access and the exact original connection.
Another authorized colleague in the same org may finalize/replay; actor attribution
is not a private-storage boundary. Always keep the original account and `name`.

| Outcome | Next action |
|---|---|
| Own PUT 429: `upload_capacity_exceeded`, `upload_attempt_consumed=false`, `Retry-After` | Wait the hint, then retry the same PUT before expiry. It is a pacing hint, not reserved capacity. |
| Lost PUT response / network error / proxy 429 | Do not blindly resend PUT. Attempt finalization of the known stage to learn its state. |
| `finalization_capacity_exceeded` / `finalization_in_progress` | Wait, then repeat the same stage/name. Capacity refusal happens before blobread and spends no service attempt. |
| `finalization_retryable` | Wait `retry_after`, keep the same stage/name; max three service attempts and at least 60 seconds cooldown. |
| `outcome_unknown` | Check the destination library; never automatically restage or resend. Filename or local SHA alone cannot prove Meta acceptance. |
| `stage_conflict` / access denied | Restore the original parameters or resolve access to the bound connection; do not switch destinations. |
| Definitive expired/failed stage with no uncertain platform effect | Fix the cause, then stage afresh if still authorized. |

### Folder workflow and local manifest

Use a window of **two files**, reserving only when a slot is free; at most five
open stages per org. Store path, SHA, destination, immutable name, stage-ID,
status and image_hash in a local manifest. Keep capabilities and credentials out
of it. On restart reuse completed hashes; retry only the explicitly safe states
above. Stop automatic processing for uncertain results and quota exhaustion.

One successful stage and one successful finalization cost **two tool calls**;
HTTP PUT costs none. A successful result replay costs another call. Estimate quota
before starting: 50 new images normally need 100 successful calls, excluding
replays, checks and ad creation. A 50-call trial cannot cover that full batch.
Ordinary plan limits apply; this is not a reservation or a quota bypass.
A sequential 50-file client flow was proven with local app/MCP/PG/Redis,
real Storage and simulated Meta. Attended production tests later accepted an
exact 20,000,000-byte PNG and an exact 500,000,000-byte MP4 at Meta through this
route; upload acceptance is not ad approval. These single live observations are
not a hosted 50-file acceptance and do not establish sustained or parallel
throughput. There is no measured 1,000-file or parallel-bulk capacity claim.
A complete empty daily orphan-inventory recurrence was observed in production
and dev on 13 September 2026. This confirms one recurrence per environment, not
every day's execution or deletion of a non-empty orphan inventory. Startup alone
is not recurrence.

Rollback stops new stages and all PUT requests, including unused issued URLs.
Already ready stages and stored results remain usable within their deadlines;
cleanup continues with retained Storage configuration. Do not keep retrying a
PUT that returns `asset_upload_disabled`.

### Legacy inline image fallback

`meta_upload_image(account_id="act_...", image_data="<base64>", name="hero")`
retains its existing raw-byte cap of 4 MiB. Use for small inputs when appropriate;
50 KB is guidance about context cost, never a new rejection rule. Prefer staging
for normal images; lack of shell access does not make remote file paths work.

## PATH D — Local MP4 video with private staging

Use MP4 with H.264 video and optional AAC audio, up to **500 MB (500,000,000
bytes)**, 1–1800 seconds, with each dimension between 120 and 1920 pixels. The
client needs local file access and HTTP upload. Current account permissions and
the returned stage policy still apply; placement requirements can be stricter.

1. Compute the exact bytecount and SHA-256 locally. Preserve the original and
   explain the private staging flow as in PATH C.
2. Reserve with `assets_stage(platform="meta", account_id="act_...",
   asset_type="video", filename="launch.mp4", content_type="video/mp4",
   size_bytes=..., sha256_expected="<local SHA-256>")`.
3. Send the original bytes once using the returned method, URL and headers.
   Apply PATH C's capability handling: private HTTP PUT from the client, no
   redirects or verbose tracing, and no file bytes or capability in MCP/chat.
4. After HTTP201, call `meta_upload_video(account_id="act_...",
   stage_id="stg_...", title="launch.mp4")`. Save the stage, account, title,
   returned video ID and receipt. `stage_id` and `video_url` are exclusive.
5. Inspect that same record with `meta_upload_video(account_id="act_...",
   stage_id="stg_...", title="launch.mp4", action="status")`. Each call reads
   the recorded video's status once. Upload acceptance alone does not establish
   readiness; require an explicit `ready_for_use=true` observation before use.

The title becomes fixed on the first finalization; keep account, stage and title
unchanged for status and retained-result replay. Private video attempts never
retry provider writes automatically. Pending processing, a failed status read
or `outcome_unknown` does not authorize another reservation or retransmission.
Status inspection never resumes bytes. Creating an ad or spending still needs
separate authorization even after the video is ready.

Reuse an existing account video ID when possible. An explicitly authorized manual
Ads Manager upload or already approved direct URL remains an alternative. Do not
publish a private file just to obtain a URL; the hosting examples below apply
only when sharing has already been authorized.

### Hosting options (ranked by practicality)

| Option | Good for | Tradeoff |
|--------|----------|----------|
| **Ads Manager "Zakelijke media" UI** | One-off uploads, bulk drops | Manual; see PATH E for bulk flow |
| **Canva export** | Assets designed in Canva | Use a direct link to the exported file, not a page that shows the design (PATH A) |
| **Google Drive direct link** | Files already in your Drive | Needs the `?export=download` trick (below) |
| **Dropbox direct link** | Files in Dropbox | Swap `?dl=0` for `?dl=1` |
| **Cloudinary (free tier)** | Programmatic pipelines, auto-optimization | Requires account; free plan has 25 monthly credits |
| **S3 presigned URL / Cloudflare R2** | Agency / team automation | Requires AWS or CF account; best for scale |
| **WeTransfer / SmashTransfer** | **Don't** | Transfer links are not direct file links (PATH A); unreliable |

### Google Drive direct link trick

Google Drive's normal share link opens a viewer page, not the file, so the server-side fetch fails on it. You need to convert it.

1. In Drive, right-click the file → Share → set to "Anyone with the link"
2. Copy the share link — it looks like:
   ```
   https://drive.google.com/file/d/1A2B3C4D5E6F/view?usp=sharing
   ```
3. Extract the file ID: `1A2B3C4D5E6F`
4. Build the direct-download URL:
   ```
   https://drive.google.com/uc?export=download&id=1A2B3C4D5E6F
   ```
5. Use this URL in `image_url` / `video_url`.

**Known issue:** Google Drive does not virus-scan files over 100 MB (Google Drive Help, "Learn how we help keep Google Drive secure": https://support.google.com/drive/answer/141702). If the direct link opens a warning page instead of the file, the upload fails. For large videos, use Dropbox, S3, or Cloudinary instead.

### Dropbox direct link trick

1. In Dropbox, right-click → Share → Copy link
2. You get:
   ```
   https://www.dropbox.com/scl/fi/abcdef/video.mp4?rlkey=xyz&dl=0
   ```
3. Change `dl=0` → `dl=1`:
   ```
   https://www.dropbox.com/scl/fi/abcdef/video.mp4?rlkey=xyz&dl=1
   ```
4. Use this URL. (`dl=1` forces a download: Dropbox Help, "How to force a shared link to download or render", https://help.dropbox.com/share/force-download, updated 30 June 2025.)

### Cloudinary (recommended for programmatic flows)

Free plan: 25 monthly credits; one credit covers 1,000 transformations, 1 GB of managed storage or 1 GB of image bandwidth (Cloudinary pricing page, https://cloudinary.com/pricing, read 10 October 2026). Upload via their API, get a stable `https://res.cloudinary.com/...` URL, and pass it to the tool. Also handles image format conversion and video transcoding if needed.

### S3 presigned URL (recommended for agencies)

```bash
aws s3 cp video.mp4 s3://your-bucket/ads/
aws s3 presign s3://your-bucket/ads/video.mp4 --expires-in 3600
```

Set the expiry to cover the upload call; the example uses one hour.

## PATH E — Bulk upload via Ads Manager UI (manual route)

You have a folder with 50+ creatives. Avoid one-at-a-time uploads.

**Flow:**

1. Go to Ads Manager → Ad Account → **Media Library** (NL: "Zakelijke media" voor media op businessniveau, **"Media op advertentieaccountniveau"** voor account-media)
2. Drag-drop the whole folder
3. Wait until Meta has processed the files (Meta processes videos asynchronously)
4. Come back to Claude:
   ```python
   meta_query(account_id="act_...", entity_type="adimages", limit=250, format="full")
   ```
   (follow `paging.next` with `pagination_url` if the library is larger)
5. Claude picks the right `hash` per placement using `aspect_ratio_bucket` (PATH B).

**Why not the Business Media Library at business level?** The Ad Superpowers tools read only the ad account's library (`meta_query` with `adimages` / `advideos`), so put the files there.

## Filename-Based Aspect Ratio Matching

When a campaign has multiple aspect ratios of the same creative (one per placement), Claude should match filenames intelligently rather than inspect every asset pixel-by-pixel. This section defines the patterns Claude should recognize. **This is interpretation-driven, not deterministic** — use judgment when a filename is ambiguous, fall back to `aspect_ratio_bucket` (post-upload, from `meta_query(adimages)`) as ground truth.

### Recognized Patterns (per aspect ratio)

**1:1 — Square (feed, carousel):**
- Explicit separators: `1x1`, `1X1`, `1-1`, `1_1`, `1.1`, `1:1`
- Compact codes: `11` (when clearly a ratio code in context, not a version number or year)
- Keywords: `square`, `sq`, `feed-square`, `ig-square`
- Resolution fingerprint: `1080x1080`, `1200x1200`, any `NxN` where N == N

**9:16 — Vertical (Stories, Reels):**
- Explicit separators: `9x16`, `9X16`, `9-16`, `9_16`, `9:16`, `9.16`
- Compact codes: `916`
- Keywords: `vertical`, `vert`, `portrait`, `story`, `stories`, `reel`, `reels`, `full-screen`, `fullscreen`
- Resolution fingerprint: `1080x1920`, `720x1280`, any `NxM` where M/N ≈ 1.78 (ratio 0.55 to 0.58, the tool's 9:16 bucket)

**4:5 — Mobile feed (Instagram + Facebook):**
- Explicit separators: `4x5`, `4X5`, `4-5`, `4_5`, `4:5`, `4.5`
- Compact codes: `45` (when clearly a ratio code, not a year/version)
- Keywords: `mobile-feed`, `mobile`, `feed-mobile`, `ig-feed-mobile`, `portrait-feed`
- Resolution fingerprint: `1080x1350`, `1200x1500`, any `NxM` where M/N ≈ 1.25 (ratio 0.78–0.82)

**16:9 — Landscape (video feed, in-stream):**
- Explicit separators: `16x9`, `16X9`, `16-9`, `16_9`, `16:9`, `16.9`
- Compact codes: `169`
- Keywords: `horizontal`, `horiz`, `landscape`, `wide`, `widescreen`, `in-stream`, `instream`
- Resolution fingerprint: `1920x1080`, `1280x720`, any `NxM` where N/M ≈ 1.78 (ratio 1.76 to 1.80, the tool's 16:9 bucket)

**1.91:1 — Link preview (open-graph style, right-column):**
- Explicit separators: `1.91x1`, `1.91-1`, `1.91_1`, `1.91:1`, `1_91x1`, `1p91x1`
- Compact codes: `1911` (rare but unambiguous in a ratio context)
- Keywords: `link`, `preview`, `og`, `banner`, `right-column`, `og-image`
- Resolution fingerprint: `1200x628`, `1080x566`, any `NxM` where N/M ≈ 1.91 (ratio 1.88 to 1.94, the tool's 1.91:1 bucket)

### Interpretation Rules

1. **Explicit ratio tokens beat compact codes.** If a filename has `1x1`, read that — don't also try to interpret the `1080x1080` tail as `10801080`.
2. **Resolution > compact code when both present.** `hero_1080x1920.jpg` → 9:16 (from dims), even if the name doesn't carry a keyword.
3. **Keywords beat compact codes.** `spring_story_final.mp4` → 9:16 (from `story`), don't try to read `storyfinal` as a ratio.
4. **Compact codes need ratio context.** `v11.jpg` is a version number. `hero_v2_11.jpg` at first glance could be version 11 — but if the sibling file is `hero_v2_916.jpg`, the `_11` is very likely a 1:1 marker. Look at siblings and naming conventions within the same folder before deciding.
5. **Year-like and version-like numbers are NOT ratios.** `campaign_2026_hero.jpg` → not a ratio. `hero_v9.jpg` → not 9:16.
6. **When ambiguous, check post-upload.** `meta_query(account_id, "adimages", since="...")` returns `aspect_ratio_bucket` derived from the actual pixel dimensions — that's ground truth. Use it to reconcile.
7. **Prefer multiple variants over guessing.** If the user has 3 files like `hero_1x1.jpg`, `hero_9x16.jpg`, `hero_4x5.jpg`, use all three: bundle them into one ad with `placement_assets` (Recipe 5), or build one ad per ratio when the copy differs, rather than picking one and forcing it into all placements.

### Placement → ratio mapping (Meta 2026)

| Placement | Recommended ratio | Also accepted |
|-----------|-------------------|---------------|
| Facebook Feed | 4:5 | 1:1, 1.91:1, 16:9 (desktop shows feed video at 1:1) |
| Instagram Feed | 4:5 (image), 9:16 (video) | 1:1, 1.91:1, 16:9, 2:3 |
| Instagram Stories / Reels | 9:16 | 4:5, 1:1, 16:9, 1.91:1 (Reels also 2:3) |
| Facebook Stories / Reels | 9:16 | 4:5, 1:1, 16:9, 1.91:1 (Reels also 2:3) |
| Facebook Right Column | 1.91:1 | 1:1 (the Ads Guide page recommends 1:1) |
| Facebook Marketplace | 1:1 | 16:9, 9:16 |
| Facebook search results | none marked | 1.91:1, 1:1, 9:16 |
| Audience Network (native, banner, interstitial) | none marked | 16:9, 4:5, 9:16 |
| Facebook in-stream video | 16:9 or 1:1 (video, Ads Guide) | 1.91:1 to 1:1 (image, Ads Guide) |
| Threads | none marked | 1.91:1, 16:9, 1:1, 4:5, 2:3, 9:16 |

Source: Meta Business Help Center, "Aspect ratios supported by placements in Meta
Ads Manager" (read
10 October 2026; the page shows no date), and the Meta Ads Guide pages for
in-stream video and the right column (https://www.facebook.com/business/ads-guide/update).
Neither lists Messenger inbox. Meta changes these pages; check them before you
produce creative.

### Example — Claude picks assets for a multi-placement campaign

Given a folder with:
```
hero_1x1_1080x1080.jpg      → 1:1 (explicit + dims)
hero_9x16_1080x1920.jpg     → 9:16 (explicit + dims)
hero_4x5_1080x1350.jpg      → 4:5 (explicit + dims)
hero_story_1080x1920.mp4    → 9:16 (keyword + dims)
hero_169_1920x1080.mp4      → 16:9 (compact + dims)
```

A campaign targeting "feed + stories + in-stream" has two paths:

**Preferred — one ad, multiple assets via `placement_assets`:**
```python
# Upload all variants first (Recipe 5), then one meta_create_ad call:
meta_create_ad(
    ...,
    image_hash="<1x1 hash>",        # primary fallback
    placement_assets=[
        {"image_hash": "<9x16 hash>",
         "placements": ["instagram_stories", "facebook_stories", "instagram_reels"]},
        {"image_hash": "<4x5 hash>",
         "placements": ["instagram_feed", "facebook_feed"]},
    ],
)
# + a separate video ad for in-stream if the format is video:
meta_create_ad(..., video_id="<16:9 video_id>", adset_id="<video-specific adset>")
```

**Fallback — separate ads when bundling is impossible** (different copy per ratio, mixed image+video within one ad):
- Ad #1 with `hero_1x1` (feed placement)
- Ad #2 with `hero_9x16` (Stories / Reels, image)
- Ad #3 with the `hero_story` video (Stories / Reels, video; one media type per ad)
- Ad #4 with `hero_169` (in-stream video)

Do NOT try to stretch a 1:1 asset across Stories placement. Meta's placement optimization may still deliver it, but the creative won't look native.

## Troubleshooting

### "URL fetch failed" / "Image download failed"

- **Open the URL in an incognito browser window.** If you see a login wall, virus warning, or preview page (not the raw file), the server-side fetch fails too.
- Google Drive: did you use the `?export=download` trick? Does the link open a warning page instead of the file (if yes, switch to Dropbox / S3)?
- Dropbox: did you change `?dl=0` → `?dl=1`?
- Signed URLs: has the link expired before the upload call ran?
- CDN: some CDNs refuse requests that do not come from a browser. Image URLs are fetched by the Ad Superpowers server and video URLs by Meta, so use a URL the CDN does not gate on the user agent.

### "Unsupported format"

- Images: Meta's Ads Guide lists JPG or PNG, and private staging accepts only JPEG and PNG. Convert WebP or HEIC first (`sips -s format jpeg image.heic --out image.jpg` on Mac).
- Videos: Meta's Ads Guide lists MP4, MOV or GIF; private staging accepts MP4 (H.264, optional AAC) only. Convert other formats with ffmpeg: `ffmpeg -i input.mkv -c:v libx264 -c:a aac output.mp4`.

### "Video file too short" or "too long"

- Meta's Ads Guide lists 1 second to 241 minutes for Facebook Feed video.
- Other placements are stricter: Instagram Feed video runs up to 60 minutes, and Facebook in-stream video needs at least 5 seconds (up to 10 minutes on mobile, 15 seconds on desktop; Meta notes the limit can vary by objective). Private staging accepts 1 to 1,800 seconds. Check the current Ads Guide page for the placement.

### "Image resolution too low"

- Meta's Ads Guide sets image minimums per placement: 600 pixels wide for Facebook Feed (750 high at 4:5) and Facebook Reels; 500 pixels wide for Instagram Feed, Instagram Stories, Instagram Reels and Facebook Stories.
- Recommended: 1440 x 1800 for 4:5 feed images and 1440 x 2560 for 9:16 Stories and Reels.
- 120 x 120 pixels is the Ads Guide minimum for Facebook Feed video, not for images.

### "Meta shows the old version of my image"

- Check that the ad uses the new `image_hash`, not the one from the earlier upload.
- If you overwrote a file at the same URL, the host or its CDN may still serve the cached old file.
- **Fix:** rename the file OR add a cache buster (`?v=2` at the end of the URL) OR upload to a new URL entirely.

### "image_hash invalid" when reusing across accounts

- An image belongs to the ad account it was uploaded to: Meta's Ad Image reference names the owning `account_id` and offers a separate `copy_from` call to copy an image to another account. No Ad Superpowers tool exposes that call, so a hash from `act_111` will not work in `act_222`.
- **Fix:** upload the file to the target account as well. Do the same for videos.

### "Claude Desktop says it can't upload local files"

For local JPEG/PNG within the returned policy, use PATH C if `assets_stage` and
local shell access are available. Do not paste base64 as the default workaround.
Without that combination use a small legacy inline input, an approved existing
URL, or manual Ads Manager upload. Local video remains on PATH D.

### "I uploaded a video 2 minutes ago but `meta_query(advideos)` doesn't show it"

- A new upload may not appear in this list right away. Wait and retry, or fetch the specific video directly via `meta_get_video_status(video_id=...)`.

## Quick Workflow Recipes

### Recipe 1 — Single image ad from Canva URL (URL route)

```
1. Export the design from Canva as JPG or PNG. Use a direct HTTPS link to that
   file (it must pass the PATH A checks; a page that shows the design is not
   enough), or stage the downloaded file instead (Recipe 2).
2. Claude: meta_create_ad(
     account_id="act_...",
     adset_id="...",
     headline="...", body="...", link_url="https://...",
     image_url="<direct link to the exported file>",
   )
```

### Recipe 2 — Single image from a local file on disk

Follow PATH C: local SHA/size → assets_stage → curl PUT →
meta_upload_image(stage_id=..., name=...). Reuse the returned image_hash in a
separately authorized meta_create_ad call. Use the legacy inline fallback only
when staging is unavailable and context cost is acceptable.

### Recipe 3 — Single video ad from a local file

Follow PATH D: local size/SHA → video `assets_stage` → private client PUT →
`meta_upload_video(stage_id=..., title=...)` → explicit same-stage `action="status"`.
Keep the account and title unchanged. Reuse the returned `video_id` only after
readiness is observed and ad creation is separately authorized. An uncertain
upload must not be automatically repeated or restaged.

### Recipe 4 — Reuse a Stories-shaped asset from last week (reuse existing asset)

```
1. meta_query(account_id, "adimages", since="2026-04-13")
2. Pick the item with aspect_ratio_bucket == "9:16" and the right name
3. meta_create_ad(..., image_hash=<that hash>)
```

### Recipe 5 — Multi-ratio campaign from a folder of local images

**Preferred**: bundle all aspect ratios into ONE ad via `placement_assets`. This matches how Ads Manager "Customize media" works, keeps one ad ID across placements (post engagement retention is unverified), and takes one `meta_create_ad` call instead of three or four.

```
User provides a folder:
  /ads/spring/
    hero_1x1_1080x1080.jpg
    hero_4x5_1080x1350.jpg
    hero_9x16_1080x1920.jpg
    hero_1.91x1_1200x628.jpg

Claude reads filenames, applies Filename Matching rules:
  hero_1x1_*    → 1:1  (feed, carousel — primary/default)
  hero_4x5_*    → 4:5  (Facebook and Instagram feeds)
  hero_9x16_*   → 9:16 (Stories, Reels)
  hero_1.91x1_* → 1.91:1 (right column, search)

Step 1 — upload variants with the PATH C window/manifest:
  local size/SHA → assets_stage → curl PUT → meta_upload_image(stage_id, name)
  → collect one destination image_hash per variant; never send folder base64

Step 2 — create ONE ad with placement_assets bundling all variants:
  meta_create_ad(
      account_id=account_id,
      adset_id="...",
      headline="Spring launch",
      body="...",
      link_url="https://...",
      image_hash="<1x1 hash>",   # primary fallback (1:1 is listed for most placements)
      placement_assets=[
          {"image_hash": "<9x16 hash>",
           "placements": ["instagram_stories", "facebook_stories",
                          "instagram_reels", "facebook_reels"]},
          {"image_hash": "<4x5 hash>",
           "placements": ["instagram_feed", "facebook_feed",
                          "audience_network"]},
          {"image_hash": "<1.91x1 hash>",
           "placements": ["facebook_right_column", "facebook_search"]},
      ],
      status="PAUSED",
  )

Meta serves the right ratio per placement automatically. One ad, one
creative_id, one engagement post across placements.
```

**When to split into multiple ads instead of using `placement_assets`:**
- Headlines or body copy differ per ratio → can't bundle, each ad needs its own copy
- Mix of image and video per placement → `meta_create_ad` takes one media type per ad and refuses a mix before it calls Meta
- A/B testing different creative concepts (not just different ratios of the same concept)

### Placement_assets quick reference (2026-supported placements)

| Placement name | Meta platform + position | Ratios Meta lists |
|----------------|-------------------------|-------------------|
| `facebook_feed` | facebook / feed | 4:5 (recommended), 1:1, 1.91:1, 16:9 |
| `facebook_stories` | facebook / story | 9:16 (recommended), 4:5, 1:1, 16:9, 1.91:1 |
| `facebook_reels` | facebook / facebook_reels | 9:16 (recommended); all six ratios listed |
| `facebook_marketplace` | facebook / marketplace | 1:1 (recommended), 16:9, 9:16 |
| `facebook_right_column` | facebook / right_hand_column | 1.91:1, 1:1 |
| `facebook_in_stream` | facebook / instream_video | 16:9 or 1:1 (video); 1.91:1 to 1:1 (image) |
| `facebook_video_feeds` | facebook / video_feeds | 1.91:1 to 4:5 (image) |
| `facebook_search` | facebook / search | 1.91:1, 1:1, 9:16 |
| `instagram_feed` | instagram / stream | 4:5 (image), 9:16 (video); also 1:1, 1.91:1, 16:9, 2:3 |
| `instagram_stories` | instagram / story | 9:16 (recommended), 4:5, 1:1, 16:9, 1.91:1 |
| `instagram_reels` | instagram / reels | 9:16 (recommended); all six ratios listed |
| `instagram_profile_feed` | instagram / profile_feed | not in Meta's ratio table |
| `messenger_inbox` | messenger / messenger_home (see note) | not in Meta's ratio table |
| `audience_network` | audience_network / classic | 16:9, 4:5, 9:16 (native, banner, interstitial) |
| `threads` | threads / feed (see note) | all six ratios listed, none marked |

Ratios come from the sources under the ratio table above.

Meta's placement asset customization guide lists no Reels position for
`customization_spec`, and its options list has `instream_video` only for
Audience Network (Marketing API, "Placement Asset Customization").
When you map `facebook_reels`, `instagram_reels` or `facebook_in_stream`, check
the ad's preview for those placements in Ads Manager before you set it to ACTIVE.

**Retired by Meta in Marketing API v26.0 (released 29 July 2026):** the Instagram
Explore Feed placement and Messenger Stories. Meta's changelog says requests that
name Explore return an error, and that the Messenger `story` position is removed
silently from v26.0 calls (and from calls on every API version from 27 October
2026), so such an ad is accepted but never delivers there. The tool refuses the
Instagram Explore, Instagram Explore home and Messenger Stories placement names
with an error that says why. Use `instagram_stories` and `facebook_stories` for
9:16 reach instead. Source: Graph API changelog, Version 26.0.

**Two names to avoid for now.** `messenger_inbox` maps to the `messenger_home`
position, which Meta's placement-targeting reference does not list (it lists
`sponsored_messages` and `story` for Messenger). `threads` maps to position
`feed`, while Meta documents `threads_positions: ["threads_stream"]` and requires
the Instagram `stream` placement alongside it. Do not map these two in
`placement_assets`; the catch-all primary asset covers the placements you leave
unmapped. Source: Marketing API placement targeting reference.

### How `placement_assets` builds the creative (under the hood)

`meta_create_ad` turns your `placement_assets` into a Meta `asset_feed_spec` with
placement `asset_customization_rules`. You never write this by hand, but knowing the
shape helps when you debug a rejected creative:

- The primary `image_hash` / `video_id` becomes the **catch-all fallback**: a rule with
  an empty `customization_spec` that covers every placement you did not map explicitly.
  Always pass a primary (a 1:1 or 4:5 asset; Meta's table lists each for most placements).
- Each `placement_assets` entry becomes one rule that targets its `placements`.
- Every asset carries an `adlabels` tag, and its rule points at that label by name, so
  Meta knows which asset belongs to which placement. That linkage is what makes the
  feature work. A rule that points at a label no asset carries makes Meta reject the
  creative.
- `ad_formats` is `SINGLE_IMAGE` or `SINGLE_VIDEO` (`CAROUSEL_IMAGE` for a carousel). One
  media type per ad: the tool refuses a mix of image and video before it calls Meta.

**Typos fail loud.** An unknown placement name (for example `instragram_stories`) now
raises a clear `Unknown placement` error that lists the valid names, instead of being
dropped silently. Check the placement against the quick-reference table above.

### placement_assets ≠ Dynamic Creative

A frequent mix-up. `placement_assets` builds an `asset_feed_spec` with placement `asset_customization_rules` — but that is **placement customization**, not Dynamic Creative, and it runs on a **standard** ad set. You do not need (and should not turn on) Dynamic Creative to use `placement_assets`.

Dynamic Creative is a different thing: an ad set created with `is_dynamic_creative=true`, where Meta auto-optimizes across multiple text/asset variants (`body_variants`). If you pass two or more `body_variants` to an ad on a *standard* ad set, `meta_create_ad` checks the ad set first and stops with an error ("body_variants needs a Dynamic Creative ad set") before it creates anything. So decide up front: one message shown well per placement → `placement_assets` on a standard ad set; multiple variants for Meta to optimize → a Dynamic Creative ad set. Meta's Help Center says that since June 2024 dynamic creative may be unavailable for new sales or app promotion ad sets in Ads Manager ("About dynamic creative in Meta Ads Manager"); if Meta rejects `is_dynamic_creative=true`, create separate ads instead. The end-to-end decision lives in `ad-launch-playbook`.

### Recipe 6 — Bulk drop 50+ creatives via Ads Manager (manual route)

```
1. Ads Manager → Media Library → drag whole folder → wait for processing
2. Claude: meta_query(account_id, "adimages", limit=250, format="full")
   (format="full" keeps hash and aspect_ratio_bucket on every row of this
   page; pages fetched with pagination_url come back raw, without
   aspect_ratio_bucket)
3. Claude groups by aspect_ratio_bucket, cross-references filenames via
   the Filename Matching rules, picks per placement, builds ads
   (one meta_create_ad per ad, run sequentially — the server mirrors Meta's
   rate limits; if Meta throttles, the error says so).
```

## Integration Points

**Tools used by this skill:**
- `assets_stage` — reserve a private, bound JPEG/PNG or MP4 upload when available
- `meta_upload_image` — finalize stage_id (preferred for local files), legacy base64 or public URL; returns image_hash
- `meta_create_ad` — build image or video ads with hash or URL; supports `placement_assets` for multi-aspect-ratio bundling (one ad serves different variants per placement via Meta's asset_customization_rules)
- `meta_upload_video` — finalize a private video stage and explicitly check it with `action="status"`; also supports the existing URL route
- `meta_get_video_status` — inspect a video ID from the existing URL/manual route
- `meta_query(adimages)` — discover existing image library with `aspect_ratio_bucket` enrichment
- `meta_query(advideos)` — discover existing video library with dimension derivation

**Complementary skills:**
- `ad-launch-playbook` — the end-to-end campaign → ad set → ads runbook; calls this skill for the media step
- `meta-ad-copy-generator` — write the copy first, then use this skill for the media
- `meta-creative-diversification-generator` — plan the creative matrix first, then use this skill per concept
- `meta-video-script-writer` — script the video first, then choose an authorized upload route

**Account integrity reminder:** every `meta_create_ad` call is a write. The server's protection stack mirrors Meta's documented rate model and backs off on Meta's throttle signals — there is **no artificial hourly cap**, while staged media uses the bounded window and capacity hints above. If a call returns a throttle error, back off and resume where you left off.

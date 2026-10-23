---
name: meta-capi-implementation-guide
description: "This skill should be used when the user asks to \"set up CAPI\", \"implement server-side tracking\", \"configure event deduplication\", or mentions \"Conversions API\", \"CAPI Gateway\", or \"CAPI troubleshooting\". Do NOT use for: EMQ optimization specifically (use emq-optimizer), attribution window decisions (use attribution-window-advisor), pixel-only tracking issues (use performance-troubleshooter)."
---
# CAPI Implementation Guide

Guide for implementing Meta's Conversions API (CAPI) for server-side tracking. Meta recommends using CAPI in addition to the Meta Pixel and sharing the same events through both: CAPI can deliver website events the Pixel may lose to network connectivity issues or page loading errors. How many events the Pixel misses differs per site, so measure it (browser versus server event counts in Events Manager) instead of assuming a percentage. Meta's Conversions API docs typically recommend aiming for an Event Match Quality (EMQ) score of **6.0** or higher where possible.

Sources: "Best Practices" and "Verifying Your Setup", Conversions API docs, Meta for Developers (checked 2026-10-10).

## Why Use CAPI Next to the Pixel

```
Browser Tracking Challenges:
├── iOS 14.5+ App Tracking Transparency
├── Safari ITP (Intelligent Tracking Prevention)
├── Ad blockers
├── Third-party cookie blocking (Chrome leaves this to the user)
└── GDPR/privacy regulations

CAPI Benefits:
├── Sends events the Pixel may lose (network issues, page load errors)
├── First-party data direct to Meta
├── Better Event Match Quality
├── Redundant tracking (Pixel + CAPI)
└── More accurate attribution
```

Chrome: Google keeps its current approach of offering users a third-party cookie choice in Chrome's settings and
will not roll out a standalone prompt ("Next steps for Privacy Sandbox and tracking protections in Chrome",
Google, 22 Apr 2025, https://privacysandbox.google.com/blog/privacy-sandbox-next-steps).

## Implementation Decision Tree

```
WHAT IS YOUR PLATFORM?
│
├─► Shopify
│   └─► Native Shopify integration
│
├─► WooCommerce
│   └─► Plugin or sGTM
│
├─► BigCommerce / Magento
│   └─► Partner integration
│
├─► Custom Website
│   └─► Direct API or sGTM
│
└─► Any Platform + GTM
    └─► Server-side GTM
```

## Implementation Methods

### Method 1: Platform Native Integration

**Shopify (Recommended for Shopify users)**

```
Setup Steps:
1. Shopify Admin → Settings → Apps and Sales Channels
2. Install Meta (Facebook & Instagram) app
3. Connect Meta Business Account
4. Facebook & Instagram → Settings → Data sharing settings → Maximum
5. Verify in Events Manager

Skill level: Beginner
```

Shopify's "Enhanced" and "Maximum" data-sharing levels use the Conversions API next to the Pixel; "Standard" is
Pixel only (Shopify Help Center, Meta pixel data sharing,
https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/meta-data-sharing, checked 2026-10-10).

**WooCommerce**

```
Option A: Meta for WooCommerce plugin (formerly Facebook for WooCommerce)
1. Install the plugin from the WordPress.org plugin directory
2. Connect it to your Meta business account (Marketing → Facebook)
3. Conversions API events are sent automatically (no extra setting)
4. Configure event settings

Option B: Third-party plugin (PixelYourSite, etc.)
- More configuration options
- Better deduplication control
- Premium features for advanced setup
```

Option A source: "Meta for WooCommerce" on WordPress.org (https://wordpress.org/plugins/facebook-for-woocommerce/)
and the WooCommerce documentation, which says the Conversions API "is automatically implemented and no additional
setting is required" (https://woocommerce.com/document/facebook-for-woocommerce/, checked 2026-10-10).

### Method 2: Server-side GTM (sGTM)

**When to use sGTM:**
- Custom website
- Need more control
- Multi-platform tracking
- Enterprise setups

**Setup Overview:**

```
Architecture:
Browser → GTM Web Container → sGTM Server Container → Meta CAPI

Requirements:
├── Google Cloud account (or other hosting)
├── Custom domain (tracking.yourdomain.com)
├── GTM Web Container
├── GTM Server Container
└── Meta System User Access Token
```

**sGTM Setup Steps:**

```
1. Server Container Setup
   ├── Create sGTM container in GTM
   ├── Deploy to Google Cloud Run (Google's recommended setup)
   ├── Configure custom domain (CNAME record)
   └── Hosting cost: Google estimates about $45/month (USD) per server and recommends at least 2 to reduce the risk of data loss

2. Web Container Configuration
   ├── Update GA4 tag to send to server container
   ├── Add Meta Pixel tag (browser side of the redundant setup)
   └── Set server_container_url to the sGTM URL

3. Server Container Tags
   ├── Add Meta's "Conversions API Tag" (Template Gallery)
   ├── Configure event mappings
   ├── Add customer information parameters
   └── Setup event_id for deduplication

4. Testing
   ├── Use GTM Preview mode
   ├── Verify in Events Manager Test Events
   └── Check deduplication working
```

Sources: "Set up server-side tagging with Cloud Run" (Google for Developers, updated 2026-05-12) for hosting and cost;
"An introduction to server-side tagging"
for `server_container_url`; "Conversions API for Server-Side Google Tag Manager (GTM)", Meta for Developers for the tag template.

### Method 3: Conversions API Gateway

**Meta's self-serve gateway, hosted in your cloud account or by a hosting partner:**

```
Benefits:
├── Codeless setup
├── Runs in your own cloud account (AWS or GCP) or a partner's
├── Automatic updates (with host admin consent)
└── Simplified maintenance

Hosting options:
├── Your own AWS account (setup wizard in Events Manager)
├── Your own GCP account
└── A hosting partner, for example Stape (partner fees)

Steps:
1. Events Manager → Data Sources → Pixel
2. Settings → "Set up with Conversions API Gateway" → Get started
3. Follow the setup wizard (cloud setup, hosting region)
4. Add a custom domain at your DNS provider (recommended)
5. Verify connection
```

Source: "Conversions API Gateway" and its setup guide, Meta for Developers
(checked 2026-10-10).
Meta: "The only cost of the Conversions API Gateway is the associated cloud resource or partner fees." Stape
describes its gateway hosting as "a server instance in the GCP cloud environment"
(https://stape.io/blog/how-to-set-up-meta-conversions-api-gateway, updated 4 Aug 2025).

### Method 4: Direct API Implementation

**For developers / custom solutions:**

```python
# Example: Direct CAPI call (Python)
import requests
import hashlib
import time

def send_capi_event(event_name, email, event_id, value=None):
    access_token = "YOUR_ACCESS_TOKEN"
    pixel_id = "YOUR_PIXEL_ID"

    # Hash user data (Meta's rule for em: trim spaces, lowercase, then SHA-256)
    hashed_email = hashlib.sha256(email.strip().lower().encode()).hexdigest()

    payload = {
        "data": [{
            "event_name": event_name,
            "event_time": int(time.time()),  # Unix seconds; Meta rejects a request with any event older than 7 days
            "event_id": event_id,  # For deduplication
            "event_source_url": "https://yoursite.com/thank-you",
            "action_source": "website",
            "user_data": {
                "em": [hashed_email],
                "client_ip_address": "user_ip",
                "client_user_agent": "user_agent"
            },
            "custom_data": {
                "currency": "EUR",
                "value": value
            }
        }],
        "access_token": access_token
    }

    # v25.0: Marketing API version of 18 Feb 2026; check the current one in the
    # Marketing API changelog (Meta for Developers).
    url = f"https://graph.facebook.com/v25.0/{pixel_id}/events"
    response = requests.post(url, json=payload)
    return response.json()
```

Website events must include `event_source_url` and `client_user_agent`, as above ("Server Event Parameters" and
"Customer Information Parameters", Meta for Developers).

## Event Deduplication

### Why Deduplication Is Crucial

Without deduplication: Pixel event + CAPI event = 2x conversions (double counting)

### Deduplication Setup

```
Requirement: Same event_id and event_name for both Pixel AND CAPI event

Pixel Event:
fbq('track', 'Purchase', {value: 50, currency: 'EUR'}, {eventID: 'order_12345'});

CAPI Event:
{
  "event_name": "Purchase",
  "event_id": "order_12345",  // MUST MATCH
  "custom_data": {"value": 50, "currency": "EUR"}
}

Meta's Logic:
├── Same event_name + event_id within 48 hours?
├── → Treated as 1 event (Meta generally keeps the first one received)
└── → No double counting
```

Source: "Handling Duplicate Pixel and Conversions API Events" and "Server Event Parameters", Meta for Developers
(checked
2026-10-10). Meta can also deduplicate on event_name plus fbp and/or external_id, but generally only when the
browser event arrives first.

### Event ID Best Practices

```
Good Event IDs:
├── Order ID: "order_12345"
├── Transaction ID: "txn_abc123"
├── UUID: "550e8400-e29b-41d4-a716-446655440000"
└── Composite: "purchase_user123_1642345678"

Bad Event IDs:
├── Random value made separately in browser and server (never matches)
├── Timestamp only (not unique enough)
├── Missing (no deduplication possible)
└── Hardcoded "1" (all events match)
```

### Verification in Events Manager

```
Checklist for correct deduplication:
□ Go to Events Manager → Pixel → Overview
□ Click on specific event (e.g., Purchase)
□ Connection Method shows the event from both browser and server
□ Event count should NOT be doubled
□ Event Deduplication tab: rate of events deduplicated (Meta warns when too low)

If NOT deduplicated:
├── Check event_id matching
├── Verify timing (within 48 hours)
├── Confirm event_name exact match
└── Review hashing consistency
```

## Prerequisites Checklist

```
BEFORE IMPLEMENTING CAPI:

□ Domain Verification
  └── Business Settings → Brand Safety → Domains → Verify

□ Pixel Installed
  └── CAPI needs the Pixel ID; Meta recommends Pixel + CAPI (redundant setup)

□ Access Token
  └── Events Manager → Settings → Generate Access Token
  └── Use System User token (not personal)

□ SSL/HTTPS
  └── Your website must use HTTPS

□ Data Layer
  └── Properly configured for event data

□ Privacy Policy
  └── Updated to reflect server-side tracking
```

## Troubleshooting

### Common Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| Events not showing | No server events in Events Manager | Check access token, pixel ID, API version |
| Dedup not working | Events doubled | Verify event_id matching |
| Low EMQ | Score <6 | Add more customer parameters |
| 400 errors | API rejection | Check payload format, hashing |
| Token expired | Sudden stop | Use System User token, refresh |

### Debugging Steps

```
STEP 1: Test Events Tool
├── Events Manager → Test Events
├── Send test conversion
├── Check if event appears
└── Review any errors

STEP 2: API Response Check
├── Log API responses
├── Look for error messages
├── Common: "Invalid parameter", "Access denied"

STEP 3: Payload Validation
├── Verify JSON structure
├── Check required fields
├── Confirm hashing (SHA256, lowercase)

STEP 4: Events Manager Diagnostics
├── Check Diagnostics tab
├── Review error rates
├── Identify failing events
```

### Verification Checklist Post-Implementation

```
24 HOURS AFTER GO-LIVE:

□ Server events visible in Events Manager
□ Event Match Quality 6.0+ where possible (Meta's recommendation)
□ Deduplication working (2 sources, 1 count)
□ No errors in Diagnostics
□ Pixel + CAPI both firing
□ Test purchase tracked correctly

7 DAYS AFTER GO-LIVE:

□ EMQ stabilized
□ Conversion volume matches expected
□ No significant errors
□ Attribution looks reasonable
□ ROAS calculation accurate
```

## Platform-Specific Guides

### Shopify Quick Reference

```
Native Integration:
1. Sales channels → Facebook & Instagram → Settings
2. Data sharing settings: Maximum
3. Done (CAPI automatically enabled)

Verify:
- Events Manager shows server events
- Test order triggers Purchase event
```

### WooCommerce Quick Reference

```
With Meta for WooCommerce:
1. WordPress admin → Marketing → Facebook
2. Connect to your Meta business account
3. CAPI runs automatically (no extra setting)
4. Test checkout flow

With PixelYourSite Pro:
1. PixelYourSite Pro → Meta (Facebook)
2. Enter Pixel ID and Conversion API access token
3. Turn on "Enable Conversion API"
4. PYS adds an event_id to each event; with any caching layer, keep both Ajax options in Global Settings → Events delivery on
```

PixelYourSite steps: "Meta (Facebook) settings setup", PixelYourSite documentation
(https://www.pixelyoursite.com/docs/meta-facebook-settings-setup, checked 2026-10-10).

### Custom Site Quick Reference

```
sGTM Route:
1. Setup sGTM on Google Cloud
2. Add Meta's Conversions API Tag
3. Map events from GA4
4. Add customer parameters
5. Setup deduplication

Direct API Route:
1. Generate System User token
2. Implement server-side code
3. Hash all PII (SHA256)
4. Include event_id for dedup
5. Send to Graph API endpoint
```

## MCP: Verify CAPI Health

```python
# Review recent campaign performance — if ROAS looks lower than expected, check EMQ first
meta_get_insights(account_id="act_XXXXX", level="campaign", date_preset="last_7d", fields=["spend","actions","cost_per_action_type","website_purchase_roas"])

# List the account's pixels: last_fired_time, enable_automatic_matching, automatic_matching_fields,
# first_party_cookie_status (the _fbp cookie needs first-party cookies on)
meta_query(account_id="act_XXXXX", entity_type="adspixels")

# EMQ, match keys, deduplication and freshness per web event (pixel id from adspixels)
meta_query(account_id="act_XXXXX", entity_type="dataset_quality", entity_id="<pixel_id>")
# Test events and the full Diagnostics tab stay in Events Manager
# Or: Pull campaign entities for a quick status overview
meta_query(account_id="act_XXXXX", entity_type="campaigns", effective_status=["ACTIVE"], fields=["id","name","status","objective"])
```

## Maintenance

```
MONTHLY CHECKS:
□ EMQ score trending
□ Error rates in Diagnostics
□ Token expiration status
□ Event volumes vs expected
□ Deduplication verification

QUARTERLY:
□ API version update check
□ Platform integration updates
□ Performance optimization
□ Documentation update
```

---
name: capi-implementation-guide
description: "Meta Conversions API (CAPI) implementatie guide en troubleshooting. Gebruik voor: (1) CAPI setup advies per platform, (2) Server-side tracking configuratie, (3) Event deduplicatie setup, (4) CAPI Gateway implementatie, (5) CAPI troubleshooting en debugging. Triggers: CAPI, Conversions API, server-side tracking, event deduplication, CAPI gateway, server events."
---

# CAPI Implementation Guide

Guide voor het implementeren van Meta's Conversions API (CAPI) voor server-side tracking.

## Waarom CAPI Essentieel Is

```
Browser Tracking Uitdagingen:
├── iOS 14.5+ App Tracking Transparency
├── Safari ITP (Intelligent Tracking Prevention)
├── Ad blockers (30%+ gebruikers)
├── Cookie deprecation
└── GDPR/privacy regelgeving

CAPI Voordelen:
├── Bypasses browser beperkingen
├── First-party data direct naar Meta
├── Betere Event Match Quality
├── Redundante tracking (Pixel + CAPI)
└── Meer accurate attribution
```

## Implementation Decision Tree

```
WAT IS JE PLATFORM?
│
├─► Shopify
│   └─► Native Shopify integration (2 uur)
│
├─► WooCommerce
│   └─► Plugin of sGTM (4-8 uur)
│
├─► BigCommerce / Magento
│   └─► Partner integration (2-4 uur)
│
├─► Custom Website
│   └─► Direct API of sGTM (8-40 uur)
│
└─► Any Platform + GTM
    └─► Server-side GTM (4-8 uur)
```

## Implementation Methods

### Method 1: Platform Native Integration

**Shopify (Aanbevolen voor Shopify users)**

```
Setup Stappen:
1. Shopify Admin → Settings → Apps and Sales Channels
2. Meta (Facebook & Instagram) app installeren
3. Connect Meta Business Account
4. Enable "Data Sharing" → Maximum
5. Verify in Events Manager

Tijd: 1-2 uur
Skill level: Beginner
Coverage: ~95% events automatisch
```

**WooCommerce**

```
Optie A: Facebook for WooCommerce Plugin
1. Install plugin van WooCommerce marketplace
2. Connect Facebook account
3. Enable Conversions API checkbox
4. Configure event settings

Optie B: Third-party plugin (PixelYourSite, etc.)
- Meer configuratie opties
- Better deduplication control
- Premium features voor advanced setup
```

### Method 2: Server-side GTM (sGTM)

**Wanneer sGTM gebruiken:**
- Custom website
- Meer controle nodig
- Multi-platform tracking
- Enterprise setups

**Setup Overview:**

```
Architecture:
Browser → GTM Web Container → sGTM Server Container → Meta CAPI

Vereisten:
├── Google Cloud account (of andere hosting)
├── Custom domain (tracking.yourdomain.com)
├── GTM Web Container
├── GTM Server Container
└── Meta System User Access Token
```

**sGTM Setup Stappen:**

```
1. Server Container Setup
   ├── Create sGTM container in GTM
   ├── Deploy to Google Cloud (App Engine)
   ├── Configure custom domain (CNAME record)
   └── Estimated cost: $100-300/month

2. Web Container Configuration
   ├── Update GA4 tag to send to server container
   ├── Add Facebook Pixel tag (browser-side backup)
   └── Configure transport URL to sGTM

3. Server Container Tags
   ├── Add Facebook Conversions API tag
   ├── Configure event mappings
   ├── Add customer information parameters
   └── Setup event_id for deduplication

4. Testing
   ├── Use GTM Preview mode
   ├── Verify in Events Manager Test Events
   └── Check deduplication working
```

### Method 3: Conversions API Gateway

**Meta's Managed Gateway:**

```
Voordelen:
├── Codeless setup
├── Managed infrastructure
├── Automatic updates
└── Simplified maintenance

Setup via Partners:
├── Stape.io (populair, betaalbaar)
├── AWS-hosted gateway
└── Other certified partners

Stappen:
1. Events Manager → Data Sources → Pixel
2. Settings → Conversions API → Gateway
3. Follow partner setup wizard
4. Add CNAME record to DNS
5. Verify connection
```

### Method 4: Direct API Implementation

**Voor developers / custom solutions:**

```python
# Voorbeeld: Direct CAPI call (Python)
import requests
import hashlib
import time

def send_capi_event(event_name, email, event_id, value=None):
    access_token = "YOUR_ACCESS_TOKEN"
    pixel_id = "YOUR_PIXEL_ID"

    # Hash user data
    hashed_email = hashlib.sha256(email.lower().encode()).hexdigest()

    payload = {
        "data": [{
            "event_name": event_name,
            "event_time": int(time.time()),
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

    url = f"https://graph.facebook.com/v18.0/{pixel_id}/events"
    response = requests.post(url, json=payload)
    return response.json()
```

## Event Deduplication

### Waarom Deduplicatie Cruciaal Is

Zonder deduplicatie: Pixel event + CAPI event = 2x conversies (dubbeltelling)

### Deduplication Setup

```
Vereiste: Zelfde event_id voor Pixel EN CAPI event

Pixel Event:
fbq('track', 'Purchase', {value: 50, currency: 'EUR'}, {eventID: 'order_12345'});

CAPI Event:
{
  "event_name": "Purchase",
  "event_id": "order_12345",  // MOET MATCHEN
  "custom_data": {"value": 50, "currency": "EUR"}
}

Meta's Logic:
├── Zelfde event_name + event_id binnen 48 uur?
├── → Behandel als 1 event
└── → Geen dubbeltelling
```

### Event ID Best Practices

```
Goede Event IDs:
├── Order ID: "order_12345"
├── Transaction ID: "txn_abc123"
├── UUID: "550e8400-e29b-41d4-a716-446655440000"
└── Composite: "purchase_user123_1642345678"

Slechte Event IDs:
├── Random per pageload (niet reproduceerbaar)
├── Timestamp only (niet uniek genoeg)
├── Missing (geen deduplicatie mogelijk)
└── Hardcoded "1" (alle events matchen)
```

### Verification in Events Manager

```
Checklist voor correcte deduplicatie:
□ Ga naar Events Manager → Pixel → Events
□ Klik op specifiek event (bijv. Purchase)
□ Check "Event Source": moet tonen "Received from 2 sources"
□ Event count moet NIET verdubbeld zijn
□ "Deduplicated" indicator zichtbaar

Als NIET deduplicated:
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
  └── Working browser-side pixel required for redundancy

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

| Issue | Symptoom | Oplossing |
|-------|----------|-----------|
| Events not showing | No server events in Events Manager | Check access token, pixel ID, API version |
| Dedup not working | Events verdubbeld | Verify event_id matching |
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
□ Event Match Quality >6 (ideally >7)
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
1. Settings → Apps → Meta
2. Data Sharing: Maximum
3. Done (CAPI automatisch enabled)

Verify:
- Events Manager shows server events
- Test order triggers Purchase event
```

### WooCommerce Quick Reference

```
With Facebook for WooCommerce:
1. WooCommerce → Marketing → Facebook
2. Advanced Settings → Enable Conversions API
3. Enter Access Token
4. Test checkout flow

With PixelYourSite Pro:
1. Settings → Conversions API
2. Enter Access Token
3. Enable "Send server events"
4. Configure deduplication
```

### Custom Site Quick Reference

```
sGTM Route:
1. Setup sGTM on Google Cloud
2. Add Facebook CAPI tag
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

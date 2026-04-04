### TikTok Ads

```
TIKTOK ADS UTM CONFIGURATION
==============================

WHERE TO CONFIGURE:
├── TikTok Ads Manager → Ad → URL → Tracking Parameters
├── Or: Bulk upload via TikTok Ads API

RECOMMENDED TEMPLATE:
utm_source=tiktok
&utm_medium=paid-social
&utm_campaign=__CAMPAIGN_NAME__
&utm_content=__AID_NAME__
&utm_term=__AID__

DYNAMIC PARAMETERS TIKTOK:
┌─────────────────────────┬────────────────────────────────────┐
│ Parameter               │ What it contains                   │
├─────────────────────────┼────────────────────────────────────┤
│ __CAMPAIGN_NAME__       │ Campaign name                      │
│ __CAMPAIGN_ID__         │ Campaign ID                        │
│ __ADGROUP_NAME__        │ Ad group name                      │
│ __ADGROUP_ID__          │ Ad group ID                        │
│ __AID_NAME__            │ Ad name                            │
│ __AID__                 │ Ad ID                              │
│ __PLACEMENT__           │ Placement (TikTok, Pangle, etc.)   │
│ __CREATIVE_ID__         │ Creative ID                        │
└─────────────────────────┴────────────────────────────────────┘

ADVANCED TEMPLATE (with IDs for debugging):
utm_source=tiktok
&utm_medium=paid-social
&utm_campaign=__CAMPAIGN_NAME__-__CAMPAIGN_ID__
&utm_content=__AID_NAME__
&utm_term=__ADGROUP_NAME__

TIKTOK PIXEL:
─────────────
In addition to UTM, install TikTok Pixel:
├── Required for TikTok Attribution
├── Required for TikTok Audiences
├── Required for Conversion Tracking
└── Implement via GTM or directly

NOTE:
├── ttclid is automatically added by TikTok
├── GA4 does NOT recognize ttclid for attribution
├── UTM is essential for GA4 tracking
└── TikTok audience is often younger - adjust messaging
```
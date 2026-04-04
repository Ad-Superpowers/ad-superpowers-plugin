## Quick Decision Tree

```
GA4 REMARKETING SETUP FLOW
│
├─► REQUIREMENTS CHECK
│   ├─► Google Ads account linked?
│   │   ├─► Yes → Proceed to audience export
│   │   └─► No → Link first (see step 1)
│   │
│   ├─► Google Signals enabled?
│   │   ├─► Yes → Cross-device remarketing possible
│   │   └─► No → Same-device targeting only
│   │
│   └─► Personalized ads enabled?
│       ├─► Yes → Audiences can be exported
│       └─► No → Export not possible (enable this!)
│
├─► WHICH REMARKETING TYPE?
│   ├─► Search (RLSA)
│   │   └─► Bid adjustments on search
│   │   └─► Minimum: 1,000 users
│   │
│   ├─► Display Network
│   │   └─► Banner remarketing
│   │   └─► Minimum: 100 users
│   │
│   ├─► YouTube
│   │   └─► Video remarketing
│   │   └─► Minimum: 1,000 users
│   │
│   └─► Discovery/Performance Max
│       └─► Cross-channel remarketing
│       └─► Minimum: 1,000 users
│
└─► WHICH AUDIENCES TO EXPORT?
    ├─► Converters (purchase, lead)
    │   └─► For: cross-sell, exclusions
    │
    ├─► Cart abandoners
    │   └─► For: recovery campaigns
    │
    ├─► Product viewers
    │   └─► For: consideration campaigns
    │
    └─► Engaged visitors
        └─► For: awareness retargeting
```

## Troubleshooting

```
TROUBLESHOOTING GUIDE
=====================

PROBLEM: Audiences not visible in Google Ads
─────────────────────────────────────────────
Causes:
├── Google Ads link not active
├── Personalized ads not enabled
├── Sync delay (24-48 hours)
├── Audience not marked for export
└── Google Ads account not selected

Solution:
├── GA4: Admin → Product Links → Google Ads → Status check
├── Verify "Personalized advertising" = ON
├── Check audience settings: Destinations → Google Ads
├── Wait 48 hours after configuration
└── Refresh Google Ads Audience Manager

PROBLEM: Audience size much smaller in Google Ads
──────────────────────────────────────────────────
Causes:
├── Match rate between GA4 and Google identity
├── Google Signals not enabled
├── Consent mode limits matching
├── Cross-device gaps
└── Normal: 30-70% match rate

Solution:
├── Enable Google Signals
├── Review consent implementation
├── Extend membership duration
├── Supplement with customer match
└── Accept that this is normal

PROBLEM: "List too small" error in Google Ads
─────────────────────────────────────────────
Causes:
├── Audience under minimum threshold
├── Match rate too low
├── Recently created audience
└── Too restrictive conditions

Solution:
├── Wait for more users (accumulation time)
├── Broaden audience conditions
├── Extend membership duration
├── Combine multiple small audiences
└── Start with broader targeting, narrow later

PROBLEM: Low remarketing performance
─────────────────────────────────────
Causes:
├── Wrong audience/campaign match
├── Creative not relevant for audience
├── Frequency too high (ad fatigue)
├── Attribution window too short
└── Competition in audience segment

Solution:
├── Align creative with audience intent
├── Lower frequency cap
├── Test different audiences
├── Extend conversion window
├── Review exclusions (converters included?)

PROBLEM: Audience stops updating
─────────────────────────────────
Causes:
├── GA4 tracking broken
├── Consent rates dropped
├── Website traffic decreased
├── Event triggering issues
└── Link between GA4/Google Ads broken

Solution:
├── Check GA4 realtime report
├── Verify event tracking in DebugView
├── Confirm Google Ads link still active
├── Review consent implementation
└── Test audience conditions manually
```
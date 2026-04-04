## Quick Decision Tree

```
GA4 AUDIENCE EXCLUSIONS FLOW
│
├─► WHY EXCLUDE?
│   ├─► Avoid wasting budget on already-converted users
│   │   └─► Exclude: Recent purchasers, completed leads
│   │
│   ├─► Prevent audience overlap
│   │   └─► Same user not in multiple campaigns
│   │
│   ├─► Prevent negative experiences
│   │   └─► Exclude: Refunders, complainers, bounced
│   │
│   └─► Frequency management
│       └─► Soft exclusions via capping
│
├─► WHICH EXCLUSION STRATEGY?
│   ├─► Hard exclusion (never show)
│   │   └─► Recent converters, existing customers
│   │
│   ├─► Timed exclusion (X days after event)
│   │   └─► Cross-sell timing, replenishment cycles
│   │
│   └─► Conditional exclusion
│       └─► Only exclude in specific campaigns
│
└─► WHERE TO IMPLEMENT?
    ├─► GA4 Audience level
    │   └─► "Exclude users when..." condition
    │
    ├─► Google Ads Campaign level
    │   └─► Audience exclusions per campaign
    │
    └─► Google Ads Ad Group level
        └─► Granular exclusions
```

## Troubleshooting

```
TROUBLESHOOTING GUIDE
======================

PROBLEM: Exclusion audience not working in Google Ads
──────────────────────────────────────────────────────
Causes:
├── Audience not exported to Google Ads
├── Wrong audience selected as exclusion
├── Campaign-level vs ad group-level confusion
├── Audience too small (<100 for Display)
└── Sync delay (up to 48 hours)

Solution:
├── Check GA4: Audience destinations → Google Ads ✅
├── Verify Google Ads: Audience Manager → list exists
├── Confirm exclusion applied at correct level
├── Wait until audience has sufficient users
└── Test with broader exclusion audience

PROBLEM: Users still see ads after conversion
───────────────────────────────────────────────
Causes:
├── Exclusion audience membership duration too short
├── Cross-device: user converted on different device
├── Consent mode: conversion not tracked
├── Exclusion only in some campaigns
└── Google Ads sync delay

Solution:
├── Extend exclusion duration (min. 7-14 days)
├── Enable Google Signals for cross-device
├── Verify conversion tracking works
├── Apply exclusion account-wide
├── Check Audience Manager for sync status

PROBLEM: Too little reach after exclusions
────────────────────────────────────────────
Causes:
├── Too many exclusions applied
├── Exclusion audiences too large
├── Small website = small audiences
└── Overlapping exclusions

Solution:
├── Review and consolidate exclusions
├── Shorten exclusion timeframes
├── Use timed exclusions instead of permanent
├── Focus on most impactful exclusions only

PROBLEM: Frequency higher than cap setting
────────────────────────────────────────────
Causes:
├── Multiple campaigns targeting same user
├── Cap applies per campaign, not account
├── Cross-device not matched
├── Display Network vs other networks
└── Reporting delay

Solution:
├── Implement account-level exclusions
├── Coordinate caps across campaigns
├── Enable Google Signals
├── Set caps on ALL campaigns, not selectively

PROBLEM: Exclusion conflicts with Smart Bidding
─────────────────────────────────────────────────
Causes:
├── Smart Bidding wants to target excluded users
├── Too strict exclusions limit learning
├── Audience signals vs audience targeting
└── Algorithm fights your exclusions

Solution:
├── Smart Bidding respects exclusions
├── But: too many exclusions = less learning data
├── Balance: exclude obvious waste, but not too aggressively
├── Monitor algorithm performance metrics
└── Adjust exclusions based on Smart Bidding feedback
```
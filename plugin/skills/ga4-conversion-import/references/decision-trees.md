## Quick Decision Tree

```
GA4 CONVERSION IMPORT FLOW
│
├─► WHICH CONVERSIONS TO IMPORT?
│   ├─► Macro-conversions (main goal)
│   │   └─► Purchase, Lead, Sign-up
│   │   └─► Import as PRIMARY conversion
│   │
│   ├─► Micro-conversions (steps)
│   │   └─► Add to cart, Begin checkout, Form start
│   │   └─► Import as SECONDARY conversion
│   │
│   └─► All site engagement
│       └─► Page views, Scroll, Video views
│       └─► DO NOT import (noise for bidding)
│
├─► SMART BIDDING STRATEGY?
│   ├─► Target CPA / Maximize Conversions
│   │   └─► Import lead/purchase as primary
│   │   └─► Counting: One per click
│   │
│   ├─► Target ROAS / Maximize Conv. Value
│   │   └─► Import purchase with value
│   │   └─► Counting: Every conversion
│   │
│   └─► Performance Max
│       └─► Minimum 1 primary conversion
│       └─► Add micro-conversions as secondary
│       └─► Allow 30 days learning time
│
└─► VOLUME CHECK
    ├─► < 30 conversions/month per campaign
    │   └─► Add micro-conversions as primary
    │   └─► Or use account-level bidding
    │
    └─► > 30 conversions/month per campaign
        └─► Use only macro-conversions as primary
        └─► Smart Bidding can optimize
```

## Troubleshooting Conversion Import

```
CONVERSION IMPORT TROUBLESHOOTING
===================================

PROBLEM: Conversions not visible for import
────────────────────────────────────────────
Causes:
├── Event not marked as key event in GA4
├── Key event has 0 events (no data)
├── Google Ads link not active
├── Wait time after marking (24-48 hours)
└── Permissions issue (no admin access)

Solution:
├── Check GA4: Admin → Key events → is event listed?
├── Check GA4: Events → does event have data in last 7 days?
├── Check link: Admin → Product Links → Google Ads
├── Wait 24-48 hours after new key event marking
└── Verify you have admin access on both platforms

PROBLEM: Conversion data mismatch GA4 vs Google Ads
─────────────────────────────────────────────────────
Causes:
├── Different attribution models
├── Different conversion windows
├── Counting method difference (one vs every)
├── Timezone difference
└── Data import delay

Expected differences:
├── 5-15% difference is NORMAL
├── > 20% difference = investigate

Solution:
├── Sync attribution models where possible
├── Match conversion windows
├── Document expected discrepancy
└── Choose one source of truth

PROBLEM: Smart Bidding not delivering results
──────────────────────────────────────────────
Causes:
├── Insufficient conversion volume
├── Learning period too short
├── Conflicting primary conversions
├── Conversion lag not configured
└── Budget too low for target

Solution:
├── Check minimum volumes (30/month for tCPA)
├── Allow 2-4 weeks learning time
├── Use max 1-2 primary conversions
├── Adjust targets to realistic levels
└── Add micro-conversions if volume too low

PROBLEM: GA4 conversions stop importing
────────────────────────────────────────
Causes:
├── Google Ads link broken
├── GA4 property permissions changed
├── Key event unmarked in GA4
├── Data stream issues
└── Consent mode blocking

Solution:
├── Re-check and re-link if needed
├── Verify permissions on both platforms
├── Check key event status in GA4
├── Test with GA4 DebugView
└── Review consent mode implementation
```
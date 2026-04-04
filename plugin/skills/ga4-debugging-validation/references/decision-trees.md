## Quick Decision Tree

```
GA4 DEBUGGING FLOW
│
├─► WHAT DO YOU WANT TO DEBUG?
│   ├─► Real-time event testing
│   │   └─► GA4 DebugView
│   │
│   ├─► Tag firing issues
│   │   └─► GTM Preview Mode + Tag Assistant
│   │
│   ├─► Network requests
│   │   └─► Browser DevTools Network tab
│   │
│   └─► Historical data issues
│       └─► Data Quality reports + Explorations
│
├─► WHEN TO TEST?
│   ├─► During development
│   │   └─► Chrome extension + DebugView
│   │
│   ├─► After deployment
│   │   └─► QA checklist + automated tests
│   │
│   └─► Ongoing monitoring
│       └─► Data anomaly alerts
│
└─► WHICH BROWSER/DEVICE?
    ├─► Desktop Chrome
    │   └─► GA Debugger extension + DevTools
    │
    ├─► Mobile web
    │   └─► Remote debugging + DebugView
    │
    └─► Mobile app
        └─► Firebase DebugView
```

## Common Tracking Problems

```
TROUBLESHOOTING COMMON ISSUES
===============================

PROBLEM: Events not visible in DebugView
─────────────────────────────────────────
Causes:
├── Debug mode not active
├── Ad blocker on
├── Wrong device selected
├── Tag not fired
└── Consent not given

Solution:
├── Verify debug mode parameter/extension
├── Disable ad blockers
├── Check device selector in DebugView
├── Check GTM Preview
└── Accept consent, retry


PROBLEM: Duplicate events
──────────────────────────
Causes:
├── GTM tag fired multiple times
├── Both GTM and gtag.js implementation
├── DataLayer push multiple times
├── Single Page App routing issues
└── Page reload triggers

Solution:
├── Check "Times Fired" in GTM Preview
├── Remove duplicate implementations
├── Add deduplication logic
├── Implement proper SPA tracking
└── Use session-based deduplication


PROBLEM: Missing parameters
────────────────────────────
Causes:
├── DataLayer not correct
├── Variable mapping error
├── Parameter name typo
├── Timing issues (async)
└── Scope issues

Solution:
├── Log dataLayer in console
├── Check GTM variable values
├── Verify exact parameter names
├── Add wait/callback logic
├── Check JavaScript scope


PROBLEM: (not set) in reports
──────────────────────────────
Causes:
├── Traffic source data missing
├── UTM parameters not parsed
├── Cross-domain tracking issues
├── Referral exclusion incorrect
└── Direct traffic (legitimate)

Solution:
├── Review UTM tagging
├── Check auto-tagging (Google Ads)
├── Verify cross-domain setup
├── Review exclusion list
├── Accept some direct is normal


PROBLEM: Revenue discrepancies
───────────────────────────────
Causes:
├── Currency mismatch
├── Tax/shipping handling
├── Test orders in data
├── Duplicate transactions
├── Timing differences

Solution:
├── Verify currency settings
├── Document value calculation
├── Exclude test transactions
├── Check transaction_id uniqueness
├── Compare same time periods


PROBLEM: Self-referrals
────────────────────────
Causes:
├── Cross-domain tracking not correct
├── Payment gateway redirects
├── Subdomains not excluded
└── Third-party hosted pages

Solution:
├── Configure cross-domain list
├── Add payment domains to tracking
├── Add subdomains to stream
└── Implement linker on third-party
```
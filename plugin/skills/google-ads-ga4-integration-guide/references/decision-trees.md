## Quick Decision Guide

```
WHICH GA4 INTEGRATION DO YOU NEED?
│
├─► BASIC LINKING
│   └─► GOOGLE ADS ↔ GA4 ACCOUNT LINK
│       ├── See Google Ads data in GA4
│       ├── See GA4 conversions in Google Ads
│       └── Automatic UTM parameter recognition
│
├─► CONVERSION TRACKING
│   └─► GA4 CONVERSIONS → GOOGLE ADS IMPORT
│       ├── Use GA4 as single source of truth
│       ├── Cross-device conversion tracking
│       └── Better attribution than client-side tags
│
├─► AUDIENCE TARGETING
│   └─► GA4 AUDIENCES → GOOGLE ADS
│       ├── Remarketing based on GA4 behavior
│       ├── Lookalike audiences
│       └── Advanced segment targeting
│
└─► FULL INTEGRATION
    └─► ALL OF THE ABOVE + REPORTING
        ├── Unified reporting
        ├── Cross-platform attribution
        └── Custom dimensions/metrics
```

### Resolving Conversion Discrepancies

```
CONVERSION DISCREPANCY TROUBLESHOOTING
═══════════════════════════════════════

PROBLEM: GOOGLE ADS AND GA4 CONVERSIONS DON'T MATCH
────────────────────────────────────────────────────

CHECK 1: ATTRIBUTION MODEL
───────────────────────────
GA4: Admin → Attribution settings
Google Ads: Conversions → Settings → Attribution

Ensure both use the same model (data-driven)

CHECK 2: LOOKBACK WINDOW
─────────────────────────
GA4: Default 30 days
Google Ads: Check per conversion action

Align both to 30 or 90 days

CHECK 3: COUNTING METHOD
─────────────────────────
GA4: Counts unique users per event (default)
Google Ads: "One" vs "Every"

For leads: "One" (one per user per day)
For purchases: "Every" (each transaction)

CHECK 4: CONVERSION TIME
─────────────────────────
GA4: Reports on conversion timestamp
Google Ads (imported): Reports on click timestamp

→ This is a normal difference, cannot be fixed

CHECK 5: FILTERS AND SEGMENTS
──────────────────────────────
GA4: Check if no filters are active
Google Ads: Check conversion action status

EXPECTED DISCREPANCIES:
───────────────────────
□ 5-15% difference is normal
□ Cross-device conversions (GA4 has more)
□ Modeled conversions (GA4 models more)
□ Timing differences (click vs conversion date)

ACTION IF >20% DIFFERENCE:
──────────────────────────
1. Verify tracking implementation
2. Check for duplicate tags
3. Verify consent mode is consistent
4. Check for bot traffic filters
```
## Quick Decision Tree

```
CROSS-PLATFORM TRACKING DECISION
│
├─► WHICH PLATFORM ARE YOU TRACKING?
│   ├─► Google Ads
│   │   └─► AUTO-TAGGING (gclid)
│   │       └─► No UTM needed
│   │       └─► Automatic in GA4
│   │
│   ├─► Meta (Facebook/Instagram)
│   │   └─► UTM PARAMETERS required
│   │   └─► fbclid only for Meta Attribution
│   │   └─► GA4 does NOT recognize fbclid automatically
│   │
│   ├─► LinkedIn Ads
│   │   └─► UTM PARAMETERS required
│   │   └─► LinkedIn Insight Tag separate
│   │
│   ├─► TikTok Ads
│   │   └─► UTM PARAMETERS required
│   │   └─► ttclid only for TikTok Attribution
│   │
│   └─► Other platforms (Pinterest, Twitter, etc.)
│       └─► UTM PARAMETERS always required
│
├─► WHAT DO YOU WANT TO MEASURE?
│   ├─► Traffic source → UTM source/medium
│   ├─► Campaign name → UTM campaign
│   ├─► Ad creative → UTM content
│   └─► Keyword/targeting → UTM term
│
└─► HOW TO STAY CONSISTENT?
    ├─► Use naming convention (see below)
    ├─► Create UTM template per platform
    ├─► Use URL builder tools
    └─► Document all campaign IDs
```

## Auto-Tagging vs UTM

```
AUTO-TAGGING VS UTM DECISION
==============================

GOOGLE ADS: ALWAYS AUTO-TAGGING
────────────────────────────────
┌─────────────────────┬──────────────────┬──────────────────────┐
│ Aspect              │ Auto-tagging     │ UTM                  │
├─────────────────────┼──────────────────┼──────────────────────┤
│ Accuracy            │ Very high        │ Depends on setup     │
├─────────────────────┼──────────────────┼──────────────────────┤
│ Cross-device        │ Full             │ Limited              │
├─────────────────────┼──────────────────┼──────────────────────┤
│ GA4 integration     │ Native           │ Manual               │
├─────────────────────┼──────────────────┼──────────────────────┤
│ Remarketing         │ Full             │ Not supported        │
├─────────────────────┼──────────────────┼──────────────────────┤
│ Maintenance         │ None             │ Continuous            │
└─────────────────────┴──────────────────┴──────────────────────┘

Conclusion: Google Ads → Auto-tagging, NO UTM needed

ENABLING AUTO-TAGGING:
LOCATION: Google Ads → Admin → Account Settings

Check: "Auto-tagging" is ON
Check: GA4 link is active
Check: gclid in URLs after ad click

WHEN TO USE UTM WITH GOOGLE ADS:
├── Third-party analytics (Adobe, etc.)
├── CRM tracking alongside GA4
├── Specific custom dimensions needed
└── WARNING: can conflict with auto-tagging

NON-GOOGLE PLATFORMS: ALWAYS UTM
─────────────────────────────────
Platform click IDs that GA4 does NOT recognize:
├── fbclid (Meta)
├── li_fat_id (LinkedIn)
├── ttclid (TikTok)
├── epik (Pinterest)
└── msclkid (Microsoft - partially recognized)

→ ALWAYS add UTM for non-Google platforms
```

## Troubleshooting Cross-Platform

```
CROSS-PLATFORM TRACKING TROUBLESHOOTING
=========================================

PROBLEM: Traffic appears as Direct
────────────────────────────────────
Causes:
├── UTM parameters not set
├── URL redirect removes parameters
├── JavaScript redirect without parameters
├── App traffic (deep links)
└── Consent tool blocks tracking

Solution:
├── Add UTM parameters to all ad URLs
├── Test full redirect chain
├── Check landing page preserves query params
├── Implement deep link tracking
└── Review consent mode implementation

PROBLEM: Source/Medium is "(not set)"
──────────────────────────────────────
Causes:
├── UTM parameters malformed
├── Special characters not encoded
├── Server-side redirect removes params
└── GTM tag configuration issue

Solution:
├── Validate UTM URL in builder tool
├── URL encode special characters
├── Check server redirects (301, 302)
└── Verify GTM GA4 config tag

PROBLEM: Inconsistent campaign names
──────────────────────────────────────
Causes:
├── Manual input with typos
├── Case-sensitivity issues
├── Different conventions per person
└── Template not used

Solution:
├── Create and enforce naming convention
├── Use URL builder templates
├── Implement campaign name generator tool
└── Review and clean up historical data

PROBLEM: Platform data != GA4 data
────────────────────────────────────
Expected discrepancies:
├── 10-30% difference is NORMAL
├── Platforms claim view-through
├── Different attribution windows
├── Cross-device gaps

Solution:
├── Document expected differences
├── Use GA4 as source of truth for cross-platform
├── Use platform data for platform-specific optimization
└── Report both metrics, explain difference

PROBLEM: UTM parameters disappear on redirect
───────────────────────────────────────────────
Causes:
├── 302 redirect to clean URL
├── JavaScript redirect without params
├── CMS that filters query parameters
└── CDN caching without query params

Solution:
├── Test redirect chain with:
│   curl -I -L "https://your-url.com/?utm_..."
├── Check server config for parameter preservation
├── Whitelist utm_* parameters in CMS
└── Configure CDN to preserve query params
```
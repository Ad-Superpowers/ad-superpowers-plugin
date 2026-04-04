## Quick Decision Tree

```
WHICH EVENT TYPE DO YOU NEED?
│
├─► AUTOMATICALLY TRACKED (Enhanced Measurement)
│   ├── page_view (automatic)
│   ├── scroll (90% depth)
│   ├── click (outbound links)
│   ├── file_download
│   ├── video_start/progress/complete (YouTube)
│   └── view_search_results
│       └─► CHECK: Is Enhanced Measurement ON?
│
├─► RECOMMENDED EVENTS (Google's standard names)
│   ├── E-commerce: view_item, add_to_cart, purchase
│   ├── Lead gen: generate_lead, sign_up
│   ├── Content: share, search
│   └── Gaming: earn_virtual_currency, level_up
│       └─► USE: Google's event names for better AI/reports
│
├─► CUSTOM EVENTS (your own names)
│   ├── Specific business actions
│   ├── Interaction tracking
│   └── Micro-conversions
│       └─► NAMING: snake_case, max 40 chars
│
└─► WHICH TRIGGER?
    ├── Click → Element Click / Just Links trigger
    ├── Form Submit → Form Submission trigger
    ├── Page Load → Page View trigger + conditions
    ├── Scroll → Scroll Depth trigger
    ├── Timer → Timer trigger
    └── Custom → Custom Event / dataLayer push
```

## Common Problems

```
TROUBLESHOOTING EVENT TRACKING
================================

PROBLEM: Event does not fire
─────────────────────────────
Checklist:
[] Is trigger correctly configured?
[] Is built-in variable enabled?
[] Is CSS selector/ID correct?
[] Test in GTM Preview - check "Tags Not Fired"
[] Is there a blocking trigger?
[] Has consent been given (consent mode)?

PROBLEM: Duplicate events
─────────────────────────
Causes:
├── Trigger fires multiple times
├── Enhanced Measurement + custom tracking
├── Multiple tags for same event
└── SPA route changes

Solution:
├── Add trigger conditions to restrict
├── Disable overlapping Enhanced Measurement
├── Use event deduplication
└── Trigger only once per page/session

PROBLEM: Parameters not appearing in reports
─────────────────────────────────────────────
Checklist:
[] Is parameter registered as custom dimension?
[] Are you waiting 24-48 hours? (processing time)
[] Is parameter name exactly matching (case-sensitive)?
[] Check DebugView - are parameters visible there?

PROBLEM: Event name validation error
──────────────────────────────────────
Causes:
├── Spaces in event name
├── Special characters
├── Starts with a digit
├── Reserved event name used

Solution:
├── Use snake_case: contact_form_submit
├── Only letters, digits, underscores
├── Start with a letter
├── Check reserved names list
```
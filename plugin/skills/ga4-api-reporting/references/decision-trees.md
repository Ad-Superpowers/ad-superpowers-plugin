## Quick Decision Tree

```
GA4 DATA API DECISION TREE
│
├─► WHICH API DO YOU NEED?
│   ├─► GA4 Data API (Reporting)
│   │   └─► Aggregated metrics & dimensions
│   │   └─► Reports like in GA4 UI
│   │
│   ├─► GA4 Admin API
│   │   └─► Property configuration
│   │   └─► Accounts, streams, links
│   │
│   └─► BigQuery Export
│       └─► Raw event-level data
│       └─► Custom analyses
│
├─► USE CASE?
│   ├─► Scheduled reports
│   │   └─► Data API + scheduler (cron/Cloud Functions)
│   │
│   ├─► Custom dashboard
│   │   └─► Data API → Looker Studio / custom app
│   │
│   ├─► Data warehouse
│   │   └─► Data API → ETL → Database
│   │
│   └─► Ad-hoc analyses
│       └─► Data API via Python/JavaScript
│
└─► LANGUAGE/PLATFORM?
    ├─► Python
    │   └─► google-analytics-data library
    │
    ├─► JavaScript/Node.js
    │   └─► @google-analytics/data
    │
    ├─► Google Sheets
    │   └─► GA4 Data API Add-on
    │
    └─► REST API
        └─► Direct HTTP calls
```

## Common Problems

```
TROUBLESHOOTING GA4 DATA API
=============================

PROBLEM: 403 Permission Denied
───────────────────────────────
Causes:
├── Service account not added to GA4
├── Wrong property ID
├── API not enabled
└── Credentials file path incorrect

Solution:
├── Verify service account email in GA4 Admin
├── Check property ID (numeric only)
├── Enable Analytics Data API in GCP
└── Verify GOOGLE_APPLICATION_CREDENTIALS path


PROBLEM: Quota exceeded
────────────────────────
Causes:
├── Too many requests in short time
├── Queries too complex
├── Multiple processes on same property
└── Realtime API overuse

Solution:
├── Implement exponential backoff
├── Simplify queries
├── Coordinate API calls between processes
├── Cache responses where possible

# Python retry logic
from google.api_core import retry

@retry.Retry(
    predicate=retry.if_exception_type(
        google.api_core.exceptions.ResourceExhausted
    ),
    initial=1.0,
    maximum=60.0,
    multiplier=2.0,
)
def run_report_with_retry():
    return client.run_report(request)


PROBLEM: Data discrepancies with UI
────────────────────────────────────
Causes:
├── Different date ranges
├── Sampling in UI
├── Timezone differences
├── Different metric definitions
└── Real-time vs processed data

Solution:
├── Match exact date ranges
├── Compare with unsampled data
├── Verify timezone in both
├── Check metric API names
└── Wait for data processing


PROBLEM: Empty response
────────────────────────
Causes:
├── Wrong dimension/metric names
├── Filters too restrictive
├── Date range has no data
├── Property ID incorrect
└── Permissions issue

Solution:
├── Check exact API names in documentation
├── Start without filters, then add
├── Verify date range has traffic
├── Double-check property ID
└── Verify viewer access in GA4
```
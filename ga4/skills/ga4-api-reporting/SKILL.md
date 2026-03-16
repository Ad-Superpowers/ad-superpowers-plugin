---
name: ga4-api-reporting
description: "GA4 Data API voor custom reporting en dashboards. Gebruik voor: (1) GA4 Data API integratie, (2) Automated reporting opzetten, (3) Custom dashboards bouwen, (4) Data extraction scripts, (5) API quota en limieten begrijpen. Triggers: ga4 api, data api, automated reports, custom dashboard, api integratie, reporting automation, ga4 data extraction."
---

# GA4 Data API Reporting Guide

Complete gids voor het gebruik van de GA4 Data API voor custom reporting en geautomatiseerde dashboards.

## Quick Decision Tree

```
GA4 DATA API BESLISBOOM
│
├─► WELKE API HEB JE NODIG?
│   ├─► GA4 Data API (Reporting)
│   │   └─► Aggregated metrics & dimensions
│   │   └─► Reports zoals in GA4 UI
│   │
│   ├─► GA4 Admin API
│   │   └─► Property configuratie
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
└─► TAAL/PLATFORM?
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

## API Setup & Authenticatie

```
GA4 DATA API SETUP
==================

STAP 1: GCP PROJECT CONFIGUREREN
────────────────────────────────
1. Ga naar console.cloud.google.com
2. Maak nieuw project of selecteer bestaand
3. Enable APIs:
   └── APIs & Services → Enable APIs
       └── "Google Analytics Data API"

STAP 2: SERVICE ACCOUNT AANMAKEN
────────────────────────────────
1. IAM & Admin → Service Accounts
2. Create Service Account:
   ├── Name: ga4-reporting-service
   └── Description: GA4 Data API access

3. Create Key:
   ├── Keys tab → Add Key → Create new key
   ├── Key type: JSON
   └── Download en bewaar veilig!

STAP 3: GA4 TOEGANG VERLENEN
────────────────────────────
1. Ga naar GA4 Admin → Property Access Management
2. Add Users → Voeg service account email toe
   └── Email format: name@project-id.iam.gserviceaccount.com
3. Rol: Viewer (voor read-only API access)

AUTHENTICATIE OPTIES:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Methode                 │ Use Case                                 │
├─────────────────────────┼──────────────────────────────────────────┤
│ Service Account (JSON)  │ Server-to-server, automated scripts     │
├─────────────────────────┼──────────────────────────────────────────┤
│ OAuth 2.0               │ User-facing apps, interactive access    │
├─────────────────────────┼──────────────────────────────────────────┤
│ API Key                 │ NIET ondersteund voor GA4 Data API      │
└─────────────────────────┴──────────────────────────────────────────┘
```

## Python Implementatie

```python
# ============================================
# GA4 DATA API - PYTHON VOORBEELDEN
# ============================================

# INSTALLATIE:
# pip install google-analytics-data

# BASIS SETUP
# ───────────
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest,
    DateRange,
    Dimension,
    Metric,
    FilterExpression,
    Filter,
)
import os

# Authenticatie via environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/service-account.json"

# Of via explicit credentials
# from google.oauth2 import service_account
# credentials = service_account.Credentials.from_service_account_file('key.json')
# client = BetaAnalyticsDataClient(credentials=credentials)

client = BetaAnalyticsDataClient()
property_id = "YOUR_PROPERTY_ID"  # Alleen numeriek ID, geen "properties/" prefix


# VOORBEELD 1: BASIS RAPPORT
# ──────────────────────────
def get_basic_report():
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="date"),
            Dimension(name="country"),
        ],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="sessions"),
            Metric(name="screenPageViews"),
        ],
        date_ranges=[
            DateRange(start_date="30daysAgo", end_date="yesterday")
        ],
    )

    response = client.run_report(request)

    # Process response
    for row in response.rows:
        date = row.dimension_values[0].value
        country = row.dimension_values[1].value
        users = row.metric_values[0].value
        sessions = row.metric_values[1].value
        pageviews = row.metric_values[2].value
        print(f"{date} | {country} | Users: {users} | Sessions: {sessions}")

    return response


# VOORBEELD 2: E-COMMERCE RAPPORT
# ───────────────────────────────
def get_ecommerce_report():
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="date"),
            Dimension(name="sessionSourceMedium"),
        ],
        metrics=[
            Metric(name="ecommercePurchases"),
            Metric(name="purchaseRevenue"),
            Metric(name="averagePurchaseRevenue"),
            Metric(name="transactions"),
        ],
        date_ranges=[
            DateRange(start_date="30daysAgo", end_date="yesterday")
        ],
        order_bys=[
            {"metric": {"metric_name": "purchaseRevenue"}, "desc": True}
        ],
        limit=50,
    )

    return client.run_report(request)


# VOORBEELD 3: RAPPORT MET FILTER
# ───────────────────────────────
def get_filtered_report():
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="pagePath"),
        ],
        metrics=[
            Metric(name="screenPageViews"),
            Metric(name="averageSessionDuration"),
        ],
        date_ranges=[
            DateRange(start_date="7daysAgo", end_date="yesterday")
        ],
        dimension_filter=FilterExpression(
            filter=Filter(
                field_name="pagePath",
                string_filter=Filter.StringFilter(
                    match_type=Filter.StringFilter.MatchType.CONTAINS,
                    value="/products/"
                )
            )
        ),
    )

    return client.run_report(request)


# VOORBEELD 4: REALTIME RAPPORT
# ─────────────────────────────
def get_realtime_report():
    from google.analytics.data_v1beta.types import RunRealtimeReportRequest

    request = RunRealtimeReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="country"),
            Dimension(name="city"),
        ],
        metrics=[
            Metric(name="activeUsers"),
        ],
    )

    return client.run_realtime_report(request)


# VOORBEELD 5: EXPORT NAAR PANDAS
# ───────────────────────────────
def export_to_dataframe():
    import pandas as pd

    response = get_basic_report()

    # Extract data
    rows = []
    for row in response.rows:
        rows.append({
            "date": row.dimension_values[0].value,
            "country": row.dimension_values[1].value,
            "users": int(row.metric_values[0].value),
            "sessions": int(row.metric_values[1].value),
            "pageviews": int(row.metric_values[2].value),
        })

    df = pd.DataFrame(rows)
    return df
```

## JavaScript/Node.js Implementatie

```javascript
// ============================================
// GA4 DATA API - NODE.JS VOORBEELDEN
// ============================================

// INSTALLATIE:
// npm install @google-analytics/data

const { BetaAnalyticsDataClient } = require('@google-analytics/data');

// Authenticatie via environment variable
// GOOGLE_APPLICATION_CREDENTIALS=path/to/key.json

const analyticsDataClient = new BetaAnalyticsDataClient();
const propertyId = 'YOUR_PROPERTY_ID';


// VOORBEELD 1: BASIS RAPPORT
// ──────────────────────────
async function runBasicReport() {
  const [response] = await analyticsDataClient.runReport({
    property: `properties/${propertyId}`,
    dateRanges: [
      {
        startDate: '30daysAgo',
        endDate: 'yesterday',
      },
    ],
    dimensions: [
      { name: 'date' },
      { name: 'country' },
    ],
    metrics: [
      { name: 'activeUsers' },
      { name: 'sessions' },
    ],
  });

  console.log('Report result:');
  response.rows.forEach(row => {
    console.log(
      row.dimensionValues[0].value,
      row.dimensionValues[1].value,
      row.metricValues[0].value,
      row.metricValues[1].value
    );
  });

  return response;
}


// VOORBEELD 2: E-COMMERCE DATA
// ────────────────────────────
async function runEcommerceReport() {
  const [response] = await analyticsDataClient.runReport({
    property: `properties/${propertyId}`,
    dateRanges: [
      { startDate: '7daysAgo', endDate: 'yesterday' },
    ],
    dimensions: [
      { name: 'itemName' },
      { name: 'itemCategory' },
    ],
    metrics: [
      { name: 'itemsPurchased' },
      { name: 'itemRevenue' },
    ],
    orderBys: [
      { metric: { metricName: 'itemRevenue' }, desc: true },
    ],
    limit: 20,
  });

  return response;
}


// VOORBEELD 3: MET FILTERS
// ────────────────────────
async function runFilteredReport() {
  const [response] = await analyticsDataClient.runReport({
    property: `properties/${propertyId}`,
    dateRanges: [
      { startDate: '30daysAgo', endDate: 'yesterday' },
    ],
    dimensions: [
      { name: 'sessionSourceMedium' },
    ],
    metrics: [
      { name: 'sessions' },
      { name: 'conversions' },
    ],
    dimensionFilter: {
      filter: {
        fieldName: 'sessionSourceMedium',
        stringFilter: {
          matchType: 'CONTAINS',
          value: 'google',
        },
      },
    },
  });

  return response;
}


// VOORBEELD 4: REALTIME DATA
// ──────────────────────────
async function runRealtimeReport() {
  const [response] = await analyticsDataClient.runRealtimeReport({
    property: `properties/${propertyId}`,
    dimensions: [
      { name: 'country' },
    ],
    metrics: [
      { name: 'activeUsers' },
    ],
  });

  return response;
}


// Uitvoeren
runBasicReport().catch(console.error);
```

## Google Sheets Integratie

```
GA4 DATA API IN GOOGLE SHEETS
=============================

METHODE 1: GA4 DATA EXPORT ADD-ON
─────────────────────────────────
1. Extensions → Add-ons → Get add-ons
2. Zoek "GA4 Reports" of "Supermetrics"
3. Installeer en autoriseer
4. Configureer rapport queries

METHODE 2: APPS SCRIPT (CUSTOM)
───────────────────────────────
// In Google Sheets: Extensions → Apps Script

function getGA4Data() {
  const propertyId = 'YOUR_PROPERTY_ID';

  const request = {
    "dateRanges": [{
      "startDate": "30daysAgo",
      "endDate": "yesterday"
    }],
    "dimensions": [
      {"name": "date"},
      {"name": "sessionSourceMedium"}
    ],
    "metrics": [
      {"name": "sessions"},
      {"name": "conversions"}
    ]
  };

  const url = `https://analyticsdata.googleapis.com/v1beta/properties/${propertyId}:runReport`;

  const options = {
    'method': 'post',
    'contentType': 'application/json',
    'headers': {
      'Authorization': 'Bearer ' + ScriptApp.getOAuthToken()
    },
    'payload': JSON.stringify(request)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response.getContentText());

  // Write to sheet
  const sheet = SpreadsheetApp.getActiveSheet();
  sheet.clear();

  // Headers
  const headers = ['Date', 'Source/Medium', 'Sessions', 'Conversions'];
  sheet.appendRow(headers);

  // Data rows
  data.rows.forEach(row => {
    sheet.appendRow([
      row.dimensionValues[0].value,
      row.dimensionValues[1].value,
      row.metricValues[0].value,
      row.metricValues[1].value
    ]);
  });
}

// Scheduled trigger toevoegen:
// Triggers → Add Trigger → getGA4Data → Time-driven → Day timer

OAUTHSCOPES TOEVOEGEN:
──────────────────────
// In appsscript.json:
{
  "oauthScopes": [
    "https://www.googleapis.com/auth/analytics.readonly",
    "https://www.googleapis.com/auth/spreadsheets"
  ]
}
```

## API Quota & Limieten

```
GA4 DATA API QUOTA'S
====================

STANDAARD QUOTA'S:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Limit Type              │ Waarde                                   │
├─────────────────────────┼──────────────────────────────────────────┤
│ Requests per day        │ 200,000 per project                      │
├─────────────────────────┼──────────────────────────────────────────┤
│ Requests per property   │ 2,000 per property per hour              │
│ per hour                │                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Concurrent requests     │ 10 per property                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Tokens per project      │ 1,750,000 per dag                        │
│ per day                 │                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Tokens per property     │ 175,000 per property per uur             │
│ per hour                │                                          │
└─────────────────────────┴──────────────────────────────────────────┘

TOKEN KOSTEN:
─────────────
Elke request verbruikt tokens afhankelijk van complexiteit:

┌─────────────────────────┬──────────────────────────────────────────┐
│ Request Type            │ Token Kosten (indicatief)                │
├─────────────────────────┼──────────────────────────────────────────┤
│ Simpele query           │ ~10 tokens                               │
│ (1-2 dimensions/metrics)│                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Medium query            │ ~50 tokens                               │
│ (3-5 dimensions/metrics)│                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Complexe query          │ ~100+ tokens                             │
│ (filters, pivots, etc.) │                                          │
├─────────────────────────┼──────────────────────────────────────────┤
│ Realtime rapport        │ ~200 tokens                              │
└─────────────────────────┴──────────────────────────────────────────┘

QUOTA OPTIMALISATIE TIPS:
─────────────────────────
1. BATCH REQUESTS
   └── Gebruik runBatchReports voor meerdere queries

2. CACHE RESPONSES
   └── Sla responses op, refresh alleen wanneer nodig

3. BEPERK DATE RANGES
   └── Kleinere ranges = minder tokens

4. SELECTEER ALLEEN NODIGE VELDEN
   └── Minder dimensions/metrics = minder tokens

5. GEBRUIK SAMPLING (indien acceptabel)
   └── Snellere responses, minder tokens

QUOTA MONITORING:
─────────────────
├── GCP Console → APIs & Services → Dashboard
├── Selecteer "Analytics Data API"
└── View quota usage graphs
```

## Beschikbare Metrics & Dimensions

```
VEELGEBRUIKTE DIMENSIONS
========================

USER & SESSION:
├── userId (custom user ID)
├── userAgeBracket
├── userGender
├── newVsReturning
├── sessionSource
├── sessionMedium
├── sessionSourceMedium
├── sessionCampaignName
└── sessionDefaultChannelGroup

TIJD:
├── date (YYYYMMDD)
├── dateHour
├── dateHourMinute
├── dayOfWeek
├── hour
├── month
└── year

PAGE & SCREEN:
├── pagePath
├── pageTitle
├── pagePathPlusQueryString
├── landingPage
├── exitPage
└── screenName

DEVICE & GEO:
├── deviceCategory
├── platform
├── browser
├── operatingSystem
├── country
├── city
└── region

E-COMMERCE:
├── itemName
├── itemId
├── itemBrand
├── itemCategory
├── transactionId
└── orderCoupon


VEELGEBRUIKTE METRICS
=====================

USERS & SESSIONS:
├── activeUsers
├── newUsers
├── totalUsers
├── sessions
├── sessionsPerUser
├── engagedSessions
├── averageSessionDuration
└── bounceRate

ENGAGEMENT:
├── screenPageViews
├── screenPageViewsPerSession
├── eventCount
├── engagementRate
└── userEngagementDuration

E-COMMERCE:
├── ecommercePurchases
├── transactions
├── purchaseRevenue
├── totalRevenue
├── averagePurchaseRevenue
├── itemsPurchased
├── itemRevenue
└── itemsViewed

CONVERSIONS:
├── conversions
├── eventValue
└── [customEvent]:eventCount

VOLLEDIGE LIJST:
────────────────
https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema
```

## Automated Reporting Setup

```
GEAUTOMATISEERDE RAPPORTAGE
===========================

OPTIE 1: CLOUD FUNCTIONS + SCHEDULER
────────────────────────────────────
# requirements.txt
google-analytics-data
google-cloud-storage
pandas

# main.py
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.cloud import storage
import pandas as pd
import json
from datetime import datetime

def daily_ga4_report(event, context):
    client = BetaAnalyticsDataClient()
    property_id = "YOUR_PROPERTY_ID"

    response = client.run_report(
        property=f"properties/{property_id}",
        dimensions=[{"name": "date"}, {"name": "sessionSourceMedium"}],
        metrics=[{"name": "sessions"}, {"name": "conversions"}],
        date_ranges=[{"start_date": "yesterday", "end_date": "yesterday"}]
    )

    # Convert to DataFrame
    rows = []
    for row in response.rows:
        rows.append({
            "date": row.dimension_values[0].value,
            "source_medium": row.dimension_values[1].value,
            "sessions": row.metric_values[0].value,
            "conversions": row.metric_values[1].value,
        })
    df = pd.DataFrame(rows)

    # Save to Cloud Storage
    bucket_name = "your-bucket"
    blob_name = f"ga4-reports/{datetime.now().strftime('%Y-%m-%d')}.csv"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(df.to_csv(index=False), 'text/csv')

    return "Report generated successfully"

# Cloud Scheduler setup:
# gcloud scheduler jobs create http daily-ga4-report \
#   --schedule="0 6 * * *" \
#   --uri="YOUR_CLOUD_FUNCTION_URL" \
#   --http-method=POST


OPTIE 2: GITHUB ACTIONS
───────────────────────
# .github/workflows/ga4-report.yml
name: Daily GA4 Report

on:
  schedule:
    - cron: '0 6 * * *'  # Dagelijks om 6:00 UTC
  workflow_dispatch:

jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install google-analytics-data pandas

      - name: Create credentials file
        run: echo '${{ secrets.GA4_CREDENTIALS }}' > credentials.json

      - name: Run report
        env:
          GOOGLE_APPLICATION_CREDENTIALS: credentials.json
        run: python scripts/generate_report.py

      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: ga4-report
          path: output/*.csv


OPTIE 3: AIRFLOW DAG
────────────────────
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'analytics',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'ga4_daily_report',
    default_args=default_args,
    schedule_interval='0 6 * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    def extract_ga4_data(**context):
        # GA4 API logic here
        pass

    def transform_data(**context):
        # Transform logic here
        pass

    def load_to_warehouse(**context):
        # Load to database/warehouse
        pass

    extract = PythonOperator(
        task_id='extract_ga4_data',
        python_callable=extract_ga4_data,
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load = PythonOperator(
        task_id='load_to_warehouse',
        python_callable=load_to_warehouse,
    )

    extract >> transform >> load
```

## Veelvoorkomende Problemen

```
TROUBLESHOOTING GA4 DATA API
============================

PROBLEEM: 403 Permission Denied
───────────────────────────────
Oorzaken:
├── Service account niet toegevoegd aan GA4
├── Verkeerde property ID
├── API niet enabled
└── Credentials file path incorrect

Oplossing:
├── Verify service account email in GA4 Admin
├── Check property ID (alleen numeriek)
├── Enable Analytics Data API in GCP
└── Verify GOOGLE_APPLICATION_CREDENTIALS path


PROBLEEM: Quota exceeded
────────────────────────
Oorzaken:
├── Te veel requests in korte tijd
├── Te complexe queries
├── Meerdere processen zelfde property
└── Realtime API overuse

Oplossing:
├── Implement exponential backoff
├── Simplificeer queries
├── Coordineer API calls tussen processen
├── Cache responses waar mogelijk

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


PROBLEEM: Data discrepancies met UI
───────────────────────────────────
Oorzaken:
├── Verschillende date ranges
├── Sampling in UI
├── Timezone differences
├── Different metric definitions
└── Real-time vs processed data

Oplossing:
├── Match exact date ranges
├── Vergelijk met unsampled data
├── Verify timezone in beide
├── Check metric API namen
└── Wacht op data processing


PROBLEEM: Empty response
────────────────────────
Oorzaken:
├── Verkeerde dimension/metric namen
├── Filters te restrictief
├── Date range heeft geen data
├── Property ID incorrect
└── Permissions issue

Oplossing:
├── Check exact API namen in documentatie
├── Start zonder filters, voeg toe
├── Verify date range heeft traffic
├── Double-check property ID
└── Verify viewer access in GA4
```

## Output: API Integration Report Template

```markdown
# GA4 Data API Integratie Rapport

## Configuratie Details

| Setting | Waarde |
|---------|--------|
| GA4 Property ID | XXXXXXXXX |
| GCP Project ID | [project-id] |
| Service Account | [email]@[project].iam.gserviceaccount.com |
| API Version | v1beta |
| Setup Datum | [Datum] |

## Authenticatie Status

| Check | Status |
|-------|--------|
| Service Account aangemaakt | ✅ |
| JSON key gedownload | ✅ |
| GA4 Viewer access verleend | ✅ |
| Analytics Data API enabled | ✅ |
| Test query succesvol | ✅ |

## Geïmplementeerde Reports

| Report Naam | Dimensions | Metrics | Schedule |
|-------------|------------|---------|----------|
| Daily Traffic | date, sourceMedium | sessions, users | Dagelijks 06:00 |
| E-commerce | date, itemCategory | revenue, transactions | Dagelijks 07:00 |
| Realtime Dashboard | country | activeUsers | Elke 5 min |

## Quota Gebruik

| Quota Type | Gebruikt | Limiet | % Gebruikt |
|------------|----------|--------|------------|
| Requests/dag | X,XXX | 200,000 | X% |
| Tokens/dag | XX,XXX | 1,750,000 | X% |
| Concurrent | X | 10 | X% |

## Data Output Locaties

| Output | Type | Locatie |
|--------|------|---------|
| Raw exports | CSV | gs://bucket/ga4-exports/ |
| Dashboard data | BigQuery | project.dataset.ga4_reports |
| Looker Studio | Connector | [Dashboard URL] |

## Code Repository

```
/scripts
├── ga4_daily_report.py
├── ga4_ecommerce_report.py
├── requirements.txt
└── README.md
```

## Monitoring & Alerting

- [ ] Quota alerts geconfigureerd
- [ ] Error notifications (email/Slack)
- [ ] Scheduled job monitoring
- [ ] Data freshness checks

## Volgende Stappen

1. [ ] [Volgende actie]
2. [ ] [Volgende actie]
3. [ ] [Volgende actie]

## Notities

[Eventuele aanvullende opmerkingen]
```

---
name: ga4-bigquery-export
description: "BigQuery linking en data warehouse integratie voor GA4. Gebruik voor: (1) BigQuery export configureren, (2) GA4 data queries schrijven, (3) Raw event data analyseren, (4) Custom dashboards met BQ data, (5) Data warehouse integratie. Triggers: bigquery export, ga4 raw data, bq linking, data warehouse, sql analytics, event level data, ga4 bigquery."
---

# GA4 BigQuery Export Guide

Complete gids voor het configureren van BigQuery export en het analyseren van GA4 raw event data.

## Quick Decision Tree

```
GA4 BIGQUERY EXPORT FLOW
│
├─► HEB JE BIGQUERY NODIG?
│   ├─► JA, als je nodig hebt:
│   │   ├─► Raw event-level data
│   │   ├─► Custom attributie modellen
│   │   ├─► Unsampled data
│   │   ├─► Data joins met andere bronnen
│   │   ├─► ML/AI analyses
│   │   └─► Lange termijn data opslag
│   │
│   └─► NEE, GA4 UI voldoet als:
│       ├─► Standaard reports voldoen
│       ├─► Exploration mogelijkheden genoeg
│       └─► Geen externe data joins nodig
│
├─► WELK EXPORT TYPE?
│   ├─► Daily export (gratis)
│   │   └─► Data beschikbaar volgende dag
│   │
│   ├─► Streaming export (GA360)
│   │   └─► Real-time data (binnen minuten)
│   │
│   └─► Fresh daily export (GA360)
│       └─► Meerdere keren per dag
│
└─► KOSTEN OVERWEGINGEN?
    ├─► Storage: ~$0.02/GB/maand
    ├─► Queries: $5/TB gescand
    └─► Optimaliseer met partitioning
```

## BigQuery Export Configureren

```
BIGQUERY LINKING SETUP
======================

VEREISTEN:
├── Google Cloud Project met billing enabled
├── BigQuery API enabled
├── GA4 property Editor of Admin access
└── BigQuery Admin rechten in GCP project

STAP 1: GCP PROJECT VOORBEREIDEN
────────────────────────────────
1. Ga naar console.cloud.google.com
2. Create project of selecteer bestaand project
3. Enable BigQuery API:
   └── APIs & Services → Enable APIs → BigQuery API

4. Billing setup (verplicht voor export)

STAP 2: GA4 BIGQUERY LINK MAKEN
───────────────────────────────
LOCATIE: GA4 Admin → Product Links → BigQuery Links

┌────┬────────────────────────────────────────────────────────────────┐
│ 1  │ Click "Link"                                                   │
├────┼────────────────────────────────────────────────────────────────┤
│ 2  │ Selecteer Google Cloud project                                 │
├────┼────────────────────────────────────────────────────────────────┤
│ 3  │ Kies data location (EU/US) - NIET wijzigbaar later!           │
├────┼────────────────────────────────────────────────────────────────┤
│ 4  │ Selecteer data streams om te exporteren                        │
├────┼────────────────────────────────────────────────────────────────┤
│ 5  │ Kies export frequency:                                         │
│    │ ├── Daily (gratis, aanbevolen start)                          │
│    │ └── Streaming (GA360 only)                                    │
├────┼────────────────────────────────────────────────────────────────┤
│ 6  │ Include advertising ID (optioneel, voor app data)             │
├────┼────────────────────────────────────────────────────────────────┤
│ 7  │ Click "Submit"                                                 │
└────┴────────────────────────────────────────────────────────────────┘

⚠️ BELANGRIJK:
├── Data location (EU/US) kan NIET gewijzigd worden
├── Kies DEZELFDE regio als andere data voor joins
├── Export begint meestal binnen 24 uur
└── Historische data wordt NIET geëxporteerd
```

## BigQuery Dataset Structuur

```
GA4 BIGQUERY DATASET STRUCTUUR
==============================

DATASET NAAM FORMAT:
analytics_[PROPERTY_ID]

TABELLEN:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Tabel                   │ Beschrijving                             │
├─────────────────────────┼──────────────────────────────────────────┤
│ events_YYYYMMDD         │ Daily export tabel (gepartitioneerd)     │
├─────────────────────────┼──────────────────────────────────────────┤
│ events_intraday_YYYYMMDD│ Streaming export (GA360)                 │
├─────────────────────────┼──────────────────────────────────────────┤
│ pseudonymous_users_*    │ User data export (indien enabled)        │
└─────────────────────────┴──────────────────────────────────────────┘

TABEL SCHEMA (VEREENVOUDIGD):
─────────────────────────────
┌─────────────────────────┬───────────┬────────────────────────────────┐
│ Kolom                   │ Type      │ Beschrijving                   │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ event_date              │ STRING    │ Datum (YYYYMMDD)               │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ event_timestamp         │ INTEGER   │ Unix timestamp (microseconds)  │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ event_name              │ STRING    │ Event naam (page_view, etc.)   │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ event_params            │ RECORD    │ REPEATED - Event parameters    │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ user_id                 │ STRING    │ Custom user ID (indien set)    │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ user_pseudo_id          │ STRING    │ GA4 client ID                  │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ user_properties         │ RECORD    │ REPEATED - User properties     │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ device                  │ RECORD    │ Device info (category, etc.)   │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ geo                     │ RECORD    │ Geo info (country, city)       │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ traffic_source          │ RECORD    │ Session traffic source         │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ ecommerce               │ RECORD    │ E-commerce data                │
├─────────────────────────┼───────────┼────────────────────────────────┤
│ items                   │ RECORD    │ REPEATED - Product items       │
└─────────────────────────┴───────────┴────────────────────────────────┘
```

## Basis Query Voorbeelden

```sql
-- ============================================
-- GA4 BIGQUERY BASIS QUERIES
-- ============================================

-- 1. EVENTS TELLEN PER DAG
-- ────────────────────────
SELECT
  event_date,
  event_name,
  COUNT(*) as event_count
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
GROUP BY
  event_date, event_name
ORDER BY
  event_date, event_count DESC;


-- 2. UNIEKE USERS PER DAG
-- ───────────────────────
SELECT
  event_date,
  COUNT(DISTINCT user_pseudo_id) as unique_users
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
GROUP BY
  event_date
ORDER BY
  event_date;


-- 3. PAGE VIEWS MET PAGE LOCATION
-- ───────────────────────────────
SELECT
  event_date,
  (SELECT value.string_value
   FROM UNNEST(event_params)
   WHERE key = 'page_location') as page_url,
  COUNT(*) as pageviews
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name = 'page_view'
GROUP BY
  event_date, page_url
ORDER BY
  pageviews DESC
LIMIT 100;


-- 4. EVENT PARAMETERS EXTRACTEN
-- ─────────────────────────────
SELECT
  event_date,
  event_name,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_title') as page_title,
  (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'engagement_time_msec') as engagement_time,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'session_engaged') as session_engaged
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX = '20240115'
  AND event_name = 'page_view'
LIMIT 100;
```

## E-commerce Queries

```sql
-- ============================================
-- GA4 BIGQUERY E-COMMERCE QUERIES
-- ============================================

-- 1. PURCHASE TRANSACTIONS
-- ────────────────────────
SELECT
  event_date,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'transaction_id') as transaction_id,
  ecommerce.purchase_revenue as revenue,
  ecommerce.total_item_quantity as items_qty,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'coupon') as coupon_code
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name = 'purchase'
ORDER BY
  event_date DESC;


-- 2. PRODUCT PERFORMANCE
-- ──────────────────────
SELECT
  items.item_name,
  items.item_brand,
  items.item_category,
  SUM(items.quantity) as total_quantity,
  SUM(items.item_revenue) as total_revenue,
  COUNT(DISTINCT
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'transaction_id')
  ) as transaction_count
FROM
  `project.analytics_XXXXXX.events_*`,
  UNNEST(items) as items
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  AND event_name = 'purchase'
GROUP BY
  items.item_name, items.item_brand, items.item_category
ORDER BY
  total_revenue DESC
LIMIT 50;


-- 3. CHECKOUT FUNNEL ANALYSE
-- ──────────────────────────
WITH funnel_events AS (
  SELECT
    user_pseudo_id,
    event_name,
    event_timestamp
  FROM
    `project.analytics_XXXXXX.events_*`
  WHERE
    _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
    AND event_name IN ('view_cart', 'begin_checkout', 'add_shipping_info', 'add_payment_info', 'purchase')
)
SELECT
  event_name,
  COUNT(DISTINCT user_pseudo_id) as users
FROM
  funnel_events
GROUP BY
  event_name
ORDER BY
  CASE event_name
    WHEN 'view_cart' THEN 1
    WHEN 'begin_checkout' THEN 2
    WHEN 'add_shipping_info' THEN 3
    WHEN 'add_payment_info' THEN 4
    WHEN 'purchase' THEN 5
  END;


-- 4. REVENUE PER TRAFFIC SOURCE
-- ─────────────────────────────
SELECT
  traffic_source.source,
  traffic_source.medium,
  COUNT(DISTINCT user_pseudo_id) as users,
  COUNT(DISTINCT
    CASE WHEN event_name = 'purchase'
    THEN (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'transaction_id')
    END
  ) as transactions,
  SUM(
    CASE WHEN event_name = 'purchase'
    THEN ecommerce.purchase_revenue
    ELSE 0 END
  ) as total_revenue
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
GROUP BY
  traffic_source.source, traffic_source.medium
ORDER BY
  total_revenue DESC;
```

## User Journey Queries

```sql
-- ============================================
-- GA4 BIGQUERY USER JOURNEY QUERIES
-- ============================================

-- 1. USER PATH NAAR PURCHASE
-- ──────────────────────────
WITH purchase_users AS (
  SELECT DISTINCT user_pseudo_id
  FROM `project.analytics_XXXXXX.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
    AND event_name = 'purchase'
),
user_events AS (
  SELECT
    e.user_pseudo_id,
    e.event_name,
    e.event_timestamp,
    ROW_NUMBER() OVER (PARTITION BY e.user_pseudo_id ORDER BY e.event_timestamp) as event_sequence
  FROM `project.analytics_XXXXXX.events_*` e
  INNER JOIN purchase_users p ON e.user_pseudo_id = p.user_pseudo_id
  WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
)
SELECT
  event_sequence,
  event_name,
  COUNT(*) as occurrences
FROM user_events
WHERE event_sequence <= 10
GROUP BY event_sequence, event_name
ORDER BY event_sequence, occurrences DESC;


-- 2. TIJD TOT CONVERSIE
-- ─────────────────────
WITH first_visit AS (
  SELECT
    user_pseudo_id,
    MIN(event_timestamp) as first_timestamp
  FROM `project.analytics_XXXXXX.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
  GROUP BY user_pseudo_id
),
purchases AS (
  SELECT
    user_pseudo_id,
    MIN(event_timestamp) as purchase_timestamp
  FROM `project.analytics_XXXXXX.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'
    AND event_name = 'purchase'
  GROUP BY user_pseudo_id
)
SELECT
  CASE
    WHEN time_to_purchase_hours < 1 THEN '< 1 uur'
    WHEN time_to_purchase_hours < 24 THEN '1-24 uur'
    WHEN time_to_purchase_hours < 168 THEN '1-7 dagen'
    WHEN time_to_purchase_hours < 720 THEN '7-30 dagen'
    ELSE '> 30 dagen'
  END as time_bucket,
  COUNT(*) as conversions
FROM (
  SELECT
    f.user_pseudo_id,
    (p.purchase_timestamp - f.first_timestamp) / 3600000000 as time_to_purchase_hours
  FROM first_visit f
  INNER JOIN purchases p ON f.user_pseudo_id = p.user_pseudo_id
)
GROUP BY time_bucket
ORDER BY
  CASE time_bucket
    WHEN '< 1 uur' THEN 1
    WHEN '1-24 uur' THEN 2
    WHEN '1-7 dagen' THEN 3
    WHEN '7-30 dagen' THEN 4
    ELSE 5
  END;


-- 3. SESSIE RECONSTRUCTIE
-- ───────────────────────
SELECT
  user_pseudo_id,
  (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') as session_id,
  MIN(TIMESTAMP_MICROS(event_timestamp)) as session_start,
  MAX(TIMESTAMP_MICROS(event_timestamp)) as session_end,
  COUNT(*) as event_count,
  COUNTIF(event_name = 'page_view') as pageviews,
  MAX(CASE WHEN event_name = 'purchase' THEN 1 ELSE 0 END) as converted
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX = '20240115'
GROUP BY
  user_pseudo_id, session_id
ORDER BY
  session_start DESC
LIMIT 100;
```

## Query Optimalisatie Tips

```
BIGQUERY KOSTEN OPTIMALISATIE
=============================

PARTITIONING GEBRUIKEN:
───────────────────────
✅ GOED - Specifieke datum suffix:
WHERE _TABLE_SUFFIX = '20240115'

✅ GOED - Date range met suffix:
WHERE _TABLE_SUFFIX BETWEEN '20240101' AND '20240131'

❌ SLECHT - Alle tabellen scannen:
WHERE event_date = '2024-01-15'  -- Scant ALLE tabellen!

KOLOM SELECTIE:
───────────────
✅ GOED - Specifieke kolommen:
SELECT event_name, event_date, user_pseudo_id

❌ SLECHT - Alle kolommen:
SELECT * FROM events_*

NESTED FIELDS EFFICIËNT:
────────────────────────
-- Unnest ALLEEN wanneer nodig
-- Gebruik subquery voor event_params

✅ GOED:
SELECT
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_title')

❌ MINDER EFFICIËNT:
SELECT ep.value.string_value
FROM events, UNNEST(event_params) as ep
WHERE ep.key = 'page_title'

CACHING EN MATERIALIZED VIEWS:
──────────────────────────────
-- Maak materialized view voor frequent gebruikte queries

CREATE MATERIALIZED VIEW `project.dataset.daily_metrics`
AS
SELECT
  event_date,
  COUNT(DISTINCT user_pseudo_id) as users,
  COUNTIF(event_name = 'purchase') as purchases
FROM `project.analytics_XXXXXX.events_*`
WHERE _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
GROUP BY event_date;

KOSTEN SCHATTING:
─────────────────
┌─────────────────────┬──────────────────────────────────────────────┐
│ Tabel grootte       │ Geschatte maandelijkse kosten                │
├─────────────────────┼──────────────────────────────────────────────┤
│ 10 GB/maand         │ Storage: ~$0.20 + Queries: variable          │
├─────────────────────┼──────────────────────────────────────────────┤
│ 100 GB/maand        │ Storage: ~$2.00 + Queries: variable          │
├─────────────────────┼──────────────────────────────────────────────┤
│ 1 TB/maand          │ Storage: ~$20.00 + Queries: variable         │
└─────────────────────┴──────────────────────────────────────────────┘

Query kosten: $5 per TB gescand (on-demand pricing)
```

## Looker Studio Integratie

```
BIGQUERY → LOOKER STUDIO
========================

CONNECTIE MAKEN:
────────────────
1. Ga naar lookerstudio.google.com
2. Create → Data source → BigQuery
3. Selecteer project → dataset → tabel
4. (Optioneel) Custom query gebruiken

CUSTOM QUERY DATA SOURCE:
─────────────────────────
Voordelen:
├── Pre-aggregated data (sneller)
├── Complexe berekeningen
├── Joins met andere bronnen
└── Lagere query kosten

Voorbeeld:
SELECT
  event_date,
  traffic_source.source,
  traffic_source.medium,
  COUNT(DISTINCT user_pseudo_id) as users,
  COUNTIF(event_name = 'purchase') as purchases,
  SUM(CASE WHEN event_name = 'purchase' THEN ecommerce.purchase_revenue END) as revenue
FROM
  `project.analytics_XXXXXX.events_*`
WHERE
  _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
GROUP BY
  event_date, traffic_source.source, traffic_source.medium

PARAMETER IN QUERY (Date range):
────────────────────────────────
SELECT *
FROM `project.analytics_XXXXXX.events_*`
WHERE _TABLE_SUFFIX BETWEEN
  FORMAT_DATE('%Y%m%d', @DS_START_DATE)
  AND FORMAT_DATE('%Y%m%d', @DS_END_DATE)

BLENDING MET ANDERE DATA:
─────────────────────────
├── Blend GA4 BQ data met CRM data
├── Join met ad spend data
├── Combineer met product database
└── Match met offline sales
```

## Veelvoorkomende Problemen

```
TROUBLESHOOTING BIGQUERY EXPORT
===============================

PROBLEEM: Geen data in BigQuery
───────────────────────────────
Oorzaken:
├── Link net gemaakt (wacht 24-48 uur)
├── Verkeerde project geselecteerd
├── BigQuery API niet enabled
├── Billing niet actief
└── Geen events in GA4

Oplossing:
├── Wacht minimaal 24 uur na linking
├── Verify correct GCP project
├── Check BigQuery API status
├── Verify billing is enabled
└── Verify GA4 ontvangt data


PROBLEEM: Discrepantie GA4 UI vs BigQuery
─────────────────────────────────────────
Oorzaken:
├── Sampling in GA4 UI
├── Data processing timing
├── Session definities verschillen
├── Consent mode differences
└── Timezone verschillen

Oplossing:
├── BQ heeft RAW data (geen sampling)
├── Vergelijk zelfde tijdsperiodes
├── Gebruik zelfde session definitie
├── Filter op consent_granted indien nodig
├── Match timezones in queries


PROBLEEM: Queries te duur
─────────────────────────
Oorzaken:
├── Te brede date ranges
├── SELECT * gebruiken
├── Inefficiënte UNNEST
├── Geen partitioning filter
└── Herhaalde queries

Oplossing:
├── Specifieke date suffixes
├── Selecteer alleen nodige kolommen
├── Gebruik subqueries voor nested data
├── ALTIJD _TABLE_SUFFIX filter
├── Maak scheduled queries/views


PROBLEEM: Event parameters ontbreken
────────────────────────────────────
Oorzaken:
├── Custom events niet correct geïmplementeerd
├── Parameter registratie in GA4 admin
├── Data processing delay
└── Verkeerde parameter naam

Oplossing:
├── Verify event in GA4 DebugView
├── Check custom dimensions setup
├── Wacht op volledige processing
├── Query alle beschikbare keys:

-- Vind alle event parameter keys:
SELECT DISTINCT
  ep.key
FROM
  `project.analytics_XXXXXX.events_*`,
  UNNEST(event_params) as ep
WHERE
  _TABLE_SUFFIX = '20240115'
  AND event_name = 'your_event'
```

## Output: BigQuery Setup Report Template

```markdown
# GA4 BigQuery Export Setup Rapport

## Configuratie Details

| Setting | Waarde |
|---------|--------|
| GA4 Property ID | XXXXXXXXX |
| GCP Project ID | [project-id] |
| BigQuery Dataset | analytics_XXXXXXXXX |
| Data Location | EU / US |
| Export Type | Daily / Streaming |
| Link Datum | [Datum] |

## Data Streams Geëxporteerd

| Stream Name | Measurement ID | Status |
|-------------|----------------|--------|
| Web - example.com | G-XXXXXXXXXX | ✅ Active |
| iOS App | [ID] | ✅ Active |
| Android App | [ID] | ⏳ Pending |

## Tabel Beschikbaarheid

| Tabel Type | Eerste Datum | Laatste Datum | Status |
|------------|--------------|---------------|--------|
| events_YYYYMMDD | 2024-01-15 | [Gisteren] | ✅ Actief |
| events_intraday | N/A | N/A | ❌ Niet geactiveerd |

## Schema Verificatie

| Veld | Aanwezig | Data Type |
|------|----------|-----------|
| event_date | ✅ | STRING |
| event_name | ✅ | STRING |
| event_params | ✅ | RECORD |
| user_pseudo_id | ✅ | STRING |
| ecommerce | ✅ | RECORD |
| items | ✅ | RECORD |

## Query Templates Geleverd

- [ ] Daily metrics query
- [ ] E-commerce performance query
- [ ] User journey query
- [ ] Checkout funnel query
- [ ] Traffic source revenue query

## Kosten Schatting

| Component | Geschatte Maandkosten |
|-----------|----------------------|
| Storage (~XX GB) | €X.XX |
| Queries (geschat) | €XX.XX |
| **Totaal** | **€XX.XX** |

## Looker Studio Integratie

| Dashboard | Data Source | Status |
|-----------|-------------|--------|
| [Dashboard naam] | BQ Custom Query | ✅ Actief |

## Volgende Stappen

1. [ ] Materialized views aanmaken voor frequent gebruikte queries
2. [ ] Scheduled queries opzetten voor dagelijkse exports
3. [ ] Data retention policy configureren
4. [ ] Team toegang configureren

## Notities

[Eventuele aanvullende opmerkingen of aandachtspunten]
```

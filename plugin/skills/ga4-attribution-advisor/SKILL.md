---
name: ga4-attribution-advisor
description: "This skill should be used when the user asks to \"choose an attribution model\", \"compare DDA vs last-click\", \"configure attribution windows\", or mentions \"cross-channel attribution\", \"first-click vs position-based\", or \"GA4 model comparison\". Do NOT use for: conversion import to Google Ads (use ga4-conversion-import), channel grouping configuration (use ga4-channel-groupings)."
---
# GA4 Attribution Advisor

Complete guide for choosing and configuring the right attribution model in Google Analytics 4 for accurate conversion attribution.

## Quick Decision Tree

```
GA4 ATTRIBUTION MODEL SELECTION
│
├─► WHAT IS YOUR PRIMARY GOAL?
│   ├─► Maximum Smart Bidding performance
│   │   └─► DATA-DRIVEN ATTRIBUTION (DDA)
│   │       └─► Recommended for Google Ads
│   │
│   ├─► Simple, predictable reporting
│   │   └─► PAID AND ORGANIC LAST CLICK
│   │       └─► Easy to explain to stakeholders
│   │
│   └─► Only Google paid channels should get credit
│       └─► GOOGLE PAID CHANNELS LAST CLICK
│
├─► FIRST CLICK, LINEAR, POSITION-BASED OR TIME DECAY?
│   └─► Removed from GA4 in 2023; not selectable
│       └─► For awareness value, read early touchpoints in Conversion paths
│
└─► WHICH CHANNELS DO YOU USE?
    ├─► Only Google Ads
    │   └─► DDA in Google Ads
    │   └─► Sync with GA4 for consistency
    │
    ├─► Google + Meta/LinkedIn/TikTok
    │   └─► GA4 DDA as a common yardstick, beside each platform's own numbers
    │   └─► Cross-channel comparison reports
    │
    └─► Complex multi-touch journey
        └─► DDA with Model Comparison tool
        └─► Analyze touchpoint value
```

## Attribution Models Comparison

```
ATTRIBUTION MODELS OVERVIEW
============================

GA4 offers three reporting attribution models (Google Analytics Help,
"Get started with attribution"):

┌─────────────────┬───────────────────────────────────────────────────────┐
│ Model           │ How it works                                          │
├─────────────────┼───────────────────────────────────────────────────────┤
│ DATA-DRIVEN     │ Credit per touchpoint from conversion patterns in     │
│ (DDA)           │ your data; one model per advertiser and key event     │
│                 │ Best for: holistic, cross-channel view                │
├─────────────────┼───────────────────────────────────────────────────────┤
│ PAID AND        │ 100% credit to the last channel clicked               │
│ ORGANIC LAST    │ (direct traffic is ignored)                           │
│ CLICK           │ Drawback: undervalues upper funnel                    │
├─────────────────┼───────────────────────────────────────────────────────┤
│ GOOGLE PAID     │ 100% credit to the last Google Ads channel clicked;   │
│ CHANNELS LAST   │ without a Google Ads click it falls back to paid and  │
│ CLICK           │ organic last click                                    │
│                 │ Best for: comparing GA4 with Google Ads reporting     │
└─────────────────┴───────────────────────────────────────────────────────┘

First click, linear, time decay and position-based were removed in 2023.

EXAMPLE: Customer Journey with 4 touchpoints
─────────────────────────────────────────────
Touchpoints: Google Ads → Organic → Email → Direct → Conversion (EUR 100)

Model comparison:
┌──────────────────────────┬───────────┬─────────┬─────────┬────────┐
│ Model                    │ Google Ads│ Organic │ Email   │ Direct │
├──────────────────────────┼───────────┼─────────┼─────────┼────────┤
│ Paid and organic LC      │ EUR 0     │ EUR 0   │ EUR 100 │ EUR 0* │
│ Google paid channels LC  │ EUR 100   │ EUR 0   │ EUR 0   │ EUR 0  │
│ DDA (illustration)       │ EUR 35    │ EUR 25  │ EUR 40  │ EUR 0  │
└──────────────────────────┴───────────┴─────────┴─────────┴────────┘
*Direct is ignored, unless the whole path is direct visits
```

## Configuring GA4 Attribution

```
CONFIGURING ATTRIBUTION SETTINGS
==================================

LOCATION: Admin → Attribution Settings

STEP 1: REPORTING ATTRIBUTION MODEL
────────────────────────────────────
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Go to Admin → Attribution Settings                        │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Under "Reporting attribution model" select:               │
│    │ - Data-driven (recommended if available)                   │
│    │ - Paid and organic last click                              │
│    │ - Google paid channels last click                          │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Choose "Acquisition conversion events" scope               │
│    │ (first user touchpoint vs session-based)                   │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Click "Save"                                               │
└────┴────────────────────────────────────────────────────────────┘

IMPORTANT:
├── Changes are NOT retroactive
├── New model applies from moment of change
├── Historical data retains old attribution
└── Test first with Model Comparison tool

STEP 2: LOOKBACK WINDOWS
─────────────────────────
┌────────────────────────┬────────────────────────────────────────┐
│ Setting                │ Recommendation                         │
├────────────────────────┼────────────────────────────────────────┤
│ Acquisition events     │ 30 days (default)                      │
│ lookback window        │ Extend for long sales cycles           │
├────────────────────────┼────────────────────────────────────────┤
│ All other events       │ 90 days (default)                      │
│ lookback window        │ B2B: consider 90 days                  │
│                        │ E-commerce: 30 days often sufficient   │
├────────────────────────┼────────────────────────────────────────┤
│ Maximum                │ 90 days                                │
│                        │ GA360: up to 1 year possible           │
└────────────────────────┴────────────────────────────────────────┘

LOOKBACK WINDOW BY INDUSTRY:
├── E-commerce: 7-30 days (fast decisions)
├── SaaS: 30-60 days (consideration phase)
├── B2B: 60-90 days (long sales cycles)
├── Real estate: 90 days (very long cycles)
└── Lead gen: 30-60 days (depends on product)
```

## Data-Driven Attribution (DDA)

```
DATA-DRIVEN ATTRIBUTION DETAILS
================================

HOW DDA WORKS:
├── Analyzes all customer journeys
├── Compares converting vs non-converting paths
├── Calculates incremental value per touchpoint
├── Applies machine learning to your specific data
└── Continuously updates based on new data

DATA REQUIREMENTS:
├── Google documents no minimum conversion or traffic volume for DDA
├── Depending on data availability, the model can use aggregate data
│   (Data sharing settings)
└── Conversions can be reattributed for up to 7 days after they happen

DDA VS GOOGLE ADS DDA:
──────────────────────
┌─────────────────────┬───────────────────┬───────────────────┐
│ Aspect              │ GA4 DDA           │ Google Ads DDA    │
├─────────────────────┼───────────────────┼───────────────────┤
│ Data scope          │ All channels      │ Google Ads only   │
├─────────────────────┼───────────────────┼───────────────────┤
│ Cross-device        │ Google Signals    │ Google accounts   │
├─────────────────────┼───────────────────┼───────────────────┤
│ Touchpoints         │ Web + App         │ Ads clicks only   │
├─────────────────────┼───────────────────┼───────────────────┤
│ Best for            │ Holistic view     │ Google Ads optim. │
└─────────────────────┴───────────────────┴───────────────────┘

EXPECT DIFFERENCES:
├── GA4 and Google Ads DDA give different results
├── This is NORMAL (different data scopes)
├── Choose one source as "source of truth"
└── Document choice for stakeholders
```

## Model Comparison Analysis

```
MODEL COMPARISON TOOL
=====================

LOCATION: Advertising → Attribution → Model Comparison

HOW TO USE:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Select date range (minimum 28 days)                       │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Choose dimension: Default Channel Group or Source/Medium   │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Select two models to compare                              │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Analyze conversion and revenue differences                │
└────┴────────────────────────────────────────────────────────────┘

ANALYSIS FRAMEWORK:
───────────────────

Compare DDA vs Last Click:

┌─────────────────────┬────────────┬────────────┬─────────────────┐
│ Channel             │ DDA Conv.  │ LC Conv.   │ Difference      │
├─────────────────────┼────────────┼────────────┼─────────────────┤
│ Paid Search         │ 120        │ 100        │ +20% (Upper)    │
│ Display             │ 45         │ 20         │ +125% (Intro)   │
│ Organic Search      │ 80         │ 95         │ -16% (Closer)   │
│ Email               │ 55         │ 85         │ -35% (Closer)   │
└─────────────────────┴────────────┴────────────┴─────────────────┘

INTERPRETATION:
├── Channel gets MORE credit in DDA = strong upper funnel role
├── Channel gets LESS credit in DDA = strong closer role
├── Large differences = channel has specific journey position
└── Small differences = consistent across entire journey

ACTION MATRIX:
┌───────────────────────────┬────────────────────────────────────┐
│ Finding                   │ Action                             │
├───────────────────────────┼────────────────────────────────────┤
│ Display: DDA >> LC        │ Increase Display budget            │
│ (undervalued in LC)       │ Awareness value is higher          │
├───────────────────────────┼────────────────────────────────────┤
│ Email: DDA << LC          │ Email is a strong closer           │
│ (overvalued in LC)        │ Invest in list growth              │
├───────────────────────────┼────────────────────────────────────┤
│ Paid Search: DDA ~ LC     │ Consistent performer               │
│ (little difference)       │ Stable channel, maintain budget    │
└───────────────────────────┴────────────────────────────────────┘
```

## Conversion Paths Analysis

```
CONVERSION PATH ANALYSIS
=========================

LOCATION: Advertising → Attribution → Conversion Paths

WHAT YOU LEARN:
├── Average number of touchpoints to conversion
├── Most common channel sequences
├── Time to conversion (days to convert)
└── Touchpoint patterns per segment

KEY METRICS:
┌─────────────────────────┬────────────────────────────────────────┐
│ Metric                  │ What it means                          │
├─────────────────────────┼────────────────────────────────────────┤
│ Avg. touchpoints        │ Average journey length                 │
│                         │ Lower = direct response                │
│                         │ Higher = consideration needed          │
├─────────────────────────┼────────────────────────────────────────┤
│ Days to conversion      │ Typical sales cycle                    │
│                         │ Basis for lookback window              │
├─────────────────────────┼────────────────────────────────────────┤
│ Early touchpoints       │ Awareness drivers                      │
│                         │ Often: Display, Video, Social          │
├─────────────────────────┼────────────────────────────────────────┤
│ Late touchpoints        │ Conversion drivers                     │
│                         │ Often: Brand Search, Email, Direct     │
└─────────────────────────┴────────────────────────────────────────┘

TYPICAL CONVERSION PATHS:
──────────────────────────

E-commerce (short cycle):
├── Display → Paid Search → Organic → Purchase
├── Social → Direct → Purchase
└── Avg: 2-3 touchpoints, 3-7 days

B2B SaaS (long cycle):
├── Content → Paid Search → Demo Page → Email → Meeting → Sign-up
├── LinkedIn → Blog → Webinar → Sales Call → Contract
└── Avg: 5-8 touchpoints, 30-90 days

Lead Generation:
├── Paid Search → Landing → Email Nurture → Conversion
├── Display → Organic → Form Submit
└── Avg: 2-4 touchpoints, 7-21 days
```

## Troubleshooting Attribution

```
ATTRIBUTION TROUBLESHOOTING
============================

PROBLEM: DDA credit looks unstable
───────────────────────────────────
Causes:
├── Few conversions for that key event
├── New property or recently changed tracking
└── Reattribution in the first 7 days after a conversion

Solution:
├── Read DDA over longer periods (28+ days)
├── Exclude the last 7 days when comparing periods
├── Combine micro-conversions into one key event where that matches the goal
└── Use Paid and organic last click for that report until volume grows

PROBLEM: Attribution data differs from platform data
─────────────────────────────────────────────────────
Causes:
├── Different attribution windows
├── View-through vs click-through difference
├── Cross-device tracking gaps
├── Consent mode impact
└── Platform-specific attribution (Meta, etc.)

Solution:
├── Document expected differences (10-30% is normal)
├── Pick one common yardstick (GA4 or your CRM) and show it beside each platform's own numbers
├── Align lookback windows where possible
└── Accept that platforms over-attribute to themselves

PROBLEM: Direct traffic gets a lot of credit
─────────────────────────────────────────────
Causes:
├── Missing UTM parameters
├── JavaScript blocking
├── App traffic without tracking
├── Bookmarks and typed URLs
└── Dark social (copied links)

Solution:
├── Audit UTM implementation
├── Check cross-domain tracking
├── Implement link shorteners with tracking
└── Accept that ~20% direct is normal

PROBLEM: Organic gets little credit in DDA
───────────────────────────────────────────
Causes:
├── Organic often in middle of journey
├── Brand searches attributed to other touchpoints
├── Last click bias in many journeys
└── DDA values incremental value

Solution:
├── Analyze conversion paths for organic's role
├── Split brand vs non-brand organic
├── Read early touchpoints in Conversion paths for awareness value
└── Organic value is often higher than DDA shows
```

## Where the settings live

GA4 has two separate places (Analytics Help, "Get started with attribution"):

- **Key event reporting:** the reporting attribution model and lookback windows for the property's
  reports, in Admin > Data display > Events > Attribution settings. It applies to the whole property.
- **Conversion settings:** conversions shared with Google Ads are managed in Advertising > Conversion
  management, including which channels are eligible for credit ("Google paid channels" shows
  conversions from Google Ads only).

Google documents no attribution model per individual key event; do not recommend one.

## MCP Tool: Run Attribution Comparison

```python
# Compare conversions by channel for attribution analysis
ga4_run_report(
    property_id="YOUR_PROPERTY_ID",
    metrics=["keyEvents", "sessionKeyEventRate", "totalRevenue"],
    dimensions=["sessionDefaultChannelGroup", "date"],
    start_date="90daysAgo",
    end_date="yesterday"
)
```

## Output: Attribution Analysis Template

```markdown
# GA4 Attribution Analysis Report

## Property & Period
- **Property:** [Property name]
- **Analysis period:** [Start] - [End]
- **Current attribution model:** [Model]
- **Lookback window:** [X] days

## Current Settings
| Setting | Value |
|---------|-------|
| Reporting attribution model | [Data-driven / Paid and organic last click / Google paid channels last click] |
| Key event lookback window | [X] days |
| Key events per month | [X] |

## Model Comparison Results

### DDA vs Last Click Comparison
| Channel | DDA Conv. | LC Conv. | Difference | Interpretation |
|---------|-----------|----------|------------|----------------|
| Paid Search | [X] | [X] | [+/-X%] | [Upper/Lower funnel] |
| Display | [X] | [X] | [+/-X%] | [Upper/Lower funnel] |
| Organic | [X] | [X] | [+/-X%] | [Upper/Lower funnel] |
| Social | [X] | [X] | [+/-X%] | [Upper/Lower funnel] |
| Email | [X] | [X] | [+/-X%] | [Upper/Lower funnel] |

## Conversion Path Insights
- **Avg. touchpoints to conversion:** [X]
- **Avg. days to conversion:** [X]
- **Most common path:** [Path description]

## Attribution Model Recommendation

### Recommended Model: [MODEL]

**Rationale:**
1. [Reason 1]
2. [Reason 2]
3. [Reason 3]

### Recommended Lookback Window
- **Acquisition events:** [X] days
- **Other conversion events:** [X] days

## Budget Implications
| Channel | Current attribution | DDA attribution | Recommended action |
|---------|--------------------|-----------------|--------------------|
| [Channel] | [EUR X] | [EUR X] | [Increase/Decrease/Maintain] |

## Next Steps
1. [ ] Change attribution model to [Model]
2. [ ] Adjust lookback window to [X] days
3. [ ] Budget reallocation based on DDA insights
4. [ ] Schedule monthly model comparison review

## Notes
[Additional observations and points of attention]
```

---
name: attribution-window-advisor
description: "Meta Ads attribution window advisor voor optimale attribution configuratie. Gebruik voor: (1) Attribution window selectie, (2) Click vs view-through attribution, (3) iOS 14+ attribution strategie, (4) Incremental Attribution setup, (5) Attribution vergelijking met andere platformen. Triggers: attribution, attribution window, click-through, view-through, 7-day click, 1-day view, iOS attribution, AEM, incrementality."
---

# Attribution Window Advisor

Advisor voor het kiezen van de optimale Meta Ads attribution configuratie op basis van product, buying cycle en doelen.

## Attribution Basics

### Wat Is Attribution?

Attribution bepaalt welke ads credit krijgen voor conversies en hoe lang na interactie een conversie nog wordt toegeschreven.

```
Attribution Types:
├── Click-Through: Conversie na klik op ad
├── View-Through: Conversie na zien van ad (geen klik)
└── Engaged-View: Conversie na 10+ sec video view
```

### Beschikbare Windows (Post-iOS 14)

| Window Type | Opties | Default |
|-------------|--------|---------|
| **Click-Through** | 1-day, 7-day | 7-day |
| **View-Through** | 1-day, None | 1-day |
| **Engaged-View** | 1-day, None | 1-day (als VT=1-day) |

**Verwijderd (niet meer beschikbaar):**
- 28-day click
- 28-day view
- 7-day view

## Attribution Window Selection

### Decision Tree

```
WAT IS JE PRODUCT/DIENST?
│
├─► Impulse Purchases (<€50, quick decision)
│   └─► 1-day click, 1-day view
│   └─► Voorbeelden: Fast fashion, accessories, digital products
│
├─► Standard E-commerce (€50-200)
│   └─► 7-day click, 1-day view (DEFAULT)
│   └─► Voorbeelden: Kleding, elektronica, home goods
│
├─► Considered Purchases (€200+, research phase)
│   └─► 7-day click, 1-day view
│   └─► Voorbeelden: Meubels, luxe items, tech
│
├─► Lead Generation (B2B/Services)
│   └─► 7-day click, 1-day view
│   └─► Lange sales cycle = 7-day click minimum
│
└─► High-Ticket / Long Sales Cycle
    └─► 7-day click, 1-day view
    └─► Supplement met external attribution tools
```

### Recommendation Matrix

| Scenario | Click Window | View Window | Rationale |
|----------|--------------|-------------|-----------|
| **Default (most cases)** | 7-day | 1-day | Balanced data collection |
| **Impulse/Flash sales** | 1-day | 1-day | Short decision cycle |
| **Brand awareness** | 7-day | 1-day | Capture delayed action |
| **Retargeting** | 7-day | 1-day | Users already familiar |
| **Strict ROAS targets** | 7-day | None | Minimize inflated metrics |
| **High-consideration B2B** | 7-day | 1-day | Research-heavy buying |

## Click-Through vs View-Through

### Understanding the Difference

```
CLICK-THROUGH ATTRIBUTION:
├── User clicks ad
├── User converts within window
├── Conversion credited to ad
└── Stronger causation signal

VIEW-THROUGH ATTRIBUTION:
├── User sees ad (no click)
├── User converts within window (andere path)
├── Conversion credited to ad
└── Measures awareness/influence

ENGAGED-VIEW (Video only):
├── User watches 10+ seconds (of 97% als <10 sec)
├── User converts within 1 day
├── Requires View-Through = 1-day
└── Middle ground between click and view
```

### When to Use View-Through

```
ENABLE VIEW-THROUGH (1-day) WANNEER:
├── Brand awareness belangrijk
├── Wilt volledige ad impact meten
├── Video ads prominent in mix
├── Upper-funnel campaigns
└── Budget voor incremental reach

DISABLE VIEW-THROUGH (None) WANNEER:
├── Strict ROAS accountability
├── Comparison met andere kanalen
├── Minimizing attribution overlap
├── Focus op direct response only
└── Incremental measurement priority
```

### View-Through Impact

```
View-Through Effect op Metrics:
├── ROAS: Typisch 10-30% hoger met VT enabled
├── Conversions: 15-40% meer reported
└── CPA: Lijkt lager (meer conversies toegeschreven)

Let op:
- VT conversies zijn NIET fake
- Ze meten brand influence
- Maar zijn minder "incremental"
- Vergelijk altijd apples-to-apples
```

## iOS 14+ Attribution

### Impact Overview

```
iOS 14.5+ (App Tracking Transparency):
├── Meeste users opt-out van tracking
├── Beperkte conversion visibility
├── Tot 72 uur delay voor iOS conversions
├── Aggregated Event Measurement (AEM)
└── Modeled conversions door Meta

Praktische Impact:
├── Reported conversions ~15-25% onder actual
├── Data delay voor iOS traffic
├── Cross-device attribution beperkt
└── View-through minder betrouwbaar voor iOS
```

### Aggregated Event Measurement (AEM)

```
Wat AEM Doet:
├── Aggregeert iOS conversion data
├── Privacy-compliant measurement
├── Removed device identifiers
├── Applies modeling en noise

2025 Update:
├── 8-event limit VERWIJDERD
├── Manual prioritization niet meer nodig
├── AEM nu automatisch voor eligible events
└── Advanced Mobile Measurement (AMM) enabled
```

### iOS Attribution Strategy

```
RECOMMENDED SETUP:

1. Event Configuration:
   ├── Focus op high-value events (Purchase)
   ├── CAPI implementatie essentieel
   ├── Enable Aggregated Event Measurement
   └── No manual event ranking needed (2025+)

2. Attribution Expectations:
   ├── Accept 20-30% underreporting
   ├── Use modeled conversions
   ├── Supplement met post-purchase surveys
   └── Cross-reference met platform data

3. Optimization Approach:
   ├── Trust Meta's modeled data
   ├── Focus op trends, niet absolute numbers
   ├── Compare period-over-period
   └── Use multiple measurement sources
```

## Incremental Attribution (2025)

### What Is Incremental Attribution?

```
Traditionele Attribution:
├── Telt alle conversies na ad exposure
├── Inclusief conversies die toch waren gebeurd
└── Kan overclaiming veroorzaken

Incremental Attribution:
├── Meet ALLEEN conversies DOOR de ad
├── Excludeert organic conversions
├── Holdout-based measurement
└── True ad effectiveness
```

### Meta's Incremental Attribution Setting

```
Hoe Te Enablen:
1. Campaign settings
2. Attribution section
3. Enable "Incremental Attribution"
4. Select conversion event

Impact:
├── Reported conversions LAGER (alleen incremental)
├── ROAS meer accurate (true ad value)
├── Algorithm optimizes for incremental lift
└── Early adopters: 20%+ improvement in true ROI
```

### When to Use Incremental Attribution

```
USE INCREMENTAL WANNEER:
├── High retargeting spend
├── Strong organic conversion base
├── Need true incrementality measurement
├── Budget optimization priority
└── Advanced measurement maturity

STICK TO STANDARD WANNEER:
├── Low conversion volume
├── New accounts/campaigns
├── Primarily prospecting
├── Need learning phase data
└── Simple measurement needs
```

## Attribution Comparison Framework

### Meta vs Google Attribution

```
COMPARISON NOTES:
├── Different attribution models
├── Different tracking methods
├── Overlap in conversions
└── Don't add together!

Meta Attribution:
├── People-based (logged-in users)
├── Cross-device by default
├── View-through included
└── Click: 7-day, View: 1-day

Google Ads:
├── Cookie/click-based
├── Last-click default (changing)
├── No view-through for search
└── Data-driven attribution available

RECONCILIATION:
├── Accept 20-40% overlap
├── Use holistic measurement (MMM)
├── Post-purchase surveys for truth
└── Don't optimize for one at expense of other
```

### Multi-Touch Attribution Considerations

```
META'S APPROACH:
├── Single-touch (last-touch within window)
├── Full credit to last Meta touchpoint
├── No native multi-touch

FOR MULTI-TOUCH:
├── Use third-party tools (Triple Whale, Northbeam)
├── Implement Marketing Mix Modeling
├── Post-purchase surveys
└── Platform-agnostic measurement
```

## Attribution Configuration Guide

### Setup Checklist

```
BEFORE CONFIGURING:

□ Define conversion events
  └── What actions matter most?

□ Understand buying cycle
  └── How long from awareness to purchase?

□ Set measurement goals
  └── Volume vs. incrementality?

□ Establish baselines
  └── Current performance benchmarks

CONFIGURATION:

□ Campaign level settings
  └── Ads Manager → Campaign → Settings → Attribution

□ Consistent across campaigns
  └── Use same windows for comparison

□ Document choices
  └── Why this configuration?
```

### Attribution Settings by Campaign Type

| Campaign Type | Recommended Window | View-Through | Notes |
|--------------|-------------------|--------------|-------|
| **Prospecting** | 7-day click | 1-day | Capture delayed conversions |
| **Retargeting** | 7-day click | 1-day or None | Consider incrementality |
| **Brand Awareness** | 7-day click | 1-day | Measure full impact |
| **Dynamic Ads (DPA)** | 7-day click | 1-day | Standard e-commerce |
| **Lead Gen** | 7-day click | 1-day | Research-heavy decision |
| **App Install** | 7-day click | 1-day | Standard mobile |

## Attribution Analysis

### Comparing Attribution Windows

```
HOW TO ANALYZE IMPACT:

1. Run comparison:
   ├── Export data met 1-day click
   ├── Export data met 7-day click
   └── Compare conversion difference

2. Calculate "extended window lift":
   ├── (7-day conversions - 1-day conversions) / 1-day conversions
   └── Shows delayed conversion rate

3. Interpret:
   ├── >50% lift: Long consideration, use 7-day
   ├── 20-50% lift: Normal, 7-day appropriate
   └── <20% lift: Quick decisions, 1-day sufficient
```

### View-Through Impact Analysis

```
MEASURING VT CONTRIBUTION:

1. Compare periods:
   ├── Period A: VT enabled
   ├── Period B: VT disabled
   └── Measure conversion difference

2. Calculate VT percentage:
   ├── (VT conversions) / (Total conversions)
   └── Shows VT contribution to reported results

3. Evaluate:
   ├── >30% VT: Significant brand influence
   ├── 10-30% VT: Normal awareness contribution
   └── <10% VT: Minimal impact, consider disabling
```

## Troubleshooting Attribution

### Common Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| Conversion delay | Sales missing, appear later | Normal for iOS, wait 72hr |
| Over-attribution | More conversions than orders | Check deduplication, VT impact |
| Under-attribution | Fewer conversions than expected | Check pixel/CAPI, attribution window |
| Inconsistent data | Different numbers in reports | Verify date ranges, attribution settings |
| GA4 mismatch | Meta shows more conversions | Different models, VT inclusion |

### Attribution Audit Template

```markdown
# Attribution Audit

## Current Configuration
- Click window: [1-day / 7-day]
- View window: [None / 1-day]
- Incremental: [Yes / No]

## Conversion Analysis
- Reported conversions: [X]
- Platform transactions: [Y]
- Difference: [Z]%

## Attribution Window Analysis
| Window | Conversions | % of Total |
|--------|-------------|------------|
| 1-day click | [X] | [X]% |
| 2-7 day click | [Y] | [Y]% |
| 1-day view | [Z] | [Z]% |

## Recommendations
1. [Recommendation based on analysis]
2. [Additional recommendation]

## Action Items
□ [Action 1]
□ [Action 2]
```

## Best Practices

```
DO:
├── Keep attribution consistent across campaigns
├── Document your attribution choices
├── Compare trends, not absolute numbers
├── Use multiple measurement sources
├── Accept some measurement uncertainty

DON'T:
├── Change attribution mid-campaign
├── Compare campaigns with different windows
├── Obsess over exact conversion counts
├── Ignore iOS measurement limitations
├── Add Meta + Google conversions together
```

## Fatigue Detection Decision Tree

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IS MY GOOGLE ADS CREATIVE FATIGUED?                       │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                         What campaign type?
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
   PERFORMANCE MAX              DISPLAY                      YOUTUBE
        │                           │                           │
        ▼                           ▼                           ▼
  Check Asset Ratings         Check Asset Ratings          Check VTR Trend
        │                           │                           │
        ▼                           ▼                           ▼
┌───────┴───────┐          ┌───────┴───────┐          ┌───────┴───────┐
│ Multiple      │          │ Multiple      │          │ VTR <20% OR   │
│ "Low" >30d?   │          │ "Low" >30d?   │          │ declining >15%│
└───────┬───────┘          └───────┬───────┘          └───────┬───────┘
        │                           │                           │
   YES  │  NO                  YES  │  NO                  YES  │  NO
        │   │                       │   │                       │   │
        ▼   ▼                       ▼   ▼                       ▼   ▼
     Check              Check      Check              Check  Check CPV
     CTR/ROAS           CTR/Conv   CTR/ROAS           CTR/   + Watch
     Trends             Trends     Trends             Conv   Time
        │                   │           │               │       │
        ▼                   │           ▼               │       ▼
  Declining               │      Declining            │    CPV +30%?
  >15% 2wks?              │      >10%/month?          │    Watch time
        │                 │           │               │    declining?
        ▼                 ▼           ▼               ▼       │
┌───────┴───────┐        NOT    ┌───────┴───────┐  NOT      │
│ FATIGUE       │     FATIGUED  │ FATIGUE       │ FATIGUED  │
│ LIKELY        │               │ LIKELY        │           ▼
│               │               │               │    ┌──────┴──────┐
│ Replace Low   │               │ Replace Low   │    │ FATIGUE     │
│ assets, add   │               │ assets, test  │    │ CONFIRMED   │
│ new variations│               │ new creatives │    │             │
└───────────────┘               └───────────────┘    │ New video   │
                                                      │ needed      │
                                                      └─────────────┘
```

## Refresh vs Replace Decision Framework

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GOOGLE ADS: REFRESH vs REPLACE                            │
└─────────────────────────────────────────────────────────────────────────────┘

SCENARIO 1: MINOR FATIGUE (Performance dipped but recoverable)
──────────────────────────────────────────────────────────────
Indicators:
├── 1-2 assets at "Low" for 30+ days
├── CTR declined 5-10%
├── ROAS/CPA still within acceptable range
└── Other assets performing well

Action: INCREMENTAL REFRESH
├── Replace "Low" rated assets only
├── Add 2-3 new variations of "Best" performers
├── Keep campaign structure intact
└── Timeline: Implement within 1 week

SCENARIO 2: MODERATE FATIGUE (Clear performance decline)
────────────────────────────────────────────────────────
Indicators:
├── 30-50% of assets at "Low" rating
├── CTR declined 10-15%
├── ROAS declining but above break-even
└── Best performers starting to decline

Action: SIGNIFICANT REFRESH
├── Replace all "Low" assets
├── Refresh 50% of "Good" assets with new angles
├── Keep "Best" performers, add variations
├── Consider new headline/description angles
└── Timeline: Implement over 1-2 weeks

SCENARIO 3: SEVERE FATIGUE (Performance tanking)
────────────────────────────────────────────────
Indicators:
├── >50% assets at "Low" or declining
├── CTR declined >15%
├── ROAS below target for 2+ weeks
├── Even "Best" rated assets declining
└── Google may flag "Limited" status

Action: COMPREHENSIVE REFRESH
├── Replace all assets (images, headlines, descriptions)
├── Test entirely new creative concepts
├── Consider new audience signals (PMax)
├── Review landing pages
├── May need new campaign structure
└── Timeline: Immediate action, 2-3 week implementation
```
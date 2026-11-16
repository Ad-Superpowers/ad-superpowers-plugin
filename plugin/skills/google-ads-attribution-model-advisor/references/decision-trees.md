## Quick Decision Guide

Google Ads offers two attribution models: Data-driven (DDA, the default for new
conversion actions) and Last click. First click, linear, time decay and
position-based were removed in 2023, and there is no minimum conversion volume
for DDA.

```
WHICH ATTRIBUTION MODEL FITS YOUR CASE?
│
├─► DEFAULT → DATA-DRIVEN ATTRIBUTION (DDA)
│   ├── Credit per touchpoint from your account's conversion paths
│   ├── Gives upper-funnel and generic campaigns credit that Last click misses
│   └── Check data_driven_model_status per conversion action
│
├─► LAST CLICK, when:
│   ├── Stakeholders need a simple, explainable number
│   ├── An action has too few conversions for a stable DDA split
│   │   (or keep DDA and widen the conversion definition)
│   └── You compare against a system that also reports last click
│
└─► AWARENESS MEASUREMENT
    └── Neither model measures awareness well; use assisted conversions,
        conversion paths and lift or incrementality tests instead
```

## Attribution Model Selection

### Decision Framework

```
ATTRIBUTION MODEL SELECTION FRAMEWORK
══════════════════════════════════════

STEP 1: CHECK THE CURRENT SETTING
─────────────────────────────────
Per conversion action (GAQL on conversion_action):
├── attribution_model_settings.attribution_model
├── attribution_model_settings.data_driven_model_status
└── Old rules-based values on historical rows cannot be selected again

STEP 2: ANALYZE BUSINESS MODEL
───────────────────────────────
┌─────────────────────────┬──────────────────────────────────┐
│ Business Type           │ Recommended Model                │
├─────────────────────────┼──────────────────────────────────┤
│ Impulse e-commerce      │ DDA (Last click differs little   │
│ (<7 days decision)      │ on short paths)                  │
├─────────────────────────┼──────────────────────────────────┤
│ Considered e-commerce   │ DDA                              │
│ (7-30 days decision)    │                                  │
├─────────────────────────┼──────────────────────────────────┤
│ B2B Lead Gen            │ DDA on the primary lead action;  │
│ (long sales cycle)      │ Last click if volume is very low │
├─────────────────────────┼──────────────────────────────────┤
│ Brand-focused           │ DDA, plus assisted conversions   │
│ (awareness priority)    │ and lift tests for awareness     │
├─────────────────────────┼──────────────────────────────────┤
│ Multi-channel mature    │ DDA                              │
│ (many active channels)  │                                  │
└─────────────────────────┴──────────────────────────────────┘

STEP 3: EVALUATE CURRENT PERFORMANCE GAPS
──────────────────────────────────────────
Questions to answer:
□ Are awareness campaigns undervalued?
□ Is brand search getting too much credit?
□ Is there a disconnect between ad spend and revenue?
□ Are certain channels "invisible"?

If YES to multiple while on Last click: consider switching to DDA.
```

### Model Transition Strategy

```
SWITCHING TO A NEW ATTRIBUTION MODEL
═════════════════════════════════════

STEP 1: BASELINE DOCUMENTATION (Week -1)
─────────────────────────────────────────
□ Export current performance per campaign
□ Note conversion volumes per channel
□ Screenshot attribution reports
□ Document current ROAS/CPA targets

STEP 2: MODEL COMPARISON (Week 0)
──────────────────────────────────
□ Tools → Attribution → Model Comparison
□ Compare current model vs new model
□ Identify campaigns with large shifts
□ Calculate new targets:
  └── New target = Old target × (New/Old ratio)

STEP 3: STAKEHOLDER COMMUNICATION
──────────────────────────────────
□ Explain why the change is needed
□ Show expected impact per campaign
□ Manage expectations (numbers will look different)
□ Set review date (4 weeks)

STEP 4: IMPLEMENTATION (Week 1)
───────────────────────────────
□ Change attribution model in conversion settings
□ Update bidding targets (if needed)
□ Monitor first 7 days intensively
□ NO major budget changes

STEP 5: EVALUATION (Week 4)
───────────────────────────
□ Compare pre vs post switch
□ Analyze Smart Bidding performance
□ Check for anomalies
□ Fine-tune targets if needed

⚠️ IMPORTANT WARNINGS:
├── Attribution change = no "real" performance change
├── Smart Bidding adjusts automatically
├── Reporting will look different, not better/worse
└── Give it at least 4 weeks
```

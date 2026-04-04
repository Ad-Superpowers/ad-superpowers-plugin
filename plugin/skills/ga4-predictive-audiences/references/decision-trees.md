## Quick Decision Tree

```
GA4 PREDICTIVE AUDIENCES FLOW
│
├─► WHICH PREDICTIVE METRIC?
│   ├─► Purchase probability
│   │   └─► "Likely 7-day purchasers"
│   │   └─► Use: acquisition, conversion campaigns
│   │
│   ├─► Churn probability
│   │   └─► "Likely 7-day churners"
│   │   └─► Use: retention, win-back campaigns
│   │
│   └─► Predicted revenue
│       └─► "High predicted revenue (28d)"
│       └─► Use: VIP targeting, value-based bidding
│
├─► ELIGIBLE FOR PREDICTIVE?
│   ├─► Yes (sufficient data)
│   │   └─► Proceed with setup
│   │
│   └─► No (insufficient data)
│       └─► Improve tracking first
│       └─► See "Eligibility Requirements"
│
└─► HOW TO ACTIVATE?
    ├─► Directly in GA4 audience builder
    │   └─► Use predictive metrics as conditions
    │
    └─► Export to Google Ads
        └─► For Smart Bidding optimization
        └─► See: ga4-remarketing-setup skill
```

## Troubleshooting

```
TROUBLESHOOTING GUIDE
=====================

PROBLEM: Predictive audiences not eligible
───────────────────────────────────────────
Causes:
├── Insufficient purchase events (<1000/week)
├── Purchase event missing value parameter
├── Inconsistent data (gaps in tracking)
├── New property (<28 days of data)
└── Model quality too low

Solution:
├── Check purchase event setup:
│   Admin → Events → purchase → Parameters
│   Must include: value, currency, transaction_id
│
├── Verify volume:
│   Explore → Users with purchase event → 28 days
│   Minimum 1,000 purchasers needed
│
├── Fix tracking gaps:
│   Check for missing days in real-time report
│   Implement consent mode correctly
│
└── Wait for sufficient data:
    28 days of consistent volume needed

PROBLEM: Predictive audience size = 0
──────────────────────────────────────
Causes:
├── Threshold too high (>95% probability)
├── Just became eligible, no users scored yet
├── Combination with other conditions filters everyone out
└── Audience just created (24h processing)

Solution:
├── Lower probability threshold (test with >50%)
├── Wait 24-48 hours after eligibility
├── Test predictive condition independently first
└── Check if standard predictive audiences have users

PROBLEM: Predictive audiences not available in Google Ads
────────────────────────────────────────────────────────
Causes:
├── Google Ads link not active
├── Personalized advertising not enabled
├── Sync delay (up to 48 hours)
├── Audience too small (<1000 users)
└── Policy violation

Solution:
├── Verify link: Admin → Product Links → Google Ads
├── Check toggle: Personalized advertising = ON
├── Wait 48 hours after audience creation
├── Check audience size in GA4
└── Review Google Ads policy compliance

PROBLEM: Predictive performance lower than expected
───────────────────────────────────────────────────
Causes:
├── Model not trained on your specific business
├── Seasonal shifts affect prediction accuracy
├── Targeting too broad or too narrow
├── Creative mismatch with audience intent
└── Attribution window mismatch

Solution:
├── Compare predictive vs. actual conversions
├── Test different probability thresholds
├── A/B test predictive targeting
├── Adjust bidding based on observed performance
└── Combine with retargeting signals

PROBLEM: Model quality degrades over time
────────────────────────────────────────
Causes:
├── Business changes (new products/pricing)
├── Seasonal patterns not in model
├── Tracking changes (consent mode updates)
├── User behavior shifts
└── Competition changes

Solution:
├── Model adapts automatically (ongoing)
├── Monitor prediction accuracy monthly
├── Compare predicted vs actual conversions
├── Report major shifts to Google Support
└── Consider custom ML if available
```
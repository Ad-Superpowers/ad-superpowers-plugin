## Quick Decision Tree

```
WHEN TO USE A DATA LAYER?
│
├─► ALWAYS RECOMMENDED FOR:
│   ├── E-commerce tracking (product data, cart, purchase)
│   ├── User properties (membership, customer type)
│   ├── Dynamic content data (A/B tests, personalization)
│   ├── Form data (form name, values)
│   └── Server-side data (CRM data, backend events)
│       └─► IMPLEMENT DATA LAYER ✅
│
├─► OPTIONAL FOR:
│   ├── Simple click tracking
│   ├── Scroll tracking
│   └── Basic page views
│       └─► GTM built-in variables are often sufficient
│
└─► HOW TO IMPLEMENT?
    ├── CMS/Platform has native support
    │   └─► Use platform plugin/module
    │
    ├── Custom website
    │   └─► Developer implements in code
    │
    └── No developer access
        └─► Custom HTML tags in GTM (limited)
```

## Common Data Layer Issues

```
TROUBLESHOOTING DATA LAYER
============================

PROBLEM: GTM does not see Data Layer variable
──────────────────────────────────────────────
Causes:
├── Push happens AFTER tag firing
├── Incorrect variable name (typo)
├── Data Layer Version mismatch
└── Scope issue (variable not global)

Solution:
├── Verify timing: data must exist before trigger
├── Check exact spelling in GTM variable
├── Use Data Layer Version 2
├── Ensure window.dataLayer is global

PROBLEM: E-commerce data not appearing in GA4
──────────────────────────────────────────────
Causes:
├── ecommerce object not cleared
├── Items is not an array
├── Wrong property names (item_id vs productId)
└── Currency missing

Solution:
├── ALWAYS: dataLayer.push({ ecommerce: null }); before push
├── Items must be an array: items: [{}]
├── Use GA4 naming convention
└── Include currency with value

PROBLEM: Duplicate Data Layer pushes
─────────────────────────────────────
Causes:
├── Code runs multiple times (SPA)
├── Event listeners not removed
├── Form submit + page load both pushing
└── GTM Preview mode (can cause duplicates)

Solution:
├── Debounce event handlers
├── Check for existing push (flag pattern)
├── Use event.preventDefault() correctly
└── Test in incognito without Preview

PROBLEM: Values are wrong type
───────────────────────────────
Causes:
├── String where number expected: "100" vs 100
├── Object where string expected
└── Array formatting issues

Solution:
```javascript
// BAD
dataLayer.push({
  'value': '100.00'  // String
});

// CORRECT
dataLayer.push({
  'value': 100.00    // Number
});

// Parse if needed
dataLayer.push({
  'value': parseFloat(priceString)
});
```
```
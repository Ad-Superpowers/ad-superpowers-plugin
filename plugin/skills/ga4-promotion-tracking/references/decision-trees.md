## Quick Decision Tree

```
GA4 PROMOTION TRACKING FLOW
|
+---> WHAT DO YOU WANT TO TRACK?
|   +---> Internal promotion banners/slots
|   |   +---> view_promotion + select_promotion events
|   |
|   +---> Coupon codes/discounts
|   |   +---> coupon parameter in e-commerce events
|   |
|   +---> Sale/campaign periods
|   |   +---> Custom dimensions + segments
|   |
|   +---> All of the above
|       +---> Complete promotion tracking setup
|
+---> WHERE ARE PROMOTIONS SHOWN?
|   +---> Homepage banners
|   |   +---> Track impression + click
|   |
|   +---> Category page slots
|   |   +---> Track with list context
|   |
|   +---> Product page upsells
|   |   +---> Track as promotion or item_list
|   |
|   +---> Cart/checkout suggestions
|       +---> Track with checkout context
|
+---> ANALYSIS GOAL?
    +---> Which promotions convert
    |   +---> Promotion funnel analysis
    |
    +---> Coupon code effectiveness
    |   +---> Coupon revenue report
    |
    +---> Promotion ROI
        +---> Attribution analysis
```

## Common Problems

```
TROUBLESHOOTING PROMOTION TRACKING
====================================

PROBLEM: Too many view_promotion events
----------------------------------------
Causes:
+-- Event fired on every scroll
+-- No deduplication logic
+-- SPA route changes re-trigger
+-- Carousel auto-rotation

Solution:
+-- Track only first view per session
+-- Use IntersectionObserver correctly
+-- Implement session-based deduplication
+-- Carousel: track only user-initiated views

IMPLEMENTATION:
---------------
const trackedPromos = new Set();

function trackPromoView(promoId, promoData) {
  if (!trackedPromos.has(promoId)) {
    trackedPromos.add(promoId);
    dataLayer.push({ ecommerce: null });
    dataLayer.push({
      event: "view_promotion",
      ecommerce: { items: [promoData] }
    });
  }
}


PROBLEM: Coupon data not in reports
------------------------------------
Causes:
+-- coupon parameter missing in purchase
+-- Custom dimension not registered
+-- Wrong parameter name
+-- Data processing delay

Solution:
+-- Verify coupon in dataLayer
+-- Check custom dimension setup
+-- Exact parameter name: "coupon"
+-- Wait 24-48 hours


PROBLEM: Promotion CTR unrealistic
------------------------------------
Causes:
+-- Views and clicks tracking mismatch
+-- Bot traffic
+-- Click tracking on wrong element
+-- Views overcounted

Solution:
+-- Verify both events track the same promo
+-- Exclude known bots
+-- Check click event target
+-- Implement proper view deduplication


PROBLEM: Attribution to promotion unclear
------------------------------------------
Causes:
+-- Promotion not carried through to purchase
+-- Session breaks
+-- Multi-touch journey
+-- No funnel tracking

Solution:
+-- Track promotion context through funnel
+-- Use promotion_id consistently
+-- Build custom funnel exploration
+-- Consider user-scoped tracking
```
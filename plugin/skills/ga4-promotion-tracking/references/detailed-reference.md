## Promotion Events Overview

```
GA4 PROMOTION EVENTS
====================

EVENT TYPES:
+---------------------+----------------------------------------------+
| Event               | When to trigger                              |
+---------------------+----------------------------------------------+
| view_promotion      | Promotion banner/slot enters viewport         |
|                     | (visible to user)                            |
+---------------------+----------------------------------------------+
| select_promotion    | User clicks on promotion                     |
|                     | (banner, link, CTA)                          |
+---------------------+----------------------------------------------+

REQUIRED PARAMETERS:
+---------------------+----------------------------------------------+
| Parameter           | Description                                  |
+---------------------+----------------------------------------------+
| promotion_id        | Unique promotion identifier                  |
|                     | Example: "summer_sale_2024"                  |
+---------------------+----------------------------------------------+
| promotion_name      | Human-readable promotion name                |
|                     | Example: "Summer Sale 2024"                  |
+---------------------+----------------------------------------------+

RECOMMENDED PARAMETERS:
+---------------------+----------------------------------------------+
| Parameter           | Description                                  |
+---------------------+----------------------------------------------+
| creative_name       | Name of the creative asset                   |
|                     | Example: "hero_banner_red"                   |
+---------------------+----------------------------------------------+
| creative_slot       | Slot/position where promotion is shown       |
|                     | Example: "homepage_hero", "sidebar_top"      |
+---------------------+----------------------------------------------+
| location_id         | Physical or logical location                 |
|                     | Example: "homepage", "category_shoes"        |
+---------------------+----------------------------------------------+
```

## Coupon/Discount Code Tracking

```
COUPON PARAMETER TRACKING
=========================

WHERE TO ADD:
+-- add_to_cart (if coupon already known)
+-- begin_checkout
+-- purchase (REQUIRED for coupon analysis)
+-- All e-commerce events with coupon context

TWO LEVELS:
-----------
1. ORDER-LEVEL COUPON
   +-- Discount on entire order
   +-- Parameter in root of ecommerce object

2. ITEM-LEVEL COUPON
   +-- Discount on specific product
   +-- Parameter in items array

DATALAYER EXAMPLE:
-----------------------------------------------------------------
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "purchase",
  ecommerce: {
    transaction_id: "ORD-2024-12345",
    value: 89.97,
    tax: 15.63,
    shipping: 4.99,
    currency: "EUR",
    coupon: "SUMMER20",                    // ORDER-LEVEL COUPON
    items: [
      {
        item_id: "SKU12345",
        item_name: "Summer T-shirt",
        price: 24.99,
        quantity: 2,
        coupon: "TSHIRT10",               // ITEM-LEVEL COUPON
        discount: 5.00                     // Discount amount per item
      },
      {
        item_id: "SKU67890",
        item_name: "Shorts",
        price: 39.99,
        quantity: 1
        // No item-level coupon
      }
    ]
  }
});
-----------------------------------------------------------------

DISCOUNT PARAMETER:
-------------------
+---------------------+----------------------------------------------+
| Parameter           | Usage                                        |
+---------------------+----------------------------------------------+
| coupon              | Coupon CODE (string)                         |
|                     | Example: "SUMMER20"                          |
+---------------------+----------------------------------------------+
| discount            | Discount AMOUNT (number)                     |
|                     | Example: 5.00                                |
+---------------------+----------------------------------------------+

WARNING - IMPORTANT:
+-- coupon is the CODE (for grouping/analysis)
+-- discount is the AMOUNT (for revenue impact)
+-- Both can be used together
+-- value must be the NET amount (after discount)
```

## GTM Configuration for Promotions

```
GTM PROMOTION TRACKING SETUP
=============================

STEP 1: DATALAYER VARIABLES
----------------------------
Create variables for promotion parameters:

+----------------------------+-------------------------------+
| Variable name              | Data Layer Variable Name      |
+----------------------------+-------------------------------+
| DLV - promotion_id         | ecommerce.items.0.promotion_id|
+----------------------------+-------------------------------+
| DLV - promotion_name       | ecommerce.items.0.promotion_name|
+----------------------------+-------------------------------+
| DLV - creative_name        | ecommerce.items.0.creative_name|
+----------------------------+-------------------------------+
| DLV - creative_slot        | ecommerce.items.0.creative_slot|
+----------------------------+-------------------------------+
| DLV - coupon               | ecommerce.coupon              |
+----------------------------+-------------------------------+

STEP 2: TRIGGERS
----------------
Trigger Type: Custom Event

+-- view_promotion trigger  -> Event name: view_promotion
+-- select_promotion trigger -> Event name: select_promotion

STEP 3: GA4 EVENT TAGS
----------------------
Tag Type: Google Analytics: GA4 Event

OPTION A - With "Send Ecommerce data":
+-- Event Name: {{Event}}
+-- Check "Send Ecommerce data"
+-- Data source: Data Layer
+-- Trigger: [promotion triggers]

OPTION B - With custom parameters:
+-- Event Name: {{Event}}
+-- Event Parameters:
|   +-- promotion_id: {{DLV - promotion_id}}
|   +-- promotion_name: {{DLV - promotion_name}}
|   +-- creative_name: {{DLV - creative_name}}
|   +-- creative_slot: {{DLV - creative_slot}}
+-- Trigger: [promotion triggers]
```

## Promotion Naming Conventions

```
PROMOTION NAMING BEST PRACTICES
================================

PROMOTION_ID FORMAT:
--------------------
[type]_[campaign]_[year]_[variant]

Examples:
+-- sale_summer_2024_v1
+-- promo_blackfriday_2024_hero
+-- banner_newcollection_2024_sidebar
+-- popup_newsletter_2024_exit

CREATIVE_NAME FORMAT:
---------------------
[format]_[theme]_[variant]

Examples:
+-- hero_beach_lifestyle
+-- banner_discount_red
+-- tile_product_minimal
+-- popup_urgency_countdown

CREATIVE_SLOT FORMAT:
---------------------
[page]_[position]

Examples:
+-- homepage_hero
+-- homepage_midpage_left
+-- category_sidebar_top
+-- product_related_bottom
+-- cart_upsell_modal
+-- checkout_crosssell

CONSISTENCY TIPS:
-----------------
+------------------------+-------------------------------------------+
| DO                     | DON'T                                     |
+------------------------+-------------------------------------------+
| Lowercase only         | Mixcase (SummerSale)                      |
+------------------------+-------------------------------------------+
| Underscores (_)        | Spaces or hyphens                         |
+------------------------+-------------------------------------------+
| Dateable names         | Generic names (promo1, banner2)           |
+------------------------+-------------------------------------------+
| Descriptive names      | Abbreviations (bf24 instead of            |
|                        | blackfriday_2024)                         |
+------------------------+-------------------------------------------+
| Document conventions   | Ad-hoc naming                             |
+------------------------+-------------------------------------------+
```
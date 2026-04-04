## Promotion Performance Analysis

```
GA4 PROMOTION REPORTS
=====================

LOCATION: Reports -> Monetization -> Promotions

AVAILABLE METRICS:
+-------------------------+------------------------------------------+
| Metric                  | Meaning                                  |
+-------------------------+------------------------------------------+
| Item promotion views    | Number of view_promotion events          |
+-------------------------+------------------------------------------+
| Item promotion clicks   | Number of select_promotion events        |
+-------------------------+------------------------------------------+
| Item promotion CTR      | Clicks / Views x 100%                    |
+-------------------------+------------------------------------------+

PROMOTION FUNNEL EXPLORATION:
-----------------------------
SETUP:
+-- Technique: Funnel exploration
+-- Steps:
|   +-- Step 1: view_promotion (with promotion_id filter)
|   +-- Step 2: select_promotion
|   +-- Step 3: view_item
|   +-- Step 4: add_to_cart
|   +-- Step 5: purchase
+-- Breakdown: promotion_name or creative_slot

COUPON ANALYSIS EXPLORATION:
-----------------------------
SETUP:
+-- Technique: Free form
+-- Rows: Order coupon (custom dimension)
+-- Values:
|   +-- Transactions
|   +-- Total revenue
|   +-- Average purchase value
|   +-- Items purchased
+-- Filter: coupon is not (not set)

NOTE: "Order coupon" must be registered as a
   custom dimension in GA4 Admin
```
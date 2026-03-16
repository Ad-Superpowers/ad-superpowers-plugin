---
name: ga4-promotion-tracking
description: "Promotie en kortingscode tracking in GA4. Gebruik voor: (1) Interne promoties tracken (banners, slots), (2) Kortingscodes meten en analyseren, (3) Promotion performance reports, (4) A/B test promotie effectiviteit, (5) Coupon ROI berekenen. Triggers: promotie tracking, kortingscode analyse, coupon tracking, banner tracking, promotion performance, sale tracking, discount analyse."
---

# GA4 Promotion Tracking Guide

Complete gids voor het tracken van interne promoties, kortingscodes en sales campagnes in Google Analytics 4.

## Quick Decision Tree

```
GA4 PROMOTIE TRACKING FLOW
│
├─► WAT WIL JE TRACKEN?
│   ├─► Interne promotie banners/slots
│   │   └─► view_promotion + select_promotion events
│   │
│   ├─► Kortingscodes/coupons
│   │   └─► coupon parameter in e-commerce events
│   │
│   ├─► Sale/campagne periodes
│   │   └─► Custom dimensions + segments
│   │
│   └─► Alle bovenstaande
│       └─► Complete promotie tracking setup
│
├─► WAAR WORDEN PROMOTIES GETOOND?
│   ├─► Homepage banners
│   │   └─► Track impression + click
│   │
│   ├─► Categoriepagina slots
│   │   └─► Track met list context
│   │
│   ├─► Product pagina upsells
│   │   └─► Track als promotion of item_list
│   │
│   └─► Cart/checkout suggesties
│       └─► Track met checkout context
│
└─► ANALYSE DOEL?
    ├─► Welke promoties converteren
    │   └─► Promotion funnel analyse
    │
    ├─► Coupon code effectiviteit
    │   └─► Coupon revenue report
    │
    └─► Promotie ROI
        └─► Attribution analyse
```

## Promotion Events Overzicht

```
GA4 PROMOTION EVENTS
====================

EVENT TYPES:
┌─────────────────────┬──────────────────────────────────────────────┐
│ Event               │ Wanneer triggeren                            │
├─────────────────────┼──────────────────────────────────────────────┤
│ view_promotion      │ Promotie banner/slot komt in viewport        │
│                     │ (zichtbaar voor gebruiker)                   │
├─────────────────────┼──────────────────────────────────────────────┤
│ select_promotion    │ Gebruiker klikt op promotie                  │
│                     │ (banner, link, CTA)                          │
└─────────────────────┴──────────────────────────────────────────────┘

VERPLICHTE PARAMETERS:
┌─────────────────────┬──────────────────────────────────────────────┐
│ Parameter           │ Beschrijving                                 │
├─────────────────────┼──────────────────────────────────────────────┤
│ promotion_id        │ Unieke promotie identifier                   │
│                     │ Voorbeeld: "summer_sale_2024"                │
├─────────────────────┼──────────────────────────────────────────────┤
│ promotion_name      │ Leesbare promotie naam                       │
│                     │ Voorbeeld: "Zomer Sale 2024"                 │
└─────────────────────┴──────────────────────────────────────────────┘

AANBEVOLEN PARAMETERS:
┌─────────────────────┬──────────────────────────────────────────────┐
│ Parameter           │ Beschrijving                                 │
├─────────────────────┼──────────────────────────────────────────────┤
│ creative_name       │ Naam van de creatieve uiting                 │
│                     │ Voorbeeld: "hero_banner_red"                 │
├─────────────────────┼──────────────────────────────────────────────┤
│ creative_slot       │ Slot/positie waar promotie getoond wordt     │
│                     │ Voorbeeld: "homepage_hero", "sidebar_top"    │
├─────────────────────┼──────────────────────────────────────────────┤
│ location_id         │ Fysieke of logische locatie                  │
│                     │ Voorbeeld: "homepage", "category_shoes"      │
└─────────────────────┴──────────────────────────────────────────────┘
```

## DataLayer Implementatie

### view_promotion Event

```javascript
VIEW_PROMOTION EVENT
====================

WANNEER: Promotie banner/element komt in viewport

DATALAYER CODE:
─────────────────────────────────────────────────────────────────
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "view_promotion",
  ecommerce: {
    items: [{
      promotion_id: "summer_sale_2024",     // VERPLICHT
      promotion_name: "Zomer Sale 2024",    // VERPLICHT
      creative_name: "hero_banner_beach",   // Aanbevolen
      creative_slot: "homepage_hero",       // Aanbevolen
      location_id: "homepage"               // Optioneel
    }]
  }
});
─────────────────────────────────────────────────────────────────

VIEWPORT TRACKING IMPLEMENTATIE:
────────────────────────────────
// Met Intersection Observer (aanbevolen)
const promotionBanner = document.querySelector('.promo-banner');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      dataLayer.push({ ecommerce: null });
      dataLayer.push({
        event: "view_promotion",
        ecommerce: {
          items: [{
            promotion_id: promotionBanner.dataset.promoId,
            promotion_name: promotionBanner.dataset.promoName,
            creative_name: promotionBanner.dataset.creative,
            creative_slot: promotionBanner.dataset.slot
          }]
        }
      });
      observer.unobserve(entry.target); // Track slechts 1x
    }
  });
}, { threshold: 0.5 }); // 50% zichtbaar

observer.observe(promotionBanner);

HTML DATA ATTRIBUTES:
─────────────────────
<div class="promo-banner"
     data-promo-id="summer_sale_2024"
     data-promo-name="Zomer Sale 2024"
     data-creative="hero_banner_beach"
     data-slot="homepage_hero">
  <!-- Banner content -->
</div>
```

### select_promotion Event

```javascript
SELECT_PROMOTION EVENT
======================

WANNEER: Gebruiker klikt op promotie element

DATALAYER CODE:
─────────────────────────────────────────────────────────────────
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "select_promotion",
  ecommerce: {
    items: [{
      promotion_id: "summer_sale_2024",
      promotion_name: "Zomer Sale 2024",
      creative_name: "hero_banner_beach",
      creative_slot: "homepage_hero",
      location_id: "homepage"
    }]
  }
});
─────────────────────────────────────────────────────────────────

CLICK HANDLER IMPLEMENTATIE:
────────────────────────────
document.querySelectorAll('.promo-banner').forEach(banner => {
  banner.addEventListener('click', function() {
    dataLayer.push({ ecommerce: null });
    dataLayer.push({
      event: "select_promotion",
      ecommerce: {
        items: [{
          promotion_id: this.dataset.promoId,
          promotion_name: this.dataset.promoName,
          creative_name: this.dataset.creative,
          creative_slot: this.dataset.slot
        }]
      }
    });
  });
});
```

## Coupon/Kortingscode Tracking

```
COUPON PARAMETER TRACKING
=========================

WAAR TOEVOEGEN:
├── add_to_cart (als coupon al bekend)
├── begin_checkout
├── purchase (VERPLICHT voor coupon analyse)
└── Alle e-commerce events met coupon context

TWEE NIVEAUS:
─────────────
1. ORDER-LEVEL COUPON
   └── Korting op gehele bestelling
   └── Parameter in root van ecommerce object

2. ITEM-LEVEL COUPON
   └── Korting op specifiek product
   └── Parameter in items array

DATALAYER VOORBEELD:
─────────────────────────────────────────────────────────────────
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "purchase",
  ecommerce: {
    transaction_id: "ORD-2024-12345",
    value: 89.97,
    tax: 15.63,
    shipping: 4.99,
    currency: "EUR",
    coupon: "ZOMER20",                    // ORDER-LEVEL COUPON
    items: [
      {
        item_id: "SKU12345",
        item_name: "Zomer T-shirt",
        price: 24.99,
        quantity: 2,
        coupon: "TSHIRT10",               // ITEM-LEVEL COUPON
        discount: 5.00                     // Kortingsbedrag per item
      },
      {
        item_id: "SKU67890",
        item_name: "Korte Broek",
        price: 39.99,
        quantity: 1
        // Geen item-level coupon
      }
    ]
  }
});
─────────────────────────────────────────────────────────────────

DISCOUNT PARAMETER:
───────────────────
┌─────────────────────┬──────────────────────────────────────────────┐
│ Parameter           │ Gebruik                                      │
├─────────────────────┼──────────────────────────────────────────────┤
│ coupon              │ Coupon CODE (string)                         │
│                     │ Voorbeeld: "ZOMER20"                         │
├─────────────────────┼──────────────────────────────────────────────┤
│ discount            │ Kortings BEDRAG (number)                     │
│                     │ Voorbeeld: 5.00                              │
└─────────────────────┴──────────────────────────────────────────────┘

⚠️ BELANGRIJK:
├── coupon is de CODE (voor grouping/analysis)
├── discount is het BEDRAG (voor revenue impact)
├── Beide kunnen samen gebruikt worden
└── value moet NETTO bedrag zijn (na korting)
```

## GTM Configuratie voor Promoties

```
GTM PROMOTION TRACKING SETUP
============================

STAP 1: DATALAYER VARIABELEN
────────────────────────────
Maak variabelen voor promotion parameters:

┌────────────────────────────┬───────────────────────────────┐
│ Variabele naam             │ Data Layer Variable Name      │
├────────────────────────────┼───────────────────────────────┤
│ DLV - promotion_id         │ ecommerce.items.0.promotion_id│
├────────────────────────────┼───────────────────────────────┤
│ DLV - promotion_name       │ ecommerce.items.0.promotion_name│
├────────────────────────────┼───────────────────────────────┤
│ DLV - creative_name        │ ecommerce.items.0.creative_name│
├────────────────────────────┼───────────────────────────────┤
│ DLV - creative_slot        │ ecommerce.items.0.creative_slot│
├────────────────────────────┼───────────────────────────────┤
│ DLV - coupon               │ ecommerce.coupon              │
└────────────────────────────┴───────────────────────────────┘

STAP 2: TRIGGERS
────────────────
Trigger Type: Custom Event

├── view_promotion trigger  → Event name: view_promotion
└── select_promotion trigger → Event name: select_promotion

STAP 3: GA4 EVENT TAGS
──────────────────────
Tag Type: Google Analytics: GA4 Event

OPTIE A - Met "Send Ecommerce data":
├── Event Name: {{Event}}
├── Check "Send Ecommerce data"
├── Data source: Data Layer
└── Trigger: [promotion triggers]

OPTIE B - Met custom parameters:
├── Event Name: {{Event}}
├── Event Parameters:
│   ├── promotion_id: {{DLV - promotion_id}}
│   ├── promotion_name: {{DLV - promotion_name}}
│   ├── creative_name: {{DLV - creative_name}}
│   └── creative_slot: {{DLV - creative_slot}}
└── Trigger: [promotion triggers]
```

## Promotie Naming Conventions

```
PROMOTIE NAMING BEST PRACTICES
==============================

PROMOTION_ID FORMAT:
────────────────────
[type]_[campaign]_[jaar]_[variant]

Voorbeelden:
├── sale_summer_2024_v1
├── promo_blackfriday_2024_hero
├── banner_newcollection_2024_sidebar
└── popup_newsletter_2024_exit

CREATIVE_NAME FORMAT:
─────────────────────
[format]_[theme]_[variant]

Voorbeelden:
├── hero_beach_lifestyle
├── banner_discount_red
├── tile_product_minimal
└── popup_urgency_countdown

CREATIVE_SLOT FORMAT:
─────────────────────
[pagina]_[positie]

Voorbeelden:
├── homepage_hero
├── homepage_midpage_left
├── category_sidebar_top
├── product_related_bottom
├── cart_upsell_modal
└── checkout_crosssell

CONSISTENTIE TIPS:
──────────────────
┌────────────────────────┬───────────────────────────────────────────┐
│ DO                     │ DON'T                                     │
├────────────────────────┼───────────────────────────────────────────┤
│ Lowercase alleen       │ Mixcase (SummerSale)                      │
├────────────────────────┼───────────────────────────────────────────┤
│ Underscores (_)        │ Spaties of hyphens                        │
├────────────────────────┼───────────────────────────────────────────┤
│ Dateerbare namen       │ Generieke namen (promo1, banner2)         │
├────────────────────────┼───────────────────────────────────────────┤
│ Beschrijvende namen    │ Afkortingen (bf24 i.p.v. blackfriday_2024)│
├────────────────────────┼───────────────────────────────────────────┤
│ Documenteer conventies │ Ad-hoc benamingen                         │
└────────────────────────┴───────────────────────────────────────────┘
```

## Promotie Performance Analyse

```
GA4 PROMOTIE REPORTS
====================

LOCATIE: Reports → Monetization → Promotions

BESCHIKBARE METRICS:
┌─────────────────────────┬──────────────────────────────────────────┐
│ Metric                  │ Betekenis                                │
├─────────────────────────┼──────────────────────────────────────────┤
│ Item promotion views    │ Aantal view_promotion events             │
├─────────────────────────┼──────────────────────────────────────────┤
│ Item promotion clicks   │ Aantal select_promotion events           │
├─────────────────────────┼──────────────────────────────────────────┤
│ Item promotion CTR      │ Clicks / Views × 100%                    │
└─────────────────────────┴──────────────────────────────────────────┘

PROMOTIE FUNNEL EXPLORATION:
────────────────────────────
SETUP:
├── Technique: Funnel exploration
├── Steps:
│   ├── Step 1: view_promotion (met promotion_id filter)
│   ├── Step 2: select_promotion
│   ├── Step 3: view_item
│   ├── Step 4: add_to_cart
│   └── Step 5: purchase
└── Breakdown: promotion_name of creative_slot

COUPON ANALYSIS EXPLORATION:
────────────────────────────
SETUP:
├── Technique: Free form
├── Rows: Order coupon (custom dimension)
├── Values:
│   ├── Transactions
│   ├── Total revenue
│   ├── Average purchase value
│   └── Items purchased
└── Filter: coupon is not (not set)

⚠️ NOOT: "Order coupon" moet als custom dimension
   geregistreerd zijn in GA4 Admin
```

## Coupon Custom Dimension Setup

```
COUPON CUSTOM DIMENSION REGISTREREN
===================================

WAAROM NODIG:
├── coupon parameter is event-scoped
├── Voor rapportage als dimension nodig
└── Maakt grouping en filtering mogelijk

STAP 1: GA4 ADMIN
─────────────────
1. Admin → Custom definitions → Create custom dimension
2. Configuratie:
   ├── Dimension name: Order Coupon
   ├── Scope: Event
   ├── Event parameter: coupon
   └── Save

STAP 2: WACHT OP DATA
─────────────────────
├── Nieuwe dimension zichtbaar na ~24 uur
├── Alleen events NA registratie krijgen dimension
└── Geen historische data

ALTERNATIEF: ITEM-SCOPED COUPON
───────────────────────────────
1. Admin → Custom definitions → Create custom dimension
2. Configuratie:
   ├── Dimension name: Item Coupon
   ├── Scope: Item
   ├── Event parameter: coupon
   └── Save

RESULTAAT:
──────────
├── Order Coupon: Coupon op order niveau
├── Item Coupon: Coupon op product niveau
└── Beide bruikbaar in reports en explorations
```

## A/B Testing Promoties

```
PROMOTIE A/B TEST TRACKING
==========================

METHODE 1: CREATIVE VARIANTS
────────────────────────────
Track varianten via creative_name:

// Variant A
dataLayer.push({
  event: "view_promotion",
  ecommerce: {
    items: [{
      promotion_id: "summer_sale_2024",
      promotion_name: "Zomer Sale 2024",
      creative_name: "hero_variant_a_red",    // Variant identifier
      creative_slot: "homepage_hero"
    }]
  }
});

// Variant B
dataLayer.push({
  event: "view_promotion",
  ecommerce: {
    items: [{
      promotion_id: "summer_sale_2024",
      promotion_name: "Zomer Sale 2024",
      creative_name: "hero_variant_b_blue",   // Variant identifier
      creative_slot: "homepage_hero"
    }]
  }
});

ANALYSE:
├── Vergelijk CTR per creative_name
├── Track conversies per variant
└── Statistische significantie berekenen


METHODE 2: USER PROPERTY VOOR TEST GROUP
────────────────────────────────────────
// Bij page load, set test group
gtag('set', 'user_properties', {
  promo_test_group: 'variant_b'
});

VOORDELEN:
├── User-level tracking
├── Cross-session consistentie
└── Makkelijker segmenteren


METHODE 3: GA4 + OPTIMIZE INTEGRATIE
────────────────────────────────────
├── (Google Optimize is deprecated)
├── Gebruik externe A/B tool
├── Stuur experiment ID naar GA4
└── Analyseer in custom exploration
```

## Veelvoorkomende Problemen

```
TROUBLESHOOTING PROMOTIE TRACKING
=================================

PROBLEEM: view_promotion events te veel
───────────────────────────────────────
Oorzaken:
├── Event fired bij elke scroll
├── Geen deduplicatie logica
├── SPA route changes re-triggeren
└── Carousel auto-rotation

Oplossing:
├── Track alleen eerste view per sessie
├── Gebruik IntersectionObserver correct
├── Implement session-based deduplicatie
└── Carousel: track alleen user-initiated views

IMPLEMENTATIE:
──────────────
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


PROBLEEM: Coupon data niet in reports
─────────────────────────────────────
Oorzaken:
├── coupon parameter ontbreekt in purchase
├── Custom dimension niet geregistreerd
├── Verkeerde parameter naam
└── Data processing delay

Oplossing:
├── Verify coupon in dataLayer
├── Check custom dimension setup
├── Exact parameter naam: "coupon"
├── Wacht 24-48 uur


PROBLEEM: Promotie CTR onrealistisch
────────────────────────────────────
Oorzaken:
├── Views en clicks tracking mismatch
├── Bot traffic
├── Click tracking op verkeerde element
└── Views overcounted

Oplossing:
├── Verify beide events tracken zelfde promo
├── Exclude known bots
├── Check click event target
└── Implement proper view deduplicatie


PROBLEEM: Attribution naar promotie onduidelijk
───────────────────────────────────────────────
Oorzaken:
├── Promotie niet doorgetrokken naar purchase
├── Session breaks
├── Multi-touch journey
└── Geen funnel tracking

Oplossing:
├── Track promotion context door funnel
├── Gebruik promotion_id consistent
├── Bouw custom funnel exploration
└── Overweeg user-scoped tracking
```

## Output: Promotion Analysis Report Template

```markdown
# GA4 Promotie Analyse Rapport

## Rapportage Periode
- **Van:** [Startdatum]
- **Tot:** [Einddatum]
- **Campagne:** [Campagne naam]

## Executive Summary

| Metric | Waarde | vs. Vorige Periode |
|--------|--------|-------------------|
| Promotie Views | XX,XXX | +XX% |
| Promotie Clicks | X,XXX | +XX% |
| Click-through Rate | X.X% | +X.X% |
| Attributed Revenue | €XX,XXX | +XX% |
| Coupon Redemptions | X,XXX | +XX% |

## Promotie Performance per Slot

| Creative Slot | Views | Clicks | CTR | Revenue |
|---------------|-------|--------|-----|---------|
| homepage_hero | XX,XXX | X,XXX | X.X% | €X,XXX |
| category_banner | XX,XXX | XXX | X.X% | €X,XXX |
| product_upsell | XX,XXX | XXX | X.X% | €X,XXX |
| cart_crosssell | X,XXX | XXX | X.X% | €X,XXX |

## Top Performing Promoties

| Promotion Name | Views | CTR | Conversions | Revenue |
|----------------|-------|-----|-------------|---------|
| [Promo 1] | XX,XXX | X.X% | XXX | €X,XXX |
| [Promo 2] | XX,XXX | X.X% | XXX | €X,XXX |
| [Promo 3] | XX,XXX | X.X% | XXX | €X,XXX |

## Creative Variant Performance (A/B Test)

| Variant | Views | CTR | Conv. Rate | Stat. Sig. |
|---------|-------|-----|------------|------------|
| Variant A (Control) | XX,XXX | X.X% | X.X% | - |
| Variant B | XX,XXX | X.X% | X.X% | XX% |
| **Winner:** | Variant [X] | +XX% CTR | +XX% Conv | ✅ |

## Coupon Code Performance

| Coupon Code | Redemptions | Revenue | Avg. Discount | AOV |
|-------------|-------------|---------|---------------|-----|
| ZOMER20 | XXX | €X,XXX | €XX | €XX |
| NIEUW10 | XXX | €X,XXX | €XX | €XX |
| VIP30 | XX | €X,XXX | €XX | €XX |

### Coupon Impact Analyse

| Metric | Met Coupon | Zonder Coupon | Verschil |
|--------|------------|---------------|----------|
| AOV | €XX | €XX | -XX% |
| Items/Order | X.X | X.X | +XX% |
| Conv. Rate | X.X% | X.X% | +XX% |

## Promotie Funnel

| Stap | Users | Drop-off |
|------|-------|----------|
| Promo View | XX,XXX | - |
| Promo Click | X,XXX | XX% |
| Product View | X,XXX | XX% |
| Add to Cart | XXX | XX% |
| Purchase | XXX | XX% |

**Promotie → Purchase Rate:** X.X%

## Aanbevelingen

### Optimalisaties
1. **[Slot/Promo]:** [Specifieke aanbeveling]
2. **[Slot/Promo]:** [Specifieke aanbeveling]

### Te Stoppen
1. **[Underperforming promo]:** CTR <X%, overweeg vervanging

### Te Testen
1. **[Test idee]:** Verwachte impact
2. **[Test idee]:** Verwachte impact

## Volgende Stappen
1. [ ] [Actie item]
2. [ ] [Actie item]
3. [ ] [Actie item]
```

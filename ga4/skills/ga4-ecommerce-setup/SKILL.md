---
name: ga4-ecommerce-setup
description: "E-commerce events implementatie voor GA4. Gebruik voor: (1) view_item, add_to_cart, purchase events configureren, (2) Enhanced e-commerce tracking opzetten, (3) Product data layer structuren, (4) E-commerce event validatie, (5) Revenue tracking in GA4. Triggers: ecommerce tracking, purchase event, add to cart, view item, product tracking, revenue ga4, winkelwagen tracking."
---

# GA4 E-commerce Setup Guide

Complete gids voor het implementeren van e-commerce tracking in Google Analytics 4 met alle vereiste events en parameters.

## Quick Decision Tree

```
GA4 E-COMMERCE IMPLEMENTATIE FLOW
│
├─► WELK TYPE WEBSHOP?
│   ├─► Shopify / WooCommerce / Magento
│   │   └─► Gebruik platform-specifieke integratie
│   │       └─► Check plugin/app configuratie
│   │
│   └─► Custom webshop
│       └─► Handmatige dataLayer implementatie
│           └─► Volg e-commerce event specs
│
├─► WELKE EVENTS NODIG?
│   ├─► Basis funnel tracking
│   │   └─► view_item → add_to_cart → purchase
│   │
│   ├─► Complete funnel tracking
│   │   └─► Alle events + checkout steps
│   │
│   └─► Advanced tracking
│       └─► + promotions, refunds, wishlists
│
└─► IMPLEMENTATIE METHODE?
    ├─► Google Tag Manager (Aanbevolen)
    │   └─► DataLayer events → GTM tags
    │
    └─► gtag.js direct
        └─► JavaScript event calls
```

## E-commerce Event Hiërarchie

```
GA4 E-COMMERCE EVENTS OVERZICHT
===============================

DISCOVERY EVENTS:
┌─────────────────────┬─────────────────────────────────────────┐
│ Event               │ Wanneer triggeren                       │
├─────────────────────┼─────────────────────────────────────────┤
│ view_item_list      │ Productlijst bekeken (categorie,        │
│                     │ zoekresultaten, aanbevelingen)          │
├─────────────────────┼─────────────────────────────────────────┤
│ select_item         │ Product aangeklikt in lijst             │
├─────────────────────┼─────────────────────────────────────────┤
│ view_item           │ Productpagina bekeken                   │
└─────────────────────┴─────────────────────────────────────────┘

CART EVENTS:
┌─────────────────────┬─────────────────────────────────────────┐
│ Event               │ Wanneer triggeren                       │
├─────────────────────┼─────────────────────────────────────────┤
│ add_to_cart         │ Product toegevoegd aan winkelwagen      │
├─────────────────────┼─────────────────────────────────────────┤
│ remove_from_cart    │ Product verwijderd uit winkelwagen      │
├─────────────────────┼─────────────────────────────────────────┤
│ view_cart           │ Winkelwagen pagina bekeken              │
└─────────────────────┴─────────────────────────────────────────┘

CHECKOUT EVENTS:
┌─────────────────────┬─────────────────────────────────────────┐
│ Event               │ Wanneer triggeren                       │
├─────────────────────┼─────────────────────────────────────────┤
│ begin_checkout      │ Checkout proces gestart                 │
├─────────────────────┼─────────────────────────────────────────┤
│ add_shipping_info   │ Verzendgegevens ingevuld                │
├─────────────────────┼─────────────────────────────────────────┤
│ add_payment_info    │ Betaalgegevens ingevuld                 │
├─────────────────────┼─────────────────────────────────────────┤
│ purchase            │ Transactie voltooid (thank you page)    │
└─────────────────────┴─────────────────────────────────────────┘

POST-PURCHASE EVENTS:
┌─────────────────────┬─────────────────────────────────────────┐
│ Event               │ Wanneer triggeren                       │
├─────────────────────┼─────────────────────────────────────────┤
│ refund              │ (Gedeeltelijke) terugbetaling           │
└─────────────────────┴─────────────────────────────────────────┘
```

## DataLayer Implementatie

### view_item Event

```javascript
VIEW_ITEM EVENT
===============

WANNEER: Productpagina wordt geladen

DATALAYER CODE:
─────────────────────────────────────────────────────────────────
dataLayer.push({ ecommerce: null });  // Clear previous ecommerce
dataLayer.push({
  event: "view_item",
  ecommerce: {
    currency: "EUR",
    value: 29.99,                     // Product prijs
    items: [{
      item_id: "SKU12345",            // VERPLICHT: Unieke product ID
      item_name: "Product Naam",      // VERPLICHT: Product naam
      affiliation: "Shop Naam",       // Optioneel: Store/affiliate
      coupon: "KORTING10",            // Optioneel: Toegepaste coupon
      discount: 3.00,                 // Optioneel: Kortingsbedrag
      index: 0,                       // Optioneel: Positie in lijst
      item_brand: "Merk",             // Aanbevolen: Merknaam
      item_category: "Categorie",     // Aanbevolen: Hoofdcategorie
      item_category2: "Subcategorie", // Optioneel: Subcategorie
      item_category3: "Sub-sub",      // Optioneel: Diepere categorie
      item_list_id: "related_prod",   // Optioneel: Lijst ID
      item_list_name: "Gerelateerd",  // Optioneel: Lijst naam
      item_variant: "Rood / L",       // Optioneel: Variant (kleur/maat)
      price: 29.99,                   // VERPLICHT: Prijs per stuk
      quantity: 1                     // VERPLICHT: Aantal
    }]
  }
});
─────────────────────────────────────────────────────────────────

⚠️ BELANGRIJK:
├── Altijd ecommerce: null eerst om vorige data te clearen
├── item_id en item_name zijn VERPLICHT
├── price moet numeriek zijn (geen string)
└── currency moet ISO 4217 format zijn (EUR, USD, etc.)
```

### add_to_cart Event

```javascript
ADD_TO_CART EVENT
=================

WANNEER: Product wordt toegevoegd aan winkelwagen

DATALAYER CODE:
─────────────────────────────────────────────────────────────────
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "add_to_cart",
  ecommerce: {
    currency: "EUR",
    value: 29.99,                     // Totale waarde toegevoegd
    items: [{
      item_id: "SKU12345",
      item_name: "Product Naam",
      item_brand: "Merk",
      item_category: "Categorie",
      item_variant: "Rood / L",
      price: 29.99,
      quantity: 1
    }]
  }
});
─────────────────────────────────────────────────────────────────

TRIGGER LOCATIES:
├── "Toevoegen aan winkelwagen" button click
├── Quick-add buttons in productlijsten
├── Product configurator submit
└── Wishlist naar cart actie
```

### purchase Event

```javascript
PURCHASE EVENT (KRITISCH!)
==========================

WANNEER: Order bevestigingspagina (thank you page)

DATALAYER CODE:
─────────────────────────────────────────────────────────────────
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "purchase",
  ecommerce: {
    transaction_id: "ORD-2024-12345", // VERPLICHT: Unieke order ID
    value: 89.97,                      // VERPLICHT: Totaal incl. BTW
    tax: 15.63,                        // Aanbevolen: BTW bedrag
    shipping: 4.99,                    // Aanbevolen: Verzendkosten
    currency: "EUR",                   // VERPLICHT: Valuta
    coupon: "KORTING10",               // Optioneel: Order-level coupon
    items: [
      {
        item_id: "SKU12345",
        item_name: "Product 1",
        item_brand: "Merk A",
        item_category: "Categorie",
        item_variant: "Rood / L",
        price: 29.99,
        quantity: 2
      },
      {
        item_id: "SKU67890",
        item_name: "Product 2",
        item_brand: "Merk B",
        item_category: "Accessoires",
        price: 29.99,
        quantity: 1
      }
    ]
  }
});
─────────────────────────────────────────────────────────────────

⚠️ KRITISCHE PUNTEN:
├── transaction_id MOET uniek zijn per order
├── Duplicate transaction_id's worden gededupliceerd (goed!)
├── value = subtotaal + tax + shipping - discount
├── Fire ALLEEN op succesvolle orders
├── Nooit op cart/checkout pagina's
└── Test grondig met DebugView
```

### Checkout Events Sequence

```javascript
CHECKOUT EVENTS SEQUENCE
========================

STAP 1: begin_checkout
───────────────────────
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "begin_checkout",
  ecommerce: {
    currency: "EUR",
    value: 89.97,
    coupon: "KORTING10",              // Als al toegepast
    items: [/* alle cart items */]
  }
});

STAP 2: add_shipping_info
─────────────────────────
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "add_shipping_info",
  ecommerce: {
    currency: "EUR",
    value: 89.97,
    shipping_tier: "Express",          // Verzendmethode naam
    items: [/* alle cart items */]
  }
});

STAP 3: add_payment_info
────────────────────────
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "add_payment_info",
  ecommerce: {
    currency: "EUR",
    value: 89.97,
    payment_type: "iDEAL",             // Betaalmethode
    items: [/* alle cart items */]
  }
});

STAP 4: purchase
────────────────
// Zie purchase event hierboven
```

## GTM Configuratie

```
GOOGLE TAG MANAGER E-COMMERCE SETUP
===================================

STAP 1: DATALAYER VARIABELEN AANMAKEN
─────────────────────────────────────
Variabele Type: Data Layer Variable

Te maken variabelen:
┌──────────────────────────┬─────────────────────────────┐
│ Variabele naam           │ Data Layer Variable Name    │
├──────────────────────────┼─────────────────────────────┤
│ DLV - ecommerce          │ ecommerce                   │
├──────────────────────────┼─────────────────────────────┤
│ DLV - ecommerce.items    │ ecommerce.items             │
├──────────────────────────┼─────────────────────────────┤
│ DLV - ecommerce.value    │ ecommerce.value             │
├──────────────────────────┼─────────────────────────────┤
│ DLV - transaction_id     │ ecommerce.transaction_id    │
├──────────────────────────┼─────────────────────────────┤
│ DLV - ecommerce.currency │ ecommerce.currency          │
└──────────────────────────┴─────────────────────────────┘

STAP 2: TRIGGERS AANMAKEN
─────────────────────────
Trigger Type: Custom Event

Per e-commerce event:
├── view_item trigger     → Event name: view_item
├── add_to_cart trigger   → Event name: add_to_cart
├── begin_checkout trigger→ Event name: begin_checkout
├── purchase trigger      → Event name: purchase
└── etc.

STAP 3: GA4 EVENT TAG
─────────────────────
Tag Type: Google Analytics: GA4 Event

Configuratie:
├── Configuration Tag: [Je GA4 Config tag]
├── Event Name: {{Event}}
├── Event Parameters:
│   ├── items: {{DLV - ecommerce.items}}
│   ├── value: {{DLV - ecommerce.value}}
│   ├── currency: {{DLV - ecommerce.currency}}
│   └── transaction_id: {{DLV - transaction_id}}
└── Trigger: [Alle e-commerce triggers]

⚠️ OF gebruik "Send Ecommerce data" checkbox:
├── Check "Send Ecommerce data"
├── Data source: Data Layer
└── GTM handelt de rest automatisch
```

## Platform-Specifieke Implementaties

```
SHOPIFY IMPLEMENTATIE
=====================

OPTIE 1: Native GA4 integratie
├── Admin → Online Store → Preferences
├── Vul Google Analytics 4 Measurement ID in
├── Basis tracking automatisch
└── BEPERKT: Niet alle events supported

OPTIE 2: Shopify Pixels (Aanbevolen)
├── Admin → Settings → Customer Events
├── Add custom pixel met GA4 code
├── Volledige controle over events
└── Ondersteunt alle e-commerce events

OPTIE 3: Third-party apps
├── Elevar (premium, zeer compleet)
├── Analyzify (goed voor beginners)
└── Littledata (enterprise focus)

WOOCOMMERCE IMPLEMENTATIE
=========================

OPTIE 1: GTM4WP Plugin (Aanbevolen)
├── Install GTM4WP (gratis)
├── Configureer e-commerce tracking
├── DataLayer automatisch gevuld
└── Koppel met GTM voor GA4 tags

OPTIE 2: MonsterInsights
├── Premium feature voor e-commerce
├── Minder flexibel dan GTM4WP
└── Makkelijker voor beginners

MAGENTO IMPLEMENTATIE
=====================

├── Gebruik GTM module (Amasty, MagePlaza)
├── Configureer dataLayer output
├── Handmatige mapping naar GA4 events
└── Test grondig met staged orders
```

## Veelvoorkomende Problemen

```
TROUBLESHOOTING E-COMMERCE TRACKING
===================================

PROBLEEM: Purchase events niet zichtbaar
────────────────────────────────────────
Oorzaken:
├── DataLayer niet correct geïmplementeerd
├── Thank you page redirect te snel
├── Tag firing before dataLayer ready
├── Consent niet gegeven
└── transaction_id ontbreekt

Oplossing:
├── Check dataLayer in browser console
├── Gebruik GTM Preview mode
├── Voeg dataLayer.push toe VOOR page load
├── Verify in GA4 DebugView
└── Check consent mode status

PROBLEEM: Revenue klopt niet
────────────────────────────
Oorzaken:
├── Prijs als string i.p.v. number
├── BTW dubbel geteld
├── Valuta mismatch
├── Duplicate transactions
└── Test orders in productie

Oplossing:
├── Verify: typeof price === 'number'
├── Controleer value berekening
├── Match currency met GA4 property
├── Check transaction_id uniciteit
└── Exclude interne IP's

PROBLEEM: Items array leeg
──────────────────────────
Oorzaken:
├── Async loading issues
├── DataLayer timing
├── SPA routing problemen
└── Object reference errors

Oplossing:
├── Log dataLayer naar console
├── Wacht op DOM ready
├── Gebruik callback na cart update
└── Clone objects before push

PROBLEEM: Checkout funnel incomplete
────────────────────────────────────
Oorzaken:
├── Niet alle checkout events geïmplementeerd
├── Event volgorde incorrect
├── Single Page Checkout complications
└── Payment redirect verliest sessie

Oplossing:
├── Implementeer ALLE checkout events
├── Verify chronologische volgorde
├── Test volledige checkout flow
└── Cross-domain tracking voor payment
```

## E-commerce Audit Checklist

```
E-COMMERCE TRACKING AUDIT
=========================

□ DATALAYER STRUCTUUR
├── □ ecommerce object correct genest
├── □ ecommerce: null voor elk event
├── □ Alle verplichte velden aanwezig
├── □ Juiste data types (number, string)
└── □ Consistente item_id across events

□ EVENT IMPLEMENTATIE
├── □ view_item op alle productpagina's
├── □ add_to_cart bij alle add-acties
├── □ begin_checkout bij checkout start
├── □ purchase ALLEEN bij success
└── □ refund voor retouren (optioneel)

□ DATA KWALITEIT
├── □ Prijzen zijn numeriek
├── □ Currency is ISO 4217
├── □ transaction_id is uniek
├── □ Quantities zijn integers
└── □ Geen PII in custom parameters

□ GTM CONFIGURATIE
├── □ Alle variabelen aangemaakt
├── □ Triggers per event type
├── □ GA4 tag correct geconfigureerd
├── □ Preview mode getest
└── □ Container gepubliceerd

□ GA4 VERIFICATIE
├── □ Events zichtbaar in DebugView
├── □ Parameters correct doorkomen
├── □ Revenue rapporteert correct
├── □ Monetization reports vullen
└── □ Key Events gemarkeerd
```

## Output: E-commerce Implementation Template

```markdown
# GA4 E-commerce Implementatie Rapport

## Webshop Informatie
- **Platform:** [Shopify/WooCommerce/Custom/etc.]
- **GA4 Property:** G-XXXXXXXXXX
- **Implementatie methode:** [GTM/Direct/Plugin]
- **Datum:** [Datum]

## Geïmplementeerde Events

| Event | Status | Trigger Locatie |
|-------|--------|-----------------|
| view_item_list | ✅ | Categoriepagina's, zoekresultaten |
| select_item | ✅ | Product clicks in lijsten |
| view_item | ✅ | Alle productpagina's |
| add_to_cart | ✅ | Add to cart buttons |
| remove_from_cart | ✅ | Cart verwijder acties |
| view_cart | ✅ | Winkelwagen pagina |
| begin_checkout | ✅ | Checkout start |
| add_shipping_info | ✅ | Na verzendkeuze |
| add_payment_info | ✅ | Na betalingskeuze |
| purchase | ✅ | Thank you page |
| refund | ⏳ | [Nog te implementeren] |

## DataLayer Verificatie

| Veld | Aanwezig | Format Correct |
|------|----------|----------------|
| item_id | ✅ | ✅ String |
| item_name | ✅ | ✅ String |
| price | ✅ | ✅ Number |
| quantity | ✅ | ✅ Integer |
| currency | ✅ | ✅ ISO 4217 |
| transaction_id | ✅ | ✅ Uniek |

## Test Resultaten

| Test Case | Resultaat | Notities |
|-----------|-----------|----------|
| Product view tracking | ✅ Pass | - |
| Add to cart tracking | ✅ Pass | - |
| Complete checkout | ✅ Pass | Test order ID: [X] |
| Revenue accuracy | ✅ Pass | Matched backend |
| Multiple items order | ✅ Pass | - |

## GA4 Monetization Reports

- **Revenue zichtbaar:** ✅ Ja
- **Product performance:** ✅ Werkend
- **Checkout funnel:** ✅ Alle stappen zichtbaar

## Volgende Stappen
1. [ ] Refund tracking implementeren
2. [ ] Promotion tracking toevoegen
3. [ ] Product scoping uitbreiden

## Notities
[Eventuele aanvullende opmerkingen]
```

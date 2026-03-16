---
name: ga4-data-layer-guide
description: "Google Tag Manager dataLayer implementatie gids voor GA4. Gebruik voor: (1) dataLayer structuur opzetten, (2) E-commerce dataLayer implementeren, (3) User data naar dataLayer pushen, (4) Form en event data via dataLayer, (5) Debug en validate dataLayer. Triggers: dataLayer, gtm datalayer, e-commerce datalayer, push datalayer, data layer variables, gtm implementation."
---

# GA4 Data Layer Guide

Complete gids voor het implementeren van een robuuste dataLayer voor Google Analytics 4 via Google Tag Manager.

## Quick Decision Tree

```
WANNEER DATALAYER GEBRUIKEN?
│
├─► ALTIJD AANBEVOLEN VOOR:
│   ├── E-commerce tracking (product data, cart, purchase)
│   ├── User properties (membership, customer type)
│   ├── Dynamic content data (ab-tests, personalisatie)
│   ├── Form data (form name, values)
│   └── Server-side data (CRM data, backend events)
│       └─► IMPLEMENTEER DATALAYER ✅
│
├─► OPTIONEEL VOOR:
│   ├── Simpele click tracking
│   ├── Scroll tracking
│   └── Basic page views
│       └─► GTM built-in variables vaak voldoende
│
└─► HOE IMPLEMENTEREN?
    ├── CMS/Platform heeft native support
    │   └─► Gebruik platform plugin/module
    │
    ├── Custom website
    │   └─► Developer implementeert in code
    │
    └── Geen developer access
        └─► Custom HTML tags in GTM (limited)
```

## DataLayer Basics

```
WAT IS DE DATALAYER?
====================

┌────────────────────────────────────────────────────────────────┐
│  dataLayer = JavaScript array die data deelt met GTM          │
│                                                                │
│  FLOW:                                                         │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐ │
│  │ Website  │ -> │ dataLayer│ -> │   GTM    │ -> │   GA4    │ │
│  │  Code    │    │  Array   │    │  Tags    │    │ Property │ │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘ │
│                                                                │
│  VOORDELEN:                                                    │
│  ├── Scheiding van data en tracking logic                      │
│  ├── Flexibiliteit: wijzig tracking zonder code changes        │
│  ├── Betrouwbaarheid: data beschikbaar wanneer nodig           │
│  ├── Structured data: consistente formats                      │
│  └── Debug-friendly: makkelijk te inspecteren                  │
└────────────────────────────────────────────────────────────────┘

BASIC SYNTAX:
─────────────
// Initialiseer dataLayer (vóór GTM snippet)
window.dataLayer = window.dataLayer || [];

// Push data naar dataLayer
dataLayer.push({
  'event': 'event_name',
  'key': 'value'
});
```

## DataLayer Initialisatie

```
CORRECTE DATALAYER SETUP
========================

STAP 1: Initialiseer vóór GTM
─────────────────────────────

PLAATS IN <head>, VÓÓR GTM snippet:

```html
<script>
  window.dataLayer = window.dataLayer || [];

  // Optioneel: initiële page data
  dataLayer.push({
    'pageType': 'product',
    'pageCategory': 'electronics',
    'userLoggedIn': true,
    'userId': 'user_12345',
    'userType': 'returning'
  });
</script>

<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){...})(window,document,'script','dataLayer','GTM-XXXXX');</script>
<!-- End Google Tag Manager -->
```


STAP 2: GTM Container Code
──────────────────────────
GTM snippet komt NA de dataLayer initialisatie.
Dit zorgt dat data beschikbaar is bij page load.


VOLGORDE IS KRITIEK:
────────────────────
1. dataLayer = window.dataLayer || [];
2. dataLayer.push({initial page data});
3. GTM <script> tag
4. Rest van de page
5. dataLayer.push() voor events (forms, clicks, etc.)
```

## DataLayer Variables in GTM

```
DATALAYER VARIABLES CONFIGUREREN
================================

STAP 1: Maak Data Layer Variable
────────────────────────────────
LOCATIE: GTM → Variables → User-Defined Variables → New

CONFIGURATIE:
┌────────────────────────────────────────────────────────────────┐
│ Variable Type: Data Layer Variable                             │
│                                                                │
│ Data Layer Variable Name: [exact key name]                     │
│ Voorbeeld: pageType                                            │
│                                                                │
│ Data Layer Version: Version 2 (aanbevolen)                     │
│                                                                │
│ Set Default Value: [optioneel fallback]                        │
└────────────────────────────────────────────────────────────────┘

NAMING CONVENTION:
├── Prefix: DLV - (Data Layer Variable)
├── Voorbeeld: {{DLV - pageType}}
├── Voorbeeld: {{DLV - user.membershipLevel}}
└── Voorbeeld: {{DLV - ecommerce.items}}


NESTED VALUES:
──────────────
dataLayer.push({
  'user': {
    'id': '12345',
    'type': 'premium',
    'ltv': 500
  }
});

GTM Variable Name: user.id → krijgt '12345'
GTM Variable Name: user.type → krijgt 'premium'


ARRAY VALUES:
─────────────
Voor e-commerce items (array):
Data Layer Variable Name: ecommerce.items
→ Krijgt hele array, gebruik in GA4 Event tag
```

## Page Data Layer

```
PAGE-LEVEL DATALAYER STRUCTUUR
==============================

STANDAARD PAGE DATA:

```javascript
dataLayer.push({
  // Page identificatie
  'pageType': 'product',           // home, category, product, cart, checkout, thank-you
  'pageCategory': 'electronics',   // content category
  'pageName': 'iPhone 15 Pro',     // friendly page name

  // Content data
  'contentGroup': 'Products',
  'author': 'Admin',               // voor blogs/content
  'publishDate': '2024-01-15',

  // User status
  'userLoggedIn': true,
  'userId': 'user_abc123',         // gehashte/anonieme ID
  'userType': 'customer',          // visitor, lead, customer

  // Business context
  'storeLocation': 'Amsterdam',
  'language': 'nl-NL',
  'currency': 'EUR'
});
```


PAGE TYPES VOORBEELDEN:
───────────────────────

HOME PAGE:
```javascript
dataLayer.push({
  'pageType': 'home',
  'pageCategory': 'homepage',
  'userLoggedIn': false
});
```

PRODUCT PAGE:
```javascript
dataLayer.push({
  'pageType': 'product',
  'pageCategory': 'electronics',
  'productId': 'SKU-12345',
  'productName': 'iPhone 15 Pro',
  'productPrice': 1199.00,
  'productCategory': 'Smartphones'
});
```

CATEGORY PAGE:
```javascript
dataLayer.push({
  'pageType': 'category',
  'pageCategory': 'electronics',
  'categoryName': 'Smartphones',
  'productCount': 48
});
```
```

## E-commerce DataLayer (GA4 Format)

```
GA4 E-COMMERCE DATALAYER
========================

VIEW ITEM (Product Page View)
─────────────────────────────

```javascript
dataLayer.push({ ecommerce: null });  // Clear previous
dataLayer.push({
  'event': 'view_item',
  'ecommerce': {
    'currency': 'EUR',
    'value': 1199.00,
    'items': [{
      'item_id': 'SKU-12345',
      'item_name': 'iPhone 15 Pro',
      'item_brand': 'Apple',
      'item_category': 'Electronics',
      'item_category2': 'Smartphones',
      'item_variant': '256GB Black',
      'price': 1199.00,
      'quantity': 1
    }]
  }
});
```


ADD TO CART
───────────

```javascript
dataLayer.push({ ecommerce: null });
dataLayer.push({
  'event': 'add_to_cart',
  'ecommerce': {
    'currency': 'EUR',
    'value': 1199.00,
    'items': [{
      'item_id': 'SKU-12345',
      'item_name': 'iPhone 15 Pro',
      'item_brand': 'Apple',
      'item_category': 'Electronics',
      'item_variant': '256GB Black',
      'price': 1199.00,
      'quantity': 1
    }]
  }
});
```


BEGIN CHECKOUT
──────────────

```javascript
dataLayer.push({ ecommerce: null });
dataLayer.push({
  'event': 'begin_checkout',
  'ecommerce': {
    'currency': 'EUR',
    'value': 1398.00,
    'coupon': 'SUMMER10',
    'items': [
      {
        'item_id': 'SKU-12345',
        'item_name': 'iPhone 15 Pro',
        'price': 1199.00,
        'quantity': 1
      },
      {
        'item_id': 'SKU-67890',
        'item_name': 'AirPods Pro',
        'price': 199.00,
        'quantity': 1
      }
    ]
  }
});
```


PURCHASE
────────

```javascript
dataLayer.push({ ecommerce: null });
dataLayer.push({
  'event': 'purchase',
  'ecommerce': {
    'transaction_id': 'T-2024-001234',
    'value': 1398.00,
    'tax': 243.00,
    'shipping': 0.00,
    'currency': 'EUR',
    'coupon': 'SUMMER10',
    'items': [
      {
        'item_id': 'SKU-12345',
        'item_name': 'iPhone 15 Pro',
        'item_brand': 'Apple',
        'item_category': 'Electronics',
        'price': 1199.00,
        'quantity': 1
      },
      {
        'item_id': 'SKU-67890',
        'item_name': 'AirPods Pro',
        'item_brand': 'Apple',
        'item_category': 'Electronics',
        'price': 199.00,
        'quantity': 1
      }
    ]
  }
});
```

⚠️ BELANGRIJK:
├── Clear ecommerce object vóór elke push: dataLayer.push({ ecommerce: null });
├── Items is ALTIJD een array, ook voor 1 item
├── Gebruik GA4 naming: item_id (niet productId)
└── currency moet meegestuurd bij value
```

## User Data Layer

```
USER DATA IN DATALAYER
======================

USER PROPERTIES STRUCTUUR:

```javascript
// Bij page load (voor ingelogde users)
dataLayer.push({
  'event': 'user_data_ready',
  'user': {
    'id': 'usr_abc123',              // Hashed user ID
    'type': 'customer',              // visitor, lead, customer
    'membershipLevel': 'premium',    // free, basic, premium
    'lifetimeValue': 2500,           // LTV in currency
    'firstPurchaseDate': '2023-06-15',
    'totalOrders': 8,
    'lastOrderDate': '2024-01-10',
    'segment': 'high_value'
  }
});
```


PRIVACY-VRIENDELIJKE IMPLEMENTATIE:

```javascript
// NOOIT direct PII in dataLayer
// ❌ FOUT:
dataLayer.push({
  'email': 'jan@example.com',  // Nooit!
  'phone': '+31612345678'      // Nooit!
});

// ✅ CORRECT: Hashed values of IDs
dataLayer.push({
  'user': {
    'id': 'usr_a1b2c3d4',
    'emailHash': 'sha256_hash_of_email',
    'hasPhone': true
  }
});
```


GTM SETUP VOOR USER PROPERTIES:

1. Data Layer Variables:
   ├── DLV - user.id
   ├── DLV - user.type
   ├── DLV - user.membershipLevel
   └── DLV - user.lifetimeValue

2. GA4 Config Tag → User Properties:
   ├── user_id: {{DLV - user.id}}
   ├── customer_type: {{DLV - user.type}}
   ├── membership_level: {{DLV - user.membershipLevel}}
   └── lifetime_value: {{DLV - user.lifetimeValue}}
```

## Form DataLayer

```
FORM DATA VIA DATALAYER
=======================

FORM SUBMIT PUSH:

```javascript
// Bij succesvolle form submit
dataLayer.push({
  'event': 'form_submit',
  'form': {
    'id': 'contact-form',
    'name': 'Contact Form',
    'location': 'homepage-hero',
    'type': 'lead',
    'fields': {
      'hasPhone': true,
      'hasCompany': true,
      'interest': 'demo-request'
    }
  }
});
```


MULTI-STEP FORM TRACKING:

```javascript
// Stap 1 compleet
dataLayer.push({
  'event': 'form_step',
  'form': {
    'name': 'Quote Request',
    'step': 1,
    'stepName': 'Contact Details'
  }
});

// Stap 2 compleet
dataLayer.push({
  'event': 'form_step',
  'form': {
    'name': 'Quote Request',
    'step': 2,
    'stepName': 'Project Details'
  }
});

// Final submit
dataLayer.push({
  'event': 'form_submit',
  'form': {
    'name': 'Quote Request',
    'step': 3,
    'stepName': 'Submit',
    'complete': true
  }
});
```


GTM SETUP:

Trigger:
├── Type: Custom Event
├── Event name: form_submit

Tag (GA4 Event):
├── Event name: generate_lead
├── Parameters:
│   ├── form_name: {{DLV - form.name}}
│   ├── form_location: {{DLV - form.location}}
│   └── form_type: {{DLV - form.type}}
```

## Custom Event DataLayer

```
CUSTOM EVENTS VIA DATALAYER
===========================

GENERAL SYNTAX:

```javascript
dataLayer.push({
  'event': 'custom_event_name',    // Triggers GTM
  'eventCategory': 'Videos',        // Optional categorization
  'eventAction': 'play',
  'eventLabel': 'Product Demo',
  // Custom data
  'customKey': 'customValue'
});
```


VOORBEELDEN:

VIDEO PLAY:
```javascript
dataLayer.push({
  'event': 'video_play',
  'video': {
    'title': 'Product Demo 2024',
    'id': 'vid_123',
    'duration': 180,
    'provider': 'vimeo'
  }
});
```

CTA CLICK:
```javascript
dataLayer.push({
  'event': 'cta_click',
  'cta': {
    'text': 'Get Started',
    'location': 'homepage-hero',
    'destination': '/signup',
    'variant': 'primary'
  }
});
```

CALCULATOR USE:
```javascript
dataLayer.push({
  'event': 'calculator_complete',
  'calculator': {
    'type': 'roi-calculator',
    'result': 25000,
    'inputs': {
      'revenue': 100000,
      'savings': 25
    }
  }
});
```

FILE DOWNLOAD:
```javascript
dataLayer.push({
  'event': 'file_download',
  'file': {
    'name': 'whitepaper-2024.pdf',
    'type': 'pdf',
    'category': 'whitepaper',
    'size': '2.5MB'
  }
});
```
```

## DataLayer Debugging

```
DATALAYER DEBUG WORKFLOW
========================

METHODE 1: Browser Console
──────────────────────────
1. Open Developer Tools (F12)
2. Console tab
3. Type: dataLayer
4. Expandeer array om alle pushes te zien

PRO TIP:
// Realtime monitoring
dataLayer.push = function(obj) {
  console.log('dataLayer push:', obj);
  Array.prototype.push.call(this, obj);
};


METHODE 2: GTM Preview Mode
───────────────────────────
1. GTM → Preview
2. Enter site URL
3. In Tag Assistant:
   ├── Click event in left panel
   ├── Check "Data Layer" tab
   └── Verify all variables present

WAT TE CHECKEN:
├── Event name correct
├── Alle keys aanwezig
├── Values correct type (string/number/array)
├── Geen undefined values
└── Timing: data aanwezig vóór tag fires


METHODE 3: dataLayer Inspector Extension
────────────────────────────────────────
Browser Extension: "dataLayer Inspector+"
├── Real-time dataLayer monitoring
├── Push history
├── Syntax highlighting
└── Filter op event type


METHODE 4: Console Snippet
──────────────────────────

```javascript
// Paste in console voor live monitoring
(function() {
  var originalPush = dataLayer.push;
  dataLayer.push = function() {
    console.group('dataLayer.push');
    console.log(arguments[0]);
    console.groupEnd();
    return originalPush.apply(this, arguments);
  };
  console.log('dataLayer monitoring enabled');
})();
```
```

## Common DataLayer Issues

```
TROUBLESHOOTING DATALAYER
=========================

PROBLEEM: GTM ziet dataLayer variable niet
──────────────────────────────────────────
Oorzaken:
├── Push gebeurt NA tag firing
├── Verkeerde variable naam (typo)
├── Data Layer Version mismatch
└── Scope issue (variable niet global)

Oplossing:
├── Verify timing: data moet er zijn vóór trigger
├── Check exact spelling in GTM variable
├── Gebruik Data Layer Version 2
├── Ensure window.dataLayer is global

PROBLEEM: E-commerce data niet in GA4
─────────────────────────────────────
Oorzaken:
├── ecommerce object niet gecleared
├── Items is geen array
├── Verkeerde property names (item_id vs productId)
└── Currency ontbreekt

Oplossing:
├── ALTIJD: dataLayer.push({ ecommerce: null }); vóór push
├── Items moet array zijn: items: [{}]
├── Gebruik GA4 naming convention
└── Voeg currency toe bij value

PROBLEEM: Duplicate dataLayer pushes
────────────────────────────────────
Oorzaken:
├── Code runs multiple times (SPA)
├── Event listeners niet verwijderd
├── Form submit + page load beide pushen
└── GTM Preview mode (kan duplicates veroorzaken)

Oplossing:
├── Debounce event handlers
├── Check voor existing push (flag pattern)
├── Use event.preventDefault() correctly
└── Test in incognito zonder Preview

PROBLEEM: Values zijn wrong type
────────────────────────────────
Oorzaken:
├── String waar number verwacht: "100" vs 100
├── Object waar string verwacht
└── Array formatting issues

Oplossing:
```javascript
// ❌ FOUT
dataLayer.push({
  'value': '100.00'  // String
});

// ✅ CORRECT
dataLayer.push({
  'value': 100.00    // Number
});

// Parse if needed
dataLayer.push({
  'value': parseFloat(priceString)
});
```
```

## Platform-Specific Implementations

```
PLATFORM DATALAYER IMPLEMENTATIES
=================================

SHOPIFY
───────
Gebruik Shopify's native Analytics integration + app:

Liquid template approach:
```liquid
<script>
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({
    'pageType': '{{ template.name }}',
    {% if customer %}
    'userLoggedIn': true,
    'userId': '{{ customer.id }}',
    {% endif %}
    {% if product %}
    'productId': '{{ product.id }}',
    'productName': '{{ product.title | escape }}',
    'productPrice': {{ product.price | money_without_currency | remove: ',' }}
    {% endif %}
  });
</script>
```


WORDPRESS / WOOCOMMERCE
───────────────────────
Plugins:
├── GTM4WP (Google Tag Manager for WordPress)
├── Pixel Manager for WooCommerce
└── Monster Insights

Of custom functions.php:
```php
add_action('wp_head', function() {
  global $post;
  echo "<script>
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
      'pageType': '" . get_post_type() . "',
      'pageId': " . get_the_ID() . "
    });
  </script>";
}, 1);
```


MAGENTO
───────
Modules:
├── GTM Pro by Mageworx
├── Google Tag Manager by Amasty
└── Custom module development

Native events via Magento layout XML + knockout.js


NEXT.JS / REACT
───────────────

```javascript
// _app.js of layout component
import { useEffect } from 'react';
import { useRouter } from 'next/router';

function MyApp({ Component, pageProps }) {
  const router = useRouter();

  useEffect(() => {
    const handleRouteChange = (url) => {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        'event': 'page_view',
        'page_path': url
      });
    };

    router.events.on('routeChangeComplete', handleRouteChange);
    return () => {
      router.events.off('routeChangeComplete', handleRouteChange);
    };
  }, [router.events]);

  return <Component {...pageProps} />;
}
```
```

## DataLayer Checklist

```
DATALAYER IMPLEMENTATION CHECKLIST
==================================

□ SETUP
├── □ dataLayer geïnitialiseerd vóór GTM
├── □ GTM container correct geplaatst
├── □ Geen JavaScript errors in console
└── □ dataLayer is global accessible

□ PAGE DATA
├── □ pageType op alle pages
├── □ User status (logged in, user ID)
├── □ Content category/type
└── □ Language/currency

□ E-COMMERCE (indien van toepassing)
├── □ view_item op product pages
├── □ add_to_cart events
├── □ begin_checkout event
├── □ purchase event met transaction_id
├── □ ecommerce object cleared vóór push
└── □ Items array correct geformatteerd

□ FORMS
├── □ Form submit events
├── □ Form identification (name, location)
├── □ Multi-step tracking (indien nodig)
└── □ Geen PII in dataLayer

□ CUSTOM EVENTS
├── □ Belangrijke clicks tracked
├── □ Video engagement
├── □ Downloads
└── □ Tool/calculator usage

□ GTM VARIABLES
├── □ Alle DLV variables aangemaakt
├── □ Correct genest (user.id, etc.)
├── □ Default values ingesteld
└── □ Naming convention consistent

□ TESTING
├── □ Console: dataLayer bevat juiste data
├── □ GTM Preview: variables resolved
├── □ DebugView: events komen door
├── □ Cross-browser getest
└── □ Mobile getest
```

## Output: DataLayer Implementation Template

```markdown
# DataLayer Implementation Specification

## Project Informatie
- **Website:** [URL]
- **Platform:** [Shopify/WooCommerce/Custom/etc.]
- **GTM Container:** GTM-XXXXXXX
- **Implementation datum:** [Datum]

## DataLayer Structure

### Page-Level Data (alle pagina's)
```javascript
dataLayer.push({
  'pageType': '[home|category|product|cart|checkout|thank-you|blog|landing]',
  'pageCategory': '[categorie naam]',
  'userLoggedIn': [true|false],
  'userId': '[hashed user id]',
  'userType': '[visitor|lead|customer]'
});
```

### E-commerce Events

#### view_item
- **Trigger:** Product page load
- **Required fields:** item_id, item_name, price, currency

#### add_to_cart
- **Trigger:** Add to cart button click
- **Required fields:** item_id, item_name, price, quantity, currency

#### begin_checkout
- **Trigger:** Checkout page load
- **Required fields:** items array, value, currency

#### purchase
- **Trigger:** Order confirmation page
- **Required fields:** transaction_id, value, currency, items array

### Custom Events

| Event Name | Trigger | Data Fields |
|------------|---------|-------------|
| form_submit | Form completion | form.name, form.location |
| cta_click | CTA button click | cta.text, cta.location |
| video_play | Video start | video.title, video.provider |

## GTM Variables Required

| Variable Name | Type | Data Layer Key |
|---------------|------|----------------|
| DLV - pageType | Data Layer Variable | pageType |
| DLV - user.id | Data Layer Variable | user.id |
| DLV - ecommerce.items | Data Layer Variable | ecommerce.items |
| DLV - form.name | Data Layer Variable | form.name |

## Testing Checklist
- [ ] dataLayer initialized before GTM
- [ ] Page data present on all pages
- [ ] E-commerce events firing correctly
- [ ] No PII in dataLayer
- [ ] GTM Preview shows all variables
- [ ] DebugView receives events
- [ ] Cross-browser tested

## Developer Notes
[Implementatie specifieke aantekeningen]

## Changelog
| Date | Change | Author |
|------|--------|--------|
| [Datum] | Initial implementation | [Naam] |
```

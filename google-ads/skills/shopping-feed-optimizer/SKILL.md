---
name: shopping-feed-optimizer
description: "Google Merchant Center en Shopping feed optimalisatie. Gebruik voor: (1) Product data kwaliteit verbeteren, (2) Title en description optimalisatie, (3) Custom labels strategie, (4) Feed rules automation, (5) Disapprovals oplossen, (6) Free listings optimalisatie. Triggers: shopping, merchant center, feed, product data, titles, custom labels, GMC, disapprovals."
---

# Shopping Feed Optimizer

Complete gids voor het optimaliseren van Google Merchant Center product feeds voor Shopping campaigns en Performance Max.

## Feed Kwaliteit Impact

```
FEED KWALITEIT → PERFORMANCE IMPACT
====================================

┌─────────────────────────────────────────────────────────────────┐
│  FEED ELEMENT          │  IMPACT OP PERFORMANCE                │
├─────────────────────────────────────────────────────────────────┤
│  Product Title         │  ★★★★★ Hoogste impact op CTR/relevance │
│  Product Image         │  ★★★★★ Directe impact op CTR          │
│  Price Accuracy        │  ★★★★☆ Conversie en trust             │
│  Availability          │  ★★★★☆ Waste prevention               │
│  GTIN/MPN              │  ★★★☆☆ Matching en vergelijking       │
│  Description           │  ★★★☆☆ Extended relevance             │
│  Product Type          │  ★★★☆☆ Google categorisatie           │
│  Custom Labels         │  ★★☆☆☆ Campagne segmentatie          │
│  Additional Attributes │  ★★☆☆☆ Filtering en rich results     │
└─────────────────────────────────────────────────────────────────┘
```

## Product Title Optimalisatie

### Title Structuur Framework

```
TITLE FORMULA (prioriteit volgorde)
===================================

FORMULE: [Brand] + [Product Type] + [Key Attributes] + [Model/Variant]

E-COMMERCE VOORBEELDEN:
───────────────────────
Fashion:
├── Slecht:  "Blauwe Jurk"
├── Beter:   "Nike Air Max 90 Sneakers Heren Wit Maat 43"
└── Best:    "Nike Air Max 90 - Heren Sneakers - Wit/Zwart - Maat 43"

Elektronica:
├── Slecht:  "Laptop"
├── Beter:   "Apple MacBook Pro 14 inch M3 16GB"
└── Best:    "Apple MacBook Pro 14 inch (2024) - M3 Pro - 16GB RAM - 512GB SSD"

Home & Garden:
├── Slecht:  "Lamp"
├── Beter:   "Philips Hue White Ambiance E27 LED Lamp"
└── Best:    "Philips Hue White Ambiance - E27 LED Smart Lamp - Dimbaar - Bluetooth"

MAXIMUM LENGTE: 150 karakters (gebruik minimaal 70+)
```

### Title Optimalisatie Checklist

```
TITLE CHECKLIST
===============

□ Brand naam aanwezig (begin of prominent)
□ Product type duidelijk benoemd
□ Belangrijkste attributen (kleur, maat, materiaal)
□ Model/variant specifiek
□ Geen keyword stuffing
□ Geen promotionele tekst ("Sale!", "Gratis verzending")
□ Geen hoofdletters voor hele woorden (NIKE → Nike)
□ Spelling en grammatica correct

VERPLICHTE ATTRIBUTEN PER CATEGORIE:
─────────────────────────────────────
Kleding:
├── Geslacht (Heren/Dames/Unisex)
├── Maat of maataanduiding
├── Kleur
└── Materiaal (indien relevant)

Elektronica:
├── Merk
├── Modelnummer
├── Belangrijkste specs
└── Capaciteit/Grootte

Meubels:
├── Type meubel
├── Materiaal
├── Afmetingen of maat
└── Kleur/Finish
```

### Title Generatie Script

```javascript
/**
 * Shopping Feed Title Optimizer Script
 *
 * Analyseert product titles en genereert optimalisatie suggesties.
 *
 * Setup:
 * 1. Pas SPREADSHEET_URL aan
 * 2. Run handmatig of schedule wekelijks
 */

var CONFIG = {
  SPREADSHEET_URL: 'YOUR_SPREADSHEET_URL',
  MIN_TITLE_LENGTH: 70,
  MAX_TITLE_LENGTH: 150
};

function main() {
  var products = ShoppingContent.Products.list(
    AdsApp.currentAccount().getCustomerId().replace(/-/g, '')
  );

  var issues = [];

  if (products.resources) {
    for (var i = 0; i < products.resources.length; i++) {
      var product = products.resources[i];
      var titleIssues = analyzeTitleQuality(product);

      if (titleIssues.length > 0) {
        issues.push({
          productId: product.offerId,
          currentTitle: product.title,
          issues: titleIssues,
          suggestedTitle: generateOptimizedTitle(product)
        });
      }
    }
  }

  writeToSpreadsheet(issues);
  Logger.log('Analyzed ' + (products.resources ? products.resources.length : 0) + ' products');
  Logger.log('Found ' + issues.length + ' products with title issues');
}

function analyzeTitleQuality(product) {
  var issues = [];
  var title = product.title || '';

  // Check length
  if (title.length < CONFIG.MIN_TITLE_LENGTH) {
    issues.push('Title te kort (' + title.length + ' chars, min: ' + CONFIG.MIN_TITLE_LENGTH + ')');
  }

  // Check for brand
  if (product.brand && title.toLowerCase().indexOf(product.brand.toLowerCase()) === -1) {
    issues.push('Brand ontbreekt in title');
  }

  // Check for all caps words
  var words = title.split(' ');
  for (var i = 0; i < words.length; i++) {
    if (words[i].length > 3 && words[i] === words[i].toUpperCase()) {
      issues.push('Vermijd hoofdletters: ' + words[i]);
      break;
    }
  }

  // Check for promotional text
  var promoPatterns = ['sale', 'korting', 'gratis', 'actie', '!', '%'];
  for (var i = 0; i < promoPatterns.length; i++) {
    if (title.toLowerCase().indexOf(promoPatterns[i]) !== -1) {
      issues.push('Promotionele tekst gevonden: ' + promoPatterns[i]);
      break;
    }
  }

  return issues;
}

function generateOptimizedTitle(product) {
  var parts = [];

  // Brand first
  if (product.brand) {
    parts.push(product.brand);
  }

  // Product type
  if (product.productTypes && product.productTypes.length > 0) {
    var lastType = product.productTypes[product.productTypes.length - 1];
    parts.push(lastType.split('>').pop().trim());
  }

  // Color
  if (product.color) {
    parts.push(product.color);
  }

  // Size
  if (product.sizes && product.sizes.length > 0) {
    parts.push('Maat ' + product.sizes[0]);
  }

  // Gender for apparel
  if (product.gender) {
    var genderMap = {'male': 'Heren', 'female': 'Dames', 'unisex': 'Unisex'};
    if (genderMap[product.gender]) {
      parts.push(genderMap[product.gender]);
    }
  }

  return parts.join(' - ');
}

function writeToSpreadsheet(issues) {
  // Implementation for spreadsheet export
  Logger.log('Would write ' + issues.length + ' issues to spreadsheet');
}
```

## Product Description Optimalisatie

```
DESCRIPTION BEST PRACTICES
==========================

STRUCTUUR:
├── Openingszin: Unique selling point
├── Key features: 3-5 bullet points
├── Specificaties: Technische details
├── Use case: Waarvoor geschikt
└── Geen: URLs, prijzen, promoties

VOORBEELD (Elektronica):
────────────────────────
"De Samsung Galaxy S24 Ultra combineert cutting-edge AI met
een professionele camera. Met 200MP hoofdcamera, S Pen
ondersteuning en titanium design. Ideaal voor power users
die het beste willen.

Specificaties:
- 6.8 inch Dynamic AMOLED 2X display
- Snapdragon 8 Gen 3 processor
- 200MP + 50MP + 12MP + 10MP camera systeem
- 5000mAh batterij met 45W snelladen
- IP68 water- en stofdicht"

MAXIMUM LENGTE: 5000 karakters (aanbevolen: 500-1500)

WAT TE VERMIJDEN:
├── Links naar je website
├── Prijzen of prijsvergelijkingen
├── Shipping informatie
├── Promoties of sale info
├── Competitive claims ("beste", "goedkoopste")
└── Tekst in ALL CAPS
```

## Custom Labels Strategie

### Custom Labels Overzicht

```
CUSTOM LABELS GEBRUIK
=====================

Je hebt 5 custom labels (0-4) beschikbaar voor segmentatie.

AANBEVOLEN STRATEGIE:
─────────────────────

CUSTOM LABEL 0: Margin Category
├── Values: high_margin, medium_margin, low_margin
├── Gebruik: Bid strategy per margin tier
└── Voorbeeld: Products >40% margin = high_margin

CUSTOM LABEL 1: Performance Tier
├── Values: bestseller, standard, slow_mover
├── Gebruik: Budget allocation
└── Voorbeeld: Top 20% verkopen = bestseller

CUSTOM LABEL 2: Seasonality
├── Values: summer, winter, evergreen, holiday
├── Gebruik: Seasonal campaigns
└── Voorbeeld: Winterjassen = winter

CUSTOM LABEL 3: Product Lifecycle
├── Values: new, core, clearance, discontinued
├── Gebruik: Promo campaigns
└── Voorbeeld: Oudere collecties = clearance

CUSTOM LABEL 4: Price Range
├── Values: budget, mid_range, premium, luxury
├── Gebruik: Audience targeting
└── Voorbeeld: >€500 = luxury
```

### Custom Label Feed Rules

```
FEED RULES VOOR CUSTOM LABELS
=============================

Locatie: Merchant Center → Products → Feeds → [Feed] → Feed Rules

REGEL 1: High Margin Products
─────────────────────────────
If: custom_attribute_0 > 40
Then: Set custom_label_0 to "high_margin"
Else If: custom_attribute_0 > 20
Then: Set custom_label_0 to "medium_margin"
Else: Set custom_label_0 to "low_margin"

REGEL 2: Bestsellers
────────────────────
If: sale_count_30d > [threshold]
Then: Set custom_label_1 to "bestseller"
Note: Vereist sales data in supplemental feed

REGEL 3: Price Tiers
────────────────────
If: price < 25 EUR
Then: Set custom_label_4 to "budget"
Else If: price < 100 EUR
Then: Set custom_label_4 to "mid_range"
Else If: price < 500 EUR
Then: Set custom_label_4 to "premium"
Else: Set custom_label_4 to "luxury"

REGEL 4: New Products
─────────────────────
If: date_added > [30 days ago]
Then: Set custom_label_3 to "new"
```

## Verplichte vs Optionele Attributen

```
FEED ATTRIBUTEN OVERZICHT
=========================

VERPLICHT (alle producten):
├── id: Unieke product identifier
├── title: Product naam (max 150 chars)
├── description: Product beschrijving
├── link: Product page URL
├── image_link: Hoofdafbeelding URL
├── price: Prijs met valuta (bijv. "49.99 EUR")
├── availability: in_stock / out_of_stock / preorder
└── condition: new / refurbished / used

VERPLICHT (specifieke categorieën):
───────────────────────────────────
Kleding/Fashion:
├── gender: male / female / unisex
├── age_group: adult / kids / etc.
├── color: Kleur benaming
└── size: Maat benaming

Elektronica/Variantproducten:
├── gtin: EAN/UPC barcode
├── mpn: Manufacturer Part Number
└── brand: Merknaam

STERK AANBEVOLEN:
├── additional_image_link: Extra product foto's (max 10)
├── sale_price: Actieprijs
├── sale_price_effective_date: Actie periode
├── google_product_category: Google taxonomie ID
├── product_type: Jouw categorie hiërarchie
├── shipping: Verzendkosten
├── shipping_weight: Gewicht voor berekening
├── custom_label_0-4: Segmentatie labels
└── product_highlight: Key benefits (max 150 chars, max 10)

OPTIONEEL MAAR WAARDEVOL:
├── material: Materiaal
├── pattern: Patroon
├── multipack: Aantal in verpakking
├── is_bundle: true/false voor bundles
├── energy_efficiency_class: EU energie label
├── unit_pricing_measure: Prijs per eenheid
└── unit_pricing_base_measure: Basis eenheid
```

## Image Optimalisatie

```
IMAGE REQUIREMENTS
==================

TECHNISCHE SPECS:
├── Minimum: 100x100 pixels (250x250 voor kleding)
├── Maximum: 64 megapixels
├── Formaat: JPEG, PNG, GIF, BMP, TIFF
├── Grootte: Max 16MB per image
└── URL: HTTPS vereist

BEST PRACTICES:
───────────────
□ Witte of neutrale achtergrond
□ Product vult 75-90% van frame
□ Geen tekst, watermerken of logo's op image
□ Hoge resolutie (min. 800x800 aanbevolen)
□ Product goed belicht, geen schaduwen
□ Meerdere hoeken via additional_image_link

VEEL VOORKOMENDE DISAPPROVALS:
├── Promotional text on image → Verwijder tekst overlays
├── Watermarks → Gebruik watermark-vrije versies
├── Generic images → Gebruik echte productfoto's
├── Placeholder images → Vervang door echte foto's
└── Blurry images → Gebruik hogere resolutie
```

## Disapprovals Oplossen

### Meest Voorkomende Disapprovals

```
TOP DISAPPROVALS & FIXES
========================

1. PRICE MISMATCH
─────────────────
Oorzaak: Prijs in feed ≠ prijs op landingspagina
Fix:
├── Sync feed frequentie verhogen (real-time of hourly)
├── Microdata/structured data op pagina updaten
├── Inclusief sale_price als product in sale is
└── Check valuta (EUR vs €)

2. AVAILABILITY MISMATCH
────────────────────────
Oorzaak: Feed zegt in_stock, pagina zegt uitverkocht
Fix:
├── Real-time inventory sync
├── Out of stock producten: availability = "out_of_stock"
├── Preorder: availability = "preorder"
└── Automatische feed updates bij stock changes

3. MISSING IDENTIFIER (GTIN/MPN/BRAND)
──────────────────────────────────────
Oorzaak: Verplichte identifiers ontbreken
Fix:
├── Voeg EAN/GTIN toe aan feed
├── Geen GTIN? Gebruik: identifier_exists = false
├── Zorg dat mpn OF gtin aanwezig is
└── Brand is altijd verplicht

4. POLICY VIOLATION - PROHIBITED CONTENT
────────────────────────────────────────
Oorzaak: Product valt onder restricted category
Check:
├── Wapens en munitie
├── Drugs en drugsgerelateerd
├── Counterfeit producten
├── Gevaarlijke producten
└── Adult content zonder age verification

5. LANDING PAGE NOT FOUND (404)
───────────────────────────────
Oorzaak: Product URL niet bereikbaar
Fix:
├── Check redirects (301/302)
├── Verwijder discontinued producten uit feed
├── Update URLs na site migratie
└── Zorg voor trailing slash consistentie

6. IMAGE QUALITY ISSUES
───────────────────────
Oorzaak: Afbeelding voldoet niet aan specs
Fix:
├── Minimum 100x100 (250x250 voor apparel)
├── Verwijder tekst overlays
├── Geen placeholders of stock photos
└── Goede belichting en kwaliteit
```

### Disapproval Monitor Script

```javascript
/**
 * Merchant Center Disapproval Monitor
 *
 * Monitort product disapprovals en stuurt dagelijkse alerts.
 *
 * Setup:
 * 1. Pas EMAIL aan
 * 2. Schedule dagelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',
  ALERT_THRESHOLD: 10  // Alert als >10 nieuwe disapprovals
};

function main() {
  var merchantId = AdsApp.currentAccount().getCustomerId().replace(/-/g, '');

  try {
    var products = ShoppingContent.Products.list(merchantId);
    var stats = analyzeProducts(products);

    Logger.log('=== Merchant Center Status ===');
    Logger.log('Total products: ' + stats.total);
    Logger.log('Approved: ' + stats.approved);
    Logger.log('Disapproved: ' + stats.disapproved);
    Logger.log('Pending: ' + stats.pending);

    if (stats.disapproved > CONFIG.ALERT_THRESHOLD) {
      sendDisapprovalAlert(stats);
    }

  } catch (e) {
    Logger.log('Error accessing Merchant Center: ' + e.message);
  }
}

function analyzeProducts(products) {
  var stats = {
    total: 0,
    approved: 0,
    disapproved: 0,
    pending: 0,
    issueTypes: {}
  };

  if (products.resources) {
    stats.total = products.resources.length;

    for (var i = 0; i < products.resources.length; i++) {
      var product = products.resources[i];

      // Check product status via issues
      if (product.issues && product.issues.length > 0) {
        var hasDisapproval = false;

        for (var j = 0; j < product.issues.length; j++) {
          var issue = product.issues[j];

          if (issue.servability === 'disapproved') {
            hasDisapproval = true;

            // Track issue types
            var issueType = issue.description || 'Unknown';
            if (!stats.issueTypes[issueType]) {
              stats.issueTypes[issueType] = 0;
            }
            stats.issueTypes[issueType]++;
          }
        }

        if (hasDisapproval) {
          stats.disapproved++;
        } else {
          stats.approved++;
        }
      } else {
        stats.approved++;
      }
    }
  }

  return stats;
}

function sendDisapprovalAlert(stats) {
  var subject = '⚠️ Merchant Center Alert: ' + stats.disapproved + ' Disapproved Products';

  var body = 'Merchant Center Disapproval Alert\n';
  body += '==================================\n\n';
  body += 'Total Products: ' + stats.total + '\n';
  body += 'Approved: ' + stats.approved + '\n';
  body += 'Disapproved: ' + stats.disapproved + ' ⚠️\n\n';

  body += 'Top Issues:\n';
  var sortedIssues = Object.keys(stats.issueTypes).sort(function(a, b) {
    return stats.issueTypes[b] - stats.issueTypes[a];
  });

  for (var i = 0; i < Math.min(5, sortedIssues.length); i++) {
    body += '- ' + sortedIssues[i] + ': ' + stats.issueTypes[sortedIssues[i]] + ' products\n';
  }

  body += '\nAction Required: Review disapprovals in Merchant Center\n';
  body += 'https://merchants.google.com/\n';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Free Listings Optimalisatie

```
FREE LISTINGS MAXIMALISEREN
===========================

FREE LISTINGS = Gratis product vermeldingen op:
├── Google Search (Shopping tab)
├── Google Images
├── YouTube
└── Google Lens

INSCHAKELEN:
Merchant Center → Growth → Manage Programs → Free Product Listings

OPTIMALISATIE TIPS:
───────────────────
1. Alle optionele attributen invullen
   ├── Verhoogt visibility in free listings
   ├── Meer attributen = betere matching
   └── Speciaal: shipping, availability_date

2. Product Ratings toevoegen
   ├── Review feeds integreren
   ├── Google Customer Reviews
   └── Third-party review aggregators

3. Shipping informatie
   ├── Gratis verzending benoemd
   ├── Delivery times (min_handling_time, max_handling_time)
   └── Transit times per regio

4. Promotions
   ├── Merchant Promotions program
   ├── Korting zichtbaar in listing
   └── Promo codes integreren

5. Product Highlights
   ├── product_highlight attribuut
   ├── Max 10 highlights per product
   └── Key benefits in bullets
```

## Supplemental Feeds

```
SUPPLEMENTAL FEED STRATEGIE
===========================

WAT IS EEN SUPPLEMENTAL FEED?
├── Aanvulling op primaire feed
├── Override of add attributen
├── Handig voor bulk updates
└── Geen volledige product data nodig

USE CASES:
──────────
1. Custom Labels (margin, performance)
2. Sale Prices (promoties)
3. Seasonal Updates
4. Inventory Exclusions
5. Title/Description Overrides

SETUP:
Merchant Center → Products → Feeds → Supplemental Feed

VOORBEELD SUPPLEMENTAL FEED:
─────────────────────────────
id,custom_label_0,custom_label_1,excluded_destination
SKU001,high_margin,bestseller,
SKU002,low_margin,slow_mover,"Shopping ads"
SKU003,high_margin,standard,
SKU004,,clearance,"Shopping ads,Free listings"

MATCHING RULES:
├── Match op 'id' (offerId)
├── Lege cellen = geen override
├── Werkt binnen minuten na upload
└── Schedule voor automatische updates
```

## Feed Audit Checklist

```markdown
# Shopping Feed Audit Checklist

## Data Quality Score: ___/100

### Product Identifiers
□ GTIN/EAN coverage: ___%
□ MPN coverage waar nodig: ___%
□ Brand altijd aanwezig: [ja/nee]
□ identifier_exists correct gebruikt: [ja/nee]

### Titles
□ Gemiddelde title lengte: ___ chars
□ Titles bevatten brand: ___%
□ Titles bevatten key attributes: ___%
□ Geen promotional text: [ja/nee]
□ Geen ALL CAPS: [ja/nee]

### Images
□ Alle producten hebben image: [ja/nee]
□ Image quality >800px: ___%
□ Additional images gebruikt: ___%
□ Geen watermarks/text: [ja/nee]

### Pricing & Availability
□ Prices in sync met website: [ja/nee]
□ Sale prices correct: [ja/nee]
□ Availability real-time: [ja/nee]
□ Out of stock properly marked: [ja/nee]

### Categorization
□ Google Product Category set: ___%
□ Product Type hiërarchie: [ja/nee]
□ Custom Labels in gebruik: [ja/nee]

### Disapproval Status
□ Disapproved products: ___
□ Top 3 disapproval reasons:
  1. _______________
  2. _______________
  3. _______________

### Recommendations
1. [Hoogste prioriteit actie]
2. [Tweede prioriteit actie]
3. [Derde prioriteit actie]
```

## Feed Management Best Practices

```
DAGELIJKS / ONGOING
===================
□ Inventory sync (real-time of hourly)
□ Price updates doorvoeren
□ New products toevoegen
□ Discontinued products verwijderen

WEKELIJKS
=========
□ Disapprovals reviewen en fixen
□ Feed health metrics checken
□ New product performance analyseren
□ Competitor pricing monitoren

MAANDELIJKS
===========
□ Title optimalisatie review
□ Custom labels updaten (performance-based)
□ Supplemental feeds refreshen
□ Full feed audit

SEIZOENSMATIG
=============
□ Holiday/seasonal products taggen
□ Promotions voorbereiden
□ Budget allocatie naar seizoensproducten
□ Clearance items markeren
```

## Output: Feed Optimization Report Template

```markdown
# Feed Optimization Report

📅 Datum: [DATUM]
🏢 Merchant ID: [ID]

## Executive Summary

Feed Health Score: [X]/100

### Current Status
- Total Products: [X]
- Approved: [X] ([X]%)
- Disapproved: [X] ([X]%)
- Pending: [X] ([X]%)

### Top Opportunities
1. [Opportunity + estimated impact]
2. [Opportunity + estimated impact]
3. [Opportunity + estimated impact]

## Detailed Findings

### Title Optimization (Score: X/20)
- Average length: [X] chars
- Brand inclusion: [X]%
- Improvements needed: [specifics]

### Image Quality (Score: X/20)
- High-res coverage: [X]%
- Additional images: [X]%
- Issues found: [specifics]

### Data Completeness (Score: X/20)
- GTIN coverage: [X]%
- Optional attributes: [X]%
- Missing critical data: [specifics]

### Price & Inventory (Score: X/20)
- Sync accuracy: [X]%
- Update frequency: [X]
- Issues: [specifics]

### Disapprovals (Score: X/20)
- Active disapprovals: [X]
- Top reasons: [list]
- Resolution plan: [specifics]

## Action Plan

### Week 1 (Critical)
□ [Action item]
□ [Action item]

### Week 2-3 (High Priority)
□ [Action item]
□ [Action item]

### Month 1 (Medium Priority)
□ [Action item]
□ [Action item]

## Expected Impact
- Approved products: +[X]%
- Impression share: +[X]%
- CTR improvement: +[X]%
```

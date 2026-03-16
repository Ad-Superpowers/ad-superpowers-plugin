---
name: ga4-audience-builder
description: "GA4 custom audience builder en segmentatie gids. Gebruik voor: (1) Custom audiences maken op basis van gedrag, (2) Audiences bouwen met events en user properties, (3) Sequentiële audiences voor customer journeys, (4) Comparison audiences voor A/B analyse, (5) Remarketing audiences voorbereiden voor export. Triggers: ga4 audience, segment maken, audience builder, doelgroep, gebruikerssegment, remarketing audience, custom audience."
---

# GA4 Audience Builder Guide

Complete gids voor het bouwen van krachtige custom audiences in Google Analytics 4 voor remarketing en analyse.

## Quick Decision Tree

```
GA4 AUDIENCE BUILDER FLOW
│
├─► WELK TYPE AUDIENCE?
│   ├─► Gedragsgebaseerd
│   │   └─► Events + parameters gebruiken
│   │       └─► Voorbeeld: "Users die product bekeken maar niet kochten"
│   │
│   ├─► User Property gebaseerd
│   │   └─► Demographics, lifetime value, acquisition
│   │       └─► Voorbeeld: "High-value customers (LTV > €500)"
│   │
│   ├─► Sequentieel (Journey)
│   │   └─► Steps in volgorde
│   │       └─► Voorbeeld: "Homepage → Category → Product → NO Purchase"
│   │
│   └─► Predictive (ML)
│       └─► Zie: ga4-predictive-audiences skill
│
├─► MEMBERSHIP DURATION?
│   ├─► Kort (1-7 dagen)
│   │   └─► Cart abandoners, recent visitors
│   │
│   ├─► Medium (8-30 dagen)
│   │   └─► Product interesse, engaged users
│   │
│   └─► Lang (30-540 dagen)
│       └─► Customer loyalty, seasonal shoppers
│
└─► EXPORT NODIG?
    ├─► Google Ads remarketing
    │   └─► Zie: ga4-remarketing-setup skill
    │
    └─► Alleen GA4 analyse
        └─► Geen export configuratie nodig
```

## Audience Types Overzicht

```
GA4 AUDIENCE TYPES
==================

┌───────────────────┬────────────────────────────────────────────────────┐
│ Type              │ Use Case                                           │
├───────────────────┼────────────────────────────────────────────────────┤
│ Static Conditions │ Eenvoudige if/then regels                          │
│                   │ "Users met event X"                                │
├───────────────────┼────────────────────────────────────────────────────┤
│ Dynamic           │ Real-time membership updates                       │
│                   │ "Users die vorige week kochten"                    │
├───────────────────┼────────────────────────────────────────────────────┤
│ Sequential        │ Ordered steps (THEN/FOLLOWED BY)                   │
│                   │ "Viewed product → Added to cart → Did NOT buy"     │
├───────────────────┼────────────────────────────────────────────────────┤
│ Exclusion         │ Exclude bepaalde users                             │
│                   │ "All visitors EXCEPT converters"                   │
├───────────────────┼────────────────────────────────────────────────────┤
│ Predictive        │ ML-gebaseerd (purchase/churn probability)          │
│                   │ "Likely 7-day purchasers"                          │
└───────────────────┴────────────────────────────────────────────────────┘
```

## Audience Aanmaken: Stap voor Stap

### Stap 1: Naar Audience Builder

```
LOCATIE: Admin → Property → Audiences → New audience

OPTIES BIJ CREATIE:
┌────────────────────────┬────────────────────────────────────────────┐
│ Optie                  │ Wanneer Gebruiken                          │
├────────────────────────┼────────────────────────────────────────────┤
│ Create a custom        │ Volledige controle, eigen condities        │
│ audience               │ (Aanbevolen voor specifieke use cases)     │
├────────────────────────┼────────────────────────────────────────────┤
│ Use a reference        │ Start met GA4 template                     │
│ (Suggested audiences)  │ (Goed voor inspiratie)                     │
├────────────────────────┼────────────────────────────────────────────┤
│ Create audience from   │ Start vanuit bestaande Exploration         │
│ exploration            │ (Handig voor analyse → actie)              │
└────────────────────────┴────────────────────────────────────────────┘
```

### Stap 2: Condities Configureren

```
AUDIENCE CONDITIONS
===================

CONDITION TYPES:
────────────────
├── Include users when: (AND/OR logic)
│   ├── Event (event_name = X)
│   ├── Event parameter (event_param = Y)
│   ├── User property (user_property = Z)
│   ├── First user (acquisition source/medium)
│   └── Device/Geo (platform, country, city)
│
└── Exclude users when: (Filter OUT)
    └── Zelfde opties als include

OPERATORS BESCHIKBAAR:
┌─────────────────────┬────────────────────────────────────────────────┐
│ Operator            │ Voorbeeld                                      │
├─────────────────────┼────────────────────────────────────────────────┤
│ equals              │ event_name = purchase                          │
├─────────────────────┼────────────────────────────────────────────────┤
│ does not equal      │ page_location != /thank-you                    │
├─────────────────────┼────────────────────────────────────────────────┤
│ contains            │ page_title contains "Product"                  │
├─────────────────────┼────────────────────────────────────────────────┤
│ begins with         │ page_path begins with /shop/                   │
├─────────────────────┼────────────────────────────────────────────────┤
│ ends with           │ page_path ends with /checkout                  │
├─────────────────────┼────────────────────────────────────────────────┤
│ matches regex       │ page_path matches regex ^/product/[0-9]+$      │
├─────────────────────┼────────────────────────────────────────────────┤
│ > / < / >= / <=     │ ltv > 100 (voor numerieke waarden)             │
├─────────────────────┼────────────────────────────────────────────────┤
│ in list             │ country in list [NL, BE, DE]                   │
└─────────────────────┴────────────────────────────────────────────────┘
```

### Stap 3: Scoping Configureren

```
AUDIENCE SCOPING
================

WAT IS SCOPING:
├── Bepaalt op welk niveau condities worden geëvalueerd
├── Kritiek voor correcte audience definitie
└── Verkeerde scoping = verkeerde users in audience

SCOPE LEVELS:
┌─────────────────┬────────────────────────────────────────────────────┐
│ Scope           │ Betekenis                                          │
├─────────────────┼────────────────────────────────────────────────────┤
│ Across all      │ Conditie ooit waar in membership window            │
│ sessions        │ "User deed dit ooit in afgelopen X dagen"          │
│                 │ └─► MEEST GEBRUIKTE scope                          │
├─────────────────┼────────────────────────────────────────────────────┤
│ Within same     │ Conditie waar binnen één sessie                    │
│ session         │ "User deed dit in dezelfde sessie"                 │
│                 │ └─► Voor session-specifieke journeys               │
├─────────────────┼────────────────────────────────────────────────────┤
│ Within same     │ Conditie waar binnen één event                     │
│ event           │ "Dit event had deze parameters"                    │
│                 │ └─► Voor specifieke event combinaties              │
└─────────────────┴────────────────────────────────────────────────────┘

VOORBEELD VERSCHIL:
───────────────────
"User viewed product AND added to cart"

Across all sessions:
└─► User die ooit product bekeek EN ooit iets toevoegde
    (Kan verschillende producten zijn!)

Within same session:
└─► User die in DEZELFDE sessie product bekeek én toevoegde
    (Meer relevant voor cart abandonment)

Within same event:
└─► Niet logisch voor dit voorbeeld (2 events)
```

### Stap 4: Membership Duration

```
MEMBERSHIP DURATION SETTINGS
============================

WAT IS HET:
├── Hoe lang blijft user in audience na laatste qualifying actie
├── Max 540 dagen (Google Ads limiet)
└── Kies gebaseerd op customer journey en campagne doel

AANBEVELINGEN PER USE CASE:
┌─────────────────────────┬────────────┬─────────────────────────────────┐
│ Use Case                │ Duration   │ Reden                           │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Cart abandonment        │ 7-14 dagen │ Korte koopintentie window       │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Product viewers         │ 14-30 dagen│ Medium interesse window         │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Recent customers        │ 30-90 dagen│ Cross-sell/upsell window        │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ All customers           │ 180-540 dgn│ Langere loyalty periode         │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Seasonal shoppers       │ 365 dagen  │ Seizoensgebonden heractivatie   │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ High-value customers    │ 540 dagen  │ Maximale retentie voor VIPs     │
└─────────────────────────┴────────────┴─────────────────────────────────┘

⚠️ BELANGRIJK:
├── Kortere duration = meer relevante targeting
├── Langere duration = grotere audience size
├── Google Ads heeft max 540 dagen
└── Kies op basis van gemiddelde sales cycle
```

## Sequentiële Audiences

```
SEQUENTIAL AUDIENCES
====================

WAT IS HET:
├── Audiences gebaseerd op volgorde van acties
├── Gebruik "is followed by" of "is indirectly followed by"
└── Perfect voor customer journey targeting

SYNTAX:
────────
Step 1: [First condition]
        │
        ├─► is followed by (direct volgende actie)
        │   └─► "Meteen daarna"
        │
        └─► is indirectly followed by (ergens later)
            └─► "Op enig moment daarna"
        │
Step 2: [Second condition]
        │
        ├─► (herhaal voor meer steps)
        │
Step N: [Final condition]

VOORBEELD: CART ABANDONERS (SEQUENTIEEL)
────────────────────────────────────────
Step 1: event_name = view_item
        is indirectly followed by
Step 2: event_name = add_to_cart
        AND EXCLUDE
Step 3: event_name = purchase

Betekenis: "Users die product bekeken, daarna toevoegden aan cart,
           maar NIET kochten"

VOORBEELD: CHECKOUT ABANDONERS
──────────────────────────────
Step 1: event_name = begin_checkout
        is indirectly followed by
Step 2: event_name = add_payment_info
        AND EXCLUDE
Step 3: event_name = purchase

Betekenis: "Users die checkout startten, payment info invoerden,
           maar niet afrondden"

TIME CONSTRAINTS:
────────────────
├── "within X time" - Step moet binnen X tijd volgen
│   └─► Voorbeeld: add_to_cart within 30 minutes of view_item
│
└── Zonder constraint - Anytime in membership window
```

## Praktische Audience Templates

```
AUDIENCE TEMPLATES VOOR ADVERTEERDERS
=====================================

1. HIGH-INTENT NON-CONVERTERS
────────────────────────────
Naam: "High Intent - No Purchase"
Condities:
├── Include: event_name = add_to_cart (count >= 2)
├── Include: session_duration > 180 (3+ minuten)
└── Exclude: event_name = purchase
Duration: 14 dagen
Use case: Hoge koopintentie, needs extra push

2. RECENT CUSTOMERS (CROSS-SELL)
────────────────────────────────
Naam: "Recent Buyers - 30 Days"
Condities:
├── Include: event_name = purchase
└── Timeframe: Last 30 days
Duration: 30 dagen
Use case: Cross-sell campagnes

3. HIGH-VALUE CUSTOMERS
───────────────────────
Naam: "VIP Customers LTV 500+"
Condities:
├── Include: LTV (user property) > 500
└── Of: purchase value sum > 500
Duration: 540 dagen
Use case: VIP behandeling, loyalty campaigns

4. ENGAGED NON-CONVERTERS
─────────────────────────
Naam: "Engaged Visitors - No Purchase"
Condities:
├── Include: session_count >= 3
├── Include: page_views >= 10
└── Exclude: event_name = purchase
Duration: 30 dagen
Use case: Retargeting engaged browsers

5. CATEGORY INTEREST
────────────────────
Naam: "[Category] Viewers"
Condities:
├── Include: page_path contains /category/[name]/
├── Of: item_category = [name]
└── Exclude: event_name = purchase (optioneel)
Duration: 14 dagen
Use case: Category-specifieke remarketing

6. LAPSED CUSTOMERS
───────────────────
Naam: "Lapsed Customers 90+ Days"
Condities:
├── Include: event_name = purchase
├── Timeframe: 90-365 days ago (NOT last 90 days)
└── Exclude: purchase in last 90 days
Duration: 275 dagen
Use case: Win-back campagnes

7. EMAIL SUBSCRIBERS NON-BUYERS
───────────────────────────────
Naam: "Newsletter - No Purchase"
Condities:
├── Include: event_name = sign_up OR newsletter_subscribe
└── Exclude: event_name = purchase
Duration: 90 dagen
Use case: Email subscriber conversie
```

## Best Practices

```
DO's ✅
═══════
├── Gebruik duidelijke, beschrijvende audience namen
│   └─► "Cart_Abandon_14d_ExclPurchase" vs "Audience 1"
│
├── Documenteer audience logica in description
│   └─► Voeg uitleg toe waarom deze condities
│
├── Start met bredere audiences, narrow down later
│   └─► Te specifiek = te weinig users
│
├── Test audience size voor activatie
│   └─► <1000 users = mogelijk te klein voor Google Ads
│
├── Gebruik exclusions om overlap te voorkomen
│   └─► Exclude converters uit prospecting audiences
│
├── Combineer met Predictive Audiences
│   └─► "Likely Purchasers" + "Cart Abandoners" = High priority
│
└── Review audiences maandelijks
    └─► Verwijder inactieve/kleine audiences

DON'Ts ❌
════════
├── Te veel audiences maken (>50 wordt onoverzichtelijk)
│   └─► Focus op 10-20 core audiences
│
├── Audiences maken zonder duidelijk campagne doel
│   └─► Eerst: wat wil ik bereiken? Dan: welke audience?
│
├── Vergeten om exclusions toe te voegen
│   └─► Converters re-targeten met prospecting ads
│
├── Te korte membership duration voor lange sales cycles
│   └─► B2B: 30-90 dagen, niet 7 dagen
│
├── Alleen op één datapunt bouwen
│   └─► Combineer meerdere signals voor betere targeting
│
└── Audiences nooit reviewen op performance
    └─► Slechte ROAS? Audience aanpassen of pauzeren
```

## Troubleshooting

```
TROUBLESHOOTING GUIDE
=====================

PROBLEEM: Audience size = 0
───────────────────────────
Oorzaken:
├── Condities te restrictief
├── Event bestaat niet of is verkeerd gespeld
├── Timeframe te kort
├── Data nog niet geprocessed
└── Verkeerde scoping

Oplossing:
├── Check event/parameter namen in DebugView
├── Verbreed condities (minder AND, meer OR)
├── Wacht 24-48 uur voor data processing
├── Gebruik Exploration om users eerst te tellen
└── Test elke conditie apart

PROBLEEM: Audience niet beschikbaar in Google Ads
─────────────────────────────────────────────────
Oorzaken:
├── Google Ads link niet actief
├── "Enable personalized ads" niet aan
├── Audience te klein (<1000 users)
├── Nog niet gesynchroniseerd (24-48 uur)
└── Policy violation (gevoelige categorieën)

Oplossing:
├── Check Admin → Product Links → Google Ads
├── Verify "Personalized advertising" toggle
├── Wacht op voldoende audience volume
├── Check Google Ads policy compliance
└── Controleer of Google Signals aan staat

PROBLEEM: Audience groeit niet
──────────────────────────────
Oorzaken:
├── Events worden niet getriggerd
├── Filters te restrictief
├── Consent mode blokkeert users
└── Membership duration te kort

Oplossing:
├── Verify event tracking in DebugView
├── Review en verbreed condities
├── Check consent rates
├── Verleng membership duration

PROBLEEM: Te veel overlap tussen audiences
──────────────────────────────────────────
Oorzaken:
├── Geen exclusions geconfigureerd
├── Condities niet mutual exclusive
└── Audience hierarchy niet doordacht

Oplossing:
├── Maak exclusion audiences
├── Gebruik "AND NOT" condities
├── Ontwerp audience architectuur met niveaus
└── Prioriteer: converters → high-intent → general
```

## Output: Audience Builder Recommendation Template

```markdown
# GA4 Audience Recommendation

## Audience Overzicht
- **Naam:** [Audience naam]
- **Doel:** [Remarketing/Analyse/Export]
- **Verwachte grootte:** [Schatting]
- **Membership duration:** [X dagen]

## Audience Configuratie

### Include Condities
| # | Type | Conditie | Scope |
|---|------|----------|-------|
| 1 | Event | [event_name = X] | [Across all sessions] |
| 2 | Parameter | [param = Y] | [Within same event] |
| 3 | User Property | [property = Z] | [Across all sessions] |

### Exclude Condities
| # | Type | Conditie | Reden |
|---|------|----------|-------|
| 1 | Event | [event_name = purchase] | Exclude converters |

### Sequentiële Steps (indien van toepassing)
```
Step 1: [Eerste actie]
        │ is indirectly followed by
Step 2: [Tweede actie]
        │ AND EXCLUDE
Step 3: [Te excluden actie]
```

## Export Configuratie
- **Google Ads:** [Ja/Nee]
- **Display & Video 360:** [Ja/Nee]
- **Search Ads 360:** [Ja/Nee]

## Campaign Use Cases
1. [Eerste campagne type - beschrijving]
2. [Tweede campagne type - beschrijving]
3. [Derde campagne type - beschrijving]

## Monitoring
- **Review frequentie:** [Wekelijks/Maandelijks]
- **KPIs:** [Audience size, Conversion rate, ROAS]
- **Alerts:** [Als size <X of >Y]

## Notities
[Eventuele aanvullende opmerkingen of context]
```

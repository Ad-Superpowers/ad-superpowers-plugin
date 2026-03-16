---
name: ga4-audience-exclusions
description: "GA4 audience exclusions en frequency management. Gebruik voor: (1) Converters excluderen uit prospecting, (2) Recent purchasers uitsluiten, (3) Frequency capping strategieën, (4) Audience overlap voorkomen, (5) Budget efficiency maximaliseren. Triggers: audience exclusion, exclude converters, frequency cap, uitsluiten, overlap voorkomen, audience management, budget optimalisatie."
---

# GA4 Audience Exclusions Guide

Complete gids voor het effectief excluderen van audiences en frequency capping om advertising budget te maximaliseren.

## Quick Decision Tree

```
GA4 AUDIENCE EXCLUSIONS FLOW
│
├─► WAAROM EXCLUDEREN?
│   ├─► Geen geld verspillen aan reeds-geconverteerden
│   │   └─► Exclude: Recent purchasers, completed leads
│   │
│   ├─► Audience overlap voorkomen
│   │   └─► Zelfde user niet in meerdere campaigns
│   │
│   ├─► Negatieve ervaringen voorkomen
│   │   └─► Exclude: Refunders, complainers, bounced
│   │
│   └─► Frequency management
│       └─► Soft exclusions via capping
│
├─► WELKE EXCLUSION STRATEGIE?
│   ├─► Hard exclusion (nooit tonen)
│   │   └─► Recent converters, existing customers
│   │
│   ├─► Timed exclusion (X dagen na event)
│   │   └─► Cross-sell timing, replenishment cycles
│   │
│   └─► Conditional exclusion
│       └─► Alleen excluderen in specifieke campaigns
│
└─► WAAR IMPLEMENTEREN?
    ├─► GA4 Audience level
    │   └─► "Exclude users when..." conditie
    │
    ├─► Google Ads Campaign level
    │   └─► Audience exclusions per campaign
    │
    └─► Google Ads Ad Group level
        └─► Granulaire exclusions
```

## Exclusion Types Overzicht

```
EXCLUSION STRATEGIEËN
=====================

┌─────────────────────┬────────────────────────────────────────────────────┐
│ Type                │ Beschrijving                                       │
├─────────────────────┼────────────────────────────────────────────────────┤
│ GA4 Built-in        │ "Exclude users when" in audience builder           │
│ Exclusion           │ Maakt audience al gefilterd                        │
│                     │ └─► Beste voor: Remarketing audiences              │
├─────────────────────┼────────────────────────────────────────────────────┤
│ Google Ads          │ Separate exclusion audience toegevoegd aan         │
│ Campaign Exclusion  │ campaign settings                                  │
│                     │ └─► Beste voor: Prospecting campaigns              │
├─────────────────────┼────────────────────────────────────────────────────┤
│ Negative Audience   │ "Do not show ads to this audience"                 │
│ Targeting           │ Campagne-level of account-level                    │
│                     │ └─► Beste voor: Account-wide exclusions            │
├─────────────────────┼────────────────────────────────────────────────────┤
│ Frequency Capping   │ Soft exclusion via impression limits               │
│                     │ User ziet max X ads per dag/week                   │
│                     │ └─► Beste voor: Display/YouTube                    │
└─────────────────────┴────────────────────────────────────────────────────┘
```

## Core Exclusion Audiences

```
ESSENTIËLE EXCLUSION AUDIENCES
==============================

1. RECENT PURCHASERS (MUST-HAVE)
────────────────────────────────
Naam: "Purchasers - Last 30 Days"
Conditie: event_name = purchase (in last 30 days)
Duration: 30 dagen

Waarom excluderen:
├── Voorkom waste op recent geconverteerden
├── Betere user experience (geen repetitieve ads)
└── Acquisition budget focussen op new customers

Excluderen VAN:
├── Alle acquisition campaigns
├── Prospecting campaigns
└── Generic remarketing

NIET excluderen van:
├── Cross-sell campaigns (andere producten)
├── Loyalty/VIP campaigns
└── Replenishment reminders (na X dagen)


2. ALL CONVERTERS (LIFETIME)
────────────────────────────
Naam: "All Purchasers - Lifetime"
Conditie: event_name = purchase (any time)
Duration: 540 dagen (maximum)

Waarom:
├── Acquisition efficiency (focus op new customers)
├── Separate campaigns voor bestaande vs nieuwe klanten
└── Different messaging/offers per segment

Excluderen VAN:
├── Pure acquisition campaigns
├── First-time buyer promos
└── New customer discounts


3. LEADS (RECENT SUBMITTERS)
────────────────────────────
Naam: "Leads - Last 14 Days"
Conditie: event_name = generate_lead OR form_submit
Duration: 14 dagen

Waarom:
├── Al in sales funnel
├── Nurturing via email, niet ads
└── Voorkom over-exposure

Excluderen VAN:
├── Lead generation campaigns
├── Demo request campaigns
└── Generic awareness


4. HIGH-VALUE CUSTOMERS (PROTECT)
─────────────────────────────────
Naam: "VIP Customers - LTV 500+"
Conditie: user_ltv > 500 OF purchase_count >= 5
Duration: 540 dagen

Waarom excluderen van sommige campaigns:
├── Deze klanten komen organisch terug
├── Geen discount ads nodig
├── Bescherm relationship

Excluderen VAN:
├── Discount campaigns
├── Win-back met grote kortingen
└── Aggressive retargeting


5. CART ABANDONERS (AL GETARGET)
────────────────────────────────
Naam: "Active Cart Abandoners - 14d"
Conditie: add_to_cart (last 14 days) EXCLUDE purchase
Duration: 14 dagen

Waarom excluderen:
├── Deze krijgen al cart abandonment emails/ads
├── Voorkom dubbele exposure
└── Budget efficiency

Excluderen VAN:
├── General product remarketing
├── Awareness campaigns
└── Top-of-funnel content


6. BOUNCED VISITORS (LOW VALUE)
───────────────────────────────
Naam: "Bouncers - Single Page"
Conditie: session_duration < 10s OF page_views = 1
Duration: 7 dagen

Waarom excluderen:
├── Lage intent, waarschijnlijk accidenteel verkeer
├── Voorkom waste op low-quality traffic
└── Betere overall ROAS

Excluderen VAN:
├── Remarketing campaigns
├── Consideration campaigns
└── High-intent targeting
```

## GA4 Exclusion Implementatie

### Methode 1: Built-in Audience Exclusions

```
GA4 AUDIENCE BUILDER EXCLUSIONS
===============================

LOCATIE: Admin → Audiences → New audience

SETUP:
──────
1. Bouw je "Include" condities eerst
   ├── Bijv: event add_to_cart (last 7 days)

2. Klik "Add new condition group"

3. Toggle naar "Exclude users when"
   ├── Bijv: event purchase (last 7 days)

4. Resultaat: Cart abandoners ZONDER converters

VOORBEELD: CART ABANDONERS EXCL PURCHASE
────────────────────────────────────────
Include users when:
├── Event: add_to_cart
├── In last: 7 days

Exclude users when:
├── Event: purchase
├── In last: 7 days

Duration: 7 dagen

VOORBEELD: ENGAGED VISITORS EXCL CONVERTERS
───────────────────────────────────────────
Include users when:
├── session_duration > 120
├── AND page_views >= 3

Exclude users when:
├── Event: purchase
├── OR Event: generate_lead

Duration: 14 dagen
```

### Methode 2: Dedicated Exclusion Audiences

```
STANDALONE EXCLUSION AUDIENCES
==============================

WAAROM APARTE AUDIENCES:
├── Herbruikbaar across campaigns
├── Makkelijker te managen centraal
├── Consistent access in Google Ads
└── Flexibeler voor verschillende exclusion windows

EXCLUSION AUDIENCE NAMING CONVENTION:
────────────────────────────────────
[Segment]_Exclude_[Timeframe]

Voorbeelden:
├── Purchasers_Exclude_30d
├── Leads_Exclude_14d
├── VIP_Exclude_Discounts
├── Bouncers_Exclude_7d
└── Complainers_Exclude_90d

SETUP IN GA4:
────────────
1. Maak audience met ALLEEN de te-excluderen conditie
2. Geef duidelijke naam (Exclude prefix)
3. Export naar Google Ads
4. Voeg toe als exclusion in campaigns

VOORBEELD AUDIENCES MAKEN:
──────────────────────────
Audience 1: "Purchasers_Exclude_30d"
├── Include: event purchase (last 30 days)
├── Duration: 30 dagen
└── Export: Google Ads

Audience 2: "Purchasers_Exclude_7d"
├── Include: event purchase (last 7 days)
├── Duration: 7 dagen
└── Export: Google Ads

Audience 3: "All_Converters_Lifetime"
├── Include: event purchase (any time)
├── Duration: 540 dagen
└── Export: Google Ads
```

## Google Ads Exclusion Implementatie

```
GOOGLE ADS EXCLUSION SETUP
==========================

CAMPAIGN-LEVEL EXCLUSIONS:
─────────────────────────
1. Ga naar Campaign → Settings → Audiences
2. Scroll naar "Audience exclusions"
3. Click "Edit audience exclusions"
4. Browse → Your data → Website visitors (GA4)
5. Selecteer exclusion audiences
6. Save

AD GROUP-LEVEL EXCLUSIONS:
─────────────────────────
1. Ga naar Ad Group → Audiences
2. Click "Exclusions" tab
3. "+ Add exclusion"
4. Selecteer GA4 audiences
5. Save

ACCOUNT-LEVEL EXCLUSIONS:
────────────────────────
Voor exclusions die OVERAL gelden:

1. Tools & Settings → Shared Library → Audience Manager
2. Audience lists → Create exclusion list
3. Voeg GA4 audiences toe aan list
4. Apply list to campaigns

WHEN TO USE EACH LEVEL:
┌─────────────────┬────────────────────────────────────────────────────────┐
│ Level           │ When to Use                                            │
├─────────────────┼────────────────────────────────────────────────────────┤
│ Account-level   │ Universal exclusions (all converters from acquisition) │
├─────────────────┼────────────────────────────────────────────────────────┤
│ Campaign-level  │ Campaign-specific logic                                │
│                 │ (exclude cart abandoners from awareness)               │
├─────────────────┼────────────────────────────────────────────────────────┤
│ Ad Group-level  │ Granular product/category exclusions                   │
│                 │ (exclude category X buyers from category X ads)        │
└─────────────────┴────────────────────────────────────────────────────────┘
```

## Frequency Capping Strategieën

```
FREQUENCY CAPPING GUIDE
=======================

WAT IS FREQUENCY CAPPING:
├── Limiet op hoe vaak user je ads ziet
├── Per dag, week, of maand
├── Alleen voor Display, Video, Discovery
└── NIET beschikbaar voor Search

WAAROM CAPPING:
├── Voorkom ad fatigue
├── Avoid negative brand perception
├── Betere overall ROI
├── Respecteer user experience

FREQUENCY CAP SETTINGS:
┌─────────────────────┬─────────────────┬─────────────────────────────────┐
│ Audience Type       │ Recommended Cap │ Rationale                       │
├─────────────────────┼─────────────────┼─────────────────────────────────┤
│ Cart abandoners     │ 5-7/dag         │ High intent, reminder nodig     │
│                     │ 15-20/week      │ Maar niet overkill              │
├─────────────────────┼─────────────────┼─────────────────────────────────┤
│ Product viewers     │ 3-5/dag         │ Medium intent                   │
│                     │ 10-15/week      │ Gentle consideration nudge      │
├─────────────────────┼─────────────────┼─────────────────────────────────┤
│ All visitors        │ 2-3/dag         │ Lower intent                    │
│                     │ 7-10/week       │ Brand presence, not pushy       │
├─────────────────────┼─────────────────┼─────────────────────────────────┤
│ YouTube remarketing │ 2-3/dag         │ Video is intrusive              │
│                     │ 5-7/week        │ Quality over quantity           │
├─────────────────────┼─────────────────┼─────────────────────────────────┤
│ Display prospecting │ 3-5/dag         │ New users need exposure         │
│                     │ 15-20/week      │ But not bombardment             │
└─────────────────────┴─────────────────┴─────────────────────────────────┘

FREQUENCY CAP SETUP (GOOGLE ADS):
────────────────────────────────
1. Campaign Settings → Additional settings
2. Frequency capping
3. Set: "Cap impressions at X per [day/week/month]"
4. Apply to: Campaign or Ad group

VIEWABLE FREQUENCY CAP:
──────────────────────
├── Cap op viewable impressions (50% pixels, 1+ second)
├── Betere metric dan total impressions
└── Available voor Display campaigns

SEQUENTIAL MESSAGING MET FREQUENCY:
──────────────────────────────────
Combineer frequency capping met sequential ads:

Day 1-2: Awareness creative (3x)
Day 3-5: Consideration creative (3x)
Day 6-7: Conversion creative (3x)

Setup via:
├── Aparte ad groups met eigen frequency caps
├── Exclude users na X days in each phase
└── Of: Campaign-level sequencing tools
```

## Audience Overlap Management

```
AUDIENCE OVERLAP VOORKOMEN
==========================

WAAROM OVERLAP PROBLEMATISCH:
├── Zelfde user ziet ads van meerdere campaigns
├── Budget competition met jezelf
├── Inconsistente messaging
├── Hoger dan nodig frequency
└── Moeilijk attributie analysis

OVERLAP DETECTIE (GOOGLE ADS):
─────────────────────────────
1. Tools → Shared Library → Audience Manager
2. Audience insights → Overlap
3. Bekijk welke audiences overlappen
4. Percentage overlap per audience pair

OVERLAP OPLOSSINGEN:

METHODE 1: HIERARCHISCHE EXCLUSIONS
───────────────────────────────────
Prioriteer audiences en exclude de hogere uit lagere:

Prioriteit 1: Converters
├── Geen exclusions nodig

Prioriteit 2: Cart abandoners
├── Exclude: Converters

Prioriteit 3: Product viewers
├── Exclude: Converters
├── Exclude: Cart abandoners

Prioriteit 4: All visitors
├── Exclude: Converters
├── Exclude: Cart abandoners
├── Exclude: Product viewers

METHODE 2: MUTUALLY EXCLUSIVE AUDIENCES
──────────────────────────────────────
Bouw audiences die per definitie niet overlappen:

Audience A: "Purchasers only"
├── purchase = true

Audience B: "Cart abandon, no purchase"
├── add_to_cart = true
├── EXCLUDE: purchase = true

Audience C: "Product view only"
├── view_item = true
├── EXCLUDE: add_to_cart = true
├── EXCLUDE: purchase = true

METHODE 3: CAMPAIGN STRUCTURE
────────────────────────────
Aparte campaigns per funnel stage:

Campaign 1: "Acquisition" (new users)
├── Target: Similar audiences
├── Exclude: All site visitors

Campaign 2: "Consideration" (browsers)
├── Target: All visitors
├── Exclude: Cart abandoners + Converters

Campaign 3: "Conversion" (high intent)
├── Target: Cart abandoners
├── Exclude: Converters

Campaign 4: "Retention" (customers)
├── Target: All converters
├── Exclude: Recent converters (7d)
```

## Timing-Based Exclusions

```
TIMED EXCLUSION STRATEGIEËN
===========================

WAAROM TIMED EXCLUSIONS:
├── Cross-sell na juiste periode
├── Replenishment herinneringen
├── Seasonal re-engagement
└── Voorkomen over-targeting na conversie

EXCLUSION WINDOWS PER USE CASE:
┌─────────────────────────┬───────────────┬─────────────────────────────────┐
│ Use Case                │ Exclude For   │ Then Include In                 │
├─────────────────────────┼───────────────┼─────────────────────────────────┤
│ Recent purchase         │ 7-14 dagen    │ Cross-sell campaigns            │
│ (post-purchase glow)    │               │                                 │
├─────────────────────────┼───────────────┼─────────────────────────────────┤
│ Subscription/membership │ Billing cycle │ Renewal reminders               │
│                         │ (30-60 dagen) │                                 │
├─────────────────────────┼───────────────┼─────────────────────────────────┤
│ High-ticket items       │ 30-90 dagen   │ Accessory/service campaigns     │
│                         │               │                                 │
├─────────────────────────┼───────────────┼─────────────────────────────────┤
│ Consumables             │ Avg usage     │ Replenishment campaigns         │
│ (skincare, vitamins)    │ (30-60 dagen) │                                 │
├─────────────────────────┼───────────────┼─────────────────────────────────┤
│ Seasonal products       │ 330-365 dagen │ Next season campaigns           │
│                         │               │                                 │
└─────────────────────────┴───────────────┴─────────────────────────────────┘

IMPLEMENTATIE VOORBEELD:
───────────────────────

"Recent Buyers - Exclude 14d, Include After"

Audience 1: "Purchasers_Exclude_14d" (voor exclusion)
├── purchase (last 14 days)
├── Duration: 14 dagen
└── Gebruik als exclusion

Audience 2: "Purchasers_14d_to_90d" (voor targeting)
├── purchase (last 90 days)
├── EXCLUDE: purchase (last 14 days)
├── Duration: 90 dagen
└── Gebruik voor cross-sell targeting
```

## Best Practices

```
DO's ✅
═══════
├── Start met core exclusions (purchasers, leads)
│   └─► Dit alleen al verbetert ROAS significant
│
├── Gebruik hiërarchische exclusions
│   └─► Voorkomt overlap en budget waste
│
├── Naming convention aanhouden
│   └─► [Segment]_Exclude_[Timeframe] format
│
├── Review exclusion lists maandelijks
│   └─► Business changes vereisen updates
│
├── Combineer frequency caps met exclusions
│   └─► Belt-and-suspenders approach
│
├── Test exclusion impact
│   └─► Vergelijk ROAS before/after
│
└── Document je exclusion strategie
    └─► Voorkomt verwarring in team

DON'Ts ❌
════════
├── Alle converters voor altijd excluderen
│   └─► Cross-sell en retention opportunities missen
│
├── Te agressief excluderen
│   └─► Kan reach te veel beperken
│
├── Vergeten om exclusion audiences te exporteren
│   └─► GA4 → Google Ads export nodig
│
├── Alleen op GA4 level excluderen
│   └─► Google Ads campaign exclusions ook nodig
│
├── Frequency cap op 1/dag zetten
│   └─► Te laag voor effectieve remarketing
│
└── Exclusions nooit reviewen
    └─► Outdated exclusions kosten opportunities
```

## Troubleshooting

```
TROUBLESHOOTING GUIDE
=====================

PROBLEEM: Exclusion audience niet werkend in Google Ads
───────────────────────────────────────────────────────
Oorzaken:
├── Audience niet geëxporteerd naar Google Ads
├── Verkeerde audience geselecteerd als exclusion
├── Campaign-level vs ad group-level confusion
├── Audience te klein (<100 voor Display)
└── Sync delay (tot 48 uur)

Oplossing:
├── Check GA4: Audience destinations → Google Ads ✅
├── Verify Google Ads: Audience Manager → list exists
├── Confirm exclusion applied at correct level
├── Wacht tot audience voldoende users heeft
└── Test met broader exclusion audience

PROBLEEM: Users zien nog steeds ads na conversie
────────────────────────────────────────────────
Oorzaken:
├── Exclusion audience membership duration te kort
├── Cross-device: user converteerde op ander device
├── Consent mode: conversie niet getrackt
├── Exclusion alleen in sommige campaigns
└── Google Ads sync delay

Oplossing:
├── Extend exclusion duration (min. 7-14 dagen)
├── Enable Google Signals voor cross-device
├── Verify conversion tracking werkt
├── Apply exclusion account-wide
├── Check Audience Manager voor sync status

PROBLEEM: Te weinig reach na exclusions
───────────────────────────────────────
Oorzaken:
├── Te veel exclusions toegepast
├── Exclusion audiences te groot
├── Kleine website = kleine audiences
└── Overlappende exclusions

Oplossing:
├── Review en consolideer exclusions
├── Shorten exclusion timeframes
├── Gebruik timed exclusions ipv permanent
├── Focus op most impactful exclusions only

PROBLEEM: Frequency hoger dan cap setting
─────────────────────────────────────────
Oorzaken:
├── Meerdere campaigns targeting zelfde user
├── Cap geldt per campaign, niet account
├── Cross-device niet gematched
├── Display Network vs andere networks
└── Reporting delay

Oplossing:
├── Implement account-level exclusions
├── Coordinate caps across campaigns
├── Enable Google Signals
├── Set caps op ALL campaigns, niet selectief

PROBLEEM: Exclusion conflicts met Smart Bidding
───────────────────────────────────────────────
Oorzaken:
├── Smart Bidding wil excludeerde users targeten
├── Te strikte exclusions beperken learning
├── Audience signals vs audience targeting
└── Algorithm fights your exclusions

Oplossing:
├── Smart Bidding respecteert exclusions
├── Maar: te veel exclusions = minder learning data
├── Balance: exclude obvious waste, maar niet te agressief
├── Monitor algorithm performance metrics
└── Adjust exclusions based on Smart Bidding feedback
```

## Output: Audience Exclusion Strategy Template

```markdown
# GA4 Audience Exclusion Strategie

## Exclusion Audiences Overzicht

### Core Exclusions (Must-Have)
| Audience Naam | Conditie | Duration | Export Status |
|---------------|----------|----------|---------------|
| Purchasers_Exclude_30d | purchase (30d) | 30 dagen | [✅/❌] |
| Purchasers_Exclude_7d | purchase (7d) | 7 dagen | [✅/❌] |
| All_Converters_Lifetime | purchase (all) | 540 dagen | [✅/❌] |
| Leads_Exclude_14d | generate_lead (14d) | 14 dagen | [✅/❌] |

### Secondary Exclusions
| Audience Naam | Conditie | Duration | Use Case |
|---------------|----------|----------|----------|
| [Naam] | [Conditie] | [X dagen] | [Use case] |
| [Naam] | [Conditie] | [X dagen] | [Use case] |

## Campaign Exclusion Matrix

| Campaign Type | Exclusions Applied |
|---------------|-------------------|
| Acquisition/Prospecting | All_Converters_Lifetime, Cart_Abandoners_14d |
| Consideration/Remarketing | Purchasers_Exclude_7d |
| Cart Recovery | Purchasers_Exclude_7d |
| Cross-sell | Purchasers_Exclude_7d (include older purchasers) |
| Retention/Loyalty | Non-purchasers excluded |

## Frequency Capping Strategy

| Audience | Daily Cap | Weekly Cap | Rationale |
|----------|-----------|------------|-----------|
| Cart abandoners | [X] | [X] | [Reden] |
| Product viewers | [X] | [X] | [Reden] |
| All visitors | [X] | [X] | [Reden] |
| YouTube remarketing | [X] | [X] | [Reden] |

## Overlap Prevention

### Audience Hierarchy
```
1. Converters (highest priority)
   └─ No exclusions
2. Cart Abandoners
   └─ Exclude: Converters
3. Product Viewers
   └─ Exclude: Converters, Cart Abandoners
4. Engaged Visitors
   └─ Exclude: All above
5. All Visitors
   └─ Exclude: All above
```

## Timed Exclusion Schedule

| Segment | Exclude For | Then Target With |
|---------|-------------|------------------|
| Recent purchasers | [X dagen] | [Campaign type] |
| [Segment] | [X dagen] | [Campaign type] |

## Implementation Checklist

### GA4
- [ ] Core exclusion audiences aangemaakt
- [ ] Alle audiences geëxporteerd naar Google Ads
- [ ] Naming convention consistent

### Google Ads
- [ ] Campaign-level exclusions toegepast
- [ ] Account-level exclusion list gemaakt
- [ ] Frequency caps ingesteld
- [ ] Exclusion audiences verified in Audience Manager

## Monitoring

- **Review frequentie:** [Wekelijks/Maandelijks]
- **Key metrics:** Overlap %, Reach impact, ROAS change
- **Alerts:** [Wanneer actie nodig]

## Notities
[Specifieke overwegingen of context]
```

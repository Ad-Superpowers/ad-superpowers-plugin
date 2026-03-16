---
name: ga4-predictive-audiences
description: "GA4 predictive audiences met machine learning. Gebruik voor: (1) Likely purchasers identificeren (7-day purchase probability), (2) Churn prediction en at-risk customers, (3) Predicted revenue segmentatie, (4) ML-audiences activeren voor Smart Bidding, (5) Predictive metrics begrijpen en troubleshooten. Triggers: predictive audience, purchase probability, churn prediction, likely buyers, at-risk customers, ml audience, predicted revenue, machine learning audience."
---

# GA4 Predictive Audiences Guide

Complete gids voor het gebruiken van GA4's machine learning predictive audiences voor geavanceerde remarketing en Smart Bidding optimalisatie.

## Quick Decision Tree

```
GA4 PREDICTIVE AUDIENCES FLOW
│
├─► WELKE PREDICTIVE METRIC?
│   ├─► Purchase probability
│   │   └─► "Likely 7-day purchasers"
│   │   └─► Use: acquisition, conversion campaigns
│   │
│   ├─► Churn probability
│   │   └─► "Likely 7-day churners"
│   │   └─► Use: retention, win-back campaigns
│   │
│   └─► Predicted revenue
│       └─► "High predicted revenue (28d)"
│       └─► Use: VIP targeting, value-based bidding
│
├─► ELIGIBLE VOOR PREDICTIVE?
│   ├─► Ja (voldoende data)
│   │   └─► Ga verder met setup
│   │
│   └─► Nee (niet genoeg data)
│       └─► Verbeter tracking eerst
│       └─► Zie "Eligibility Requirements"
│
└─► HOE ACTIVEREN?
    ├─► Direct in GA4 audience builder
    │   └─► Gebruik predictive metrics als conditie
    │
    └─► Export naar Google Ads
        └─► Voor Smart Bidding optimization
        └─► Zie: ga4-remarketing-setup skill
```

## Predictive Metrics Overzicht

```
GA4 PREDICTIVE METRICS
======================

┌──────────────────────┬──────────────────────────────────────────────────┐
│ Metric               │ Beschrijving                                     │
├──────────────────────┼──────────────────────────────────────────────────┤
│ Purchase probability │ Kans dat actieve user in komende 7 dagen koopt   │
│                      │ Range: 0-100%                                    │
│                      │ Update: dagelijks                                │
├──────────────────────┼──────────────────────────────────────────────────┤
│ Churn probability    │ Kans dat actieve user in komende 7 dagen churnt  │
│                      │ (geen activiteit meer)                           │
│                      │ Range: 0-100%                                    │
├──────────────────────┼──────────────────────────────────────────────────┤
│ Predicted revenue    │ Verwachte omzet van user in komende 28 dagen     │
│                      │ Gebaseerd op historisch gedrag                   │
│                      │ In property currency                             │
└──────────────────────┴──────────────────────────────────────────────────┘

HOE WERKT HET:
─────────────
├── Google's ML modellen analyseren user behavior
├── Getraind op jouw property data
├── Vereist minimum data volume om te werken
├── Updates dagelijks voor alle eligible users
└── Geen extra implementatie nodig (als purchase event correct is)
```

## Eligibility Requirements

```
VEREISTEN VOOR PREDICTIVE AUDIENCES
===================================

⚠️ KRITIEKE VEREISTEN - Alle moeten voldaan zijn:

1. PURCHASE EVENTS
──────────────────
┌────────────────────────────────────────────────────────────────────────┐
│ Vereiste: Minimum 1.000 kopers EN 1.000 niet-kopers in 7 dagen        │
│                                                                        │
│ Dit betekent:                                                          │
│ ├── Actief e-commerce tracking met purchase event                     │
│ ├── Voldoende verkeer (typisch >10.000 users/week)                    │
│ ├── Purchase event moet correct geconfigureerd zijn                   │
│ └── Consistent data over tijd (geen gaps)                             │
└────────────────────────────────────────────────────────────────────────┘

2. CHURN PREDICTIONS
────────────────────
┌────────────────────────────────────────────────────────────────────────┐
│ Vereiste: Minimum 1.000 churners EN 1.000 actieve users in 7 dagen    │
│                                                                        │
│ Dit betekent:                                                          │
│ ├── Voldoende returning users                                         │
│ ├── Clear churn definition (7 dagen geen activiteit)                  │
│ └── Consistent engagement tracking                                    │
└────────────────────────────────────────────────────────────────────────┘

3. GENERAL REQUIREMENTS
───────────────────────
┌─────────────────────────┬──────────────────────────────────────────────┐
│ Requirement             │ Details                                      │
├─────────────────────────┼──────────────────────────────────────────────┤
│ Model quality           │ Voldoende predictive power                   │
│                         │ Google evalueert automatisch                 │
├─────────────────────────┼──────────────────────────────────────────────┤
│ Sustained data          │ Consistent volume over 28+ dagen             │
│                         │ Geen grote gaps in data                      │
├─────────────────────────┼──────────────────────────────────────────────┤
│ Purchase event params   │ Correct value en currency parameters         │
│                         │ Transactie ID voor deduplicatie              │
├─────────────────────────┼──────────────────────────────────────────────┤
│ User identification     │ Consistent user_id of client_id              │
│                         │ Cross-device tracking helpt                  │
└─────────────────────────┴──────────────────────────────────────────────┘

ELIGIBILITY CHECKEN:
────────────────────
Locatie: Admin → Audiences → New audience → Predictive
├── Groen vinkje = Eligible
├── Geel waarschuwing = Bijna eligible
└── Grijs = Niet eligible (hover voor reden)
```

## Predictive Audiences Aanmaken

### Stap 1: Eligibility Verifiëren

```
ELIGIBILITY CHECK
=================

LOCATIE: Admin → Audiences → New audience → Predictive

WAT JE ZIET:
┌──────────────────────────────────────────────────────────────────────┐
│ Predictive audiences                                                 │
│                                                                      │
│ ✅ Likely 7-day purchasers                    [Create audience]     │
│    Users with >X% probability to purchase                           │
│                                                                      │
│ ✅ Likely 7-day churners                      [Create audience]     │
│    Users with >X% probability to churn                              │
│                                                                      │
│ ⚠️ Predicted revenue                          [Not yet available]   │
│    Need more purchase data with value                               │
└──────────────────────────────────────────────────────────────────────┘

NIET ELIGIBLE? CHECK:
────────────────────
├── Reports → Monetization → Ecommerce purchases
│   └─► Zijn er purchase events?
│
├── Admin → Events → purchase event parameters
│   └─► Heeft purchase een value parameter?
│
├── Realtime report → Events
│   └─► Worden purchases getrackt?
│
└── Explore → Free form → Users met purchase
    └─► Minimum 1.000 in afgelopen 28 dagen?
```

### Stap 2: Audience Configureren

```
PREDICTIVE AUDIENCE CONFIGURATIE
================================

OPTIE A: SUGGESTED PREDICTIVE AUDIENCES
───────────────────────────────────────
Google biedt kant-en-klare opties:

1. Likely 7-day purchasers
   ├── Users met hoge purchase probability
   ├── Automatisch threshold bepaald
   └── Ideaal voor conversie campaigns

2. Likely 7-day churners
   ├── Users met hoge churn probability
   ├── Nog recent actief, maar at-risk
   └── Ideaal voor retention campaigns

3. Predicted high spenders
   ├── Users met hoge predicted revenue
   ├── Gebaseerd op 28-day forecast
   └── Ideaal voor VIP targeting

OPTIE B: CUSTOM PREDICTIVE AUDIENCE
──────────────────────────────────
Combineer predictive metrics met andere condities:

Voorbeeld: "High-Value Likely Purchasers"
├── Include: Purchase probability > 70%
├── AND: LTV > €200
└── Duration: 7 dagen

Voorbeeld: "At-Risk VIP Customers"
├── Include: Churn probability > 50%
├── AND: Previous purchases >= 3
└── Duration: 14 dagen

Voorbeeld: "High Predicted Revenue + Cart Abandon"
├── Include: Predicted revenue > €100
├── AND: event add_to_cart (last 7 days)
├── Exclude: event purchase
└── Duration: 7 dagen
```

### Stap 3: Thresholds Instellen

```
PROBABILITY THRESHOLDS
======================

PURCHASE PROBABILITY TIERS:
┌─────────────────┬──────────────┬───────────────────────────────────────┐
│ Tier            │ Probability  │ Use Case                              │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Top tier        │ >90%         │ Bijna zekere kopers                   │
│                 │              │ └─► Minimale incentive nodig          │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ High            │ 70-90%       │ Waarschijnlijke kopers                │
│                 │              │ └─► Light push campaigns              │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Medium          │ 50-70%       │ Potentiële kopers                     │
│                 │              │ └─► Stronger incentives               │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Low-Medium      │ 30-50%       │ Need nurturing                        │
│                 │              │ └─► Awareness + consideration         │
└─────────────────┴──────────────┴───────────────────────────────────────┘

CHURN PROBABILITY TIERS:
┌─────────────────┬──────────────┬───────────────────────────────────────┐
│ Tier            │ Probability  │ Use Case                              │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ High risk       │ >80%         │ Bijna weg                             │
│                 │              │ └─► Aggressive win-back               │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Medium risk     │ 50-80%       │ At-risk                               │
│                 │              │ └─► Re-engagement campaigns           │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Low risk        │ <50%         │ Likely to stay                        │
│                 │              │ └─► Standard nurturing                │
└─────────────────┴──────────────┴───────────────────────────────────────┘

PREDICTED REVENUE TIERS:
┌─────────────────┬──────────────┬───────────────────────────────────────┐
│ Tier            │ Revenue      │ Use Case                              │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ High value      │ >€200        │ VIP treatment                         │
│                 │              │ └─► Premium ad spend                  │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Medium value    │ €50-200      │ Standard valuable                     │
│                 │              │ └─► Normal campaign inclusion         │
├─────────────────┼──────────────┼───────────────────────────────────────┤
│ Low value       │ <€50         │ Lower priority                        │
│                 │              │ └─► Efficiency focus                  │
└─────────────────┴──────────────┴───────────────────────────────────────┘
```

## Strategische Audience Combinaties

```
PREDICTIVE + BEHAVIORAL COMBINATIES
====================================

1. HIGH-VALUE CART ABANDONERS
─────────────────────────────
Condities:
├── Predicted revenue > €100
├── AND: event add_to_cart (last 3 days)
└── EXCLUDE: event purchase

Strategie: Premium retargeting, higher bids
ROAS verwachting: Hoog

2. LIKELY PURCHASERS + CATEGORY INTEREST
────────────────────────────────────────
Condities:
├── Purchase probability > 60%
├── AND: page_path contains /category/[naam]/

Strategie: Category-specifieke ads voor high-intent users
Use: Product-specifieke campaigns

3. AT-RISK LOYAL CUSTOMERS
──────────────────────────
Condities:
├── Churn probability > 60%
├── AND: total purchases >= 3
├── AND: LTV > €200

Strategie: VIP win-back met exclusive offers
Priority: Hoog (waardevol om te behouden)

4. LIKELY CHURNERS - RECENT BROWSERS
────────────────────────────────────
Condities:
├── Churn probability > 70%
├── AND: session (last 7 days)
└── EXCLUDE: purchase (last 30 days)

Strategie: Re-engagement met nieuwe producten
Timing: Snel handelen

5. HIGH PREDICTED REVENUE - NEW VISITORS
────────────────────────────────────────
Condities:
├── Predicted revenue > €150
├── AND: session_number = 1 of 2

Strategie: Fast-track naar conversie
Focus: Reduce friction, clear CTA

6. LOW PURCHASE PROB + HIGH ENGAGEMENT
──────────────────────────────────────
Condities:
├── Purchase probability < 30%
├── AND: session_duration > 300s
├── AND: page_views > 5

Strategie: Research phase - nurture content
Goal: Move up probability ladder
```

## Google Ads Integratie

```
PREDICTIVE AUDIENCES IN GOOGLE ADS
==================================

AUTOMATISCHE SYNC:
─────────────────
├── Eligible predictive audiences synchen automatisch
├── Vereist: Google Ads link + Personalized ads enabled
├── Sync tijd: 24-48 uur na audience creatie
└── Updates: Dagelijks (real-time probability updates)

SMART BIDDING OPTIMIZATION:
──────────────────────────
Predictive audiences zijn ideaal voor:

┌────────────────────────┬─────────────────────────────────────────────────┐
│ Bid Strategy           │ Hoe Predictive Helpt                            │
├────────────────────────┼─────────────────────────────────────────────────┤
│ Target ROAS            │ Focus budget op high predicted revenue users    │
│                        │ Bid hoger voor high purchase probability        │
├────────────────────────┼─────────────────────────────────────────────────┤
│ Target CPA             │ Optimaliseer naar users met hoge koop kans     │
│                        │ Vermijd spend op low probability                │
├────────────────────────┼─────────────────────────────────────────────────┤
│ Maximize Conversions   │ Prioriteer likely purchasers                    │
│                        │ Efficiëntere spend allocation                   │
├────────────────────────┼─────────────────────────────────────────────────┤
│ Value-Based Bidding    │ Predicted revenue als value signal              │
│                        │ Hogere bids voor hogere predicted value         │
└────────────────────────┴─────────────────────────────────────────────────┘

CAMPAIGN SETUP TIPS:
───────────────────
├── Maak aparte ad groups voor probability tiers
├── Pas creative messaging aan per tier
├── Monitor performance per probability segment
└── A/B test predictive vs. behavior-only targeting
```

## Best Practices

```
DO's ✅
═══════
├── Combineer predictive met behavioral signals
│   └─► "Likely purchasers" + "Cart abandoners" = Super high intent
│
├── Segment op probability tiers
│   └─► >70%, 50-70%, <50% behandelen als aparte audiences
│
├── Gebruik voor Smart Bidding optimization
│   └─► Target ROAS met predicted revenue signals
│
├── Monitor model quality over tijd
│   └─► Seasonal shifts kunnen model accuracy beïnvloeden
│
├── Start met Google's suggested audiences
│   └─► Daarna customizen met eigen condities
│
├── Combineer met exclusions
│   └─► "Likely purchasers" EXCLUDE "Recent purchasers"
│
└── Track ROAS per probability tier
    └─► Validate dat high probability = high ROAS

DON'Ts ❌
════════
├── Alleen vertrouwen op predictive
│   └─► Combineer met first-party data
│
├── Negeren dat je niet eligible bent
│   └─► Fix tracking eerst, dan predictive gebruiken
│
├── Verwachten dat predictive instant werkt
│   └─► Model heeft 28+ dagen data nodig
│
├── Alle users in één predictive audience
│   └─► Segment op tiers voor betere performance
│
├── Model blindly vertrouwen
│   └─► Validate met actual conversion data
│
└── Vergeten om audiences te refreshen
    └─► Predictive updates dagelijks, review performance
```

## Troubleshooting

```
TROUBLESHOOTING GUIDE
=====================

PROBLEEM: Predictive audiences niet eligible
────────────────────────────────────────────
Oorzaken:
├── Onvoldoende purchase events (<1000/week)
├── Purchase event mist value parameter
├── Inconsistente data (gaps in tracking)
├── Nieuw property (<28 dagen data)
└── Model quality te laag

Oplossing:
├── Check purchase event setup:
│   Admin → Events → purchase → Parameters
│   Moet bevatten: value, currency, transaction_id
│
├── Verify volume:
│   Explore → Users met purchase event → 28 dagen
│   Minimum 1.000 purchasers nodig
│
├── Fix tracking gaps:
│   Check voor missing days in real-time report
│   Implementeer consent mode correct
│
└── Wacht op voldoende data:
    28 dagen consistent volume nodig

PROBLEEM: Predictive audience size = 0
──────────────────────────────────────
Oorzaken:
├── Threshold te hoog (>95% probability)
├── Net eligible geworden, nog geen users gescoord
├── Combinatie met andere condities filtert iedereen uit
└── Audience net aangemaakt (24h processing)

Oplossing:
├── Verlaag probability threshold (test met >50%)
├── Wacht 24-48 uur na eligibility
├── Test predictive conditie los eerst
└── Check of standaard predictive audiences users hebben

PROBLEEM: Predictive audiences in Google Ads niet beschikbaar
────────────────────────────────────────────────────────────
Oorzaken:
├── Google Ads link niet actief
├── Personalized advertising niet enabled
├── Sync delay (tot 48 uur)
├── Audience te klein (<1000 users)
└── Policy violation

Oplossing:
├── Verify link: Admin → Product Links → Google Ads
├── Check toggle: Personalized advertising = ON
├── Wacht 48 uur na audience creatie
├── Controleer audience size in GA4
└── Review Google Ads policy compliance

PROBLEEM: Predictive performance lager dan verwacht
───────────────────────────────────────────────────
Oorzaken:
├── Model niet getraind op jouw specifieke business
├── Seasonal shifts beïnvloeden prediction accuracy
├── Targeting te breed of te smal
├── Creative mismatch met audience intent
└── Attribution window mismatch

Oplossing:
├── Compare predictive vs. actual conversions
├── Test verschillende probability thresholds
├── A/B test predictive targeting
├── Adjust bidding based on observed performance
└── Combine with retargeting signals

PROBLEEM: Model quality degradeert over tijd
────────────────────────────────────────────
Oorzaken:
├── Business changes (nieuwe producten/pricing)
├── Seasonal patterns niet in model
├── Tracking changes (consent mode updates)
├── User behavior shifts
└── Competition changes

Oplossing:
├── Model past zich automatisch aan (doorlopend)
├── Monitor prediction accuracy maandelijks
├── Vergelijk predicted vs actual conversies
├── Rapporteer grote shifts aan Google Support
└── Overweeg custom ML indien beschikbaar
```

## Output: Predictive Audience Recommendation Template

```markdown
# GA4 Predictive Audience Recommendation

## Eligibility Status
- **Purchase probability:** [✅ Eligible / ⚠️ Not yet / ❌ Not eligible]
- **Churn probability:** [✅ Eligible / ⚠️ Not yet / ❌ Not eligible]
- **Predicted revenue:** [✅ Eligible / ⚠️ Not yet / ❌ Not eligible]

## Eligibility Metrics
| Metric | Required | Current | Status |
|--------|----------|---------|--------|
| Weekly purchasers | >1,000 | [X] | [✅/❌] |
| Weekly non-purchasers | >1,000 | [X] | [✅/❌] |
| Data consistency | 28+ dagen | [X dagen] | [✅/❌] |
| Purchase value param | Ja | [Ja/Nee] | [✅/❌] |

## Recommended Predictive Audiences

### Audience 1: [Naam]
- **Type:** [Purchase/Churn/Revenue] probability
- **Threshold:** >[X]%
- **Combinatie met:** [Extra condities]
- **Verwachte size:** [X users]
- **Use case:** [Campagne type]

### Audience 2: [Naam]
- **Type:** [Type]
- **Threshold:** >[X]%
- **Combinatie met:** [Condities]
- **Verwachte size:** [X users]
- **Use case:** [Campagne type]

## Google Ads Strategie

### Bid Adjustments per Tier
| Probability Tier | Bid Adjustment | Rationale |
|-----------------|----------------|-----------|
| >80% | +[X]% | Highest intent |
| 50-80% | +[X]% | Medium intent |
| <50% | -[X]% | Lower intent |

### Campaign Recommendations
1. **[Campaign type]:** Target [audience] met [strategie]
2. **[Campaign type]:** Target [audience] met [strategie]

## Monitoring Plan
- **Review frequentie:** [Wekelijks]
- **Key metrics:** [Prediction accuracy, ROAS per tier, Size trends]
- **Alerts:** [Als accuracy <X% of size drop >Y%]

## Actie Items (als niet eligible)
1. [ ] [Eerste stap om eligibility te bereiken]
2. [ ] [Tweede stap]
3. [ ] [Derde stap]

## Notities
[Specifieke aanbevelingen of context voor deze property]
```

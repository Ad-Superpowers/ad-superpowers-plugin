---
name: automated-rules-builder
description: Bouw effectieve geautomatiseerde regels voor Meta Ads om campagnes 24/7 te optimaliseren, budget te beschermen en performance te maximaliseren. Gebruik deze skill wanneer je rules wilt opzetten voor budget management, performance acties, of notificaties.
---

# Automated Rules Builder

## Overview

Deze skill helpt bij het opzetten van geautomatiseerde regels in Meta Ads Manager die je campagnes continu monitoren en automatisch acties uitvoeren op basis van performance metrics, zodat je tijd bespaart en snel kunt reageren op veranderingen.

## Automated Rules Fundamentals

### Wat Zijn Automated Rules?

```
┌─────────────────────────────────────────────────────────────────┐
│  AUTOMATED RULES WERKING                                        │
│                                                                 │
│  1. TRIGGER: Wanneer checkt Meta de regel?                      │
│     └── Elke 30 min, dagelijks, of aangepast interval           │
│                                                                 │
│  2. CONDITIE: Welke criteria moeten voldaan zijn?               │
│     └── Bijv: CPA > €25 AND Impressions > 1000                  │
│                                                                 │
│  3. ACTIE: Wat gebeurt er als conditie waar is?                 │
│     └── Pause, budget wijzigen, bid aanpassen, notificatie      │
│                                                                 │
│  4. SCOPE: Op welke items past de regel?                        │
│     └── Campaigns, Ad Sets, of Ads                              │
└─────────────────────────────────────────────────────────────────┘
```

### Rules Locatie in Meta

```
NAVIGATIE:
Ads Manager → Rules → Create Rule
OF
Ads Manager → Select items → Rules → Create New Rule

RULE TYPES:
├── Reduce Audience Overlap
├── Reduce Auction Overlap
├── Optimize Ad Creative
└── Custom Rule (meest flexibel)
```

## Rule Categories & Use Cases

### Category 1: Budget Protection Rules

```
DOEL: Voorkom budget verspilling bij slechte performance

RULE: CPA Limiet Pauzeren
├── Apply to: Ad Sets (actief)
├── Action: Turn off ad set
├── Conditions:
│   ├── Cost per Result > €[MAX CPA]
│   └── Impressions > 1000 (wacht op data)
├── Time Range: Last 3 days
├── Schedule: Continuously
└── Notification: On

RULE: ROAS Minimum Guard
├── Apply to: Campaigns
├── Action: Turn off campaign
├── Conditions:
│   ├── Purchase ROAS < [MIN ROAS]
│   └── Amount Spent > €100
├── Time Range: Last 7 days
├── Schedule: Continuously
└── Notification: On
```

### Category 2: Scale Rules

```
DOEL: Automatisch opschalen bij goede performance

RULE: Budget Verhogen bij Lage CPA
├── Apply to: Ad Sets
├── Action: Increase daily budget by 20%
├── Conditions:
│   ├── Cost per Result < €[TARGET CPA - 20%]
│   └── Results > 10
├── Time Range: Last 3 days
├── Schedule: Daily at 06:00
├── Max Budget Cap: €[MAX DAILY BUDGET]
└── Notification: On

RULE: Decrease Budget bij Hoge CPA
├── Apply to: Ad Sets
├── Action: Decrease daily budget by 15%
├── Conditions:
│   ├── Cost per Result > €[TARGET CPA + 20%]
│   └── Amount Spent > €50
├── Time Range: Last 3 days
├── Schedule: Daily at 06:00
├── Min Budget Floor: €[MIN DAILY BUDGET]
└── Notification: On
```

### Category 3: Creative Management Rules

```
DOEL: Automatisch slecht presterende ads pauzeren

RULE: Low CTR Ad Pauzeren
├── Apply to: Ads
├── Action: Turn off ad
├── Conditions:
│   ├── CTR (link) < 0.5%
│   └── Impressions > 3000
├── Time Range: Last 7 days
├── Schedule: Daily at 00:00
└── Notification: On

RULE: Hoge Frequentie Waarschuwing
├── Apply to: Ad Sets
├── Action: Send notification only
├── Conditions:
│   └── Frequency > 3.0
├── Time Range: Last 7 days
├── Schedule: Daily at 09:00
└── Notification: On
```

### Category 4: Learning Phase Rules

```
DOEL: Bescherm learning phase en voorkom vroegtijdige beslissingen

RULE: Learning Phase Budget Lock
├── Apply to: Ad Sets
├── Action: Send notification only (!)
├── Conditions:
│   ├── Delivery is "Learning"
│   └── Results < 50
├── Time Range: Last 7 days
├── Schedule: Daily
└── Notification: On
⚠️ Note: Geen auto-pause tijdens learning!

RULE: Post-Learning Performance Check
├── Apply to: Ad Sets
├── Action: Turn off ad set
├── Conditions:
│   ├── Delivery is NOT "Learning"
│   ├── Cost per Result > €[TARGET CPA x 1.5]
│   └── Amount Spent > €[CPA TARGET x 50]
├── Time Range: Last 7 days
├── Schedule: Daily
└── Notification: On
```

## Rule Builder Templates

### Template 1: Complete Budget Protection Set

```
RULE SET: BUDGET BESCHERMING
============================

📋 RULE 1: Emergency Stop
├── Naam: [ACCOUNT]_Emergency_Stop_High_CPA
├── Apply to: All active ad sets
├── Action: Turn off
├── Conditions:
│   ├── Cost per Purchase > €[CPA TARGET x 2]
│   └── Purchases = 0
│   └── Amount Spent > €[CPA TARGET]
├── Time Range: Today
├── Schedule: Every 30 minutes
└── Why: Stop bleeding bij duidelijk verliezende ads

📋 RULE 2: CPA Limiet Daily
├── Naam: [ACCOUNT]_CPA_Limit_Daily
├── Apply to: All active ad sets
├── Action: Turn off
├── Conditions:
│   ├── Cost per Purchase > €[CPA TARGET x 1.3]
│   └── Purchases > 3
├── Time Range: Last 3 days
├── Schedule: Continuously
└── Why: Pauzeer bij aanhoudend hoge CPA

📋 RULE 3: No Conversions Alert
├── Naam: [ACCOUNT]_No_Conv_Alert
├── Apply to: All active ad sets
├── Action: Notification only
├── Conditions:
│   ├── Purchases = 0
│   └── Amount Spent > €[CPA TARGET x 2]
├── Time Range: Last 3 days
├── Schedule: Daily at 09:00
└── Why: Vroege waarschuwing bij 0 conversies
```

### Template 2: Auto-Scaling Rule Set

```
RULE SET: AUTO-SCALING
======================

📋 RULE 1: Scale Up Winners
├── Naam: [ACCOUNT]_Scale_Up_Winners
├── Apply to: All active ad sets
├── Action: Increase daily budget by 20%
├── Conditions:
│   ├── Cost per Purchase < €[CPA TARGET x 0.8]
│   └── Purchases > 5
│   └── Daily Budget < €[MAX BUDGET]
├── Time Range: Last 3 days
├── Schedule: Daily at 06:00
├── Budget Cap: €[MAX DAILY BUDGET]
└── Why: Geef budget aan winnaars

📋 RULE 2: Scale Down Losers
├── Naam: [ACCOUNT]_Scale_Down_Losers
├── Apply to: All active ad sets
├── Action: Decrease daily budget by 20%
├── Conditions:
│   ├── Cost per Purchase > €[CPA TARGET x 1.2]
│   └── Purchases > 3
│   └── Daily Budget > €[MIN BUDGET]
├── Time Range: Last 3 days
├── Schedule: Daily at 06:00
├── Budget Floor: €[MIN DAILY BUDGET]
└── Why: Reduceer verliezers automatisch

📋 RULE 3: Weekend Budget Boost
├── Naam: [ACCOUNT]_Weekend_Boost
├── Apply to: All active campaigns
├── Action: Increase daily budget by 30%
├── Conditions:
│   └── Current day is Saturday OR Sunday
├── Schedule: Custom (Fri 18:00)
└── Why: Extra budget voor weekend traffic
```

### Template 3: Creative Rotation Rules

```
RULE SET: CREATIVE MANAGEMENT
=============================

📋 RULE 1: Kill Low Performers
├── Naam: [ACCOUNT]_Kill_Low_CTR
├── Apply to: All active ads
├── Action: Turn off ad
├── Conditions:
│   ├── CTR (link click-through rate) < 0.5%
│   └── Impressions > 5000
├── Time Range: Last 7 days
├── Schedule: Daily at 00:00
└── Why: Stop budget naar slechte ads

📋 RULE 2: High Frequency Warning
├── Naam: [ACCOUNT]_Frequency_Alert
├── Apply to: All active ad sets
├── Action: Send notification only
├── Conditions:
│   └── Frequency > 3.5
├── Time Range: Last 7 days
├── Schedule: Daily at 09:00
└── Why: Signal voor creative refresh

📋 RULE 3: Cost per ThruPlay Alert
├── Naam: [ACCOUNT]_Video_Cost_Alert
├── Apply to: Video ads
├── Action: Turn off ad
├── Conditions:
│   ├── Cost per ThruPlay > €0.15
│   └── ThruPlays > 500
├── Time Range: Last 7 days
├── Schedule: Daily
└── Why: Pauzeer dure video ads
```

## Condition Builder Guide

### Beschikbare Metrics

```
PERFORMANCE METRICS:
├── Results (conversies naar keuze)
├── Cost per Result
├── Impressions
├── Reach
├── Frequency
├── CPM (cost per 1000 impressions)
├── CPC (cost per click)
├── CTR (click-through rate)
├── Amount Spent

CONVERSION METRICS:
├── Purchases
├── Cost per Purchase
├── Purchase ROAS
├── Leads
├── Cost per Lead
├── Add to Carts
├── Checkouts Initiated

VIDEO METRICS:
├── Video Plays
├── ThruPlays
├── Cost per ThruPlay
├── Video Average Play Time
├── Video Plays at 25%, 50%, 75%, 100%

STATUS METRICS:
├── Delivery (Learning, Active, etc.)
├── Current Day (Mon, Tue, etc.)
├── Current Time
```

### Condition Combinaties

```
AND vs OR LOGIC:

AND (alle condities moeten waar zijn):
├── CPA > €20 AND Impressions > 1000
└── Beide moeten waar zijn voor actie

OR (één conditie is genoeg):
├── CPA > €30 OR CTR < 0.3%
└── Één van beide triggert actie

VOORBEELD COMPLEX:
(CPA > €25 AND Purchases > 5) OR (CTR < 0.5% AND Impressions > 5000)
```

## Best Practices & Waarschuwingen

### Do's ✅

```
✅ AANBEVOLEN:
├── Altijd "AND Impressions > X" toevoegen
│   └── Voorkomt beslissingen op te weinig data
├── Gebruik 3-7 dagen time range
│   └── Balans tussen reactiesnelheid en betrouwbaarheid
├── Stel budget caps/floors in bij scaling rules
│   └── Voorkomt runaway budgetten
├── Test rules eerst op kleine subset
│   └── Valideer voor breed uitrollen
├── Documenteer je rules
│   └── Weet waarom je iets hebt ingesteld
└── Check rules weekly
    └── Pas thresholds aan bij veranderende metrics
```

### Don'ts ❌

```
❌ VERMIJDEN:
├── Automatisch pauzeren tijdens Learning Phase
│   └── Laat learning fase uitlopen (50 conv)
├── Te korte time ranges (Today/Yesterday)
│   └── Te volatiel, onbetrouwbare data
├── Te lage impression thresholds
│   └── Minimaal 1000+ voor betrouwbare CTR
├── Conflicterende rules
│   └── Rule A verhoogt, Rule B verlaagt tegelijk
├── Vergeten rules die nog draaien
│   └── Audit maandelijks
└── Geen notificaties aan
    └── Altijd weten wat er gebeurt
```

## Rule Audit Checklist

### Maandelijkse Review

```
RULE AUDIT CHECKLIST
====================

□ INVENTARIS
├── Hoeveel rules zijn actief?
├── Welke rules hebben >30 dagen niet getriggerd?
└── Zijn er conflicterende rules?

□ THRESHOLDS
├── Kloppen CPA targets nog met huidige performance?
├── Zijn budget caps/floors nog relevant?
└── Zijn impression minimums voldoende?

□ PERFORMANCE
├── Welke rules hebben het meest getriggerd?
├── Hebben auto-actions het verwachte effect gehad?
└── Zijn er false positives/negatives?

□ CLEANUP
├── Verwijder inactieve rules
├── Update naming conventions
└── Documenteer wijzigingen
```

## Voorbeeld Interactie

**Gebruiker**: "Ik wil regels instellen zodat mijn ads automatisch stoppen als de CPA te hoog wordt. Mijn target CPA is €15."

**Claude response**:

"Ik help je met een complete rule set voor CPA bescherming. Met een target CPA van €15 stel ik het volgende voor:

---

**RULE SET: CPA Protection (Target: €15)**

**Rule 1: Emergency Stop** 🚨
```
Naam: CPA_Emergency_Stop
Apply to: All active ad sets
Action: Turn OFF ad set
Conditions:
├── Cost per Purchase > €30 (2x target)
└── Impressions > 500
Time Range: Today
Schedule: Every 30 minutes
```
*Stopt direct bij extreme CPA*

---

**Rule 2: CPA Limiet** ⚠️
```
Naam: CPA_Limit_Pause
Apply to: All active ad sets
Action: Turn OFF ad set
Conditions:
├── Cost per Purchase > €19.50 (1.3x target)
└── Purchases > 3
Time Range: Last 3 days
Schedule: Continuously
```
*Pauzeer bij aanhoudend hoge CPA*

---

**Rule 3: No Conversion Alert** 📢
```
Naam: No_Conv_Warning
Apply to: All active ad sets
Action: Send notification only
Conditions:
├── Purchases = 0
└── Amount Spent > €30 (2x target)
Time Range: Last 3 days
Schedule: Daily at 09:00
```
*Waarschuwing bij geen conversies*

---

**⚠️ Belangrijk:**
- Zet **NIET** een auto-pause rule tijdens learning phase
- Wacht tot je minimaal 50 conversies hebt gehad
- Check na 1 week of de thresholds goed werken

Wil je dat ik ook scaling rules toevoeg voor wanneer CPA onder target zit?"

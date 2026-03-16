---
name: scaling-calculator
description: Bereken optimale scaling strategieën voor Meta Ads campagnes met budget incrementen, timeline planning en risk assessment. Gebruik deze skill wanneer je succesvol wilt opschalen zonder performance te verliezen.
---

# Scaling Calculator

## Overview

Deze skill helpt bij het berekenen van optimale scaling strategieën voor Meta Ads, inclusief budget verhogingen, tijdlijnen, en risicobeoordeling om performance te behouden tijdens groei.

## Scaling Fundamentals

### Waarom Scaling Lastig Is

```
┌─────────────────────────────────────────────────────────────────┐
│  HET SCALING DILEMMA                                            │
│                                                                 │
│  Te snel schalen:                                               │
│  ├── Learning phase reset                                       │
│  ├── CPA spike door algoritme adjustments                       │
│  ├── Audience exhaustion                                        │
│  └── Budget waste                                               │
│                                                                 │
│  Te langzaam schalen:                                           │
│  ├── Missed revenue opportunity                                 │
│  ├── Competitor voorsprong                                      │
│  ├── Seizoensgebonden kansen gemist                             │
│  └── Inefficiënte growth                                        │
│                                                                 │
│  Sweet spot: 15-20% budget increase per 3-4 dagen               │
│              mits performance stabiel blijft                    │
└─────────────────────────────────────────────────────────────────┘
```

### De 20% Regel

```
META'S AANBEVOLEN SCALING:
==========================

Budget verhogingen tot 20% triggeren GEEN learning phase reset.

Voorbeeld:
├── Dag 1: €50/dag
├── Dag 4: €60/dag (+20%)
├── Dag 7: €72/dag (+20%)
├── Dag 10: €86/dag (+20%)
└── Dag 13: €103/dag (+20%)

Na 2 weken: Budget verdubbeld zonder learning phase reset!
```

## Scaling Readiness Check

### Pre-Scaling Checklist

```
VOORDAT JE SCHAALT - VALIDEER:
==============================

□ PERFORMANCE STABILITEIT
├── CPA stabiel laatste 7 dagen? (variatie <15%)
├── Voldoende conversies? (>50 per week)
├── Positieve ROAS boven target?
└── ✓ Ready als: Alle 3 checks positief

□ AUDIENCE HEADROOM
├── Huidige frequency <2.5?
├── Audience size >10x dagbudget?
├── Reach nog groeipotentieel?
└── ✓ Ready als: Alle 3 checks positief

□ CREATIVE STRENGTH
├── CTR stabiel of stijgend?
├── Minimaal 3-5 actieve creatives?
├── Geen creative fatigue signalen?
└── ✓ Ready als: Alle 3 checks positief

□ TECHNICAL READINESS
├── Pixel/CAPI correct werkend?
├── Geen delivery issues?
├── Budget cap niet bereikt?
└── ✓ Ready als: Alle 3 checks positief

SCALING GO/NO-GO:
├── 12/12 checks: 🟢 GO - Scale aggressief
├── 9-11 checks: 🟡 CAUTIOUS - Scale conservatief
├── 6-8 checks: 🟠 PREPARE - Fix issues eerst
└── <6 checks: 🔴 NO-GO - Niet schalen
```

## Scaling Calculator

### Vertical Scaling (Budget Verhogen)

```
BUDGET SCALING CALCULATOR
=========================

INPUT:
├── Huidig dagbudget: €[X]
├── Target dagbudget: €[Y]
├── Huidige CPA: €[Z]
├── Max acceptable CPA: €[W]

BEREKENING:
├── Budget multiplier: Y / X = [M]x
├── Geschatte scaling periode: log(M) / log(1.2) × 3 dagen
├── CPA buffer: (W - Z) / Z × 100 = [B]%
└── Risk level: [Laag/Medium/Hoog]

VOORBEELD:
Huidig: €100/dag → Target: €500/dag

Scaling timeline (20% increments):
├── Week 1: €100 → €120 → €144
├── Week 2: €173 → €207 → €249
├── Week 3: €299 → €358 → €430
└── Week 4: €516 ✓ Target bereikt!

Totale periode: ~3-4 weken voor 5x scale
```

### Horizontal Scaling (Meer Ad Sets)

```
HORIZONTAL SCALING CALCULATOR
=============================

INPUT:
├── Huidige winnende audiences: [AANTAL]
├── Nieuwe audiences te testen: [LIJST]
├── Budget per test ad set: €[X]
├── Test periode: [Y] dagen

BEREKENING:
├── Totaal test budget: audiences × budget × dagen
├── Minimum conversies voor conclusie: 50 per ad set
├── Test duration: 50 / (daily conversions estimate)

STRUCTURE:
Original Campaign (bewezen):
├── Ad Set 1 (winning): €100/dag
├── Ad Set 2 (winning): €80/dag
└── Ad Set 3 (winning): €60/dag

Test Campaign (experimental):
├── Ad Set 4 (new LAL): €30/dag
├── Ad Set 5 (new interest): €30/dag
└── Ad Set 6 (new geo): €30/dag

Regel: Test budget = max 30% van totaal
```

## Scaling Scenarios

### Scenario 1: Conservative Scale (Laag Risico)

```
CONSERVATIVE SCALING PLAN
=========================

Situatie: Stabiele performance, wil behouden

Budget increases: 15% per 4 dagen
Timeline: Langzaam maar steady
Risk: Laag

WEEK 1:
├── Dag 1-4: €100/dag (baseline)
└── Dag 5-7: €115/dag (+15%)

WEEK 2:
├── Dag 8-11: €132/dag (+15%)
└── Dag 12-14: €152/dag (+15%)

WEEK 3:
├── Dag 15-18: €175/dag (+15%)
└── Dag 19-21: €201/dag (+15%)

RESULTAAT: 2x budget in 3 weken
Verwachte CPA impact: +5-10%
```

### Scenario 2: Moderate Scale (Medium Risico)

```
MODERATE SCALING PLAN
=====================

Situatie: Goede performance, ruimte om te pushen

Budget increases: 20% per 3 dagen
Timeline: Gebalanceerd
Risk: Medium

WEEK 1:
├── Dag 1-3: €100/dag
├── Dag 4-6: €120/dag (+20%)
└── Dag 7: €144/dag (+20%)

WEEK 2:
├── Dag 8-10: €173/dag (+20%)
├── Dag 11-13: €207/dag (+20%)
└── Dag 14: €249/dag (+20%)

RESULTAAT: 2.5x budget in 2 weken
Verwachte CPA impact: +10-20%
```

### Scenario 3: Aggressive Scale (Hoog Risico)

```
AGGRESSIVE SCALING PLAN
=======================

Situatie: Hot product, seizoensgebonden urgentie

Budget increases: 30-50% per 2-3 dagen
Timeline: Snel
Risk: Hoog

⚠️ ALLEEN GEBRUIKEN BIJ:
├── CPA ver onder target (>30% marge)
├── Bewezen grote audiences
├── Veel creative variatie
└── Bereid om CPA spike te accepteren

WEEK 1:
├── Dag 1-2: €100/dag
├── Dag 3-4: €150/dag (+50%)
├── Dag 5-6: €225/dag (+50%)
└── Dag 7: €337/dag (+50%)

RESULTAAT: 3.4x budget in 1 week
Verwachte CPA impact: +20-40% (tijdelijk)

FALLBACK PLAN:
Als CPA >target + 30%:
└── Reduceer budget met 20%
└── Stabiliseer 3-4 dagen
└── Probeer opnieuw met 20% stappen
```

## Scaling Decision Tree

```
SCALING DECISION FLOWCHART
==========================

START: Wil je schalen?
│
├─► Vraag 1: CPA onder target?
│   ├── JA → Ga door
│   └── NEE → STOP, optimaliseer eerst
│
├─► Vraag 2: >50 conversies/week?
│   ├── JA → Ga door
│   └── NEE → STOP, verzamel meer data
│
├─► Vraag 3: Frequency <2.5?
│   ├── JA → Ga door
│   └── NEE → Horizontal scale (nieuwe audiences)
│
├─► Vraag 4: CPA marge t.o.v. target?
│   ├── >30% onder → Aggressive scale mogelijk
│   ├── 15-30% onder → Moderate scale
│   └── <15% onder → Conservative scale
│
└─► Vraag 5: Hoeveel tijd?
    ├── <1 week → Aggressive (accepteer risico)
    ├── 2-3 weken → Moderate
    └── 4+ weken → Conservative
```

## Scaling Monitoring Dashboard

### Metrics om te Tracken Tijdens Scale

```
DAILY SCALING MONITOR
=====================

Dag │ Budget │ Spend │ Conv │  CPA  │ ROAS │ Freq │ Status
────┼────────┼───────┼──────┼───────┼──────┼──────┼────────
 1  │ €100   │ €98   │  8   │ €12.25│ 3.2x │ 1.2  │ 🟢
 2  │ €100   │ €100  │  9   │ €11.11│ 3.5x │ 1.3  │ 🟢
 3  │ €100   │ €99   │  7   │ €14.14│ 2.8x │ 1.4  │ 🟢
 4  │ €120   │ €118  │  8   │ €14.75│ 2.7x │ 1.5  │ 🟢 Scale
 5  │ €120   │ €120  │  7   │ €17.14│ 2.3x │ 1.6  │ 🟡
 6  │ €120   │ €119  │  9   │ €13.22│ 3.0x │ 1.7  │ 🟢
 7  │ €144   │ €142  │ 10   │ €14.20│ 2.8x │ 1.8  │ 🟢 Scale

ALERT TRIGGERS:
├── 🟡 Warning: CPA +15% vs baseline
├── 🔴 Stop: CPA +30% vs baseline of >target
├── 🔴 Stop: Frequency >3.0
└── 🔴 Stop: CTR drops >20%
```

## Scaling Formulas

### Budget Scaling Formula

```
OPTIMAL DAILY BUDGET CALCULATOR
===============================

Formule voor max dagbudget per ad set:

Max Budget = (Target CPA × Weekly Conv Goal) / 7

Voorbeeld:
├── Target CPA: €20
├── Weekly conversions goal: 100
├── Max budget: (€20 × 100) / 7 = €286/dag

CHECK: Audience headroom
├── Audience size: 500.000
├── Dagelijks bereik bij €286: ~15.000 (3%)
└── Headroom: ✅ Ruim voldoende
```

### Scale Timeline Calculator

```
TIMELINE CALCULATOR
===================

Van €[A] naar €[B] met [X]% stappen:

Formule:
Days = (log(B/A) / log(1 + X/100)) × step_interval

Voorbeeld: €100 → €500, 20% stappen, elke 3 dagen
Days = (log(5) / log(1.2)) × 3
Days = (1.61 / 0.18) × 3
Days = 8.9 × 3 = ~27 dagen

QUICK REFERENCE TABLE:
──────────────────────────────────────────
Multiplier │ 15% stappen │ 20% stappen
──────────────────────────────────────────
    2x     │   16 dagen  │   12 dagen
    3x     │   25 dagen  │   19 dagen
    5x     │   37 dagen  │   27 dagen
   10x     │   53 dagen  │   39 dagen
──────────────────────────────────────────
```

## Scaling Strategy Templates

### Template: Scale Plan Generator

```
SCALING PLAN - [ACCOUNT/CAMPAIGN]
=================================

📊 HUIDIGE SITUATIE:
├── Dagbudget: €[X]
├── CPA: €[Y] (target: €[Z])
├── CPA marge: [Y-Z]/Z × 100 = [M]%
├── Weekly conversions: [N]
└── Frequency: [F]

🎯 SCALING GOAL:
├── Target budget: €[TARGET]
├── Multiplier: [TARGET/X]x
└── Deadline: [DATUM]

📋 AANBEVOLEN APPROACH:
[Conservative/Moderate/Aggressive]

📅 SCALING TIMELINE:

Week 1:
├── [Dag]: €[budget] → Actions: [...]
├── [Dag]: €[budget] → Check: [...]
└── [Dag]: €[budget] → Evaluate: [...]

Week 2:
├── [Dag]: €[budget] → Actions: [...]
[etc...]

⚠️ STOP CONDITIONS:
├── CPA > €[threshold]
├── Frequency > [X]
├── CTR drops below [X]%
└── ROAS < [X]

✅ SUCCESS METRICS:
├── Target bereikt binnen [X] dagen
├── CPA blijft onder €[X]
└── Geen learning phase resets
```

## Voorbeeld Interactie

**Gebruiker**: "Mijn campagne doet het goed met €100/dag en €15 CPA (target is €20). Ik wil schalen naar €500/dag. Hoe doe ik dat het beste?"

**Claude response**:

"Goed nieuws - je hebt 25% CPA marge, dat geeft ruimte om te schalen! Hier is je plan:

---

**SCALING ASSESSMENT:**

| Metric | Waarde | Status |
|--------|--------|--------|
| CPA marge | 25% onder target | 🟢 Goed |
| Scale multiplier | 5x | Medium |
| Recommended approach | Moderate | ✅ |

---

**AANBEVOLEN TIMELINE (20% stappen, ~4 weken):**

```
Week 1:
├── Dag 1-3: €100/dag (baseline)
├── Dag 4-6: €120/dag (+20%)
└── Dag 7: €144/dag (+20%)

Week 2:
├── Dag 8-10: €173/dag (+20%)
├── Dag 11-13: €207/dag (+20%)
└── Dag 14: €249/dag (+20%)

Week 3:
├── Dag 15-17: €299/dag (+20%)
├── Dag 18-20: €358/dag (+20%)
└── Dag 21: €430/dag (+20%)

Week 4:
├── Dag 22-24: €516/dag ✓ Target!
└── Dag 25+: Stabiliseren
```

---

**⚠️ MONITORING:**
Stop en stabiliseer als:
- CPA > €18 (meer dan 20% stijging)
- Frequency > 2.5
- CTR daalt >15%

**💡 TIP:** Overweeg parallel een test campaign met nieuwe audiences te starten voor horizontal scale.

Wil je een gedetailleerd dag-voor-dag tracking sheet?"

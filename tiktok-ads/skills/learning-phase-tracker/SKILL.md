---
name: tiktok-learning-phase-tracker
description: "TikTok Ads learning phase management en edit impact analyzer. Gebruik voor: (1) Learning phase status beoordelen, (2) 72-hour learning window navigeren, (3) Edit impact voorspellen, (4) Consolidation strategies, (5) Learning phase exit strategieën. Triggers: learning phase, learning limited, tiktok learning, ad group stuck, exit learning, 50 conversions, edit impact, significant edit."
---

# TikTok Learning Phase Tracker

Analyzer voor TikTok Ads learning phase management. Voorspelt edit impact en adviseert over optimale timing voor wijzigingen.

## Learning Phase Basics

### Wat Is TikTok's Learning Phase?

```
TIKTOK LEARNING PHASE UITLEG
============================

Periode waarin TikTok's algoritme data verzamelt over:
├── Welke gebruikers het meest relevant zijn
├── Optimale bid prijzen per auction
├── Beste tijden en placements
└── Creative performance patterns

STATUS INDICATOREN:
├── "Learning": Algoritme verzamelt data
├── "Active": Exitied, stabiele optimalisatie
├── "Learning Limited": Te weinig conversies
└── "Not Delivering": Budget/bid issues
```

### Exit Criteria

```
TIKTOK EXIT REQUIREMENTS
========================

MINIMUM VEREISTEN:
├── 50 conversion events per week per ad group
├── 72-hour initial learning window
├── Voldoende budget voor target CPA
└── Stabiele creative performance

FORMULE VOOR MINIMUM BUDGET:
Daily Budget = (Target CPA × 50) / 7

VOORBEELD:
├── Target CPA: €20
├── Minimum weekly: €20 × 50 = €1,000
├── Minimum daily: €1,000 / 7 = €143/dag
└── Met buffer (1.5x): €215/dag aanbevolen

72-HOUR RULE:
├── Eerste 72 uur: GEEN wijzigingen maken
├── Algoritme leert fundamentele patterns
├── Edits in deze periode = reset learning
└── Ook kleine wijzigingen vermijden
```

### Learning Phase Statuses

```
STATUS INTERPRETATIE
====================

STATUS: Learning (Normal)
├── Duration: 0-7 dagen
├── Betekenis: Algoritme leert actief
├── Actie: WACHTEN, niet wijzigen
├── Verwachting: CPA fluctueert 30-50%
└── Exit: Na 50+ conversies/week

STATUS: Learning Limited
├── Duration: >7 dagen zonder exit
├── Oorzaken:
│   ├── Budget te laag
│   ├── Audience te klein (<100k)
│   ├── Bid te laag
│   └── Event te zeldzaam
├── Actie: Intervene (zie Exit Strategies)
└── Urgentie: Hoog

STATUS: Active
├── Betekenis: Learning complete
├── CPA: Gestabiliseerd
├── Actie: Optimaliseren, schalen
└── Edits: Voorzichtig, kan re-trigger

STATUS: Not Delivering
├── Oorzaken:
│   ├── Budget exhausted
│   ├── Bid te laag voor auction
│   ├── Creative rejected
│   └── Audience exhausted
├── Actie: Diagnose en fix
└── Urgentie: Kritiek
```

## TikTok vs Meta Learning Phase

```
PLATFORMVERGELIJKING
====================

Kenmerk                │ TikTok          │ Meta
───────────────────────┼─────────────────┼─────────────────
Exit threshold         │ 50/week/ad group│ 50/week/ad set
Initial learning       │ 72 hours strict │ 3-7 days flex
Edit sensitivity       │ HOOG            │ Gemiddeld
Recovery time          │ 3-5 dagen       │ 3-7 dagen
Consolidation impact   │ Zeer positief   │ Positief
Creative refresh impact│ 4x sneller fatigue│ 2-3 weken
Budget change tolerance│ 20% safe        │ 20% safe

BELANGRIJKSTE VERSCHIL:
├── TikTok = strikter 72-hour window
├── TikTok = snellere creative fatigue
├── TikTok = vaker consolidation nodig
└── TikTok = hogere edit sensitivity
```

## Edit Impact Matrix

### Significant Edits (Trigger Learning Reset)

```
SIGNIFICANT EDITS - VERMIJDEN IN LEARNING
=========================================

Edit Type                │ Impact │ Reset Risk │ Recovery
─────────────────────────┼────────┼────────────┼──────────
Budget change >20%       │ High   │ 90%        │ 3-5 dagen
Audience change          │ High   │ 95%        │ 3-7 dagen
Optimization goal change │ High   │ 100%       │ 3-7 dagen
Bid/bid strategy change  │ High   │ 85%        │ 3-5 dagen
New creative addition    │ Med    │ 60%        │ 2-4 dagen
Geographic change        │ High   │ 90%        │ 3-5 dagen
Schedule change          │ Med    │ 50%        │ 2-3 dagen
Placement change         │ Med    │ 70%        │ 2-4 dagen

⚠️ IN EERSTE 72 UUR:
├── ALLE edits triggeren reset
├── Zelfs "minor" edits
├── Wacht tot window compleet
└── Plan wijzigingen vooraf
```

### Non-Significant Edits (Meestal Veilig)

```
VEILIGE EDITS
=============

Edit Type                │ Impact │ Reset Risk │ Notes
─────────────────────────┼────────┼────────────┼──────────
Ad group name change     │ None   │ 0%         │ Altijd veilig
Campaign name change     │ None   │ 0%         │ Altijd veilig
Budget <20% change       │ Low    │ 10%        │ Incrementeel OK
Ad creative pause        │ Low    │ 20%        │ Als andere actief
Bid adjustment <10%      │ Low    │ 15%        │ Minor tweaks OK
Ad copy minor tweak      │ Low    │ 25%        │ Tekst alleen
```

## Budget Change Impact Calculator

### Safe Budget Zones

```
BUDGET WIJZIGING IMPACT
=======================

Current Budget: €[X]/dag
Learning Status: [Learning/Active/Limited]

SAFE ZONE (Geen Reset):
├── Maximum increase: +20% (€[X × 1.2])
├── Maximum decrease: -20% (€[X × 0.8])
├── Frequency: 1x per 3 dagen
└── Example: €100 → €120 is safe

YELLOW ZONE (Mogelijk Reset):
├── Increase: 20-40%
├── Decrease: 20-40%
├── Aanbeveling: Split in 2 stappen
└── Example: €100 → €140 doe via €100 → €120 → €140

RED ZONE (Waarschijnlijk Reset):
├── Increase: >40%
├── Decrease: >40%
├── Aanbeveling: Dupliceer ad group
└── Example: €100 → €200 = nieuwe ad group maken
```

### Budget Change Decision Tree

```
WIL JE BUDGET VERHOGEN?
│
├─► <20% increase
│   ├─► Status: Active → Direct doorvoeren
│   └─► Status: Learning → Wacht tot Active
│
├─► 20-40% increase
│   ├─► Split in 2 stappen (10-20% elk)
│   ├─► Wacht 3 dagen tussen stappen
│   └─► Monitor CPA na elke stap
│
└─► >40% increase
    ├─► NIET wijzigen (triggert reset)
    ├─► Dupliceer ad group met nieuwe budget
    ├─► Laat origineel parallel draaien
    └─► Evalueer na 7 dagen
```

## Learning Phase Exit Strategies

### Snelle Exit Tactieken

```
TACTIC 1: BUDGET BOOST
======================
Wanneer: Learning Limited door budget
Hoe:
├── Bereken: Target CPA × 50 / 7 × 1.5
├── Verhoog budget naar dit niveau
├── Wacht 72 uur
└── Na exit: Scale terug naar gewenst niveau (geleidelijk)

Voorbeeld:
├── Target CPA: €25
├── Minimum: €25 × 50 / 7 = €179/dag
├── Met buffer: €179 × 1.5 = €268/dag
└── Na exit: Scale down 20%/3 dagen


TACTIC 2: CONSOLIDATIE
======================
Wanneer: Meerdere ad groups met weinig volume
Hoe:
├── Identificeer 2-3 vergelijkbare ad groups
├── Maak nieuwe ad group met:
│   ├── Gecombineerd budget
│   ├── Beste creatives van alle groups
│   └── Broader audience (union)
├── Pause originelen
└── Monitor nieuwe ad group

Voordeel:
├── Aggregated data = snellere learning
├── Efficiënter budget gebruik
├── Minder fragmentatie
└── TikTok prefereert consolidated structure


TACTIC 3: HIGHER-FUNNEL EVENT
=============================
Wanneer: Conversion event te zeldzaam
Hoe:
├── Tijdelijk optimaliseren voor:
│   ├── AddToCart ipv Purchase
│   ├── InitiateCheckout ipv Purchase
│   └── ViewContent ipv Lead
├── Meer events = snellere learning
├── Na exit: Switch terug naar lower-funnel
└── Let op: Traffic kwaliteit kan wijzigen

Wanneer NIET:
├── Je hebt al genoeg volume
├── Budget is het probleem (niet event frequency)
└── Quality/fraud concerns


TACTIC 4: BROADER TARGETING
===========================
Wanneer: Audience te klein (<100k)
Hoe:
├── Verwijder narrowing restrictions
├── Expand age ranges
├── Toevoegen vergelijkbare interests
├── Test Auto-Targeting mode
└── Let lookalike algoritme werken

TikTok Specific:
├── Auto-Targeting vaak beter dan manual
├── Algoritme is sterk in discovery
├── Begin broad, narrow later
└── Minimum audience: 100k+ aanbevolen
```

### Learning Limited Oplossingen

```
DIAGNOSE: WAAROM LEARNING LIMITED?
==================================

Check 1: Budget vs CPA
├── Current budget: €[X]/dag
├── Achieved CPA: €[Y]
├── Conversies/week: [Z]
├── Minimum budget: €Y × 50 / 7
└── Probleem? Budget < Minimum

Check 2: Audience Size
├── Current audience: [X]
├── Minimum aanbevolen: 100,000
├── Optimal: 500k-2M
└── Probleem? Audience < 100k

Check 3: Bid Competitiveness
├── Current bid/cap: €[X]
├── Suggested range: €[Y-Z]
├── Winning auctions: [X]%
└── Probleem? Bid < suggested range

Check 4: Event Frequency
├── Events/week: [X]
├── Required: 50/week
├── Event type: [specified]
└── Probleem? Events < 50

OPLOSSINGSMATRIX:
│
├── Budget issue → Tactic 1 (Budget Boost)
├── Audience issue → Tactic 4 (Broader Targeting)
├── Bid issue → Raise bid/switch to auto
└── Event issue → Tactic 3 (Higher-Funnel)
```

## 72-Hour Rule Management

```
72-HOUR LEARNING WINDOW PROTOCOL
================================

HOUR 0-24:
├── Status: Initial data collection
├── CPA: Highly volatile (±50-100%)
├── Volume: Inconsistent
├── Action: ZERO edits
└── Monitoring: Observe only

HOUR 24-48:
├── Status: Pattern formation
├── CPA: Still volatile (±30-50%)
├── Volume: Stabilizing
├── Action: ZERO edits
└── Monitoring: Note trends

HOUR 48-72:
├── Status: Final learning phase
├── CPA: Narrowing range (±20-30%)
├── Volume: More consistent
├── Action: ZERO edits
└── Monitoring: Prepare optimization plan

HOUR 72+:
├── Status: Safe to optimize
├── Check: 50+ conversions achieved?
│   ├── Yes → Active status, can optimize
│   └── No → Learning continues, wait more
├── Action: Minor optimizations allowed
└── Caution: Still avoid significant edits
```

### Pre-Launch Checklist

```
VOOR LANCERING CHECKLIST
========================

□ Budget voldoende?
  ├── Minimum: CPA target × 50 / 7
  └── Aanbevolen: 1.5x minimum

□ Audience >100k?
  ├── Check audience size estimator
  └── Broader is beter voor learning

□ Meerdere creatives?
  ├── Minimum: 3-5 ads per ad group
  └── Mix: Different hooks, formats

□ Tracking correct?
  ├── Pixel events firing
  └── Conversions registreren

□ Geen wijzigingen gepland?
  ├── Plan 72+ uur hands-off
  └── Block calendar indien nodig

□ Monitoring setup?
  ├── Alerts voor anomalies
  └── Daily check-in scheduled
```

## Edit Timing Best Practices

### Wanneer Wijzigingen Doorvoeren

```
BESTE TIMING VOOR EDITS
=======================

IDEAAL:
├── Na 72-hour window compleet
├── Na 50+ conversions bereikt
├── Begin van de week (maandag/dinsdag)
├── Na stabiele 5-7 dagen performance
└── Overdag (avoid late-night deploys)

VERMIJD:
├── Eerste 72 uur (KRITIEK)
├── Tijdens learning phase
├── Weekend (minder data)
├── Peak shopping periods
├── Direct na vorige wijziging (<3 dagen)
├── Tijdens TikTok Shop mega events
└── Late avond (monitoring difficult)
```

### Batch vs Sequential Edits

```
MEERDERE EDITS NODIG?
│
├─► Optie 1: Batch Alle Edits
│   ├── Wanneer: Grote refresh/restructure
│   ├── Voordeel: Eén learning reset
│   ├── Nadeel: Geen isolatie van impact
│   └── Timing: Begin van de week
│
└─► Optie 2: Sequential Edits
    ├── Wanneer: Testing hypotheses
    ├── Voordeel: Isoleer impact per change
    ├── Nadeel: Meerdere potentiële resets
    ├── Spacing: 5-7 dagen tussen edits
    └── Priority: Biggest impact first
```

## Ad Group Health Check

### Quick Health Assessment

```
AD GROUP HEALTH CHECK
=====================

□ Learning Status: [Learning/Active/Limited]
□ Days in status: [X] dagen
□ Conversions L7D: [X]
□ Daily budget: €[X]
□ Current CPA: €[X]
□ Target CPA: €[X]
□ Frequency L7D: [X]
□ CTR: [X]%
□ 2-sec View Rate: [X]%

HEALTH SCORE:
├── 🟢 HEALTHY: Active + 50+ conv/week + CPA ≤1.2x target
├── 🟡 WARNING: Learning >7d OR 25-50 conv/week OR CPA 1.2-1.5x target
├── 🔴 CRITICAL: Limited OR <25 conv/week OR CPA >1.5x target
└── ⚫ DEAD: Not Delivering >24 hours
```

### Recommended Actions by Status

```
ACTIE PER STATUS
================

🟢 HEALTHY (Active, Performing)
├── Actie: Gentle optimization
├── Scale: +20% budget per 3-4 dagen
├── Creative: Add new (don't replace)
├── Monitor: Weekly review
└── Goal: Maintain momentum

🟡 WARNING (Learning Extended / Moderate Issues)
├── Diagnose: Budget? Audience? Creative?
├── Priority 1: Fix root cause
├── Priority 2: Consider consolidation
├── Avoid: Multiple changes at once
└── Timeline: Fix within 7 dagen

🔴 CRITICAL (Learning Limited / Poor Performance)
├── Diagnose: Use Learning Limited checklist
├── Immediate: Implement exit tactic
├── Option A: Budget boost (if budget issue)
├── Option B: Consolidate (if fragmented)
├── Option C: Rebuild (if fundamentally broken)
└── Timeline: Act within 48 hours

⚫ DEAD (Not Delivering)
├── Check 1: Budget exhausted?
├── Check 2: Bid too low?
├── Check 3: Creative rejected?
├── Check 4: Audience exhausted?
├── Immediate: Identify blocker
└── Timeline: Fix within 24 hours
```

## Common Scenarios

### Scenario 1: Stuck in Learning (>7 dagen)

```
SITUATIE:
├── Ad group: 10 dagen in Learning
├── Budget: €75/dag
├── Conversies L7D: 18
├── CPA: €28
├── Target CPA: €25

DIAGNOSE:
├── Required budget: €25 × 50 / 7 = €179/dag
├── Current budget: €75/dag (42% van requirement)
└── Root cause: BUDGET TE LAAG

OPLOSSING:
1. Verhoog budget naar €200/dag (met buffer)
2. Wacht nieuwe 72-hour window
3. Na learning exit: Scale terug naar €150/dag
4. Achieve sustainable 50+ conv/week

ALTERNATIEF:
├── Consolideer met andere ad groups
└── Aggregate budget = faster learning
```

### Scenario 2: Creative Refresh Nodig

```
SITUATIE:
├── Ad group: Active (4 weken)
├── CTR: Gedaald van 2.1% naar 1.2%
├── CPM: Gestegen van €8 naar €12
├── Diagnose: Creative fatigue (TikTok = 3-7 dagen!)

AANPAK:
1. NIET alle creatives vervangen (triggers reset)
2. VOEG nieuwe creatives toe aan bestaande ad group
3. Laat algoritme nieuwe vs oude testen
4. Na 5-7 dagen: Pause underperformers
5. Herhaal cycle met nieuwe additions

BEST PRACTICE:
├── Add 2-3 new creatives per week
├── Maintain 5-8 active creatives
├── Remove bottom 20% performers
└── Never full creative swap
```

### Scenario 3: Budget Verdubbelen

```
SITUATIE:
├── Ad group: Active, performing well
├── Current budget: €100/dag
├── Target: €200/dag
├── Risk: >40% increase = reset

OPLOSSING A: Gradueel
├── Week 1: €100 → €120 (+20%)
├── Week 2: €120 → €145 (+20%)
├── Week 3: €145 → €175 (+20%)
├── Week 4: €175 → €200 (+14%)
└── Total: 4 weken voor 2x scale (safe)

OPLOSSING B: Duplicatie
├── Dupliceer ad group met €200/dag budget
├── Laat origineel op €100/dag draaien
├── Na 7-10 dagen: Vergelijk performance
├── Scale winner, pause loser
└── Total: 2 weken maar parallelle spend
```

### Scenario 4: Post-Edit Recovery

```
SITUATIE:
├── Onbedoeld significant edit gemaakt
├── Learning phase getriggered
├── CPA spiked 40%

RECOVERY PROTOCOL:
1. GEEN VERDERE EDITS (maakt het erger)
2. Monitor 72 uur zonder actie
3. Als na 72 uur nog geen stabilisatie:
   ├── Check of edit correct was
   ├── Overweeg rollback (nieuwe reset)
   └── Of: Accept en wacht op re-learning
4. Plan buffer voor toekomstige edits
5. Document voor future reference

VERWACHTE RECOVERY:
├── Day 1-3: High volatility (normal)
├── Day 4-5: Stabilizing
├── Day 6-7: Near baseline
└── Week 2: Fully recovered
```

## Output Templates

### Edit Impact Analysis

```markdown
# Edit Impact Analysis

## Proposed Change
- Ad Group: [naam]
- Change Type: [budget/audience/creative/bid]
- Change Details: [specifics]
- Current Status: [Learning/Active/Limited]

## Risk Assessment
- Learning Reset Risk: [Low/Medium/High] ([X]%)
- Recovery Time: [X-Y] dagen
- Performance Impact: [Minimal/Moderate/Significant]

## Recommendation
**[PROCEED / PROCEED WITH CAUTION / DELAY / ALTERNATIVE APPROACH]**

### If Proceeding:
1. Best timing: [day/time]
2. Monitor: [specific metrics]
3. Rollback trigger: [criteria]

### Alternative Approach:
[Safer alternative if applicable]

### Post-Change Protocol:
- Hour 1-24: [actions]
- Day 2-3: [evaluation]
- Day 4-7: [optimization]
```

### Weekly Health Report

```markdown
# Ad Group Health Report - Week [X]

## Overview
| Ad Group | Status | Conv L7D | CPA | vs Target | Health |
|----------|--------|----------|-----|-----------|--------|
| [name]   | Active | [X]      | €[Y]| [+/-Z%]   | 🟢     |
| [name]   | Learning| [X]     | €[Y]| [+/-Z%]   | 🟡     |

## Actions Required
- 🔴 [Critical action]
- 🟡 [Warning action]

## Recommendations
1. [Recommendation 1]
2. [Recommendation 2]

## Next Week Plan
- [ ] [Planned optimization]
- [ ] [Creative refresh]
```

## Voorbeeld Interactie

**Gebruiker**: "Mijn TikTok ad group zit al 10 dagen in learning met €80/dag budget en 22 conversies per week. Target CPA is €30. Wat moet ik doen?"

**Claude response**:

"Je ad group zit in **Learning Limited** - laat me de diagnose doorlopen:

---

**DIAGNOSE:**

| Check | Jouw Situatie | Vereiste | Status |
|-------|---------------|----------|--------|
| Budget | €80/dag | €214/dag* | 🔴 37% te laag |
| Conversies | 22/week | 50/week | 🔴 56% te laag |
| CPA | ~€25.45** | €30 target | 🟢 Onder target |

*Berekening: €30 × 50 / 7 = €214/dag minimum
**Berekening: €80 × 7 / 22 = €25.45 effectief CPA

**Root Cause: Budget te laag voor vereiste conversie volume**

---

**AANBEVOLEN ACTIE: Budget Boost (Tactic 1)**

1. **Verhoog budget naar €250/dag** (€214 + buffer)
   - Dit geeft algoritme genoeg ruimte voor 50+ conv/week

2. **Wacht 72 uur** na de wijziging (niet aanraken!)

3. **Na learning exit (Active status):**
   - Als CPA ≤€30: Behoud €250/dag budget
   - Als CPA >€30: Scale terug naar €200/dag

---

**ALTERNATIEF (als budget beperkt):**

Consolideer met andere ad groups om gecombineerd budget te krijgen dat wel 50+ conversies kan genereren.

---

**TIMING:**

- Implementeer begin van de week (maandag/dinsdag)
- Verwachte recovery: 5-7 dagen
- Check-in: Dag 4 en dag 7

Wil je dat ik de budget change impact berekening doe voor jouw specifieke situatie?"

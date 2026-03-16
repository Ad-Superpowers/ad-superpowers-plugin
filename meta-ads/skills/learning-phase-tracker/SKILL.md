---
name: learning-phase-tracker
description: "Meta Ads learning phase management en edit impact analyzer. Gebruik voor: (1) Learning phase status beoordelen, (2) Significant edits impact voorspellen, (3) Learning phase exit strategieen, (4) Budget change impact berekenen, (5) Ad set health checks. Triggers: learning phase, learning limited, significant edit, ad set stuck, exit learning, reset learning, edit impact."
---

# Learning Phase Tracker

Analyzer voor Meta Ads learning phase management. Voorspelt edit impact en adviseert over optimale timing voor wijzigingen.

## Learning Phase Basics

### Wat Is Learning Phase?

Periode waarin Meta's algoritme leert wie te targeten en hoe te bidden. Ad sets tonen "Learning" status tot voldoende data verzameld is.

### Exit Criteria (2025 Update)

```
Traditionele regel: 50 optimization events per ad set per week

2025 Update: Sommige accounts zien 10 conversies over 3 dagen
als nieuwe threshold (Meta test dit).

Praktische vuistregel: Plan voor 50/week, maar monitor
of snellere exit mogelijk is.
```

### Learning Phase Statuses

| Status | Betekenis | Actie |
|--------|-----------|-------|
| **Learning** | Algoritme verzamelt data | Niet wijzigen, wachten |
| **Active** | Exitied, optimalisatie stabiel | Monitor en optimize |
| **Learning Limited** | Onvoldoende events | Verhoog budget of broader targeting |

## Edit Impact Matrix

### Significant Edits (Trigger Learning Reset)

| Edit Type | Impact | Learning Reset? |
|-----------|--------|-----------------|
| Budget >20% increase | High | Meestal ja |
| Budget >20% decrease | High | Meestal ja |
| Audience change | High | Ja |
| New creative | High | Ja |
| Optimization goal change | High | Ja |
| Bid strategy change | High | Ja |
| Placement change | Medium | Vaak ja |

### Non-Significant Edits (Meestal Veilig)

| Edit Type | Impact | Learning Reset? |
|-----------|--------|-----------------|
| Budget <20% change | Low | Meestal nee |
| Ad name change | None | Nee |
| Campaign name change | None | Nee |
| Adding new ad (2025) | Variable | Soms niet meer |
| Minor copy tweak | Low | Meestal nee |

### 2025 Updates

Meta toont nu berichten zoals:
> "You can increase your budget to €[X] without restarting learning"

Dit geeft specifieke safe thresholds per ad set.

## Budget Change Impact Calculator

### Safe Budget Increase Zones

```
Current Daily Budget: €[X]
Learning Phase Status: [Learning/Active/Limited]

SAFE ZONE (No Reset):
├── Increase: Tot 20% (€[X × 1.2])
└── Decrease: Tot 20% (€[X × 0.8])

YELLOW ZONE (Possible Reset):
├── Increase: 20-50% (€[X × 1.2] - €[X × 1.5])
└── Decrease: 20-50%
└── Aanbeveling: Doe in 2 stappen over 3-4 dagen

RED ZONE (Likely Reset):
├── Increase: >50%
└── Decrease: >50%
└── Aanbeveling: Duplicate ad set met nieuwe budget
```

### Budget Change Decision Tree

```
Wil je budget verhogen?
│
├─► <20% increase
│   └─► Veilig, direct doorvoeren
│
├─► 20-50% increase
│   ├─► Ad set in Learning?
│   │   └─► Wacht tot Active, dan verhogen
│   └─► Ad set Active?
│       └─► Doe in 2 stappen (10% + 10%)
│
└─► >50% increase
    └─► Dupliceer ad set met nieuwe budget
        └─► Laat origineel draaien als backup
```

## Learning Phase Exit Strategies

### Snelle Exit Tactieken

```
Tactic 1: Budget Boost
├── Verhoog budget naar 3x CPA × 50 / 7 dagen
├── Voorbeeld: CPA €20 → Budget €429/week = €61/dag
└── Na exit: Terugschalen naar gewenst niveau

Tactic 2: Broader Targeting
├── Gebruik Advantage+ Audience
├── Verwijder interest restricties
├── Expand age ranges
└── Meer conversie opportunities = snellere learning

Tactic 3: Higher-Funnel Event
├── Tijdelijk optimaliseren voor AddToCart ipv Purchase
├── Meer events = snellere learning
├── Na exit: Switch terug naar Purchase
└── Let op: Kan traffic kwaliteit beïnvloeden

Tactic 4: Consolidatie
├── Merge small ad sets
├── Combineer budgets
├── Eén sterk ad set > meerdere zwakke
└── Aggregated data = snellere learning
```

### Learning Limited Oplossingen

```
Diagnose: Waarom Learning Limited?
│
├─► Budget te laag
│   └─► Verhoog tot €[CPA × 50 / 7] per dag
│
├─► Audience te klein
│   └─► Broader targeting of merge audiences
│
├─► Te weinig creatives
│   └─► Voeg meer ads toe (niet 1 ad per ad set)
│
├─► Event te zeldzaam
│   └─► Switch naar higher-funnel event
│
└─► Competition te hoog
    └─► Verhoog budget of adjust bid strategy
```

## Edit Timing Best Practices

### Wanneer Wijzigingen Doorvoeren

```
BESTE TIMING:
├── Begin van de week (maandag/dinsdag)
│   └─► Geeft algoritme weekdagen om te leren
│
├── Na stabiele 5-7 dagen performance
│   └─► Baseline data beschikbaar voor comparison
│
└── NIET tijdens:
    ├── Learning phase (wacht op exit)
    ├── Weekend (minder data)
    ├── Peak periods (Black Friday, etc.)
    └── Direct na vorige wijziging (<3 dagen)
```

### Batch Edits Strategy

```
Multiple edits nodig?
│
├─► Optie 1: Batch alle edits tegelijk
│   ├── Voordeel: Eén learning reset ipv meerdere
│   └─► Gebruik wanneer: Grote refresh/overhaul
│
└─► Optie 2: Staggered edits
    ├── Voordeel: Isoleer impact per change
    ├── Wacht 3-5 dagen tussen edits
    └─► Gebruik wanneer: Testing hypotheses
```

## Ad Set Health Check

### Quick Health Assessment

```
AD SET HEALTH CHECK

□ Learning Phase Status: [Learning/Active/Limited]
□ Days in current status: [X]
□ Conversions last 7 days: [X]
□ Daily budget: €[X]
□ Estimated CPA: €[X]
□ Frequency: [X]
□ CTR: [X]%
□ Delivery status: [Active/Limited/Off]

HEALTH SCORE:
├── Green (Healthy): Active + 50+ conv/week + Frequency <4
├── Yellow (Watch): Learning >7 days OF 25-50 conv/week
└── Red (Action needed): Limited OF <25 conv/week OF Frequency >5
```

### Recommended Actions by Status

```
STATUS: Learning (Normal)
├── Days in learning: <7
├── Action: Wacht, niet aanpassen
└── Check again: Na 7 dagen

STATUS: Learning (Extended)
├── Days in learning: >7
├── Action: Evaluate budget/audience/event
└── Consider: Tactic 1-4 van Exit Strategies

STATUS: Learning Limited
├── Action: Immediate intervention
├── Primary: Verhoog budget
├── Secondary: Broader audience
└── Tertiary: Higher-funnel event

STATUS: Active (Healthy)
├── Action: Monitor, geen wijzigingen nodig
├── Optimize: Test new creatives (add, don't replace)
└── Scale: 20% budget increase als performance stable

STATUS: Active (Declining)
├── Symptoms: Rising CPA, falling ROAS
├── Diagnose: Creative fatigue? Audience saturation?
├── Action: Refresh creatives, expand audience
└── Avoid: Major restructuring (resets learning)
```

## Edit Impact Simulator

### Input Template

```
CURRENT AD SET:
- Daily budget: €[X]
- Learning status: [Learning/Active/Limited]
- Days in status: [X]
- Conv. last 7 days: [X]
- Current CPA: €[X]

PROPOSED CHANGE:
- Change type: [budget/audience/creative/bid/event]
- Change details: [specifics]
```

### Output Template

```
EDIT IMPACT ANALYSIS

Proposed Change: [description]

RISK ASSESSMENT:
├── Learning Reset Risk: [Low/Medium/High]
├── Performance Impact: [Minimal/Moderate/Significant]
└── Recovery Time: [X] dagen

RECOMMENDATION:
[Proceed/Proceed with caution/Delay/Alternative approach]

ALTERNATIVE APPROACH (if risky):
[Safer alternative to achieve same goal]

TIMING ADVICE:
[When to implement if proceeding]

POST-CHANGE MONITORING:
- Day 1-3: [wat te monitoren]
- Day 4-7: [evaluatie criteria]
- Action triggers: [wanneer in te grijpen]
```

## Common Scenarios

### Scenario 1: Budget Verdubbelen

```
Situatie: Ad set performing well, wil budget 2x
Risico: High (>50% increase)

Aanbeveling:
1. Dupliceer ad set met 2x budget
2. Laat origineel draaien op huidig budget
3. Na 7 dagen: Evalueer welke beter performed
4. Pause de underperformer
```

### Scenario 2: Creative Refresh

```
Situatie: CTR dalend, wil alle ads vervangen
Risico: High (triggers reset)

Aanbeveling:
1. Voeg nieuwe ads toe aan bestaande ad set (niet vervangen)
2. Laat algoritme nieuwe vs oude testen
3. Pause underperformers na 5-7 dagen
4. Vermijd volledige creative swap
```

### Scenario 3: Audience Wijzigen

```
Situatie: Wil interest targeting toevoegen
Risico: High (audience change = reset)

Aanbeveling:
1. Maak nieuwe ad set met nieuwe audience
2. Laat origineel parallel draaien
3. Vergelijk performance na 7-14 dagen
4. Scale winner, pause loser
```

### Scenario 4: Stuck in Learning

```
Situatie: 14 dagen in Learning, geen progress
Diagnose: Budget €30/dag, CPA €25, 8 conv/week

Aanbeveling:
1. Verhoog budget naar €90/dag (€25 CPA × 50 / 7 × 0.5 buffer)
2. OF switch naar AddToCart event tijdelijk
3. OF merge met andere ad sets
4. Na exit: Optimaliseer terug naar gewenste setup
```

---
name: ab-test-planner
description: Ontwerp statisch significante A/B tests voor Meta Ads met correcte test setup, sample size berekeningen en analyse frameworks. Gebruik deze skill wanneer je een test wilt opzetten, resultaten wilt analyseren, of een testing roadmap wilt maken.
---

# A/B Test Planner

## Overview

Deze skill helpt bij het opzetten van statistically sound A/B tests in Meta Ads, inclusief hypothese formulering, test structuur, sample size calculaties en resultaat interpretatie voor betrouwbare optimalisatie beslissingen.

## A/B Testing Fundamentals

### Waarom A/B Testen in Meta Ads?

```
┌─────────────────────────────────────────────────────────────────┐
│  A/B TESTING vs "GEWOON DRAAIEN"                                │
│                                                                 │
│  Zonder A/B test:                                               │
│  ├── Algoritme kiest "winnaar" op basis van early signals       │
│  ├── Geen statistische zekerheid                                │
│  ├── Seasonal/timing effecten verwarren resultaten              │
│  └── Learnings niet reproduceerbaar                             │
│                                                                 │
│  Met A/B test:                                                  │
│  ├── Gelijke condities voor beide varianten                     │
│  ├── Statistische significantie (95%+ confidence)               │
│  ├── Geïsoleerde variabele = duidelijke learning                │
│  └── Reproduceerbare resultaten                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Meta's Native A/B Test Tool

```
LOCATIE: Ads Manager → Experiments → A/B Test

VOORDELEN:
├── Automatische audience split (geen overlap)
├── Statistische significantie berekening
├── Gecontroleerde test omgeving
└── Duidelijke winnaar declaratie

WANNEER GEBRUIKEN:
├── Creative testing (afbeelding A vs B)
├── Audience testing (LAL vs Interest)
├── Placement testing (Auto vs Manual)
└── Optimization goal testing
```

## Hypothese Framework

### SMART Hypothese Formuleren

```
HYPOTHESE STRUCTUUR:
"Als we [VARIABELE] veranderen van [A] naar [B],
dan verwachten we dat [METRIC] met [X%] verbetert,
omdat [RATIONALE]."

VOORBEELD:
"Als we de video hook veranderen van 'product-first' naar
'problem-first', dan verwachten we dat de View Rate (3 sec)
met 15% verbetert, omdat mensen eerst hun probleem herkennen
voordat ze geïnteresseerd zijn in de oplossing."
```

### Goede vs Slechte Hypotheses

| ❌ Slecht | ✅ Goed |
|-----------|---------|
| "Ik denk dat versie B beter werkt" | "Versie B (met social proof) verhoogt CTR met 10% vs versie A (zonder)" |
| "We testen nieuwe creative" | "UGC-style creative verlaagt CPA met 15% vs studio creative" |
| "Laten we audiences vergelijken" | "LAL 1% purchasers heeft 20% lagere CPA dan Interest targeting" |

## Test Prioritering Framework

### ICE Score Methode

```
PRIORITERING FORMULE:
ICE Score = (Impact + Confidence + Ease) / 3

IMPACT (1-10):
├── Hoeveel invloed op resultaat?
├── 10 = Core element (hook, offer)
└── 1 = Minor detail (button kleur)

CONFIDENCE (1-10):
├── Hoe zeker ben je van verbetering?
├── 10 = Data/research ondersteund
└── 1 = Pure gok

EASE (1-10):
├── Hoe makkelijk uit te voeren?
├── 10 = Copy wijziging
└── 1 = Hele video opnieuw maken
```

### Test Prioriteit Matrix

```
PRIORITEIT  │ WAT TESTEN                    │ ICE
────────────┼───────────────────────────────┼─────
🔴 HOOG     │ Video hook (eerste 3 sec)     │ 9.0
🔴 HOOG     │ Headline                       │ 8.5
🔴 HOOG     │ Offer/aanbieding              │ 8.5
🟡 MEDIUM   │ Primary text lengte           │ 7.0
🟡 MEDIUM   │ CTA button                    │ 6.5
🟡 MEDIUM   │ Afbeelding stijl              │ 6.5
🟢 LAAG     │ Beschrijving tekst            │ 5.0
🟢 LAAG     │ Emoji gebruik                 │ 4.5
⚪ SKIP     │ Button kleur                  │ 2.0
```

## Test Types & Setup

### Type 1: Creative Test

```
DOEL: Welke creative presteert beter?
VARIABELE: Afbeelding, video, of carousel

SETUP IN META:
├── Campaign: [Bestaande campagne]
├── Test Type: Creative
├── Varianten: 2-5 creatives
├── Metric: CTR, CPA, of ROAS
├── Budget Split: Equal (50/50 voor 2 varianten)
└── Duration: Min. 7 dagen

VOORBEELD:
├── Variant A: Product lifestyle foto
├── Variant B: Product op witte achtergrond
├── Variant C: UGC-style foto
└── Primary Metric: CTR (of Purchase CPA)
```

### Type 2: Audience Test

```
DOEL: Welke audience heeft beste CPA/ROAS?
VARIABELE: Targeting

SETUP IN META:
├── Campaign: Nieuwe test campaign
├── Test Type: Audience
├── Varianten: 2 audiences
├── Creative: ZELFDE voor beide (!)
├── Budget: Gelijk per variant
└── Duration: Min. 14 dagen (meer data nodig)

VOORBEELD:
├── Variant A: LAL 1% Purchasers
├── Variant B: Interest Stack "Fitness"
├── Control: Zelfde creative set
└── Primary Metric: CPA of ROAS
```

### Type 3: Placement Test

```
DOEL: Auto placements vs Manual?
VARIABELE: Waar ads getoond worden

SETUP IN META:
├── Campaign: Test campaign
├── Test Type: Placement
├── Varianten:
│   ├── A: Advantage+ Placements (auto)
│   └── B: Manual (bijv. Feed + Stories only)
├── Creative: Zelfde
└── Duration: 14 dagen

WANNEER RELEVANT:
├── Je vermoedt Audience Network verspilt budget
├── Je wilt Stories performance isoleren
└── Nieuw account zonder placement data
```

## Sample Size & Duration Calculator

### Minimum Test Duration

```
VUISTREGEL:
├── Minimaal 7 dagen (om dag-variatie te dekken)
├── Minimaal 100 conversies per variant
├── Of minimaal 1000 clicks per variant (voor CTR tests)
└── Statistische significantie >90% bereikt

CALCULATOR INPUTS:
├── Baseline conversion rate: [X%]
├── Minimum detectable effect: [Y%]
├── Statistical significance: 95%
├── Power: 80%
└── Daily traffic/conversions: [Z]
```

### Quick Reference Table

| Test Type | Min. per Variant | Aanbevolen Duration |
|-----------|------------------|---------------------|
| CTR Test | 1.000 clicks | 7-10 dagen |
| Conversion Test | 100 conversies | 14-21 dagen |
| ROAS Test | 100 purchases | 14-28 dagen |
| Audience Test | 200 conversies | 21-30 dagen |

### Wanneer Test Beëindigen?

```
✅ BEËINDIG ALS:
├── 95%+ statistische significantie bereikt
├── Beide varianten >100 conversies hebben
├── Test minimaal 7 dagen gedraaid heeft
└── Geen grote externe factoren (feestdagen, etc.)

❌ BEËINDIG NIET ALS:
├── <90% significantie (tenzij budget op)
├── <50 conversies per variant
├── <7 dagen gedraaid
└── Tijdens abnormale periode (Black Friday, etc.)
```

## Test Structuur Templates

### Single Variable Test Template

```
A/B TEST PLAN
=============

📋 TEST INFO:
├── Test Naam: [Beschrijvende naam]
├── Hypothese: [SMART hypothese]
├── Start Datum: [Datum]
└── Verwachte Einddatum: [Datum]

🎯 TEST DETAILS:
├── Type: [Creative / Audience / Placement]
├── Variabele: [Wat testen we]
├── Primary Metric: [CPA / CTR / ROAS]
└── Secondary Metrics: [CTR, Frequency, etc.]

📊 VARIANTEN:
├── Variant A (Control): [Beschrijving]
└── Variant B (Test): [Beschrijving]

💰 BUDGET:
├── Totaal Test Budget: €[X]
├── Per Variant: €[X/2]
└── Dagbudget per Variant: €[X]

⏱️ DURATION & SAMPLE SIZE:
├── Minimum Duration: [X] dagen
├── Target Conversies per Variant: [X]
└── Stop Criterium: 95% significantie OF [datum]

📈 SUCCESS CRITERIA:
├── Winnaar als: [Metric] verschil >10%
├── Met: >95% statistische significantie
└── Decision: [Wat doen we met winnaar?]
```

## Resultaat Analyse Framework

### Interpretatie Guide

```
RESULTAAT SCENARIO'S:

SCENARIO 1: Duidelijke winnaar (>95% sig, >15% verschil)
├── Actie: Implementeer winnaar
├── Learning: Documenteer waarom het werkte
└── Next: Test volgende variabele

SCENARIO 2: Marginale winnaar (90-95% sig, 5-15% verschil)
├── Actie: Overweeg meer data verzamelen
├── Learning: Verschil mogelijk echt maar klein
└── Next: Implementeer of hertest met groter budget

SCENARIO 3: Geen winnaar (<90% sig)
├── Actie: Geen wijziging doorvoeren
├── Learning: Variabele maakt geen verschil
└── Next: Test grotere/andere wijziging

SCENARIO 4: Verrassende verliezer (jouw favoriete versie verliest)
├── Actie: Implementeer de winnaar (data > gevoel!)
├── Learning: Documenteer het verschil
└── Next: Onderzoek WAAROM verwachting fout was
```

### Post-Test Documentatie

```
TEST RESULTATEN RAPPORT
=======================

📋 TEST: [Naam]
📅 Periode: [Start] - [Eind]

📊 RESULTATEN:

Metric          │ Variant A │ Variant B │ Verschil
────────────────┼───────────┼───────────┼──────────
Impressions     │  50.000   │  50.000   │    0%
Clicks          │   2.500   │   3.000   │  +20%
CTR             │   5.0%    │   6.0%    │  +20%
Conversions     │    125    │    150    │  +20%
CPA             │  €20.00   │  €16.67   │  -17%
ROAS            │   2.5x    │   3.0x    │  +20%

📈 STATISTISCHE SIGNIFICANTIE: [X%]

🏆 WINNAAR: Variant [A/B]

💡 KEY LEARNINGS:
├── [Learning 1]
├── [Learning 2]
└── [Learning 3]

▶️ NEXT STEPS:
├── [Actie 1]
├── [Actie 2]
└── [Volgende test]
```

## Testing Roadmap Template

### Quarterly Testing Calendar

```
Q[X] TESTING ROADMAP
====================

MAAND 1:
├── Week 1-2: Creative Test - Hook variaties
├── Week 3-4: Creative Test - Format (video vs static)
└── Learnings toepassen

MAAND 2:
├── Week 1-2: Audience Test - LAL vs Interest
├── Week 3-4: Copy Test - Lang vs kort
└── Learnings toepassen

MAAND 3:
├── Week 1-2: Offer Test - % korting vs € korting
├── Week 3-4: Winning combo test
└── Quarter review & planning

PRIORITEIT VOLGORDE:
1. Hook/eerste indruk (hoogste impact)
2. Offer/value proposition
3. Audience targeting
4. Copy elementen
5. Technische optimalisaties
```

## Voorbeeld Interactie

**Gebruiker**: "Ik wil testen of UGC-style video's beter werken dan mijn huidige studio content. Hoe zet ik dit het beste op?"

**Claude response**:

"Goede test! Hier is je A/B test plan:

---

**A/B TEST PLAN: UGC vs Studio Content**

**📋 HYPOTHESE:**
'Als we UGC-style video's gebruiken i.p.v. studio content, dan verwachten we dat de CPA met 20% daalt, omdat UGC authentieker overkomt en beter past bij social media gedrag.'

**🎯 TEST SETUP:**

| Element | Details |
|---------|---------|
| Type | Creative Test |
| Platform | Meta Ads A/B Test tool |
| Variabele | Video style |
| Control (A) | Huidige studio video |
| Test (B) | UGC-style video |

**⚠️ BELANGRIJK: Houd constant:**
- Zelfde boodschap/script strekking
- Zelfde offer/CTA
- Zelfde audience
- Zelfde budget split

**💰 BUDGET & DURATION:**
- Minimaal €500 per variant (€1000 totaal)
- Minimaal 14 dagen
- Doel: 100+ conversies per variant

**📊 METRICS:**
- Primary: CPA (Cost per Acquisition)
- Secondary: CTR, Hook Rate (3 sec views), ThruPlay Rate

**✅ SUCCESS CRITERIA:**
- Winnaar bij >95% significantie
- Minimum 15% verschil in CPA
- Beide >100 conversies

---

**Wil je dat ik ook een UGC script schrijf dat je kunt testen?**"

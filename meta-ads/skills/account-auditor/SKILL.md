---
name: account-auditor
description: Voer complete Meta Ads account audits uit met gestructureerde checklists, health scores en actionable aanbevelingen. Gebruik deze skill wanneer je een nieuw account overneemt, periodieke reviews doet, of performance problemen wilt diagnosticeren.
---

# Account Auditor

## Overview

Deze skill biedt een systematisch framework voor het uitvoeren van complete Meta Ads account audits, inclusief health scoring, issue identificatie en geprioriteerde aanbevelingen voor optimalisatie.

## Audit Framework

### Audit Scope Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  META ADS ACCOUNT AUDIT GEBIEDEN                                │
│                                                                 │
│  1. TRACKING & DATA QUALITY                                     │
│     └── Pixel, CAPI, Events, Attribution                        │
│                                                                 │
│  2. ACCOUNT STRUCTURE                                           │
│     └── Campaigns, Ad Sets, Ads, Naming                         │
│                                                                 │
│  3. AUDIENCE STRATEGY                                           │
│     └── Custom, Lookalike, Targeting, Exclusions                │
│                                                                 │
│  4. CREATIVE PERFORMANCE                                        │
│     └── Formats, Fatigue, Testing, Diversity                    │
│                                                                 │
│  5. BUDGET & BIDDING                                            │
│     └── Allocation, Strategy, Efficiency                        │
│                                                                 │
│  6. PERFORMANCE METRICS                                         │
│     └── KPIs, Trends, Benchmarks                                │
│                                                                 │
│  7. COMPLIANCE & SETTINGS                                       │
│     └── Policies, Settings, Access                              │
└─────────────────────────────────────────────────────────────────┘
```

## Complete Audit Checklist

### Section 1: Tracking & Data Quality

```
TRACKING AUDIT
==============

□ PIXEL STATUS
├── Is pixel geïnstalleerd en actief?
├── Pixel ID correct in alle relevante domains?
├── Test events in Events Manager
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ CONVERSIONS API (CAPI)
├── Is CAPI geïmplementeerd?
├── Event Match Quality score (doel: >6.0)
├── Deduplicatie correct ingesteld?
├── Welke parameters worden gestuurd?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ EVENT TRACKING
├── Welke events zijn actief?
├── Vuren events correct? (test conversies)
├── Zijn er custom events nodig?
├── Value tracking voor purchases?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ DOMAIN VERIFICATION
├── Is domein geverifieerd?
├── Aggregated Event Measurement (AEM) ingesteld?
├── Event prioritering correct?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

TRACKING SCORE: ___/40 punten
```

### Section 2: Account Structure

```
STRUCTUUR AUDIT
===============

□ CAMPAIGN ORGANISATIE
├── Hoeveel actieve campagnes? (Ideaal: 3-8)
├── Duidelijke funnel segmentatie? (TOFU/MOFU/BOFU)
├── Logische campaign objectives?
├── Geen duplicate campagnes?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ AD SET STRUCTUUR
├── Aantal ad sets per campaign (Ideaal: 2-5)
├── Voldoende budget per ad set voor learning?
├── Geen overlappende audiences?
├── Logische audience segmentatie?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ ADS ORGANISATIE
├── Aantal ads per ad set (Ideaal: 3-6)
├── Creative diversiteit aanwezig?
├── Geen duplicate ads?
├── DCO/Advantage+ correct gebruikt?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ NAMING CONVENTIONS
├── Consistent naming systeem?
├── Bevat campaign: objective, funnel, date?
├── Bevat ad set: audience type?
├── Bevat ad: creative type, version?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

STRUCTUUR SCORE: ___/40 punten
```

### Section 3: Audience Strategy

```
AUDIENCE AUDIT
==============

□ CUSTOM AUDIENCES
├── Welke custom audiences bestaan?
├── Zijn ze up-to-date (recent data)?
├── Minimum grootte bereikt? (>1000)
├── Source quality assessment
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ LOOKALIKE AUDIENCES
├── Welke LALs zijn actief?
├── Source audience quality?
├── Percentage selectie passend?
├── Worden value-based LALs gebruikt?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ INTEREST/BEHAVIOR TARGETING
├── Relevantie van geselecteerde interests?
├── Audience size niet te breed/smal?
├── Worden Advantage+ audiences gebruikt?
├── Testing van nieuwe interests?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ EXCLUSIONS
├── Worden kopers ge-excludeerd waar nodig?
├── Funnel-based exclusions actief?
├── Audience overlap minimized?
├── Geen conflicterende exclusions?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

AUDIENCE SCORE: ___/40 punten
```

### Section 4: Creative Performance

```
CREATIVE AUDIT
==============

□ FORMAT DIVERSITEIT
├── Mix van video, static, carousel?
├── Verschillende aspect ratios (1:1, 4:5, 9:16)?
├── UGC vs produced content balance?
├── Stories/Reels-specifieke creative?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ CREATIVE HEALTH
├── Gemiddelde leeftijd actieve creatives?
├── CTR trend (stijgend/dalend)?
├── Frequency per creative?
├── Creative fatigue signalen?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ MESSAGING & COPY
├── Duidelijke value proposition?
├── Strong hooks (eerste 3 sec)?
├── Variatie in copy angles?
├── CTA's duidelijk en consistent?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ TESTING CADENCE
├── Worden nieuwe creatives getest?
├── A/B testing actief?
├── Duidelijke test hypotheses?
├── Learnings gedocumenteerd?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

CREATIVE SCORE: ___/40 punten
```

### Section 5: Budget & Bidding

```
BUDGET AUDIT
============

□ BUDGET ALLOCATIE
├── Budget verdeling over funnel?
├── Geen ad sets onder minimum budget?
├── Budget aligned met goals?
├── Pacing correct (daily vs lifetime)?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ BID STRATEGY
├── Welke bid strategies in gebruik?
├── Passend bij campaign objectives?
├── Cost caps realistisch?
├── ROAS targets haalbaar?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ BUDGET EFFICIENCY
├── Spend vs budget ratio?
├── Worden budgetten volledig besteed?
├── ROI per campaign/funnel fase?
├── Identificatie van budget waste?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ SCALING POTENTIAL
├── Winnende ad sets met scale ruimte?
├── Headroom in audiences?
├── Budget increase history succesvol?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

BUDGET SCORE: ___/40 punten
```

### Section 6: Performance Review

```
PERFORMANCE AUDIT
=================

□ KEY METRICS (vs benchmarks)
├── CPA: €___ (benchmark: €___)
├── ROAS: ___ (benchmark: ___)
├── CTR: ___% (benchmark: ___%)
├── CPM: €___ (benchmark: €___)
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ TREND ANALYSIS (Last 30 days)
├── CPA trend: [↑ / → / ↓]
├── ROAS trend: [↑ / → / ↓]
├── Volume trend: [↑ / → / ↓]
├── Efficiency trend: [↑ / → / ↓]
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ FUNNEL METRICS
├── TOFU: Reach, CPM, Video Views
├── MOFU: CTR, CPC, Engagement
├── BOFU: CPA, ROAS, Conv Rate
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

□ LEARNING PHASE STATUS
├── % ad sets in learning?
├── Gemiddelde tijd in learning?
├── Learning phase success rate?
└── Score: [🟢 OK / 🟡 Issues / 🔴 Kritiek]

PERFORMANCE SCORE: ___/40 punten
```

### Section 7: Unused Feature Detection (NEW)

```
UNUSED FEATURES AUDIT
=====================
⚡ This section identifies money left on the table - features that are
   available but not being used, representing optimization opportunities.

□ ADVANTAGE+ FEATURES (Underutilized?)
├── Advantage+ Shopping Campaigns (ASC)
│   └── E-commerce account with €5k+/month? ASC not active?
│       → Potential: 10-20% ROAS improvement
├── Advantage+ Placements
│   └── Manual placements only? Missing reach opportunities
│       → Potential: 15-30% more reach at same cost
├── Advantage Detailed Targeting
│   └── Disabled? AI audience expansion not working
│       → Potential: 10-15% more conversions
├── Advantage+ Creative
│   └── Not using? Missing creative optimization
│       → Potential: 5-10% CTR improvement
└── Score: [🟢 Using / 🟡 Partially / 🔴 Not Using]

□ CONVERSIONS API (CAPI) - Enabled but Low Volume?
├── CAPI enabled but <50% of events from server?
│   └── Missing: Better attribution, lower CPM
├── Only PageView sent? Missing Add-to-Cart, Purchase?
│   └── Missing: Conversion signal strength
├── Event Match Quality <6.0?
│   └── Missing: Full CAPI value (poor matching)
└── Score: [🟢 OK / 🟡 Partial / 🔴 Not Optimized]

□ AUDIENCE ASSETS (Created but Not Used?)
├── Custom Audiences uploaded but not in active ad sets?
│   └── Wasted asset: Customer data not being leveraged
├── Lookalike Audiences created but inactive?
│   └── Wasted asset: Expansion opportunities unused
├── Value-based Lookalikes available but not used?
│   └── Missing: Higher-value customer targeting
├── Website remarketing lists exist but no retargeting campaigns?
│   └── Wasted: Warm audiences not being targeted
└── Score: [🟢 Using All / 🟡 Partially / 🔴 Many Unused]

□ CATALOG & SHOPPING FEATURES (E-commerce)
├── Catalog connected but no Dynamic Ads?
│   └── Missing: Personalized product recommendations
├── Advantage+ Catalog Ads not enabled?
│   └── Missing: Automated creative optimization
├── Collection Ads not tested?
│   └── Missing: Mobile shopping experience
├── Collaborative Ads available (retailer) but not used?
│   └── Missing: Partner reach
└── Score: [🟢 OK / 🟡 Partial / 🔴 Underutilized]

□ AUTOMATION & RULES (Not Configured?)
├── No automated rules for budget/bid management?
│   └── Missing: Proactive management, less manual work
├── No campaign budget optimization (CBO)?
│   └── Missing: Automated budget allocation
├── No cost caps or bid caps when needed?
│   └── Risk: Uncontrolled spending
├── No scheduled ad set rules (day/time)?
│   └── Missing: Performance optimization by schedule
└── Score: [🟢 Using / 🟡 Basic / 🔴 None]

□ MEASUREMENT & ATTRIBUTION (Not Set Up?)
├── Conversion Lift studies available but not run?
│   └── Missing: True incrementality data
├── Brand Lift studies available but not used?
│   └── Missing: Brand impact measurement
├── A/B testing (Experiments) not used?
│   └── Missing: Statistical testing framework
├── Attribution comparison report not reviewed?
│   └── Missing: Understanding of attribution impact
└── Score: [🟢 Using / 🟡 Basic / 🔴 None]

UNUSED FEATURES SCORE: ___/60 punten

⚠️ OPPORTUNITY COST ESTIMATE:
├── Each unused Advantage+ feature: ~€500-2000/month missed
├── Low CAPI adoption: ~15-25% higher CPMs
├── Unused audiences: ~20-30% efficiency loss
├── No automation: ~2-5 hours/week manual work
└── TOTAL ESTIMATED OPPORTUNITY: €___/month
```

## Health Score Calculator

### Score Interpretatie

```
ACCOUNT HEALTH SCORE
====================

SECTIE               │ MAX PUNTEN │ JOUW SCORE
─────────────────────┼────────────┼───────────
Tracking & Data      │     40     │    ___
Account Structure    │     40     │    ___
Audience Strategy    │     40     │    ___
Creative Performance │     40     │    ___
Budget & Bidding     │     40     │    ___
Performance Metrics  │     40     │    ___
Unused Features      │     60     │    ___    ← NEW
─────────────────────┼────────────┼───────────
TOTAAL               │    300     │    ___

SCORE INTERPRETATIE:
├── 250-300: 🟢 Excellent - Minor optimizations
├── 200-249: 🟡 Good - Several improvements needed
├── 150-199: 🟠 Fair - Significant work required
└── <150:    🔴 Poor - Major restructuring needed
```

## Issue Prioritization Matrix

### Categoriseer gevonden issues:

```
ISSUE PRIORITERING
==================

🔴 KRITIEK (Fix binnen 24 uur):
├── Tracking niet werkend
├── Geen conversies trackend
├── Budget volledig gestopt
├── Policy violations
└── Major data discrepancies

🟠 HOOG (Fix binnen 1 week):
├── Slechte EMQ score (<5)
├── Hoge audience overlap (>50%)
├── Creative fatigue (CTR <0.5%)
├── CPA >50% boven target
└── Learning phase failures

🟡 MEDIUM (Fix binnen 2 weken):
├── Naming conventions inconsistent
├── Ad set consolidatie nodig
├── Audience refresh nodig
├── Budget reallocation nodig
└── Missing exclusions

🟢 LAAG (Fix binnen 1 maand):
├── Nice-to-have optimizations
├── Testing opportunities
├── Documentatie updates
└── Minor structural changes
```

## Audit Report Template

### Wanneer de gebruiker vraagt om een account audit:

```
ACCOUNT AUDIT RAPPORT
=====================

📅 Audit Datum: [DATUM]
🏢 Account: [ACCOUNT NAAM]
👤 Auditor: Claude AI

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 EXECUTIVE SUMMARY
────────────────────
Account Health Score: [X]/240 ([STATUS])

Top 3 Sterke Punten:
1. [Sterk punt]
2. [Sterk punt]
3. [Sterk punt]

Top 3 Verbeterpunten:
1. [Verbeterpunt]
2. [Verbeterpunt]
3. [Verbeterpunt]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 GEDETAILLEERDE BEVINDINGEN
─────────────────────────────

1. TRACKING & DATA
   Status: [🟢/🟡/🔴]
   Issues: [Lijst]
   Aanbevelingen: [Lijst]

2. ACCOUNT STRUCTURE
   Status: [🟢/🟡/🔴]
   Issues: [Lijst]
   Aanbevelingen: [Lijst]

[...etc voor alle secties...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 ACTIEPLAN (Geprioriteerd)
────────────────────────────

WEEK 1 (Kritiek):
□ [Actie 1]
□ [Actie 2]

WEEK 2-3 (Hoog):
□ [Actie 3]
□ [Actie 4]

MAAND 1 (Medium):
□ [Actie 5]
□ [Actie 6]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 VERWACHTE IMPACT
───────────────────
Na implementatie verwachten we:
├── CPA: [X%] verbetering
├── ROAS: [X%] verbetering
└── Efficiency: [X%] verbetering
```

## Quick Audit Checklist

### Voor snelle health check:

```
QUICK AUDIT (15 minuten)
========================

□ Pixel actief? (Events Manager → Test Events)
□ Conversies laatste 7 dagen? (ja/nee/hoeveel)
□ Learning phase issues? (% in learning)
□ CPA vs target? (onder/op/boven)
□ Frequentie <3? (ja/nee)
□ CTR >1%? (ja/nee)
□ Active creatives >3 per ad set? (ja/nee)
□ Budget fully spending? (ja/nee)

QUICK SCORE: ___/8
└── 7-8: Gezond account
└── 5-6: Aandacht nodig
└── <5: Diepgaande audit nodig
```

## Voorbeeld Interactie

**Gebruiker**: "Ik heb net een nieuw account overgenomen. Kun je me helpen met een audit?"

**Claude response**:

"Ik help je met een systematische account audit. Laten we beginnen:

---

**STAP 1: Basis Info Verzamelen**

Kun je me het volgende vertellen:
1. Wat is de branche/industry?
2. Wat is het maandelijkse advertentiebudget?
3. Wat zijn de huidige KPI targets (CPA/ROAS)?
4. Sinds wanneer draait het account?

---

**STAP 2: Controleer deze punten in Ads Manager**

**Tracking Check:**
- [ ] Ga naar Events Manager → Data Sources
- [ ] Is de pixel actief (groen)?
- [ ] Wat is de EMQ score voor Purchase event?

**Structure Check:**
- [ ] Hoeveel actieve campagnes zijn er?
- [ ] Zijn er campagnes met >10 ad sets?
- [ ] Hoeveel ads zijn actief totaal?

**Performance Check (Last 7 days):**
- [ ] Totaal spend: €___
- [ ] Totaal conversies: ___
- [ ] CPA: €___
- [ ] ROAS: ___

---

Deel deze info en ik genereer een complete audit met health score en actieplan!"

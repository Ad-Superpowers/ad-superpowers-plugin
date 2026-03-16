---
name: linkedin-benchmark-database
description: "Referentiedatabase met industry benchmarks voor LinkedIn Ads metrics per branche, campagnetype en funnel fase. Gebruik deze skill wanneer je wilt weten of je LinkedIn metrics goed presteren of wanneer je targets moet bepalen. Triggers: linkedin benchmark, linkedin CPL, linkedin CTR, linkedin CPC, is my CPL good, linkedin average, B2B benchmark."
---

# LinkedIn Ads Benchmark Database

## Overview

Deze skill biedt een uitgebreide database met LinkedIn Ads benchmarks per industrie, ad format, funnel fase en campagnetype, zodat je kunt beoordelen hoe je B2B metrics presteren ten opzichte van marktstandaarden.

## Benchmark Disclaimer

```
⚠️ BELANGRIJKE CONTEXT

Deze benchmarks zijn gebaseerd op:
├── Geaggregeerde industry data (2024-2026)
├── Bronnen: LinkedIn, AdBacklog, GrackerAI, Factors.ai
├── Primair gericht op West-Europese/Noord-Amerikaanse markten
└── B2B focus (LinkedIn's kernmarkt)

Benchmarks zijn RICHTLIJNEN, geen absolute waarheden:
├── Jouw specifieke niche kan significant afwijken
├── Enterprise vs SMB heeft enorme impact
├── Sales cycle length beïnvloedt CPL acceptatie
└── Altijd vergelijken met je eigen LTV:CAC ratio
```

## CPL Benchmarks by Industry

```
COST PER LEAD (CPL) BY INDUSTRY
===============================

Industry              │ Poor    │ Average │ Good    │ Excellent
──────────────────────┼─────────┼─────────┼─────────┼──────────
Finance & Insurance   │ >€120   │ €90-120 │ €60-90  │ <€60
Healthcare            │ >€150   │ €100-150│ €70-100 │ <€70
SaaS / Software       │ >€120   │ €80-120 │ €50-80  │ <€50
Education             │ >€80    │ €60-80  │ €40-60  │ <€40
Marketing / Agencies  │ >€120   │ €80-120 │ €50-80  │ <€50
Professional Services │ >€100   │ €70-100 │ €45-70  │ <€45
Manufacturing         │ >€130   │ €90-130 │ €60-90  │ <€60
Technology (Hardware) │ >€140   │ €100-140│ €65-100 │ <€65
Consulting            │ >€110   │ €75-110 │ €50-75  │ <€50
Recruitment / HR Tech │ >€90    │ €60-90  │ €40-60  │ <€40

CONTEXTFACTOREN:
├── Enterprise deals (€50k+ ACV): CPL €150-300+ acceptabel
├── SMB deals (€5k ACV): CPL <€50 target
├── Freemium SaaS: CPL <€30 ideal
└── High-touch sales: Hogere CPL OK als SQL rate hoog
```

## CPC & CPM Benchmarks

```
COST PER CLICK (CPC) BY INDUSTRY
================================

Industry              │ Poor    │ Average │ Good    │ Excellent
──────────────────────┼─────────┼─────────┼─────────┼──────────
Finance & Insurance   │ >€8.00  │ €5-8    │ €3-5    │ <€3.00
SaaS / Software       │ >€10.00 │ €6-10   │ €4-6    │ <€4.00
Technology            │ >€9.00  │ €5-9    │ €3-5    │ <€3.00
Healthcare            │ >€7.00  │ €4-7    │ €2.50-4 │ <€2.50
Education             │ >€6.00  │ €3.50-6 │ €2-3.50 │ <€2.00
Manufacturing         │ >€7.50  │ €4.50-7.5│€3-4.50 │ <€3.00
Professional Services │ >€6.50  │ €4-6.50 │ €2.50-4 │ <€2.50
General B2B           │ >€7.00  │ €4-7    │ €2.50-4 │ <€2.50

NOTES:
├── LinkedIn CPC is 3-5x hoger dan Meta/Google
├── Maar: B2B audience quality compenseert vaak
└── Focus op CPL/CPA, niet alleen CPC
```

```
COST PER MILLE (CPM) BY TARGETING
=================================

Targeting Type         │ Range
───────────────────────┼────────────
Broad Professional     │ €25-35
Job Title Targeting    │ €35-50
Job Function           │ €30-45
Industry + Seniority   │ €40-60
Matched Audiences      │ €20-30
Lookalike Audiences    │ €25-40
ABM / Account Lists    │ €50-80
C-Suite Only           │ €60-100

CONTEXTFACTOREN:
├── US/UK markets: +20-30% vs EU
├── Small audiences (<50k): Premium pricing
└── Q4: +15-25% seasonal increase
```

## CTR Benchmarks by Ad Format

```
CLICK-THROUGH RATE (CTR) BY FORMAT
==================================

Ad Format               │ Poor    │ Average │ Good    │ Excellent
────────────────────────┼─────────┼─────────┼─────────┼──────────
Sponsored Content       │ <0.35%  │ 0.35-0.55%│0.55-0.80%│ >0.80%
Video Ads               │ <0.30%  │ 0.30-0.45%│0.45-0.65%│ >0.65%
Carousel Ads            │ <0.40%  │ 0.40-0.60%│0.60-0.90%│ >0.90%
Message Ads (InMail)    │ <2.00%  │ 2.00-3.50%│3.50-5.00%│ >5.00%
Text Ads                │ <0.015% │ 0.015-0.03%│0.03-0.05%│>0.05%
Dynamic Ads             │ <0.05%  │ 0.05-0.10%│0.10-0.20%│ >0.20%
Lead Gen Forms (CVR)    │ <6%     │ 6-10%    │ 10-15%  │ >15%

NOTES:
├── Message Ads: Hogere CTR maar beperkt volume
├── Lead Gen Forms: Meet CVR (form completion), niet CTR
├── Video: Focus op View Rate (25/50/75% completion)
└── Carousel: Swipe rate 30-50% = healthy
```

## Conversion Rate Benchmarks by Funnel Stage

```
CONVERSION RATE BY FUNNEL STAGE
===============================

Funnel Stage           │ Poor    │ Average │ Good    │ Excellent
───────────────────────┼─────────┼─────────┼─────────┼──────────
TOFU (Awareness)
├── Video View Rate    │ <15%    │ 15-25%  │ 25-40%  │ >40%
├── Engagement Rate    │ <0.5%   │ 0.5-1%  │ 1-2%    │ >2%
└── Brand Lift         │ <3%     │ 3-8%    │ 8-15%   │ >15%

MOFU (Consideration)
├── Landing Page CVR   │ <2%     │ 2-4%    │ 4-6%    │ >6%
├── Content Download   │ <4%     │ 4-8%    │ 8-12%   │ >12%
└── Webinar Signup     │ <3%     │ 3-6%    │ 6-10%   │ >10%

BOFU (Conversion)
├── Demo Request       │ <1.5%   │ 1.5-3%  │ 3-5%    │ >5%
├── Free Trial         │ <2%     │ 2-4%    │ 4-7%    │ >7%
└── Contact Form       │ <1%     │ 1-2.5%  │ 2.5-4%  │ >4%
```

## Lead Gen Forms vs Landing Pages

```
LEAD GEN FORMS vs LANDING PAGES
===============================

Metric                  │ Lead Gen Forms │ Landing Pages
────────────────────────┼────────────────┼───────────────
Conversion Rate         │ 10-13%         │ 4-6%
Cost per Lead           │ 15-25% lower   │ Higher
SQL Rate (quality)      │ 20-40% lower   │ Higher
Mobile Experience       │ Excellent      │ Variable
Form Fields Limit       │ Up to 12       │ Unlimited
Custom Validation       │ Limited        │ Full control
Retargeting Data        │ Limited        │ Full pixel

WHEN TO USE WHAT:

LEAD GEN FORMS (Native)
├── High-volume lead generation
├── Mobile-first audience
├── Simple qualification (job title, company)
├── TOFU/MOFU content offers
└── Lower friction = higher volume, lower quality

LANDING PAGES
├── Complex qualification needed
├── Multi-step forms
├── Custom validation rules
├── BOFU demo/trial requests
└── Higher friction = lower volume, higher quality

HYBRID APPROACH (Best Practice)
├── Use Lead Gen Forms for initial capture
├── Add 1-2 qualifying questions to filter
├── Retarget form submitters with LP ads
└── Measure SQL rate, not just lead volume
```

## SQL Rate & Pipeline Benchmarks

```
LEAD QUALITY BENCHMARKS
=======================

Metric                  │ Poor    │ Average │ Good    │ Excellent
────────────────────────┼─────────┼─────────┼─────────┼──────────
MQL to SQL Rate         │ <10%    │ 10-20%  │ 20-35%  │ >35%
SQL to Opportunity      │ <20%    │ 20-35%  │ 35-50%  │ >50%
Opportunity to Close    │ <15%    │ 15-25%  │ 25-40%  │ >40%
Lead Gen Form SQL Rate  │ <8%     │ 8-15%   │ 15-25%  │ >25%
Landing Page SQL Rate   │ <15%    │ 15-30%  │ 30-45%  │ >45%

B2B SALES CYCLE CONTEXT:
├── Avg LinkedIn-sourced cycle: 200+ days
├── Multi-touch attribution: 6-12 touches average
├── First touch to opportunity: 30-90 days
└── Don't judge CPL without SQL rate data
```

## Engagement Benchmarks

```
ENGAGEMENT RATE BENCHMARKS
==========================

Metric                  │ Poor    │ Average │ Good    │ Excellent
────────────────────────┼─────────┼─────────┼─────────┼──────────
Total Engagement Rate   │ <0.3%   │ 0.3-0.6%│ 0.6-1%  │ >1%
Like Rate               │ <0.15%  │ 0.15-0.3%│0.3-0.5% │ >0.5%
Comment Rate            │ <0.02%  │ 0.02-0.05%│0.05-0.1%│>0.1%
Share Rate              │ <0.01%  │ 0.01-0.03%│0.03-0.06%│>0.06%
Follow Rate (per ad)    │ <0.05%  │ 0.05-0.1%│0.1-0.2% │ >0.2%

VIDEO SPECIFIC:
├── 25% View Rate       │ <20%    │ 20-35%  │ 35-50%  │ >50%
├── 50% View Rate       │ <10%    │ 10-20%  │ 20-35%  │ >35%
├── 75% View Rate       │ <5%     │ 5-12%   │ 12-20%  │ >20%
└── 100% Completion     │ <3%     │ 3-8%    │ 8-15%   │ >15%
```

## Seasonal Adjustment Factors

```
SEIZOENSGEBONDEN VARIATIES (B2B)
================================

Periode              │ CPM Factor │ CPL Factor │ Notes
─────────────────────┼────────────┼────────────┼──────────────
Q1 (Jan-Mar)         │   0.90     │   0.95     │ Budget resets
April-May            │   0.95     │   1.00     │ Baseline
Juni                 │   0.92     │   0.98     │ Summer start
Juli-Augustus        │   0.85     │   1.05     │ Vacation mode
September            │   1.00     │   1.00     │ Back to work
Oktober              │   1.05     │   1.00     │ Q4 planning
November             │   1.15     │   1.05     │ Budget flush
December 1-15        │   1.20     │   1.10     │ Year-end push
December 16-31       │   0.80     │   1.15     │ Holiday shutdown

B2B SPECIFIC PATTERNS:
├── Decision makers OOO: Jul-Aug, Dec 20-Jan 3
├── Budget cycles: Jan (resets), Nov-Dec (use-or-lose)
├── Conference season: Spring/Fall = more noise
└── Summer: Lower CPM but lower response rates
```

## Benchmark Comparison Template

### Wanneer gebruiker vraagt om metrics te evalueren:

```
METRIC EVALUATIE - [ACCOUNT]
============================

📊 JOUW METRICS vs BENCHMARKS

Metric      │ Jouw Waarde │ Benchmark │ Verschil │ Status
────────────┼─────────────┼───────────┼──────────┼────────
CPL         │   €[X]      │   €[Y]    │  [+/-Z%] │ [🟢🟡🔴]
CPC         │   €[X]      │   €[Y]    │  [+/-Z%] │ [🟢🟡🔴]
CTR         │   [X]%      │   [Y]%    │  [+/-Z%] │ [🟢🟡🔴]
CVR (Form)  │   [X]%      │   [Y]%    │  [+/-Z%] │ [🟢🟡🔴]
SQL Rate    │   [X]%      │   [Y]%    │  [+/-Z%] │ [🟢🟡🔴]
Eng. Rate   │   [X]%      │   [Y]%    │  [+/-Z%] │ [🟢🟡🔴]

INTERPRETATIE:
🟢 Boven benchmark (>10% beter)
🟡 Op benchmark (±10%)
🔴 Onder benchmark (>10% slechter)

CONTEXT FACTOREN:
├── Industry: [specified]
├── Funnel Stage: [TOFU/MOFU/BOFU]
├── Ad Format: [specified]
└── Target Audience: [specified]

AANBEVELINGEN:
├── [Focus area 1]
├── [Focus area 2]
└── [Focus area 3]
```

## LTV:CAC Framework

```
LINKEDIN ADS ROI EVALUATIE
==========================

Stap 1: Bereken Customer Acquisition Cost (CAC)
├── Total LinkedIn Spend: €[X]
├── Number of Customers: [Y]
└── CAC = €[X] / [Y] = €[Z]

Stap 2: Bepaal Customer Lifetime Value (LTV)
├── Average Contract Value: €[X]
├── Average Customer Lifespan: [Y] years
├── Gross Margin: [Z]%
└── LTV = €[X] × [Y] × [Z]% = €[W]

Stap 3: Evalueer LTV:CAC Ratio
├── <1:1 = Verliesgevend
├── 1:1 - 3:1 = Break-even tot marginaal
├── 3:1 - 5:1 = Gezond (target range)
├── 5:1 - 7:1 = Excellent
└── >7:1 = Under-investing in growth?

LINKEDIN TYPICAL LTV:CAC:
├── SaaS B2B: 4:1 - 6:1 target
├── Enterprise: 5:1 - 8:1 (long sales cycle)
├── SMB: 3:1 - 5:1 (shorter cycle)
└── Services: 4:1 - 7:1
```

## Voorbeeld Interactie

**Gebruiker**: "Mijn LinkedIn campagne voor SaaS heeft een CPL van €95 en een SQL rate van 18%. Is dat goed?"

**Claude response**:

"Laat me je metrics vergelijken met SaaS benchmarks:

---

**BENCHMARK VERGELIJKING - SaaS B2B:**

| Metric | Jouw Waarde | Benchmark Range | Status |
|--------|-------------|-----------------|--------|
| CPL | €95 | €80-120 (average) | 🟢 Goed |
| SQL Rate | 18% | 10-20% (average-good) | 🟢 Goed |
| Effective Cost per SQL | €528 | €400-600 (calculated) | 🟡 OK |

---

**INTERPRETATIE:**

✅ **CPL (€95)** - Midden in de average range voor SaaS. Acceptabel.

✅ **SQL Rate (18%)** - Boven gemiddeld. Dit compenseert de CPL significant.

🟡 **Cost per SQL (€528)** - Dit is de metric die echt telt. €95 / 18% = €528 per qualified lead.

---

**CONTEXT VRAAG:**
Wat is je Average Contract Value (ACV)?
- Als ACV >€10k: Excellent performance
- Als ACV €5-10k: Gezond
- Als ACV <€5k: CPL optimalisatie nodig

**AANBEVELINGEN:**

1. **Behoud SQL rate** - Dit is je sterke punt. Voeg geen extra friction toe.

2. **Test CPL reductie** via:
   - Broader targeting (kan CPL 15-20% verlagen)
   - Organic content boost (thought leadership)
   - Lead Gen Forms vs Landing Page A/B test

3. **Track LTV:CAC ratio** - Als deze >3:1 is, kun je veilig opschalen.

Wil je dat ik je Cost per SQL analyseer tegen je ACV?"

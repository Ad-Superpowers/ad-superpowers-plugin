---
name: prompt-engineering-library
description: Bibliotheek met geoptimaliseerde prompts voor AI-tools in Meta Ads workflows, inclusief prompts voor creative generation, data analyse, copy writing en reporting. Gebruik deze skill wanneer je AI effectiever wilt inzetten voor Meta Ads taken.
---

# Prompt Engineering Library

## Overview

Deze skill biedt een verzameling van geoptimaliseerde prompts voor het inzetten van AI (ChatGPT, Claude, Midjourney, etc.) binnen Meta Ads workflows, van creative briefing tot data analyse en copy generation.

## Prompt Fundamentals

### Anatomie van een Goede Prompt

```
┌─────────────────────────────────────────────────────────────────┐
│  PROMPT STRUCTUUR (CRISP Framework)                             │
│                                                                 │
│  C - Context: Geef achtergrond en situatie                      │
│  R - Role: Definieer de expertise die je nodig hebt             │
│  I - Instructions: Geef duidelijke, specifieke opdracht         │
│  S - Specifics: Voeg details, constraints, formats toe          │
│  P - Parameters: Output format, lengte, stijl                   │
└─────────────────────────────────────────────────────────────────┘
```

### Prompt Quality Levels

| Level | Voorbeeld | Kwaliteit |
|-------|-----------|-----------|
| ❌ Basic | "Schrijf ad copy" | Vaag, generiek resultaat |
| ⚠️ Better | "Schrijf Facebook ad copy voor een fitness app" | Beter maar nog onvolledig |
| ✅ Good | "Je bent een direct response copywriter. Schrijf 3 Facebook ad copy variaties voor FitPro app gericht op vrouwen 25-40 die willen afvallen. Gebruik PAS framework. Max 125 karakters primary text." | Specifiek, actionable |

## Prompt Categories

### Category 1: Ad Copy Generation

#### Primary Text Generator

```
PROMPT: AD COPY GENERATOR

Je bent een ervaren Meta Ads copywriter gespecialiseerd in
direct response advertising.

CONTEXT:
- Product: [PRODUCT/DIENST]
- Doelgroep: [DEMOGRAFIE + PSYCHOGRAFIE]
- Unique Selling Point: [USP]
- Funnel fase: [TOFU/MOFU/BOFU]
- Aanbieding: [INDIEN VAN TOEPASSING]

OPDRACHT:
Schrijf 5 variaties van primary text voor een Meta ad.

SPECIFICATIES:
- Framework: Gebruik afwisselend PAS, AIDA, en BAB
- Hook: Eerste zin moet aandacht pakken binnen 3 seconden
- Lengte: 100-150 karakters (eerste 125 zichtbaar)
- Toon: [Casual/Professional/Urgent/Friendly]
- CTA: Eindig met duidelijke call-to-action

OUTPUT FORMAT:
Voor elke variatie:
1. [Framework gebruikt]
2. Primary text
3. Headline suggestie (max 40 karakters)
4. CTA button aanbeveling
```

#### Hook Generator

```
PROMPT: HOOK GENERATOR

Genereer 10 scroll-stopping hooks voor een Meta ad.

PRODUCT: [PRODUCT]
DOELGROEP: [DOELGROEP]
PIJN PUNT: [BELANGRIJKSTE PROBLEEM]
GEWENST RESULTAAT: [WAT WILLEN ZE BEREIKEN]

HOOK TYPES (gebruik mix):
1. Vraag hooks ("Wist je dat...?")
2. Statistiek hooks ("80% van...")
3. Contrarian hooks ("Vergeet wat je wist over...")
4. Result hooks ("Zo bereikte ik [X] in [tijd]")
5. Curiosity hooks ("Het geheim achter...")

CONSTRAINTS:
- Max 10 woorden per hook
- Moet stoppen met scrollen
- Geen clickbait die niet waargemaakt kan worden
- Geschikt voor [PLATFORM: Feed/Stories/Reels]
```

### Category 2: Creative Briefing

#### UGC Creator Brief Generator

```
PROMPT: UGC BRIEF GENERATOR

Maak een complete UGC video brief voor creators.

PRODUCT INFO:
- Product: [PRODUCT]
- Prijs: [PRIJS]
- USPs: [LIJST MET VOORDELEN]
- Website: [URL]

CAMPAGNE INFO:
- Platform: [Instagram Reels/TikTok/Facebook]
- Doel: [Awareness/Consideration/Conversion]
- Doelgroep: [DEMOGRAFIE]
- Toon: [Authentiek/Energiek/Informatief]

GENEREER EEN BRIEF MET:
1. Overzicht (1 paragraaf)
2. Key messages (3-5 bullets)
3. Script outline met timing (hook, body, CTA)
4. Do's en Don'ts
5. Technische specs (formaat, lengte, kwaliteit)
6. Voorbeeld hooks om te gebruiken
7. Voorbeelden van wat te vermijden

OUTPUT: Markdown format, klaar om naar creator te sturen
```

#### Image Ad Concept Generator

```
PROMPT: AD VISUAL CONCEPT GENERATOR

Genereer 5 visuele concepten voor Meta ad afbeeldingen.

PRODUCT: [PRODUCT]
BRAND GUIDELINES: [KLEUREN, STIJL, TONE]
DOELGROEP: [WIE]
BOODSCHAP: [WAT COMMUNICEREN]

VOOR ELK CONCEPT, GEEF:
1. Concept naam
2. Visuele beschrijving (wat zie je)
3. Tekst overlay suggestie
4. Waarom dit werkt voor de doelgroep
5. Productie aanpak (stock, fotoshoot, design)

CONCEPT TYPES (include mix):
- Product-focused (product in actie)
- Lifestyle (aspirational scenario)
- Before/After
- Social proof (reviews, ratings visueel)
- Problem/Solution split
```

### Category 3: Data Analysis

#### Performance Report Analyzer

```
PROMPT: CAMPAIGN ANALYSIS

Analyseer de volgende Meta Ads performance data en geef
actionable insights.

DATA:
[PLAK HIER JE CAMPAIGN DATA]

ANALYSEER:
1. Top 3 best presterende elementen (en waarom)
2. Top 3 underperformers (en mogelijke oorzaken)
3. Trends over tijd (verbeterend/verslechterend)
4. Anomalieën of opvallende patronen
5. Vergelijking met benchmarks indien gegeven

GEEF AANBEVELINGEN:
- Quick wins (binnen 24 uur uitvoerbaar)
- Medium-term optimalisaties (deze week)
- Strategische wijzigingen (volgende maand)

FORMAT:
Gebruik tabellen waar relevant
Prioriteer aanbevelingen (Hoog/Medium/Laag impact)
Wees specifiek (geen vage suggesties)
```

#### A/B Test Results Interpreter

```
PROMPT: A/B TEST ANALYSE

Interpreteer de volgende A/B test resultaten.

TEST SETUP:
- Hypothese: [WAT TESTTEN WE]
- Variant A (Control): [BESCHRIJVING]
- Variant B (Test): [BESCHRIJVING]
- Test duur: [X DAGEN]
- Primary metric: [CPA/CTR/ROAS]

RESULTATEN:
[PLAK DATA HIER]

ANALYSEER:
1. Is het resultaat statistisch significant? (waarom wel/niet)
2. Wat is de impact in absolute en relatieve termen?
3. Zijn er secondary metrics die extra inzicht geven?
4. Wat kunnen we leren van dit resultaat?
5. Wat zou de volgende test moeten zijn?

RECOMMENDATION:
- Implementeer winner: Ja/Nee + waarom
- Confidence level: Hoog/Medium/Laag
- Suggested follow-up action
```

### Category 4: Audience Research

#### Audience Persona Builder

```
PROMPT: DOELGROEP PERSONA

Creëer een gedetailleerde buyer persona voor Meta Ads targeting.

PRODUCT/DIENST: [WAT VERKOOP JE]
HUIDIGE KLANTEN: [WAT WEET JE OVER HEN]
PRIJSPUNT: [PRIJS]
MARKT: [B2C/B2B, REGIO]

GENEREER PERSONA MET:

1. DEMOGRAFIE
├── Leeftijd range
├── Geslacht
├── Locatie
├── Inkomen/opleidingsniveau
└── Gezinssituatie

2. PSYCHOGRAFIE
├── Waarden en overtuigingen
├── Levensstijl
├── Interesses en hobby's
└── Mediagedrag (platforms, content types)

3. PAINS & GAINS
├── Top 3 frustraties/problemen
├── Top 3 doelen/aspiraties
├── Wat houdt hen 's nachts wakker
└── Wat zou hun leven verbeteren

4. BUYING BEHAVIOR
├── Waar zoeken ze informatie
├── Wat triggert een aankoop
├── Bezwaren/barrières
└── Decision making process

5. META ADS TARGETING SUGGESTIES
├── Interest targeting opties
├── Lookalike audience sources
├── Custom audience ideeën
└── Messaging angles per funnel fase
```

### Category 5: Reporting

#### Weekly Report Generator

```
PROMPT: WEEKLY PERFORMANCE REPORT

Genereer een professioneel weekrapport voor Meta Ads.

WEEK: [WEEK NUMMER]
ACCOUNT: [ACCOUNT NAAM]

PERFORMANCE DATA:
[PLAK METRICS HIER]
- Spend, Impressions, Clicks, CTR
- Conversions, CPA, ROAS
- Top campaigns/ad sets

STRUCTUREER RAPPORT ALS:

1. EXECUTIVE SUMMARY (3-5 bullets)
├── Belangrijkste resultaat
├── Grootste verandering vs vorige week
└── Key action item

2. PERFORMANCE OVERVIEW
├── Tabel met KPIs vs targets
├── Week-over-week vergelijking
└── Trend indicator (↑↓→)

3. HIGHLIGHTS
├── Beste performer (waarom)
├── Nieuwe tests gelanceerd
└── Belangrijke learnings

4. AANDACHTSPUNTEN
├── Underperformers
├── Budget issues
└── Aankomende challenges

5. NEXT WEEK PLAN
├── Geplande acties
├── Tests om te starten
└── Budget wijzigingen

FORMAT: Professional, scanbaar, max 1 pagina
```

### Category 6: AI Image Generation

#### Midjourney Ad Image Prompts

```
PROMPT: MIDJOURNEY AD VISUALS

Genereer Midjourney prompts voor Meta ad afbeeldingen.

PRODUCT: [PRODUCT]
STIJL: [Fotorealistisch/Illustratie/Minimalistisch]
MOOD: [Energiek/Kalm/Premium/Speels]
KLEURENPALET: [KLEUREN]

GENEREER 5 MIDJOURNEY PROMPTS:

Format per prompt:
/imagine [beschrijving], [stijl parameters], [technische specs]

INCLUDE IN ELKE PROMPT:
- Onderwerp/scene beschrijving
- Belichting (soft, dramatic, natural)
- Compositie (centered, rule of thirds)
- Camera angle indien relevant
- Stijl referenties
- Technische params: --ar 1:1, --v 5.2, --q 2

VARIATIES:
1. Product hero shot
2. Lifestyle/usage scenario
3. Abstract/conceptual
4. Social proof visual
5. Problem/solution visual
```

#### DALL-E Ad Concepts

```
PROMPT: DALL-E AD VISUALS

Genereer DALL-E prompts voor social media advertenties.

PRODUCT: [PRODUCT]
BOODSCHAP: [KEY MESSAGE]
FORMAT: [1:1 Square / 4:5 / 9:16]

GENEREER 5 DALL-E PROMPTS:

Format:
"[Gedetailleerde beschrijving], [stijl], [belichting],
[compositie], digital art/photography/illustration"

OVERWEGINGEN:
- Geen tekst in afbeelding (voeg later toe)
- Duidelijk focal point
- Ruimte voor overlay tekst
- Brand-consistente kleuren
- Geen gezichten (copyright issues)
```

## Prompt Templates Library

### Quick Copy Prompts

```
🔹 HEADLINE GENERATOR:
"Genereer 10 headlines voor [PRODUCT] gericht op [DOELGROEP].
Max 40 karakters. Focus op [BENEFIT]. Mix van vraag, statement
en urgentie formats."

🔹 CTA VARIATIES:
"Geef 8 call-to-action variaties voor [ACTIE] die [EMOTIE]
oproepen. Sterker dan 'Klik hier'. Max 3 woorden."

🔹 SOCIAL PROOF COPY:
"Herschrijf deze review als korte ad copy (50 woorden):
[REVIEW]. Maak het compelling zonder te overdrijven."

🔹 URGENCY CREATOR:
"Genereer 5 urgentie-elementen voor [AANBIEDING] die FOMO
creëren zonder spammy te klinken. Ethisch en eerlijk."
```

### Quick Analysis Prompts

```
🔹 QUICK AUDIT:
"Bekijk deze metrics [DATA] en geef in 3 bullets:
1) Grootste probleem 2) Quick win 3) Prioriteit deze week"

🔹 COMPETITOR COPY ANALYSE:
"Analyseer deze competitor ad [COPY]. Wat werkt? Wat niet?
Hoe kunnen we dit beter doen voor [ONS PRODUCT]?"

🔹 AUDIENCE INSIGHT:
"Gebaseerd op deze engagement data [DATA], wat vertelt dit
over onze doelgroep? Geef 3 actionable targeting insights."
```

## Voorbeeld Interactie

**Gebruiker**: "Ik heb prompts nodig om snel ad copy te genereren voor mijn skincare merk."

**Claude response**:

"Hier zijn geoptimaliseerde prompts voor je skincare merk:

---

**PROMPT 1: Primary Text Generator**

```
Je bent een beauty copywriter gespecialiseerd in skincare DTC brands.

MERK: [Jouw merknaam]
PRODUCT: [Specifiek product, bijv. "Vitamin C Serum"]
DOELGROEP: Vrouwen 25-45, interesse in clean beauty
USP: [Bijv. "100% natuurlijk, zichtbaar resultaat in 2 weken"]
FUNNEL: BOFU (retargeting)

Schrijf 5 primary text variaties:
- Mix van PAS en AIDA frameworks
- Eerste zin = scroll-stopping hook
- 100-125 karakters
- Eindig met soft CTA

Lever ook: matching headline (max 40 char) per variatie
```

---

**PROMPT 2: Hook Generator (Quick)**

```
Genereer 10 hooks voor skincare ad. Product: [X]
Probleem: [acne/rimpels/doffe huid]
Resultaat: [stralende huid/minder rimpels]

Mix: vraag, statistiek, before/after, curiosity
Max 8 woorden per hook. Scroll-stopping.
```

---

**PROMPT 3: Testimonial Rewriter**

```
Herschrijf deze klantreview als ad copy:

"[Plak review hier]"

Maak het:
- Korter (max 80 woorden)
- Meer engaging (hook toevoegen)
- Met duidelijk resultaat highlight
- Inclusief emoji's (max 3)
Behoud authenticiteit, geen overclaims.
```

---

Wil je dat ik ook prompts maak voor visual concepts of UGC briefings?"

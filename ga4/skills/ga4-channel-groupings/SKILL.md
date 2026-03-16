---
name: ga4-channel-groupings
description: "Custom channel groupings configureren in GA4. Gebruik voor: (1) Default channel group regels begrijpen, (2) Custom channel groups aanmaken, (3) Source/medium mapping optimaliseren, (4) Branded vs non-branded traffic splitsen, (5) Affiliate en partner tracking. Triggers: channel grouping, custom channels, source medium, traffic categorisatie, default channel, primary channel."
---

# GA4 Channel Groupings Guide

Complete gids voor het configureren en optimaliseren van channel groupings in Google Analytics 4 voor accurate traffic categorisatie.

## Quick Decision Tree

```
CHANNEL GROUPING BESLISSING
│
├─► WAAROM CUSTOM CHANNELS?
│   ├─► Default channels matchen niet met business
│   │   └─► Voorbeeld: Affiliate traffic in "Referral"
│   │   └─► Oplossing: Custom "Affiliate" channel
│   │
│   ├─► Branded vs non-branded splitsen
│   │   └─► Voorbeeld: Brand search apart zien
│   │   └─► Oplossing: Custom "Paid Brand" channel
│   │
│   ├─► Partner traffic apart tracken
│   │   └─► Voorbeeld: Resellers, distributors
│   │   └─► Oplossing: Custom "Partner" channel
│   │
│   └─► Specifieke campagnes apart rapporteren
│       └─► Voorbeeld: Influencer marketing
│       └─► Oplossing: Custom "Influencer" channel
│
├─► HOE WERKEN GA4 CHANNELS?
│   ├─► Default Channel Group (system-defined)
│   │   └─► 18 standaard channels
│   │   └─► Gebaseerd op source/medium regels
│   │
│   ├─► Primary Channel Group (editable)
│   │   └─► Kopie van default die je kunt aanpassen
│   │   └─► Wordt standaard in reports
│   │
│   └─► Custom Channel Groups
│       └─► Volledig zelf definiëren
│       └─► Tot 2 extra custom groups (gratis GA4)
│
└─► WANNEER CUSTOM GROUP MAKEN?
    ├─► Traffic past niet in default channels
    ├─► Business heeft unieke categorieën nodig
    ├─► Rapportage requirements zijn specifiek
    └─► Marketing teams willen andere indeling
```

## Default Channel Groups

```
GA4 DEFAULT CHANNEL GROUPS
==========================

DE 18 STANDAARD CHANNELS:
┌─────────────────────┬───────────────────────────────────────────┐
│ Channel             │ Wanneer getriggerd                        │
├─────────────────────┼───────────────────────────────────────────┤
│ Direct              │ Source = (direct) EN medium = (none/not   │
│                     │ set)                                      │
├─────────────────────┼───────────────────────────────────────────┤
│ Organic Search      │ Source = zoekmachine EN medium = organic  │
│                     │ (google, bing, yahoo, etc.)               │
├─────────────────────┼───────────────────────────────────────────┤
│ Paid Search         │ Source = zoekmachine EN medium =          │
│                     │ cpc/ppc/paid EN campaign ≠ shopping       │
├─────────────────────┼───────────────────────────────────────────┤
│ Paid Shopping       │ (Source = shopping sites) OF              │
│                     │ (campaign contains shop/shopping)         │
├─────────────────────┼───────────────────────────────────────────┤
│ Paid Social         │ Source = social network EN medium =       │
│                     │ cpc/ppc/paid/paid-social                  │
├─────────────────────┼───────────────────────────────────────────┤
│ Organic Social      │ Source = social network EN medium =       │
│                     │ social/organic-social OF referral         │
├─────────────────────┼───────────────────────────────────────────┤
│ Email               │ Medium = email                            │
├─────────────────────┼───────────────────────────────────────────┤
│ Affiliates          │ Medium = affiliate                        │
├─────────────────────┼───────────────────────────────────────────┤
│ Referral            │ Medium = referral (en niet social)        │
├─────────────────────┼───────────────────────────────────────────┤
│ Paid Video          │ Source = video platform EN medium = cpc   │
│                     │ (youtube, vimeo, etc.)                    │
├─────────────────────┼───────────────────────────────────────────┤
│ Organic Video       │ Source = video platform EN medium =       │
│                     │ organic/referral                          │
├─────────────────────┼───────────────────────────────────────────┤
│ Display             │ Medium = display/banner/cpm               │
├─────────────────────┼───────────────────────────────────────────┤
│ Paid Other          │ Medium = cpc/ppc/paid (niet elders match) │
├─────────────────────┼───────────────────────────────────────────┤
│ Organic Shopping    │ Source = shopping EN medium ≠ paid        │
├─────────────────────┼───────────────────────────────────────────┤
│ Audio               │ Medium = audio                            │
├─────────────────────┼───────────────────────────────────────────┤
│ SMS                 │ Medium = sms                              │
├─────────────────────┼───────────────────────────────────────────┤
│ Mobile Push         │ Medium = push/mobile/notification         │
├─────────────────────┼───────────────────────────────────────────┤
│ Unassigned          │ Geen van bovenstaande regels matcht       │
└─────────────────────┴───────────────────────────────────────────┘

⚠️ VOLGORDE MATTERS:
├── GA4 evalueert channels van boven naar beneden
├── Eerste match wint
├── Daarom: specifieke regels eerst, algemene later
└── "Unassigned" is altijd laatste fallback
```

## Channel Group Configuratie

```
PRIMARY CHANNEL GROUP AANPASSEN
===============================

LOCATIE: Admin → Data display → Default channel group

WAT KUN JE AANPASSEN:
├── Channel volgorde (prioriteit)
├── Channel regels (source/medium matching)
├── Nieuwe channels toevoegen
└── Bestaande channels hernoemen

STAP-VOOR-STAP AANPASSEN:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Ga naar Admin → Data display → Default channel group      │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Click op het channel dat je wilt aanpassen                │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Review de huidige regels                                  │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Click "Add new condition" voor extra regels               │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Definieer source/medium/campaign matching                 │
├────┼────────────────────────────────────────────────────────────┤
│ 6  │ Save changes                                              │
└────┴────────────────────────────────────────────────────────────┘

NIEUWE CHANNEL TOEVOEGEN:
┌────┬────────────────────────────────────────────────────────────┐
│ 1  │ Scroll naar beneden in channel list                       │
├────┼────────────────────────────────────────────────────────────┤
│ 2  │ Click "Add new channel"                                   │
├────┼────────────────────────────────────────────────────────────┤
│ 3  │ Geef channel een naam                                     │
├────┼────────────────────────────────────────────────────────────┤
│ 4  │ Definieer matching regels                                 │
├────┼────────────────────────────────────────────────────────────┤
│ 5  │ Drag channel naar juiste positie (volgorde!)              │
├────┼────────────────────────────────────────────────────────────┤
│ 6  │ Save                                                      │
└────┴────────────────────────────────────────────────────────────┘

⚠️ BELANGRIJK:
├── Wijzigingen zijn NIET retroactief
├── Alleen toekomstige data wordt beïnvloed
├── Test eerst met exploration report
└── Document alle wijzigingen voor team
```

## Custom Channel Rules

```
CHANNEL RULE SYNTAX
===================

BESCHIKBARE CONDITIES:
┌─────────────────────┬────────────────────────────────────────────┐
│ Dimension           │ Voorbeelden                                │
├─────────────────────┼────────────────────────────────────────────┤
│ Source              │ google, facebook, linkedin, affiliate-name │
├─────────────────────┼────────────────────────────────────────────┤
│ Medium              │ cpc, organic, referral, email, affiliate   │
├─────────────────────┼────────────────────────────────────────────┤
│ Campaign            │ campagne naam of ID                        │
├─────────────────────┼────────────────────────────────────────────┤
│ Source platform     │ Advertising platform (Google Ads, etc.)    │
└─────────────────────┴────────────────────────────────────────────┘

MATCHING OPERATORS:
┌─────────────────────┬────────────────────────────────────────────┐
│ Operator            │ Gebruik                                    │
├─────────────────────┼────────────────────────────────────────────┤
│ exactly matches     │ Exacte string match (case insensitive)     │
├─────────────────────┼────────────────────────────────────────────┤
│ contains            │ Substring ergens in waarde                 │
├─────────────────────┼────────────────────────────────────────────┤
│ begins with         │ String begint met waarde                   │
├─────────────────────┼────────────────────────────────────────────┤
│ ends with           │ String eindigt met waarde                  │
├─────────────────────┼────────────────────────────────────────────┤
│ matches regex       │ Regular expression match                   │
├─────────────────────┼────────────────────────────────────────────┤
│ is one of           │ Match tegen lijst van waarden              │
└─────────────────────┴────────────────────────────────────────────┘

VOORBEELD REGELS:

Channel: "Affiliate"
├── Rule 1: Medium exactly matches "affiliate"
├── Rule 2: Source contains "partner"
└── Rule 3: Campaign begins with "aff-"
→ Matches indien ANY van bovenstaande true

Channel: "Paid Brand Search"
├── Rule 1: Medium is one of [cpc, ppc, paid]
├── AND
├── Rule 2: Source exactly matches "google"
├── AND
├── Rule 3: Campaign contains "brand"
→ Matches indien ALL van bovenstaande true

COMBINING RULES (AND vs OR):
────────────────────────────
Binnen één regel: AND (alle condities moeten matchen)
Tussen regels: OR (één van de regels moet matchen)

Voorbeeld "Paid Social" channel:
├── Rule 1: Source=facebook AND Medium=paid-social
├── OR
├── Rule 2: Source=instagram AND Medium=paid-social
├── OR
├── Rule 3: Source=linkedin AND Medium=paid-social
└── → Traffic wordt "Paid Social" als ANY regel matcht
```

## Veelgebruikte Custom Channels

```
POPULAIRE CUSTOM CHANNEL CONFIGURATIES
======================================

1. BRANDED VS NON-BRANDED SEARCH
────────────────────────────────

Channel: "Paid Search - Brand"
┌─────────────────────┬────────────────────────────────────────────┐
│ Condition           │ Setting                                    │
├─────────────────────┼────────────────────────────────────────────┤
│ Medium              │ is one of: cpc, ppc, paid                  │
│ AND Source          │ is one of: google, bing                    │
│ AND Campaign        │ contains: brand (of jouw brandnaam)        │
└─────────────────────┴────────────────────────────────────────────┘

Channel: "Paid Search - Non-Brand"
┌─────────────────────┬────────────────────────────────────────────┐
│ Condition           │ Setting                                    │
├─────────────────────┼────────────────────────────────────────────┤
│ Medium              │ is one of: cpc, ppc, paid                  │
│ AND Source          │ is one of: google, bing                    │
│ AND Campaign        │ does not contain: brand                    │
└─────────────────────┴────────────────────────────────────────────┘

⚠️ Plaats "Paid Search - Brand" BOVEN "Paid Search - Non-Brand"

2. AFFILIATE MARKETING
──────────────────────

Channel: "Affiliate"
┌─────────────────────┬────────────────────────────────────────────┐
│ Rule 1              │ Medium exactly matches: affiliate          │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 2           │ Source contains: affiliate                 │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 3           │ Campaign begins with: aff_                 │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 4           │ Source is one of: [affiliate-partner-1,    │
│                     │ affiliate-partner-2, etc.]                 │
└─────────────────────┴────────────────────────────────────────────┘

3. INFLUENCER MARKETING
───────────────────────

Channel: "Influencer"
┌─────────────────────┬────────────────────────────────────────────┐
│ Rule 1              │ Medium exactly matches: influencer         │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 2           │ Campaign contains: influencer              │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 3           │ Campaign begins with: inf_                 │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 4           │ Source contains: creator                   │
└─────────────────────┴────────────────────────────────────────────┘

4. PARTNER/RESELLER TRAFFIC
───────────────────────────

Channel: "Partner"
┌─────────────────────┬────────────────────────────────────────────┐
│ Rule 1              │ Medium exactly matches: partner            │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 2           │ Source is one of: [partner-1.com,          │
│                     │ partner-2.com, reseller.com]               │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 3           │ Campaign begins with: partner_             │
└─────────────────────┴────────────────────────────────────────────┘

5. RETARGETING APART
────────────────────

Channel: "Retargeting"
┌─────────────────────┬────────────────────────────────────────────┐
│ Rule 1              │ Medium exactly matches: retargeting        │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 2           │ Campaign contains: retargeting             │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 3           │ Campaign contains: remarketing             │
├─────────────────────┼────────────────────────────────────────────┤
│ OR Rule 4           │ Medium exactly matches: remarketing        │
└─────────────────────┴────────────────────────────────────────────┘

⚠️ Plaats "Retargeting" BOVEN "Paid Social" en "Paid Search"
   Anders wordt retargeting traffic in die channels gecategoriseerd
```

## Channel Volgorde Optimalisatie

```
CHANNEL PRIORITEIT BEPALEN
==========================

AANBEVOLEN VOLGORDE:
┌────┬────────────────────────┬────────────────────────────────────┐
│ #  │ Channel                │ Rationale                          │
├────┼────────────────────────┼────────────────────────────────────┤
│ 1  │ Retargeting            │ Meest specifieke paid traffic      │
├────┼────────────────────────┼────────────────────────────────────┤
│ 2  │ Paid Search - Brand    │ Specifieke search subset           │
├────┼────────────────────────┼────────────────────────────────────┤
│ 3  │ Paid Shopping          │ Shopping-specifieke campaigns      │
├────┼────────────────────────┼────────────────────────────────────┤
│ 4  │ Paid Search            │ Algemene paid search               │
├────┼────────────────────────┼────────────────────────────────────┤
│ 5  │ Paid Social            │ Social advertising                 │
├────┼────────────────────────┼────────────────────────────────────┤
│ 6  │ Display                │ Display/banner ads                 │
├────┼────────────────────────┼────────────────────────────────────┤
│ 7  │ Paid Video             │ YouTube/video ads                  │
├────┼────────────────────────┼────────────────────────────────────┤
│ 8  │ Paid Other             │ Andere betaalde traffic            │
├────┼────────────────────────┼────────────────────────────────────┤
│ 9  │ Affiliate              │ Affiliate partners                 │
├────┼────────────────────────┼────────────────────────────────────┤
│ 10 │ Influencer             │ Influencer collaborations          │
├────┼────────────────────────┼────────────────────────────────────┤
│ 11 │ Partner                │ Business partners                  │
├────┼────────────────────────┼────────────────────────────────────┤
│ 12 │ Email                  │ Email marketing                    │
├────┼────────────────────────┼────────────────────────────────────┤
│ 13 │ SMS                    │ SMS campaigns                      │
├────┼────────────────────────┼────────────────────────────────────┤
│ 14 │ Push Notifications     │ Mobile push                        │
├────┼────────────────────────┼────────────────────────────────────┤
│ 15 │ Organic Search         │ SEO traffic                        │
├────┼────────────────────────┼────────────────────────────────────┤
│ 16 │ Organic Social         │ Unpaid social                      │
├────┼────────────────────────┼────────────────────────────────────┤
│ 17 │ Organic Video          │ YouTube organic                    │
├────┼────────────────────────┼────────────────────────────────────┤
│ 18 │ Referral               │ Website referrals                  │
├────┼────────────────────────┼────────────────────────────────────┤
│ 19 │ Direct                 │ Direct traffic                     │
├────┼────────────────────────┼────────────────────────────────────┤
│ 20 │ Unassigned             │ Catch-all (altijd laatste)         │
└────┴────────────────────────┴────────────────────────────────────┘

PRINCIPE:
├── Meest specifieke regels eerst
├── Betaalde traffic vóór organisch
├── Custom channels vóór default channels
├── Direct en Unassigned altijd laatste
└── Test volgorde met sample data
```

## Troubleshooting Channel Issues

```
CHANNEL TROUBLESHOOTING GUIDE
=============================

PROBLEEM: Traffic in "Unassigned"
─────────────────────────────────
Oorzaken:
├── UTM parameters niet correct
├── Medium niet herkend
├── Source niet in standaard lijsten
└── Speciale characters in waarden

Diagnose:
├── GA4 → Explorations → Traffic source report
├── Filter op "Unassigned" channel
├── Bekijk source/medium combinaties
└── Identificeer patroon

Oplossing:
├── Fix UTM parameters bij bron
├── Voeg custom channel regel toe
├── Update naming convention
└── Creëer catch-all regel voor dit type

PROBLEEM: Traffic in verkeerde channel
──────────────────────────────────────
Oorzaken:
├── Channel volgorde incorrect
├── Regel te breed/te smal
├── Medium niet consistent
└── Conflicting campaign names

Diagnose:
├── Test met exploration: wat matcht welke regel?
├── Review channel volgorde
├── Check rule specificity
└── Trace specifieke traffic source

Oplossing:
├── Herorder channels (specifiek → algemeen)
├── Maak regels specifieker
├── Enforce naming convention
└── Add exclusion rules

PROBLEEM: Paid Social in "Referral"
───────────────────────────────────
Oorzaken:
├── UTM medium niet "paid-social" of "cpc"
├── Geen UTM parameters
├── Platform click ID alleen (fbclid, etc.)
└── Medium is "referral" of "social"

Oplossing:
├── Controleer UTM template in ad platform
├── Gebruik medium=paid-social
├── Verify UTM parameters blijven in URL
└── Add custom rule: Source=facebook → Paid Social

PROBLEEM: Direct traffic te hoog
────────────────────────────────
Oorzaken:
├── Ontbrekende UTM parameters
├── HTTPS → HTTP redirect (strips referrer)
├── Mobile app traffic
├── Dark social (messaging apps)
├── Bookmarks en typed URLs
└── JavaScript redirect zonder params

Oplossing:
├── Audit alle campagne URLs voor UTM
├── Ensure HTTPS throughout
├── Implement app deep link tracking
├── Accept 15-25% direct is normaal
└── Use link shorteners met tracking

PROBLEEM: Inconsistente source/medium
─────────────────────────────────────
Oorzaken:
├── Verschillende teamleden, verschillende UTMs
├── Case-sensitivity issues
├── Platform dynamic params verschillend
└── Geen enforced naming convention

Oplossing:
├── Creëer en documenteer naming convention
├── Gebruik URL builder templates
├── Train team op standaarden
├── Periodic audit van source/medium values
└── Maak "clean-up" custom channels

DIAGNOSE QUERY (voor exploration):
──────────────────────────────────
Dimensies:
├── Session default channel group
├── Session source
├── Session medium
├── Session campaign

Filter:
├── Channel = [probleem channel]
├── Date range: laatste 30 dagen

→ Identificeer welke source/medium combos in channel vallen
```

## Output: Channel Configuration Template

```markdown
# GA4 Channel Grouping Configuratie

## Property Information
- **GA4 Property:** [Property naam]
- **Measurement ID:** G-XXXXXXXXXX
- **Configuratie datum:** [Datum]
- **Laatst gewijzigd:** [Datum]

## Channel Overview

### Custom Channels Toegevoegd
| Channel Name | Priority | Rationale |
|--------------|----------|-----------|
| Retargeting | 1 | Separate remarketing measurement |
| Paid Search - Brand | 2 | Brand vs non-brand split |
| Affiliate | 9 | Affiliate partner tracking |
| Influencer | 10 | Creator collaborations |
| Partner | 11 | B2B partner traffic |

### Channel Volgorde
| # | Channel | Status |
|---|---------|--------|
| 1 | Retargeting | Custom |
| 2 | Paid Search - Brand | Custom |
| 3 | Paid Shopping | Default |
| 4 | Paid Search | Default (modified) |
| 5 | Paid Social | Default |
| 6 | Display | Default |
| 7 | Paid Video | Default |
| 8 | Paid Other | Default |
| 9 | Affiliate | Custom |
| 10 | Influencer | Custom |
| 11 | Partner | Custom |
| 12 | Email | Default |
| 13 | Organic Search | Default |
| 14 | Organic Social | Default |
| 15 | Referral | Default |
| 16 | Direct | Default |
| 17 | Unassigned | Default |

## Channel Rule Details

### Retargeting
| Condition Type | Field | Operator | Value |
|----------------|-------|----------|-------|
| Rule 1 | Medium | exactly matches | retargeting |
| OR Rule 2 | Campaign | contains | retargeting |
| OR Rule 3 | Campaign | contains | remarketing |

### Paid Search - Brand
| Condition Type | Field | Operator | Value |
|----------------|-------|----------|-------|
| Condition 1 | Medium | is one of | cpc, ppc, paid |
| AND Condition 2 | Source | is one of | google, bing |
| AND Condition 3 | Campaign | contains | brand |

### Affiliate
| Condition Type | Field | Operator | Value |
|----------------|-------|----------|-------|
| Rule 1 | Medium | exactly matches | affiliate |
| OR Rule 2 | Source | contains | affiliate |
| OR Rule 3 | Campaign | begins with | aff_ |

### [Additional channels...]
[Document remaining custom channel rules]

## UTM Requirements per Channel

| Channel | Required UTM | Example |
|---------|--------------|---------|
| Paid Social | medium=paid-social | utm_medium=paid-social |
| Affiliate | medium=affiliate | utm_medium=affiliate |
| Influencer | medium=influencer | utm_medium=influencer |
| Partner | medium=partner | utm_medium=partner |
| Retargeting | campaign contains "retargeting" | utm_campaign=fb-retargeting-cart |

## Testing & Verification

### Test Cases
| Test URL | Expected Channel | Actual Channel | Status |
|----------|------------------|----------------|--------|
| ?utm_source=facebook&utm_medium=paid-social | Paid Social | [Result] | ✅/❌ |
| ?utm_source=google&utm_medium=cpc&utm_campaign=brand | Paid Search - Brand | [Result] | ✅/❌ |
| ?utm_source=partner-x&utm_medium=affiliate | Affiliate | [Result] | ✅/❌ |
| ?utm_source=influencer-y&utm_medium=influencer | Influencer | [Result] | ✅/❌ |

## Traffic Distribution Analysis

### Current Distribution (Last 30 Days)
| Channel | Sessions | % of Total | Conversions |
|---------|----------|------------|-------------|
| Paid Search | [X] | [X]% | [X] |
| Paid Social | [X] | [X]% | [X] |
| Organic Search | [X] | [X]% | [X] |
| Direct | [X] | [X]% | [X] |
| Referral | [X] | [X]% | [X] |
| Unassigned | [X] | [X]% | [X] |

### Target: Unassigned < 5%
Current Unassigned: [X]% - Action needed: ✅ On target / ❌ Review UTMs

## Issues & Resolutions Log

| Date | Issue | Resolution |
|------|-------|------------|
| [Date] | [Issue description] | [How resolved] |

## Volgende Stappen
1. [ ] [Actie 1]
2. [ ] [Actie 2]
3. [ ] [Actie 3]

## Notities
[Aanvullende observaties, uitzonderingen, of speciale situaties]
```

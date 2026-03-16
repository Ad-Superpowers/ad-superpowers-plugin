---
name: ga4-remarketing-setup
description: "GA4 remarketing audiences exporteren naar Google Ads. Gebruik voor: (1) GA4 audiences activeren in Google Ads, (2) RLSA (Remarketing Lists for Search Ads) setup, (3) Display remarketing campagnes, (4) YouTube remarketing, (5) Audience sync troubleshooting. Triggers: remarketing setup, rlsa, ga4 naar google ads, audience export, remarketing lijst, display remarketing, youtube remarketing."
---

# GA4 Remarketing Setup Guide

Complete gids voor het exporteren en activeren van GA4 audiences in Google Ads voor effectieve remarketing campagnes.

## Quick Decision Tree

```
GA4 REMARKETING SETUP FLOW
│
├─► VEREISTEN CHECK
│   ├─► Google Ads account gekoppeld?
│   │   ├─► Ja → Door naar audience export
│   │   └─► Nee → Eerst koppelen (zie stap 1)
│   │
│   ├─► Google Signals enabled?
│   │   ├─► Ja → Cross-device remarketing mogelijk
│   │   └─► Nee → Alleen same-device targeting
│   │
│   └─► Personalized ads enabled?
│       ├─► Ja → Audiences kunnen exporteren
│       └─► Nee → Geen export mogelijk (activeer dit!)
│
├─► WELK REMARKETING TYPE?
│   ├─► Search (RLSA)
│   │   └─► Bid adjustments op search
│   │   └─► Minimum: 1.000 users
│   │
│   ├─► Display Network
│   │   └─► Banner remarketing
│   │   └─► Minimum: 100 users
│   │
│   ├─► YouTube
│   │   └─► Video remarketing
│   │   └─► Minimum: 1.000 users
│   │
│   └─► Discovery/Performance Max
│       └─► Cross-channel remarketing
│       └─► Minimum: 1.000 users
│
└─► WELKE AUDIENCES EXPORTEREN?
    ├─► Converters (purchase, lead)
    │   └─► Voor: cross-sell, exclusions
    │
    ├─► Cart abandoners
    │   └─► Voor: recovery campaigns
    │
    ├─► Product viewers
    │   └─► Voor: consideration campaigns
    │
    └─► Engaged visitors
        └─► Voor: awareness retargeting
```

## Stap 1: Google Ads Koppeling Verifiëren

```
GOOGLE ADS LINK VERIFICATIE
============================

LOCATIE: Admin → Product Links → Google Ads Links

VEREISTEN VOOR REMARKETING:
┌─────────────────────────────┬────────────────────────────────────────────┐
│ Setting                     │ Vereiste Status                            │
├─────────────────────────────┼────────────────────────────────────────────┤
│ Google Ads account linked   │ ✅ Active                                  │
│                             │ (Alle accounts die audiences nodig hebben) │
├─────────────────────────────┼────────────────────────────────────────────┤
│ Enable personalized         │ ✅ ON                                      │
│ advertising                 │ (KRITIEK voor audience export!)            │
├─────────────────────────────┼────────────────────────────────────────────┤
│ Auto-tagging                │ ✅ Enabled in Google Ads                   │
│                             │ (Voor correcte attribution)                │
└─────────────────────────────┴────────────────────────────────────────────┘

KOPPELING AANMAKEN (indien niet bestaand):
──────────────────────────────────────────
1. GA4: Admin → Product Links → Google Ads Links
2. Click "Link"
3. Selecteer Google Ads account(s)
4. ✅ Enable "Enable personalized advertising"
5. Click "Submit"
6. Wacht 24-48 uur voor sync

VERIFICATIE IN GOOGLE ADS:
─────────────────────────
1. Google Ads → Tools & Settings → Linked accounts
2. Zoek Google Analytics (GA4) section
3. Verify: Link status = "Active"
4. Check: "Import site metrics" = ON
```

## Stap 2: Google Signals Configureren

```
GOOGLE SIGNALS VOOR REMARKETING
===============================

WAAROM BELANGRIJK:
├── Cross-device remarketing (user op mobile → desktop)
├── Demografische targeting in Google Ads
├── Verhoogde match rates met Google users
└── Required voor sommige predictive audiences

LOCATIE: Admin → Data Settings → Data Collection

SETUP:
┌────┬────────────────────────────────────────────────────────────────────┐
│ 1  │ Ga naar Admin → Data Settings → Data Collection                   │
├────┼────────────────────────────────────────────────────────────────────┤
│ 2  │ Click "Get started" bij Google signals                            │
├────┼────────────────────────────────────────────────────────────────────┤
│ 3  │ Accept data collection terms                                      │
├────┼────────────────────────────────────────────────────────────────────┤
│ 4  │ Enable voor alle regions (of selecteer specifieke)                │
├────┼────────────────────────────────────────────────────────────────────┤
│ 5  │ Toggle: "Enable Google signals data collection" = ON              │
└────┴────────────────────────────────────────────────────────────────────┘

⚠️ GDPR OVERWEGINGEN:
├── Vereist cookie consent voor personalization
├── Consent mode moet correct geïmplementeerd zijn
├── Niet alle users worden gematched (opt-in required)
└── Kan data thresholding activeren in reports
```

## Stap 3: Audiences voor Export Configureren

```
AUDIENCE EXPORT CONFIGURATIE
============================

BIJ AUDIENCE CREATIE:
────────────────────
Wanneer je een audience aanmaakt in GA4:
├── Scroll naar "Audience destinations"
├── Selecteer: ✅ Google Ads
├── Selecteer: ✅ Alle gekoppelde accounts die audience nodig hebben
└── Save audience

BESTAANDE AUDIENCES EXPORTEREN:
──────────────────────────────
1. Ga naar Admin → Audiences
2. Click op audience naam
3. Edit → Scroll naar "Audience destinations"
4. ✅ Selecteer Google Ads accounts
5. Save

WELKE AUDIENCES EXPORTEREN:
┌─────────────────────────┬────────────┬─────────────────────────────────┐
│ Audience                │ Priority   │ Use Case                        │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ All Users               │ ★★★        │ Baseline voor exclusions        │
│                         │            │ Display prospecting             │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Purchasers (all time)   │ ★★★        │ Cross-sell, lookalikes          │
│                         │            │ RLSA bid adjustments            │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Recent purchasers       │ ★★★        │ Exclusion van acquisition       │
│ (30 days)               │            │ Cross-sell timing               │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Cart abandoners         │ ★★★        │ Recovery campaigns              │
│                         │            │ High intent retargeting         │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Product viewers         │ ★★☆        │ Consideration retargeting       │
│                         │            │ Category-specific ads           │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Engaged visitors        │ ★★☆        │ Awareness retargeting           │
│ (high session duration) │            │ Brand building                  │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Likely purchasers       │ ★★★        │ Smart Bidding optimization      │
│ (predictive)            │            │ High priority targeting         │
├─────────────────────────┼────────────┼─────────────────────────────────┤
│ Likely churners         │ ★★☆        │ Retention campaigns             │
│ (predictive)            │            │ Win-back messaging              │
└─────────────────────────┴────────────┴─────────────────────────────────┘
```

## Remarketing Types in Google Ads

### RLSA (Remarketing Lists for Search Ads)

```
RLSA SETUP
==========

WAT IS HET:
├── Pas bids aan voor GA4 audiences op Search
├── Target specifieke keywords alleen voor audiences
├── Combine audience signals met search intent
└── Geen aparte ads nodig (zelfde ads, andere bids)

MINIMUM SIZE: 1.000 users

SETUP IN GOOGLE ADS:
───────────────────
1. Ga naar Campaign → Audiences
2. Click "+ Add audience segments"
3. Browse → "Your data" → "Website visitors" (GA4)
4. Selecteer GA4 audiences
5. Kies: "Targeting" of "Observation"

TARGETING VS OBSERVATION:
┌───────────────────┬────────────────────────────────────────────────────┐
│ Mode              │ Betekenis                                          │
├───────────────────┼────────────────────────────────────────────────────┤
│ Observation       │ Audience ziet dezelfde ads, met bid adjustment     │
│                   │ └─► Start hiermee! Meet eerst performance          │
├───────────────────┼────────────────────────────────────────────────────┤
│ Targeting         │ ALLEEN audience ziet ads op deze keywords          │
│                   │ └─► Voor specifieke remarketing keywords           │
└───────────────────┴────────────────────────────────────────────────────┘

RLSA BID ADJUSTMENT STRATEGIE:
─────────────────────────────
┌─────────────────────────┬─────────────┬─────────────────────────────────┐
│ Audience                │ Bid Adj.    │ Rationale                       │
├─────────────────────────┼─────────────┼─────────────────────────────────┤
│ All converters          │ +20% to +50%│ Bewezen kopers                  │
├─────────────────────────┼─────────────┼─────────────────────────────────┤
│ Cart abandoners         │ +30% to +60%│ Hoge intent, bijna geconverteerd│
├─────────────────────────┼─────────────┼─────────────────────────────────┤
│ Product viewers         │ +10% to +25%│ Geïnteresseerd, not ready yet   │
├─────────────────────────┼─────────────┼─────────────────────────────────┤
│ Likely purchasers       │ +40% to +80%│ ML voorspelt hoge kans          │
├─────────────────────────┼─────────────┼─────────────────────────────────┤
│ Bounced visitors        │ -20% to -40%│ Lage engagement, lower value    │
└─────────────────────────┴─────────────┴─────────────────────────────────┘

⚠️ Let op: Smart Bidding past automatisch aan. Gebruik audience insights
   voor strategie, niet manual bid adjustments met Smart Bidding.
```

### Display Remarketing

```
DISPLAY REMARKETING SETUP
=========================

WAT IS HET:
├── Banner/image ads op Google Display Network
├── Reach users across millions of websites
├── Visual remarketing voor brand recall
└── Lagere CPC dan Search, hogere reach

MINIMUM SIZE: 100 users

CAMPAIGN SETUP:
──────────────
1. Google Ads → + New Campaign
2. Goal: Sales/Leads/Website traffic
3. Campaign type: Display
4. Audiences: Add GA4 audiences
5. Creatives: Responsive display ads

BEST PRACTICES:
┌────────────────────────────────────────────────────────────────────────┐
│ ✅ Frequency capping instellen (3-5 impressies/dag)                   │
│ ✅ Exclusions toevoegen (recent purchasers)                           │
│ ✅ Separate campaigns per audience tier                                │
│ ✅ Dynamic remarketing indien e-commerce                               │
│ ✅ Brand-safe placements (exclude sensitive content)                   │
│ ❌ NIET: Alle audiences in één campaign                                │
│ ❌ NIET: Onbeperkte frequency (ad fatigue!)                            │
└────────────────────────────────────────────────────────────────────────┘

DISPLAY AUDIENCE TIERS:
──────────────────────
Tier 1 (Highest intent): Cart abandoners, checkout abandoners
├── Frequency: 5-7/dag
├── Budget: Hoogste share
└── Creative: Product-focused, urgency

Tier 2 (Medium intent): Product viewers, engaged visitors
├── Frequency: 3-5/dag
├── Budget: Medium share
└── Creative: Benefits, social proof

Tier 3 (Lower intent): All visitors
├── Frequency: 2-3/dag
├── Budget: Laagste share
└── Creative: Brand awareness, value prop
```

### YouTube Remarketing

```
YOUTUBE REMARKETING SETUP
=========================

WAT IS HET:
├── Video ads voor GA4 website audiences
├── In-stream, discovery, bumper ads
├── Combine video impact met remarketing precision
└── Goede optie voor brand consideration

MINIMUM SIZE: 1.000 users

CAMPAIGN SETUP:
──────────────
1. Google Ads → + New Campaign
2. Goal: Brand awareness/Product consideration
3. Campaign type: Video
4. Audiences: Add GA4 audiences
5. Ad formats: Choose based on goal

YOUTUBE AD FORMATS:
┌───────────────────┬─────────────┬────────────────────────────────────────┐
│ Format            │ Skippable   │ Best For                               │
├───────────────────┼─────────────┼────────────────────────────────────────┤
│ In-stream         │ After 5s    │ Story-telling, longer messages         │
│ (skippable)       │             │ Pay per view (30s or completion)       │
├───────────────────┼─────────────┼────────────────────────────────────────┤
│ In-stream         │ No          │ Short, punchy messages (15s max)       │
│ (non-skippable)   │             │ Brand recall, reach                    │
├───────────────────┼─────────────┼────────────────────────────────────────┤
│ Bumper            │ No (6s)     │ Quick reminder, frequency reach        │
│                   │             │ Awareness only                         │
├───────────────────┼─────────────┼────────────────────────────────────────┤
│ Discovery         │ N/A         │ YouTube search/homepage                │
│                   │             │ High-intent video seekers              │
└───────────────────┴─────────────┴────────────────────────────────────────┘

YOUTUBE REMARKETING STRATEGIE:
─────────────────────────────
Cart abandoners → Short reminder video (15-30s)
├── Focus: Product reminder, incentive
└── CTA: Return to cart

Product viewers → Longer story video (30-60s)
├── Focus: Benefits, testimonials
└── CTA: Learn more

All visitors → Brand video (15-30s)
├── Focus: Brand values, unique selling points
└── CTA: Visit website
```

### Performance Max Remarketing

```
PERFORMANCE MAX AUDIENCE SIGNALS
================================

WAT IS HET:
├── Cross-channel automation (Search, Display, YouTube, etc.)
├── GA4 audiences als "audience signals"
├── Google's ML optimaliseert targeting
└── Signals geven hints, geen harde targeting

HOE HET WERKT:
─────────────
1. Voeg GA4 audiences toe als "audience signals"
2. Google gebruikt dit als startsignaal
3. ML expandeert naar vergelijkbare users
4. Audience is hint, niet restrictie

SETUP:
──────
1. Performance Max campaign → Asset Groups
2. Scroll naar "Audience signals"
3. Add: Your data → GA4 audiences
4. Add: Custom segments (optional)
5. Add: Demographics, interests

BEST PRACTICES:
┌────────────────────────────────────────────────────────────────────────┐
│ ✅ Voeg meerdere GA4 audiences toe (layered signals)                  │
│ ✅ Combineer met customer match lists                                  │
│ ✅ Review "Audience insights" tab voor learnings                       │
│ ✅ Aparte asset groups voor acquisition vs retention                   │
│ ❌ NIET: Verwachten dat alleen GA4 audience wordt getarget             │
│ ❌ NIET: Te weinig audiences als signals geven                         │
└────────────────────────────────────────────────────────────────────────┘

AUDIENCE SIGNAL STRATEGIE:
─────────────────────────
High-value signals (voeg eerst toe):
├── All converters (GA4)
├── High-value customers (GA4)
├── Customer match: email lists
└── Likely purchasers (predictive)

Supporting signals:
├── Product/category viewers
├── Engaged visitors
├── Cart abandoners
└── Website visitors (all)
```

## Audience Size & Match Rates

```
AUDIENCE SIZE REQUIREMENTS
==========================

MINIMUM SIZES PER NETWORK:
┌─────────────────────────┬──────────────┬─────────────────────────────────┐
│ Network                 │ Minimum      │ Recommended                     │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ Display Network         │ 100          │ 1.000+ voor consistente reach   │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ Search (RLSA)           │ 1.000        │ 5.000+ voor significante impact │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ YouTube                 │ 1.000        │ 5.000+ voor betere targeting    │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ Discovery               │ 1.000        │ 10.000+ voor schaal             │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ Gmail                   │ 1.000        │ 5.000+ voor deliverability      │
├─────────────────────────┼──────────────┼─────────────────────────────────┤
│ Similar/Lookalike       │ 1.000+       │ 5.000+ voor ML optimization     │
└─────────────────────────┴──────────────┴─────────────────────────────────┘

MATCH RATE FACTOREN:
───────────────────
GA4 audience size ≠ Google Ads audience size

Typische match rates: 30-70%

Factoren die match rate beïnvloeden:
├── Google Signals enabled (hoger = betere match)
├── Cross-device tracking (meer touchpoints = betere match)
├── Consent mode (meer consents = hogere match)
├── User login status (logged in = hogere match)
└── Region (EU/GDPR = lagere match)

MATCH RATE VERBETEREN:
─────────────────────
├── Enable Google Signals
├── Implement consent mode correctly
├── Encourage user login
├── Use customer match supplemental lists
└── Extend membership duration (more users accumulate)
```

## Best Practices

```
DO's ✅
═══════
├── Start met "Observation" mode, niet "Targeting"
│   └─► Verzamel data eerst voordat je restricts
│
├── Layer audiences met exclusions
│   └─► Target cart abandoners EXCLUDE converters
│
├── Match creative aan audience intent
│   └─► Cart abandoners → "Forgot something?" messaging
│
├── Set frequency caps
│   └─► Voorkom ad fatigue en annoyance
│
├── Segment audiences in tiers
│   └─► High/medium/low intent met verschillende bids
│
├── Monitor list sizes dagelijks
│   └─► Catch tracking issues vroeg
│
└── Combineer met customer match
    └─► Email lists + GA4 = betere coverage

DON'Ts ❌
════════
├── Export ALLE audiences naar Google Ads
│   └─► Focus op actionable audiences
│
├── Vergeten om recent converters te excluden
│   └─► Irritant en waste of budget
│
├── Identical messaging voor alle audiences
│   └─► Cart abandoners ≠ new visitors
│
├── Te korte membership durations
│   └─► Audiences te klein voor effectiveness
│
├── Geen frequency capping
│   └─► Creepy en negative brand impact
│
└── Vertrouwen op GA4 size = Google Ads size
    └─► Match rates zorgen voor verschil
```

## Troubleshooting

```
TROUBLESHOOTING GUIDE
=====================

PROBLEEM: Audiences niet zichtbaar in Google Ads
────────────────────────────────────────────────
Oorzaken:
├── Google Ads link niet actief
├── Personalized ads niet enabled
├── Sync delay (24-48 uur)
├── Audience niet gemarkeerd voor export
└── Google Ads account niet geselecteerd

Oplossing:
├── GA4: Admin → Product Links → Google Ads → Status check
├── Verify "Personalized advertising" = ON
├── Check audience settings: Destinations → Google Ads ✅
├── Wacht 48 uur na configuratie
└── Refresh Google Ads Audience Manager

PROBLEEM: Audience size veel kleiner in Google Ads
──────────────────────────────────────────────────
Oorzaken:
├── Match rate tussen GA4 en Google identity
├── Google Signals niet enabled
├── Consent mode beperkt matching
├── Cross-device gaps
└── Normaal: 30-70% match rate

Oplossing:
├── Enable Google Signals
├── Review consent implementation
├── Extend membership duration
├── Supplementeer met customer match
└── Accepteer dat dit normaal is

PROBLEEM: "List too small" error in Google Ads
──────────────────────────────────────────────
Oorzaken:
├── Audience onder minimum threshold
├── Match rate te laag
├── Recent aangemaakte audience
└── Te restrictieve condities

Oplossing:
├── Wacht op meer users (accumulation time)
├── Verbreed audience condities
├── Verleng membership duration
├── Combineer meerdere kleine audiences
└── Start met bredere targeting, narrow later

PROBLEEM: Remarketing performance laag
──────────────────────────────────────
Oorzaken:
├── Verkeerde audience/campaign match
├── Creative niet relevant voor audience
├── Frequency te hoog (ad fatigue)
├── Attributie window te kort
└── Competition in audience segment

Oplossing:
├── Align creative met audience intent
├── Lower frequency cap
├── Test verschillende audiences
├── Extend conversion window
├── Review exclusions (converters included?)

PROBLEEM: Audience stops updating
─────────────────────────────────
Oorzaken:
├── GA4 tracking broken
├── Consent rates dropped
├── Website traffic decreased
├── Event triggering issues
└── Link between GA4/Google Ads broken

Oplossing:
├── Check GA4 realtime report
├── Verify event tracking in DebugView
├── Confirm Google Ads link still active
├── Review consent implementation
└── Test audience condities handmatig
```

## Output: Remarketing Setup Recommendation Template

```markdown
# GA4 Remarketing Setup Rapport

## Account Koppeling Status
| Setting | Status | Account ID |
|---------|--------|------------|
| Google Ads Link | [✅/❌] | [XXX-XXX-XXXX] |
| Personalized Ads | [✅/❌] | - |
| Google Signals | [✅/❌] | - |
| Auto-tagging | [✅/❌] | - |

## Audiences voor Export

### Priority 1: Core Remarketing
| Audience | GA4 Size | Est. Ads Size | Export Status |
|----------|----------|---------------|---------------|
| All Converters | [X] | [X] | [✅/❌] |
| Cart Abandoners | [X] | [X] | [✅/❌] |
| Product Viewers | [X] | [X] | [✅/❌] |

### Priority 2: Advanced Segments
| Audience | GA4 Size | Est. Ads Size | Export Status |
|----------|----------|---------------|---------------|
| Likely Purchasers | [X] | [X] | [✅/❌] |
| High-Value Customers | [X] | [X] | [✅/❌] |
| [Custom Audience] | [X] | [X] | [✅/❌] |

## Campaign Recommendations

### RLSA (Search)
| Audience | Bid Adjustment | Rationale |
|----------|---------------|-----------|
| [Audience 1] | +[X]% | [Reden] |
| [Audience 2] | +[X]% | [Reden] |

### Display Remarketing
| Tier | Audience | Frequency Cap | Budget % |
|------|----------|---------------|----------|
| 1 (High intent) | [Audience] | [X]/dag | [X]% |
| 2 (Medium) | [Audience] | [X]/dag | [X]% |
| 3 (Low) | [Audience] | [X]/dag | [X]% |

### YouTube (Optional)
| Audience | Ad Format | Length | Focus |
|----------|-----------|--------|-------|
| [Audience] | [Format] | [Xs] | [Message focus] |

## Exclusions Setup
| From Campaign | Exclude Audience | Reden |
|---------------|------------------|-------|
| [Campaign] | Recent Purchasers | Prevent waste |
| [Campaign] | [Audience] | [Reden] |

## Monitoring Checklist
- [ ] Weekly audience size check
- [ ] Match rate monitoring
- [ ] Performance per audience tier
- [ ] Frequency cap effectiveness
- [ ] Creative fatigue signals

## Actie Items
1. [ ] [Eerste actie]
2. [ ] [Tweede actie]
3. [ ] [Derde actie]

## Notities
[Specifieke aanbevelingen of context]
```

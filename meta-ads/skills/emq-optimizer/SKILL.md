---
name: emq-optimizer
description: "Meta Event Match Quality (EMQ) optimizer voor betere user matching. Gebruik voor: (1) EMQ score analyseren en verbeteren, (2) Customer Information Parameters optimaliseren, (3) Advanced Matching configureren, (4) Matching diagnostiek, (5) EMQ troubleshooting. Triggers: EMQ, Event Match Quality, matching, user match, customer parameters, advanced matching, match rate."
---

# EMQ Optimizer

Optimizer voor Meta's Event Match Quality (EMQ) score om user matching en attribution te verbeteren.

## Wat Is EMQ?

Event Match Quality meet hoe goed Meta conversie events kan matchen aan Facebook/Instagram gebruikers.

```
EMQ Score Schaal: 0-10

Score Interpretatie:
├── 0-3: Poor - Veel gemiste matches
├── 4-5: OK - Basis matching, verbetering nodig
├── 6-7: Good - Goede match rate
├── 8-10: Great - Optimale matching
└── Target: 7+ voor Purchase events
```

## Waarom EMQ Cruciaal Is

```
Hogere EMQ = Beter:
├── Meer accurate attribution
├── Betere algoritme optimization
├── Hogere reported ROAS
├── Betere audience building
└── Effectievere retargeting

Lage EMQ Impact:
├── Gemiste conversies in reporting
├── Algoritme optimaliseert op incomplete data
├── Underreported ROAS
├── Zwakkere lookalike audiences
└── Minder effectieve retargeting
```

## EMQ Check Workflow

```
STAP 1: Check huidige EMQ
└── Events Manager → Pixel → Event → Details → Match Quality

STAP 2: Identify gaps
└── Welke parameters ontbreken?

STAP 3: Implement verbeteringen
└── Voeg ontbrekende parameters toe

STAP 4: Monitor resultaat
└── EMQ update duurt 24-72 uur
```

## Customer Information Parameters (CIPs)

### Parameter Impact Ranking

| Parameter | Code | Impact | Beschrijving |
|-----------|------|--------|--------------|
| **Email** | em | Zeer Hoog | Belangrijkste matcher |
| **Phone** | ph | Zeer Hoog | Bijna even belangrijk als email |
| **First Name** | fn | Hoog | Versterkt andere matches |
| **Last Name** | ln | Hoog | Versterkt andere matches |
| **External ID** | external_id | Hoog | Persistent user identifier |
| **City** | ct | Medium | Location matching |
| **State** | st | Medium | Location matching |
| **Zip Code** | zp | Medium | Location matching |
| **Country** | country | Medium | Location matching |
| **Date of Birth** | db | Medium | Extra identifier |
| **Gender** | ge | Medium | Extra identifier |
| **Client IP** | client_ip_address | Basis | Vereist voor server events |
| **User Agent** | client_user_agent | Basis | Vereist voor server events |
| **Click ID** | fbc | Hoog | Facebook click identifier |
| **Browser ID** | fbp | Hoog | Facebook browser identifier |

### Prioriteit Volgorde voor Implementatie

```
FASE 1 - Essentials (Verwacht EMQ: 5-6)
├── Email (em)
├── Client IP Address
├── User Agent
├── fbc (Facebook Click ID - from URL)
└── fbp (Facebook Browser ID - from cookie)

FASE 2 - High Impact (Verwacht EMQ: 7-8)
├── Phone Number (ph)
├── First Name (fn)
├── Last Name (ln)
└── External ID (customer ID)

FASE 3 - Optimization (Verwacht EMQ: 8-10)
├── City (ct)
├── State (st)
├── Zip Code (zp)
├── Country (country)
├── Date of Birth (db)
└── Gender (ge)
```

## Advanced Matching Setup

### Automatic Advanced Matching (AAM)

```
Wat het doet:
Meta leest automatisch form fields en matcht data

Setup (2 minuten):
1. Events Manager → Data Sources → Pixel
2. Settings → Advanced Matching
3. Toggle "Automatic Advanced Matching" ON
4. Review detected fields
5. Done

Detecteert automatisch:
├── Email fields
├── Phone fields
├── Name fields
├── Address fields
└── Form submissions
```

### Manual Advanced Matching

**Browser-side (Pixel):**

```javascript
// Init met user data
fbq('init', 'PIXEL_ID', {
  em: 'john@example.com',          // Email (wordt automatisch gehashed)
  fn: 'john',                       // First name
  ln: 'doe',                        // Last name
  ph: '31612345678',               // Phone (met landcode, geen +)
  external_id: 'customer_12345',    // Your customer ID
  ge: 'm',                          // Gender: m/f
  db: '19900115',                   // DOB: YYYYMMDD
  ct: 'amsterdam',                  // City (lowercase)
  st: 'nh',                         // State/Province
  zp: '1012',                       // Zip code
  country: 'nl'                     // Country (ISO 2-letter)
});
```

**Server-side (CAPI):**

```json
{
  "user_data": {
    "em": ["ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"],
    "ph": ["ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"],
    "fn": ["ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"],
    "ln": ["ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"],
    "external_id": ["customer_12345"],
    "client_ip_address": "192.168.1.1",
    "client_user_agent": "Mozilla/5.0...",
    "fbc": "fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890",
    "fbp": "fb.1.1558571054389.1098115397"
  }
}
```

## Hashing Requirements

### Correct Hashen (CAPI)

```
HASHING REGELS:
1. Gebruik SHA256
2. Lowercase alles VOOR hashing
3. Trim whitespace
4. Remove special characters (phone)
5. Hash elke parameter apart

VOORBEELD PYTHON:
import hashlib

def hash_parameter(value):
    if not value:
        return None
    # Lowercase, trim, encode
    normalized = str(value).lower().strip()
    # SHA256 hash
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()

# Correct:
email = "John.Doe@Example.com"
hashed = hash_parameter(email)  # Hash van "john.doe@example.com"

# Phone normalisatie:
phone = "+31 6 12345678"
normalized_phone = ''.join(filter(str.isdigit, phone))  # "31612345678"
hashed_phone = hash_parameter(normalized_phone)
```

### Pixel Hashing

```
PIXEL HASHING (Automatisch):
- fbq() hashed automatisch als je raw values stuurt
- Je kunt ook pre-hashed sturen

Pre-hashed sturen:
fbq('init', 'PIXEL_ID', {
  em: 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
});

Of raw (auto-hashed):
fbq('init', 'PIXEL_ID', {
  em: 'john@example.com'  // Meta hashed dit automatisch
});
```

## fbc en fbp Parameters

### Facebook Click ID (fbc)

```
Wat het is:
Tracking parameter die Meta toevoegt aan URLs na ad click

Waar te vinden:
URL: https://yoursite.com/?fbclid=AbCdEfGhIjKlMnOp...

Hoe te gebruiken:
1. Capture fbclid uit URL
2. Sla op in first-party cookie
3. Stuur als fbc parameter

Format:
fbc = fb.{version}.{creation_time}.{fbclid}
Voorbeeld: fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz
```

### Facebook Browser ID (fbp)

```
Wat het is:
First-party cookie die Pixel automatisch set

Waar te vinden:
Cookie: _fbp

Hoe te gebruiken:
1. Lees _fbp cookie
2. Stuur mee met CAPI events

Format:
fbp = fb.{version}.{creation_time}.{random_number}
Voorbeeld: fb.1.1558571054389.1098115397
```

### Implementation

```javascript
// JavaScript helper
function getFacebookParams() {
  const cookies = document.cookie.split(';');
  let fbp = null;
  let fbc = null;

  cookies.forEach(cookie => {
    const [name, value] = cookie.trim().split('=');
    if (name === '_fbp') fbp = value;
    if (name === '_fbc') fbc = value;
  });

  // Als fbc niet in cookie, check URL
  if (!fbc) {
    const urlParams = new URLSearchParams(window.location.search);
    const fbclid = urlParams.get('fbclid');
    if (fbclid) {
      fbc = `fb.1.${Date.now()}.${fbclid}`;
    }
  }

  return { fbp, fbc };
}
```

## EMQ Diagnostic Framework

### Score Analysis

```
HUIDIGE EMQ: [score]

SCORE < 4 (Poor):
├── Check: Is CAPI actief?
├── Check: Zijn basis parameters aanwezig? (IP, UA)
├── Check: Wordt email/phone meegestuurd?
└── Actie: Implementeer Fase 1 parameters

SCORE 4-5 (OK):
├── Check: Ontbreken email OF phone?
├── Check: Worden fbc/fbp meegestuurd?
├── Check: Hashing correct?
└── Actie: Voeg ontbrekende high-impact params toe

SCORE 6-7 (Good):
├── Check: Alle Fase 1+2 parameters aanwezig?
├── Check: Advanced Matching enabled?
├── Check: Multiple parameters per event?
└── Actie: Voeg Fase 3 parameters toe

SCORE 8-10 (Great):
├── Behoud huidige setup
├── Monitor voor degradatie
└── Document configuratie
```

### Common EMQ Issues

| Issue | Symptoom | Oplossing |
|-------|----------|-----------|
| Email niet gehashed | EMQ laag ondanks email | Verify hashing (SHA256, lowercase) |
| Phone format fout | Phone parameter ignored | Remove +, spaces, use digits only |
| fbc/fbp missing | EMQ 1-2 punten lager | Capture en stuur mee |
| CAPI only | EMQ matig | Enable Pixel + AAM ook |
| Parameters null | Events zonder user data | Check data layer population |

### Troubleshooting Checklist

```
□ Events Manager → Diagnostics → Match Quality
  └── Toont welke parameters ontvangen worden

□ Test Events tool
  └── Stuur test event, check parameters

□ Browser Developer Tools
  └── Network tab → Check pixel requests

□ CAPI Response Logging
  └── Log API responses, check errors

□ Parameter Verification
  └── Per event: welke params zijn gevuld?
```

## EMQ Improvement Plan Template

```markdown
# EMQ Improvement Plan

## Current State
- EMQ Score: [score]
- Event: [event name]
- Current parameters: [lijst]

## Gap Analysis
| Parameter | Beschikbaar? | In Data Layer? | Meegestuurd? |
|-----------|--------------|----------------|--------------|
| Email | [ja/nee] | [ja/nee] | [ja/nee] |
| Phone | [ja/nee] | [ja/nee] | [ja/nee] |
| ... | ... | ... | ... |

## Improvement Actions

### Quick Wins (Week 1)
1. Enable Automatic Advanced Matching
2. Add fbc/fbp to CAPI events
3. [andere quick wins]

### Implementation (Week 2-3)
1. Add missing parameters to data layer
2. Update CAPI payload
3. Verify hashing
4. Test deduplication

### Expected Result
- Current EMQ: [X]
- Target EMQ: [Y]
- Timeline: [2-4 weken]

## Verification
□ Test event met alle parameters
□ Events Manager toont parameters
□ EMQ score verbeterd (24-72 uur)
□ Attribution improvement zichtbaar
```

## Platform-Specific Tips

### Shopify

```
Native integration:
- AAM automatisch enabled met "Maximum" data sharing
- Customer info automatisch meegestuurd
- Verify in Events Manager

Extra verbetering:
- Ensure checkout forms complete
- Use logged-in customer data
- Check app settings voor advanced options
```

### WooCommerce

```
Met plugin:
- Enable "Advanced Matching" in plugin settings
- Configure welke velden te sturen
- Check user profile data population

Extra verbetering:
- Ensure account creation bij checkout
- Capture phone number (vaak optioneel)
- Add birthday field indien relevant
```

### Custom Implementation

```
Data layer requirements:
- Populate user object op alle relevante pages
- Include in checkout/conversion events
- Persist customer ID across sessions

CAPI checklist:
- Hash alle PII correct
- Include fbc/fbp
- Log en verify payload
```

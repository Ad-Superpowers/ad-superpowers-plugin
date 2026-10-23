---
name: meta-emq-optimizer
description: "This skill should be used when the user asks to \"improve EMQ score\", \"optimize event match quality\", \"configure Advanced Matching\", or mentions \"EMQ\", \"Customer Information Parameters\", or \"match quality diagnostics\". Do NOT use for: CAPI implementation (use capi-implementation-guide), attribution window configuration (use attribution-window-advisor), pixel installation issues (use performance-troubleshooter)."
---
# EMQ Optimizer

Optimizer for Meta's Event Match Quality (EMQ) score to improve user matching and attribution.

## What Is EMQ?

Event Match Quality is Meta's score (out of 10; Conversions API docs, sources below) for how effective the customer information in your server events (Conversions API) may be at matching them to a Meta account. Meta shows it for web events only, per event in Events Manager.

```
EMQ Score Scale: out of 10

Score Interpretation:
├── 1-3: Poor - Many missed matches
├── 4-5: OK - Basic matching, improvement needed
├── 6-7: Good - Good match rate
├── 8-10: Great - Optimal matching
├── Meta: aim for 6.0 or higher where possible
├── Meta: aim for a "Good" or "Great" rating in Events Manager
└── Our target: 7+ for Purchase events
```

Rules of thumb, not Meta figures: check them against the account's own history. This covers the score bands and
the 7+ target for Purchase events; the Meta pages cited here give no score ranges for its ratings, so read the
rating in Events Manager. The 6.0 line is Meta's: "Where possible, we typically recommend that you aim for an
Event Match Quality score of 6.0 or higher" ("Verifying Your Setup", Conversions API docs, Meta for Developers; scope and scale: "Best
Practices" and "Dataset Quality API" in the same docs). The rating advice is from "Monitor Your Conversions API
Gateway Setup" (Meta for Developers:
"An EMQ designation of 'Good' or 'Great' is considered to be optimal"; all checked 2026-10-10).

## Why EMQ Is Crucial

```
Higher EMQ = Better:
├── More accurate attribution
├── Better algorithm optimization
├── Can help decrease cost per action (Meta)
├── Better audience building
└── More effective retargeting

Low EMQ Impact:
├── Missed conversions in reporting
├── Algorithm optimizes on incomplete data
├── Underreported ROAS
├── Weaker lookalike audiences
└── Less effective retargeting
```

## EMQ Check Workflow

```
STEP 1: Check current EMQ
└── meta_query(account_id, "dataset_quality", entity_id=<pixel_id>), or Events Manager → Pixel → Overview → Event

STEP 2: Identify gaps
└── Which parameters are missing? (match_key_feedback in dataset_quality, or event → View Details → Event Matching tab)

STEP 3: Implement improvements
└── Add missing parameters

STEP 4: Monitor results
└── Recheck after 1-2 days (Meta: wait 1-2 days for EMQ to update in Events Manager)
```

Timing: "Signals Gateway: Enhance Events with Advanced Matching Data", Meta for Developers
(checked 2026-10-10).

## Customer Information Parameters (CIPs)

### Parameter Impact Ranking

| Parameter | Code | Impact | Description |
|-----------|------|--------|-------------|
| **Email** | em | Very High | High-quality parameter per Meta |
| **Phone** | ph | Very High | High-quality parameter per Meta; include the country code |
| **First Name** | fn | High | High-quality parameter per Meta (with ln) |
| **Last Name** | ln | High | High-quality parameter per Meta (with fn) |
| **External ID** | external_id | High | Meta asks for it on all events; same value in Pixel and CAPI |
| **City** | ct | Medium | Location matching |
| **State** | st | Medium | Location matching |
| **Zip Code** | zp | Medium | Location matching |
| **Country** | country | Medium | Location matching |
| **Date of Birth** | db | Medium | Extra identifier |
| **Gender** | ge | Medium | Extra identifier |
| **Client IP** | client_ip_address | High | High-quality parameter per Meta; never hash; send the real IP |
| **User Agent** | client_user_agent | Basic | Required for website events; never hash |
| **Click ID** | fbc | High | Meta click ID (_fbc cookie or fbclid); never hash |
| **Browser ID** | fbp | High | Meta browser ID (_fbp cookie); never hash |

Rules of thumb, not Meta figures: check them against the account's own history. The Impact column and the phases
below are our ranking. Meta names email, IP address, first and last name and phone as examples of high-quality
customer information parameters, and asks for external_id and event_id on all events ("Best Practices",
Conversions API docs, Meta for Developers).
Required, hashing and format rules: "Customer Information Parameters"
(both checked 2026-10-10).

### Implementation Priority Order

```
PHASE 1 - Essentials
├── Email (em)
├── Client IP Address
├── User Agent
├── External ID (customer ID; Meta asks for it on all events)
├── fbc (Facebook Click ID - from URL)
└── fbp (Facebook Browser ID - from cookie)

PHASE 2 - High Impact
├── Phone Number (ph)
├── First Name (fn)
└── Last Name (ln)

PHASE 3 - Optimization
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
What it does:
Meta automatically reads form fields and matches data

Setup:
1. Events Manager → Data Sources → Pixel
2. Settings → Advanced Matching
3. Toggle "Automatic Advanced Matching" ON
4. Review detected fields
5. Done

Fields it can share (automatic_matching_fields in the Marketing API):
├── Email, phone
├── First and last name
├── City, state, zip, country
├── Gender, date of birth
└── External ID
```

Advanced Matching adds customer information to Pixel (browser) events. EMQ scores the customer information in
server (Conversions API) events, so send the same parameters with your CAPI events as well. With the Conversions
API Gateway, which passes Pixel events on to Meta from the server, Meta's gateway docs suggest turning on
Automatic Advanced Matching first and Manual Advanced Matching next when EMQ is low (see Timing source above).
Field list: AdsPixel reference, Meta for Developers (checked 2026-10-10). `meta_query(account_id, "adspixels")` shows whether it is on (`enable_automatic_matching`).

### Manual Advanced Matching

**Browser-side (Pixel):**

```javascript
// Init with user data
fbq('init', 'PIXEL_ID', {
  em: 'john@example.com',          // Email (auto-hashed)
  fn: 'john',                       // First name
  ln: 'doe',                        // Last name
  ph: '31612345678',               // Phone (with country code, no +)
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

### Correct Hashing (CAPI)

```
HASHING RULES:
1. Use SHA256
2. Lowercase everything BEFORE hashing
3. Trim whitespace
4. Phone: digits only, with country code, no leading zeros
5. Hash each parameter separately
6. Never hash client_ip_address, client_user_agent, fbc or fbp

EXAMPLE PYTHON:
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
hashed = hash_parameter(email)  # Hash of "john.doe@example.com"

# Phone normalization:
phone = "+31 6 12345678"
normalized_phone = ''.join(filter(str.isdigit, phone))  # "31612345678"
hashed_phone = hash_parameter(normalized_phone)
```

### Pixel Hashing

```
PIXEL HASHING (Automatic):
- fbq() hashes automatically when raw values are sent
- Pre-hashed values are also accepted

Sending pre-hashed:
fbq('init', 'PIXEL_ID', {
  em: 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
});

Or raw (auto-hashed):
fbq('init', 'PIXEL_ID', {
  em: 'john@example.com'  // Meta hashes this automatically
});
```

## fbc and fbp Parameters

### Facebook Click ID (fbc)

```
What it is:
Tracking parameter Meta adds to URLs after ad click

Where to find:
URL: https://yoursite.com/?fbclid=AbCdEfGhIjKlMnOp...

How to use:
1. Capture fbclid from URL
2. Store in first-party cookie
3. Send as fbc parameter
4. Keep fbclid exactly as it is (it is case sensitive)

Format:
fbc = fb.{subdomain_index}.{creation_time}.{fbclid}
(creation_time in milliseconds; subdomain_index 1 if you build it on a server)
Example: fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz
```

### Facebook Browser ID (fbp)

```
What it is:
First-party cookie that Pixel automatically sets (when it uses first-party cookies)

Where to find:
Cookie: _fbp

How to use:
1. Read _fbp cookie
2. Send with CAPI events

Format:
fbp = fb.{subdomain_index}.{creation_time}.{random_number}
Example: fb.1.1558571054389.1098115397
```

Formats: "fbp and fbc Parameters", Conversions API docs, Meta for Developers
(checked 2026-10-10).

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

  // If fbc not in cookie, check URL
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

Rules of thumb, not Meta figures: check them against the account's own history. The bands below are ours; Meta's
own line is 6.0 or higher where possible.

```
CURRENT EMQ: [score]

SCORE < 4 (Poor):
├── Check: Is CAPI active?
├── Check: Are basic parameters present? (IP, UA)
├── Check: Is email/phone being sent?
└── Action: Implement Phase 1 parameters

SCORE 4-5 (OK):
├── Check: Missing email OR phone?
├── Check: Are fbc/fbp being sent?
├── Check: Hashing correct?
└── Action: Add missing high-impact params

SCORE 6-7 (Good):
├── Check: All Phase 1+2 parameters present?
├── Check: Same customer fields sent with CAPI as with Advanced Matching?
├── Check: Multiple parameters per event?
└── Action: Add Phase 3 parameters

SCORE 8-10 (Great):
├── Maintain current setup
├── Monitor for degradation
└── Document configuration
```

### Common EMQ Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| Email not hashed | EMQ low despite email | Verify hashing (SHA256, lowercase) |
| Phone format wrong | Phone parameter ignored | Digits only, with country code, no leading zeros |
| fbc/fbp missing | Lower EMQ than with them | Capture and send along |
| CAPI only | No _fbp cookie (the Pixel sets it) | Run the Pixel too (Meta's redundant setup) and send _fbp/_fbc with CAPI |
| Parameters null | Events without user data | Check data layer population |

### Troubleshooting Checklist

```
□ Events Manager → event → View Details → Event Matching tab
  └── Details per customer information parameter

□ Test Events tool
  └── Send test event, check parameters

□ Browser Developer Tools
  └── Network tab → Check pixel requests

□ CAPI Response Logging
  └── Log API responses, check errors

□ Parameter Verification
  └── Per event: which params are populated?
```

## MCP: Check Current EMQ and Event Volume

EMQ comes from meta_query with entity_type "dataset_quality" (Meta's Dataset Quality API, web events only): per
event the composite_score, match_key_feedback (coverage per identifier), dedupe_key_feedback and data_freshness.
Status "unavailable" means Meta denied the connected user access to the dataset, not that tracking is poor.

```python
# Cross-check ROAS: events Meta cannot match are harder to attribute, so low EMQ can show as lower reported ROAS
meta_get_insights(account_id="act_XXXXX", level="campaign", date_preset="last_7d", fields=["spend","website_purchase_roas","actions"])

# Pixel settings: last_fired_time, enable_automatic_matching, automatic_matching_fields, first_party_cookie_status
meta_query(account_id="act_XXXXX", entity_type="adspixels")

# EMQ, match keys, dedup and freshness per web event (pixel id from adspixels)
meta_query(account_id="act_XXXXX", entity_type="dataset_quality", entity_id="<pixel_id>")
```

> **EMQ target:** Meta's Conversions API docs say: "Where possible, we typically recommend that you aim for an Event Match Quality score of 6.0 or higher", and that a high score "can help decrease your cost per action" ("Verifying Your Setup", Meta for Developers, checked 2026-10-10). The 7+ target for Purchase events is our rule of thumb, not a Meta figure.

## EMQ Improvement Plan Template

```markdown
# EMQ Improvement Plan

## Current State
- EMQ Score: [score]
- Event: [event name]
- Current parameters: [list]

## Gap Analysis
| Parameter | Available? | In Data Layer? | Being Sent? |
|-----------|------------|----------------|-------------|
| Email | [yes/no] | [yes/no] | [yes/no] |
| Phone | [yes/no] | [yes/no] | [yes/no] |
| ... | ... | ... | ... |

## Improvement Actions

### Quick Wins (Week 1)
1. Send the Advanced Matching fields with CAPI events too (AAM adds them to Pixel events only)
2. Add fbc/fbp to CAPI events
3. [other quick wins]

### Implementation (Week 2-3)
1. Add missing parameters to data layer
2. Update CAPI payload
3. Verify hashing
4. Test deduplication

### Expected Result
- Current EMQ: [X]
- Target EMQ: [Y]
- Timeline: [2-4 weeks]

## Verification
□ Test event with all parameters
□ Events Manager shows parameters
□ EMQ score improved (recheck after 1-2 days)
□ Attribution improvement visible
```

## Platform-Specific Tips

### Shopify

```
Native integration:
- "Enhanced" and "Maximum" data sharing use the Conversions API
- Customer info automatically sent
- Verify in Events Manager

Extra improvement:
- Ensure checkout forms are complete
- Use logged-in customer data
- Check app settings for advanced options
```

Per the Shopify Help Center, the "Enhanced" and "Maximum" levels share name, location, email and phone to match
users; "Standard" is Pixel only
(https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/meta-data-sharing, checked 2026-10-10).

### WooCommerce

```
With plugin:
- Enable advanced matching if the plugin offers it
- Configure which fields to send
- Check user profile data population

Extra improvement:
- Ensure account creation at checkout
- Capture phone number (often optional)
- Add birthday field if relevant
```

### Custom Implementation

```
Data layer requirements:
- Populate user object on all relevant pages
- Include in checkout/conversion events
- Persist customer ID across sessions

CAPI checklist:
- Hash all PII correctly
- Include fbc/fbp
- Log and verify payload
```

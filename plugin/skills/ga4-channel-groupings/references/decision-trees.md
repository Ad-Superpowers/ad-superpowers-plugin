## Quick Decision Tree

```
CHANNEL GROUPING DECISION
│
├─► WHY CUSTOM CHANNELS?
│   ├─► Default channels don't match business
│   │   └─► Example: Affiliate traffic in "Referral"
│   │   └─► Solution: Custom "Affiliate" channel
│   │
│   ├─► Split branded vs non-branded
│   │   └─► Example: See brand search separately
│   │   └─► Solution: Custom "Paid Brand" channel
│   │
│   ├─► Track partner traffic separately
│   │   └─► Example: Resellers, distributors
│   │   └─► Solution: Custom "Partner" channel
│   │
│   └─► Report specific campaigns separately
│       └─► Example: Influencer marketing
│       └─► Solution: Custom "Influencer" channel
│
├─► HOW DO GA4 CHANNELS WORK?
│   ├─► Default Channel Group (system-defined)
│   │   └─► 18 standard channels
│   │   └─► Based on source/medium rules
│   │
│   ├─► Primary Channel Group (editable)
│   │   └─► Copy of default you can customize
│   │   └─► Becomes default in reports
│   │
│   └─► Custom Channel Groups
│       └─► Fully self-defined
│       └─► Up to 2 extra custom groups (free GA4)
│
└─► WHEN TO CREATE CUSTOM GROUP?
    ├─► Traffic doesn't fit in default channels
    ├─► Business needs unique categories
    ├─► Reporting requirements are specific
    └─► Marketing teams want different grouping
```

## Troubleshooting Channel Issues

```
CHANNEL TROUBLESHOOTING GUIDE
===============================

PROBLEM: Traffic in "Unassigned"
─────────────────────────────────
Causes:
├── UTM parameters not correct
├── Medium not recognized
├── Source not in standard lists
└── Special characters in values

Diagnosis:
├── GA4 → Explorations → Traffic source report
├── Filter on "Unassigned" channel
├── Look at source/medium combinations
└── Identify pattern

Solution:
├── Fix UTM parameters at source
├── Add custom channel rule
├── Update naming convention
└── Create catch-all rule for this type

PROBLEM: Traffic in wrong channel
──────────────────────────────────
Causes:
├── Channel order incorrect
├── Rule too broad/too narrow
├── Medium not consistent
└── Conflicting campaign names

Diagnosis:
├── Test with exploration: what matches which rule?
├── Review channel order
├── Check rule specificity
└── Trace specific traffic source

Solution:
├── Reorder channels (specific → general)
├── Make rules more specific
├── Enforce naming convention
└── Add exclusion rules

PROBLEM: Paid Social in "Referral"
───────────────────────────────────
Causes:
├── UTM medium not "paid-social" or "cpc"
├── No UTM parameters
├── Platform click ID only (fbclid, etc.)
└── Medium is "referral" or "social"

Solution:
├── Check UTM template in ad platform
├── Use medium=paid-social
├── Verify UTM parameters remain in URL
└── Add custom rule: Source=facebook → Paid Social

PROBLEM: Direct traffic too high
─────────────────────────────────
Causes:
├── Missing UTM parameters
├── HTTPS → HTTP redirect (strips referrer)
├── Mobile app traffic
├── Dark social (messaging apps)
├── Bookmarks and typed URLs
└── JavaScript redirect without params

Solution:
├── Audit all campaign URLs for UTM
├── Ensure HTTPS throughout
├── Implement app deep link tracking
├── Accept 15-25% direct is normal
└── Use link shorteners with tracking

PROBLEM: Inconsistent source/medium
─────────────────────────────────────
Causes:
├── Different team members, different UTMs
├── Case-sensitivity issues
├── Platform dynamic params differ
└── No enforced naming convention

Solution:
├── Create and document naming convention
├── Use URL builder templates
├── Train team on standards
├── Periodic audit of source/medium values
└── Create "clean-up" custom channels

DIAGNOSIS QUERY (for exploration):
──────────────────────────────────
Dimensions:
├── Session default channel group
├── Session source
├── Session medium
├── Session campaign

Filter:
├── Channel = [problem channel]
├── Date range: last 30 days

→ Identify which source/medium combos fall in channel
```
# Meta Ads Naming Conventions Reference

## Waarom Naming Conventions?

Goede naming conventions zorgen voor:
- Snelle identificatie in Ads Manager
- Makkelijke filtering en rapportage
- Consistentie bij teamwork
- Betere integratie met analytics tools

## Aanbevolen Structuur

### Campaign Level

```
[Brand]_[Objective]_[Funnel]_[Geo]_[MMYY]
```

| Component | Opties | Voorbeeld |
|-----------|--------|-----------|
| Brand | Bedrijfsnaam of afkorting | `Acme`, `ACM` |
| Objective | `Conv`, `Traffic`, `Awareness`, `Leads`, `Engagement` | `Conv` |
| Funnel | `TOFU`, `MOFU`, `BOFU`, `Retarget` | `BOFU` |
| Geo | ISO landcode | `NL`, `BE`, `DACH` |
| MMYY | Maand/jaar | `0126` |

**Voorbeeld**: `Acme_Conv_BOFU_NL_0126`

### Ad Set Level

```
[AudienceType]_[AudienceDetail]_[Placement]
```

| Component | Opties | Voorbeeld |
|-----------|--------|-----------|
| AudienceType | `LAL`, `Interest`, `Retarget`, `Broad`, `CustList` | `LAL` |
| AudienceDetail | Specifieke beschrijving | `1pct_Purchasers` |
| Placement | `AllPlace`, `Feed`, `Stories`, `Reels` | `AllPlace` |

**Voorbeeld**: `LAL_1pct_Purchasers_AllPlace`

### Ad Level

```
[CreativeType]_[Format]_[Version]_[Hook]
```

| Component | Opties | Voorbeeld |
|-----------|--------|-----------|
| CreativeType | `UGC`, `Studio`, `Static`, `Carousel`, `Catalog` | `UGC` |
| Format | `Video`, `Image`, `Carousel` | `Video` |
| Version | `v1`, `v2`, `v3` | `v2` |
| Hook | `ProblemHook`, `BenefitHook`, `SocialProof`, `Question` | `ProblemHook` |

**Voorbeeld**: `UGC_Video_v2_ProblemHook`

## Volledige Voorbeeld

```
Campaign: Acme_Conv_BOFU_NL_0126
└── Ad Set: LAL_1pct_Purchasers_AllPlace
    ├── Ad: UGC_Video_v1_ProblemHook
    ├── Ad: UGC_Video_v2_BenefitHook
    └── Ad: Static_Image_v1_SocialProof
└── Ad Set: Retarget_Cart30d_AllPlace
    ├── Ad: DPA_Carousel_v1_Reminder
    └── Ad: Static_Image_v1_Urgency
```

## Speciale Cases

### A/B Tests

Voeg `_TestA` / `_TestB` toe aan campaign naam:
```
Acme_Conv_BOFU_NL_0126_TestA
Acme_Conv_BOFU_NL_0126_TestB
```

### Seasonal Campaigns

Voeg seizoen/event toe:
```
Acme_Conv_BOFU_NL_BF24  (Black Friday 2024)
Acme_Conv_BOFU_NL_XMAS24
Acme_Conv_BOFU_NL_SUMMER25
```

### Multi-Product

Voeg product categorie toe:
```
Acme_Conv_BOFU_NL_0126_Shoes
Acme_Conv_BOFU_NL_0126_Bags
```

## UTM Parameters Alignment

Zorg dat UTM parameters overeenkomen met naming:

```
utm_source=facebook
utm_medium=paid
utm_campaign=Acme_Conv_BOFU_NL_0126
utm_content=UGC_Video_v2_ProblemHook
```

## Regex Patterns voor Validatie

### Campaign Name Validation
```regex
^[A-Za-z]+_[A-Za-z]+_[A-Z]{4}_[A-Z]{2,4}_\d{4}(_[A-Za-z0-9]+)?$
```

### Ad Set Name Validation
```regex
^[A-Za-z]+_[A-Za-z0-9]+_[A-Za-z]+$
```

### Ad Name Validation
```regex
^[A-Za-z]+_[A-Za-z]+_v\d+_[A-Za-z]+$
```

## Checklist

- [ ] Consistent format across all campaigns
- [ ] No spaces (gebruik underscores)
- [ ] No special characters
- [ ] Date format consistent (MMYY)
- [ ] Audience type duidelijk
- [ ] Creative type identificeerbaar
- [ ] Version tracking mogelijk

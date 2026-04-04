## Channel Overview

### Custom Channels Added
| Channel Name | Priority | Rationale |
|--------------|----------|-----------|
| Retargeting | 1 | Separate remarketing measurement |
| Paid Search - Brand | 2 | Brand vs non-brand split |
| Affiliate | 9 | Affiliate partner tracking |
| Influencer | 10 | Creator collaborations |
| Partner | 11 | B2B partner traffic |

### Channel Order
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

### Channel Order
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
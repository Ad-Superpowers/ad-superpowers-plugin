---
description: Proactively detect ad creative fatigue before performance tanks. Uses platform-specific evidence-based thresholds: TikTok fatigues 4x faster (3-7 days) than Meta (14 days). Google Ads uses asset ratings (4-8 weeks). LinkedIn has longest cycles (4-6 weeks). (requires Pro subscription)
---

> **Platforms:** meta, tiktok, linkedin, google_ads
> **Tier:** pro
> 
> This command requires the Ad Superpowers MCP connector to access your ad account data.
> Connect at https://app.adsuperpowers.ai if you haven't already.

# Creative Fatigue Scanner

Scan for creative fatigue across all ad platforms with **platform-specific thresholds**.

## CRITICAL: Platform Fatigue Speeds Differ Dramatically

```
┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│                          CREATIVE FATIGUE: PLATFORM COMPARISON                                 │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                │
│  TIKTOK ADS           META ADS             GOOGLE ADS            LINKEDIN ADS                  │
│  ──────────           ─────────            ──────────            ─────────────                 │
│  Fatigue: 3-7 days    Fatigue: ~14 days    Fatigue: 4-8 weeks    Fatigue: 4-6 weeks           │
│  Refresh: 3-5 days    Refresh: 7-14 days   Refresh: Monthly      Refresh: 4-6 weeks           │
│  Creatives: 8-12      Creatives: 4-6       Assets: 15+ per AG    Creatives: 3-4               │
│  CTR decline: CLIFF   CTR decline: GRADUAL CTR decline: V.SLOW   CTR decline: SLOW            │
│  (-20%/day)           (~2%/day)            (~0.5%/week)          (~1%/day)                    │
│  Indicator: Frequency Indicator: Frequency Indicator: RATINGS    Indicator: Frequency         │
│                                                                                                │
│  Fatigue Speed: TikTok (4x) > Meta (1x) > LinkedIn (0.25x) > Google Ads (0.125x)              │
│  ⚠️ Google Ads uses ASSET RATINGS (Best/Good/Low/Pending) instead of frequency!               │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Platform-Specific Thresholds

### Meta Ads (Facebook/Instagram)
| Indicator | Prospecting | Retargeting | Warning | Critical |
|-----------|-------------|-------------|---------|----------|
| Frequency | >3/week | >5/week | >4/week | >6/week |
| CTR Decline (WoW) | >10% | >15% | >15% | >20% |
| CPM Increase (WoW) | >20% | >25% | >25% | >40% |
| Days Active | >10 days | >14 days | >14 days | >21 days |

### TikTok Ads (4x Faster Fatigue!)
| Indicator | Prospecting | Retargeting | Warning | Critical |
|-----------|-------------|-------------|---------|----------|
| Frequency | >4/week | >6/week | >5/week | >8/week |
| CTR Decline (3-day) | >15% | >20% | >20% | >30% |
| CPM Increase (3-day) | >20% | >25% | >25% | >40% |
| Days Active | >5 days | >7 days | >5 days | >7 days |

### LinkedIn Ads (Slower B2B Cycles)
| Indicator | Lead Gen | Brand | Warning | Critical |
|-----------|----------|-------|---------|----------|
| Frequency | >4/week | >6/week | >5/week | >8/week |
| CTR Decline (2-week) | >15% | >20% | >20% | >30% |
| CPM Increase (2-week) | >25% | >30% | >30% | >50% |
| Days Active | >30 days | >45 days | >35 days | >45 days |

### Google Ads (PMax/Display/YouTube - Asset Ratings Based!)
⚠️ **Different Detection Method:** Google Ads uses asset performance ratings, NOT frequency.

| Indicator | PMax | Display | YouTube | Warning | Critical |
|-----------|------|---------|---------|---------|----------|
| "Low" Assets | >20% | >25% | N/A | >30% | >40% |
| CTR Decline (month) | >10% | >15% | >15% VTR | >15% | >25% |
| CPA Increase (month) | >15% | >20% | >25% CPV | >20% | >35% |
| Days Active | >45 days | >30 days | >60 days | >45d | >60d |
| Asset Refresh Date | >4 weeks | >4 weeks | >8 weeks | >6wk | >8wk |

**Key Differences:**
- No frequency metric at creative level - use ASSET RATINGS instead
- "Low" rated assets for 30+ days = fatigue signal
- PMax: Check asset group performance, not ad-level
- Longer cycles: Plan monthly refreshes, not weekly

## Instructions

### 1. Gather Creative Data Per Platform

**Meta Ads:** Use `meta_get_insights` with level="ad" and fields including frequency, CTR, CPM
**TikTok Ads:** Use `tiktok_get_report` with level="ad" for impressions, clicks, CTR, CPM
**LinkedIn Ads:** Use `linkedin_get_analytics` for campaign-level metrics
**Google Ads:** Use `google_ads_run_gaql` with ad-level GAQL queries for asset-level performance data

Retrieve for each:
- Ad-level metrics: impressions, reach, frequency (not Google Ads), CTR, CPC, CPM
- Time series: TikTok (3-day), Meta (7-day), LinkedIn (14-day), Google Ads (30-day)
- Creative details: format, age, last refresh date
- **Google Ads specific:** Asset ratings (Best/Good/Low/Pending), asset group performance

### 2. Apply Platform-Specific Fatigue Detection

```python
def calculate_fatigue_score(ad, platform, audience_type):
    score = 0

    if platform == "tiktok":
        # TikTok: 4x faster fatigue
        freq_threshold = 4 if audience_type == "prospecting" else 6
        ctr_threshold = -15  # 3-day threshold
        cpm_threshold = 20
        age_threshold = 5

    elif platform == "meta":
        # Meta: Standard 2-week cycle
        freq_threshold = 3 if audience_type == "prospecting" else 5
        ctr_threshold = -10  # 7-day threshold
        cpm_threshold = 20
        age_threshold = 14

    elif platform == "linkedin":
        # LinkedIn: Long B2B cycles
        freq_threshold = 4 if audience_type == "prospecting" else 6
        ctr_threshold = -15  # 14-day threshold
        cpm_threshold = 25
        age_threshold = 30

    elif platform == "google_ads":
        # Google Ads: Asset ratings based, longest cycles
        # Different detection: uses "Low" asset percentage instead of frequency
        low_asset_threshold = 20  # >20% assets at "Low" = warning
        ctr_threshold = -10  # 30-day threshold (very gradual)
        cpa_threshold = 15  # CPA increase threshold
        age_threshold = 45  # Days since last asset refresh

    # Platform-specific scoring
    if platform == "google_ads":
        # Asset rating check (35 points - most important for Google Ads)
        if low_asset_percentage > low_asset_threshold:
            score += 35

        # CTR decline check (20 points)
        if ctr_change < ctr_threshold:
            score += 20

        # CPA increase check (25 points)
        if cpa_change > cpa_threshold:
            score += 25

        # Age check (20 points)
        if days_since_refresh > age_threshold:
            score += 20
    else:
        # Standard frequency-based scoring for other platforms
        # Frequency check (30 points)
        if frequency > freq_threshold:
            score += 30

        # CTR decline check (25 points)
        if ctr_change < ctr_threshold:
            score += 25

        # CPM increase check (25 points)
        if cpm_change > cpm_threshold:
            score += 25

        # Age check (20 points)
        if creative_age_days > age_threshold:
            score += 20

    # Status assignment
    if score >= 50: return "HIGH FATIGUE"
    elif score >= 30: return "MODERATE FATIGUE"
    else: return "HEALTHY"
```

### 3. Output Format

```
================================================================================
                         CREATIVE FATIGUE SCANNER
                    Period: Platform-Appropriate Windows
================================================================================

PLATFORM SUMMARY:
| Platform    | Ads/Assets Scanned | Healthy | Warning | Critical | Avg Age |
|-------------|-------------------|---------|---------|----------|---------|
| TikTok      | [X]               | [Y]     | [Z]     | [W]      | [D] days|
| Meta        | [X]               | [Y]     | [Z]     | [W]      | [D] days|
| Google Ads  | [X] assets        | [Y]     | [Z]     | [W]      | [D] days|
| LinkedIn    | [X]               | [Y]     | [Z]     | [W]      | [D] days|

⚠️ CRITICAL: TikTok ads fatigue 4x faster - check these first!
⚠️ NOTE: Google Ads uses Asset Ratings (Best/Good/Low) instead of frequency

HIGH FATIGUE - REFRESH IMMEDIATELY:
-----------------------------------
TIKTOK (Refresh within 24-48h):
| Ad Name          | Freq | CTR Chg (3d) | CPM Chg | Days | Score |
|------------------|------|--------------|---------|------|-------|
| [Ad Name]        | 5.2  | -25%         | +32%    | 8    | 80    |

META (Refresh within 7 days):
| Ad Name          | Freq | CTR Chg (7d) | CPM Chg | Days | Score |
|------------------|------|--------------|---------|------|-------|
| [Ad Name]        | 4.2  | -18%         | +28%    | 21   | 75    |

GOOGLE ADS (Refresh within 2-4 weeks - Asset Ratings Based):
| Asset Group/Ad   | % Low | CTR Chg (30d)| CPA Chg | Last Refresh | Score |
|------------------|-------|--------------|---------|--------------|-------|
| [AG/Ad Name]     | 35%   | -15%         | +22%    | 52 days ago  | 75    |
Note: "Low" = % of assets rated "Low" for 30+ days

LINKEDIN (Refresh within 2 weeks):
| Ad Name          | Freq | CTR Chg (14d)| CPM Chg | Days | Score |
|------------------|------|--------------|---------|------|-------|
| [Ad Name]        | 5.0  | -22%         | +35%    | 42   | 70    |

PLATFORM-SPECIFIC RECOMMENDATIONS:
----------------------------------
TIKTOK:
- Rotate creatives every 3-5 days
- Keep 8-12 creatives in rotation
- UGC lasts 20-30% longer than polished content
- New hook = highest impact refresh tactic

META:
- Rotate creatives every 7-14 days
- Keep 4-6 creatives per ad set
- Dynamic Creative extends lifespan
- UGC lasts 17-18 days vs 10-12 for polished

GOOGLE ADS:
- Monthly 20-30% asset refresh (much longer cycles!)
- Replace "Low" rated assets after 30+ days
- Add variations of "Best" rated assets
- PMax needs 15+ assets per asset group
- No frequency metric - watch Asset Ratings instead

LINKEDIN:
- Rotate every 4-6 weeks
- Keep 3-4 creatives per campaign
- Message Ads fatigue slower
- Professional audience tolerates higher frequency
```
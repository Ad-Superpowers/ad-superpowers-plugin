---
description: End-to-end new client onboarding workflow — from discovery through tracking setup to campaign launch
disable-model-invocation: true
---

# New Client Launch

Guide the user through a complete new client/account onboarding workflow. This is a structured, multi-step process.

## Phase 1: Discovery (Gather Information)

Ask the user for:
1. **Business type**: E-commerce, Lead Gen, SaaS, Local Business, or other
2. **Platforms to use**: Which ad platforms are connected? Check with `meta_list_ad_accounts`, `google_ads_list_accounts`, `linkedin_list_ad_accounts`, `tiktok_get_advertiser_info`
3. **Monthly budget**: Total and per-platform allocation
4. **Primary KPI**: Revenue/ROAS, Leads/CPL, Traffic, Brand Awareness
5. **Target audience**: Who is the ideal customer?
6. **Current performance**: Pull existing data if accounts have history

## Phase 2: Tracking Audit

1. **GTM Check**: `gtm_list_containers` → `gtm_audit` — are tracking tags properly configured?
2. **GA4 Check**: `ga4_list_properties` → `ga4_run_report` — are events firing correctly?
3. **Platform pixels**: Verify Meta Pixel, Google Ads tag, LinkedIn Insight Tag, TikTok Pixel are installed
4. **Flag issues**: List any tracking gaps that need fixing before launch

## Phase 3: Competitive & Market Research

1. **Keyword landscape**: `google_ads_run_keyword_planner` for search volume and competition
2. **Organic position**: `gsc_search_analytics` for existing organic rankings
3. **Existing performance**: Pull last 30 days from any active campaigns

## Phase 4: Campaign Strategy

Based on discovery, recommend:
1. **Channel mix** with budget per platform
2. **Campaign structure** per platform
3. **Target audiences** per platform
4. **Creative requirements** (formats, messaging themes)
5. **KPI targets** with benchmarks

## Phase 5: Launch Checklist

Present a checklist before execution:
- [ ] Tracking verified on all platforms
- [ ] Audiences created and exclusions set
- [ ] Campaign structure approved
- [ ] Creatives ready
- [ ] Budget confirmed
- [ ] Attribution windows configured
- [ ] Reporting cadence agreed (weekly/bi-weekly)

## Phase 6: 30/60/90 Day Plan

Outline the optimization roadmap:
- **Days 1-30**: Learning phase, data collection, initial optimizations
- **Days 31-60**: First scaling decisions, creative refresh, audience expansion
- **Days 61-90**: Full optimization, A/B testing, budget reallocation based on data

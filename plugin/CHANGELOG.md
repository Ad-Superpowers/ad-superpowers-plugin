# Changelog

All notable changes to the Ad Superpowers Claude plugin will be documented in this file.

## [2.1.0] - 2026-04-04

### Added

- **17 new expert skills** filling platform coverage gaps:
  - LinkedIn (+4): ABM targeting strategy, content strategy, lead scoring framework, campaign scaling guide
  - TikTok (+4): Spark Ads strategy, hook optimization guide, shopping ads guide, audience strategy
  - GTM/Tracking (+4): tracking plan builder, conversion setup guide, server-side tagging guide, consent mode guide
  - Cross-Platform (+5): e-commerce funnel optimizer, LTV/CAC modeling, experiment design, client onboarding, local business guide
- **4 new workflow commands**: new-client-launch, ecommerce-health-check, b2b-pipeline-review, quarterly-business-review
- Injected new skills into agent `skills` fields for deeper expertise

### Removed

- 4 redundant skills consolidated: meta-full-funnel-designer, meta-prompt-engineering-library, google-ads-gaql-query-guide, google-ads-pmax-asset-group-optimizer

## [2.0.0] - 2026-04-04

### Changed

- **Consolidated 9 agents into 5 focused specialists** — clearer domains, no overlap:
  - `marketing-strategist` — Strategy, competitive analysis, channel selection, personas
  - `media-buyer` — Campaign execution, budgets, bidding, audiences, scaling, troubleshooting
  - `creative-analyst` — Creative fatigue, A/B tests, refresh strategies
  - `reporting-agent` — Structured performance reports
  - `tracking-specialist` — GTM audits, conversion tracking, SEO vs SEA analysis
- All agents now include `tools` field (principle of least privilege)
- All agents now include `skills` field (platform-specific expertise injected at startup)

### Removed

- Removed 4 overlapping agents: `campaign-auditor`, `campaign-builder`, `budget-optimizer`, `audience-strategist`, `seo-sea-analyst`, `gtm-specialist`, `performance-marketing-agent` (functionality absorbed into the 5 specialists)

## [1.1.0] - 2026-04-03

### Added

- **5 new specialized agents** for focused advertising tasks:
  - `campaign-auditor` — Comprehensive account audits with structured scoring
  - `creative-analyst` — Creative fatigue detection and refresh strategies
  - `budget-optimizer` — Cross-platform budget allocation and pacing
  - `reporting-agent` — Structured performance reports (weekly, monthly, executive)
  - `seo-sea-analyst` — Organic vs paid search overlap and cannibalization analysis
- Updated `performance-marketing-agent` with color coding

## [1.0.0] - 2026-04-03

### Added

- **Unified plugin** combining all 8 platform modules into a single installable plugin
- **98 expert skills** (v2.0) across Meta Ads, Google Ads, GA4, LinkedIn Ads, TikTok Ads, Google Search Console, Google Tag Manager, and cross-platform strategy
- **26 workflow commands** for performance reviews, audits, creative analysis, budget planning, and reporting
- **1 specialized agent** for performance marketing analysis
- **29 MCP tools** via `mcp.adsuperpowers.ai/v1` for direct API access to all platforms
- OAuth authentication for all 8 platforms via the Ad Superpowers dashboard
- Safety confirmations: campaigns create paused, budget changes require approval

### Platforms

| Platform | Skills | Tools |
|----------|--------|-------|
| Meta Ads (Facebook/Instagram) | 23 | 8 |
| Google Ads | 32 | 4 |
| Google Analytics 4 | 18 | 2 |
| Google Search Console | 2 | 3 |
| Google Tag Manager | 1 | 3 |
| LinkedIn Ads | 7 | 4 |
| TikTok Ads | 6 | 6 |
| Cross-Platform | 9 | — |

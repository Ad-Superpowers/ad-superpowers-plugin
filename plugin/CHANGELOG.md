# Changelog

All notable changes to the Ad Superpowers Claude plugin will be documented in this file.

## [2.1.2] - 2026-04-07

### Requirements

- **Claude Code `2.1.74` or newer is required** for the 5 bundled agents to access MCP tools. Earlier versions hit upstream bug [anthropics/claude-code#21560](https://github.com/anthropics/claude-code/issues/21560) where plugin-defined subagents do not inherit MCP server registrations from the plugin's `.mcp.json`. Anthropic shipped the fix in `2.1.74`. Live-verified against this plugin on `2.1.92` (2026-04-07): `reporting-agent` returns all 16 expected MCP tools and successfully calls `meta_list_ad_accounts`.

### Changed

- **Removed non-standard `skills:` frontmatter from all 5 agent definitions** (`media-buyer`, `reporting-agent`, `creative-analyst`, `marketing-strategist`, `tracking-specialist`). Symptom: `media-buyer` dispatch on Sonnet consistently failed with `Prompt is too long` in under 1 second with 0 tool uses, before the model ever saw the user's prompt — even after stripping the body to 790 bytes with minimal tools. Root cause: Claude Code resolved each skill name in the `skills:` list to its full `SKILL.md` content at session start and bundled them into the in-memory agent definition. For `media-buyer` with 50 listed skills (~878 KB / ~220K tokens), this exceeded Sonnet's 200K context window. Opus (1M context) confirmed the bloat (376K tokens at dispatch, 4× reporting-agent's 110K baseline). Fix: replaced the eager-load `skills:` frontmatter with a concise "Finding the right skill" section in each agent body that instructs the agent to discover skills at runtime via `skill(action="search", query=...)` → `skill(action="get", skill_id=...)` — the progressive-disclosure pattern skills were designed for. Agents still reference skill domains in hints so auto-discovery remains effective. Verification of this fix requires a Claude Code session restart (agent definitions are cached in-memory at session start; mid-session file edits are not picked up). Phase 5 of the Round 3 smoke test will re-verify in a fresh session.

### Fixed

- **`seed_workflows.py` auto-activation now reactivates previously-deactivated workflows.** The Phase 3 query was selecting all `UserWorkflowActivation` records regardless of `is_active`, so users who had workflows deactivated (via dashboard or slug renames) were silently skipped on re-seed. Replaced the SELECT + INSERT pattern with a PostgreSQL UPSERT (`ON CONFLICT DO UPDATE`) that resets `is_active=True` and clears `deactivated_at`. Verified against production: `nick@zendigital.nl` went from 13 active / 29 inactive → 42 active / 0 inactive after the fix. Backend commit: `94a3f22`.
- **Meta tools no longer abort parallel batches on upstream API errors** (Issue #17). All 7 Meta tool functions (`meta_list_ad_accounts`, `meta_query`, `meta_get_insights`, `meta_get_creatives`, `meta_update`, `meta_create_ad`, `meta_duplicate`, `meta_create`) now wrap their `MetaAPIError` sites in try/except blocks and return structured `{found: false, error, hint}` (reads) or `{success: false, error, hint}` (writes) responses via two new helper functions, `_meta_read_error` and `_meta_write_error`. Previously, a bad entity_id, deprecated creative spec, or permissions issue would raise — FastMCP wrapped that as `Internal error: ...` which Claude Code treats as a hard failure and cancels every sibling parallel call in the same batch. This fixes the same architectural issue v2.1.1 fixed for TikTok in `123e40c`. Hints are deliberately specific (e.g., the `meta_duplicate` hint explicitly names the 191x100 image_crop deprecation and recommends `meta_create_ad` as the workaround). Backend commit: `123e40c`.

### Documentation

- README "Claude Code" install section now states the minimum Claude Code version requirement (`2.1.74`) with a link to the upstream issue.

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

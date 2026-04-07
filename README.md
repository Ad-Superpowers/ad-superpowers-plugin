# Ad Superpowers for Claude

Manage, analyze, and optimize your ad campaigns across 8 platforms through natural language in Claude Code and Claude Desktop.

**115 expert skills** · **30 workflow commands** · **5 specialized agents** · **33 MCP tools**

## Platforms

| Platform | Skills | MCP Tools | What you can do |
|----------|-------:|----------:|------------------|
| **Meta Ads** | 23 | 8 | Campaign management, creative fatigue analysis, audience targeting, ad creation, budget optimization |
| **Google Ads** | 32 | 4 | GAQL queries, Performance Max, keyword strategy, bid optimization, campaign creation |
| **Google Analytics 4** | 18 | 2 | Event tracking, attribution models, audience building, ecommerce analysis |
| **Google Search Console** | 2 | 3 | SEO performance, keyword rankings, indexing diagnostics, sitemap management |
| **Google Tag Manager** | · | 3 | Container auditing, consent mode, server-side tagging, conversion setup |
| **LinkedIn Ads** | 11 | 4 | B2B lead gen, ABM targeting, revenue attribution, Thought Leader Ads, CTV |
| **TikTok Ads** | 10 | 6 | Creative fatigue, video performance, Smart+ campaigns, Search Ads, Shop |
| **Cross-platform** | 19 | · | Attribution reconciliation, SEO vs SEA gaps, budget allocation, competitive analysis |
| **Gemini (image gen)** | · | 1 | AI image generation for ad creatives, BYOK via Gemini API key |

## Install

Pick the path that matches how you use Claude. All four give you the MCP tools; only Claude Code and Cowork give you the bundled skills, commands, and agents.

### Claude Code (terminal or VSCode extension)

**Requires Claude Code `2.1.74` or newer.** Earlier versions have an upstream bug ([anthropics/claude-code#21560](https://github.com/anthropics/claude-code/issues/21560)) that prevents plugin-defined subagents from accessing MCP tools, which breaks all 5 specialized agents in this plugin. The MCP tools and skills work on older versions, but the agents will refuse cleanly instead of running. Upgrade with `npm i -g @anthropic-ai/claude-code@latest` (terminal) or via the VSCode extension marketplace, then `Developer: Reload Window`.

Add the marketplace once, then install the plugin:

```bash
/plugin marketplace add Ad-Superpowers/claude-plugin
/plugin install ad-superpowers@ad-superpowers
```

That's it. The MCP server, all 115 skills, 30 workflow commands, 5 agents, and safety confirmations are bundled.

### Cowork (Claude Desktop's agentic coding mode)

Cowork supports plugins through an admin UI, not through a slash command. This path is available on **Team** and **Enterprise** plans, and only Owners or Primary Owners can add plugins for the organization.

1. In Claude Desktop, go to **Organization settings → Plugins**
2. Click **Add plugin** and choose **Sync from GitHub**
3. Enter the repository: `Ad-Superpowers/claude-plugin`
4. Set distribution: **Available for install** (members can opt in) or **Installed by default**
5. Members then open **Browse plugins** inside Cowork to install it

Once installed, members get the full plugin experience (skills, commands, agents, and MCP tools) inside Cowork.

### Claude Desktop (chat mode, via Connectors)

The regular Claude Desktop chat interface doesn't have a plugin system. You can still get the MCP tools by adding Ad Superpowers as a Connector, but you won't get the bundled skills, commands, or agents (those need Claude Code or Cowork).

1. Open Claude Desktop
2. Go to **Settings → Connectors → Add Custom Connector**
3. Enter the URL: `https://mcp.adsuperpowers.ai/v1`
4. Complete the OAuth flow in your browser

If you want the full experience, use Claude Code or Cowork instead.

### ChatGPT

ChatGPT supports the Ad Superpowers MCP server through the Apps Directory. Search for "Ad Superpowers" in the ChatGPT Apps interface and authorize access. You'll get the MCP tools but not the bundled skills, commands, or agents.

## Setup

1. Create an account at [app.adsuperpowers.ai](https://app.adsuperpowers.ai)
2. Connect your ad platforms through OAuth in the dashboard
3. Start asking Claude about your campaigns

No API keys to configure, no manual MCP setup. Authentication happens via OAuth through the Ad Superpowers dashboard.

## What you can do

### Ask questions in natural language

* "How are my Meta campaigns performing this week?"
* "Which Google Ads keywords have the highest CPA?"
* "Compare my LinkedIn and Meta lead gen performance"
* "Is my TikTok creative showing signs of fatigue?"
* "What's my organic vs paid keyword overlap?"

### Run workflow commands

| Command | What it does |
|---------|--------------|
| `/ad-superpowers:weekly-performance-pulse` | Cross-platform weekly health check |
| `/ad-superpowers:creative-fatigue-scanner` | Detect fatigued creatives across platforms |
| `/ad-superpowers:budget-allocation-planner` | Data-driven budget reallocation recommendations |
| `/ad-superpowers:keyword-opportunities` | SEO vs paid keyword gap analysis |
| `/ad-superpowers:monthly-executive-summary` | Executive-ready monthly performance report |
| `/ad-superpowers:anomaly-detective` | Detect performance anomalies across campaigns |
| `/ad-superpowers:competitive-landscape-analyzer` | Competitive positioning analysis |

[See all 30 commands](plugin/commands/)

### Specialized agents

Claude automatically delegates to the right agent based on your task:

| Agent | Focus | Triggers |
|-------|-------|----------|
| **marketing-strategist** | Strategy, competitive analysis, channel selection, personas | "analyze competition", "which channels?", "new client onboarding" |
| **media-buyer** | Campaign execution, budgets, bidding, audiences, scaling | "create campaign", "optimize budget", "scale winners" |
| **creative-analyst** | Creative fatigue detection, A/B tests, refresh strategy | "check creative fatigue", "which ads are tired" |
| **reporting-agent** | Structured performance reports and comparisons | "weekly report", "monthly summary" |
| **tracking-specialist** | GTM audits, conversion tracking, SEO vs SEA analysis | "audit my GTM", "keyword overlap", "missing conversions" |

### Expert skills (auto-invoked)

Claude automatically uses the right skill based on your question. Skills provide decision frameworks, benchmarks, and actionable recommendations for:

* Campaign optimization (bid strategies, budget scaling, learning phase management)
* Creative analysis (fatigue detection, A/B testing, diversification)
* Audience strategy (lookalike planning, overlap detection, remarketing)
* Measurement (attribution models, conversion tracking, CAPI setup)
* Technical work (GAQL queries, GTM auditing, GA4 event tracking)

### Write operations (with safety)

* Create Meta ads (image upload, creative, and ad in one step)
* Duplicate ads with creative overrides
* Pause or resume campaigns and update budgets
* Create Google Ads campaigns (budget, campaign, ad group, ads, keywords)

All write operations include safety confirmations:

* Campaigns always create paused so you can review before going live
* Budget changes require explicit approval
* Destructive operations are clearly flagged

## Known limitations

### Specialized agents may run with reduced capabilities

The 5 bundled agents (`marketing-strategist`, `media-buyer`, `creative-analyst`, `reporting-agent`, `tracking-specialist`) are designed to call Ad Superpowers MCP tools directly when Claude Code dispatches them. As of Claude Code's current release, **MCP tools shipped from a plugin's `.mcp.json` are not propagated into plugin-defined subagents**. This is a Claude Code platform limitation tracked upstream at [anthropics/claude-code#21560](https://github.com/anthropics/claude-code/issues/21560), not an Ad Superpowers bug.

What this means in practice:

* When Claude Code spawns one of these agents via the `Agent` tool, the agent's tool registry only contains read-only tools (`Glob`, `Grep`, `Read`, `WebFetch`, `WebSearch`). The Ad Superpowers MCP tools are absent.
* The agents are programmed to **detect this and refuse cleanly** rather than fabricate data. You'll see a structured failure report instead of an invented analysis.
* Asking Claude directly (without explicit agent dispatch) is unaffected — the main thread has full access to all 33 MCP tools, all 30 workflow commands, and all 115 skills. **The plugin works fully when used in the main conversation.**

We will re-enable the agents for direct MCP access once the upstream Claude Code fix lands. If you want to be notified, ⭐ the [issue on GitHub](https://github.com/anthropics/claude-code/issues/21560).

## Pricing

| Tier | Monthly | Connected accounts | Platforms |
|------|---------|--------------------|-----------|
| **Free** | €0 | 3 | Meta, Google Ads, GA4, Search Console |
| **Pro** | €79 | 25 | All 8 platforms |
| **Team** | €249 | 100 | All 8 platforms |
| **Enterprise** | Custom | Unlimited | All plus custom integrations |

20% discount on annual plans. Start free at [adsuperpowers.ai](https://adsuperpowers.ai).

## Security

* OAuth authentication, credentials are never stored locally
* All API communication over HTTPS
* Users can revoke platform access at any time
* Per-user authentication in team environments
* See [SECURITY.md](SECURITY.md) for our responsible disclosure policy

## Support

* Website: [adsuperpowers.ai](https://adsuperpowers.ai)
* Dashboard: [app.adsuperpowers.ai](https://app.adsuperpowers.ai)
* Email: support@adsuperpowers.ai

## License

MIT, see [LICENSE](LICENSE)

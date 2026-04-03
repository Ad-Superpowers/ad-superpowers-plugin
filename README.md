# Ad Superpowers — Claude Plugin

AI-powered advertising intelligence across 8 platforms. Manage, analyze, and optimize your ad campaigns through natural language in Claude Code and Cowork.

**98 expert skills** | **26 workflow commands** | **29 MCP tools** | **1 specialized agent**

## Platforms

| Platform | Skills | MCP Tools | Capabilities |
|----------|--------|-----------|--------------|
| **Meta Ads** | 23 | 8 | Campaign management, creative fatigue analysis, audience targeting, ad creation, budget optimization |
| **Google Ads** | 32 | 4 | GAQL queries, Performance Max, keyword strategy, bid optimization, campaign creation |
| **Google Analytics 4** | 18 | 2 | Event tracking, attribution models, audience building, ecommerce analysis |
| **Google Search Console** | 2 | 3 | SEO performance, keyword rankings, indexing diagnostics, sitemap management |
| **Google Tag Manager** | 1 | 3 | Container auditing, tag management, configuration |
| **LinkedIn Ads** | 7 | 4 | B2B lead gen optimization, CPL troubleshooting, campaign analytics |
| **TikTok Ads** | 6 | 6 | Creative fatigue tracking, video performance, audience targeting |
| **Cross-Platform** | 9 | — | Attribution reconciliation, SEO vs SEA gaps, budget allocation, competitive analysis |

## Install

```bash
/plugin install ad-superpowers@claude-plugins-official
```

That's it. The MCP server, all 94 skills, 26 workflow commands, and safety confirmations are bundled.

## Setup

1. **Create an account** at [app.adsuperpowers.ai](https://app.adsuperpowers.ai)
2. **Connect your ad platforms** via OAuth in the dashboard
3. **Start using** — ask Claude anything about your campaigns

No API keys to configure. No manual MCP setup. Authentication is handled via OAuth through the Ad Superpowers dashboard.

## What You Can Do

### Ask questions in natural language

- "How are my Meta campaigns performing this week?"
- "Which Google Ads keywords have the highest CPA?"
- "Compare my LinkedIn and Meta lead gen performance"
- "Is my TikTok creative showing signs of fatigue?"
- "What's my organic vs paid keyword overlap?"

### Run workflow commands

| Command | What It Does |
|---------|--------------|
| `/ad-superpowers:weekly-performance-pulse` | Cross-platform weekly health check |
| `/ad-superpowers:creative-fatigue-scanner` | Detect fatigued creatives across platforms |
| `/ad-superpowers:budget-allocation-planner` | Data-driven budget reallocation recommendations |
| `/ad-superpowers:keyword-opportunities` | SEO vs paid keyword gap analysis |
| `/ad-superpowers:monthly-executive-summary` | Executive-ready monthly performance report |
| `/ad-superpowers:anomaly-detective` | Detect performance anomalies across campaigns |
| `/ad-superpowers:competitive-landscape-analyzer` | Competitive positioning analysis |

[See all 26 commands →](commands/)

### Expert skills (auto-invoked)

Claude automatically uses the right skill based on your question. Skills provide decision frameworks, benchmarks, and actionable recommendations for:

- **Campaign optimization** — bid strategies, budget scaling, learning phase management
- **Creative analysis** — fatigue detection, A/B testing, diversification
- **Audience strategy** — lookalike planning, overlap detection, remarketing
- **Measurement** — attribution models, conversion tracking, CAPI setup
- **Technical** — GAQL queries, GTM auditing, GA4 event tracking

### Write operations (with safety)

- Create Meta ads (image upload + creative + ad in one step)
- Duplicate ads with creative overrides
- Pause/resume campaigns and update budgets
- Create Google Ads campaigns (budget + campaign + ad group + ads + keywords)

All write operations include safety confirmations:
- **Campaigns always create paused** for review before going live
- **Budget changes require explicit approval**
- **Destructive operations are clearly flagged**

## Pricing

| Tier | Monthly | Connected Accounts | Platforms |
|------|---------|-------------------|-----------|
| **Free** | €0 | 3 | Meta, Google Ads, GA4, Search Console |
| **Pro** | €79 | 25 | All 8 platforms |
| **Team** | €249 | 100 | All 8 platforms |
| **Enterprise** | Custom | Unlimited | All + custom integrations |

20% discount on annual plans. Start free at [adsuperpowers.ai](https://adsuperpowers.ai).

## Security

- OAuth authentication — credentials never stored locally
- All API communication over HTTPS
- Users can revoke platform access at any time
- Per-user authentication in team environments
- See [SECURITY.md](SECURITY.md) for our responsible disclosure policy

## Support

- **Website**: [adsuperpowers.ai](https://adsuperpowers.ai)
- **Dashboard**: [app.adsuperpowers.ai](https://app.adsuperpowers.ai)
- **Email**: support@adsuperpowers.ai

## License

MIT — see [LICENSE](LICENSE)

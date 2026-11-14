# Ad Superpowers for Claude

Ad Superpowers sits between you and your ad platforms. One connection gives Claude Meta, Google Ads, GA4, Search Console, Tag Manager, Merchant Center, LinkedIn and TikTok, with client context, workflows and expert skills for agencies and PPC specialists.

**124 expert skills** · **35 slash commands** (29 workflow, 6 utility) · **5 specialized agents** · **61 MCP tools**

## What you can do

- **Audit an account** across channels and get the three changes that matter most.
- **Report across clients**: weekly pulses, monthly reports and cross-platform comparisons from live data.
- **Launch campaigns from a media plan** in minutes: Claude prepares each campaign, you check it, and new campaigns start paused.

## Platforms

| Platform | Skills | MCP Tools | What you can do |
|----------|-------:|----------:|------------------|
| **Meta Ads** | 26 | 15 | Campaigns, ads and budgets, creative strategy and fatigue, audiences, catalog ads |
| **Google Ads** | 32 | 5 | GAQL reporting, Performance Max, keywords, bidding, campaign changes |
| **Google Analytics 4** | 18 | 2 | Traffic and conversion reports, attribution, audiences, ecommerce |
| **Google Search Console** | 2 | 3 | Search performance, keyword rankings, indexing, sitemaps |
| **Google Tag Manager** | 4 | 4 | Container audits, consent mode, server-side tagging, supervised changes |
| **Google Merchant Center** | 0 | 6 | Feed and Shopping reads, product issues and performance |
| **LinkedIn Ads** | 14 | 6 | B2B lead gen, ABM, analytics, campaign changes |
| **TikTok Ads** | 10 | 9 | Reporting, creatives, audiences, campaign changes |
| **Cross-platform** | 18 | 9 | Getting started, client context, workflows, skills and the workspace |

## Install

1. In Claude, open **Customize → Plugins → Discover**, find **Ad Superpowers** and select **Add**. The plugin is saved to your account and also appears in Cowork and Claude Code.
2. Open the plugin's **Connectors** tab and connect **Ad Superpowers**: sign in, choose your workspace and allow access. Adding the plugin does not connect anything by itself.
3. Connect your ad platforms once in the dashboard at [app.adsuperpowers.ai](https://app.adsuperpowers.ai/dashboard/integrations).

Skills, commands and the connector work in chat, Cowork and Claude Code. The five agents run in Cowork and Claude Code.

Claude Code from the command line:

```bash
/plugin marketplace add Ad-Superpowers/ad-superpowers-plugin
/plugin install ad-superpowers@ad-superpowers
```

ChatGPT and other MCP clients get the same tools through the connector: [setup guides](https://adsuperpowers.ai/docs).

## You stay in control

- Reads run on the accounts your workspace can access; a member can be read-only.
- Tools that change something are marked as write tools; how often your client asks before using them depends on its settings.
- On Meta, new campaigns and ad sets are created paused, and archiving, budget changes over 20% and changes that reset learning need an explicit extra confirmation in the call.
- The workspace activity trail records each supported action with who, when, what and the outcome.

## What the plugin sends, and where

| What | Where it goes |
|---|---|
| Your requests to Ad Superpowers tools | `mcp.adsuperpowers.ai/v1` over HTTPS, signed in with OAuth |
| Platform reads and changes | The ad platform APIs you connected, through Ad Superpowers |
| Analysis scripts, such as the creative X-ray | Run on the Ad Superpowers server, not on your computer |
| Media you upload to an ad platform | Through Ad Superpowers to temporary private storage (Supabase), then to the platform; the source file is deleted after the upload |
| Competitor and market research steps in some commands | Your Claude client's own web search, when you allow it |
| Tool results | Back to your Claude client; Anthropic's policies apply there |

Nothing runs on your computer when you install the plugin: it has no hooks, local scripts or local servers. Platform credentials are encrypted on our server, API responses are cached for one minute to six hours, and Ad Superpowers does not run its own AI model. Details: [Data privacy](https://adsuperpowers.ai/docs/data-privacy) · [Privacy policy](https://adsuperpowers.ai/privacy-policy) · [Terms](https://adsuperpowers.ai/terms-of-service).

## Pricing

| Tier | Monthly | Annual | Tool calls/mo | Account slots per platform | Users | Platforms |
|------|--------:|-------:|--------------:|---------:|------:|-----------|
| **Pro** | €99 | €79 | 1,500 | 25 | 1 | All 8 |
| **Team** | €249 | €199 | 6,000 | 100 | 5 | All 8 |

Free trial: 14 days from workspace creation, 50 tool calls per month. No credit card. The trial includes 25 account slots per platform, 1 user and all 8 platforms. To continue after the trial, choose a paid plan. Annual plans get a 20% discount. A "tool call" is one MCP tool invocation; workflows that fan out to multiple tools count each invocation. Enterprise enquiries use custom usage and volume pricing. Start at [adsuperpowers.ai](https://adsuperpowers.ai).

## Support

[adsuperpowers.ai/contact](https://adsuperpowers.ai/contact) · contact@adsuperpowers.ai · [Security policy](https://github.com/Ad-Superpowers/ad-superpowers-plugin/blob/main/plugin/SECURITY.md)

MIT, see [LICENSE](https://github.com/Ad-Superpowers/ad-superpowers-plugin/blob/main/LICENSE)

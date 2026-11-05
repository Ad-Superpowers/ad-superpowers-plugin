---
name: connection-troubleshooter
description: "This skill should be used when a user says the Ad Superpowers connector looks broken or half-empty: \"I only see a few tools\", \"my platform tools are missing\", \"the connector isn't working\", \"I connected my account but nothing shows up\", \"the tool says not connected\", or asks how to \"reconnect\" a platform. It explains what a platform_not_connected answer means (not connected, needs reconnecting, or no account selected), walks through the fix on the dashboard, and how to get the tools into the chat when a client still shows an old tool list. Google Ads, Analytics, Search Console, Tag Manager and Merchant Center are connected individually, so each may need its own reconnect. Do NOT use for: a workspace that never connected anything (use getting-started), campaign performance (use the per-platform performance-troubleshooter skills), or client profiles (use client-context-onboarding)."
allowed-tools: skill, workflow, clients, clients_update, get_started
---

# Connection Troubleshooter

## Purpose

Help a user whose platform tools refuse, or who sees only a handful of Ad
Superpowers tools, understand what happened and fix it. In almost every case
**a platform connection needs (re)connecting** or no account is selected for
it yet. Nothing is broken and no data was lost; the connection just needs
attention on the dashboard.

## When to Use This Skill

Use this skill when the user reports any of:

- A platform tool answered `platform_not_connected`, or "not connected".
- "I only see a few tools" / "most of my tools are gone" / "my platform tools are missing".
- "Where are my Google Ads / GA4 / Search Console / Tag Manager tools?" or
  "Where are my Meta / LinkedIn / TikTok tools?"
- "The connector isn't working" / "I connected my account but nothing shows up".
- "How do I reconnect <platform>?"

For a workspace that never connected anything, load `getting-started` instead
(or call `get_started`). Do **not** use this skill for campaign performance
problems, questions about the Ad Superpowers account itself, or client
onboarding.

## What the answer means

Every platform tool your plan includes is listed in the chat, connected or
not. When a platform cannot be used in this request, its tool answers with
`platform_not_connected` and says which of these it is:

- **Not connected (or not usable):** connect the platform on the dashboard.
- **Needs reconnecting:** it was connected, but the login you granted (the
  OAuth grant) was revoked or expired, for example after a password change or
  when an admin removed the app's access. Reconnect it.
- **No account enabled:** the platform is connected, but no account is
  selected for this workspace. Enable the accounts you want on the dashboard.
- **Connected in another workspace:** connect it in this workspace too.

For the live status of every platform at once, call
`skill(action="connection_health")`: it returns a status per platform with a
reconnect link.

## If tools seem missing from the list

If you see only a few tools (typically `workflow`, `skill`, `clients`,
`get_started`), your client is most likely still showing a tool list it
loaded earlier. Tool names tell you which group is missing:

- No `google_ads_*` tools: **Google Ads**.
- No `ga4_*` tools: **Google Analytics (GA4)**.
- No `gsc_*` tools: **Google Search Console**.
- No `gtm_*` tools: **Google Tag Manager**.
- No `merchant_*` tools: **Merchant Center**.
- No `meta_*` tools: **Meta** (Facebook/Instagram).
- No `linkedin_*` tools: **LinkedIn**.
- No `tiktok_*` tools: **TikTok**.

The tool list refreshes per client: on claude.ai that can take a while; in
ChatGPT a custom connection needs a manual refresh; in Claude Code and most
desktop clients a new session loads it. If the tools for that platform are not
in this chat yet, start a new chat.

## The fix (step by step)

1. Go to the dashboard: **`https://app.adsuperpowers.ai/dashboard/integrations`**
   (the Integrations page).
2. For each platform that refuses, click **Connect** or **Reconnect**, or
   enable an account. Google Ads, Analytics, Search Console, Tag Manager and
   Merchant Center are connected **individually**: do this for **each** Google
   service you use.
3. Complete the login and consent in the browser.
4. Come back here and ask again. If the tools for that platform are not in
   this chat yet, start a new chat.
5. If a Google service still refuses, go back to step 2 and reconnect that
   specific Google service too.

## If it still doesn't work

- Check on the dashboard that the connection shows active and that an account
  is selected for this workspace. For Google, confirm each service you expected.
- The connection may belong to a different workspace than the one this chat
  uses; `workspace_info` shows the workspace of this request.
- Contact Ad Superpowers support with the platform name and the account you
  expected to see.

## Key facts to remember

- A `platform_not_connected` answer says what to do: connect, reconnect, or
  enable an account.
- **Google is five separate connections** (Ads, Analytics, Search Console, Tag
  Manager, Merchant Center). Reconnect **each** Google service that refuses;
  reconnecting one often renews the others (shared sign-in), but it is not
  guaranteed after a revoked login.
- After reconnecting, ask again here; a new chat is only needed when the
  client still shows an old tool list.

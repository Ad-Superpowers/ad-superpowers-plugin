---
name: getting-started
description: "This skill should be used when a user is new to Ad Superpowers or has not connected an ad platform yet: \"how do I start\", \"what can I do with this\", \"get started\", \"nothing is connected\", \"how do I connect my ad account\", \"the tools say not connected\", or when a platform tool answers platform_not_connected. It gives the three steps from zero to a first answer about the user's own data, one first question per platform, and what becomes possible once an account is connected. Call get_started for the live status of this workspace. Do NOT use for: a connection that used to work and stopped (use connection-troubleshooter), campaign performance questions, or client profiles (use client-context-onboarding)."
allowed-tools: get_started, skill, workspace_info, workflow, clients
---

# Getting Started

## What this is for

Connect your first ad accounts and ask about your data right here. Then manage your first campaigns or publish your first ads from this chat, with built-in skills and workflows written by media buyers.

Call `get_started` first: it returns which platforms this workspace has connected, the one next step with its link, and a first question to ask once data is connected. Pass `platform` when the user named one.

## Three steps

1. Connect an account at https://app.adsuperpowers.ai/dashboard/integrations?src=assistant. Google Ads, Analytics, Search Console, Tag Manager and Merchant Center are connected one by one; pick the ones you advertise or measure with. Takes about two minutes.
2. Select the accounts you want to work with on that page.
3. Come back here and ask your first question. If the tools for that platform are not in this chat yet, start a new chat.

Accounts are connected by the user on the dashboard; nothing can be connected from the chat.

## A first question per platform

Replace `[account]` with the account name or id.

- **Meta Ads:** Show my Meta ad account [account] for the last 7 days: spend, impressions, clicks and results per campaign.
- **Google Ads:** List the campaigns in my Google Ads account [account] with cost, clicks and conversions for the last 7 days.
- **TikTok Ads:** Show spend, impressions and conversions per campaign for my TikTok advertiser [account] for the last 7 days.
- **LinkedIn Ads:** Show spend, impressions and clicks per campaign for my LinkedIn Ads account [account] for the last 7 days.
- **Google Analytics 4:** Show sessions and conversions by default channel group for my GA4 property [account] for the last 7 days.
- **Search Console:** Show the top 20 search queries by clicks for my Search Console site [account] for the last 28 days.
- **Merchant Center:** List the current product issues in my Merchant Center account [account] and how many products each one affects.
- **Tag Manager:** List the tags, triggers and variables in my Tag Manager container [account].

## If tools seem missing

If a platform was connected before and its tools now refuse or seem missing, load the `connection-troubleshooter` skill (`skill(action="get", skill_id="connection-troubleshooter")`) or call `skill(action="connection_health")` for the live status per platform with reconnect links.

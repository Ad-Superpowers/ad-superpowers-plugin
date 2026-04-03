---
name: linkedin-benchmark-database
description: |
  Reference database with industry benchmarks for LinkedIn Ads metrics by industry, campaign type, and funnel stage. Use this skill when you want to know if LinkedIn metrics are performing well or when you need to set targets.
  Use when: linkedin benchmark, linkedin CPL, linkedin CTR, linkedin CPC, is my CPL good, linkedin average, B2B benchmark, LinkedIn performance evaluation, LinkedIn target setting.
  Do NOT use for: LinkedIn bid strategy selection (use linkedin-bid-strategy-selector), LinkedIn lead gen optimization (use linkedin-lead-gen-optimizer), LinkedIn performance troubleshooting (use linkedin-performance-troubleshooter).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "linkedin"
  phase: "fase-2-measurement"
compatibility: "Requires AdSuperpowers MCP server with LinkedIn Ads connection"
---
# LinkedIn Ads Benchmark Database

## Overview

This skill provides a comprehensive database of LinkedIn Ads benchmarks by industry, ad format, funnel stage, and campaign type, so you can assess how your B2B metrics perform compared to market standards.

## Benchmark Disclaimer

```
IMPORTANT CONTEXT

These benchmarks are based on:
+-- Aggregated industry data (2024-2026)
+-- Sources: LinkedIn, AdBacklog, GrackerAI, Factors.ai
+-- Primarily focused on Western European/North American markets
+-- B2B focus (LinkedIn's core market)

Benchmarks are GUIDELINES, not absolute truths:
+-- Your specific niche may deviate significantly
+-- Enterprise vs SMB has enormous impact
+-- Sales cycle length affects CPL acceptance
+-- Always compare with your own LTV:CAC ratio
```

## CPL Benchmarks by Industry

```
COST PER LEAD (CPL) BY INDUSTRY
===============================

Industry              | Poor    | Average | Good    | Excellent
----------------------+---------+---------+---------+----------
Finance & Insurance   | >$120   | $90-120 | $60-90  | <$60
Healthcare            | >$150   | $100-150| $70-100 | <$70
SaaS / Software       | >$120   | $80-120 | $50-80  | <$50
Education             | >$80    | $60-80  | $40-60  | <$40
Marketing / Agencies  | >$120   | $80-120 | $50-80  | <$50
Professional Services | >$100   | $70-100 | $45-70  | <$45
Manufacturing         | >$130   | $90-130 | $60-90  | <$60
Technology (Hardware) | >$140   | $100-140| $65-100 | <$65
Consulting            | >$110   | $75-110 | $50-75  | <$50
Recruitment / HR Tech | >$90    | $60-90  | $40-60  | <$40

CONTEXT FACTORS:
+-- Enterprise deals ($50k+ ACV): CPL $150-300+ acceptable
+-- SMB deals ($5k ACV): CPL <$50 target
+-- Freemium SaaS: CPL <$30 ideal
+-- High-touch sales: Higher CPL OK if SQL rate is high
```

## CPC & CPM Benchmarks

```
COST PER CLICK (CPC) BY INDUSTRY
================================

Industry              | Poor    | Average | Good    | Excellent
----------------------+---------+---------+---------+----------
Finance & Insurance   | >$8.00  | $5-8    | $3-5    | <$3.00
SaaS / Software       | >$10.00 | $6-10   | $4-6    | <$4.00
Technology            | >$9.00  | $5-9    | $3-5    | <$3.00
Healthcare            | >$7.00  | $4-7    | $2.50-4 | <$2.50
Education             | >$6.00  | $3.50-6 | $2-3.50 | <$2.00
Manufacturing         | >$7.50  | $4.50-7.5| $3-4.50| <$3.00
Professional Services | >$6.50  | $4-6.50 | $2.50-4 | <$2.50
General B2B           | >$7.00  | $4-7    | $2.50-4 | <$2.50

NOTES:
+-- LinkedIn CPC is 3-5x higher than Meta/Google
+-- But: B2B audience quality often compensates
+-- Focus on CPL/CPA, not just CPC
```

```
COST PER MILLE (CPM) BY TARGETING
=================================

Targeting Type         | Range
-----------------------+------------
Broad Professional     | $25-35
Job Title Targeting    | $35-50
Job Function           | $30-45
Industry + Seniority   | $40-60
Matched Audiences      | $20-30
Lookalike Audiences    | $25-40
ABM / Account Lists    | $50-80
C-Suite Only           | $60-100

CONTEXT FACTORS:
+-- US/UK markets: +20-30% vs EU
+-- Small audiences (<50k): Premium pricing
+-- Q4: +15-25% seasonal increase
```

## CTR Benchmarks by Ad Format

```
CLICK-THROUGH RATE (CTR) BY FORMAT
==================================

Ad Format               | Poor    | Average   | Good      | Excellent
------------------------+---------+-----------+-----------+----------
Sponsored Content       | <0.35%  | 0.35-0.55%| 0.55-0.80%| >0.80%
Video Ads               | <0.30%  | 0.30-0.45%| 0.45-0.65%| >0.65%
Carousel Ads            | <0.40%  | 0.40-0.60%| 0.60-0.90%| >0.90%
Message Ads (InMail)    | <2.00%  | 2.00-3.50%| 3.50-5.00%| >5.00%
Text Ads                | <0.015% | 0.015-0.03%| 0.03-0.05%| >0.05%
Dynamic Ads             | <0.05%  | 0.05-0.10%| 0.10-0.20%| >0.20%
Lead Gen Forms (CVR)    | <6%     | 6-10%     | 10-15%    | >15%

NOTES:
+-- Message Ads: Higher CTR but limited volume
+-- Lead Gen Forms: Measure CVR (form completion), not CTR
+-- Video: Focus on View Rate (25/50/75% completion)
+-- Carousel: Swipe rate 30-50% = healthy
```

## Conversion Rate Benchmarks by Funnel Stage

```
CONVERSION RATE BY FUNNEL STAGE
===============================

Funnel Stage           | Poor    | Average | Good    | Excellent
-----------------------+---------+---------+---------+----------
TOFU (Awareness)
+-- Video View Rate    | <15%    | 15-25%  | 25-40%  | >40%
+-- Engagement Rate    | <0.5%   | 0.5-1%  | 1-2%    | >2%
+-- Brand Lift         | <3%     | 3-8%    | 8-15%   | >15%

MOFU (Consideration)
+-- Landing Page CVR   | <2%     | 2-4%    | 4-6%    | >6%
+-- Content Download   | <4%     | 4-8%    | 8-12%   | >12%
+-- Webinar Signup     | <3%     | 3-6%    | 6-10%   | >10%

BOFU (Conversion)
+-- Demo Request       | <1.5%   | 1.5-3%  | 3-5%    | >5%
+-- Free Trial         | <2%     | 2-4%    | 4-7%    | >7%
+-- Contact Form       | <1%     | 1-2.5%  | 2.5-4%  | >4%
```

## Lead Gen Forms vs Landing Pages

```
LEAD GEN FORMS vs LANDING PAGES
===============================

Metric                  | Lead Gen Forms | Landing Pages
------------------------+----------------+---------------
Conversion Rate         | 10-13%         | 4-6%
Cost per Lead           | 15-25% lower   | Higher
SQL Rate (quality)      | 20-40% lower   | Higher
Mobile Experience       | Excellent      | Variable
Form Fields Limit       | Up to 12       | Unlimited
Custom Validation       | Limited        | Full control
Retargeting Data        | Limited        | Full pixel

WHEN TO USE WHAT:

LEAD GEN FORMS (Native)
+-- High-volume lead generation
+-- Mobile-first audience
+-- Simple qualification (job title, company)
+-- TOFU/MOFU content offers
+-- Lower friction = higher volume, lower quality

LANDING PAGES
+-- Complex qualification needed
+-- Multi-step forms
+-- Custom validation rules
+-- BOFU demo/trial requests
+-- Higher friction = lower volume, higher quality

HYBRID APPROACH (Best Practice)
+-- Use Lead Gen Forms for initial capture
+-- Add 1-2 qualifying questions to filter
+-- Retarget form submitters with LP ads
+-- Measure SQL rate, not just lead volume
```

## SQL Rate & Pipeline Benchmarks

```
LEAD QUALITY BENCHMARKS
=======================

Metric                  | Poor    | Average | Good    | Excellent
------------------------+---------+---------+---------+----------
MQL to SQL Rate         | <10%    | 10-20%  | 20-35%  | >35%
SQL to Opportunity      | <20%    | 20-35%  | 35-50%  | >50%
Opportunity to Close    | <15%    | 15-25%  | 25-40%  | >40%
Lead Gen Form SQL Rate  | <8%     | 8-15%   | 15-25%  | >25%
Landing Page SQL Rate   | <15%    | 15-30%  | 30-45%  | >45%

B2B SALES CYCLE CONTEXT:
+-- Avg LinkedIn-sourced cycle: 200+ days
+-- Multi-touch attribution: 6-12 touches average
+-- First touch to opportunity: 30-90 days
+-- Don't judge CPL without SQL rate data
```

## Engagement Benchmarks

```
ENGAGEMENT RATE BENCHMARKS
==========================

Metric                  | Poor    | Average   | Good      | Excellent
------------------------+---------+-----------+-----------+----------
Total Engagement Rate   | <0.3%   | 0.3-0.6%  | 0.6-1%    | >1%
Like Rate               | <0.15%  | 0.15-0.3% | 0.3-0.5%  | >0.5%
Comment Rate            | <0.02%  | 0.02-0.05%| 0.05-0.1% | >0.1%
Share Rate              | <0.01%  | 0.01-0.03%| 0.03-0.06%| >0.06%
Follow Rate (per ad)    | <0.05%  | 0.05-0.1% | 0.1-0.2%  | >0.2%

VIDEO SPECIFIC:
+-- 25% View Rate       | <20%    | 20-35%  | 35-50%  | >50%
+-- 50% View Rate       | <10%    | 10-20%  | 20-35%  | >35%
+-- 75% View Rate       | <5%     | 5-12%   | 12-20%  | >20%
+-- 100% Completion     | <3%     | 3-8%    | 8-15%   | >15%
```

## Seasonal Adjustment Factors

```
SEASONAL VARIATIONS (B2B)
================================

Period               | CPM Factor | CPL Factor | Notes
---------------------+------------+------------+--------------
Q1 (Jan-Mar)         |   0.90     |   0.95     | Budget resets
April-May            |   0.95     |   1.00     | Baseline
June                 |   0.92     |   0.98     | Summer start
July-August          |   0.85     |   1.05     | Vacation mode
September            |   1.00     |   1.00     | Back to work
October              |   1.05     |   1.00     | Q4 planning
November             |   1.15     |   1.05     | Budget flush
December 1-15        |   1.20     |   1.10     | Year-end push
December 16-31       |   0.80     |   1.15     | Holiday shutdown

B2B SPECIFIC PATTERNS:
+-- Decision makers OOO: Jul-Aug, Dec 20-Jan 3
+-- Budget cycles: Jan (resets), Nov-Dec (use-or-lose)
+-- Conference season: Spring/Fall = more noise
+-- Summer: Lower CPM but lower response rates
```

## Benchmark Comparison Template

### When a user asks to evaluate their metrics:

```
METRIC EVALUATION - [ACCOUNT]
============================

YOUR METRICS vs BENCHMARKS

Metric      | Your Value | Benchmark | Difference | Status
------------+------------+-----------+------------+--------
CPL         |   $[X]     |   $[Y]    |  [+/-Z%]   | [Good/OK/Poor]
CPC         |   $[X]     |   $[Y]    |  [+/-Z%]   | [Good/OK/Poor]
CTR         |   [X]%     |   [Y]%    |  [+/-Z%]   | [Good/OK/Poor]
CVR (Form)  |   [X]%     |   [Y]%    |  [+/-Z%]   | [Good/OK/Poor]
SQL Rate    |   [X]%     |   [Y]%    |  [+/-Z%]   | [Good/OK/Poor]
Eng. Rate   |   [X]%     |   [Y]%    |  [+/-Z%]   | [Good/OK/Poor]

INTERPRETATION:
Good = Above benchmark (>10% better)
OK   = On benchmark (+/-10%)
Poor = Below benchmark (>10% worse)

CONTEXT FACTORS:
+-- Industry: [specified]
+-- Funnel Stage: [TOFU/MOFU/BOFU]
+-- Ad Format: [specified]
+-- Target Audience: [specified]

RECOMMENDATIONS:
+-- [Focus area 1]
+-- [Focus area 2]
+-- [Focus area 3]
```

## LTV:CAC Framework

```
LINKEDIN ADS ROI EVALUATION
==========================

Step 1: Calculate Customer Acquisition Cost (CAC)
+-- Total LinkedIn Spend: $[X]
+-- Number of Customers: [Y]
+-- CAC = $[X] / [Y] = $[Z]

Step 2: Determine Customer Lifetime Value (LTV)
+-- Average Contract Value: $[X]
+-- Average Customer Lifespan: [Y] years
+-- Gross Margin: [Z]%
+-- LTV = $[X] x [Y] x [Z]% = $[W]

Step 3: Evaluate LTV:CAC Ratio
+-- <1:1 = Unprofitable
+-- 1:1 - 3:1 = Break-even to marginal
+-- 3:1 - 5:1 = Healthy (target range)
+-- 5:1 - 7:1 = Excellent
+-- >7:1 = Under-investing in growth?

LINKEDIN TYPICAL LTV:CAC:
+-- SaaS B2B: 4:1 - 6:1 target
+-- Enterprise: 5:1 - 8:1 (long sales cycle)
+-- SMB: 3:1 - 5:1 (shorter cycle)
+-- Services: 4:1 - 7:1
```

## Example Interaction

**User**: "My LinkedIn campaign for SaaS has a CPL of $95 and an SQL rate of 18%. Is that good?"

**Claude response**:

"Let me compare your metrics with SaaS benchmarks:

---

**BENCHMARK COMPARISON - SaaS B2B:**

| Metric | Your Value | Benchmark Range | Status |
|--------|-------------|-----------------|--------|
| CPL | $95 | $80-120 (average) | Good |
| SQL Rate | 18% | 10-20% (average-good) | Good |
| Effective Cost per SQL | $528 | $400-600 (calculated) | OK |

---

**INTERPRETATION:**

**CPL ($95)** - Right in the middle of the average range for SaaS. Acceptable.

**SQL Rate (18%)** - Above average. This significantly compensates for the CPL.

**Cost per SQL ($528)** - This is the metric that truly matters. $95 / 18% = $528 per qualified lead.

---

**CONTEXT QUESTION:**
What is your Average Contract Value (ACV)?
- If ACV >$10k: Excellent performance
- If ACV $5-10k: Healthy
- If ACV <$5k: CPL optimization needed

**RECOMMENDATIONS:**

1. **Maintain SQL rate** - This is your strong point. Don't add extra friction.

2. **Test CPL reduction** via:
   - Broader targeting (can lower CPL 15-20%)
   - Organic content boost (thought leadership)
   - Lead Gen Forms vs Landing Page A/B test

3. **Track LTV:CAC ratio** - If it's >3:1, you can safely scale up.

Would you like me to analyze your Cost per SQL against your ACV?"

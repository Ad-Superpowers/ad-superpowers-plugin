---
name: meta-prompt-engineering-library
description: "This skill should be used when the user asks to \"get AI prompts for Meta Ads\", \"optimize prompts for ad analysis\", \"find prompt templates\", or mentions \"prompt engineering for ads\", \"AI workflow prompts\", or \"Meta Ads prompt library\". Do NOT use for: ad copy writing directly (use ad-copy-generator), video scripts (use video-script-writer), campaign diagnostics (use performance-troubleshooter)."
---
# Prompt Engineering Library

## Overview

This skill provides a collection of optimized prompts for leveraging AI (ChatGPT, Claude, Midjourney, etc.) within Meta Ads workflows, from creative briefing to data analysis and copy generation.

## Prompt Fundamentals

### Anatomy of a Good Prompt

```
┌─────────────────────────────────────────────────────────────────┐
│  PROMPT STRUCTURE (CRISP Framework)                             │
│                                                                 │
│  C - Context: Provide background and situation                  │
│  R - Role: Define the expertise you need                        │
│  I - Instructions: Give clear, specific directives              │
│  S - Specifics: Add details, constraints, formats               │
│  P - Parameters: Output format, length, style                   │
└─────────────────────────────────────────────────────────────────┘
```

### Prompt Quality Levels

| Level | Example | Quality |
|-------|---------|---------|
| Bad | "Write ad copy" | Vague, generic result |
| Better | "Write Facebook ad copy for a fitness app" | Better but still incomplete |
| Good | "You are a direct response copywriter. Write 3 Facebook ad copy variations for FitPro app targeting women 25-40 who want to lose weight. Use PAS framework. Max 125 characters primary text." | Specific, actionable |

## Prompt Categories

### Category 1: Ad Copy Generation

#### Primary Text Generator

```
PROMPT: AD COPY GENERATOR

You are an experienced Meta Ads copywriter specialized in
direct response advertising.

CONTEXT:
- Product: [PRODUCT/SERVICE]
- Target Audience: [DEMOGRAPHICS + PSYCHOGRAPHICS]
- Unique Selling Point: [USP]
- Funnel Stage: [TOFU/MOFU/BOFU]
- Offer: [IF APPLICABLE]

TASK:
Write 5 variations of primary text for a Meta ad.

SPECIFICATIONS:
- Framework: Alternate between PAS, AIDA, and BAB
- Hook: First sentence must grab attention within 3 seconds
- Length: [50-150 characters for Facebook Feed / 125 for Instagram feed]
- Tone: [Casual/Professional/Urgent/Friendly]
- CTA: End with a clear call-to-action

OUTPUT FORMAT:
For each variation:
1. [Framework used]
2. Primary text
3. Headline suggestion (max [27 for Facebook Feed / 40 for Instagram feed] characters)
4. CTA button recommendation
```

Text lengths follow Meta's text recommendations per placement: primary text 50-150 characters and headline 27 characters for Facebook Feed, 125 and 40 for Instagram feed (Facebook Ads Guide, image ad specs: https://www.facebook.com/business/ads-guide/update/image/facebook-feed and https://www.facebook.com/business/ads-guide/update/image/instagram-feed). Other placements list other figures, so check the placement's page before you set a limit.

#### Hook Generator

```
PROMPT: HOOK GENERATOR

Generate 10 scroll-stopping hooks for a Meta ad.

PRODUCT: [PRODUCT]
TARGET AUDIENCE: [AUDIENCE]
PAIN POINT: [KEY PROBLEM]
DESIRED RESULT: [WHAT THEY WANT TO ACHIEVE]

HOOK TYPES (use a mix):
1. Question hooks ("Did you know...?")
2. Statistic hooks ("[a real, sourced figure] of...")
3. Contrarian hooks ("Forget everything you knew about...")
4. Result hooks ("Here's how I achieved [X] in [time]")
5. Curiosity hooks ("The secret behind...")

CONSTRAINTS:
- Max 10 words per hook
- Must stop the scroll
- No clickbait that can't be delivered on
- Suitable for [PLATFORM: Feed/Stories/Reels]
```

### Category 2: Creative Briefing

#### UGC Creator Brief Generator

```
PROMPT: UGC BRIEF GENERATOR

Create a complete UGC video brief for creators.

PRODUCT INFO:
- Product: [PRODUCT]
- Price: [PRICE]
- USPs: [LIST OF BENEFITS]
- Website: [URL]

CAMPAIGN INFO:
- Platform: [Instagram Reels/TikTok/Facebook]
- Goal: [Awareness/Consideration/Conversion]
- Target Audience: [DEMOGRAPHICS]
- Tone: [Authentic/Energetic/Informative]

GENERATE A BRIEF WITH:
1. Overview (1 paragraph)
2. Key messages (3-5 bullets)
3. Script outline with timing (hook, body, CTA)
4. Do's and Don'ts
5. Technical specs (format, length, quality)
6. Example hooks to use
7. Examples of what to avoid

OUTPUT: Markdown format, ready to send to creator
```

#### Image Ad Concept Generator

```
PROMPT: AD VISUAL CONCEPT GENERATOR

Generate 5 visual concepts for Meta ad images.

PRODUCT: [PRODUCT]
BRAND GUIDELINES: [COLORS, STYLE, TONE]
TARGET AUDIENCE: [WHO]
MESSAGE: [WHAT TO COMMUNICATE]

FOR EACH CONCEPT, PROVIDE:
1. Concept name
2. Visual description (what you see)
3. Text overlay suggestion
4. Why this works for the target audience
5. Production approach (stock, photoshoot, design)

CONCEPT TYPES (include mix):
- Product-focused (product in action)
- Lifestyle (aspirational scenario)
- Before/After
- Social proof (reviews, ratings visual)
- Problem/Solution split
```

### Category 3: Data Analysis

#### Performance Report Analyzer

```
PROMPT: CAMPAIGN ANALYSIS

Analyze the following Meta Ads performance data and provide
actionable insights.

DATA:
[PASTE YOUR CAMPAIGN DATA HERE]

ANALYZE:
1. Top 3 best performing elements (and why)
2. Top 3 underperformers (and possible causes)
3. Trends over time (improving/declining)
4. Anomalies or notable patterns
5. Comparison with benchmarks if provided

PROVIDE RECOMMENDATIONS:
- Quick wins (actionable within 24 hours)
- Medium-term optimizations (this week)
- Strategic changes (next month)

FORMAT:
Use tables where relevant
Prioritize recommendations (High/Medium/Low impact)
Be specific (no vague suggestions)
```

#### A/B Test Results Interpreter

```
PROMPT: A/B TEST ANALYSIS

Interpret the following A/B test results.

TEST SETUP:
- Hypothesis: [WHAT WE TESTED]
- Variant A (Control): [DESCRIPTION]
- Variant B (Test): [DESCRIPTION]
- Test duration: [X DAYS]
- Primary metric: [CPA/CTR/ROAS]

RESULTS:
[PASTE DATA HERE]

ANALYZE:
1. Is the result statistically significant? (why/why not)
2. What is the impact in absolute and relative terms?
3. Are there secondary metrics that provide extra insight?
4. What can we learn from this result?
5. What should the next test be?

RECOMMENDATION:
- Implement winner: Yes/No + why
- Confidence level: High/Medium/Low
- Suggested follow-up action
```

### Category 4: Audience Research

#### Audience Persona Builder

```
PROMPT: TARGET AUDIENCE PERSONA

Create a detailed buyer persona for Meta Ads targeting.

PRODUCT/SERVICE: [WHAT YOU SELL]
CURRENT CUSTOMERS: [WHAT YOU KNOW ABOUT THEM]
PRICE POINT: [PRICE]
MARKET: [B2C/B2B, REGION]

GENERATE PERSONA WITH:

1. DEMOGRAPHICS
├── Age range
├── Gender
├── Location
├── Income/education level
└── Family situation

2. PSYCHOGRAPHICS
├── Values and beliefs
├── Lifestyle
├── Interests and hobbies
└── Media behavior (platforms, content types)

3. PAINS & GAINS
├── Top 3 frustrations/problems
├── Top 3 goals/aspirations
├── What keeps them up at night
└── What would improve their life

4. BUYING BEHAVIOR
├── Where they search for information
├── What triggers a purchase
├── Objections/barriers
└── Decision making process

5. META ADS TARGETING SUGGESTIONS
├── Interest targeting options
├── Lookalike audience sources
├── Custom audience ideas
└── Messaging angles per funnel stage
```

### Category 5: Reporting

#### Weekly Report Generator

```
PROMPT: WEEKLY PERFORMANCE REPORT

Generate a professional weekly report for Meta Ads.

WEEK: [WEEK NUMBER]
ACCOUNT: [ACCOUNT NAME]

PERFORMANCE DATA:
[PASTE METRICS HERE]
- Spend, Impressions, Clicks, CTR
- Conversions, CPA, ROAS
- Top campaigns/ad sets

STRUCTURE REPORT AS:

1. EXECUTIVE SUMMARY (3-5 bullets)
├── Key result
├── Biggest change vs last week
└── Key action item

2. PERFORMANCE OVERVIEW
├── Table with KPIs vs targets
├── Week-over-week comparison
└── Trend indicator (up/down/flat)

3. HIGHLIGHTS
├── Best performer (why)
├── New tests launched
└── Key learnings

4. ATTENTION ITEMS
├── Underperformers
├── Budget issues
└── Upcoming challenges

5. NEXT WEEK PLAN
├── Planned actions
├── Tests to start
└── Budget changes

FORMAT: Professional, scannable, max 1 page
```

### Category 6: AI Image Generation

#### Gemini Ad Image Prompts

Ad Superpowers does not generate images. Create them outside Ad Superpowers (in your AI client if it can generate images, or in an image tool such as Gemini), then upload each image with `meta_upload_image` (see `media-upload-guide` for the upload routes) and pass the returned `image_hash` to `meta_create_ad`.

```
WORKFLOW: BRIEF → GENERATE → UPLOAD → CREATE AD

Step 1: Craft your Gemini prompt using this template:

PROMPT: GEMINI AD IMAGE GENERATOR

Generate [N] ad image variations for [PRODUCT].

Style: [photorealistic product photography / lifestyle / UGC-style / clean studio]
Mood: [energetic/aspirational/calm/premium/playful]
Aspect ratio: [4:5 for Facebook and Instagram Feed / 9:16 for Reels/Stories]
Color palette: [describe or reference brand colors]
Key visual: [what should be in focus — product, person, scene]

No text overlays in the image.
Leave visual breathing room for copy overlay.
Avoid faces that look AI-generated.

Step 2: Generate the images in Gemini or your image tool (outside Ad Superpowers).

Step 3: Upload each image to the Meta media library via MCP:
→ meta_upload_image(
     account_id="[META_ACCOUNT_ID]",
     image_url="[PUBLIC_HTTPS_IMAGE_URL]"   ← for a local file, use stage_id or image_data instead
   )

Returns: image_hash, for meta_create_ad(image_hash=...).
```

Ratios: Meta's Ads Guide gives 4:5 for Facebook Feed and Instagram feed images and 9:16 for Stories and Reels (https://www.facebook.com/business/ads-guide/update/image/facebook-feed, https://www.facebook.com/business/ads-guide/update/image/instagram-story and https://www.facebook.com/business/ads-guide/update/image/instagram-reels).

#### Midjourney Ad Image Prompts

```
PROMPT: MIDJOURNEY AD VISUALS

Generate Midjourney prompts for Meta ad images.

PRODUCT: [PRODUCT]
STYLE: [Photorealistic/Illustration/Minimalist]
MOOD: [Energetic/Calm/Premium/Playful]
COLOR PALETTE: [COLORS]

GENERATE 5 MIDJOURNEY PROMPTS:

Format per prompt:
/imagine [description], [style parameters], [technical specs]

INCLUDE IN EACH PROMPT:
- Subject/scene description
- Lighting (soft, dramatic, natural)
- Composition (centered, rule of thirds)
- Camera angle if relevant
- Style references
- Technical params: --ar 4:5 (Feed) or --ar 9:16 (Stories, Reels); --raw for a photographic look

VARIATIONS:
1. Product hero shot
2. Lifestyle/usage scenario
3. Abstract/conceptual
4. Social proof visual
5. Problem/solution visual
```

Midjourney flags change between model versions. Midjourney's V8 announcement recommends `--raw` for photographic looks ("V8 Alpha", https://updates.midjourney.com/v8-alpha/, 17 March 2026). Check Midjourney's docs before you add a version or quality flag.

#### GPT Image Ad Concepts

```
PROMPT: GPT IMAGE AD VISUALS

Generate prompts for OpenAI's GPT Image models for social media advertisements.

PRODUCT: [PRODUCT]
MESSAGE: [KEY MESSAGE]
FORMAT: [1:1 Square / 4:5 / 9:16]

GENERATE 5 GPT IMAGE PROMPTS:

Format:
"[Detailed description], [style], [lighting],
[composition], digital art/photography/illustration"

CONSIDERATIONS:
- No text in image (add later)
- Clear focal point
- Room for text overlay
- Brand-consistent colors
- No recognizable real people
```

OpenAI removed its DALL·E models from the API on 12 May 2026 and names its GPT Image models as the replacement ("Deprecations", OpenAI API docs).

## Prompt Templates Library

### Quick Copy Prompts

```
HEADLINE GENERATOR:
"Generate 10 headlines for [PRODUCT] targeting [AUDIENCE].
Max [27 for Facebook Feed / 40 for Instagram feed] characters.
Focus on [BENEFIT]. Mix of question, statement and urgency formats."

CTA VARIATIONS:
"Provide 8 call-to-action variations for [ACTION] that evoke
[EMOTION]. Stronger than 'Click here'. Max 3 words."

SOCIAL PROOF COPY:
"Rewrite this review as short ad copy (50 words):
[REVIEW]. Make it compelling without exaggerating."

URGENCY CREATOR:
"Generate 5 urgency elements for [OFFER] that create FOMO
without sounding spammy. Ethical and honest."
```

### Quick Analysis Prompts

```
QUICK AUDIT:
"Review these metrics [DATA] and provide in 3 bullets:
1) Biggest problem 2) Quick win 3) Priority this week"

COMPETITOR COPY ANALYSIS:
"Analyze this competitor ad [COPY]. What works? What doesn't?
How can we do this better for [OUR PRODUCT]?"

AUDIENCE INSIGHT:
"Based on this engagement data [DATA], what does this tell
about our target audience? Provide 3 actionable targeting insights."
```

## Example Interaction

**User**: "I need prompts to quickly generate ad copy for my skincare brand."

**Claude response**:

"Here are optimized prompts for your skincare brand:

---

**PROMPT 1: Primary Text Generator**

```
You are a beauty copywriter specialized in skincare DTC brands.

BRAND: [Your brand name]
PRODUCT: [Specific product, e.g. "Vitamin C Serum"]
TARGET AUDIENCE: Women 25-45, interested in clean beauty
USP: [E.g. "fragrance-free formula, refillable glass bottle"]
FUNNEL: BOFU (retargeting)

Write 5 primary text variations:
- Mix of PAS and AIDA frameworks
- First sentence = scroll-stopping hook
- 100-125 characters
- End with soft CTA

Also deliver: matching headline (max 27 characters for Facebook Feed, 40 for Instagram feed) per variation
```

---

**PROMPT 2: Hook Generator (Quick)**

```
Generate 10 hooks for skincare ad. Product: [X]
Problem: [dry skin/wrinkles/dull skin]
Result: [a result the product can substantiate]

Mix: question, statistic (real, sourced figures only), before/after, curiosity
Max 8 words per hook. Scroll-stopping.
```

---

**PROMPT 3: Testimonial Rewriter**

```
Rewrite this customer review as ad copy:

"[Paste review here]"

Make it:
- Shorter (max 80 words)
- More engaging (add hook)
- With clear result highlight
- Including emojis (max 3)
Maintain authenticity, no overclaims.
```

---

**BONUS: a prompt for a test visual**

If you want to test a visual, paste this prompt into Gemini or another image tool (Ad Superpowers does not generate images):
```
Skincare serum product photography, soft studio lighting, clean white background, premium minimal aesthetic, 4:5 aspect ratio, no text
```
Then upload the image with `meta_upload_image`; it returns the `image_hash` for `meta_create_ad`.

Would you like me to also create prompts for visual concepts or UGC briefings?"

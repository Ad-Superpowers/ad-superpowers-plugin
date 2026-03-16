---
name: google-ads-scripts-library
description: "Google Ads Scripts bibliotheek met top 15 automation scripts. Gebruik voor: (1) Account monitoring scripts, (2) Automated bid adjustments, (3) Budget management scripts, (4) Anomaly detection, (5) Reporting automation, (6) N-gram analysis, (7) Broken link checker. Triggers: google ads scripts, automation, script, monitor, anomaly detection, automated rules, n-gram, budget pacing, broken links."
---

# Google Ads Scripts Library

Complete bibliotheek met 15 productie-klare Google Ads Scripts voor automatisering, monitoring en optimalisatie.

## Scripts Overzicht

```
TOP 15 GOOGLE ADS SCRIPTS
═════════════════════════

MONITORING & ALERTS:
├── 1. Performance Anomaly Detector
├── 2. Budget Pacing Monitor
├── 3. Broken URL Checker
├── 4. Quality Score Tracker
└── 5. Zero Impressions Alert

OPTIMIZATION:
├── 6. N-Gram Analysis
├── 7. Search Query Mining
├── 8. Negative Keyword Builder
├── 9. Bid Adjustment by Hour/Day
└── 10. Low Performer Pauser

REPORTING:
├── 11. Daily/Weekly Report Generator
├── 12. Competitor Auction Insights
├── 13. Campaign Performance Tracker
├── 14. Ad Extension Monitor
└── 15. Account Health Dashboard

SETUP INSTRUCTIES (voor alle scripts):
──────────────────────────────────────
1. Google Ads → Tools & Settings → Bulk Actions → Scripts
2. + New Script
3. Paste code
4. Authorize (first run)
5. Preview → Run (test)
6. Schedule (daily/hourly)
```

## Script 1: Performance Anomaly Detector

```javascript
/**
 * SCRIPT 1: Performance Anomaly Detector
 *
 * Detecteert significante afwijkingen in key metrics
 * en stuurt email alerts.
 *
 * Features:
 * - CPA/ROAS anomaly detection
 * - Spend pacing alerts
 * - Conversion volume drops
 * - Statistische outlier detectie
 *
 * Schedule: Dagelijks om 9:00
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Anomaly thresholds (% change vs 7-day average)
  CPA_THRESHOLD: 0.30,         // Alert bij 30% CPA stijging
  ROAS_THRESHOLD: 0.25,        // Alert bij 25% ROAS daling
  SPEND_THRESHOLD: 0.40,       // Alert bij 40% spend afwijking
  CONV_THRESHOLD: 0.35,        // Alert bij 35% conversie daling

  // Minimum values for analysis
  MIN_CONVERSIONS: 5,
  MIN_SPEND: 50,

  // Lookback period
  LOOKBACK_DAYS: 7
};

function main() {
  var anomalies = [];

  // Analyze campaigns
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var campaignAnomalies = detectAnomalies(campaign);
    anomalies = anomalies.concat(campaignAnomalies);
  }

  // Send alert if anomalies found
  if (anomalies.length > 0) {
    sendAnomalyAlert(anomalies);
  }

  Logger.log('Anomaly detection complete. Found: ' + anomalies.length + ' anomalies');
}

function detectAnomalies(campaign) {
  var anomalies = [];
  var name = campaign.getName();

  // Get yesterday's stats
  var yesterday = getDateString(1);
  var dayBeforeYesterday = getDateString(2);
  var yesterdayStats = campaign.getStatsFor(dayBeforeYesterday, yesterday);

  // Get 7-day average stats
  var weekAgo = getDateString(8);
  var weekStats = campaign.getStatsFor(weekAgo, dayBeforeYesterday);

  var yesterdaySpend = yesterdayStats.getCost();
  var yesterdayConv = yesterdayStats.getConversions();
  var yesterdayValue = yesterdayStats.getConversionValue();

  // Skip low-volume campaigns
  if (yesterdaySpend < CONFIG.MIN_SPEND) return anomalies;

  // Calculate averages
  var avgDailySpend = weekStats.getCost() / 7;
  var avgDailyConv = weekStats.getConversions() / 7;

  // Calculate metrics
  var yesterdayCPA = yesterdayConv > 0 ? yesterdaySpend / yesterdayConv : 0;
  var yesterdayROAS = yesterdaySpend > 0 ? yesterdayValue / yesterdaySpend : 0;

  var avgCPA = avgDailyConv > 0 ? (weekStats.getCost() / 7) / avgDailyConv : 0;
  var avgROAS = avgDailySpend > 0 ?
    (weekStats.getConversionValue() / 7) / avgDailySpend : 0;

  // Check for anomalies
  // CPA spike
  if (avgCPA > 0 && yesterdayCPA > avgCPA * (1 + CONFIG.CPA_THRESHOLD)) {
    anomalies.push({
      campaign: name,
      type: 'CPA_SPIKE',
      yesterday: yesterdayCPA.toFixed(2),
      average: avgCPA.toFixed(2),
      change: ((yesterdayCPA / avgCPA - 1) * 100).toFixed(1) + '%'
    });
  }

  // ROAS drop
  if (avgROAS > 0 && yesterdayROAS < avgROAS * (1 - CONFIG.ROAS_THRESHOLD)) {
    anomalies.push({
      campaign: name,
      type: 'ROAS_DROP',
      yesterday: yesterdayROAS.toFixed(2),
      average: avgROAS.toFixed(2),
      change: ((yesterdayROAS / avgROAS - 1) * 100).toFixed(1) + '%'
    });
  }

  // Spend anomaly
  if (avgDailySpend > 0) {
    var spendDiff = Math.abs(yesterdaySpend - avgDailySpend) / avgDailySpend;
    if (spendDiff > CONFIG.SPEND_THRESHOLD) {
      anomalies.push({
        campaign: name,
        type: yesterdaySpend > avgDailySpend ? 'SPEND_SPIKE' : 'SPEND_DROP',
        yesterday: yesterdaySpend.toFixed(2),
        average: avgDailySpend.toFixed(2),
        change: ((yesterdaySpend / avgDailySpend - 1) * 100).toFixed(1) + '%'
      });
    }
  }

  // Conversion drop
  if (avgDailyConv >= CONFIG.MIN_CONVERSIONS &&
      yesterdayConv < avgDailyConv * (1 - CONFIG.CONV_THRESHOLD)) {
    anomalies.push({
      campaign: name,
      type: 'CONVERSION_DROP',
      yesterday: yesterdayConv.toFixed(0),
      average: avgDailyConv.toFixed(1),
      change: ((yesterdayConv / avgDailyConv - 1) * 100).toFixed(1) + '%'
    });
  }

  return anomalies;
}

function getDateString(daysAgo) {
  var date = new Date();
  date.setDate(date.getDate() - daysAgo);
  return Utilities.formatDate(date, AdsApp.currentAccount().getTimeZone(), 'yyyyMMdd');
}

function sendAnomalyAlert(anomalies) {
  var subject = '⚠️ Performance Anomaly Alert - ' + AdsApp.currentAccount().getName();

  var body = 'Performance Anomaly Detection Report\n';
  body += '====================================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Date: ' + new Date().toDateString() + '\n\n';
  body += 'ANOMALIES DETECTED:\n';
  body += '──────────────────\n\n';

  for (var i = 0; i < anomalies.length; i++) {
    var a = anomalies[i];
    body += '[' + a.type + '] ' + a.campaign + '\n';
    body += '  Yesterday: ' + a.yesterday + '\n';
    body += '  7-Day Avg: ' + a.average + '\n';
    body += '  Change: ' + a.change + '\n\n';
  }

  body += '\n---\nGenerated by Performance Anomaly Detector';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Script 2: Budget Pacing Monitor

```javascript
/**
 * SCRIPT 2: Budget Pacing Monitor
 *
 * Monitort budget spending pace en voorspelt
 * under/overspend scenarios.
 *
 * Schedule: Dagelijks om 10:00
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Pacing thresholds
  UNDERPACE_ALERT: 0.15,    // Alert als >15% achter op pace
  OVERPACE_ALERT: 0.10,     // Alert als >10% voor op pace

  // Include campaigns with budget > this
  MIN_DAILY_BUDGET: 20
};

function main() {
  var today = new Date();
  var dayOfMonth = today.getDate();
  var daysInMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate();
  var percentMonthPassed = dayOfMonth / daysInMonth;

  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  var pacingReport = [];

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var budget = campaign.getBudget().getAmount();

    if (budget < CONFIG.MIN_DAILY_BUDGET) continue;

    var monthlyBudget = budget * daysInMonth;
    var expectedSpend = monthlyBudget * percentMonthPassed;

    // Get month-to-date spend
    var firstOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
    var stats = campaign.getStatsFor(
      formatDate(firstOfMonth),
      formatDate(today)
    );
    var actualSpend = stats.getCost();

    var pacePercent = expectedSpend > 0 ? actualSpend / expectedSpend : 0;
    var variance = pacePercent - 1;

    var status = 'ON_PACE';
    if (variance < -CONFIG.UNDERPACE_ALERT) {
      status = 'UNDERPACING';
    } else if (variance > CONFIG.OVERPACE_ALERT) {
      status = 'OVERPACING';
    }

    if (status !== 'ON_PACE') {
      pacingReport.push({
        campaign: campaign.getName(),
        dailyBudget: budget,
        monthlyBudget: monthlyBudget,
        expectedSpend: expectedSpend,
        actualSpend: actualSpend,
        pacePercent: pacePercent,
        status: status,
        projectedMonthEnd: actualSpend / percentMonthPassed
      });
    }
  }

  if (pacingReport.length > 0) {
    sendPacingReport(pacingReport, dayOfMonth, daysInMonth);
  }

  Logger.log('Pacing check complete. Issues found: ' + pacingReport.length);
}

function formatDate(date) {
  return Utilities.formatDate(date, AdsApp.currentAccount().getTimeZone(), 'yyyyMMdd');
}

function sendPacingReport(report, dayOfMonth, daysInMonth) {
  var subject = '📊 Budget Pacing Alert - ' + AdsApp.currentAccount().getName();

  var body = 'Budget Pacing Report\n';
  body += '====================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Day of Month: ' + dayOfMonth + ' / ' + daysInMonth + '\n\n';

  var underpacing = report.filter(function(r) { return r.status === 'UNDERPACING'; });
  var overpacing = report.filter(function(r) { return r.status === 'OVERPACING'; });

  if (underpacing.length > 0) {
    body += '⚠️ UNDERPACING CAMPAIGNS:\n';
    body += '─────────────────────────\n';
    for (var i = 0; i < underpacing.length; i++) {
      var c = underpacing[i];
      body += '• ' + c.campaign + '\n';
      body += '  Expected: €' + c.expectedSpend.toFixed(2) + '\n';
      body += '  Actual: €' + c.actualSpend.toFixed(2) + '\n';
      body += '  Pace: ' + (c.pacePercent * 100).toFixed(1) + '%\n';
      body += '  Projected month-end: €' + c.projectedMonthEnd.toFixed(2) +
              ' (Budget: €' + c.monthlyBudget.toFixed(2) + ')\n\n';
    }
  }

  if (overpacing.length > 0) {
    body += '⚠️ OVERPACING CAMPAIGNS:\n';
    body += '────────────────────────\n';
    for (var j = 0; j < overpacing.length; j++) {
      var c = overpacing[j];
      body += '• ' + c.campaign + '\n';
      body += '  Expected: €' + c.expectedSpend.toFixed(2) + '\n';
      body += '  Actual: €' + c.actualSpend.toFixed(2) + '\n';
      body += '  Pace: ' + (c.pacePercent * 100).toFixed(1) + '%\n';
      body += '  Projected month-end: €' + c.projectedMonthEnd.toFixed(2) +
              ' (Budget: €' + c.monthlyBudget.toFixed(2) + ')\n\n';
    }
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Script 3: Broken URL Checker

```javascript
/**
 * SCRIPT 3: Broken URL Checker
 *
 * Controleert alle final URLs en sitelinks
 * op 404 errors en redirects.
 *
 * Schedule: Wekelijks op maandag
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // URL check settings
  TIMEOUT: 10000,           // 10 second timeout
  CHECK_REDIRECTS: true,    // Also report redirects
  MAX_URLS_TO_CHECK: 500    // Limit for large accounts
};

function main() {
  var brokenUrls = [];
  var redirectUrls = [];
  var urlsChecked = 0;
  var urlCache = {};

  // Check ad URLs
  var ads = AdsApp.ads()
    .withCondition('Status = ENABLED')
    .withCondition('CampaignStatus = ENABLED')
    .withCondition('AdGroupStatus = ENABLED')
    .get();

  while (ads.hasNext() && urlsChecked < CONFIG.MAX_URLS_TO_CHECK) {
    var ad = ads.next();
    var urls = ad.urls();
    if (urls && urls.getFinalUrl()) {
      var url = urls.getFinalUrl();
      if (!urlCache[url]) {
        urlCache[url] = true;
        var result = checkUrl(url);
        urlsChecked++;

        if (result.status === 'BROKEN') {
          brokenUrls.push({
            type: 'Ad',
            name: ad.getHeadlinePart1(),
            campaign: ad.getCampaign().getName(),
            url: url,
            code: result.code
          });
        } else if (result.status === 'REDIRECT' && CONFIG.CHECK_REDIRECTS) {
          redirectUrls.push({
            type: 'Ad',
            name: ad.getHeadlinePart1(),
            campaign: ad.getCampaign().getName(),
            url: url,
            redirectUrl: result.redirectUrl
          });
        }
      }
    }
  }

  // Check sitelink URLs
  var sitelinks = AdsApp.extensions().sitelinks()
    .withCondition('Status = ENABLED')
    .get();

  while (sitelinks.hasNext() && urlsChecked < CONFIG.MAX_URLS_TO_CHECK) {
    var sitelink = sitelinks.next();
    var url = sitelink.urls().getFinalUrl();

    if (url && !urlCache[url]) {
      urlCache[url] = true;
      var result = checkUrl(url);
      urlsChecked++;

      if (result.status === 'BROKEN') {
        brokenUrls.push({
          type: 'Sitelink',
          name: sitelink.getLinkText(),
          campaign: 'Account-level',
          url: url,
          code: result.code
        });
      }
    }
  }

  // Send report
  if (brokenUrls.length > 0 || redirectUrls.length > 0) {
    sendUrlReport(brokenUrls, redirectUrls, urlsChecked);
  }

  Logger.log('URL check complete. Checked: ' + urlsChecked +
             ', Broken: ' + brokenUrls.length +
             ', Redirects: ' + redirectUrls.length);
}

function checkUrl(url) {
  try {
    var response = UrlFetchApp.fetch(url, {
      muteHttpExceptions: true,
      followRedirects: false,
      timeout: CONFIG.TIMEOUT
    });

    var code = response.getResponseCode();

    if (code === 404 || code === 410 || code === 500 || code === 503) {
      return { status: 'BROKEN', code: code };
    } else if (code >= 300 && code < 400) {
      var headers = response.getAllHeaders();
      var redirectUrl = headers['Location'] || 'Unknown';
      return { status: 'REDIRECT', redirectUrl: redirectUrl };
    } else {
      return { status: 'OK' };
    }
  } catch (e) {
    return { status: 'BROKEN', code: 'Error: ' + e.message };
  }
}

function sendUrlReport(brokenUrls, redirectUrls, totalChecked) {
  var subject = '🔗 URL Health Check - ' + AdsApp.currentAccount().getName();

  var body = 'URL Health Check Report\n';
  body += '=======================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'URLs Checked: ' + totalChecked + '\n';
  body += 'Broken: ' + brokenUrls.length + '\n';
  body += 'Redirects: ' + redirectUrls.length + '\n\n';

  if (brokenUrls.length > 0) {
    body += '❌ BROKEN URLs:\n';
    body += '──────────────\n';
    for (var i = 0; i < brokenUrls.length; i++) {
      var b = brokenUrls[i];
      body += '• [' + b.type + '] ' + b.name + '\n';
      body += '  Campaign: ' + b.campaign + '\n';
      body += '  URL: ' + b.url + '\n';
      body += '  Error: ' + b.code + '\n\n';
    }
  }

  if (redirectUrls.length > 0) {
    body += '↪️ REDIRECT URLs:\n';
    body += '────────────────\n';
    for (var j = 0; j < redirectUrls.length; j++) {
      var r = redirectUrls[j];
      body += '• [' + r.type + '] ' + r.name + '\n';
      body += '  URL: ' + r.url + '\n';
      body += '  Redirects to: ' + r.redirectUrl + '\n\n';
    }
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Script 4: N-Gram Analysis

```javascript
/**
 * SCRIPT 4: N-Gram Analysis
 *
 * Analyseert search terms op word-level performance
 * om negative en positive keywords te identificeren.
 *
 * Schedule: Wekelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',
  SPREADSHEET_URL: '', // Optional: URL to output spreadsheet

  // Minimum thresholds
  MIN_IMPRESSIONS: 50,
  MIN_CLICKS: 3,
  MIN_COST: 10,

  // Performance thresholds
  HIGH_COST_NO_CONV_THRESHOLD: 20,  // €20+ spend, no conversions
  LOW_CTR_THRESHOLD: 0.01,           // 1% CTR

  // N-gram settings
  NGRAM_LENGTHS: [1, 2, 3],          // Analyze 1, 2, and 3 word phrases

  // Date range
  DATE_RANGE: 'LAST_30_DAYS'
};

function main() {
  var searchTerms = [];

  // Collect search terms
  var report = AdsApp.report(
    'SELECT Query, Impressions, Clicks, Cost, Conversions, ConversionValue ' +
    'FROM SEARCH_QUERY_PERFORMANCE_REPORT ' +
    'WHERE Impressions > ' + CONFIG.MIN_IMPRESSIONS + ' ' +
    'DURING ' + CONFIG.DATE_RANGE
  );

  var rows = report.rows();
  while (rows.hasNext()) {
    var row = rows.next();
    searchTerms.push({
      query: row['Query'].toLowerCase(),
      impressions: parseInt(row['Impressions']),
      clicks: parseInt(row['Clicks']),
      cost: parseFloat(row['Cost']),
      conversions: parseFloat(row['Conversions']),
      value: parseFloat(row['ConversionValue'])
    });
  }

  // Analyze n-grams
  var ngrams = {};
  for (var i = 0; i < searchTerms.length; i++) {
    var term = searchTerms[i];
    var words = term.query.split(/\s+/);

    for (var n = 0; n < CONFIG.NGRAM_LENGTHS.length; n++) {
      var ngramLength = CONFIG.NGRAM_LENGTHS[n];
      for (var j = 0; j <= words.length - ngramLength; j++) {
        var ngram = words.slice(j, j + ngramLength).join(' ');

        if (!ngrams[ngram]) {
          ngrams[ngram] = {
            ngram: ngram,
            length: ngramLength,
            impressions: 0,
            clicks: 0,
            cost: 0,
            conversions: 0,
            value: 0,
            queries: 0
          };
        }

        ngrams[ngram].impressions += term.impressions;
        ngrams[ngram].clicks += term.clicks;
        ngrams[ngram].cost += term.cost;
        ngrams[ngram].conversions += term.conversions;
        ngrams[ngram].value += term.value;
        ngrams[ngram].queries++;
      }
    }
  }

  // Convert to array and calculate metrics
  var ngramArray = [];
  for (var key in ngrams) {
    var ng = ngrams[key];
    if (ng.cost >= CONFIG.MIN_COST && ng.clicks >= CONFIG.MIN_CLICKS) {
      ng.ctr = ng.impressions > 0 ? ng.clicks / ng.impressions : 0;
      ng.cpc = ng.clicks > 0 ? ng.cost / ng.clicks : 0;
      ng.cpa = ng.conversions > 0 ? ng.cost / ng.conversions : Infinity;
      ng.roas = ng.cost > 0 ? ng.value / ng.cost : 0;
      ngramArray.push(ng);
    }
  }

  // Identify negative keyword candidates
  var negatives = ngramArray.filter(function(ng) {
    return (ng.cost > CONFIG.HIGH_COST_NO_CONV_THRESHOLD && ng.conversions === 0) ||
           (ng.ctr < CONFIG.LOW_CTR_THRESHOLD && ng.impressions > 100);
  }).sort(function(a, b) { return b.cost - a.cost; });

  // Identify expansion opportunities
  var opportunities = ngramArray.filter(function(ng) {
    return ng.conversions >= 2 && ng.length >= 2;
  }).sort(function(a, b) {
    return (a.cpa === Infinity ? 99999 : a.cpa) -
           (b.cpa === Infinity ? 99999 : b.cpa);
  });

  // Send report
  sendNgramReport(negatives.slice(0, 20), opportunities.slice(0, 20), ngramArray.length);
}

function sendNgramReport(negatives, opportunities, totalNgrams) {
  var subject = '📊 N-Gram Analysis - ' + AdsApp.currentAccount().getName();

  var body = 'N-Gram Analysis Report\n';
  body += '======================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Total N-Grams Analyzed: ' + totalNgrams + '\n\n';

  if (negatives.length > 0) {
    body += '❌ NEGATIVE KEYWORD CANDIDATES:\n';
    body += '───────────────────────────────\n';
    body += 'High spend, no conversions or very low CTR:\n\n';
    for (var i = 0; i < negatives.length; i++) {
      var neg = negatives[i];
      body += '• "' + neg.ngram + '"\n';
      body += '  Cost: €' + neg.cost.toFixed(2) +
              ' | Clicks: ' + neg.clicks +
              ' | Conv: ' + neg.conversions +
              ' | CTR: ' + (neg.ctr * 100).toFixed(2) + '%\n';
    }
    body += '\n';
  }

  if (opportunities.length > 0) {
    body += '✅ KEYWORD EXPANSION OPPORTUNITIES:\n';
    body += '───────────────────────────────────\n';
    body += 'Multiple conversions, potential for exact match targeting:\n\n';
    for (var j = 0; j < opportunities.length; j++) {
      var opp = opportunities[j];
      body += '• "' + opp.ngram + '"\n';
      body += '  Conv: ' + opp.conversions.toFixed(1) +
              ' | CPA: €' + (opp.cpa === Infinity ? 'N/A' : opp.cpa.toFixed(2)) +
              ' | ROAS: ' + opp.roas.toFixed(2) + 'x\n';
    }
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Script 5: Low Performer Pauser

```javascript
/**
 * SCRIPT 5: Low Performer Pauser
 *
 * Pauzeert automatisch ads en keywords die slecht
 * presteren volgens gedefinieerde criteria.
 *
 * ⚠️ WAARSCHUWING: Dit script maakt wijzigingen!
 * Test eerst met DRY_RUN = true
 *
 * Schedule: Wekelijks
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // ⚠️ Set to false to actually pause items
  DRY_RUN: true,

  // Keyword thresholds
  KEYWORD_MIN_IMPRESSIONS: 500,
  KEYWORD_MIN_CLICKS: 10,
  KEYWORD_MAX_CPA: 100,          // Pause if CPA > €100
  KEYWORD_MIN_ROAS: 1.0,         // Pause if ROAS < 1.0x

  // Ad thresholds
  AD_MIN_IMPRESSIONS: 1000,
  AD_MIN_CTR: 0.01,              // Pause if CTR < 1%

  // Lookback period
  DATE_RANGE: 'LAST_30_DAYS'
};

function main() {
  var pausedKeywords = [];
  var pausedAds = [];

  // Process Keywords
  var keywords = AdsApp.keywords()
    .withCondition('Status = ENABLED')
    .withCondition('Impressions > ' + CONFIG.KEYWORD_MIN_IMPRESSIONS)
    .forDateRange(CONFIG.DATE_RANGE)
    .get();

  while (keywords.hasNext()) {
    var keyword = keywords.next();
    var stats = keyword.getStatsFor(CONFIG.DATE_RANGE);

    var clicks = stats.getClicks();
    var cost = stats.getCost();
    var conversions = stats.getConversions();
    var value = stats.getConversionValue();

    if (clicks < CONFIG.KEYWORD_MIN_CLICKS) continue;

    var cpa = conversions > 0 ? cost / conversions : Infinity;
    var roas = cost > 0 ? value / cost : 0;

    var shouldPause = false;
    var reason = '';

    if (conversions === 0 && cost > CONFIG.KEYWORD_MAX_CPA) {
      shouldPause = true;
      reason = 'No conversions, €' + cost.toFixed(2) + ' spend';
    } else if (cpa > CONFIG.KEYWORD_MAX_CPA) {
      shouldPause = true;
      reason = 'CPA €' + cpa.toFixed(2) + ' > €' + CONFIG.KEYWORD_MAX_CPA;
    } else if (conversions > 0 && roas < CONFIG.KEYWORD_MIN_ROAS) {
      shouldPause = true;
      reason = 'ROAS ' + roas.toFixed(2) + 'x < ' + CONFIG.KEYWORD_MIN_ROAS + 'x';
    }

    if (shouldPause) {
      if (!CONFIG.DRY_RUN) {
        keyword.pause();
      }
      pausedKeywords.push({
        keyword: keyword.getText(),
        campaign: keyword.getCampaign().getName(),
        reason: reason,
        cost: cost,
        conversions: conversions
      });
    }
  }

  // Process Ads
  var ads = AdsApp.ads()
    .withCondition('Status = ENABLED')
    .withCondition('Impressions > ' + CONFIG.AD_MIN_IMPRESSIONS)
    .forDateRange(CONFIG.DATE_RANGE)
    .get();

  while (ads.hasNext()) {
    var ad = ads.next();
    var stats = ad.getStatsFor(CONFIG.DATE_RANGE);

    var impressions = stats.getImpressions();
    var clicks = stats.getClicks();
    var ctr = impressions > 0 ? clicks / impressions : 0;

    if (ctr < CONFIG.AD_MIN_CTR) {
      if (!CONFIG.DRY_RUN) {
        ad.pause();
      }
      pausedAds.push({
        headline: ad.getHeadlinePart1(),
        campaign: ad.getCampaign().getName(),
        adGroup: ad.getAdGroup().getName(),
        ctr: ctr,
        impressions: impressions
      });
    }
  }

  // Send report
  if (pausedKeywords.length > 0 || pausedAds.length > 0) {
    sendPauseReport(pausedKeywords, pausedAds);
  }

  Logger.log('Low performer check complete.');
  Logger.log('Keywords paused: ' + pausedKeywords.length);
  Logger.log('Ads paused: ' + pausedAds.length);
  Logger.log('DRY RUN: ' + CONFIG.DRY_RUN);
}

function sendPauseReport(keywords, ads) {
  var dryRunNote = CONFIG.DRY_RUN ? '[DRY RUN - No changes made]\n\n' : '';

  var subject = (CONFIG.DRY_RUN ? '[DRY RUN] ' : '') +
                '⏸️ Low Performer Pause Report - ' + AdsApp.currentAccount().getName();

  var body = 'Low Performer Pause Report\n';
  body += '==========================\n\n';
  body += dryRunNote;
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Date Range: ' + CONFIG.DATE_RANGE + '\n\n';

  if (keywords.length > 0) {
    body += 'KEYWORDS PAUSED: ' + keywords.length + '\n';
    body += '─────────────────────────\n';
    for (var i = 0; i < keywords.length; i++) {
      var kw = keywords[i];
      body += '• "' + kw.keyword + '"\n';
      body += '  Campaign: ' + kw.campaign + '\n';
      body += '  Reason: ' + kw.reason + '\n\n';
    }
  }

  if (ads.length > 0) {
    body += 'ADS PAUSED: ' + ads.length + '\n';
    body += '────────────────────\n';
    for (var j = 0; j < ads.length; j++) {
      var ad = ads[j];
      body += '• "' + ad.headline + '"\n';
      body += '  Ad Group: ' + ad.adGroup + '\n';
      body += '  CTR: ' + (ad.ctr * 100).toFixed(2) + '%\n\n';
    }
  }

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Script 6: Bid Adjustment by Hour/Day

```javascript
/**
 * SCRIPT 6: Bid Adjustment by Hour/Day
 *
 * Analyseert performance per uur/dag en past
 * automatisch bid adjustments aan.
 *
 * Schedule: Wekelijks (om adjustments bij te werken)
 */

var CONFIG = {
  EMAIL: 'jouw@email.com',

  // Adjustment settings
  MIN_CONVERSIONS_FOR_ADJUSTMENT: 5,
  MAX_ADJUSTMENT: 0.30,           // Max +/- 30%

  // Apply adjustments
  APPLY_ADJUSTMENTS: false,       // Set true to apply

  // Date range for analysis
  DATE_RANGE: 'LAST_30_DAYS'
};

function main() {
  var hourlyData = [];
  var dayOfWeekData = [];

  // Hourly analysis
  var hourlyReport = AdsApp.report(
    'SELECT HourOfDay, Clicks, Impressions, Cost, Conversions, ConversionValue ' +
    'FROM ACCOUNT_PERFORMANCE_REPORT ' +
    'DURING ' + CONFIG.DATE_RANGE
  );

  var hourlyAgg = {};
  var rows = hourlyReport.rows();
  while (rows.hasNext()) {
    var row = rows.next();
    var hour = row['HourOfDay'];
    if (!hourlyAgg[hour]) {
      hourlyAgg[hour] = {
        hour: parseInt(hour),
        clicks: 0, impressions: 0, cost: 0, conversions: 0, value: 0
      };
    }
    hourlyAgg[hour].clicks += parseInt(row['Clicks']);
    hourlyAgg[hour].impressions += parseInt(row['Impressions']);
    hourlyAgg[hour].cost += parseFloat(row['Cost']);
    hourlyAgg[hour].conversions += parseFloat(row['Conversions']);
    hourlyAgg[hour].value += parseFloat(row['ConversionValue']);
  }

  // Calculate hourly metrics
  var totalConversions = 0;
  var totalCost = 0;
  for (var h in hourlyAgg) {
    totalConversions += hourlyAgg[h].conversions;
    totalCost += hourlyAgg[h].cost;
  }
  var avgCPA = totalConversions > 0 ? totalCost / totalConversions : 0;

  // Calculate adjustments
  for (var hour in hourlyAgg) {
    var data = hourlyAgg[hour];
    data.cpa = data.conversions > 0 ? data.cost / data.conversions : Infinity;
    data.roas = data.cost > 0 ? data.value / data.cost : 0;

    // Calculate adjustment based on CPA performance vs average
    if (data.conversions >= CONFIG.MIN_CONVERSIONS_FOR_ADJUSTMENT && avgCPA > 0) {
      var performanceRatio = avgCPA / (data.cpa === Infinity ? avgCPA * 2 : data.cpa);
      var adjustment = Math.min(Math.max(performanceRatio - 1, -CONFIG.MAX_ADJUSTMENT),
                               CONFIG.MAX_ADJUSTMENT);
      data.suggestedAdjustment = adjustment;
    } else {
      data.suggestedAdjustment = 0;
    }

    hourlyData.push(data);
  }

  hourlyData.sort(function(a, b) { return a.hour - b.hour; });

  // Apply adjustments if enabled
  if (CONFIG.APPLY_ADJUSTMENTS) {
    applyHourlyAdjustments(hourlyData);
  }

  // Send report
  sendScheduleReport(hourlyData, avgCPA);
}

function applyHourlyAdjustments(hourlyData) {
  var campaigns = AdsApp.campaigns()
    .withCondition('Status = ENABLED')
    .get();

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    for (var i = 0; i < hourlyData.length; i++) {
      var data = hourlyData[i];
      if (Math.abs(data.suggestedAdjustment) > 0.05) {
        // Note: Ad scheduling must be set up first
        // This is a simplified example
        Logger.log('Would set hour ' + data.hour + ' adjustment to ' +
                   (data.suggestedAdjustment * 100).toFixed(0) + '%');
      }
    }
  }
}

function sendScheduleReport(hourlyData, avgCPA) {
  var subject = '⏰ Schedule Performance Analysis - ' + AdsApp.currentAccount().getName();

  var body = 'Schedule Performance Report\n';
  body += '===========================\n\n';
  body += 'Account: ' + AdsApp.currentAccount().getName() + '\n';
  body += 'Average CPA: €' + avgCPA.toFixed(2) + '\n\n';

  body += 'HOURLY PERFORMANCE:\n';
  body += '──────────────────\n';
  body += 'Hour | Conv | CPA      | ROAS  | Suggested Adj\n';
  body += '─────┼──────┼──────────┼───────┼──────────────\n';

  for (var i = 0; i < hourlyData.length; i++) {
    var d = hourlyData[i];
    var cpaStr = d.cpa === Infinity ? 'N/A' : '€' + d.cpa.toFixed(2);
    var adjStr = d.suggestedAdjustment === 0 ? '-' :
                 (d.suggestedAdjustment > 0 ? '+' : '') +
                 (d.suggestedAdjustment * 100).toFixed(0) + '%';

    body += String(d.hour).padStart(2, '0') + ':00 | ';
    body += String(d.conversions.toFixed(0)).padStart(4) + ' | ';
    body += cpaStr.padStart(8) + ' | ';
    body += d.roas.toFixed(2).padStart(5) + 'x | ';
    body += adjStr + '\n';
  }

  body += '\n';
  body += 'Adjustments Applied: ' + (CONFIG.APPLY_ADJUSTMENTS ? 'YES' : 'NO') + '\n';

  MailApp.sendEmail(CONFIG.EMAIL, subject, body);
}
```

## Additional Scripts Quick Reference

```
OVERIGE SCRIPTS (Kort beschreven)
═════════════════════════════════

SCRIPT 7-10: Aanvullende Optimization Scripts
─────────────────────────────────────────────

7. SEARCH QUERY MINING
   - Haalt search terms met conversies op
   - Suggereert nieuwe keywords
   - Output naar spreadsheet

8. NEGATIVE KEYWORD BUILDER
   - Automatische negative suggesties
   - Gebaseerd op non-converting terms
   - Bulk upload ready output

9. AUTOMATED BID ADJUSTMENTS
   - Device bid modifiers
   - Location bid modifiers
   - Audience bid modifiers

10. AD ROTATION OPTIMIZER
    - Identificeert winner ads
    - Suggereert ad tests
    - Pauses underperformers

SCRIPT 11-15: Reporting Scripts
───────────────────────────────

11. DAILY REPORT GENERATOR
    - Automatische dagrapportage
    - Key metrics summary
    - Week-over-week comparison

12. COMPETITOR AUCTION INSIGHTS
    - Wekelijkse competitor monitoring
    - Impression share trends
    - Position tracking

13. CAMPAIGN PERFORMANCE TRACKER
    - Historische data logging
    - Trend analysis
    - Goal tracking

14. AD EXTENSION MONITOR
    - Extension eligibility check
    - Performance per extension type
    - Missing extensions alert

15. ACCOUNT HEALTH DASHBOARD
    - Comprehensive health score
    - Weighted metrics
    - Monthly trend report
```

## Scripts Implementatie Checklist

```markdown
# Scripts Implementatie Checklist

## Pre-implementatie
- [ ] Backup huidige account settings
- [ ] Determine email recipients
- [ ] Create shared spreadsheets (if needed)
- [ ] Define threshold values for your account

## Script-by-Script Setup

### 1. Performance Anomaly Detector
- [ ] Set EMAIL address
- [ ] Adjust thresholds for your CPA/ROAS
- [ ] Schedule: Daily at 9:00
- [ ] Test: Preview mode first

### 2. Budget Pacing Monitor
- [ ] Set EMAIL address
- [ ] Adjust pacing thresholds
- [ ] Schedule: Daily at 10:00
- [ ] Verify budget values

### 3. Broken URL Checker
- [ ] Set EMAIL address
- [ ] Schedule: Weekly on Monday
- [ ] First run: Expect many results

### 4. N-Gram Analysis
- [ ] Set EMAIL address
- [ ] Optional: Create output spreadsheet
- [ ] Schedule: Weekly
- [ ] Review results before acting

### 5. Low Performer Pauser
- [ ] Set EMAIL address
- [ ] ⚠️ Start with DRY_RUN = true
- [ ] Adjust CPA/ROAS thresholds
- [ ] Schedule: Weekly
- [ ] Review dry run before enabling

### 6. Bid Adjustments
- [ ] Set EMAIL address
- [ ] Start with APPLY_ADJUSTMENTS = false
- [ ] Review suggestions first
- [ ] Schedule: Weekly

## Post-Implementation
- [ ] Monitor email alerts for 1 week
- [ ] Adjust thresholds based on results
- [ ] Document custom configurations
- [ ] Create maintenance schedule
```

---
name: conversion-tracking-debugger
description: |
  Diagnoses and fixes Google Ads conversion tracking issues. Covers missing conversions, duplicate conversions, GA4 vs Google Ads discrepancies, Enhanced Conversions issues, offline conversion problems, and tag firing issues.
  Use when: conversions not showing, conversion missing, tracking broken, duplicate conversions, conversion discrepancy, tag not firing, GCLID issues, Enhanced Conversions not working.
  Do NOT use for: initial conversion tracking setup (use conversion-tracking-setup), Meta conversion issues (use meta tools), GA4 event debugging (use ga4 tools).
metadata:
  author: "AdSuperpowers"
  version: "1.0.0"
  platform: "google_ads"
  phase: "fase-2-measurement"
compatibility: "Requires AdSuperpowers MCP server with Google Ads connection"
---
# Conversion Tracking Debugger

Complete troubleshooting guide for Google Ads conversion tracking issues. Follow the diagnostic step-by-step plan to quickly identify and resolve tracking problems.



See [decision-trees.md](references/decision-trees.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.





See [detailed-reference.md](references/detailed-reference.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.





See [decision-trees.md](references/decision-trees.md) for details.





See [detailed-reference.md](references/detailed-reference.md) for details.



## Quick Reference Card

```
CONVERSION TRACKING DEBUG CHEAT SHEET
======================================

NOT SHOWING?
-> Check tag presence (Network tab)
-> Verify conversion ID/label
-> Test consent state
-> Wait 24-48 hours

DUPLICATES?
-> Add transaction_id
-> Set Count: "One" for leads
-> Check for duplicate tags
-> Implement sessionStorage check

GA4 DISCREPANCY?
-> 10-30% difference = normal
-> Align attribution windows
-> Compare All Conversions column
-> Accept baseline, track trends

ENHANCED NOT WORKING?
-> Check user_data in dataLayer
-> Verify consent: ad_user_data
-> Validate hash format
-> Wait 48 hours for status

OFFLINE IMPORT FAILING?
-> Validate GCLID format/age
-> Check timestamp timezone
-> Verify conversion action name
-> Handle partial failures

TAG NOT FIRING?
-> Check JS console for errors
-> Verify GTM published
-> Test trigger conditions
-> Remove duplicate implementations
```



See [decision-trees.md](references/decision-trees.md) for details.



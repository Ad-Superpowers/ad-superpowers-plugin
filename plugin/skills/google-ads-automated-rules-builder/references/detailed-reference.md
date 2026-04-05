## Active Rules Overview

### Protection Rules
| Rule Name | Action | Condition | Frequency | Status |
|-----------|--------|-----------|-----------|--------|
| Budget-Cap-Pause | Pause campaign | Cost > €X | Hourly | Active |
| Zero-Conv-Pause | Pause keyword | Cost > €100, Conv = 0 | Weekly | Active |

### Optimization Rules
| Rule Name | Action | Condition | Frequency | Status |
|-----------|--------|-----------|-----------|--------|
| Bid-Increase-TopPerf | +10% bid | CPA < €X, Conv >= 5 | Weekly | Active |
| Bid-Decrease-LowPerf | -15% bid | CPA > €X | Weekly | Active |
| Budget-Scale-Winners | +15% budget | ROAS > X | Weekly | Active |

### Scheduling Rules
| Rule Name | Action | Condition | Frequency | Status |
|-----------|--------|-----------|-----------|--------|
| Weekday-Pause | Pause | Label: Weekdays-Only | Fri 22:00 | Active |
| Weekday-Enable | Enable | Label: Weekdays-Only | Mon 06:00 | Active |

### Alert Rules
| Rule Name | Alert Trigger | Frequency | Recipients |
|-----------|---------------|-----------|------------|
| CPA-Spike-Alert | CPA > €X | Daily | [emails] |
| CTR-Drop-Alert | CTR < 1% | Weekly | [emails] |
| Zero-Impr-Alert | Impr = 0 | Daily | [emails] |
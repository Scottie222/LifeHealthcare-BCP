# Life Healthcare Group – Business Continuity & Disaster Recovery Tool
## ISO 22301:2019 | Based on the Real June 2020 Ransomware Attack

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![ISO 22301](https://img.shields.io/badge/ISO-22301:2019-teal) ![POPIA](https://img.shields.io/badge/Regulation-POPIA-green) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A fully Python-based Business Continuity Planning and Disaster Recovery tool built around the **real June 2020 ransomware attack** on Life Healthcare Group — South Africa's second-largest private hospital operator. This project demonstrates hands-on BCP/DR skills including Business Impact Analysis, ISO 22301 documentation, DR runbooks and an interactive tabletop exercise simulator.

---

## The Real Incident — Life Healthcare June 2020

In **June 2020**, Life Healthcare Group — operating **66 hospitals across 7 South African provinces and Botswana** — confirmed that its southern African operation was the victim of a **targeted criminal ransomware attack**. The attack occurred during the height of the COVID-19 pandemic, making it one of the most high-profile cybersecurity incidents in South African healthcare history.

### What Was Confirmed by Life Healthcare

| System Affected | Impact | Duration |
|---|---|---|
| **Admissions Systems** | Taken completely offline | 28 days |
| **Business Processing Systems** | Taken completely offline | 28 days |
| **Email Servers** | Taken completely offline | 28 days |
| **Patient Billing** | Disrupted — manual processing only | June + part of July 2020 |
| **Medical Aid Claims** | Disrupted — delayed submissions | June + part of July 2020 |
| **Supplier Invoice Processing** | Disrupted | 28 days |
| **Financial Reporting** | Disrupted — results delayed | 28 days |
| **Patient Care (Clinical)** | **NOT IMPACTED** | N/A |

### Life Healthcare's Response

- Immediately took all affected systems offline to contain the attack
- Activated **manual backup processes** across all 66 hospitals — maintaining patient care throughout
- Engaged **external cybersecurity experts and forensic teams**
- Alerted relevant South African authorities
- **Did NOT pay the ransom** — restored from clean backups
- Substantially restored all IT systems within **28 days**

### Why This Incident Matters for BCP

- Manual fallback procedures saved patient care when digital systems failed
- Refusing to pay the ransom proved that clean backups and a tested BCP are more valuable than any ransom payment
- The 28-day recovery exposed critical gaps between RTO targets and real-world recovery capability
- POPIA Section 22 breach notification obligations were triggered for the first time at scale in South African healthcare

---

## What This Project Builds

### Command 1 — Full BCP Documentation Suite

```bash
python run_bcp.py
```

Generates **4 outputs** automatically:

- `outputs/reports/lh_bia_register.csv` — Full Business Impact Analysis register (8 processes)
- `outputs/reports/lh_bcp_dr_plan.md` — Full ISO 22301:2019 BCP/DR Plan document
- `outputs/charts/lh_bia_chart.png` — Dark-themed dual-panel BIA chart
- `outputs/charts/lh_recovery_timeline.png` — Dual-panel recovery timeline chart

### Command 2 — Interactive Tabletop Exercise

```bash
python run_bcp.py --sim
```

Launches a **fully interactive terminal-based tabletop exercise** where you play the role of CISO of Life Healthcare as the real June 2020 ransomware attack unfolds in real time.

#### The 5 Scenarios

| # | Time | Situation |
|---|---|---|
| 1 | **06:45** | SOC detects 847 files being encrypted with .LOCKED extension |
| 2 | **07:15** | $2M Bitcoin ransom demand arrives for 12 affected hospitals |
| 3 | **09:00** | TimesLIVE journalist calls the CEO directly |
| 4 | **Day 3** | Forensics suspects patient PII may have been exfiltrated |
| 5 | **Day 7** | IT proposes restoring from last night's backup |

#### Scoring

| Score | Rating |
|---|---|
| 80–100% | **PASS — BCP Competent** |
| 60–79% | **MARGINAL** |
| Below 60% | **FAIL** |

---

## Business Impact Analysis Summary

| Process | Criticality | RTO Target | Actual Downtime | Breach |
|---|---|---|---|---|
| Patient Admissions System | Critical | 4 hours | **28 days** | YES |
| Patient Billing & Claims | Critical | 8 hours | **28 days** | YES |
| Email & Communication | High | 2 hours | **28 days** | YES |
| Electronic Patient Records | Critical | 1 hour | 0 days | NO — protected |
| Supplier Invoice Processing | Medium | 48 hours | **28 days** | YES |
| Financial Reporting | Medium | 72 hours | **28 days** | YES |
| ICU & Theatre Management | Critical | 0 hours | 0 days | NO — protected |
| HR & Payroll Systems | Medium | 48 hours | **14 days** | PARTIAL |

---

## Project Structure
LifeHealthcare-BCP/
│
├── data/
│   └── bcp_data.py
├── scripts/
│   ├── bia_analysis.py
│   ├── generate_bcp.py
│   └── tabletop_simulator.py
├── outputs/
│   ├── reports/
│   │   ├── lh_bia_register.csv
│   │   ├── lh_bcp_dr_plan.md
│   │   └── lh_tabletop_exercise_report.md
│   └── charts/
│       ├── lh_bia_chart.png
│       └── lh_recovery_timeline.png
├── run_bcp.py
├── requirements.txt
├── .gitignore
└── README.md

---

## How to Run

```bash
git clone https://github.com/Scottie222/LifeHealthcare-BCP.git
cd LifeHealthcare-BCP
pip install -r requirements.txt
python run_bcp.py
python run_bcp.py --sim
```

---

## ISO 22301:2019 Alignment

| ISO 22301 Clause | Requirement | How This Project Addresses It |
|---|---|---|
| **4.1** | Understanding the organisation | Company profile and incident context in `bcp_data.py` |
| **6.1** | Business Impact Analysis | Full BIA register with RTO, RPO and MTPD per process |
| **8.3** | Business continuity strategy | Manual fallback procedures — confirmed effective June 2020 |
| **8.4** | Business continuity plans | Full ISO 22301-aligned BCP/DR Plan document |
| **8.5** | Exercise and testing | Interactive tabletop simulator with scoring and reporting |
| **9.1** | Monitoring and measurement | Recovery timeline analysis and RTO breach analysis |
| **10.1** | Nonconformity and improvement | Lessons learned section from real incident |

---

## Key Lessons from the Real Incident

1. **Do not pay the ransom** — Life Healthcare restored from backups without paying.
2. **Manual fallback procedures saved patient care** — 66 hospitals operated on paper for 28 days.
3. **Your RTO targets are probably wrong** — A 4-hour RTO became 28 days of actual downtime.
4. **Restore from before the compromise date** — Ransomware can be dormant for weeks.
5. **Engage external forensics immediately** — Do not attempt internal investigation.
6. **POPIA Section 22 is triggered early** — Notify on reasonable grounds, not confirmed proof.
7. **Pre-approved crisis communications are essential** — Consistent messaging protects reputation.

---

## References

1. ITWeb: https://www.itweb.co.za/article/life-healthcare-reveals-damage-caused-by-data-breach/rW1xLv59YPGvRk6m
2. TimesLIVE: https://www.timeslive.co.za/news/south-africa/2020-06-09-hackers-strike-at-life-healthcare-extent-of-data-breach-yet-to-be-assessed/
3. ISO 22301:2019 — Business Continuity Management Systems
4. POPIA Act 4 of 2013: https://www.justice.gov.za/inforeg
5. Information Regulator South Africa: https://inforegulator.org.za

---

## Related GRC Portfolio Projects

| Project | Description |
|---|---|
| [StandardBank-Risk-Assessment](https://github.com/Scottie222/StandardBank-Risk-Assessment) | ISO 27001 Risk Assessment — Experian SA breach 2020 |
| [MTN-ISMS-Audit](https://github.com/Scottie222/MTN-ISMS-Audit) | Internal Audit Tool — MTN SA breach April 2025 |
| [OpenVantage-ISMS](https://github.com/Scottie222/OpenVantage-ISMS) | Full ISO 27001:2022 ISMS Documentation Suite |
| [POPIA-GDPR-Compliance-Tracker](https://github.com/Scottie222/POPIA-GDPR-Compliance-Tracker) | Automated POPIA/GDPR compliance scoring |
| [GRC-Controls-Lab](https://github.com/Scottie222/GRC-Controls-Lab) | ISO 27001 & NIST CSF control implementation lab |

---

*Built by Bakithi Scott Ngcampalala | Junior Security Administrator @ Open Vantage*  
*LinkedIn: https://www.linkedin.com/in/bakithi-scott-ngcampalala-0051a4105*
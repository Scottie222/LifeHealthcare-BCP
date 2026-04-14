
# Life Healthcare Group — Business Continuity & Disaster Recovery Plan

**Standard:** ISO 22301:2019 Business Continuity Management Systems

**Version:** 1.0 | **Date:** 14 April 2026

**Classification:** CONFIDENTIAL — INTERNAL USE ONLY

**Scope:** All 66 hospitals across 7 South African provinces and Botswana

---


## 1. Executive Summary

This Business Continuity and Disaster Recovery Plan has been developed for Life Healthcare Group in direct response to the confirmed **Ransomware Attack** of **June 2020**, which impacted the company's southern African IT infrastructure across 66 hospitals.

**Key incident metrics from the real June 2020 attack:**

| Metric | Value |
| --- | --- |
| Incident Type | Targeted Ransomware Attack |
| Hospitals Affected | 12 of 66 |
| Ransom Demanded | $2 Million USD (Bitcoin) |
| Ransom Paid | NO — restored from clean backups |
| Systems Offline | Admissions, Billing, Email, Supplier Invoicing, Financial Reporting |
| Patient Care Impact | NONE — manual fallback procedures activated |
| Total Recovery Duration | 28 days |
| Post-Incident Review Completed | Day 35 |


## 2. BCP Scope and Context

**Organisation:** Life Healthcare Group

**Sector:** Private Healthcare

**Operations:** 66 hospitals across South Africa, Botswana

**Applicable Regulations:**

- POPIA Act 4 of 2013

- Health Professions Act

- NHI Act

- Companies Act 71/2008

- PASA




## 3. Business Continuity Objectives

| Objective | Description |
| --- | --- |
| Protect Patient Safety | Maintain uninterrupted clinical care across all hospitals at all times |
| Preserve Data Integrity | Ensure patient records are protected and recoverable |
| Minimise Downtime | Reduce recovery time versus the 28-day actual downtime of June 2020 |
| Regulatory Compliance | Meet POPIA Section 22 notification obligations within required timeframes |
| Reputation Protection | Maintain public and investor confidence through crisis communications |
| Financial Continuity | Preserve billing and financial reporting capability |


## 4. Business Impact Analysis Summary

| ID | Process | Criticality | RTO Target | Actual Downtime (Jun 2020) | RTO Breached |
| --- | --- | --- | --- | --- | --- |
| P-001 | Patient Admissions System | Critical | 4h | 28 days | YES |
| P-002 | Patient Billing & Claims | Critical | 8h | 28 days | YES |
| P-003 | Email & Communication | High | 2h | 28 days | YES |
| P-004 | Electronic Patient Records | Critical | 1h | 0 (Not impacted) | NO |
| P-005 | Supplier Invoice Processing | Medium | 48h | 28 days | YES |
| P-006 | Financial Reporting | Medium | 72h | 28 days | YES |
| P-007 | ICU & Theatre Management | Critical | 0h | 0 (Not impacted) | NO |
| P-008 | HR & Payroll Systems | Medium | 48h | 14 days | YES |

**Key finding:** Every RTO target was breached during the real attack. The Admissions System had a 4-hour RTO but was offline for **672 hours (28 days)**.


## 5. Threat Scenarios


### Scenario S-001 — Ransomware Attack

**Likelihood:** HIGH | **Impact:** CRITICAL

Targeted ransomware encrypting core IT systems — the confirmed June 2020 scenario

*Real-world example: Life Healthcare June 2020 — $2M Bitcoin ransom demand*


### Scenario S-002 — Extended Power Failure

**Likelihood:** HIGH | **Impact:** HIGH

Load shedding Stage 6+ causing extended UPS failure across hospital campuses

*Real-world example: South Africa Eskom grid instability 2022-2024*


### Scenario S-003 — Pandemic / Mass Casualty Event

**Likelihood:** MEDIUM | **Impact:** CRITICAL

COVID-19 style surge overwhelming hospital capacity and IT demand simultaneously

*Real-world example: COVID-19 March 2020 — occurred simultaneously with the ransomware attack*


### Scenario S-004 — Data Centre Fire / Physical Disaster

**Likelihood:** LOW | **Impact:** CRITICAL

Primary data centre destruction requiring full DR site activation

*Real-world example: OVHcloud Strasbourg fire March 2021*


## 6. Manual Fallback Procedures

| Process | Manual Fallback | Status |
| --- | --- | --- |
| Patient Admissions System | Available | Confirmed effective Jun 2020 |
| Patient Billing & Claims | Available | Confirmed effective Jun 2020 |
| Email & Communication | Available | Confirmed effective Jun 2020 |
| Electronic Patient Records | Available | Not tested — not impacted |
| Supplier Invoice Processing | Available | Confirmed effective Jun 2020 |
| Financial Reporting | Not Available | Not tested — not impacted |
| ICU & Theatre Management | Available | Not tested — not impacted |
| HR & Payroll Systems | Available | Confirmed effective Jun 2020 |


## 7. DR Runbook — Ransomware Response (10 Steps)

| Step | Phase | Action | Time Target |
| --- | --- | --- | --- |
| 1 | Detect & Declare | SOC detects anomaly — escalate immediately to CISO and IT Director | 0–30 minutes |
| 2 | Declare BCP Event | CISO declares BCP event — activate Crisis Management Team across all regions | 30–60 minutes |
| 3 | Isolate Affected Systems | Network disconnect all affected systems — prevent lateral movement | 1–2 hours |
| 4 | Activate Manual Fallback | Deploy manual fallback procedures to all 66 hospitals — paper-based admissions and records | 2–4 hours |
| 5 | Engage External Forensics | Engage pre-contracted cybersecurity forensics firm — preserve all evidence | 4–8 hours |
| 6 | Determine Compromise Scope | Full forensic assessment — identify all affected systems and potential data exfiltration | 24–48 hours |
| 7 | Notify Authorities | Notify SA Police, SAPS Cybercrime Unit, Information Regulator (POPIA Section 22) | 48–72 hours |
| 8 | Establish Clean Environment | Build isolated clean recovery environment — verify backup integrity pre-compromise date | Day 5–7 |
| 9 | Phased System Restoration | Restore clinical systems first, then admin, then billing — verify each before proceeding | Day 7–21 |
| 10 | Full Normalisation | Full system restoration complete — conduct post-incident review and update BCP | Day 28–35 |


## 8. POPIA Section 22 — Breach Notification Obligations

Under **POPIA Act 4 of 2013**, Section 22 requires notification to the **Information Regulator** as soon as there are **reasonable grounds** to believe personal information was accessed by an unauthorised person.

Notification is **NOT** contingent on confirmed proof — reasonable grounds is the trigger.

**Action items:**

1. Legal team to assess breach scope on Day 1–3

2. Submit Section 22 notification if reasonable grounds exist

3. Prepare patient communications template

4. Document all notification actions for regulatory evidence


## 9. Lessons Learned — June 2020 Real Incident

1. Do not pay the ransom — Life Healthcare restored from backups without paying.

2. Manual fallback procedures saved patient care — 66 hospitals ran on paper for 28 days.

3. Your RTO targets are probably wrong — a 4-hour RTO became 28 days of actual downtime.

4. Restore from before the compromise date — recent backups may contain the attacker's foothold.

5. Engage external forensics immediately — do not attempt internal investigation.

6. POPIA Section 22 is triggered early — notify on reasonable grounds, not confirmed proof.

7. Pre-approved crisis communications are essential — Life Healthcare's messaging protected reputation.


## 10. BCP Testing Schedule

| Test Type | Frequency | Participants | Output |
| --- | --- | --- | --- |
| Tabletop Exercise | Annually | CISO, Crisis Team, Department Heads | Scored exercise report |
| IT DR Test | Bi-annually | IT, Security, Operations | Recovery time vs RTO |
| Manual Fallback Drill | Annually | Hospital Operations, Nursing, Admin | Drill completion report |
| Full BCP Review | Annually | All BCP owners | Updated BCP document |
| POPIA Compliance Review | Annually | Legal, CISO, Information Officer | Compliance gap register |


## 11. References

1. ITWeb — Life Healthcare breach: https://www.itweb.co.za/article/life-healthcare-reveals-damage-caused-by-data-breach/rW1xLv59YPGvRk6m

2. TimesLIVE — Hackers strike Life Healthcare: https://www.timeslive.co.za/news/south-africa/2020-06-09-hackers-strike-at-life-healthcare-extent-of-data-breach-yet-to-be-assessed/

3. ISO 22301:2019 — Business Continuity Management Systems

4. POPIA Act 4 of 2013: https://www.justice.gov.za/inforeg

5. Information Regulator South Africa: https://inforegulator.org.za


---

*Generated: 14 April 2026 | ISO 22301:2019 | POPIA Compliant*

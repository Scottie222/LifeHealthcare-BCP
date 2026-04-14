import os
import sys
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.bcp_data import COMPANY, BIA, SCENARIOS, DR_RUNBOOK, LESSONS_LEARNED


def generate_bcp_plan(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    today = date.today().strftime("%d %B %Y")
    lines = []

    def h(level, text):
        lines.append(f"\n{'#' * level} {text}\n")

    def p(text=""):
        lines.append(text + "\n")

    def table(headers, rows):
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
        for row in rows:
            lines.append("| " + " | ".join(str(c) for c in row) + " |")
        lines.append("")

    h(1, f"{COMPANY['name']} — Business Continuity & Disaster Recovery Plan")
    p(f"**Standard:** ISO 22301:2019 Business Continuity Management Systems")
    p(f"**Version:** 1.0 | **Date:** {today}")
    p(f"**Classification:** CONFIDENTIAL — INTERNAL USE ONLY")
    p(f"**Scope:** All {COMPANY['hospitals']} hospitals across {COMPANY['provinces']} South African provinces and Botswana")
    p("---")

    h(2, "1. Executive Summary")
    p(f"This Business Continuity and Disaster Recovery Plan has been developed for {COMPANY['name']} "
      f"in direct response to the confirmed **{COMPANY['incident_type']}** of **{COMPANY['incident_date']}**, "
      f"which impacted the company's southern African IT infrastructure across {COMPANY['hospitals']} hospitals.")
    p("**Key incident metrics from the real June 2020 attack:**")
    table(
        ["Metric", "Value"],
        [
            ["Incident Type", "Targeted Ransomware Attack"],
            ["Hospitals Affected", "12 of 66"],
            ["Ransom Demanded", "$2 Million USD (Bitcoin)"],
            ["Ransom Paid", "NO — restored from clean backups"],
            ["Systems Offline", "Admissions, Billing, Email, Supplier Invoicing, Financial Reporting"],
            ["Patient Care Impact", "NONE — manual fallback procedures activated"],
            ["Total Recovery Duration", "28 days"],
            ["Post-Incident Review Completed", "Day 35"],
        ]
    )

    h(2, "2. BCP Scope and Context")
    p(f"**Organisation:** {COMPANY['name']}")
    p(f"**Sector:** {COMPANY['sector']}")
    p(f"**Operations:** {COMPANY['hospitals']} hospitals across {', '.join(COMPANY['regions'])}")
    p("**Applicable Regulations:**")
    for reg in COMPANY['regulation']:
        p(f"- {reg}")
    p("")

    h(2, "3. Business Continuity Objectives")
    table(
        ["Objective", "Description"],
        [
            ["Protect Patient Safety", "Maintain uninterrupted clinical care across all hospitals at all times"],
            ["Preserve Data Integrity", "Ensure patient records are protected and recoverable"],
            ["Minimise Downtime", "Reduce recovery time versus the 28-day actual downtime of June 2020"],
            ["Regulatory Compliance", "Meet POPIA Section 22 notification obligations within required timeframes"],
            ["Reputation Protection", "Maintain public and investor confidence through crisis communications"],
            ["Financial Continuity", "Preserve billing and financial reporting capability"],
        ]
    )

    h(2, "4. Business Impact Analysis Summary")
    bia_rows = []
    for p_ in BIA:
        actual = f"{p_['actual_downtime_days']} days" if p_['actual_downtime_days'] > 0 else "0 (Not impacted)"
        breach = "YES" if p_['impacted_june_2020'] and p_['actual_downtime_days'] > 0 else ("PARTIAL" if p_['impacted_june_2020'] else "NO")
        bia_rows.append([p_['process_id'], p_['process_name'], p_['criticality'], f"{p_['rto_hours']}h", actual, breach])
    table(["ID", "Process", "Criticality", "RTO Target", "Actual Downtime (Jun 2020)", "RTO Breached"], bia_rows)
    p("**Key finding:** Every RTO target was breached during the real attack. "
      "The Admissions System had a 4-hour RTO but was offline for **672 hours (28 days)**.")

    h(2, "5. Threat Scenarios")
    for s in SCENARIOS:
        h(3, f"Scenario {s['id']} — {s['name']}")
        p(f"**Likelihood:** {s['likelihood']} | **Impact:** {s['impact']}")
        p(s['description'])
        p(f"*Real-world example: {s['real_world_example']}*")

    h(2, "6. Manual Fallback Procedures")
    fallback_rows = []
    for p_ in BIA:
        fallback_rows.append([
            p_['process_name'],
            "Available" if p_['manual_fallback'] else "Not Available",
            "Confirmed effective Jun 2020" if p_['impacted_june_2020'] and p_['manual_fallback'] else "Not tested — not impacted"
        ])
    table(["Process", "Manual Fallback", "Status"], fallback_rows)

    h(2, "7. DR Runbook — Ransomware Response (10 Steps)")
    table(["Step", "Phase", "Action", "Time Target"],
          [[r['step'], r['phase'], r['action'], r['time_target']] for r in DR_RUNBOOK])

    h(2, "8. POPIA Section 22 — Breach Notification Obligations")
    p("Under **POPIA Act 4 of 2013**, Section 22 requires notification to the **Information Regulator** "
      "as soon as there are **reasonable grounds** to believe personal information was accessed by an unauthorised person.")
    p("Notification is **NOT** contingent on confirmed proof — reasonable grounds is the trigger.")
    p("**Action items:**")
    p("1. Legal team to assess breach scope on Day 1–3")
    p("2. Submit Section 22 notification if reasonable grounds exist")
    p("3. Prepare patient communications template")
    p("4. Document all notification actions for regulatory evidence")

    h(2, "9. Lessons Learned — June 2020 Real Incident")
    for i, lesson in enumerate(LESSONS_LEARNED, 1):
        p(f"{i}. {lesson}")

    h(2, "10. BCP Testing Schedule")
    table(
        ["Test Type", "Frequency", "Participants", "Output"],
        [
            ["Tabletop Exercise", "Annually", "CISO, Crisis Team, Department Heads", "Scored exercise report"],
            ["IT DR Test", "Bi-annually", "IT, Security, Operations", "Recovery time vs RTO"],
            ["Manual Fallback Drill", "Annually", "Hospital Operations, Nursing, Admin", "Drill completion report"],
            ["Full BCP Review", "Annually", "All BCP owners", "Updated BCP document"],
            ["POPIA Compliance Review", "Annually", "Legal, CISO, Information Officer", "Compliance gap register"],
        ]
    )

    h(2, "11. References")
    refs = [
        "ITWeb — Life Healthcare breach: https://www.itweb.co.za/article/life-healthcare-reveals-damage-caused-by-data-breach/rW1xLv59YPGvRk6m",
        "TimesLIVE — Hackers strike Life Healthcare: https://www.timeslive.co.za/news/south-africa/2020-06-09-hackers-strike-at-life-healthcare-extent-of-data-breach-yet-to-be-assessed/",
        "ISO 22301:2019 — Business Continuity Management Systems",
        "POPIA Act 4 of 2013: https://www.justice.gov.za/inforeg",
        "Information Regulator South Africa: https://inforegulator.org.za",
    ]
    for i, ref in enumerate(refs, 1):
        p(f"{i}. {ref}")

    p("\n---")
    p(f"*Generated: {today} | ISO 22301:2019 | POPIA Compliant*")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"  [+] BCP/DR Plan saved: {output_path}")


if __name__ == "__main__":
    base = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    generate_bcp_plan(os.path.join(base, 'reports', 'lh_bcp_dr_plan.md'))
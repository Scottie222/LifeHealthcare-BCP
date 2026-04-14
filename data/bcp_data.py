# ============================================================
# Life Healthcare BCP — Master Data File
# ============================================================

COMPANY = {
    "name": "Life Healthcare Group",
    "sector": "Private Healthcare",
    "country": "South Africa",
    "hospitals": 66,
    "provinces": 7,
    "regions": ["South Africa", "Botswana"],
    "incident_date": "June 2020",
    "incident_type": "Ransomware Attack",
    "recovery_days": 28,
    "ransom_paid": False,
    "ceo_acting": "Pieter van der Westhuizen",
    "stock_exchange": "JSE",
    "regulation": ["POPIA Act 4 of 2013", "Health Professions Act", "NHI Act", "Companies Act 71/2008", "PASA"],
}

BIA = [
    {"process_id": "P-001", "process_name": "Patient Admissions System", "department": "Hospital Operations", "criticality": "Critical", "rto_hours": 4, "rpo_hours": 1, "mtpd_hours": 24, "financial_impact_per_day": 850000, "patient_safety_impact": "HIGH — admission delays affect emergency throughput", "manual_fallback": True, "impacted_june_2020": True, "actual_downtime_days": 28},
    {"process_id": "P-002", "process_name": "Patient Billing & Claims", "department": "Finance", "criticality": "Critical", "rto_hours": 8, "rpo_hours": 4, "mtpd_hours": 48, "financial_impact_per_day": 1200000, "patient_safety_impact": "MEDIUM — delayed billing, no direct patient harm", "manual_fallback": True, "impacted_june_2020": True, "actual_downtime_days": 28},
    {"process_id": "P-003", "process_name": "Email & Communication", "department": "IT / All Departments", "criticality": "High", "rto_hours": 2, "rpo_hours": 1, "mtpd_hours": 8, "financial_impact_per_day": 150000, "patient_safety_impact": "MEDIUM — affects internal coordination", "manual_fallback": True, "impacted_june_2020": True, "actual_downtime_days": 28},
    {"process_id": "P-004", "process_name": "Electronic Patient Records", "department": "Clinical / IT", "criticality": "Critical", "rto_hours": 1, "rpo_hours": 0, "mtpd_hours": 4, "financial_impact_per_day": 2000000, "patient_safety_impact": "CRITICAL — loss of records endangers patient safety", "manual_fallback": True, "impacted_june_2020": False, "actual_downtime_days": 0},
    {"process_id": "P-005", "process_name": "Supplier Invoice Processing", "department": "Procurement", "criticality": "Medium", "rto_hours": 48, "rpo_hours": 24, "mtpd_hours": 120, "financial_impact_per_day": 300000, "patient_safety_impact": "LOW — supply chain risk if prolonged", "manual_fallback": True, "impacted_june_2020": True, "actual_downtime_days": 28},
    {"process_id": "P-006", "process_name": "Financial Reporting", "department": "Finance", "criticality": "Medium", "rto_hours": 72, "rpo_hours": 24, "mtpd_hours": 168, "financial_impact_per_day": 500000, "patient_safety_impact": "LOW — regulatory/investor risk", "manual_fallback": False, "impacted_june_2020": True, "actual_downtime_days": 28},
    {"process_id": "P-007", "process_name": "ICU & Theatre Management", "department": "Clinical", "criticality": "Critical", "rto_hours": 0, "rpo_hours": 0, "mtpd_hours": 0, "financial_impact_per_day": 5000000, "patient_safety_impact": "CRITICAL — direct patient life risk", "manual_fallback": True, "impacted_june_2020": False, "actual_downtime_days": 0},
    {"process_id": "P-008", "process_name": "HR & Payroll Systems", "department": "Human Resources", "criticality": "Medium", "rto_hours": 48, "rpo_hours": 24, "mtpd_hours": 120, "financial_impact_per_day": 200000, "patient_safety_impact": "LOW — staff payment delays", "manual_fallback": True, "impacted_june_2020": True, "actual_downtime_days": 14},
]

SCENARIOS = [
    {"id": "S-001", "name": "Ransomware Attack", "description": "Targeted ransomware encrypting core IT systems — the confirmed June 2020 scenario", "likelihood": "HIGH", "impact": "CRITICAL", "real_world_example": "Life Healthcare June 2020 — $2M Bitcoin ransom demand"},
    {"id": "S-002", "name": "Extended Power Failure", "description": "Load shedding Stage 6+ causing extended UPS failure across hospital campuses", "likelihood": "HIGH", "impact": "HIGH", "real_world_example": "South Africa Eskom grid instability 2022-2024"},
    {"id": "S-003", "name": "Pandemic / Mass Casualty Event", "description": "COVID-19 style surge overwhelming hospital capacity and IT demand simultaneously", "likelihood": "MEDIUM", "impact": "CRITICAL", "real_world_example": "COVID-19 March 2020 — occurred simultaneously with the ransomware attack"},
    {"id": "S-004", "name": "Data Centre Fire / Physical Disaster", "description": "Primary data centre destruction requiring full DR site activation", "likelihood": "LOW", "impact": "CRITICAL", "real_world_example": "OVHcloud Strasbourg fire March 2021"},
]

RECOVERY_TIMELINE = [
    {"day": 0,  "event": "Attack detected — ransomware encrypting Johannesburg servers",        "status": "INCIDENT",  "systems_online_pct": 0},
    {"day": 0,  "event": "All affected systems taken offline — containment activated",           "status": "CONTAIN",   "systems_online_pct": 0},
    {"day": 1,  "event": "Manual fallback activated across all 66 hospitals",                    "status": "FALLBACK",  "systems_online_pct": 5},
    {"day": 1,  "event": "External cybersecurity forensics team engaged",                        "status": "FORENSICS", "systems_online_pct": 5},
    {"day": 2,  "event": "South African authorities alerted",                                    "status": "NOTIFY",    "systems_online_pct": 5},
    {"day": 3,  "event": "Full scope of compromise determined — 12 hospitals affected",          "status": "ASSESS",    "systems_online_pct": 8},
    {"day": 5,  "event": "Clean recovery environment established",                               "status": "RECOVER",   "systems_online_pct": 15},
    {"day": 7,  "event": "Clinical systems (ICU, Theatre) confirmed unaffected — fully online",  "status": "RECOVER",   "systems_online_pct": 30},
    {"day": 10, "event": "Email servers partially restored",                                     "status": "RECOVER",   "systems_online_pct": 45},
    {"day": 14, "event": "HR & Payroll systems restored",                                        "status": "RECOVER",   "systems_online_pct": 60},
    {"day": 21, "event": "Admissions system phased restoration begins",                         "status": "RECOVER",   "systems_online_pct": 75},
    {"day": 25, "event": "Billing and claims systems restored",                                  "status": "RECOVER",   "systems_online_pct": 88},
    {"day": 28, "event": "All core systems substantially restored — no ransom paid",             "status": "RESTORED",  "systems_online_pct": 95},
    {"day": 35, "event": "Post-incident review complete — lessons learned documented",           "status": "COMPLETE",  "systems_online_pct": 100},
]

DR_RUNBOOK = [
    {"step": 1,  "phase": "Detect & Declare",           "action": "SOC detects anomaly — escalate immediately to CISO and IT Director",                         "time_target": "0–30 minutes"},
    {"step": 2,  "phase": "Declare BCP Event",          "action": "CISO declares BCP event — activate Crisis Management Team across all regions",               "time_target": "30–60 minutes"},
    {"step": 3,  "phase": "Isolate Affected Systems",   "action": "Network disconnect all affected systems — prevent lateral movement",                         "time_target": "1–2 hours"},
    {"step": 4,  "phase": "Activate Manual Fallback",   "action": "Deploy manual fallback procedures to all 66 hospitals — paper-based admissions and records",  "time_target": "2–4 hours"},
    {"step": 5,  "phase": "Engage External Forensics",  "action": "Engage pre-contracted cybersecurity forensics firm — preserve all evidence",                 "time_target": "4–8 hours"},
    {"step": 6,  "phase": "Determine Compromise Scope", "action": "Full forensic assessment — identify all affected systems and potential data exfiltration",    "time_target": "24–48 hours"},
    {"step": 7,  "phase": "Notify Authorities",         "action": "Notify SA Police, SAPS Cybercrime Unit, Information Regulator (POPIA Section 22)",           "time_target": "48–72 hours"},
    {"step": 8,  "phase": "Establish Clean Environment","action": "Build isolated clean recovery environment — verify backup integrity pre-compromise date",     "time_target": "Day 5–7"},
    {"step": 9,  "phase": "Phased System Restoration",  "action": "Restore clinical systems first, then admin, then billing — verify each before proceeding",   "time_target": "Day 7–21"},
    {"step": 10, "phase": "Full Normalisation",         "action": "Full system restoration complete — conduct post-incident review and update BCP",             "time_target": "Day 28–35"},
]

TABLETOP_SCENARIOS = [
    {
        "id": "T-001", "time": "06:45", "title": "Initial Detection",
        "situation": "Your SOC analyst calls you directly. 847 files on the Johannesburg Central Hospital server farm have been encrypted with a .LOCKED extension in the last 4 minutes. The encryption is spreading. You are the CISO. What is your immediate action?",
        "options": {"A": "Wait for more information before acting — could be a false positive", "B": "Immediately isolate affected network segments and escalate to Crisis Team", "C": "Contact the ransom negotiator first to understand the attacker's demands", "D": "Notify the media proactively before the story breaks"},
        "correct": "B", "points": 20,
        "explanation": "ISO 22301 and Life Healthcare's real response: immediate isolation to contain spread. Every minute of delay allows ransomware to encrypt more systems. Life Healthcare took all affected systems offline immediately on Day 0.",
    },
    {
        "id": "T-002", "time": "07:15", "title": "Ransom Demand",
        "situation": "Ransomware confirmed across 12 hospitals. A $2 million Bitcoin ransom demand has arrived. The attackers claim to have exfiltrated patient data and threaten to publish it. The CFO is asking whether to pay. What do you recommend?",
        "options": {"A": "Pay the ransom immediately — patient data exposure is too risky", "B": "Negotiate the ransom down to $500K and pay", "C": "Do NOT pay — activate BCP, restore from clean backups, engage forensics", "D": "Pay only if the attackers can prove they will delete the exfiltrated data"},
        "correct": "C", "points": 20,
        "explanation": "Life Healthcare did NOT pay the ransom. Paying funds criminal activity, does not guarantee decryption or data deletion, and may violate sanctions law. Clean backups and a tested BCP are worth more than any ransom payment.",
    },
    {
        "id": "T-003", "time": "09:00", "title": "Media Crisis",
        "situation": "A TimesLIVE journalist calls the CEO directly asking: 'Can you confirm that patient data has been compromised in today's cyberattack?' The CEO looks to you for guidance. What should the response be?",
        "options": {"A": "Deny everything — no comment until the full picture is known", "B": "Confirm the attack, state that patient care is unaffected, investigation is underway", "C": "Give the journalist a full technical briefing to show transparency", "D": "Ignore the call — media engagement is not a priority during an incident"},
        "correct": "B", "points": 20,
        "explanation": "Life Healthcare issued a measured, factual statement confirming the attack while emphasising that patient care was unaffected. Denying a confirmed incident destroys trust. Pre-approved crisis communications templates are a BCP requirement.",
    },
    {
        "id": "T-004", "time": "Day 3", "title": "POPIA Notification",
        "situation": "Forensics suspects that patient PII on the billing server may have been exfiltrated before the ransomware was triggered. You cannot yet confirm the full scope. Your legal team asks: when must you notify the Information Regulator under POPIA?",
        "options": {"A": "Only notify once you have full confirmation of what data was taken", "B": "You do not need to notify unless patients complain", "C": "Notify the Information Regulator as soon as there are reasonable grounds to believe a breach occurred", "D": "Wait 90 days to assess financial impact before notifying"},
        "correct": "C", "points": 20,
        "explanation": "POPIA Section 22 requires notification to the Information Regulator as soon as there are reasonable grounds to believe that personal information has been accessed or acquired by an unauthorised person. You do NOT need full confirmation — reasonable grounds is the trigger.",
    },
    {
        "id": "T-005", "time": "Day 7", "title": "Recovery Strategy",
        "situation": "Your IT team proposes restoring systems from last night's backup — it is clean and fast. Your forensics team warns that ransomware can be dormant for 14–90 days before triggering. Restoring from last night means you may restore the attacker's foothold. What do you do?",
        "options": {"A": "Restore from last night's backup — speed is the priority", "B": "Restore from a backup taken before the suspected compromise date — verified clean", "C": "Rebuild all systems from scratch — do not use any backups", "D": "Ask the attackers for the decryption key in exchange for partial payment"},
        "correct": "B", "points": 20,
        "explanation": "Restoring from a recent but potentially compromised backup reintroduces the attacker. The correct approach is to identify the likely compromise date from forensics and restore from a backup taken before that date — even if it means more data loss.",
    },
]

LESSONS_LEARNED = [
    "Do not pay the ransom — Life Healthcare restored from backups without paying.",
    "Manual fallback procedures saved patient care — 66 hospitals ran on paper for 28 days.",
    "Your RTO targets are probably wrong — a 4-hour RTO became 28 days of actual downtime.",
    "Restore from before the compromise date — recent backups may contain the attacker's foothold.",
    "Engage external forensics immediately — do not attempt internal investigation.",
    "POPIA Section 22 is triggered early — notify on reasonable grounds, not confirmed proof.",
    "Pre-approved crisis communications are essential — Life Healthcare's messaging protected reputation.",
]
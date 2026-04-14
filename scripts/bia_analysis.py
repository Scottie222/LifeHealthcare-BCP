import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from data.bcp_data import BIA, COMPANY, RECOVERY_TIMELINE


def generate_bia_csv(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fieldnames = [
        "Process ID", "Process Name", "Department", "Criticality",
        "RTO (hours)", "RPO (hours)", "MTPD (hours)",
        "Financial Impact/Day (ZAR)", "Patient Safety Impact",
        "Manual Fallback Available", "Impacted June 2020", "Actual Downtime (days)"
    ]
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in BIA:
            writer.writerow({
                "Process ID": p["process_id"],
                "Process Name": p["process_name"],
                "Department": p["department"],
                "Criticality": p["criticality"],
                "RTO (hours)": p["rto_hours"],
                "RPO (hours)": p["rpo_hours"],
                "MTPD (hours)": p["mtpd_hours"],
                "Financial Impact/Day (ZAR)": f"R {p['financial_impact_per_day']:,}",
                "Patient Safety Impact": p["patient_safety_impact"],
                "Manual Fallback Available": "Yes" if p["manual_fallback"] else "No",
                "Impacted June 2020": "YES" if p["impacted_june_2020"] else "NO",
                "Actual Downtime (days)": p["actual_downtime_days"],
            })
    print(f"  [+] BIA CSV saved: {output_path}")


def generate_bia_chart(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    fig.patch.set_facecolor('#0d1117')

    ax1.set_facecolor('#161b22')
    names = [p["process_name"].replace(" & ", "\n& ").replace(" / ", "\n/ ") for p in BIA]
    rto_hours = [p["rto_hours"] for p in BIA]
    actual_hours = [p["actual_downtime_days"] * 24 for p in BIA]

    x = np.arange(len(names))
    width = 0.35

    ax1.bar(x - width/2, rto_hours, width, label='RTO Target (hours)', color='#238636', alpha=0.9, edgecolor='#2ea043')
    ax1.bar(x + width/2, actual_hours, width, label='Actual Downtime (hours)', color='#da3633', alpha=0.9, edgecolor='#f85149')

    ax1.set_xlabel('Business Process', color='#8b949e', fontsize=10, labelpad=10)
    ax1.set_ylabel('Hours', color='#8b949e', fontsize=10)
    ax1.set_title('RTO Target vs Actual Downtime\nJune 2020 Ransomware Attack', color='#f0f6fc', fontsize=13, fontweight='bold', pad=15)
    ax1.set_xticks(x)
    ax1.set_xticklabels(names, rotation=35, ha='right', fontsize=7.5, color='#c9d1d9')
    ax1.tick_params(colors='#8b949e')
    ax1.spines['bottom'].set_color('#30363d')
    ax1.spines['left'].set_color('#30363d')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.legend(facecolor='#161b22', edgecolor='#30363d', labelcolor='#c9d1d9', fontsize=9)
    ax1.yaxis.grid(True, color='#21262d', linestyle='--', alpha=0.5)
    ax1.set_axisbelow(True)

    for i, (rto, actual) in enumerate(zip(rto_hours, actual_hours)):
        if actual > rto and actual > 0:
            ax1.annotate('BREACHED', xy=(i + width/2, actual), xytext=(0, 5),
                        textcoords='offset points', ha='center', fontsize=6.5, color='#f85149', fontweight='bold')

    ax2.set_facecolor('#161b22')
    criticality_counts = {}
    for p in BIA:
        criticality_counts[p["criticality"]] = criticality_counts.get(p["criticality"], 0) + 1

    colors_map = {'Critical': '#da3633', 'High': '#e3b341', 'Medium': '#238636'}
    labels = list(criticality_counts.keys())
    sizes = list(criticality_counts.values())
    colors = [colors_map.get(l, '#58a6ff') for l in labels]

    wedges, texts, autotexts = ax2.pie(
        sizes, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90, pctdistance=0.75,
        wedgeprops=dict(width=0.5, edgecolor='#0d1117', linewidth=2),
        textprops=dict(color='#c9d1d9', fontsize=11)
    )
    for at in autotexts:
        at.set_color('#f0f6fc')
        at.set_fontsize(12)
        at.set_fontweight('bold')

    ax2.set_title('Process Criticality Distribution\n8 Critical Hospital Processes', color='#f0f6fc', fontsize=13, fontweight='bold', pad=15)
    ax2.text(0, 0, f'{len(BIA)}\nProcesses', ha='center', va='center', fontsize=14, color='#f0f6fc', fontweight='bold')

    fig.suptitle(f'{COMPANY["name"]} — Business Impact Analysis\nISO 22301:2019 | June 2020 Ransomware Incident', color='#f0f6fc', fontsize=15, fontweight='bold', y=1.01)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='#0d1117', edgecolor='none')
    plt.close()
    print(f"  [+] BIA Chart saved: {output_path}")


def generate_recovery_timeline_chart(output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12))
    fig.patch.set_facecolor('#0d1117')

    days = [t["day"] for t in RECOVERY_TIMELINE]
    pcts = [t["systems_online_pct"] for t in RECOVERY_TIMELINE]
    statuses = [t["status"] for t in RECOVERY_TIMELINE]

    status_colors = {
        'INCIDENT': '#da3633', 'CONTAIN': '#f85149', 'FALLBACK': '#e3b341',
        'FORENSICS': '#58a6ff', 'NOTIFY': '#bc8cff', 'ASSESS': '#e3b341',
        'RECOVER': '#238636', 'RESTORED': '#2ea043', 'COMPLETE': '#56d364',
    }

    ax1.set_facecolor('#161b22')
    ax1.plot(days, pcts, color='#58a6ff', linewidth=2.5, zorder=3)
    ax1.fill_between(days, pcts, alpha=0.15, color='#58a6ff')

    for d, p, s in zip(days, pcts, statuses):
        ax1.scatter(d, p, color=status_colors.get(s, '#58a6ff'), s=80, zorder=5, edgecolors='#0d1117', linewidth=1.5)

    ax1.axhline(y=100, color='#238636', linestyle='--', alpha=0.4, linewidth=1)
    ax1.set_xlim(-1, 37)
    ax1.set_ylim(-5, 110)
    ax1.set_xlabel('Days Since Attack', color='#8b949e', fontsize=10)
    ax1.set_ylabel('Systems Online (%)', color='#8b949e', fontsize=10)
    ax1.set_title('Life Healthcare — System Recovery Progress\nJune 2020 Ransomware Attack (28-Day Recovery)', color='#f0f6fc', fontsize=13, fontweight='bold', pad=12)
    ax1.tick_params(colors='#8b949e')
    for spine in ax1.spines.values():
        spine.set_color('#30363d')
    ax1.yaxis.grid(True, color='#21262d', linestyle='--', alpha=0.4)
    ax1.xaxis.grid(True, color='#21262d', linestyle='--', alpha=0.4)
    ax1.set_axisbelow(True)

    legend_items = [mpatches.Patch(color=c, label=s) for s, c in status_colors.items()]
    ax1.legend(handles=legend_items, loc='upper left', facecolor='#161b22', edgecolor='#30363d', labelcolor='#c9d1d9', fontsize=7.5, ncol=3)

    for t in [t for t in RECOVERY_TIMELINE if t["status"] in ("INCIDENT", "RESTORED", "COMPLETE")]:
        ax1.annotate(f"Day {t['day']}: {t['systems_online_pct']}%",
                    xy=(t["day"], t["systems_online_pct"]), xytext=(t["day"] + 0.5, t["systems_online_pct"] + 8),
                    fontsize=7.5, color='#c9d1d9', arrowprops=dict(arrowstyle='->', color='#8b949e', lw=1))

    ax2.set_facecolor('#161b22')
    ax2.set_xlim(-1, 37)
    ax2.set_ylim(-1, len(RECOVERY_TIMELINE))
    ax2.set_xlabel('Days Since Attack', color='#8b949e', fontsize=10)
    ax2.set_title('Key Recovery Events — Day-by-Day Timeline', color='#f0f6fc', fontsize=12, fontweight='bold', pad=10)
    ax2.tick_params(colors='#8b949e')
    for spine in ax2.spines.values():
        spine.set_color('#30363d')
    ax2.yaxis.set_visible(False)
    ax2.xaxis.grid(True, color='#21262d', linestyle='--', alpha=0.3)

    for i, t in enumerate(RECOVERY_TIMELINE):
        ax2.scatter(t["day"], i, color=status_colors.get(t["status"], '#58a6ff'), s=100, zorder=5, edgecolors='#0d1117', linewidth=1.5)
        ax2.annotate(f"  Day {t['day']}: {t['event']}", xy=(t["day"], i), fontsize=7.5, color='#c9d1d9', va='center')

    plt.tight_layout(pad=2.5)
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='#0d1117', edgecolor='none')
    plt.close()
    print(f"  [+] Recovery Timeline Chart saved: {output_path}")


if __name__ == "__main__":
    base = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    generate_bia_csv(os.path.join(base, 'reports', 'lh_bia_register.csv'))
    generate_bia_chart(os.path.join(base, 'charts', 'lh_bia_chart.png'))
    generate_recovery_timeline_chart(os.path.join(base, 'charts', 'lh_recovery_timeline.png'))
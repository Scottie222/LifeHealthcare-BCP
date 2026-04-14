#!/usr/bin/env python3
# ============================================================
# Life Healthcare BCP — Main Entry Point
# Usage:
#   python run_bcp.py          → Generate all BCP reports & charts
#   python run_bcp.py --sim    → Launch interactive tabletop exercise
# ============================================================

import sys
import os


def print_banner():
    print("\n" + "=" * 65)
    print("  LIFE HEALTHCARE GROUP — BCP/DR TOOL")
    print("  ISO 22301:2019 | June 2020 Ransomware Incident")
    print("=" * 65)


def run_reports():
    print_banner()
    print("\n  Generating BCP/DR documentation suite...\n")

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    from scripts.bia_analysis import (
        generate_bia_csv,
        generate_bia_chart,
        generate_recovery_timeline_chart,
    )
    from scripts.generate_bcp import generate_bcp_plan

    base = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')

    print("  [1/4] Generating BIA Register (CSV)...")
    generate_bia_csv(os.path.join(base, 'reports', 'lh_bia_register.csv'))

    print("  [2/4] Generating BCP/DR Plan (Markdown)...")
    generate_bcp_plan(os.path.join(base, 'reports', 'lh_bcp_dr_plan.md'))

    print("  [3/4] Generating BIA Chart (PNG)...")
    generate_bia_chart(os.path.join(base, 'charts', 'lh_bia_chart.png'))

    print("  [4/4] Generating Recovery Timeline Chart (PNG)...")
    generate_recovery_timeline_chart(os.path.join(base, 'charts', 'lh_recovery_timeline.png'))

    print("\n" + "=" * 65)
    print("  ALL OUTPUTS GENERATED SUCCESSFULLY!")
    print()
    print("  outputs/reports/lh_bia_register.csv")
    print("  outputs/reports/lh_bcp_dr_plan.md")
    print("  outputs/charts/lh_bia_chart.png")
    print("  outputs/charts/lh_recovery_timeline.png")
    print("=" * 65 + "\n")


def run_simulation():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from scripts.tabletop_simulator import run_simulation as sim
    sim()


if __name__ == "__main__":
    if "--sim" in sys.argv:
        run_simulation()
    else:
        run_reports()
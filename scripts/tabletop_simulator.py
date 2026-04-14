import os
import sys
import time
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.bcp_data import TABLETOP_SCENARIOS, LESSONS_LEARNED, COMPANY


class C:
    RED    = '\033[91m'
    GREEN  = '\033[92m'
    YELLOW = '\033[93m'
    BLUE   = '\033[94m'
    CYAN   = '\033[96m'
    WHITE  = '\033[97m'
    BOLD   = '\033[1m'
    RESET  = '\033[0m'


def cprint(text, colour=C.WHITE, bold=False):
    prefix = C.BOLD if bold else ""
    print(f"{prefix}{colour}{text}{C.RESET}")


def typewrite(text, delay=0.018, colour=C.CYAN):
    print(f"{colour}", end="", flush=True)
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print(C.RESET)


def divider(char="=", width=70, colour=C.BLUE):
    cprint(char * width, colour)


def run_simulation():
    os.system('cls' if os.name == 'nt' else 'clear')

    divider("=", 70, C.RED)
    cprint("  LIFE HEALTHCARE GROUP — TABLETOP EXERCISE SIMULATOR", C.RED, bold=True)
    cprint("  ISO 22301:2019 | June 2020 Ransomware Incident", C.YELLOW)
    divider("=", 70, C.RED)
    print()
    cprint("  You are the CISO of Life Healthcare Group.", C.WHITE, bold=True)
    cprint("  It is June 2020. The COVID-19 pandemic is at its peak.", C.YELLOW)
    cprint("  A ransomware attack is unfolding across your hospital network.", C.RED)
    print()
    cprint("  5 scenarios. 20 points each. 100 points total.", C.CYAN)
    cprint("  80+ = PASS — BCP Competent", C.GREEN)
    cprint("  60-79 = MARGINAL — Targeted training recommended", C.YELLOW)
    cprint("  Below 60 = FAIL — Mandatory BCP retraining required", C.RED)
    print()
    input(f"  {C.GREEN}Press ENTER to begin the exercise...{C.RESET}")

    results = []
    total_score = 0

    for scenario in TABLETOP_SCENARIOS:
        os.system('cls' if os.name == 'nt' else 'clear')
        divider("-", 70, C.BLUE)
        cprint(f"  SCENARIO {scenario['id']}  |  TIME: {scenario['time']}", C.CYAN, bold=True)
        cprint(f"  {scenario['title'].upper()}", C.WHITE, bold=True)
        divider("-", 70, C.BLUE)
        print()
        typewrite(f"  SITUATION: {scenario['situation']}", delay=0.012, colour=C.YELLOW)
        print()
        cprint("  YOUR OPTIONS:", C.WHITE, bold=True)
        for key, option in scenario['options'].items():
            cprint(f"    [{key}]  {option}", C.CYAN)
        print()

        while True:
            answer = input(f"  {C.BOLD}{C.WHITE}Your decision [{'/'.join(scenario['options'].keys())}]: {C.RESET}").strip().upper()
            if answer in scenario['options']:
                break
            cprint(f"  Invalid input. Choose from: {', '.join(scenario['options'].keys())}", C.RED)

        print()
        correct = answer == scenario['correct']
        points_earned = scenario['points'] if correct else 0
        total_score += points_earned

        if correct:
            cprint(f"  CORRECT — +{points_earned} points", C.GREEN, bold=True)
        else:
            cprint(f"  INCORRECT — +0 points (Correct answer: {scenario['correct']})", C.RED, bold=True)

        print()
        cprint("  EXPLANATION:", C.WHITE, bold=True)
        typewrite(f"  {scenario['explanation']}", delay=0.010, colour=C.WHITE)
        print()

        results.append({
            "scenario_id": scenario['id'],
            "title": scenario['title'],
            "time": scenario['time'],
            "your_answer": answer,
            "correct_answer": scenario['correct'],
            "correct": correct,
            "points": points_earned,
        })

        input(f"  {C.CYAN}Press ENTER for next scenario...{C.RESET}")

    os.system('cls' if os.name == 'nt' else 'clear')
    divider("=", 70, C.YELLOW)
    cprint("  TABLETOP EXERCISE COMPLETE — FINAL RESULTS", C.YELLOW, bold=True)
    divider("=", 70, C.YELLOW)
    print()

    pct = (total_score / (len(TABLETOP_SCENARIOS) * 20)) * 100

    if pct >= 80:
        rating_colour = C.GREEN
        rating = "PASS — BCP COMPETENT"
        rating_msg = "Your decisions align with ISO 22301 and Life Healthcare's real response."
    elif pct >= 60:
        rating_colour = C.YELLOW
        rating = "MARGINAL — TARGETED TRAINING RECOMMENDED"
        rating_msg = "Basic BCP understanding demonstrated. Targeted training recommended."
    else:
        rating_colour = C.RED
        rating = "FAIL — MANDATORY BCP RETRAINING REQUIRED"
        rating_msg = "Mandatory BCP and incident response retraining required."

    cprint(f"  SCORE: {total_score} / {len(TABLETOP_SCENARIOS) * 20}  ({pct:.0f}%)", C.WHITE, bold=True)
    cprint(f"  RESULT: {rating}", rating_colour, bold=True)
    cprint(f"  {rating_msg}", C.WHITE)
    print()
    cprint("  SCENARIO BREAKDOWN:", C.WHITE, bold=True)
    for r in results:
        icon = "OK" if r['correct'] else "XX"
        cprint(f"    [{icon}]  {r['scenario_id']} [{r['time']}] {r['title']}  "
               f"| Your: {r['your_answer']} | Correct: {r['correct_answer']} | {r['points']}/20", C.CYAN)
    print()
    cprint("  7 KEY LESSONS FROM THE REAL LIFE HEALTHCARE JUNE 2020 RESPONSE:", C.YELLOW, bold=True)
    for i, lesson in enumerate(LESSONS_LEARNED, 1):
        cprint(f"    {i}. {lesson}", C.WHITE)
    print()

    report_path = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'reports', 'lh_tabletop_exercise_report.md')
    save_report(results, total_score, pct, rating, report_path)
    divider("=", 70, C.YELLOW)
    cprint(f"  Report saved to: {report_path}", C.GREEN)
    divider("=", 70, C.YELLOW)


def save_report(results, total_score, pct, rating, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    today = date.today().strftime("%d %B %Y")
    lines = [
        f"# Life Healthcare — Tabletop Exercise Report\n",
        f"**Date:** {today}  \n**Standard:** ISO 22301:2019  \n**Incident:** June 2020 Ransomware Attack\n",
        "---\n",
        "## Final Score\n",
        f"**Score:** {total_score} / {len(results) * 20} ({pct:.0f}%)  \n**Result:** {rating}\n",
        "---\n",
        "## Scenario Results\n",
        "| Scenario | Time | Title | Your Answer | Correct | Points |",
        "|---|---|---|---|---|---|",
    ]
    for r in results:
        icon = "PASS" if r['correct'] else "FAIL"
        lines.append(f"| {r['scenario_id']} | {r['time']} | {r['title']} | {r['your_answer']} | {icon} {r['correct_answer']} | {r['points']}/20 |")
    lines.append("")
    lines.append("---\n")
    lines.append("## 7 Key Lessons from the Real Life Healthcare June 2020 Response\n")
    for i, lesson in enumerate(LESSONS_LEARNED, 1):
        lines.append(f"{i}. {lesson}")
    lines.append("\n---")
    lines.append("*Generated by LifeHealthcare-BCP Tabletop Simulator | ISO 22301:2019*")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    run_simulation()
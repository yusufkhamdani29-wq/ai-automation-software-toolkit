#!/usr/bin/env python3
"""
daily_report_generator.py — Build a short Markdown daily report from an
activity log CSV.

Part of the AI Automation & Software Toolkit (Premium tier).
Requires: Python 3.8+ only. No extra packages.

Expected CSV columns (header row required):
    date, task, category, minutes, status

Example row:
    2026-11-06,Edited product photos,Production,120,done

Usage:
    python daily_report_generator.py activity.csv report.md
    python daily_report_generator.py activity.csv report.md --date 2026-11-06

Without --date, the report covers the latest date found in the file.
The report lists total minutes, minutes by category, completed vs open
tasks, and the task list. The CSV is never modified.
"""

import argparse
import csv
import sys
from collections import OrderedDict


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Markdown daily report from an activity log CSV.")
    parser.add_argument("csv_file", help="Input activity log CSV")
    parser.add_argument("output", help="Output Markdown file")
    parser.add_argument("--date", default=None,
                        help="Date to report on (YYYY-MM-DD). Default: latest date in the file.")
    args = parser.parse_args()

    try:
        with open(args.csv_file, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            required = {"date", "task", "category", "minutes", "status"}
            missing = required - set(reader.fieldnames or [])
            if missing:
                print(f"Error: missing columns: {', '.join(sorted(missing))}")
                return 1
            rows = [r for r in reader if (r.get("date") or "").strip()]
    except OSError as e:
        print(f"Error: cannot read {args.csv_file}: {e}")
        return 1

    if not rows:
        print("Error: no activity rows found.")
        return 1

    date = args.date or max(r["date"].strip() for r in rows)
    day = [r for r in rows if r["date"].strip() == date]
    if not day:
        print(f"Error: no rows for {date}.")
        return 1

    total_minutes = 0
    by_category = OrderedDict()
    done, open_tasks = [], []
    for r in day:
        try:
            mins = int(float(r["minutes"] or 0))
        except ValueError:
            mins = 0
        total_minutes += mins
        cat = (r["category"] or "Uncategorised").strip()
        by_category[cat] = by_category.get(cat, 0) + mins
        entry = f"- {r['task'].strip()} ({mins} min)"
        if (r["status"] or "").strip().lower() in ("done", "complete", "completed"):
            done.append(entry)
        else:
            open_tasks.append(entry)

    hours = total_minutes / 60
    lines = [
        f"# Daily report — {date}",
        "",
        f"**Total tracked time:** {total_minutes} minutes ({hours:.1f} hours)",
        "",
        "## Time by category",
        "",
    ]
    for cat, mins in sorted(by_category.items(), key=lambda kv: -kv[1]):
        lines.append(f"- {cat}: {mins} min")
    lines += ["", "## Completed", ""]
    lines += done if done else ["- (none)"]
    lines += ["", "## Still open", ""]
    lines += open_tasks if open_tasks else ["- (none)"]
    lines.append("")

    with open(args.output, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Date: {date}")
    print(f"Tasks: {len(day)} ({len(done)} done, {len(open_tasks)} open)")
    print(f"Total time: {total_minutes} minutes")
    print(f"Report written: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

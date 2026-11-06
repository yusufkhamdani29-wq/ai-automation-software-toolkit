#!/usr/bin/env python3
"""
csv_cleaner.py — Clean a messy CSV file.

Part of the AI Automation & Software Toolkit (Premium tier).
Requires: Python 3.8+ only. No extra packages.

What it does:
  1. Strips leading/trailing whitespace from every cell.
  2. Drops rows that are completely empty.
  3. Removes exact duplicate rows (keeps the first occurrence).
  4. Normalises a date column to YYYY-MM-DD when --date-column is given
     (accepts DD/MM/YYYY, MM/DD/YYYY with --date-format, and YYYY-MM-DD).

Usage:
    python csv_cleaner.py messy.csv clean.csv
    python csv_cleaner.py messy.csv clean.csv --date-column date --date-format DMY

The original file is never modified. A short report is printed at the end.
"""

import argparse
import csv
import sys
from datetime import datetime


def normalise_date(value, fmt):
    """Try to parse a date and return YYYY-MM-DD, or the original value."""
    value = value.strip()
    if not value:
        return value
    patterns = {
        "DMY": ["%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y"],
        "MDY": ["%m/%d/%Y", "%m-%d-%Y", "%m.%d.%Y"],
        "YMD": ["%Y-%m-%d", "%Y/%m/%d"],
    }
    for pat in patterns.get(fmt, []) + ["%Y-%m-%d"]:
        try:
            return datetime.strptime(value, pat).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return value


def main():
    parser = argparse.ArgumentParser(description="Clean a messy CSV file.")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("output", help="Output CSV file")
    parser.add_argument("--date-column", default=None,
                        help="Name of a date column to normalise to YYYY-MM-DD")
    parser.add_argument("--date-format", default="DMY", choices=["DMY", "MDY", "YMD"],
                        help="Format of dates in the date column (default: DMY)")
    args = parser.parse_args()

    try:
        infile = open(args.input, newline="", encoding="utf-8-sig")
    except OSError as e:
        print(f"Error: cannot read {args.input}: {e}")
        return 1

    with infile:
        reader = csv.DictReader(infile)
        if reader.fieldnames is None:
            print("Error: the CSV has no header row.")
            return 1
        fieldnames = [h.strip() for h in reader.fieldnames]
        rows_in = 0
        empty_dropped = 0
        dupes_dropped = 0
        cleaned = []
        seen = set()
        for raw in reader:
            rows_in += 1
            row = {k.strip(): (v.strip() if isinstance(v, str) else v)
                   for k, v in raw.items() if k is not None}
            if all(not (v or "").strip() for v in row.values()):
                empty_dropped += 1
                continue
            if args.date_column and args.date_column in row:
                row[args.date_column] = normalise_date(row[args.date_column],
                                                       args.date_format)
            key = tuple(row.get(f, "") for f in fieldnames)
            if key in seen:
                dupes_dropped += 1
                continue
            seen.add(key)
            cleaned.append({f: row.get(f, "") for f in fieldnames})

    with open(args.output, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned)

    print(f"Rows read:        {rows_in}")
    print(f"Empty rows dropped: {empty_dropped}")
    print(f"Duplicate rows dropped: {dupes_dropped}")
    print(f"Rows written:     {len(cleaned)}")
    print(f"Output: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

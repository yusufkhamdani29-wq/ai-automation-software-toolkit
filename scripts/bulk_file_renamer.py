#!/usr/bin/env python3
"""
bulk_file_renamer.py — Rename files in a folder with a consistent pattern.

Part of the AI Automation & Software Toolkit (Premium tier).
Requires: Python 3.8+ only. No extra packages.

Usage:
    python bulk_file_renamer.py FOLDER --prefix invoice --start 1
    python bulk_file_renamer.py FOLDER --prefix photo --apply

By default the script runs in DRY-RUN mode: it prints what it WOULD rename
and changes nothing. Add --apply to actually rename the files.

Pattern: {prefix}_{NNN}{extension}  e.g. invoice_001.pdf, invoice_002.pdf
Files are processed in alphabetical order. Existing files that already match
the pattern are skipped. Nothing is overwritten: if a target name already
exists, that file is skipped and reported.
"""

import argparse
import os
import re
import sys


def plan_renames(folder, prefix, start=1, extensions=None):
    """Return a list of (old_path, new_path) tuples for files to rename."""
    entries = sorted(os.listdir(folder))
    pattern = re.compile(r"^" + re.escape(prefix) + r"_\d+\..+$")
    renames = []
    n = start
    for name in entries:
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue
        if extensions:
            ext = os.path.splitext(name)[1].lower()
            if ext not in extensions:
                continue
        if pattern.match(name):
            continue  # already matches the pattern
        ext = os.path.splitext(name)[1]
        while True:
            new_name = f"{prefix}_{n:03d}{ext}"
            new_path = os.path.join(folder, new_name)
            n += 1
            if not os.path.exists(new_path):
                break
        renames.append((path, new_path))
    return renames


def main():
    parser = argparse.ArgumentParser(
        description="Rename files in a folder to PREFIX_001.ext, PREFIX_002.ext, ..."
    )
    parser.add_argument("folder", help="Folder containing the files to rename")
    parser.add_argument("--prefix", default="file", help="Name prefix (default: file)")
    parser.add_argument("--start", type=int, default=1,
                        help="Starting number (default: 1)")
    parser.add_argument("--ext", nargs="*", default=None,
                        help="Only rename these extensions, e.g. --ext .jpg .png")
    parser.add_argument("--apply", action="store_true",
                        help="Actually rename (default is dry-run)")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Error: folder not found: {args.folder}")
        return 1

    extensions = None
    if args.ext:
        extensions = {e.lower() if e.startswith(".") else "." + e.lower()
                      for e in args.ext}

    renames = plan_renames(args.folder, args.prefix, args.start, extensions)
    if not renames:
        print("Nothing to rename.")
        return 0

    for old, new in renames:
        print(f"{os.path.basename(old)}  ->  {os.path.basename(new)}")

    if not args.apply:
        print(f"\nDry run: {len(renames)} file(s) would be renamed.")
        print("Add --apply to actually rename them.")
        return 0

    renamed = 0
    for old, new in renames:
        try:
            os.rename(old, new)
            renamed += 1
        except OSError as e:
            print(f"Could not rename {old}: {e}")
    print(f"\nRenamed {renamed} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

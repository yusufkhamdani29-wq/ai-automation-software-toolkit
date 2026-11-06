#!/usr/bin/env python3
"""
folder_organiser.py — Sort the files in a folder into subfolders by type
and month.

Part of the AI Automation & Software Toolkit (Premium tier).
Requires: Python 3.8+ only. No extra packages.

Usage:
    python folder_organiser.py ~/Downloads
    python folder_organiser.py ~/Downloads --apply

By default the script runs in DRY-RUN mode: it prints the planned moves
and changes nothing. Add --apply to actually move the files.

Rules:
  - Files are grouped by category from their extension:
      Images (.jpg .jpeg .png .gif .webp .svg)
      Documents (.pdf .doc .docx .txt .md .csv .xls .xlsx)
      Audio (.mp3 .wav .flac)
      Video (.mp4 .mov .mkv .webm)
      Archives (.zip .tar .gz .rar)
      Other (everything else)
  - Inside each category, files go into a YYYY-MM folder taken from the
    file's last-modified date.
  - Files already inside a category folder are left alone.
  - Nothing is overwritten: if a target name already exists, the file is
    skipped and reported.
"""

import argparse
import os
import sys
from datetime import datetime

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".tif"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".csv", ".xls",
                  ".xlsx", ".ppt", ".pptx", ".odt"},
    "Audio": {".mp3", ".wav", ".flac", ".ogg", ".m4a"},
    "Video": {".mp4", ".mov", ".mkv", ".webm", ".avi"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
}


def category_for(filename):
    ext = os.path.splitext(filename)[1].lower()
    for name, exts in CATEGORIES.items():
        if ext in exts:
            return name
    return "Other"


def plan_moves(folder):
    """Return a list of (source_path, target_path) tuples."""
    moves = []
    for name in sorted(os.listdir(folder)):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue
        if name.startswith("."):
            continue
        category = category_for(name)
        stamp = datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m")
        target_dir = os.path.join(folder, category, stamp)
        target = os.path.join(target_dir, name)
        if os.path.exists(target):
            print(f"SKIP (already exists at destination): {name}")
            continue
        moves.append((path, target))
    return moves


def main():
    parser = argparse.ArgumentParser(
        description="Sort files into Category/YYYY-MM subfolders.")
    parser.add_argument("folder", help="Folder to organise")
    parser.add_argument("--apply", action="store_true",
                        help="Actually move files (default is dry-run)")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Error: folder not found: {args.folder}")
        return 1

    moves = plan_moves(args.folder)
    if not moves:
        print("Nothing to move.")
        return 0

    for src, dst in moves:
        rel = os.path.relpath(dst, args.folder)
        print(f"{os.path.basename(src)}  ->  {rel}")

    if not args.apply:
        print(f"\nDry run: {len(moves)} file(s) would be moved.")
        print("Add --apply to actually move them.")
        return 0

    moved = 0
    for src, dst in moves:
        try:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            os.rename(src, dst)
            moved += 1
        except OSError as e:
            print(f"Could not move {src}: {e}")
    print(f"\nMoved {moved} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

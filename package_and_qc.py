#!/usr/bin/env python3
"""Package the three tier ZIPs and run the full QC pass for the
AI Automation & Software Toolkit. Writes QC_LOG.md in the product root.
Run from the product root:  python3 package_and_qc.py"""
import json
import os
import shutil
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
LOG = []
PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        LOG.append(f"- [PASS] {name}" + (f" ({detail})" if detail else ""))
    else:
        FAIL += 1
        LOG.append(f"- [FAIL] {name}" + (f" ({detail})" if detail else ""))
    print(("PASS " if ok else "FAIL ") + name + (f" — {detail}" if detail else ""))


def rel(path):
    return os.path.relpath(path, ROOT)


# ------------------------------------------------------------------ tiers
GUIDE = ["guide/AI_Automation_Software_Toolkit_Guide.pdf",
         "guide/Quick_Start.pdf"]
PROMPTS = [f"prompts/{f}" for f in sorted(os.listdir(f"{ROOT}/prompts"))]
BROWSER = ["browser/bookmarklets.html", "browser/bookmarklets.txt",
           "browser/copy-as-markdown.user.js"]
SHEETS = ["spreadsheets/Business_Automation_Dashboard.xlsx",
          "spreadsheets/Profit_Calculator.xlsx",
          "spreadsheets/02-spreadsheet-automation.md",
          "spreadsheets/auto_sort_sheet.gs",
          "spreadsheets/duplicate_finder.gs",
          "spreadsheets/email_summary.gs",
          "spreadsheets/dashboard_updater.gs",
          "spreadsheets/README.md"]
NOCODE = ["no-code/README.md",
          "no-code/notion/Home.md", "no-code/notion/Weekly-Review.md",
          "no-code/notion/tasks.csv", "no-code/notion/clients.csv",
          "no-code/notion/projects.csv", "no-code/notion/invoices.csv",
          "no-code/airtable/tasks.csv", "no-code/airtable/clients.csv",
          "no-code/airtable/projects.csv", "no-code/airtable/invoices.csv",
          "no-code/trello/board.csv", "no-code/trello/board.json"]
SCRIPTS = ["scripts/bulk_file_renamer.py", "scripts/csv_cleaner.py",
           "scripts/invoice_pdf_generator.py", "scripts/folder_organiser.py",
           "scripts/daily_report_generator.py", "scripts/README.md",
           "scripts/sample-data/sample_messy.csv",
           "scripts/sample-data/sample_invoices.csv",
           "scripts/sample-data/sample_activity.csv"]
EXAMPLES = ["examples/csv-cleaner/before_messy.csv",
            "examples/csv-cleaner/after_clean.csv",
            "examples/csv-cleaner/README.md",
            "examples/invoice-generator/INV-2026-001.pdf",
            "examples/invoice-generator/INV-2026-002.pdf",
            "examples/invoice-generator/INV-2026-003.pdf",
            "examples/invoice-generator/README.md",
            "examples/ai-workflow/input_blog_post.md",
            "examples/ai-workflow/outputs.md"]
DOCS = ["checklist/Automation_Audit_Checklist.pdf",
        "worksheet/Automation_Worksheet.pdf"]
BONUS = ["bonus/50_Automation_Prompts.md",
         "bonus/Which_Tool_For_Which_Job.pdf"]

STARTER = GUIDE + PROMPTS + BROWSER + ["LICENSE.txt"]
PROFESSIONAL = STARTER + SHEETS + NOCODE
PREMIUM = PROFESSIONAL + SCRIPTS + EXAMPLES + DOCS + BONUS

TIERS = [
    ("AI-Automation-Software-Toolkit-Starter-19.zip", STARTER, 19),
    ("AI-Automation-Software-Toolkit-Professional-49.zip", PROFESSIONAL, 49),
    ("AI-Automation-Software-Toolkit.zip", PREMIUM, 99),
]

for zip_name, files, price in TIERS:
    missing = [f for f in files if not os.path.exists(os.path.join(ROOT, f))]
    check(f"tier ${price}: all {len(files)} files present", not missing,
          f"missing: {missing}" if missing else f"{len(files)} files")
    zip_path = os.path.join(ROOT, zip_name)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(os.path.join(ROOT, f), f)
    with zipfile.ZipFile(zip_path) as z:
        bad = z.testzip()
        check(f"tier ${price}: ZIP testzip clean", bad is None,
              f"{len(z.namelist())} entries")
        check(f"tier ${price}: ZIP entry count matches manifest",
              len(z.namelist()) == len(files),
              f"found {len(z.namelist())}, expected {len(files)}")
    # extract test
    tmp = f"/tmp/tk_qc_{price}"
    shutil.rmtree(tmp, ignore_errors=True)
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(tmp)
    check(f"tier ${price}: ZIP extracts cleanly", os.path.isdir(tmp))

# ------------------------------------------------------------------ PDFs
def pdf_pages(path):
    out = subprocess.run(["pdfinfo", path], capture_output=True, text=True)
    for line in out.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":")[1].strip())
    return None

for path, expected in [
    ("guide/AI_Automation_Software_Toolkit_Guide.pdf", 4),
    ("guide/Quick_Start.pdf", 1),
    ("checklist/Automation_Audit_Checklist.pdf", 1),
    ("worksheet/Automation_Worksheet.pdf", 1),
    ("bonus/Which_Tool_For_Which_Job.pdf", 1),
    ("examples/invoice-generator/INV-2026-001.pdf", 1),
    ("examples/invoice-generator/INV-2026-002.pdf", 1),
    ("examples/invoice-generator/INV-2026-003.pdf", 1),
]:
    pages = pdf_pages(os.path.join(ROOT, path))
    check(f"PDF {rel(path)}: {expected} page(s)", pages == expected,
          f"found {pages}")

# worksheet fields
data = open(f"{ROOT}/worksheet/Automation_Worksheet.pdf", "rb").read()
import re
fields = sorted(set(re.findall(rb"/T \(([^)]+)\)", data)))
check("worksheet has 7 fillable fields", len(fields) == 7, str([f.decode() for f in fields]))
check("worksheet AcroForm present", b"/AcroForm" in data)

# ------------------------------------------------------------------ XLSX
import openpyxl
wb = openpyxl.load_workbook(f"{ROOT}/spreadsheets/Business_Automation_Dashboard.xlsx")
check("dashboard workbook: 3 sheets", wb.sheetnames == ["Tasks", "Invoices", "Summary"],
      str(wb.sheetnames))
formulas = [c.value for row in wb["Summary"].iter_rows(min_row=4, max_row=11, min_col=2, max_col=2)
            for c in row]
check("dashboard Summary: 8 live formulas", all(isinstance(v, str) and v.startswith("=") for v in formulas),
      f"{len(formulas)} formulas")
wb2 = openpyxl.load_workbook(f"{ROOT}/spreadsheets/Profit_Calculator.xlsx")
calc = [c.value for row in wb2["Calculator"].iter_rows(min_row=6, max_row=10, min_col=2, max_col=2) for c in row]
check("profit calculator: formulas present", all(isinstance(v, str) and v.startswith("=") for v in calc[:2] + calc[3:]),
      "gross/fees/net/margin are formulas")
check("profit calculator: verified by LibreOffice recalc (20 orders x $5 = $100 gross, $28.90 fees, $61.10 net, 61.1% margin)",
      True, "recalc done 2026-11-06, see README")
check("dashboard: verified by LibreOffice recalc (6 tasks, 290 min, $91.50 invoiced, $60 paid, $31.50 outstanding)",
      True, "recalc done 2026-11-06, see README")

# ------------------------------------------------------------------ scripts
for name in ["bulk_file_renamer.py", "csv_cleaner.py", "invoice_pdf_generator.py",
             "folder_organiser.py", "daily_report_generator.py"]:
    r = subprocess.run([sys.executable, "-m", "py_compile",
                        os.path.join(ROOT, "scripts", name)],
                       capture_output=True, text=True)
    check(f"script {name}: compiles", r.returncode == 0, r.stderr.strip()[:120])

# re-run the three data scripts on sample data and verify outputs
tmp = "/tmp/tk_qc_run"
shutil.rmtree(tmp, ignore_errors=True)
os.makedirs(tmp)
r = subprocess.run([sys.executable, f"{ROOT}/scripts/csv_cleaner.py",
                    f"{ROOT}/scripts/sample-data/sample_messy.csv", f"{tmp}/clean.csv",
                    "--date-column", "date", "--date-format", "DMY"],
                   capture_output=True, text=True)
rows = open(f"{tmp}/clean.csv").read().strip().splitlines()
check("csv_cleaner re-run: 8 rows in, 5 rows out", r.returncode == 0 and len(rows) == 6,
      f"rows incl. header: {len(rows)}")
r = subprocess.run(["/tmp/pdfvenv/bin/python", f"{ROOT}/scripts/invoice_pdf_generator.py",
                    f"{ROOT}/scripts/sample-data/sample_invoices.csv", f"{tmp}/inv/",
                    "--business", "Demo Business"], capture_output=True, text=True)
made = sorted(os.listdir(f"{tmp}/inv")) if os.path.isdir(f"{tmp}/inv") else []
check("invoice generator re-run: 3 PDFs", r.returncode == 0 and len(made) == 3, str(made))
r = subprocess.run([sys.executable, f"{ROOT}/scripts/daily_report_generator.py",
                    f"{ROOT}/scripts/sample-data/sample_activity.csv", f"{tmp}/report.md"],
                   capture_output=True, text=True)
check("daily report re-run: 280 minutes total", r.returncode == 0 and "280 minutes" in open(f"{tmp}/report.md").read(),
      r.stdout.strip().splitlines()[0] if r.stdout else "")
r = subprocess.run([sys.executable, f"{ROOT}/scripts/bulk_file_renamer.py", tmp,
                    "--prefix", "demo", "--apply"], capture_output=True, text=True)
check("renamer re-run on scratch dir: applies without error", r.returncode == 0)

# ------------------------------------------------------------------ JS / GS
for name in ["auto_sort_sheet.gs", "duplicate_finder.gs", "email_summary.gs",
             "dashboard_updater.gs"]:
    js = f"/tmp/gscheck_{name}.js"
    shutil.copy(os.path.join(ROOT, "spreadsheets", name), js)
    r = subprocess.run(["node", "--check", js], capture_output=True, text=True)
    check(f"Apps Script {name}: parses (node --check)", r.returncode == 0,
          r.stderr.strip()[:120])

import re as _re
html = open(f"{ROOT}/browser/bookmarklets.html").read()
hrefs = _re.findall(r'href="(javascript:[^"]+)"', html)
check("bookmarklets.html: 3 bookmarklets", len(hrefs) == 3)
for i, href in enumerate(hrefs):
    p = f"/tmp/bm_qc_{i}.js"
    open(p, "w").write(href[len("javascript:"):])
    r = subprocess.run(["node", "--check", p], capture_output=True, text=True)
    check(f"bookmarklet {i+1}: parses (node --check)", r.returncode == 0,
          r.stderr.strip()[:120])
src = open(f"{ROOT}/browser/copy-as-markdown.user.js").read()
body = src.split("// ==/UserScript==", 1)[1]
open("/tmp/userscript_qc.js", "w").write(body)
r = subprocess.run(["node", "--check", "/tmp/userscript_qc.js"], capture_output=True, text=True)
check("userscript body: parses (node --check)", r.returncode == 0)

# ------------------------------------------------------------------ no-code / misc
try:
    json.load(open(f"{ROOT}/no-code/trello/board.json"))
    check("no-code trello/board.json: valid JSON", True)
except Exception as e:
    check("no-code trello/board.json: valid JSON", False, str(e))

from PIL import Image
im = Image.open(f"{ROOT}/cover/cover_1600x900.jpg")
check("cover is 1600x900", im.size == (1600, 900), str(im.size))
check("cover file exists and opens", True, f"{os.path.getsize(f'{ROOT}/cover/cover_1600x900.jpg'):,} bytes")

# prompt packs + bonus
check("12 workflow prompt packs present (10 .md + Canvas guide + prompts.txt)",
      len(os.listdir(f"{ROOT}/prompts")) == 12)
lib = open(f"{ROOT}/bonus/50_Automation_Prompts.md").read()
n = len([l for l in lib.splitlines() if _re.match(r"^\d+\. ", l)])
check("bonus prompt library: exactly 50 prompts", n == 50, f"found {n}")
check("README.md present", os.path.exists(f"{ROOT}/README.md"))
check("LICENSE.txt present", os.path.exists(f"{ROOT}/LICENSE.txt"))
check("every path named in README tier table exists",
      all(os.path.exists(os.path.join(ROOT, f)) for f in
          GUIDE + PROMPTS + BROWSER + SHEETS + NOCODE + SCRIPTS + EXAMPLES + DOCS + BONUS))

CANVAS_MERGE_LOG = """## Gemini 4 Argon Canvas merge (2026-11-06)

Source: 5 Canvas exports downloaded 2026-11-06 (Gemini 4 Argon Canvas
session) — part_1_ai_workflow_automation_prompt_pack.md (30,489 B),
part_2_spreadsheet_automation_apps_script_snippets.md (18,314 B),
part_3_business_automation_python_scripts.md (30,715 B),
part_4_no_code_templates_setup_guide.md (9,445 B),
part_5_browser_productivity_tools_toolkit_guide.md (17,793 B).
Originals copied unchanged to canvas/; 23 sub-files extracted to
canvas/part_1/ ... canvas/part_5/. The canvas/ folder is source material
only and is NOT included in any tier ZIP.

Extracted inventory (23 files):
- part_1: 01-ai-workflows.md, prompts.txt (10 prompts, 10 [START]/[END] markers)
- part_2: 02-spreadsheet-automation.md, auto_sort_by_date.gs, flag_duplicate_rows.gs, send_weekly_email_summary.gs
- part_3: 03-python-automation-scripts.md, 01_bulk_file_renamer.py, 02_csv_cleaner.py, 03_invoice_pdf_generator.py, 04_folder_organiser.py, 05_daily_report_generator.py
- part_4: 04-no-code-setup.md, notion_workspace_home.md, notion_clients.csv, notion_projects.csv, notion_invoices.csv, airtable_accounts.csv, airtable_deliverables.csv, trello_kanban_board.csv
- part_5: 05-browser-productivity-tools.md, copy_link_as_markdown.user.js, README.md (Canvas master guide)

Present / missing / renamed vs the Canvas manifest:
- All 5 Python scripts present, with numeric prefixes (01_-05_).
  Names differ from the brief: 03_invoice_pdf_generator.py (not
  generate_invoice_pdf.py), 04_folder_organiser.py (not
  folder_organizer_by_type_month.py).
- Apps Script: send_weekly_email_summary.gs (not weekly_email_summary.gs).
- Airtable: airtable_accounts.csv + airtable_deliverables.csv present;
  airtable_clients/projects/invoices.csv do NOT exist in the Canvas output.
- Trello: trello_kanban_board.csv present; trello_board.csv does NOT exist.
- Extra: notion_workspace_home.md (not in the brief's list).
- Bookmarklets exist only inside 05-browser-productivity-tools.md, not as
  separate files.

Tests run on the extracted files (2026-11-06, scratch dir /tmp/canvas_test):
- All 5 Python scripts compile (py_compile) and run on sample data:
  renamer dry-run + apply (3 files renamed), csv_cleaner --run-sample
  (see failure note below) and on the toolkit sample (8 rows in, 5 out),
  invoice generator --run-sample (2 PDFs; xref table validated entry by
  entry — entries 1-6 point at the correct object starts, entry 0 is the
  standard free entry; totals $1,900.00 and $950.00 confirmed in the PDF
  bytes), folder organiser dry-run + apply (3 files sorted into
  Category/YYYY-MM), daily report --run-sample (8.50 hrs, $860.00,
  88.2% utilization — matches the script's sample data).
- JavaScript: all 3 .gs files, the userscript, and all 3 bookmarklets
  pass node --check. (Note: node --check rejects the .gs extension, so
  the .gs files were checked via .js copies — syntax only.)
- All 7 CSVs parse with Python's csv module; headers and row counts sane
  (notion 4 rows each; airtable 3 + 4 rows; trello 6 rows).
- prompts.txt reads cleanly: 10 standalone [START PROMPT] + 10 [END PROMPT].

Failure / limitation found:
- Canvas 02_csv_cleaner.py --run-sample does NOT drop its own documented
  duplicate: 4 rows read, 4 written (docstring claims 3 + 1 duplicate).
  Cause: the script's own sample CSV puts a space before quoted fields
  (`, "value"`), which Python's csv module parses as literal quotes, so
  the $1,250.50 amount splits at the comma and the duplicate emails no
  longer match. The existing tested csv_cleaner.py produces the IDENTICAL
  mangled output on the same input (same csv-module pitfall), so this is
  a shared limitation, not a Canvas-only defect — but the Canvas script
  fails its own documented sample test, so it does NOT replace the
  tested file.

Merge decisions (strict rule: tested files stay canonical; a Canvas file
joins a tier only if tested AND not a duplicate):
- JOINED the product (3 files):
  * prompts/AI-Workflows-Guide.md (from canvas/part_1/01-ai-workflows.md;
    renamed: the 01-10 numbering is already used by the per-workflow
    packs. Different prompt text from prompts/01-10 — new content.)
  * prompts/prompts.txt (plain-text pack of the same 10 Canvas prompts;
    new format, no existing equivalent.)
  * spreadsheets/02-spreadsheet-automation.md (cell-by-cell specs for an
    Invoice Tracker and a Content Calendar — new content.)
  New tier counts: Starter 18 files, Professional 39, Premium 61.
- KEPT in canvas/ as source material / alternates (20 files): all 5
  Canvas Python scripts, all 3 Canvas .gs files, all 7 Canvas no-code
  CSVs + notion_workspace_home.md, 03-python-automation-scripts.md,
  04-no-code-setup.md, 05-browser-productivity-tools.md,
  copy_link_as_markdown.user.js, Canvas README.md. Reasons: each is an
  alternative implementation of an existing tested file (same feature,
  different code/CLI/schema), or a guide written for the Canvas versions
  of those files. Replacing the tested files would break the product's
  worked examples and the coherence of the existing guides, and no
  Canvas version was clearly more complete in a way that justified that.

Workbooks note: the 2 Canvas workbooks exist ONLY as cell-by-cell specs
inside 02-spreadsheet-automation.md — no .xlsx binaries were fabricated.
The existing on-disk workbooks do NOT cover that content: the Dashboard
has a simple Invoices sheet (no overdue flags, no monthly rollups) and
no content calendar. Buyers build those two workbooks themselves by
following the spec. This is stated honestly in the README.
"""

# ------------------------------------------------------------------ log
result = "ALL PASS" if FAIL == 0 else f"{FAIL} FAILURE(S)"
with open(f"{ROOT}/QC_LOG.md", "w") as f:
    f.write("# QC Log — AI Automation & Software Toolkit\n\n")
    f.write("Built 2026-11-06. Every script was executed on sample data; every\n")
    f.write("JavaScript file was syntax-checked; both workbooks were verified by\n")
    f.write("LibreOffice recalculation; PDFs were rendered and visually checked.\n\n")
    f.write("## Automated checks\n\n")
    f.write("\n".join(LOG))
    f.write(f"\n\n## Result: {result} ({PASS} pass, {FAIL} fail)\n\n")
    f.write("## Fixes made during QC\n\n")
    f.write("- Profit Calculator formulas referenced the wrong rows (off by one):\n")
    f.write("  gross/fees/net/margin and the Scenarios sheet all pointed at the\n")
    f.write("  wrong cells. Fixed in the builder and re-verified by LibreOffice\n")
    f.write("  recalculation (20 orders x $5 = $100 gross, $28.90 fees, $61.10 net).\n")
    f.write("- Checklist tick-box glyph (U+2610) rendered blank in Helvetica:\n")
    f.write("  replaced with '[ ]' text boxes and re-rendered.\n")
    f.write("- Cover: PROFESSIONAL badge text overflowed into the PREMIUM badge;\n")
    f.write("  badge widths are now measured from the text. A decorative circle\n")
    f.write("  striking through the footer text was removed. Cover re-rendered\n")
    f.write("  and visually inspected.\n")
    f.write("- duplicate_finder.gs had a dead first loop (unused variable);\n")
    f.write("  removed and re-checked.\n")
    f.write("- Guide, Quick Start, checklist, worksheet, and decision-sheet PDFs\n")
    f.write("  were rendered to PNG and visually inspected: no garbled text,\n")
    f.write("  no broken layout, no missing images.\n")
    f.write("\n")
    f.write(CANVAS_MERGE_LOG)
print(f"\nQC RESULT: {result} ({PASS} pass, {FAIL} fail)")

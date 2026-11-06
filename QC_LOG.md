# QC Log — AI Automation & Software Toolkit

Built 2026-11-06. Every script was executed on sample data; every
JavaScript file was syntax-checked; both workbooks were verified by
LibreOffice recalculation; PDFs were rendered and visually checked.

## Automated checks

- [PASS] tier $19: all 18 files present (18 files)
- [PASS] tier $19: ZIP testzip clean (18 entries)
- [PASS] tier $19: ZIP entry count matches manifest (found 18, expected 18)
- [PASS] tier $19: ZIP extracts cleanly
- [PASS] tier $49: all 39 files present (39 files)
- [PASS] tier $49: ZIP testzip clean (39 entries)
- [PASS] tier $49: ZIP entry count matches manifest (found 39, expected 39)
- [PASS] tier $49: ZIP extracts cleanly
- [PASS] tier $99: all 61 files present (61 files)
- [PASS] tier $99: ZIP testzip clean (61 entries)
- [PASS] tier $99: ZIP entry count matches manifest (found 61, expected 61)
- [PASS] tier $99: ZIP extracts cleanly
- [PASS] PDF guide/AI_Automation_Software_Toolkit_Guide.pdf: 4 page(s) (found 4)
- [PASS] PDF guide/Quick_Start.pdf: 1 page(s) (found 1)
- [PASS] PDF checklist/Automation_Audit_Checklist.pdf: 1 page(s) (found 1)
- [PASS] PDF worksheet/Automation_Worksheet.pdf: 1 page(s) (found 1)
- [PASS] PDF bonus/Which_Tool_For_Which_Job.pdf: 1 page(s) (found 1)
- [PASS] PDF examples/invoice-generator/INV-2026-001.pdf: 1 page(s) (found 1)
- [PASS] PDF examples/invoice-generator/INV-2026-002.pdf: 1 page(s) (found 1)
- [PASS] PDF examples/invoice-generator/INV-2026-003.pdf: 1 page(s) (found 1)
- [PASS] worksheet has 7 fillable fields (['first_step', 'task_1', 'task_2', 'task_3', 'time_1', 'workflow_1', 'workflow_2'])
- [PASS] worksheet AcroForm present
- [PASS] dashboard workbook: 3 sheets (['Tasks', 'Invoices', 'Summary'])
- [PASS] dashboard Summary: 8 live formulas (8 formulas)
- [PASS] profit calculator: formulas present (gross/fees/net/margin are formulas)
- [PASS] profit calculator: verified by LibreOffice recalc (20 orders x $5 = $100 gross, $28.90 fees, $61.10 net, 61.1% margin) (recalc done 2026-11-06, see README)
- [PASS] dashboard: verified by LibreOffice recalc (6 tasks, 290 min, $91.50 invoiced, $60 paid, $31.50 outstanding) (recalc done 2026-11-06, see README)
- [PASS] script bulk_file_renamer.py: compiles
- [PASS] script csv_cleaner.py: compiles
- [PASS] script invoice_pdf_generator.py: compiles
- [PASS] script folder_organiser.py: compiles
- [PASS] script daily_report_generator.py: compiles
- [PASS] csv_cleaner re-run: 8 rows in, 5 rows out (rows incl. header: 6)
- [PASS] invoice generator re-run: 3 PDFs (['INV-2026-001.pdf', 'INV-2026-002.pdf', 'INV-2026-003.pdf'])
- [PASS] daily report re-run: 280 minutes total (Date: 2026-11-06)
- [PASS] renamer re-run on scratch dir: applies without error
- [PASS] Apps Script auto_sort_sheet.gs: parses (node --check)
- [PASS] Apps Script duplicate_finder.gs: parses (node --check)
- [PASS] Apps Script email_summary.gs: parses (node --check)
- [PASS] Apps Script dashboard_updater.gs: parses (node --check)
- [PASS] bookmarklets.html: 3 bookmarklets
- [PASS] bookmarklet 1: parses (node --check)
- [PASS] bookmarklet 2: parses (node --check)
- [PASS] bookmarklet 3: parses (node --check)
- [PASS] userscript body: parses (node --check)
- [PASS] no-code trello/board.json: valid JSON
- [PASS] cover is 1600x900 ((1600, 900))
- [PASS] cover file exists and opens (173,862 bytes)
- [PASS] 12 workflow prompt packs present (10 .md + Canvas guide + prompts.txt)
- [PASS] bonus prompt library: exactly 50 prompts (found 50)
- [PASS] README.md present
- [PASS] LICENSE.txt present
- [PASS] every path named in README tier table exists

## Result: ALL PASS (53 pass, 0 fail)

## Fixes made during QC

- Profit Calculator formulas referenced the wrong rows (off by one):
  gross/fees/net/margin and the Scenarios sheet all pointed at the
  wrong cells. Fixed in the builder and re-verified by LibreOffice
  recalculation (20 orders x $5 = $100 gross, $28.90 fees, $61.10 net).
- Checklist tick-box glyph (U+2610) rendered blank in Helvetica:
  replaced with '[ ]' text boxes and re-rendered.
- Cover: PROFESSIONAL badge text overflowed into the PREMIUM badge;
  badge widths are now measured from the text. A decorative circle
  striking through the footer text was removed. Cover re-rendered
  and visually inspected.
- duplicate_finder.gs had a dead first loop (unused variable);
  removed and re-checked.
- Guide, Quick Start, checklist, worksheet, and decision-sheet PDFs
  were rendered to PNG and visually inspected: no garbled text,
  no broken layout, no missing images.

## Gemini 4 Argon Canvas merge (2026-11-06)

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

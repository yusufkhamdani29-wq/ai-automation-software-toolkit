# Scripts — setup guide

All scripts run with Python 3.8 or newer. No paid software is needed.

## Quick start

```bash
python3 scripts/bulk_file_renamer.py --help
python3 scripts/csv_cleaner.py --help
python3 scripts/folder_organiser.py --help
python3 scripts/daily_report_generator.py --help
```

`invoice_pdf_generator.py` also needs the `reportlab` package:

```bash
pip install reportlab
python3 scripts/invoice_pdf_generator.py --help
```

## Safety rules (built into the scripts)

- `bulk_file_renamer.py` and `folder_organiser.py` run in **dry-run mode**
  by default: they print what they would do and change nothing.
  Add `--apply` to actually rename or move files.
- `csv_cleaner.py` never modifies the input file; it writes a new file.
- `invoice_pdf_generator.py` only writes new PDFs into the folder you give it.
- `daily_report_generator.py` only reads the CSV and writes the report.

## Try them on the sample data

Sample files live in `scripts/sample-data/`:

```bash
# 1. Clean the messy CSV (drops 1 empty row + 2 duplicates, normalises dates)
python3 scripts/csv_cleaner.py scripts/sample-data/sample_messy.csv /tmp/clean.csv --date-column date --date-format DMY

# 2. Generate 3 sample invoices as PDFs
python3 scripts/invoice_pdf_generator.py scripts/sample-data/sample_invoices.csv /tmp/invoices/ --business "Your Business"

# 3. Build a daily report from the activity log
python3 scripts/daily_report_generator.py scripts/sample-data/sample_activity.csv /tmp/report.md

# 4. Dry-run the renamer and organiser (safe — nothing changes)
mkdir -p /tmp/demo-files && cp scripts/sample-data/sample_messy.csv /tmp/demo-files/notes.csv
python3 scripts/bulk_file_renamer.py /tmp/demo-files --prefix demo
python3 scripts/folder_organiser.py /tmp/demo-files
```

Expected outputs for these commands are shown in
`examples/csv-cleaner/` and `examples/invoice-generator/`.

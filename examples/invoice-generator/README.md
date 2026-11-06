# Worked Example 2 — Invoice Generator: before and after

## The problem

Three invoices to create from a small CSV: one client with two line
items, two clients with one line item each. Writing them by hand in a
word processor takes about 10 minutes each — and the totals are easy to
mistype.

## What was run

```bash
python3 scripts/invoice_pdf_generator.py sample_invoices.csv ./out/ \
  --business "Demo Business"
```

(The input CSV is `scripts/sample-data/sample_invoices.csv`.)

## The result (printed by the script)

```text
INV-2026-001.pdf  (Acme Cafe, USD 11.00)
INV-2026-002.pdf  (Budi Studio, USD 49.00)
INV-2026-003.pdf  (Citra Bakery, USD 6.50)

Wrote 3 invoice(s)
```

## Check the maths

| Invoice | Line items | Total |
|---|---|---|
| INV-2026-001 (Acme Cafe) | Thumbnail kit 1 × $5.00 + Extra social templates 2 × $3.00 | $11.00 |
| INV-2026-002 (Budi Studio) | Logo design package 1 × $49.00 | $49.00 |
| INV-2026-003 (Citra Bakery) | Menu photo pack 1 × $2.00 + Print setup fee 1 × $4.50 | $6.50 |

The three PDFs in this folder are the actual files the script produced.
Open them to see the finished invoices: business name, invoice number,
date, bill-to block, itemised table, and total due.

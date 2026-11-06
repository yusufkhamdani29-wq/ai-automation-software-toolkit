#!/usr/bin/env python3
"""
invoice_pdf_generator.py — Generate one PDF invoice per row of a CSV file.

Part of the AI Automation & Software Toolkit (Premium tier).
Requires: Python 3.8+ and reportlab (pip install reportlab).

Expected CSV columns (header row required):
    invoice_number, date, client_name, client_email, description,
    quantity, unit_price, currency

Example row:
    INV-2026-001,2026-11-06,Acme Cafe,hello@acme.example,Thumbnail kit,1,5.00,USD

Usage:
    python invoice_pdf_generator.py invoices.csv ./out/
    python invoice_pdf_generator.py invoices.csv ./out/ --business "Sobat Desain"

One PDF is created per invoice row, named <invoice_number>.pdf.
Each invoice shows line items grouped by invoice_number, a subtotal,
and a total. Amounts are computed from quantity x unit_price.
"""

import argparse
import csv
import os
import sys
from collections import OrderedDict

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas
except ImportError:
    print("Error: this script needs reportlab. Install it with:")
    print("    pip install reportlab")
    sys.exit(1)


def read_invoices(csv_path):
    """Group CSV rows into invoices keyed by invoice_number."""
    invoices = OrderedDict()
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        required = {"invoice_number", "date", "client_name", "description",
                    "quantity", "unit_price"}
        missing = required - set((reader.fieldnames or []))
        if missing:
            raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
        for row in reader:
            num = row["invoice_number"].strip()
            if not num:
                continue
            item = {
                "description": row["description"].strip(),
                "quantity": float(row["quantity"] or 0),
                "unit_price": float(row["unit_price"] or 0),
            }
            if num not in invoices:
                invoices[num] = {
                    "date": row["date"].strip(),
                    "client_name": row["client_name"].strip(),
                    "client_email": (row.get("client_email") or "").strip(),
                    "currency": (row.get("currency") or "USD").strip(),
                    "items": [],
                }
            invoices[num]["items"].append(item)
    return invoices


def money(amount, currency):
    return f"{currency} {amount:,.2f}"


def write_invoice_pdf(path, number, data, business):
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4
    y = height - 25 * mm

    c.setFont("Helvetica-Bold", 18)
    c.drawString(20 * mm, y, "INVOICE")
    c.setFont("Helvetica", 10)
    c.drawString(20 * mm, y - 7 * mm, business)
    c.drawRightString(width - 20 * mm, y, number)
    c.drawRightString(width - 20 * mm, y - 7 * mm, f"Date: {data['date']}")

    y -= 22 * mm
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20 * mm, y, "Bill to:")
    c.setFont("Helvetica", 11)
    c.drawString(20 * mm, y - 6 * mm, data["client_name"])
    if data["client_email"]:
        c.setFont("Helvetica", 10)
        c.drawString(20 * mm, y - 12 * mm, data["client_email"])

    y -= 28 * mm
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20 * mm, y, "Description")
    c.drawRightString(120 * mm, y, "Qty")
    c.drawRightString(145 * mm, y, "Unit price")
    c.drawRightString(width - 20 * mm, y, "Amount")
    c.line(20 * mm, y - 2 * mm, width - 20 * mm, y - 2 * mm)

    total = 0.0
    y -= 8 * mm
    c.setFont("Helvetica", 10)
    for item in data["items"]:
        amount = item["quantity"] * item["unit_price"]
        total += amount
        c.drawString(20 * mm, y, item["description"][:60])
        c.drawRightString(120 * mm, y, f"{item['quantity']:g}")
        c.drawRightString(145 * mm, y, money(item["unit_price"], data["currency"]))
        c.drawRightString(width - 20 * mm, y, money(amount, data["currency"]))
        y -= 7 * mm

    y -= 3 * mm
    c.line(120 * mm, y + 2 * mm, width - 20 * mm, y + 2 * mm)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20 * mm, y - 5 * mm, "Total due:")
    c.drawRightString(width - 20 * mm, y - 5 * mm, money(total, data["currency"]))

    c.setFont("Helvetica", 9)
    c.drawString(20 * mm, 20 * mm,
                 "Thank you for your business. Payment due within 14 days.")
    c.showPage()
    c.save()
    return total


def main():
    parser = argparse.ArgumentParser(
        description="Generate one PDF invoice per invoice_number in a CSV file.")
    parser.add_argument("csv_file", help="Input CSV file")
    parser.add_argument("out_dir", help="Folder to write the PDF invoices into")
    parser.add_argument("--business", default="Your Business",
                        help="Business name shown on the invoice")
    args = parser.parse_args()

    try:
        invoices = read_invoices(args.csv_file)
    except (OSError, ValueError) as e:
        print(f"Error: {e}")
        return 1

    os.makedirs(args.out_dir, exist_ok=True)
    grand_total = 0.0
    for number, data in invoices.items():
        path = os.path.join(args.out_dir, f"{number}.pdf")
        total = write_invoice_pdf(path, number, data, args.business)
        grand_total += total
        print(f"{number}.pdf  ({data['client_name']}, "
              f"{money(total, data['currency'])})")

    print(f"\nWrote {len(invoices)} invoice(s) to {args.out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

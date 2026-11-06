# Spreadsheets & Google Apps Script

## Workbooks (open in Excel, LibreOffice, or Google Sheets)

- **Business_Automation_Dashboard.xlsx** — Tasks, Invoices, and a Summary
  sheet with live formulas. Edit the Tasks and Invoices sheets; the Summary
  updates itself. Sample data is included — replace it with your own.
- **Profit_Calculator.xlsx** — Calculator sheet (edit the yellow cells:
  orders per month, price, other revenue, other costs) plus a Scenarios
  sheet at 10 / 20 / 50 / 100 orders per month. Gumroad fees use the
  direct-sale rate: 12.9% + $0.80 per order.

## Google Apps Script snippets (.gs)

These are snippets you paste into the Apps Script editor in Google Sheets
(Extensions > Apps Script). They do nothing on their own and only run
inside Google Sheets. Each file explains its own setup at the top.

- **auto_sort_sheet.gs** — adds a "Sort" menu to sort by column A or B.
- **duplicate_finder.gs** — highlights duplicate values in a selection.
- **email_summary.gs** — emails you a daily list of open tasks (set a
  time-driven trigger after pasting; edit RECIPIENT first).
- **dashboard_updater.gs** — refreshes a "Dashboard" sheet with live
  counts from the Tasks and Invoices sheets.

All four files were syntax-checked with Node.js before shipping.

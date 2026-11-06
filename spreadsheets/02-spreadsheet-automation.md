# AI Automation & Software Toolkit
## Part 2: Spreadsheet Automation & Google Apps Scripts (`02-spreadsheet-automation.md`)

This document contains two complete, cell-by-cell spreadsheet workbook specifications (compatible with both **Google Sheets** and **Microsoft Excel**) and three complete **Google Apps Script (`.gs`)** automation files.

---

# Workbook A: Automated Invoice Tracker (`Invoice_Tracker_Workbook`)

This workbook uses two tabs (`Invoices` and `Monthly_Summary`) to track client billing, automatically flag overdue invoices, calculate days overdue, and roll up monthly paid and outstanding totals.

## Tab 1: `Invoices` (Data Entry & Live Status Formulas)

### Column Headers (Row 1)
Enter these exact headers in cells `A1` through `K1`:
* **`A1`**: `Invoice ID`
* **`B1`**: `Client Name`
* **`C1`**: `Project Description`
* **`D1`**: `Issue Date`
* **`E1`**: `Due Date`
* **`F1`**: `Invoice Amount`
* **`G1`**: `Date Paid`
* **`H1`**: `Payment Status` *(Formula Column)*
* **`I1`**: `Overdue Flag` *(Formula Column)*
* **`J1`**: `Days Overdue` *(Formula Column)*
* **`K1`**: `Issue Month` *(Formula Helper Column for Monthly Totals)*

### Sample Data (Rows 2 to 4 — Manual Inputs in Columns A–G)
| Row | A (Invoice ID) | B (Client Name) | C (Project Description) | D (Issue Date) | E (Due Date) | F (Amount) | G (Date Paid) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2** | `INV-1001` | `Acme Studio` | `Website Copywriting` | `2026-01-10` | `2026-01-24` | `1500.00` | `2026-01-20` |
| **3** | `INV-1002` | `Bright Leaf Co` | `Q1 Retainer` | `2026-01-15` | `2026-01-29` | `2200.00` | *(leave blank)* |
| **4** | `INV-1003` | `North Star LLC` | `SEO Audit` | `2026-02-01` | `2026-12-31` | `850.00` | *(leave blank)* |

*(Note: Format Columns D, E, and G as Date `YYYY-MM-DD`, and Column F as Currency `$0.00`.)*

### Cell-by-Cell Formulas for Tab 1 (`Invoices`)
Enter these formulas into **Row 2**, then drag the fill handle down through **Row 100**:

* **Cell `H2` (`Payment Status`)**:
  ```excel
  =IF(ISBLANK(A2), "", IF(NOT(ISBLANK(G2)), "Paid", "Unpaid"))
  ```
  * **How it works:** If there is no Invoice ID in `A2`, it leaves the cell blank. Otherwise, it checks if `G2` (`Date Paid`) has a date entered. If yes, it outputs `"Paid"`; if blank, it outputs `"Unpaid"`.

* **Cell `I2` (`Overdue Flag`)**:
  ```excel
  =IF(ISBLANK(A2), "", IF(AND(H2="Unpaid", TODAY()>E2), "OVERDUE", "OK"))
  ```
  * **How it works:** Checks if the invoice is currently `"Unpaid"` AND today's date (`TODAY()`) is past the `Due Date` (`E2`). If both are true, it flags `"OVERDUE"`; otherwise, it displays `"OK"`.

* **Cell `J2` (`Days Overdue`)**:
  ```excel
  =IF(ISBLANK(A2), "", IF(I2="OVERDUE", TODAY()-E2, 0))
  ```
  * **How it works:** If `I2` is flagged as `"OVERDUE"`, it subtracts the Due Date (`E2`) from `TODAY()` to show the exact number of days late. Otherwise, it displays `0`. (Format Column J as a plain Number with `0` decimal places).

* **Cell `K2` (`Issue Month`)**:
  ```excel
  =IF(ISBLANK(D2), "", TEXT(D2, "YYYY-MM"))
  ```
  * **How it works:** Converts the `Issue Date` in `D2` into a clean `YYYY-MM` text string (e.g., `"2026-01"`) so the summary tab can group totals accurately by month.

---

## Tab 2: `Monthly_Summary` (Dashboard & Monthly Rollups)

### Top KPI Summary Block (Cells `A1:B5`)
Enter the labels in Column A and the live formulas in Column B:

* **Cell `A1`**: `Metric` | **Cell `B1`**: `Value`
* **Cell `A2`**: `Total Invoiced (All Time)`
  * **Cell `B2` Formula**:
    ```excel
    =SUM(Invoices!F2:F100)
    ```
* **Cell `A3`**: `Total Paid (Collected)`
  * **Cell `B3` Formula**:
    ```excel
    =SUMIF(Invoices!H2:H100, "Paid", Invoices!F2:F100)
    ```
* **Cell `A4`**: `Total Unpaid (Outstanding)`
  * **Cell `B4` Formula**:
    ```excel
    =SUMIF(Invoices!H2:H100, "Unpaid", Invoices!F2:F100)
    ```
* **Cell `A5`**: `Total Overdue Amount`
  * **Cell `B5` Formula**:
    ```excel
    =SUMIF(Invoices!I2:I100, "OVERDUE", Invoices!F2:F100)
    ```
* **Cell `A6`**: `Count of Overdue Invoices`
  * **Cell `B6` Formula**:
    ```excel
    =COUNTIF(Invoices!I2:I100, "OVERDUE")
    ```

### Monthly Breakdown Table (Rows 8 to 20)
Enter these headers in Row 8:
* **`A8`**: `Month (YYYY-MM)`
* **`B8`**: `Total Invoiced`
* **`C8`**: `Paid Total`
* **`D8`**: `Unpaid Total`
* **`E8`**: `Overdue Count`

Enter your target months in Column A (`A9` = `2026-01`, `A10` = `2026-02`, `A11` = `2026-03`, etc., formatted as Plain Text), then place these formulas in Row 9 and drag down:

* **Cell `B9` (`Total Invoiced` for Month `A9`)**:
  ```excel
  =SUMIF(Invoices!$K$2:$K$100, A9, Invoices!$F$2:$F$100)
  ```
* **Cell `C9` (`Paid Total` for Month `A9`)**:
  ```excel
  =SUMIFS(Invoices!$F$2:$F$100, Invoices!$K$2:$K$100, A9, Invoices!$H$2:$H$100, "Paid")
  ```
* **Cell `D9` (`Unpaid Total` for Month `A9`)**:
  ```excel
  =SUMIFS(Invoices!$F$2:$F$100, Invoices!$K$2:$K$100, A9, Invoices!$H$2:$H$100, "Unpaid")
  ```
* **Cell `E9` (`Overdue Count` for Month `A9`)**:
  ```excel
  =COUNTIFS(Invoices!$K$2:$K$100, A9, Invoices!$I$2:$I$100, "OVERDUE")
  ```

---

# Workbook B: Content Calendar with Auto-Status Counts (`Content_Calendar_Workbook`)

This single-sheet workbook (`Content_Calendar`) combines a top status counter bar (Rows 1–4) with a structured content schedule (starting at Row 6) that automatically calculates publication readiness and overdue drafts.

## Top Status Counter Block (Rows 1 to 4)

### Cell-by-Cell Layout & Live Formulas
* **Row 1 (Headers)**:
  * `A1`: `Total Planned`
  * `B1`: `Idea`
  * `C1`: `Drafting`
  * `D1`: `Ready`
  * `E1`: `Published`
  * `F1`: `Needs Attention (Late)`

* **Row 2 (Auto-Status Count Formulas)**:
  * **Cell `A2` (`Total Planned`)**:
    ```excel
    =COUNTA(A7:A200)
    ```
  * **Cell `B2` (`Idea` Count)**:
    ```excel
    =COUNTIF(E7:E200, "Idea")
    ```
  * **Cell `C2` (`Drafting` Count)**:
    ```excel
    =COUNTIF(E7:E200, "Drafting")
    ```
  * **Cell `D2` (`Ready` Count)**:
    ```excel
    =COUNTIF(E7:E200, "Ready")
    ```
  * **Cell `E2` (`Published` Count)**:
    ```excel
    =COUNTIF(E7:E200, "Published")
    ```
  * **Cell `F2` (`Needs Attention` Count)**:
    ```excel
    =COUNTIF(G7:G200, "LATE - UNPUBLISHED")
    ```

* **Row 3 (`Completion Rate %`)**:
  * **Cell `A3`**: `Publish Completion Rate`
  * **Cell `B3` Formula** (Format as Percentage `0.0%`):
    ```excel
    =IF(A2=0, 0, E2/A2)
    ```

---

## Content Schedule Table (Row 6 Headers & Row 7+ Data)

### Column Headers (Row 6)
* **`A6`**: `Publish Date`
* **`B6`**: `Channel` *(e.g., LinkedIn, Newsletter, Blog, YouTube)*
* **`C6`**: `Content Title / Hook`
* **`D6`**: `Content Pillar` *(e.g., Case Study, How-To, Industry News)*
* **`E6`**: `Status` *(Data Validation Dropdown: `Idea`, `Drafting`, `Ready`, `Published`)*
* **`F6`**: `Live URL`
* **`G6`**: `Schedule Health` *(Auto-Formula Column)*
* **`H6`**: `Days Until Publish` *(Auto-Formula Column)*

### Cell-by-Cell Formulas for Row 7 (Drag down through Row 200)

* **Cell `G7` (`Schedule Health`)**:
  ```excel
  =IF(ISBLANK(A7), "", IF(E7="Published", "Complete", IF(TODAY()>A7, "LATE - UNPUBLISHED", IF(AND(A7-TODAY()<=2, E7<>"Ready"), "URGENT DRAFT", "On Track"))))
  ```
  * **How it works:**
    1. If `A7` (`Publish Date`) is empty, stays blank.
    2. If `E7` is `"Published"`, shows `"Complete"`.
    3. If `Publish Date` is in the past and `Status` is not `"Published"`, flags `"LATE - UNPUBLISHED"`.
    4. If `Publish Date` is within 2 days and `Status` is not `"Ready"`, flags `"URGENT DRAFT"`.
    5. Otherwise, shows `"On Track"`.

* **Cell `H7` (`Days Until Publish`)**:
  ```excel
  =IF(ISBLANK(A7), "", IF(E7="Published", "-", A7-TODAY()))
  ```
  * **How it works:** Shows how many days remain until the scheduled date in `A7` (negative numbers indicate days past due), or `"-"` once published.

---

# Google Apps Script Snippets (`.gs` Files)

## Snippet 1: `auto_sort_by_date.gs`
Automatically sorts your active sheet by a date column whenever a cell in that column is edited, keeping row 1 headers frozen at the top.

```javascript
/**
 * ============================================================================
 * FILE: auto_sort_by_date.gs
 * DESCRIPTION: Automatically sorts a specified Google Sheet tab by its Date
 *              column whenever a date cell is edited, or via custom menu.
 *
 * 3-STEP SETUP GUIDE:
 * 1. Open your Google Sheet and click Extensions > Apps Script.
 * 2. Delete any code in Code.gs, paste this entire file, and update
 *    CONFIG.SHEET_NAME and CONFIG.DATE_COLUMN_INDEX below if needed.
 * 3. Click the Save icon (Ctrl+S / Cmd+S) and reload your Google Sheet.
 *    (An "Automation" menu will appear at the top, and edits to the date
 *    column will auto-sort immediately).
 * ============================================================================
 */

var CONFIG_SORT = {
  SHEET_NAME: 'Invoices',     // Exact name of the tab to sort
  HEADER_ROWS: 1,             // Number of header rows to ignore at the top
  DATE_COLUMN_INDEX: 4,       // Column number for dates (1 = Col A, 4 = Col D)
  SORT_ASCENDING: true        // true = oldest first, false = newest first
};

/**
 * Adds a manual trigger button to the Google Sheets toolbar on open.
 */
function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Automation Toolkit')
    .addItem('Sort Sheet by Date Now', 'sortSheetByDate')
    .addToUi();
}

/**
 * Built-in simple trigger that runs automatically when a user edits a cell.
 * @param {Object} e The edit event object provided by Google Sheets.
 */
function onEdit(e) {
  if (!e || !e.range) return;

  var sheet = e.range.getSheet();
  var editedRow = e.range.getRow();
  var editedCol = e.range.getColumn();

  // Only run if edit happened on the target sheet, below headers, in the date column
  if (
    sheet.getName() === CONFIG_SORT.SHEET_NAME &&
    editedRow > CONFIG_SORT.HEADER_ROWS &&
    editedCol === CONFIG_SORT.DATE_COLUMN_INDEX
  ) {
    sortSheetByDate();
  }
}

/**
 * Sorts all data rows below the header row by the configured date column.
 */
function sortSheetByDate() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(CONFIG_SORT.SHEET_NAME);

  if (!sheet) {
    SpreadsheetApp.getUi().alert(
      'Sheet "' + CONFIG_SORT.SHEET_NAME + '" not found. Check CONFIG_SORT.SHEET_NAME.'
    );
    return;
  }

  var lastRow = sheet.getLastRow();
  var lastCol = sheet.getLastColumn();

  // Need at least 2 data rows to sort
  if (lastRow <= CONFIG_SORT.HEADER_ROWS + 1 || lastCol === 0) {
    return;
  }

  var numDataRows = lastRow - CONFIG_SORT.HEADER_ROWS;
  var dataRange = sheet.getRange(
    CONFIG_SORT.HEADER_ROWS + 1,
    1,
    numDataRows,
    lastCol
  );

  dataRange.sort({
    column: CONFIG_SORT.DATE_COLUMN_INDEX,
    ascending: CONFIG_SORT.SORT_ASCENDING
  });
}
```

---

## Snippet 2: `flag_duplicate_rows.gs`
Scans a sheet for duplicate rows (either based on a key column like `Invoice ID` / `Email` or across the entire row), highlights duplicates in soft red, and writes `"DUPLICATE"` into an optional status note or alert summary.

```javascript
/**
 * ============================================================================
 * FILE: flag_duplicate_rows.gs
 * DESCRIPTION: Scans the active sheet for duplicate entries in a primary key
 *              column (e.g., Column A: Invoice ID or Email) and highlights
 *              duplicate rows in light red so you can review them safely.
 *
 * 3-STEP SETUP GUIDE:
 * 1. In your Google Sheet, go to Extensions > Apps Script.
 * 2. Paste this code into a new script file (or Code.gs) and adjust
 *    DUPLICATE_CONFIG.KEY_COLUMN if your unique ID is not in Column A (1).
 * 3. Save the script, select "flagDuplicateRows" from the toolbar dropdown at
 *    the top of the Apps Script editor, and click "Run" (authorize when asked).
 * ============================================================================
 */

var DUPLICATE_CONFIG = {
  HEADER_ROWS: 1,                   // Number of header rows at top of sheet
  KEY_COLUMN: 1,                    // Column to check (1 = Col A, 2 = Col B, etc.)
  HIGHLIGHT_COLOR: '#fce8e6',       // Soft light-red background for duplicates
  NORMAL_COLOR: '#ffffff'           // White background for unique rows
};

/**
 * Scans the currently active sheet and highlights rows with duplicate keys.
 */
function flagDuplicateRows() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var lastRow = sheet.getLastRow();
  var lastCol = sheet.getLastColumn();

  if (lastRow <= DUPLICATE_CONFIG.HEADER_ROWS || lastCol === 0) {
    SpreadsheetApp.getUi().alert('No data rows found to scan.');
    return;
  }

  var numRows = lastRow - DUPLICATE_CONFIG.HEADER_ROWS;
  var dataRange = sheet.getRange(
    DUPLICATE_CONFIG.HEADER_ROWS + 1,
    1,
    numRows,
    lastCol
  );
  var values = dataRange.getValues();

  // First pass: count occurrences of each normalized key
  var counts = {};
  for (var i = 0; i < values.length; i++) {
    var rawKey = values[i][DUPLICATE_CONFIG.KEY_COLUMN - 1];
    var normalizedKey = String(rawKey).trim().toLowerCase();
    if (normalizedKey !== '') {
      counts[normalizedKey] = (counts[normalizedKey] || 0) + 1;
    }
  }

  // Second pass: build background color matrix and count duplicates
  var backgrounds = [];
  var duplicateRowCount = 0;

  for (var r = 0; r < values.length; r++) {
    var cellValue = values[r][DUPLICATE_CONFIG.KEY_COLUMN - 1];
    var key = String(cellValue).trim().toLowerCase();
    var isDuplicate = key !== '' && counts[key] > 1;

    if (isDuplicate) {
      duplicateRowCount++;
    }

    var rowColors = [];
    for (var c = 0; c < lastCol; c++) {
      rowColors.push(
        isDuplicate
          ? DUPLICATE_CONFIG.HIGHLIGHT_COLOR
          : DUPLICATE_CONFIG.NORMAL_COLOR
      );
    }
    backgrounds.push(rowColors);
  }

  // Apply background colors in a single batch call for speed
  dataRange.setBackgrounds(backgrounds);

  SpreadsheetApp.getUi().alert(
    'Scan Complete: Found ' +
      duplicateRowCount +
      ' row(s) sharing a duplicate value in Column ' +
      DUPLICATE_CONFIG.KEY_COLUMN +
      '.'
  );
}
```

---

## Snippet 3: `send_weekly_email_summary.gs`
Reads your `Invoices` tab, calculates total paid, unpaid, and overdue invoices (listing each overdue client by name and amount), and emails a clean summary to your inbox.

```javascript
/**
 * ============================================================================
 * FILE: send_weekly_email_summary.gs
 * DESCRIPTION: Reads the "Invoices" sheet, calculates Paid, Unpaid, and
 *              Overdue totals, and emails a formatted weekly digest to you.
 *
 * 3-STEP SETUP GUIDE:
 * 1. Open your Google Sheet, click Extensions > Apps Script, and paste this
 *    code into a script file.
 * 2. Test it immediately by selecting "sendWeeklyInvoiceSummary" in the top
 *    bar and clicking "Run" (approve the email permission prompt).
 * 3. To automate it every Monday: click the "Triggers" (alarm clock) icon on
 *    the left sidebar > "+ Add Trigger" > choose "sendWeeklyInvoiceSummary",
 *    Event source: "Time-driven", Type: "Week timer", Day: "Every Monday".
 * ============================================================================
 */

var EMAIL_CONFIG = {
  SHEET_NAME: 'Invoices',
  RECIPIENT_EMAIL: '', // Leave blank to automatically email the Google account owner
  SUBJECT_PREFIX: '[Weekly Business Digest] Invoice & Cash Flow Summary'
};

/**
 * Reads invoice data and sends a clean plain-text + HTML email digest.
 */
function sendWeeklyInvoiceSummary() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(EMAIL_CONFIG.SHEET_NAME);

  if (!sheet) {
    throw new Error('Sheet "' + EMAIL_CONFIG.SHEET_NAME + '" was not found.');
  }

  var recipient =
    EMAIL_CONFIG.RECIPIENT_EMAIL || Session.getActiveUser().getEmail();
  if (!recipient) {
    throw new Error('Could not determine recipient email. Set EMAIL_CONFIG.RECIPIENT_EMAIL.');
  }

  var lastRow = sheet.getLastRow();
  if (lastRow <= 1) {
    return; // No invoice rows to report
  }

  // Read columns A through J (Invoice ID to Days Overdue)
  var data = sheet.getRange(2, 1, lastRow - 1, 10).getValues();

  var totalPaid = 0;
  var totalUnpaid = 0;
  var totalOverdue = 0;
  var overdueItems = [];

  for (var i = 0; i < data.length; i++) {
    var row = data[i];
    var invoiceId = String(row[0]).trim();
    if (!invoiceId) continue;

    var clientName = String(row[1]).trim();
    var amount = parseFloat(row[5]) || 0;
    var status = String(row[7]).trim();       // Column H: "Paid" or "Unpaid"
    var overdueFlag = String(row[8]).trim();  // Column I: "OVERDUE" or "OK"
    var daysOverdue = parseInt(row[9], 10) || 0;

    if (status.toLowerCase() === 'paid') {
      totalPaid += amount;
    } else {
      totalUnpaid += amount;
      if (overdueFlag.toUpperCase() === 'OVERDUE') {
        totalOverdue += amount;
        overdueItems.push(
          '- ' +
            invoiceId +
            ' | ' +
            clientName +
            ': $' +
            amount.toFixed(2) +
            ' (' +
            daysOverdue +
            ' days overdue)'
        );
      }
    }
  }

  var todayStr = Utilities.formatDate(
    new Date(),
    ss.getSpreadsheetTimeZone(),
    'yyyy-MM-dd'
  );

  var bodyLines = [
    'Weekly Invoice Summary (' + todayStr + ')',
    '==================================================',
    'Total Paid (Collected):     $' + totalPaid.toFixed(2),
    'Total Unpaid (Outstanding): $' + totalUnpaid.toFixed(2),
    'Total Overdue Amount:       $' + totalOverdue.toFixed(2),
    '',
    'Overdue Invoices Requiring Follow-Up (' + overdueItems.length + '):',
    '--------------------------------------------------'
  ];

  if (overdueItems.length === 0) {
    bodyLines.push('None! All unpaid invoices are within their due dates.');
  } else {
    bodyLines = bodyLines.concat(overdueItems);
  }

  bodyLines.push('');
  bodyLines.push('Open Tracker: ' + ss.getUrl());

  MailApp.sendEmail({
    to: recipient,
    subject: EMAIL_CONFIG.SUBJECT_PREFIX + ' - ' + todayStr,
    body: bodyLines.join('\n')
  });
}
```
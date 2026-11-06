/**
 * auto_sort_sheet.gs — Sort a sheet's data range by a column.
 *
 * HOW TO USE
 * 1. In Google Sheets: Extensions > Apps Script.
 * 2. Paste this code, save, and reload the sheet.
 * 3. A new "Sort" menu appears. Pick "Sort by column A" (or edit the
 *    column letter in the code below).
 * 4. The header row (row 1) is never sorted.
 *
 * This is a snippet you paste into the Apps Script editor. It only runs
 * inside Google Sheets; it does nothing on its own.
 */

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Sort')
    .addItem('Sort by column A (A-Z)', 'sortByColumnA')
    .addItem('Sort by column B (A-Z)', 'sortByColumnB')
    .addToUi();
}

function sortByColumn(column) {
  var sheet = SpreadsheetApp.getActiveSheet();
  var range = sheet.getDataRange();
  var lastRow = range.getLastRow();
  var lastCol = range.getLastColumn();
  if (lastRow < 3) {
    SpreadsheetApp.getUi().alert('Need at least 2 data rows (plus a header) to sort.');
    return;
  }
  // Keep row 1 (headers) fixed; sort rows 2..lastRow by the given column.
  sheet.getRange(2, 1, lastRow - 1, lastCol).sort(column);
}

function sortByColumnA() { sortByColumn(1); }
function sortByColumnB() { sortByColumn(2); }

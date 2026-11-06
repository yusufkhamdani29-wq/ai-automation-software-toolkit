/**
 * duplicate_finder.gs — Highlight duplicate values in a column.
 *
 * HOW TO USE
 * 1. In Google Sheets: Extensions > Apps Script.
 * 2. Paste this code, save, and reload the sheet.
 * 3. Select the cells you want to check (one column at a time works best).
 * 4. Use the "Duplicates" menu > "Highlight duplicates in selection".
 * 5. Duplicates are filled light red. Run "Clear highlighting" to undo.
 *
 * This is a snippet you paste into the Apps Script editor. It only runs
 * inside Google Sheets; it does nothing on its own.
 */

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Duplicates')
    .addItem('Highlight duplicates in selection', 'highlightDuplicates')
    .addItem('Clear highlighting', 'clearHighlighting')
    .addToUi();
}

function highlightDuplicates() {
  var range = SpreadsheetApp.getActiveRange();
  var values = range.getValues();
  // Highlight only the second (and later) occurrences, not the first.
  var firstSeen = {};
  var toHighlight = [];
  for (var r2 = 0; r2 < values.length; r2++) {
    for (var c2 = 0; c2 < values[r2].length; c2++) {
      var v2 = String(values[r2][c2]).trim();
      if (v2 === '') continue;
      if (firstSeen[v2]) {
        toHighlight.push(range.getCell(r2 + 1, c2 + 1));
      } else {
        firstSeen[v2] = true;
      }
    }
  }
  toHighlight.forEach(function(cell) { cell.setBackground('#F4CCCC'); });
  SpreadsheetApp.getUi().alert(toHighlight.length + ' duplicate cell(s) highlighted.');
}

function clearHighlighting() {
  var range = SpreadsheetApp.getActiveRange();
  range.setBackground(null);
}

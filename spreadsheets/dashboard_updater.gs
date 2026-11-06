/**
 * dashboard_updater.gs — Refresh a "Dashboard" sheet with live counts.
 *
 * HOW TO USE
 * 1. In Google Sheets: Extensions > Apps Script.
 * 2. Paste this code, save, and reload the sheet.
 * 3. Make sure your workbook has a sheet named "Tasks" (column D = status)
 *    and a sheet named "Invoices" (column C = amount, column D = status),
 *    plus an empty sheet named "Dashboard". Adjust the names and columns
 *    below if your sheets are different.
 * 4. Use the "Dashboard" menu > "Refresh dashboard".
 *
 * The script writes: total tasks, done tasks, open tasks, invoice count,
 * total invoiced, total paid, and total outstanding. It overwrites whatever
 * is in the Dashboard sheet, so keep that sheet for the dashboard only.
 * This is a snippet you paste into the Apps Script editor. It only runs
 * inside Google Sheets; it does nothing on its own.
 */

var TASKS_SHEET = 'Tasks';
var INVOICES_SHEET = 'Invoices';
var DASHBOARD_SHEET = 'Dashboard';

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Dashboard')
    .addItem('Refresh dashboard', 'refreshDashboard')
    .addToUi();
}

function countWhere(values, colIndex, match) {
  var n = 0;
  for (var i = 1; i < values.length; i++) {
    if (String(values[i][colIndex]).toLowerCase() === match) n++;
  }
  return n;
}

function sumWhere(values, amountCol, statusCol, match) {
  var total = 0;
  for (var i = 1; i < values.length; i++) {
    if (String(values[i][statusCol]).toLowerCase() === match) {
      total += Number(values[i][amountCol]) || 0;
    }
  }
  return total;
}

function refreshDashboard() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var tasks = ss.getSheetByName(TASKS_SHEET).getDataRange().getValues();
  var invoices = ss.getSheetByName(INVOICES_SHEET).getDataRange().getValues();
  var dash = ss.getSheetByName(DASHBOARD_SHEET);
  if (!dash) {
    dash = ss.insertSheet(DASHBOARD_SHEET);
  }
  dash.clear();

  var totalTasks = tasks.length - 1;
  var doneTasks = countWhere(tasks, 3, 'done');
  var totalInvoiced = 0;
  for (var i = 1; i < invoices.length; i++) {
    totalInvoiced += Number(invoices[i][2]) || 0;
  }
  var paid = sumWhere(invoices, 2, 3, 'paid');
  var outstanding = totalInvoiced - paid;

  var rows = [
    ['Metric', 'Value'],
    ['Total tasks', totalTasks],
    ['Tasks done', doneTasks],
    ['Tasks open', totalTasks - doneTasks],
    ['Invoices', invoices.length - 1],
    ['Total invoiced', totalInvoiced],
    ['Total paid', paid],
    ['Outstanding', outstanding],
    ['Last updated', new Date()],
  ];
  dash.getRange(1, 1, rows.length, 2).setValues(rows);
  dash.getRange(1, 1, 1, 2).setFontWeight('bold');
  SpreadsheetApp.getUi().alert('Dashboard refreshed.');
}

/**
 * email_summary.gs — Email yourself a daily summary of a sheet.
 *
 * HOW TO USE
 * 1. In Google Sheets: Extensions > Apps Script.
 * 2. Paste this code, save.
 * 3. Edit RECIPIENT, SHEET_NAME, and the column numbers below to match
 *    your sheet.
 * 4. Run sendDailySummary once by hand (Apps Script will ask for
 *    permission to send email as you — approve it).
 * 5. To automate: in the Apps Script editor, click the clock icon
 *    (Triggers) > Add Trigger > sendDailySummary > Time-driven > Day
 *    timer > pick an hour.
 *
 * The email lists rows whose Status column is not "done". Edit the
 * STATUS_COLUMN to match your sheet (1 = column A, 2 = column B, ...).
 * This is a snippet you paste into the Apps Script editor. It only runs
 * inside Google Sheets; it does nothing on its own.
 */

var RECIPIENT = 'you@example.com';   // <-- change this to your email
var SHEET_NAME = 'Tasks';            // <-- change this to your sheet name
var STATUS_COLUMN = 4;               // column with the status (D = 4)
var TASK_COLUMN = 2;                 // column with the task name (B = 2)

function sendDailySummary() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
  if (!sheet) {
    throw new Error('Sheet not found: ' + SHEET_NAME);
  }
  var data = sheet.getDataRange().getValues();
  var open = [];
  for (var i = 1; i < data.length; i++) {  // skip header row
    var status = String(data[i][STATUS_COLUMN - 1] || '').toLowerCase();
    if (status !== 'done' && status !== 'complete') {
      open.push(data[i][TASK_COLUMN - 1]);
    }
  }
  var subject = 'Daily summary: ' + open.length + ' open task(s)';
  var body = 'Open tasks in "' + SHEET_NAME + '":\n\n';
  open.forEach(function (task) { body += '- ' + task + '\n'; });
  if (open.length === 0) {
    body += '(none — everything is done.)\n';
  }
  MailApp.sendEmail(RECIPIENT, subject, body);
}

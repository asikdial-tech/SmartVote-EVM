function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Votes");
  var data = JSON.parse(e.postData.contents);
  sheet.appendRow([new Date(), data.voterID, data.candidate, "Confirmed"]);
  return ContentService.createTextOutput("Success").setMimeType(ContentService.MimeType.TEXT);
}

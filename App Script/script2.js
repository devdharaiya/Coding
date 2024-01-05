// This function copies all the zip codes from a Google Sheets spreadsheet into a new Google Document.
function copyAllZips() {
  // Get the spreadsheet and the sheet containing the zip codes.
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Zip Codes");
  // Get all the data in the sheet.
  var data = sheet.getDataRange().getValues();
  // Initialize an empty string to hold the output.
  var output = "";
  // Loop through all the rows in the sheet, starting with the second row (i.e., row 2).
  for (var i = 2; i < data.length; i++) {
    // Split the zip codes in column D into an array.
    var zipCodes = data[i][3].toString().split(",");
    // Loop through each zip code in the array.
    for (var j = 0; j < zipCodes.length; j++) {
      // Trim any whitespace from the zip code and remove any consecutive commas.
      var zipCode = zipCodes[j].trim().replace(/,{2,}/g, ",");
      // Add the zip code to the output string, followed by a comma.
      output += zipCode + ",";
    }
  }
  // Remove any consecutive commas from the output string.
  output = output.replace(/,{2,}/g, ",");
  // Remove any leading or trailing commas from the output string.
  output = output.replace(/(^,|,$)/g, "");
  // Get the current date
  var dateTime = new Date();
  // Format the date as MMM d:HH:mm
  var time = Utilities.formatDate(dateTime,"GMT+0530","MMM d HH:mm");
  // Create a new Google Document with the specified name.
  var docName = "Zip Codes - " + time;
  var doc = DocumentApp.create(docName);
  // Get the body of the new document.
  var body = doc.getBody();
  // Append the output string as a paragraph in the new document.
  body.appendParagraph(output);
  // Get the URL of the new document.
  var url = doc.getUrl();
  // Get the cell in the sheet where the hyperlink to the new document will be placed.
  var destination = sheet.getRange(2,8);
  // Clear any existing content in the cell.
  destination.clearContent();
  // Set the value of the cell to the URL of the new document as a hyperlink.
  destination.setValue(url);
  // Display an alert to the user to indicate that the zip codes have been added to the new document.
  SpreadsheetApp.getUi().alert("Zip codes added to document");
}

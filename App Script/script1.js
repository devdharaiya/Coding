function dataExtraction() {
  // Specify the name of the top-level folder
  var folderName = "#Fielding Managing";

  // Get the top-level folder using its name
  var folder = DriveApp.getFoldersByName(folderName).next();

  // Get all the subfolders of the top-level folder
  var subFolders = folder.getFolders();

  // Get the active sheet in the spreadsheet
  var sheet =
    SpreadsheetApp.getActiveSpreadsheet().getSheetByName("TER Backend");

  // Get the range of cells to be cleared
  var range = sheet.getRange(2, 1, sheet.getLastRow(), 3);

  // Clear the contents of the cells
  range.clearContent();
  //------------------------------------------------------------------------
  // Variables to keep track of the subfolder and its files
  var subFolder, files;

  // Variables to keep track of the file, its name, and its URL
  var file, fileName, fileUrl;

  // Variable to keep track of the name of the subfolder
  var subFolderName;

  // Variable to keep track of the row in the sheet where the data will be written
  var row = 2;

  // Loop through all the subfolders
  while (subFolders.hasNext()) {
    subFolder = subFolders.next();

    // Get the name of the subfolder
    subFolderName = subFolder.getName();

    // Get all the files in the subfolder
    files = subFolder.getFiles();

    // Loop through all the files
    while (files.hasNext()) {
      file = files.next();
      fileName = file.getName();
      fileUrl = file.getUrl();

      // Write the name of the subfolder in Column A
      sheet.getRange(row, 1).setValue(subFolderName);

      // Write the name of the file in Column C
      sheet.getRange(row, 2).setValue(fileName);

      // Write the URL of the file in Column D
      sheet.getRange(row, 3).setValue(fileUrl);

      // Move to the next row
      row++;
    }
  }
  //------------------------------------------------------------------------
}

/**
 * Synchronizes a Google Sheets spreadsheet with a Google Calendar.
 * Clears events on specified dates and creates new events based on data in the spreadsheet.
 */
function imsCalendar() {
  // Retrieve the active spreadsheet and get the "July" sheet
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("July");
 
  // Retrieve the calendar ID from cell B4 of the "July" sheet
  var calendarid = spreadsheet.getRange("B4").getValue();
 
  // Get the calendar object using the retrieved calendar ID
  var eventCal = CalendarApp.getCalendarById(calendarid);
  // Retrieve all the values from the data range of the sheet
  var data = spreadsheet.getDataRange().getValues();
  // Clear events on specified dates
  for (var i = 7; i < data.length; i++) {
    var del = data[i];
   
    // Retrieve the date to clear events from cell E (column 4)
    var dateToClear = new Date(del[4]);
   
    // Get all events for the specified date
    var eventsToClear = eventCal.getEventsForDay(dateToClear);
   
    // Delete each event for the specified date
    for (var y = 0; y < eventsToClear.length; y++) {
      eventsToClear[y].deleteEvent();
    }
  }
  // Create events from the data
  for (var x = 7; x < data.length; x++) {
    var shift = data[x];
   
    // Retrieve the start time from cell A (column 0)
    var startTime = new Date(shift[0]);
   
    // Retrieve the end time from cell B (column 1)
    var endTime = new Date(shift[1]);
   
    // Retrieve the subject from cell C (column 2)
    var subject = shift[2];
   
    // Retrieve the description from cell D (column 3)
    var description = shift[3];
    // Create a new event in the calendar with the retrieved details
    var event = eventCal.createEvent(subject, startTime, endTime);
   
    // Set the description for the event
    event.setDescription(description);
  }
}

# Import the SQLite library to handle database operations
import os
import sqlite3

# Define the path for the database file
path = '/workspaces/Coding/Python/Using Databases with Python/Worked Example - Counting Email in DB/emaildb.sqlite'
if os.path.exists(path):  # Check if the file already exists
    os.remove(path)  # If it exists, remove it

# Create a connection to the SQLite database file and a cursor object
conn = sqlite3.connect(path)
cur = conn.cursor()

# Drop the table 'EDB' if it already exists and create a new table 'EDB'
cur.execute('DROP TABLE IF EXISTS EDB')
cur.execute('CREATE TABLE EDB(Email TEXT, Freq INTEGER)')

# Prompt the user to enter a file name
fname = input("Enter File Name:")
if len(fname) < 1:  # If no file name is entered, use the default file path
    fname = '/workspaces/Coding/Python/Using Databases with Python/Worked Example - Counting Email in DB/mbox-short.txt'

# Open the file
fhandle = open(fname)
for line in fhandle:
    if line.startswith("From:"):  # Look for lines that start with 'From:'
        pieces = line.split()  # Split the line into words
        email = pieces[1]  # Extract the email address
        # Check if the email address is already in the 'EDB' table
        cur.execute('SELECT Freq FROM EDB WHERE Email = ?', (email,))
        row = cur.fetchone()  # Fetch one result from the query
        if row is None:  # If the email address is not in the table
            cur.execute('INSERT INTO EDB(Email, Freq) VALUES(?, 1)', (email,))  # Insert a new record with Freq 1
        else:  # If the email address is already in the table
            cur.execute('UPDATE EDB SET Freq = Freq + 1 WHERE Email = ?', (email,))  # Update the frequency count
        conn.commit()  # Commit the changes to the database

# Define the SQL query to retrieve the top 10 email addresses and their frequency, sorted by frequency in descending order
sqlstr = 'SELECT Email, Freq FROM EDB ORDER BY Freq DESC LIMIT 10'

# Execute the query and print the results
for row in cur.execute(sqlstr):
    print(row[0], ":", row[1])  # Print each email address and its frequency

# Close the cursor
cur.close()

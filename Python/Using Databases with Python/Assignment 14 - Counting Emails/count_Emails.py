# Import the SQLite library to handle database operations
import sqlite3

# Establish a connection to a SQLite database file 'email_db.sqlite' and create a cursor object
conn = sqlite3.connect('email_db.sqlite')
cur = conn.cursor()

# Create the table 'Counts' in the database
cur.execute('DROP TABLE IF EXISTS Counts')  # Drop the table if it already exists
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')  # Create a new table

# Prompt the user to enter a file name
fname = input('Enter File Name:')
if len(fname) < 1:  # If no file name is entered, use the default file path
    fname = 'Python/Using Databases with Python/Assignment 14 - Counting Emails/mbox.txt'
fhandle = open(fname)  # Open the file

# Process each line in the file
for line in fhandle:
    if line.startswith("From:"):  # Look for lines that start with 'From:'
        pieces = line.split()[1]  # Extract the email address from the line
        email = pieces.split('@')[1]  # Extract the domain name from the email address
        # Check if the domain name is already in the 'Counts' table
        cur.execute('SELECT count FROM Counts WHERE org = ?', (email,))
        row = cur.fetchone()  # Fetch one result from the query
        if row is None:  # If the domain name is not in the table
            cur.execute('INSERT INTO Counts(org, count) VALUES(?, 1)', (email,))  # Insert a new record with count 1
        else:  # If the domain name is already in the table
            cur.execute('UPDATE Counts SET count = count + 1 where org = ?', (email,))  # Update the count
conn.commit()  # Commit the changes to the database

# Retrieve and print the domain names and their counts, sorted by count in descending order
sqllist = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqllist):
    print(row[0], row[1])  # Print each domain name and its count

conn.close()  # Close the database connection
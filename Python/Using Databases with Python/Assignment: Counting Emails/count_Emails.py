# Import SQLite
import sqlite3
conn = sqlite3.connect('email_db.sqlite')
cur = conn.cursor()

# Create Table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

# Pulling Emails from File
fname = input('Enter File Name:')
if len(fname) < 1:
    fname = '/workspaces/Coding/Python/Using Databases with Python/Assignment: Counting Emails/mbox.txt'
fhandle = open(fname)

# Pushing Org ids to Database
for line in fhandle:
    if line.startswith("From:"):
        pieces = line.split()[1]
        email = pieces.split('@')[1]
        cur.execute('SELECT count FROM Counts WHERE org = ?', (email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts(org, count) VALUES(?, 1)',(email,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 where org = ?',(email,))
conn.commit()

#Print Emails listed in descending order based on count
sqllist = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in cur.execute(sqllist):
    print(row[0], row[1])

conn.close()
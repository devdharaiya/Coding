# import and connect to sqlite
import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS EDB')

# #Create Table
cur.execute('CREATE TABLE EDB(Email TEXT, Freq INTEGER  )')

# Read the file:
fname = input("Enter File Name:")
if len(fname) < 1:
    fname = '/workspaces/Coding/Python/Using Databases with Python/Worked Example: Counting Email in DB/mbox-short.txt'

# Push data in DataBase
fhandle = open(fname)
for line in fhandle:
    if line.startswith("From:"):
        pieces = line.split()
        email = pieces[1]
        cur.execute('SELECT Freq from EDB where Email = ?', (email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO EDB(Email, Freq) VALUES(?,1)',(email,))
        else:
            cur.execute('UPDATE EDB SET Freq = Freq + 1 where Email = ?',(email,))
        conn.commit()

sqlstr = 'SELECT Email, Freq from EDB ORDER BY Freq DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(row[0], ":", row[1])

cur.close()
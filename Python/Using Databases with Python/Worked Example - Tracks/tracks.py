import os
import sqlite3

path = '/workspaces/Coding/Python/Using Databases with Python/Worked Example - Tracks/Tracks.sqlite'
if os.path.exists(path):
    os.remove(path)

conn = sqlite3.connect('/workspaces/Coding/Python/Using Databases with Python/Worked Example - Tracks/Tracks.sqlite')
cur = conn.cursor()
cur.executescript('''
            DROP TABLE IF EXISTS Artist;
            DROP TABLE IF EXISTS Album;
            DROP TABLE IF EXISTS Tracks;
            DROP TABLE IF EXISTS Genre''')

cur.executescript('''CREATE TABLE Artist(
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
            );

            CREATE TABLE Album(
            id INTEGER PRIMARY KEY,
            head TEXT UNIQUE,
            artist TEXT
            );

            CREATE TABLE Tracks(
            id INTEGER PRIMARY KEY,
            title TEXT UNIQUE,
            album TEXT,
            genre TEXT,
            rating INTEGER, len INTEGER, count INTEGER
            );

            CREATE TABLE Genre(
            id INTEGER PRIMARY KEY,
            categ TEXT UNIQUE
            );
''')

fhandle = open('/workspaces/Coding/Python/Using Databases with Python/Worked Example - Tracks/tracks.csv')
for line in fhandle:
    pieces = line.split(',')
    if len(pieces) != 7: continue
    
    tracks = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]
    print(tracks, artist, album, count, rating, length, genre)

    cur.execute('INSERT OR IGNORE INTO Artist(name) VALUES(?)',(artist,))
    # cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    # artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album(head, artist) VALUES(?, ?)',(album, artist))
    # cur.execute('SELECT id from Album WHERE head = ?',(album,))
    # album_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre(categ) VALUES(?)',(genre,))
    # cur.execute('SELECT id from Genre WHERE categ = ?''',(genre,))
    # genre_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Tracks(title, album_id, genre, rating, len, count) VALUES(?, ?, ?, ?, ?, ?)',(tracks, album, genre, rating, length, count))
    
conn.commit()    
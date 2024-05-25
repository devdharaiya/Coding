import os
import sqlite3

# Define the path for the database file
path = '/workspaces/Coding/Python/Using Databases with Python/Assignment 15 - Tracks/Tracks.sqlite'
if os.path.exists(path):  # Check if the file already exists
    os.remove(path)  # If it exists, remove it

# Create a connection to the SQLite database file and a cursor object
conn = sqlite3.connect(path)
cur = conn.cursor()

# Execute multiple SQL commands to drop tables if they exist and create new tables
cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;
''')

# Create the tables: Artist, Album, Track, and Genre
cur.executescript('''
    CREATE TABLE Artist(
        id INTEGER NOT NULL UNIQUE PRIMARY KEY,
        name TEXT UNIQUE
    );

    CREATE TABLE Album(
        id INTEGER NOT NULL UNIQUE PRIMARY KEY,
        title TEXT UNIQUE,
        artist_id INTEGER
    );

    CREATE TABLE Track(
        id INTEGER NOT NULL UNIQUE PRIMARY KEY,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );

    CREATE TABLE Genre(
        id INTEGER NOT NULL UNIQUE PRIMARY KEY,
        name TEXT UNIQUE
    );
''')

# Open the CSV file containing the track data
fhandle = open('/workspaces/Coding/Python/Using Databases with Python/Assignment 15 - Tracks/tracks.csv')
for line in fhandle:
    pieces = line.split(',')  # Split each line by commas
    if len(pieces) != 7: continue  # Skip lines that do not have exactly 7 elements

    # Extract the data from each line
    track = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6].strip()  # Remove any extra whitespace from the genre

    # Insert or ignore the artist into the Artist table
    cur.execute('INSERT OR IGNORE INTO Artist(name) VALUES(?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]  # Get the artist_id

    # Insert or ignore the album into the Album table
    cur.execute('INSERT OR IGNORE INTO Album(title, artist_id) VALUES(?, ?)', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]  # Get the album_id

    # Insert or ignore the genre into the Genre table
    cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES(?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]  # Get the genre_id

    # Insert or ignore the track into the Track table
    cur.execute('INSERT OR IGNORE INTO Track(title, album_id, genre_id, rating, len, count) VALUES(?, ?, ?, ?, ?, ?)', 
                (track, album_id, genre_id, rating, length, count))

# Commit the changes to the database
conn.commit()

# Define the SQL query to retrieve track details joined with artist, album, and genre information
sqlstrng = '''
    SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
'''

# Execute the query and print the results
for row in cur.execute(sqlstrng):
    print(row)

# Close the cursor
cur.close()

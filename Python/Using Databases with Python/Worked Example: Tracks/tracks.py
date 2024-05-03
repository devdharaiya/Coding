import sqlite3
conn = sqlite3.connect('track.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS ARTIST',
            'DROP TABLE IF EXISTS ALBUM',
            'DROP TABLE IF EXISTS TRACKS',
            'DROP TABLE IF EXISTS GENRE')
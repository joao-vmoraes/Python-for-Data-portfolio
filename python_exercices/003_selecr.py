import sqlite3

from matplotlib.backend_bases import cursors

conn = sqlite3.connect('data/db.sqlite3')
cursor = conn.cursor()

cursor.execute(
    'SELECT * FROM customers '
    'WHERE id = "1" '
)

for row in cursor.fetchall():
    id, name, weight = row
    print(id, name, weight)

cursor.close()
conn.close()
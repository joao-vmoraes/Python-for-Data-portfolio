import sqlite3

conn = sqlite3.connect('data/db.sqlite3')
cursor = conn.cursor()

cursor.execute(
    'DELETE FROM customers '
    'WHERE id = "3" '
)
conn.commit()

cursor.execute(
    'SELECT * FROM customers'
)

for row in cursor.fetchall():
    print(row)


cursor.close()
conn.close()
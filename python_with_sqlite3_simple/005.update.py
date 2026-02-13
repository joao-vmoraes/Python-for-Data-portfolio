import sqlite3

conn =  sqlite3.connect('data/db.sqlite3')
cursor = conn.cursor()


cursor.execute(
    'UPDATE customers SET name = "Luiza", ' 
    'weight = 60 '
    'WHERE id = 1 '
)
conn.commit()


cursor.close()
conn.close()
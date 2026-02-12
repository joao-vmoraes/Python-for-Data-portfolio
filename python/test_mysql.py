import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="dados_db"
)

cursor = con.cursor()
cursor.execute("SELECT DATABASE();")

for x in cursor:
    print(x)

import os
import pymysql
import pymysql.cursors
import dotenv
import time

time.sleep(30)

dotenv.load_dotenv()

while True:
    try:
        conn = pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"), #type: ignore
            database=os.getenv("MYSQL_DATABASE")
        ) #type: ignore
        print("Conectado ao MySQL!")
        break
    except:
        print("Aguardando MySQL iniciar...")
        time.sleep(10)

cursor = conn.cursor()

with conn:
    with conn.cursor() as cursor:
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS customers ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(30) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
    conn.commit()

    with conn.cursor() as cursor:
        cursor.execute(
            'TRUNCATE TABLE customers'
        )
    conn.commit()

    with conn.cursor() as cursor:
        sql = ('INSERT INTO customers (nome, idade) '
            'VALUES '
            '(%s, %s) ' 
            )
        result = cursor.execute(sql, ('Carla', 30))
    print(result)
    conn.commit()

    with conn.cursor() as cursor:
        sql = ('INSERT INTO customers (nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) ' 
            )
        data = (
            {"name" : "Pedro" , "age": 30}, 
            {"name" : "Juan" , "age": 36}, 
            {"name" : "Mariana" , "age": 12},
            {"name" : "Juazeiro" , "age": 12},
            {"name" : "Pedrinho" , "age": 30}, 
        )
        cursor.executemany(sql, data) 
    conn.commit()

    
    with conn.cursor() as cursor:
        sql = (
            'DELETE FROM customers ' \
            'WHERE id = 4 '
        )
        cursor.execute(sql)
        conn.commit()
    
    with conn.cursor() as cursor:
        sql = (
            'SELECT * FROM customers ' \
            'WHERE id > 0'
        )
        cursor.execute(sql)
        
        for row in cursor.fetchall():
            print(row)

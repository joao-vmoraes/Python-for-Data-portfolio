import os
import pymysql
import pymysql.cursors
import dotenv

dotenv.load_dotenv('..')

conn = pymysql.connect(
    host= os.environ['MYSQL_HOST'],
    user= os.environ['MYSQL_USER'],
    password= os.environ['MYSQL_PASSWORD'],
    database= os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor
)
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

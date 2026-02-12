import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()

# cria a tabelka
cursor.execute(
    'CREATE TABLE IF NOT EXISTS customers'
    '(' 
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT, '
    'weight REAL'
    ')'
)
con.commit()

#registrar valores nas colunas da tabela
cursor.execute(
    'INSERT INTO customers (id, name, weight)'
    'VALUES (NULL, "Joao Vitor", 70)'
)
con.commit()

cursor.close()
con.close()
import sqlite3

def cria_tabela_e_insere_customer():

    con = sqlite3.connect('data/db.sqlite3')
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

if __name__ == '__main__':
    
    cria_tabela_e_insere_customer()
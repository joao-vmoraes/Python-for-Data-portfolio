import sqlite3


def insere_varios_customer_placeholder():
    conn = sqlite3.connect('data/db.sqlite3')
    cursor = conn.cursor()

    sql =(
        'INSERT INTO customers (name, weight) '
        'VALUES '
        '(?, ?)'
    )
    
    cursor.executemany(sql, [['Paulo', 82], ['Fatima', 53]])
    conn.commit()
    print(sql)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    insere_varios_customer_placeholder()
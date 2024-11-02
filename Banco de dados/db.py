import psycopg2


conn = psycopg2.connect("dbname=database-python host=localhost user=postgres password=0303 port=5432")
cur = conn.cursor()


def criar_tabela(conn, cur):
    cur.execute("CREATE TABLE IF NOT EXISTS clientes (id serial PRIMARY KEY, nome varchar, email varchar);")
    conn.commit()

def inserindo_registro(conn, cur):
    cur.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s);", ('Byanka', 'byanka@gmail.com'))
    conn.commit()


def atualizando_registro(conn, cur, nome, email, id):
    data = (nome, email, id)
    cur.execute("UPDATE clientes SET nome=%s, email=%s WHERE id=%s;", data)
    conn.commit()

def deletando_registro(conn, cur, id):
    cur.execute("DELETE FROM clientes WHERE id=%s;", (id,))
    conn.commit()


def listar_clientes(cur):
    cur.execute("SELECT * FROM clientes;")
    clientes = cur.fetchall()
    for cliente in clientes:
        print(cliente)


criar_tabela(conn, cur)
#inserindo_registro(conn, cur)
atualizando_registro(conn, cur, 'Beatriz', 'beatriz@gmail.com', 3)
deletando_registro(conn, cur, 3)
listar_clientes(cur)
cur.close()
conn.close()

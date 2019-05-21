import sqlite3

conn = sqlite3.connect('shallownowschool.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE TB_ESTUDANTE(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        NOME VARCHAR(30) NOT NULL,
        ENDERECO TEXT NOT NULL,
        NASCIMENTO DATE NOT NULL,
        MATRICULA VARCHAR(12) NOT NULL
    );
""")

print("Tabela criada com sucesso.")

conn.close()

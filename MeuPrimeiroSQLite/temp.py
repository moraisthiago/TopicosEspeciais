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

cursor.execute("""
    INSERT INTO TB_ESTUDANTE(NOME, ENDERECO, NASCIMENTO, MATRICULA)
    VALUES(
        'Maria da Conceição', 'Rua da Paz', '2019-03-03', '201910010013'
    );
""")

conn.commit()

print("Inserido com sucesso!")

conn.close()

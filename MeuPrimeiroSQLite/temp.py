import sqlite3

conn = sqlite3.connect('shallownowschool.db')

cursor = conn.cursor()

cursor.execute("""
    INSERT INTO TB_ESTUDANTE(NOME, ENDERECO, NASCIMENTO, MATRICULA)
    VALUES(
        'Maria da Conceição', 'Rua da Paz', '2019-03-03', '201910010013'
    );
""")

conn.commit()

print("Inserido com sucesso!")

conn.close()

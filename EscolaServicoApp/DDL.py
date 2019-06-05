import sqlite3

conn = sqlite3.connect('ifpb.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE TB_ESCOLAS(
		 ID_ESCOLA INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		 NOME VARCHAR(45) NOT NULL,
		 LOGRADOURO VARCHAR(70) NOT NULL,
		 CIDADE VARCHAR(45) NOT NULL
		);

""")

cursor.execute("""

	CREATE TABLE TB_ALUNOS(
		ID_ALUNO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		NOME VARCHAR(45) NOT NULL,
		MATRICULA VARCHAR(12) NOT NULL,
		CPF VARCHAR(11) NOT NULL,
		NASCIMENTO DATE NOT NULL
		);

        """)

cursor.execute("""

	CREATE TABLE TB_CURSOS(

		ID_CURSO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		NOME VARCHAR(45) NOT NULL,
		TURNO VARCHAR(10) NOT NULL

		);

""")

cursor.execute("""

	CREATE TABLE TB_TURMAS(

		ID_TURMA INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		NOME VARCHAR(45) NOT NULL,
		CURSO VARCHAR(45) NOT NULL
		);

""")

cursor.execute("""

	CREATE TABLE TB_DISCIPLINAS(

		ID_DISCIPLINA INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		NOME VARCHAR(45) NOT NULL
		);

""")
print ("Tabelas criadas!")
conn.close()

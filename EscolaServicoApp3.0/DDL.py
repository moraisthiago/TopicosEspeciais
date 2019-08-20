import sqlite3

conn = sqlite3.connect('EscolaApp_versao2.db')

cursor = conn.cursor()

cursor.execute("""
    create table tb_endereco(
        id_endereco integer primary key autoincrement not null,
        logradouro varchar(65) not null,
        complemento varchar(45) not null,
        bairro varchar(45) not null,
        cep varchar(8) not null,
        numero integer not null
        );
""")

print("Tabela tb_endereço criada com sucesso.")

cursor.execute("""
    create table tb_campus(
        id_campus integer primary key autoincrement not null,
        sigla varchar(3) not null,
        cidade varchar(45) not null
        );
""")
print ("Tabela tb_campus criada com sucesso.")

cursor.execute("""
    create table tb_escola(
        id_escola integer primary key autoincrement not null,
        nome varchar(45) not null,
        fk_id_endereco integer not null,
        fk_id_campus integer not null
        );
""")
print("Tabela tb_escola criada com sucesso.")


cursor.execute("""
    create table tb_turno(
        id_turno integer primary key autoincrement not null,
        nome varchar(10) not null
        );
""")
print("Tabela tb_turno criada  com sucesso.")

cursor.execute("""
    create table tb_curso(
        id_curso integer primary key autoincrement not null,
        nome varchar(45) not null,
        fk_id_turno integer not null
        );
""")
print("Tabela tb_curso criada com sucesso.")

cursor.execute("""
    create table tb_aluno(
        id_aluno integer primary key  autoincrement not null,
        nome varchar(45) not null,
        matricula varchar(12) not null,
        cpf varchar(11) not null,
        nascimento date not null,
        fk_id_endereco integer not null,
        fk_id_curso integer not null
        );
""")

cursor.execute("""
    create table tb_turma(
        id_turma integer primary key autoincrement not null,
        nome varchar(45) not null,
        fk_id_curso integer not null
        );
""")
print("Tabela tb_turma criada com sucesso.")

cursor.execute("""
    create table tb_professor(
        id_professor integer primary key autoincrement not null,
        nome varchar(45) not null,
        fk_id_endereco integer not null
        );
""")
print("Tabela tb_professor criada com sucesso.")

cursor.execute("""
    create table tb_disciplina(
        id_disciplina integer primary key autoincrement not null,
        nome varchar(45) not null,
        fk_id_professor integer not null
        );
""")
print("Tabela id_disciplina criada com sucesso.")

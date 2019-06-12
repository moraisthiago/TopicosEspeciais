from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def show_list(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/escolas", methods=['GET'])
def getEscolas():

    conn = sqlite3.connect("ifpb.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM TB_ESCOLAS;
    """)
    
    escolas = []
    for linha in cursor.fetchall():
        escolas.append(show_list(cursor, linha))

    conn.close()

    return (jsonify(escolas))

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolaByID(id):

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_ESCOLAS WHERE ID_ESCOLA = ?;

    """, (id, ))

    escola = []
    for linha in cursor.fetchall():
        escola.append(show_list(cursor, linha))

    conn.close()

    return (jsonify(escola))

@app.route("/escola", methods=['POST'])
def setEscola():

    nome = request.form['nome']
    logradouro = request.form['logradouro']
    cidade = request.form['cidade']

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_ESCOLAS(NOME, LOGRADOURO, CIDADE)
        VALUES(?,?,?);

    """, (nome, logradouro, cidade, ))

    conn.commit()
    conn.close()

    return ("Cadastro realizado com sucesso!", 200)

@app.route("/alunos", methods=['GET'])
def getAlunos():

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_ALUNOS;

    """)

    alunos = []
    for linha in cursor.fetchall():
        alunos.append(show_list(cursor, linha))

    conn.close()

    return (jsonify(alunos))

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunoByID(id):

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_ALUNOS WHERE ID_ALUNO = ?;

    """, (id, ))

    aluno = []
    for linha in cursor.fetchall():
        aluno.append(show_list(cursor, linha))


    conn.close()

    return (jsonify(aluno))

@app.route("/aluno", methods=['POST'])
def setAlunos():

    nome = request.form['nome']
    matricula = request.form['matricula']
    cpf = request.form['cpf']
    nascimento = request.form['nascimento']

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_ALUNOS(NOME, MATRICULA, CPF, NASCIMENTO)
        VALUES(?,?,?,?);

    """, (nome, matricula, cpf, nascimento, ))

    conn.commit()
    conn.close()

    return ("Cadastro realizado com sucesso!", 200)

@app.route("/cursos", methods=['GET'])
def getCursos():

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_CURSOS;

    """)

    cursos = []
    for linha in cursor.fetchall():
        cursos.append(show_list(cursor, linha))

    conn.close()

    return (jsonify(cursos))

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursoByID(id):

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_CURSOS WHERE ID_CURSO = ?;

    """, (id, ))

    curso = []
    for linha in cursor.fetchall():
        curso.append(show_list(cursor, linha))

    conn.close()

    return (jsonify(curso))

@app.route("/curso", methods=['POST'])
def setCursos():

    nome = request.form['nome']
    turno = request.form['turno']

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_CURSOS(NOME, TURNO)
        VALUES(?, ?);

    """, (nome, turno, ))

    conn.commit()
    conn.close()

    return ("Cadastro realizado com sucesso!", 200)

@app.route("/turmas", methods=['GET'])
def getTurmas():

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_TURMAS;

    """)

    turmas = []
    for linha in cursor.fetchall():
        turmas.append(show_list(cursor, linha))

    conn.close()

    return (jsonify(turmas))

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmaByID(id):

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_TURMAS WHERE ID_TURMA = ?;

    """, (id, ))

    turma = []
    for linha in cursor.fetchall():
        turma.append(show_list(cursor, linha))

    conn.close()

    return (jsonify(turma))

@app.route("/turma", methods=['POST'])
def setTurmas():

    nome = request.form['nome']
    curso = request.form['curso']

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_TURMAS(NOME, CURSO)
        VALUES(?, ?);

    """, (nome, curso, ))

    conn.commit()
    conn.close()

    return ("Cadastro realizado com sucesso!", 200)

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_DISCIPLINAS;

    """)

    disciplinas = []
    for linha in cursor.fetchall():
        disciplinas.append(show_list(cursor, linha))

    conn.close()

    return(jsonify(disciplinas))

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinaByID(id):

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_DISCIPLINAS WHERE ID_DISCIPLINA = ?;

    """, (id, ))

    disciplina = []
    for linha in cursor.fetchall():
        disciplina.append(show_list(cursor, linha))

    conn.close()

    return(jsonify(disciplina))

@app.route("/disciplina", methods=['POST'])
def setDisciplinas():

    nome = request.form['nome']

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_DISCIPLINAS(NOME)
        VALUES(?);

    """, (nome, ))

    conn.commit()
    conn.close()

    return ("Cadastro realizado com sucesso!", 200)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)

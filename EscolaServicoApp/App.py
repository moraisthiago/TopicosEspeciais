from flask import Flask, request, jsonify
import logging

import sqlite3

app = Flask(__name__)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("escolaapp.log")
handler.setFormatter(formatter)

logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def show_list(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/escolas", methods=['GET'])
def getEscolas():
    logger.info("Listando escolas.")
    try:
        conn = sqlite3.connect("ifpb.db")

        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM TB_ESCOLAS;
        """)

        escolas = []
        for linha in cursor.fetchall():
            escolas.append(show_list(cursor, linha))

        conn.close()

    except:
        logger.error("Ocorreu um erro.")


    return (jsonify(escolas))

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolaByID(id):
    logger.info("Listando escola pelo id: {}" .format(id))

    try:
        conn = sqlite3.connect('ifpb.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM TB_ESCOLAS WHERE ID_ESCOLA = ?;

        """, (id, ))

        linha = cursor.fetchone()
        escola = []
        escola.append(show_list(cursor, linha))

        conn.close()

    except:
        logger.erro("Ocorreu um erro.")

    return (jsonify(escola))

@app.route("/escola", methods=['POST'])
def setEscola():

    escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']

    logger.info("Inserindo escola: \n Nome: {} \n Logradouro: {} \n Cidade: {}" .format(nome, logradouro, cidade))

    try:
        conn = sqlite3.connect('ifpb.db')

        cursor = conn.cursor()

        cursor.execute("""

            INSERT INTO TB_ESCOLAS(NOME, LOGRADOURO, CIDADE)
            VALUES(?,?,?);

        """, (nome, logradouro, cidade, ))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        escola['id_escola'] = id

    except:
        logger.error("Ocorreu um erro.")

    return (jsonify(escola))

@app.route("/escolas/<int:id>", methods=['PUT'])
def updateEscola():

    escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']

    logger.info("Atualizando escola: \n Nome: {} \n Logradouro: {} \n Cidade: {}" .format(nome, logradouro, cidade))

    try:
        conn = sqlite3.connect("ifpb.db")

        cursor.execute("""

            SELECT * FROM TB_ESCOLAS WHERE ID_ESCOLA = ?;

        """(id,))

        data = cursor.fetchone()

        if data is not None:

            cursor.execute("""

                UPDATE TB_ESCOLAS SET NOME=?, LOGRADOURO=?, CIDADE=? WHERE ID_ESCOLA=?;

            """(nome, logradouro, cidade, id))

            conn.commit()

        else:

            cursor.execute("""

                INSERT INTO TB_ESCOLAS(NOME, LOGRADOURO, CIDADE)
                VALUES(?,?,?)

            """(nome, logradouro, cidade))

            conn.commit()
            id = cursor.lastrowid
            escola['id_escola']

        conn.close()

    except:
        logger.error("Ocorreu um erro.")

    return(jsonify(escola))

@app.route("/alunos", methods=['GET'])
def getAlunos():

    logger.info("Listando alunos.")

    try:
        conn = sqlite3.connect('ifpb.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM TB_ALUNOS;

        """)

        alunos = []
        for linha in cursor.fetchall():
            alunos.append(show_list(cursor, linha))

        conn.close()

    except:
        logger.error("Ocorreu um erro.")

    return (jsonify(alunos))

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunoByID(id):
    logger.info("Listando aluno pelo id: {}" .format(id))

    try:
        conn = sqlite3.connect('ifpb.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM TB_ALUNOS WHERE ID_ALUNO = ?;

        """, (id, ))

        linha = cursor.fetchone()
        aluno = []
        aluno.append(show_list(cursor, linha))

        conn.close()

    except:
        logger.error("Ocorreuum erro.")

    return (jsonify(aluno))

@app.route("/aluno", methods=['POST'])
def setAlunos():

    aluno = request.get_json()
    nome = aluno['nome']
    matricula = aluno['matricula']
    cpf = aluno['cpf']
    nascimento = aluno['nascimento']

    logger.info("Inserindo aluno: \n Nome: {} \n Matricula: {} \n CPf: {} \n Nascimento: {}" .format(nome, matricula, cpf, aluno))

    try:
        conn = sqlite3.connect('ifpb.db')

        cursor = conn.cursor()

        cursor.execute("""

            INSERT INTO TB_ALUNOS(NOME, MATRICULA, CPF, NASCIMENTO)
            VALUES(?,?,?,?);

        """, (nome, matricula, cpf, nascimento, ))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        aluno['id_aluno'] = id

    except:
        logger.error("Ocorreu um erro.")

    return (jsonify(aluno))

@app.route("/alunos/<int:id>", methods=["PUT"])
def updateAluno():

    aluno = request.get_json()
    nome = aluno['nome']
    matricula = aluno['matricula']
    cpf = aluno['cpf']
    nascimento = aluno['nascimento']

    logger.info("Atualizando aluno: \n Nome: {} \n Matricula: {} \n CPf: {} \n Nascimento: {}" .format(nome, matricula, cpf, aluno))

    try:
        conn = sqlite3.connect('ifpb.db')
        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM TB_ALUNOS WHERE ID_ALUNO = ?;

        """(id,))

        data = cursor.fetchone()

        if data is not None:

            cursor.execute("""

                UPDATE TB_ALUNOS SET NOME = ?, MATRICULA = ?, CPF = ?, NASCIMENTO = ? WHERE ID_ALUNO = ?;
            """(nome, matricula, cpf, nascimento, id))

            conn.commit()

        else:

            cursor.execute("""

                INSERT INTO TB_ALUNOS(NOME, MATRICULA, CPF, NASCIMENTO)
                VALUES(?,?,?,?)

            """(nome, matricula, cpf, nascimento))

            conn.commit()
            id = cursor.lastrowid
            aluno['id_aluno'] = id

        conn.close()

    except:
        logger.error("Ocorreu um erro.")

    return jsonify(aluno)

@app.route("/cursos", methods=['GET'])
def getCursos():
    logger.info("Listando cursos.")

    try:
        conn = sqlite3.connect('ifpb.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM TB_CURSOS;

        """)

        cursos = []
        for linha in cursor.fetchall():
            cursos.append(show_list(cursor, linha))

        conn.close()

    except:
        logger.error("Ocorreu um erro.")

    return (jsonify(cursos))

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursoByID(id):
    logging.info("Listando curso pelo id: {}" .format(id))

    try:
        conn = sqlite3.connect('ifpb.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM TB_CURSOS WHERE ID_CURSO = ?;

        """, (id, ))

        linha = cursor.fetchone()
        curso = []
        curso.append(show_list(cursor, linha))

        conn.close()

    except:
        logger.error("Ocorreu um erro.")

    return (jsonify(curso))

@app.route("/curso", methods=['POST'])
def setCursos():

    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']

    logger.info("Inserindo curso: \n Nome: {} \n Turno: {}" .format(nome, turno))

    try:
        conn = sqlite3.connect('ifpb.db')

        cursor = conn.cursor()

        cursor.execute("""

            INSERT INTO TB_CURSOS(NOME, TURNO)
            VALUES(?, ?);

        """, (nome, turno, ))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        curso['id_curso'] = id

    except:
        logger.error("Ocorreu um erro.")

    return (jsonify(curso))

@app.route("/cursos/<int:id>, methods=['PUT']")
def updateCurso():
    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']
    conn = sqlite3.connect('ifpb.db')

    logger.info("Atualizando curso: \n Nome: {} \n Turno: {}" .format(nome, turno))

    try:
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM TB_CURSOS WHERE ID_CURSO = ?;"""(id,))

        data = cursor.fetchone()

        if data is not None:
            cursor.execute("""UPDATE TB_CURSOS SET NOME=?, TURNO=? WHERE ID_CURSO = ?;"""(nome, turno, id))

            conn.commit()

        else:
            cursor.execute("""INSERT INTO TB_CURSOS(NOME, TURNO) VALUES(?,?)"""(nome, turno))
            conn.commit()
            id = cursor.lastrowid
            curso['id_curso'] = id

        conn.close()

    except:
        logger.error("Ocorreu um erro.")

    return jsonify()

@app.route("/turmas", methods=['GET'])
def getTurmas():
    logger.info("Listando turmas.")

    try:
        conn = sqlite3.connect('ifpb.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM TB_TURMAS;

        """)

        turmas = []
        for linha in cursor.fetchall():
            turmas.append(show_list(cursor, linha))

        conn.close()

    except:
        logger.error("Ocorreu um erro.")

    return (jsonify(turmas))

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmaByID(id):
    logger.info("Listando turma pelo id: {}" .format(id))

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_TURMAS WHERE ID_TURMA = ?;

    """, (id, ))

    linha = cursor.fetchone()
    turma = []
    turma.append(show_list(cursor, linha))

    conn.close()

    return (jsonify(turma))

@app.route("/turma", methods=['POST'])
def setTurmas():


    turma = request.get_json()
    nome = turma['nome']
    curso = turma['curso']

    logger.info("Inserindo turma: \n Nome: {} \n Curso: {}" .format(nome, curso))

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_TURMAS(NOME, CURSO)
        VALUES(?, ?);

    """, (nome, curso, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    turma['id_turma'] = id

    return (jsonify(turma))

@app.route("/turmas/<int:id>, methods=['PUT']")
def updateTurma():

    turma = request.get_json()

    nome = turma['nome']
    curso = turma['curso']

    logger.info("Atualizando turma: \n Nome: {} \n Curso: {}" .format(nome, curso))

    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_TURMAS WHERE ID_TURMA = ?;

        """(id,))

    data = cursor.fetchone()

    if data is not None:

        cursor.execute("""
            UPDATE TB_TURMAS SET NOME=?, CURSO=? WHERE  = ?;
        """(nome, curso, id))

        conn.commit()

    else:

        cursor.execute("""

            INSERT INTO TB_TURMAS(NOME, CURSO)
            VALUES(?,?)

        """(nome, curso))

        conn.commit()
        id = cursor.lastrowid
        turma['id_turma'] = id

    conn.close()

    return jsonify()

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():
    logger.info("Listando disciplinas.")

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
    logger.info("Listando disciplina pelo id: {}" .format(id))

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_DISCIPLINAS WHERE ID_DISCIPLINA = ?;

    """, (id, ))

    linha = cursor.fetchone()
    disciplina = []
    disciplina.append(show_list(cursor, linha))

    conn.close()

    return(jsonify(disciplina))

@app.route("/disciplina", methods=['POST'])
def setDisciplinas():

    disciplina = request.get_json()
    nome = disciplina['nome']

    logger.info("Inserindo disciplina: \n Nome: {}" .format(nome))

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_DISCIPLINAS(NOME)
        VALUES(?);

    """, (nome, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    disciplina['id_disciplina'] = id

    return (jsonify(disciplina))

@app.route("/disciplinas/<int:id>, methods=['PUT']")
def updateDisciplina():

    disciplina = request.get_json()
    nome = disciplina['nome']

    logger.info("Atualizando disciplina: \n Nome: {}" .format(nome))

    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_DISCIPLINAS WHERE ID_DISCIPLINA = ?;

    """(id,))

    data = cursor.fetchone()

    if data is not None:

        cursor.execute("""

            UPDATE TB_DISCIPLINAS SET NOME=? WHERE ID_DISCIPLINA = ?;
        """(nome, ))

        conn.commit()

    else:

        cursor.execute("""

            INSERT INTO TB_DISCIPLINAS(NOME)
            VALUES(?)

        """(nome, ))

        conn.commit()
        id = cursor.lastrowid
        disciplina['id_disciplina'] = id

    conn.close()

    return jsonify()

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)

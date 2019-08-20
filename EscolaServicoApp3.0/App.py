from flask import Flask, request, jsonify
import sqlite3
import logging
from flask_json_schema import JsonSchema, JsonValidationError


app = Flask(__name__)
schema = JsonSchema(app)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("escolaAPP.log")
handler.setFormatter(formatter)
logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)

endereco_schema = {
    'required' : ['logradouro', 'complemento','bairro', 'cep', 'numero'],
    'properties':{
    'logradouro':{'type':'string'},
    'complemento':{'type':'string'},
    'bairro':{'type':'string'},
    'cep':{'type':'string'},
    "numero":{'type':'string'}
    }
}

campus_schema = {

    'required':['sigla','cidade'],
    'properties':{
    'sigla':{'type':'string'},
    'cidade':{'type':'string'}
    }
}

escola_schema = {
    'required': ['nome', 'fk_id_endereco', 'fk_id_campus'],
    'properties':{
    'nome':{'type':'string'},
    'fk_id_endereco':{'type':'string'},
    'fk_id_campus':{'type':'string'}
    }
}

turno_schema = {
    'required': ['nome'],
    'properties':{
    'nome':{'type':'string'}
    }
}

curso_schema = {
    'required':['nome', 'fk_id_turno'],
    'properties':{
    'nome':{'type':'string'},
    'fk_id_turno':{'type':'string'}
    }
}

aluno_schema = {
    'required':['nome','matricula', 'cpf', 'nascimento', 'fk_id_endereco','fk_id_curso'],
    'properties':{
    'nome':{'type':'string'},
    'matricula':{'type':'string'},
    'cpf':{'type':'string'},
    'nascimento':{'type':'string'},
    'fk_id_endereco':{'type':'string'},
    'fk_id_curso':{'type':'string'}
    }
}

turma_schema = {
    'required': ['nome','fk_id_curso'],
    'properties':{
    'nome':{'type':'string'},
    'fk_id_curso':{'type':'string'}
    }
}

professor_schema ={
    'required': ['nome','fk_id_endereco'],
    'properties':{
    'nome':{'type':'string'},
    'fk_id_endereco':{'type':'string'}
    }
}

disciplina_schema = {
    'required':['nome','fk_id_endereco'],
    'properties':{
    'nome':{'type':'string'},
    'fk_id_endereco':{'type':'string'}
    }
}

@app.route("/enderecos", methods = ['GET'])
def getEndereco():

    logger.info("Listando endereços.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()

        cursor.execute("""
                select * from tb_endereco;
        """)
        enderecos = []

        for linha in cursor.fetchall():

            enderecos.append(dict_factory(linha, cursor))

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(enderecos))

@app.route("/enderecos/<int:id>", methods= ['GET'])
def getEnderecoById(id):

    logger.info("Listando endereço pelo seu Id.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM tb_endereco WHERE id_endereco = ?;

        """, (id, ))


        linha = cursor.fetchone()
        endereco = []
        endereco.append(dict_factory(linha,cursor))

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(endereco))

@app.route("/endereco", methods= ['POST'])
@schema.validate(endereco_schema)
def setEndereco():

    logger.info("Buscando dados do endereco.")

    enderecoJson = request.get_json()
    logradouro = enderecoJson['logradouro']
    complemento = enderecoJson['complemento']
    bairro = enderecoJson['bairro']
    cep = enderecoJson['cep']
    numero = enderecoJson['numero']


    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_endereco(logradouro, complemento, bairro, cep, numero)
            VALUES(?, ?, ?, ?, ?);
        """, (logradouro, complemento, bairro, cep, numero))
        conn.commit()
        conn.close()

    except(sqlite3.Error):
        logger.error("Ops,aconteceu um erro.")
        logger.error(sqlite3.Error)

    id = cursor.lastrowid
    enderecoJson["id_endereco"] = id

    return jsonify(enderecoJson)

@app.route("/endereco/<int:id>", methods=['PUT'])
def updateEndereco():

    logger.info("Atualizando dados do endereço.")

    enderecoJson = request.get_json()
    logradouro = enderecoJson['logradouro']
    complemento = enderecoJson['complemento']
    bairro = enderecoJson['bairro']
    cep = enderecoJson['numero']
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""

            SELECT * FROM tb_endereco WHERE id_endereco = ?;

        """(id,))

        data = cursor.fetchone()

        if data is not None:

            cursor.execute("""

                UPDATE tb_endereco SET logradouro=?, complemento=?, bairro=?, cep=?, numero=? WHERE id_endereco=?;

            """(logradouro, complemento, bairro, cep, numero, id))

            conn.commit()

        else:

            cursor.execute("""

                INSERT INTO tb_endereco(logradouro, complemento, bairro, cep, numero)
                VALUES(?,?,?,?,?)

            """(logradouro, complemento, bairro, cep, numero))

            conn.commit()
            id = cursor.lastrowid
            endereco['id_endereco']= id

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return(jsonify(enderecoJson))


@app.route("/campi", methods = ['GET'])
def getCampus():

    logger.info("Listando campus.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()

        cursor.execute("""
                select * from tb_campus;
        """)
        campus = []

        for linha in cursor.fetchall():

            campus.append(dict_factory(linha, cursor))

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(campus))

@app.route("/campi/<int:id>", methods= ['GET'])
def getCampusById(id):

    logger.info("Listando campus pelo seu Id.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM tb_campus WHERE id_campus = ?;

        """, (id, ))


        linha = cursor.fetchone()
        campus = []
        campus.append(dict_factory(linha,cursor))

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(campus))

@app.route("/campus", methods= ['POST'])
@schema.validate(campus_schema)
def setCampus():

    logger.info("Buscando dados do campus.")

    campusJson = request.get_json()
    sigla = campusJson['sigla']
    cidade = campusJson['cidade']

    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_campus(sigla, cidade)
            VALUES(?, ?);
        """, (sigla, cidade))
        conn.commit()
        conn.close()

    except(sqlite3.Error):
        logger.error("Ops,aconteceu um erro.")
        logger.error(sqlite3.Error)

    id = cursor.lastrowid
    campusJson["id_campus"] = id

    return jsonify(campusJson)

@app.route("/campus/<int:id>", methods=['PUT'])
def updateCampus():

    logger.info("Atualizando dados do campus.")

    campusJson = request.get_json()
    sigla = campusJson['sigla']
    cidade = campusJson['cidade']

    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""

            SELECT * FROM tb_campus WHERE id_campus = ?;

        """(id,))

        data = cursor.fetchone()

        if data is not None:

            cursor.execute("""

                UPDATE tb_campus SET sigla=?, cidade=? WHERE id_campus=?;

            """(sigla,cidade, id))

            conn.commit()

        else:

            cursor.execute("""

                INSERT INTO tb_campus(sigla, cidade)
                VALUES(?,?)

            """(sigla, cidade))

            conn.commit()
            id = cursor.lastrowid
            campus['id_campus']

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return(jsonify(campusJson))

@app.route("/escolas", methods = ['GET'])
def getEscola():

    logger.info("Listando escolas.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()

        cursor.execute("""
                select * from tb_escola;
        """)
        escola = []

        for linha in cursor.fetchall():

            escola.append(dict_factory(linha, cursor))

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(escola))

@app.route("/escola/<int:id>", methods= ['GET'])
def getEscolaById(id):

    logger.info("Listando escola pelo seu Id.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM tb_escola WHERE id_escola = ?;

        """, (id, ))


        linha = cursor.fetchone()
        escola = []
        escola.append(dict_factory(linha,cursor))

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(escola))

@app.route("/escola", methods= ['POST'])
@schema.validate(escola_schema)
def setEscola():

    logger.info("Buscando dados da escola.")

    escolaJson = request.get_json()
    nome = escolaJson['nome']
    fk_id_endereco = escolaJson['fk_id_endereco']
    fk_id_campus = escolaJson['fk_id_campus']

    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_escola(nome, fk_id_endereco, fk_id_campus)
            VALUES(?, ?, ?);
        """, (nome, fk_id_endereco, fk_id_campus))
        conn.commit()
        conn.close()

    except(sqlite3.Error):
        logger.error("Ops,aconteceu um erro.")
        logger.error(sqlite3.Error)

    id = cursor.lastrowid
    escolaJson["id_escola"] = id

    return jsonify(escolaJson)

@app.route("/escolas/<int:id>", methods=['PUT'])
def updateEscola():

    logger.info("Atualizando dados da escola.")

    escolaJson = request.get_json()
    nome = escolaJson['nome']
    fk_id_endereco = escolaJson['fk_id_endereco']
    fk_id_campus = escolaJson['fk_id_campus']

    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""

            SELECT * FROM tb_escola WHERE id_escola = ?;

        """(id,))

        data = cursor.fetchone()

        if data is not None:

            cursor.execute("""

                UPDATE tb_escola SET nome=?, fk_id_endereco=?, fk_id_campus=? WHERE id_escola=?;

            """(nome, fk_id_endereco, fk_id_campus, id))

            conn.commit()

        else:

            cursor.execute("""

                INSERT INTO tb_escola(nome, fk_id_endereco, fk_id_campus)
                VALUES(?,?,?)

            """(nome, fk_id_endereco, fk_id_campus))

            conn.commit()
            id = cursor.lastrowid
            escola['id_escola']= id

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return(jsonify(escolaJson))

@app.route("/turnos", methods = ['GET'])
def getTurnos():

    logger.info("Listando turnos.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()

        cursor.execute("""
                select * from tb_turno;
        """)
        turno = []

        for linha in cursor.fetchall():

            turno.append(dict_factory(linha, cursor))

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(turno))

@app.route("/turno/<int:id>", methods= ['GET'])
def getTurnoById(id):

    logger.info("Listando turno pelo seu Id.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM tb_turno WHERE id_turno = ?;

        """, (id, ))


        linha = cursor.fetchone()
        turno = []
        turno.append(dict_factory(linha,cursor))

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(turno))

@app.route("/turno", methods= ['POST'])
@schema.validate(turno_schema)
def setTurno():

    logger.info("Buscando dados do turno.")

    turnoJson = request.get_json()
    nome = turnoJson['nome']

    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_turno(nome)
            VALUES(?);
        """, (nome))
        conn.commit()
        conn.close()

    except(sqlite3.Error):
        logger.error("Ops,aconteceu um erro.")
        logger.error(sqlite3.Error)

    id = cursor.lastrowid
    turnoJson["id_turno"] = id

    return jsonify(turnoJson)

@app.route("/turnos/<int:id>", methods=['PUT'])
def updateTurno():

    logger.info("Atualizando dados do turno.")

    turnoJson = request.get_json()
    nome = turnoJson['nome']
    turno = Turno(nome)
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""

            SELECT * FROM tb_turno WHERE id_turno = ?;

        """(id,))

        data = cursor.fetchone()

        if data is not None:

            cursor.execute("""

                UPDATE tb_turno SET nome=? WHERE id_turno=?;

            """(nome, id))

            conn.commit()

        else:

            cursor.execute("""

                INSERT INTO tb_turno(nome)
                VALUES(?)

            """(nome))

            conn.commit()
            id = cursor.lastrowid
            turno['id_turno']= id

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return(jsonify(turnoJson))

@app.route("/cursos", methods = ['GET'])
def getCursos():

    logger.info("Listando cursos.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()

        cursor.execute("""
                select * from tb_curso;
        """)
        curso = []

        for linha in cursor.fetchall():

            curso.append(dict_factory(linha, cursor))

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(curso))

@app.route("/curso/<int:id>", methods= ['GET'])
def getCursoById(id):

    logger.info("Listando curso pelo seu Id.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM tb_curso WHERE id_curso = ?;

        """, (id, ))


        linha = cursor.fetchone()
        curso = []
        curso.append(dict_factory(linha,cursor))

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(curso))

@app.route("/curso", methods= ['POST'])
@schema.validate(curso_schema)
def setCurso():

    logger.info("Buscando dados do curso.")

    cursoJson = request.get_json()
    nome = cursoJson['nome']
    fk_id_turno = cursoJson['fk_id_endereco']


    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_curso(nome, fk_id_turno)
            VALUES(?, ?);
        """, (nome, fk_id_endereco))
        conn.commit()
        conn.close()

    except(sqlite3.Error):
        logger.error("Ops,aconteceu um erro.")
        logger.error(sqlite3.Error)

    id = cursor.lastrowid
    cursoJson["id_curso"] = id

    return jsonify(cursoJson)

@app.route("/cursos/<int:id>", methods=['PUT'])
def updateCurso():

    logger.info("Atualizando dados do curso.")

    cursoJson = request.get_json()
    nome = cursoJson['nome']
    fk_id_turno = cursoJson['fk_id_turno']
    curso = Curso(nome, fk_id_turno)
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""

            SELECT * FROM tb_curso WHERE id_curso = ?;

        """(id,))

        data = cursor.fetchone()

        if data is not None:

            cursor.execute("""

                UPDATE tb_curso SET nome=?, fk_id_turno=? WHERE id_curso=?;

            """(nome, fk_id_turno, id))

            conn.commit()

        else:

            cursor.execute("""

                INSERT INTO tb_curso(nome, fk_id_turno)
                VALUES(?,?)

            """(nome, fk_id_turno))

            conn.commit()
            id = cursor.lastrowid
            curso['id_curso']= id

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return(jsonify(cursoJson))

@app.route("/alunos", methods = ['GET'])
def getAlunos():

    logger.info("Listando alunos.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()

        cursor.execute("""
                select * from tb_aluno;
        """)
        aluno = []

        for linha in cursor.fetchall():

            aluno.append(dict_factory(linha, cursor))

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(aluno))

@app.route("/aluno/<int:id>", methods= ['GET'])
def getAlunoById(id):

    logger.info("Listando aluno pelo seu Id.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM tb_aluno WHERE id_aluno = ?;

        """, (id, ))


        linha = cursor.fetchone()
        aluno = []
        aluno.append(dict_factory(linha,cursor))

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(aluno))

@app.route("/aluno", methods= ['POST'])
@schema.validate(aluno_schema)
def setAluno():

    logger.info("Buscando dados do aluno.")

    alunoJson = request.get_json()
    nome = alunoJson['nome']
    matricula = alunoJson['matricula']
    cpf= alunoJson['cpf']
    nascimento = alunoJson['nascimento']
    fk_id_endereco = alunoJson['fk_id_endereco']
    fk_id_curso = alunoJson['fk_id_curso']


    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_aluno(nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso)
            VALUES(?,?,?,?,?,?);
        """, (nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso))
        conn.commit()
        conn.close()

    except(sqlite3.Error):
        logger.error("Ops,aconteceu um erro.")
        logger.error(sqlite3.Error)

    id = cursor.lastrowid
    alunoJson["id_aluno"] = id

    return jsonify(alunoJson)

@app.route("/alunos/<int:id>", methods=['PUT'])
def updateAluno():

    logger.info("Atualizando dados do aluno.")

    alunoJson = request.get_json()
    nome = alunoJson['nome']
    matricula = alunoJson['matricula']
    cpf= alunoJson['cpf']
    nascimento = alunoJson['nascimento']
    fk_id_endereco = alunoJson['fk_id_endereco']
    fk_id_curso = alunoJson['fk_id_curso']
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""

            SELECT * FROM tb_aluno WHERE id_aluno = ?;

        """(id,))

        data = cursor.fetchone()

        if data is not None:

            cursor.execute("""

                UPDATE tb_aluno SET nome=?, matricula=?, cpf=?, nascimento=?, fk_id_endereco=?, fk_id_curso WHERE id_aluno=?;

            """(nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso, id))

            conn.commit()

        else:

            cursor.execute("""

                INSERT INTO tb_aluno (nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso)
                VALUES(?,?,?,?,?,?)

            """(nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso))

            conn.commit()
            id = cursor.lastrowid
            alunoJson['id_aluno']= id

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return(jsonify(alunoJson))

@app.route("/turmas", methods = ['GET'])
def getTurmas():

    logger.info("Listando turmas.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()

        cursor.execute("""
                select * from tb_turma;
        """)
        turma = []

        for linha in cursor.fetchall():

            turma.append(dict_factory(linha, cursor))

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(turma))

@app.route("/turma/<int:id>", methods= ['GET'])
def getTurmaById(id):

    logger.info("Listando turma pelo seu Id.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM tb_turma WHERE id_turma = ?;

        """, (id, ))


        linha = cursor.fetchone()
        turma = []
        turma.append(dict_factory(linha,cursor))

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(turma))

@app.route("/turma", methods= ['POST'])
@schema.validate(turma_schema)
def setTurma():

    logger.info("Buscando dados da turma.")

    turmaJson = request.get_json()
    nome = turmaJson['nome']
    fk_id_curso = turmaJson['fk_id_curso']


    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_turma(nome, fk_id_curso)
            VALUES(?,?);
        """, (nome, fk_id_curso))
        conn.commit()
        conn.close()

    except(sqlite3.Error):
        logger.error("Ops,aconteceu um erro.")
        logger.error(sqlite3.Error)

    id = cursor.lastrowid
    turmaJson["id_turma"] = id

    return jsonify(turmaJson)

@app.route("/turmas/<int:id>", methods=['PUT'])
def updateTurma():

    logger.info("Atualizando dados da turma.")

    turmaJson = request.get_json()
    nome = turmaJson['nome']
    fk_id_curso = turmaJson['fk_id_curso']
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""

            SELECT * FROM tb_turma WHERE id_turma = ?;

        """(id,))

        data = cursor.fetchone()

        if data is not None:

            cursor.execute("""

                UPDATE tb_turma SET nome=?, fk_id_curso WHERE id_turma=?;

            """(nome, fk_id_curso, id))

            conn.commit()

        else:

            cursor.execute("""

                INSERT INTO tb_turma (nome, fk_id_curso)
                VALUES(?,?)

            """(nome, fk_id_curso))

            conn.commit()
            id = cursor.lastrowid
            turmaJson['id_turma']= id

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return(jsonify(turmaJson))


@app.route("/professores", methods = ['GET'])
def getProfessores():

    logger.info("Listando professores.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()

        cursor.execute("""
                select * from tb_professor;
        """)
        professor = []

        for linha in cursor.fetchall():

            professor.append(dict_factory(linha, cursor))

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(professor))

@app.route("/professor/<int:id>", methods= ['GET'])
def getProfessorById(id):

    logger.info("Listando professor pelo seu Id.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM tb_professor WHERE id_professor = ?;

        """, (id, ))


        linha = cursor.fetchone()
        professor = []
        professor.append(dict_factory(linha,cursor))

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(professor))

@app.route("/professor", methods= ['POST'])
@schema.validate(professor_schema)
def setProfessor():

    logger.info("Buscando dados do professor.")

    professorJson = request.get_json()
    nome = professorJson['nome']
    fk_id_endereco = professorJson['fk_id_endereco']


    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_professor(nome, fk_id_endereco)
            VALUES(?,?);
        """, (nome, fk_id_endereco))
        conn.commit()
        conn.close()

    except(sqlite3.Error):
        logger.error("Ops,aconteceu um erro.")
        logger.error(sqlite3.Error)

    id = cursor.lastrowid
    professorJson["id_professor"] = id

    return jsonify(professorJson)

@app.route("/professores/<int:id>", methods=['PUT'])
def updateProfessor():

    logger.info("Atualizando dados do professor.")

    professorJson = request.get_json()
    nome = professorJson['nome']
    fk_id_endereco = professorJson['fk_id_endereco']

    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""

            SELECT * FROM tb_professor WHERE id_professor = ?;

        """(id,))

        data = cursor.fetchone()

        if data is not None:

            cursor.execute("""

                UPDATE tb_professor SET nome=?, fk_id_endereco WHERE id_professor=?;

            """(nome, fk_id_endereco, id))

            conn.commit()

        else:

            cursor.execute("""

                INSERT INTO tb_professor (nome, fk_id_endereco)
                VALUES(?,?)

            """(nome, fk_id_endereco))

            conn.commit()
            id = cursor.lastrowid
            professor['id_professor']= id

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return(jsonify(professorJson))

@app.route("/disciplinas", methods = ['GET'])
def getDisciplinas():

    logger.info("Listando disciplinas.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()

        cursor.execute("""
                select * from tb_disciplina;
        """)
        disciplina = []

        for linha in cursor.fetchall():

            disciplina.append(dict_factory(linha, cursor))

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(disciplina))

@app.route("/disciplina/<int:id>", methods= ['GET'])
def getDisciplinaById(id):

    logger.info("Listandodisciplina pelo seu Id.")
    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM tb_disciplina WHERE id_disciplina = ?;

        """, (id, ))


        linha = cursor.fetchone()
        disciplina = []
        disciplina.append(dict_factory(linha,cursor))

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, aconteceu um erro.")
        logger.error(sqlite3.Error)

    return (jsonify(disciplina))

@app.route("/disciplina", methods= ['POST'])
@schema.validate(disciplina_schema)
def setDisciplina():

    logger.info("Buscando dados da disciplina.")

    disciplinaJson = request.get_json()
    nome = disciplinaJson['nome']
    fk_id_professor = disciplinaJson['fk_id_professor']


    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_disciplina(nome, fk_id_professor)
            VALUES(?,?);
        """, (nome, fk_id_professor))
        conn.commit()
        conn.close()

    except(sqlite3.Error):
        logger.error("Ops,aconteceu um erro.")
        logger.error(sqlite3.Error)

    id = cursor.lastrowid
    disciplinaJson["id_disciplina"] = id

    return jsonify(disciplinaJson)

@app.route("/disciplinas/<int:id>", methods=['PUT'])
def updateDisciplina():

    logger.info("Atualizando dados da disciplina.")

    disciplinaJson = request.get_json()
    nome = disciplinaJson['nome']
    fk_id_professor = disciplinaJson['fk_id_professor']

    try:
        conn = sqlite3.connect('EscolaApp_versao2.db')
        cursor = conn.cursor()
        cursor.execute("""

            SELECT * FROM tb_disciplina WHERE id_disciplina = ?;

        """(id,))

        data = cursor.fetchone()

        if data is not None:

            cursor.execute("""

                UPDATE tb_disciplina SET nome=?, fk_id_professor WHERE id_disciplina=?;

            """(nome, fk_id_professor, id))

            conn.commit()

        else:

            cursor.execute("""

                INSERT INTO tb_disciplina (nome, fk_id_professor)
                VALUES(?,?)

            """(nome, fk_id_professor))

            conn.commit()
            id = cursor.lastrowid
            disciplinaJson['id_disciplina']= id

        conn.close()
    except(sqlite3.Error):
        logger.error("Ops, Aconteceu um erro.")
        logger.error(sqlite3.Error)

    return(jsonify(disciplinaJson))


def dict_factory(linha, cursor):
    dicionario = {}
    for idx, col in enumerate(cursor.description):
        dicionario[col[0]] = linha[idx]
    return dicionario

@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]})


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)

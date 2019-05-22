from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("Olá Mundo! Estou aprendendo Flask", 200)

@app.route("/alunos", methods=['GET'])
def getAlunos():
    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM TB_ALUNO;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

    return("Executado!", 200)


@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunosByID(id):
    pass


@app.route("/cursos", methods=['GET'])
def getCursos():
    pass


@app.route("/cursos/<int:id>", methods=['GET'])
def getCursosByID(id):
    pass


@app.route("/turmas", methods=['GET'])
def getTurmas():
    pass


@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasByID(id):
    pass

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)

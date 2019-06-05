from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route("/json", methods=['GET'])
def testeJson():
    list = [{'a': 1, 'b': 2},{'a': 5, 'b': 10}]
    return jsonify(results = list)

@app.route("/escolas", methods=['GET'])
def getEscolas():

	conn = sqlite3.connect('ifpb.db')

	cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_ESCOLAS;

    """)

    for linha in cursor.fetchall():
        print(linha)

	conn.close()

	return ("Executado!", 200)

if (__name__ == '__main__'):
	app.run(host='0.0.0.0', debug = True, use_reloader = True)

from flask import Flask

app = Flask(__name__)

@app.route("/olamundo/<nome>")
def hello_world(nome):
    return ("Olá, {}! Estou aprendendo Flask. =)" .format(nome), 200)

@app.route("/noticias/<categoria>")
def getNoticias(categoria):
    pass

@app.route("/usuario/<int:id>")
def getUsuario(id):
    usuarios = [{1: "João"}, {2: "Maria"}, {3: "José"}]

    for usuario in usuarios:
        if (id in usuario.keys()):
            print (usuario[id])
            return (usuario[id], 200)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)

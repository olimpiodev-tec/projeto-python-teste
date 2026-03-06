from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!!!</h1>"

@app.route("/curso")
def curso():
    return "<h1>Técnico em Desenvolvimento de Sistemas</h1>"

@app.route("/cidade")
def cidade():
    return {
        "nome": "Piracicaba",
        "idade": 258,
        "habitantes": 440000,
        "fundacao": 1767
    }

@app.route("/musicas")
def musicas():
    return [
        "Patati, patata",
        "Meu lanchinho",
        "Bananas de pijamas",
        "Galinha pintadinha"
    ]


if __name__ == "__main__":
    app.run(debug=True)
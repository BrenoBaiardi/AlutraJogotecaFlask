from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


lista = [Jogo('Super Mario', 'Ação', 'SNES'),Jogo('Pokemon Gold', 'RPG', 'GBA')]

@app.route('/')
def index():
    return render_template('lista.html', titulo='JOGOS', jogos=lista)

@app.route("/novo")
def novo():
    return render_template("novo.html", titulo = "Novo Jogo")

@app.route("/criar",methods=['POST'])
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    lista.append(Jogo(nome, categoria, console))
    return redirect('/')

@app.route("/login")
def login():
    return render_template("login.html",titulo="login")

@app.route("/autenticar", methods=["POST"])
def autenticar():
    if "mestra" == request.form["senha"]:
        session["usuario_logado"] = request.form["usuario"]
        return redirect("/")
    else:
        return redirect("/login")

app.run(debug=True)
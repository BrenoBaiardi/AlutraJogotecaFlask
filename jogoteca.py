from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = "key"

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
    if "usuario_logado" not in session or session["usuario_logado"] == None:
        return redirect(url_for('login',proxima=url_for("novo")))
    return render_template("novo.html", titulo = "Novo Jogo")

@app.route("/criar",methods=['POST'])
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    lista.append(Jogo(nome, categoria, console))
    return redirect(url_for("index"))

@app.route("/login")
def login():
    proxima = request.args.get("proxima")
    return render_template("login.html", titulo="login",proxima=proxima)

@app.route("/autenticar", methods=["POST"])
def autenticar():
    if "mestra" == request.form["senha"]:
        session["usuario_logado"] = request.form["usuario"]
        flash(request.form["usuario"]+" login realizado")
        proxima_pagina = request.form["proxima"]
        return redirect(proxima_pagina)
    else:
        flash("login não realizado")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session["usuario_logado"] = None
    flash("Usuário deslogado")
    return redirect(url_for("index"))

app.run(debug=True)
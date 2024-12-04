from flask import flash, redirect, render_template, request
from main import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario != 'admin' or senha != 'senha123':
        if usuario == 'admin':
            flash('O login está correto', 'yellow-50')
        else:
            flash('O login não está correto', 'red-400')
        if senha == 'senha123':
            flash('A senha está correta', 'yellow-50')
        else:
            flash('A senha não está correta', 'red-400')

        return redirect('/login')
    else:
        return f'Os dados recebidos foram: usuário = {usuario} e senha = {senha}'


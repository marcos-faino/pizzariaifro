from main import app
from flask import render_template, redirect, flash, request


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario != 'admin' or senha != 'senha123':
        if usuario == 'admin':
            flash('O login está correto', 'green-50')
        else:
            flash('O login não está correto.', 'red-300')
        if senha == 'senha123':
            flash('A senha está correta', 'green-50')
        else:
            flash('A senha não está correta.', 'red-300')
        return redirect('/login')
    else:
        return (f'Os dados recebidos foram:\n'
                f'usuario: {usuario}\n'
                f'senha: {senha}')

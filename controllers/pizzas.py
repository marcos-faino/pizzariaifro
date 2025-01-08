from flask import render_template, request, redirect, flash, url_for
from flask import Blueprint

from models.Categoria import Categoria
from utils import db

from models.Pizza import Pizza

bp_pizzas = Blueprint('pizzas', __name__, template_folder='templates')


@bp_pizzas.route('/recovery')
def recovery():
    pizzas = Pizza.query.all()
    for p in pizzas:
        cat = Categoria.query.get(p.categoria_id)
        p.preco = str(cat.preco).replace('.', ',')
        p.categoria = cat
    return render_template('pizzas/pizzas_recovery.html', pizzas=pizzas)


@bp_pizzas.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        categorias = Categoria.query.all()
        return render_template('pizzas/pizzas_create.html', categorias=categorias)

    if request.method == "POST":
        sabor = request.form.get('sabor')
        ingredientes = request.form.get('ingredientes')
        categoria_id = request.form.get('categoria_id')
        pizza = Pizza(sabor, ingredientes, categoria_id)
        db.session.add(pizza)
        db.session.commit()
        return redirect(url_for('.recovery'))


@bp_pizzas.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if id and request.method == 'GET':
        pizza = Pizza.query.get(id)
        categorias = Categoria.query.all()
        return render_template('pizzas/pizzas_update.html', pizza=pizza, categorias=categorias)

    if request.method == 'POST':
        pizza = Pizza.query.get(id)
        pizza.sabor = request.form.get('sabor')
        pizza.ingredientes = request.form.get('ingredientes')
        pizza.categoria = request.form.get('categoria_id')

    db.session.add(pizza)
    db.session.commit()
    flash('Dados atualizados com sucesso!')
    return redirect(url_for('.recovery'))


@bp_pizzas.route('/delete', methods=['POST'])
@bp_pizzas.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id=None):
    if id and request.method == 'GET':
        pizza = Pizza.query.get(id)
        pizza.categoria = Categoria.query.get(pizza.categoria_id)
        return render_template('pizzas/pizzas_delete.html', pizza=pizza)
    else:
        flash('Escolha uma pizza a ser excluída')

    if request.method == 'POST':
        pizza = Pizza.query.get(request.form.get('id'))
        db.session.delete(pizza)
        db.session.commit()
        flash('Pizza excluída com sucesso')
        return redirect(url_for('.recovery'))

    return redirect(url_for('pizzas.recovery'))

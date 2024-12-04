from flask import render_template, request, redirect, flash, url_for
from flask import Blueprint
from utils import db

from models.Categoria import Categoria

bp_categorias = Blueprint('categorias', __name__, template_folder='templates')


@bp_categorias.route('/recovery')
def recovery():
    categorias = Categoria.query.all()
    for c in categorias:
        c.preco = str(c.preco).replace('.', ',')
    return render_template('categorias/categorias_recovery.html', categorias=categorias)


@bp_categorias.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('categorias/categorias_create.html')
 
    if request.method == "POST":
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        categoria = Categoria(descricao, preco.replace(",", "."))
        db.session.add(categoria)
        db.session.commit()
        #return redirect('/usuarios/recovery')
        return redirect(url_for('.recovery'))


@bp_categorias.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if id and request.method == 'GET':
        categoria = Categoria.query.get(id)
        return render_template('categorias/categorias_update.html', categoria=categoria)

    if request.method == 'POST':
        categoria = Categoria.query.get(id)
        categoria.descricao = request.form.get('descricao')
        categoria.preco = request.form.get('preco').replace(',', '.')

    db.session.add(categoria)
    db.session.commit()
    flash('Dados atualizados com sucesso!')
    return redirect(url_for('.recovery'))


@bp_categorias.route('/delete', methods=['POST'])
@bp_categorias.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id=None):
    if id and request.method == 'GET':
        categoria = Categoria.query.get(id)
        return render_template('categorias/categorias_delete.html', categoria=categoria)
    else:
        flash('Escolha uma categoria a ser excluída')

    if request.method == 'POST':
        categoria = Categoria.query.get(request.form.get('id'))
        db.session.delete(categoria)
        db.session.commit()
        flash('Categoria excluída com sucesso')
        return redirect(url_for('.recovery'))

    return redirect(url_for('categorias.recovery'))
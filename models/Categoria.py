from utils import db
from flask_migrate import Migrate

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50))
    preco = db.Column(db.Numeric(scale=2, precision=8))


    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco


    def __repr__(self):
        return self.descricao
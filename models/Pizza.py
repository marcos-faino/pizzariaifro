from utils import db


class Pizza(db.Model):
    __tablename__ = 'pizza'
    id = db.Column(db.Integer, primary_key=True)
    sabor = db.Column(db.String(80))
    ingredientes = db.Column(db.String(280))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)

    def __init__(self, sabor, ingredientes, categoria_id):
        self.sabor = sabor
        self.ingredientes = ingredientes
        self.categoria_id = categoria_id

    def __repr__(self):
        return self.sabor


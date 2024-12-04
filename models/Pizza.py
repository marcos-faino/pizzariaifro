from utils import db


class Pizza(db.Model):
    __tablename__ = 'pizza'
    id = db.Column(db.Integer, primary_key=True)
    sabor = db.Column(db.String(80))
    imagem = db.Column(db.String(280))
    ingredientes = db.Column(db.String(280))
    preco = db.Column(db.Float(8,2))

    def __init__(self, sabor, ingredientes, preco, imagem=None):
        self.sabor = sabor
        self.imagem = imagem
        self.ingredientes = ingredientes
        self.preco = preco

    def __repr__(self):
        return self.sabor


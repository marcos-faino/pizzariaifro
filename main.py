from flask import Flask
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Palavra-passe-muiiiiito-forte'

conexao = "sqlite:///pizzaria.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

import routes
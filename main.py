from flask import Flask, Blueprint
from utils import db
import os
from flask_migrate import Migrate
from controllers.usuarios import bp_usuarios
from controllers.categorias import bp_categorias


app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_meudb = os.getenv('DB_DATABASE')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}/{db_meudb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)

import routes
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
app.register_blueprint(bp_categorias, url_prefix='/categorias')
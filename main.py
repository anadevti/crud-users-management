from flask import Flask
from flask_migrate import Migrate

from database import db
from routes.home import home_route
from routes.client import client_route


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chave de segurança.'

conexao = 'mysql+pymysql://root:admin@localhost:3306/database'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(home_route)
app.register_blueprint(client_route, url_prefix='/clients')

app.run(debug=True)
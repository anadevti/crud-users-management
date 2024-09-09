from flask import Flask
from routes.home import home_route
from routes.client import client_route
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(client_route, url_prefix='/clients')

app.run(debug=True)
"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_basicauth import BasicAuth
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from api.utils import APIException, generate_sitemap
from api.models import db
from api.routes import api
from api.admin import setup_admin
from api.commands import setup_commands



ENV = os.getenv("FLASK_ENV")
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../public/')
app = Flask(__name__)
app.url_map.strict_slashes = False

# # set admin username and password
# app.config['BASIC_AUTH_USERNAME'] = os.getenv("BASIC_AUTH_USER")
# app.config['BASIC_AUTH_PASSWORD'] = os.getenv("BASIC_AUTH_PASS")

# # add flask-basicauth to flask app
# basic_auth = BasicAuth(app)

# # app.config['BASIC_AUTH_FORCE'] = True

# Database Configuration
db_url = os.getenv("DATABASE_URL")
# COMENTO ESTAS LINEAS PARA USAR SQLITE
# if db_url is not None:
#     app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
# else:

# AQUI USO SQLITE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    # app.config['SQLALCHEMY_CHARSET'] = 'utf8mb4'
    # mysql://user:pass@localhost/db?charset=utf8
    # sqlite:////tmp/test.db        # ORIGINAL CON EL BOILERPLATE
    # sqlite:///test.db         # Tener archivo al que poder acceder

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db, compare_type = True)
db.init_app(app)
# AQUI SE CREAN LAS TABLAS A PARTIR DE SQLITE, Y SE GENERA UNA CARPETA TMP Y UN ARCHIVO TEST.DB, DONDE DENTRO ESTA LA DB CON LAS TABLAS Y ES COMPARTIDA 
with app.app_context():
    db.create_all()

#  Configura la extensión Flask-JWT-Extended
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET') # ESTA PALABRA GENERA LOS TOKENS UNICOS Y NO SE DEBE COMPARTIR!!!           (# ¡Cambia las palabras "super-secret" por otra cosa!)
jwt = JWTManager(app)                                       # SE PONE EN ENV PARA NO SUBIRSE A LA NUBE Y QUE SEA SECRETA

# Allow CORS requests to this API
CORS(app)

# add the admin
setup_admin(app)

# add the admin
setup_commands(app)

# Add all endpoints form the API with a "api" prefix
app.register_blueprint(api, url_prefix='/api')

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    if ENV == "development":
        return generate_sitemap(app)
    return send_from_directory(static_file_dir, 'index.html')


# # PROTEGIENDO SOLO UNA RUTA
# @app.route('/admin/')
# @basic_auth.required
# def secret_view():
#     setup_admin(app)

#     return render_template('index.html')


###################################################################
# any other endpoint will try to serve it like a static file
@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = 'index.html'
    response = send_from_directory(static_file_dir, path)
    response.cache_control.max_age = 0 # avoid cache memory
    return response





# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)
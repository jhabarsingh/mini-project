from flask import Flask, Blueprint, request, jsonify
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from kubernetes import client, config


app = Flask(__name__)
CORS(app)

app.config.from_object('config')

jwt = JWTManager(app=app)

db = MongoEngine(app)

config.load_kube_config()
apps_v1 = client.AppsV1Api()
core_v1= client.CoreV1Api()

api = Blueprint('api',__name__,url_prefix='/api')


from app.auth.controllers import auth
api.register_blueprint(auth)

from app.user.controllers import user
api.register_blueprint(user)

from app.admin.controllers import admin
api.register_blueprint(admin)

app.register_blueprint(api)


@app.errorhandler(404)
@app.errorhandler(405)
def _handle_error(ex):
    if request.path.startswith('/api/'):
        return jsonify(error=str(ex)), ex.code
    else:
        return ex

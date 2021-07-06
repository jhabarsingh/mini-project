from flask import Flask, Blueprint, request, jsonify

from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS,cross_origin


app = Flask(__name__)
CORS(app)

app.config.from_object('config')

jwt = JWTManager(app=app)

db = MongoEngine(app)


api = Blueprint('api',__name__,url_prefix='/api')


from app.auth.controllers import auth
api.register_blueprint(auth)

from app.user.controllers import user
api.register_blueprint(user)


app.register_blueprint(api)


@app.errorhandler(404)
@app.errorhandler(405)
def _handle_error(ex):
    if request.path.startswith('/api/'):
        return jsonify(error=str(ex)), ex.code
    else:
        return ex
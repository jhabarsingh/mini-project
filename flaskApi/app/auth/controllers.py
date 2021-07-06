from flask import Blueprint,request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity,jwt_required
from datetime import timedelta
from mongoengine.errors import ValidationError

from app.error import  handleErrors,AppError
from app.models import  Users


auth = Blueprint('auth',__name__,url_prefix='/auth')

bcrypt = Bcrypt()


@auth.route('/signup',methods=['POST'])
@handleErrors
def signup():
        data = request.get_json()
        username = data['username']
        password = data['password']
        role = data['role']
        if len(password)<8:
            return AppError.badRequest('Password must have length greater than or equal to 8')
        password = bcrypt.generate_password_hash(password) 
        newUser = Users(username=username,password=password,role=role)
        newUser.save()
        return {'message':'SingnUp Sucessfull'},200

@auth.route('/signin',methods=['POST'])
@handleErrors
def signin():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = Users.objects(username=username).first()
    if user == None:
        return AppError.error("Username does not exists.")
    if not bcrypt.check_password_hash(user.password,password):
        return AppError.error("Invalid Password.")
    res = {}
    user = {}
    user['username'] = username
    user['role'] = user.role
    res['user'] = user
    res['accessToken'] = create_access_token(str(user.id),expires_delta=timedelta(days=1))
    return res,200

@auth.route('/getUser',methods=['POST'])
@jwt_required()
def getUser():
    identity = get_jwt_identity()
    user = Users.objects(id=identity).first()
    if user == None:
        return AppError.error("Username does not exists.")
    res = {}
    res['username'] = user.username
    res['role'] = user.role
    return res,200


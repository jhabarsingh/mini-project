from flask import Blueprint,request,jsonify
from flask_jwt_extended import get_jwt_identity,jwt_required

from app.error import handleErrors,AppError
from app.models import  UserDeploymentRequest,Users
from app.utils import addUsernames

admin = Blueprint('admin',__name__,url_prefix='/admin')

@admin.route('/get-requests',methods=['POST'])
@jwt_required()
def getRequets():
    identity = get_jwt_identity()
    user = Users.objects(id = identity).first()
    if(user.role=="admin"):
        requirements = UserDeploymentRequest.objects
        requirements = list(map(addUsernames,requirements))
        pending = list(filter(lambda x:x['status']=='pending',requirements))
        running = list(filter(lambda x:x['status']=='running',requirements))
        stopped = list(filter(lambda x:x['status']=='stopped',requirements))
        response = jsonify({'data':{
            'pending':{
                'count':len(pending),
                'array':pending
            },
            'running':{
                'count':len(running),
                'array':running
            },
            'stopped':{
                'count':len(stopped),
                'array':stopped
            },
        }})
        return response,200
    return AppError.badRequest("Admin only route")


@admin.route('/get-users',methods=['POST'])
@jwt_required()
def getUsers():
    identity = get_jwt_identity()
    user = Users.objects(id = identity).first()
    if(user.role=="admin"):
        users = Users.objects.exclude('id').exclude('password')
        admins = list(filter(lambda x:x.role=='admin',users))
        userss = list(filter(lambda x:x.role=='user',users))
        response = jsonify({'data':{
            'admins':{
                'count':len(admins),
                'array':admins
            },
            'users':{
                'count':len(userss),
                'array':userss
            }
        }})
        return response,200
    return AppError.badRequest("Admin only route")


    
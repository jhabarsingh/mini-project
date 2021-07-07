from flask import Blueprint,request,jsonify
from flask_jwt_extended import get_jwt_identity,jwt_required

from app.error import handleErrors,AppError
from app.models import  UserDeploymentRequest,Users
from app.utils import addUsernames
from app.middleware import adminRoute

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
    else:
        requirements = UserDeploymentRequest.objects(by=identity)
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


@admin.route('/get-users',methods=['POST'])
@jwt_required()
@adminRoute
def getUsers():
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


@admin.route('/update-requirement',methods=['POST'])
@jwt_required()
@handleErrors
@adminRoute
def updateRequirement():
    data = request.get_json()
    _id =  data['id']
    req = UserDeploymentRequest.objects(id=_id).first()
    if 'cpu' in data:
        req.cpu = data['cpu']
    if 'memory' in data:
        req.memory = data['memory']
    if 'cpuLimit' in data:
        req.cpuLimit = data['cpuLimit']
    if 'memLimit' in data:
        req.memLimit = data['memLimit']
    if 'maxReplicas' in data:
        req.maxReplicas = data['maxReplicas']
    if 'maxRuntime' in data:
        req.maxRuntime = data['maxRuntime']
    req.save()
    return {'message':'Updated Successfully'},200
    

@admin.route('/delete-container',methods=['POST'])
@jwt_required()
@handleErrors
@adminRoute
def deleteContainer():
    data = request.get_json()
    _id =  data['id']
    req = UserDeploymentRequest.objects(id=_id).first()
    if(req.status!="running"):
        req.delete()
        return {'message':'Deleted Successfully'},200
    else:
        return AppError.error("The container is running")
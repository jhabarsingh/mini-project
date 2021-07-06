from flask import Blueprint,request,jsonify
from flask_jwt_extended import get_jwt_identity,jwt_required

from app.error import handleErrors,AppError
from app.models import  UserDeploymentRequest,Users
from app.utils import addUsernames

admin = Blueprint('admin',__name__,url_prefix='/admin')

@admin.route('/getRequests',methods=['POST'])
@jwt_required()
def requirements():
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




    
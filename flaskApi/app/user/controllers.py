from flask import Blueprint,request,jsonify
from flask_jwt_extended import get_jwt_identity,jwt_required
from flask_cors import CORS, cross_origin

from app.error import handleErrors
from app.models import  Users,UserDeploymentRequest

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/send-requirements',methods=['POST'])
@handleErrors
@jwt_required()
def requirements():
    identity = get_jwt_identity()
    data = request.get_json()
    data = data['requirements']
    data['by'] = identity
    requirements = UserDeploymentRequest(**data)
    requirements.save()
    requirements.appName = str(requirements.name)+"_app_"+str(requirements.id)
    requirements.deploymentName = str(requirements.name)+"_deploy_"+str(requirements.id)
    requirements.serviceName = str(requirements.name)+"_service_"+str(requirements.id)
    requirements.save()
    return jsonify({'message':'Added Sucessfull'}),200


    

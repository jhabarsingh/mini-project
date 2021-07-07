from flask import Blueprint,request,jsonify
from flask_jwt_extended import get_jwt_identity,jwt_required
from flask_cors import CORS, cross_origin

from app.error import handleErrors
from app.models import  Users,UserDeploymentRequest
from app.utils import Kube
from app import core_v1,apps_v1
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
    requirements.appName = str(requirements.name)+"-app-"+str(requirements.id)
    requirements.deploymentName = str(requirements.name)+"-deploy-"+str(requirements.id)
    requirements.serviceName = str(requirements.name)+"-service-"+str(requirements.id)
    requirements.save()
    return jsonify({'message':'Added Sucessfull'}),200

@user.route('/delete-entry',methods=['POST'])
@jwt_required()
@handleErrors
def deleteEntry():
    data = request.get_json()
    _id =  data['id']
    req = UserDeploymentRequest.objects(id=_id).first()
    if(req.status=="running"):
        Kube.delete(req,core_v1,apps_v1)
    req.delete()
    return {'message':'Deleted Successfully'},200


    



from app import db

class Users(db.Document):
    username = db.StringField(required=True,unique=True)
    password = db.StringField(required=True)
    role = db.StringField(required=True)

class UserDeploymentRequest(db.Document):
    name = db.StringField(required=True)
    image = db.StringField(required=True)
    port = db.IntField(required=True)
    cpu = db.StringField(required=True)
    memory = db.StringField(required=True)
    by = db.ReferenceField('Users',required=True)
    status = db.StringField(default="pending")
    approvedBy = db.ReferenceField('Users')
    maxReplicas = db.IntField()
    memLimit =  db.StringField()
    cpuLimit = db.StringField()
    maxRuntime = db.IntField()
    appName = db.StringField()
    deploymentName = db.StringField()
    serviceName = db.StringField()
    exposedPort = db.IntField()

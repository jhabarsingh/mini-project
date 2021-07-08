

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
    maxReplicas = db.IntField(default="5")
    memLimit =  db.StringField(default="500Mi")
    cpuLimit = db.StringField(default="400m")
    maxRuntime = db.IntField(default="7200")
    appName = db.StringField()
    deploymentName = db.StringField()
    serviceName = db.StringField()
    exposedPort = db.IntField()

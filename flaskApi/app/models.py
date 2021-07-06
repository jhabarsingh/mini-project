

from app import db

class Users(db.Document):
    username = db.StringField(required=True,unique=True)
    password = db.StringField(required=True)
    role = db.StringField(required=True)

# class RegisterKeys(db.Document):
#     by = db.ReferenceField('Users',required=True)

# class SyncData(db.Document):
#     of = db.ReferenceField('Users',required=True)
#     url = db.StringField(required = True,unique_with='of')
#     thumb = db.StringField(required = True)
#     title = db.StringField()
#     type = db.StringField(required=True)

class UserDeploymentRequest(db.Document):
    name = db.StringField(required=True,unique=True)
    app = db.StringField(required=True,unique=True)
    image = db.StringField(required=True)
    port = db.IntField(required=True)
    cpu = db.StringField(required=True)
    memory = db.StringField(required=True)
    by = db.ReferenceField('Users',required=True)
    status = db.StringField(default="pending")
from functools import wraps
from flask import request
from flask_jwt_extended import get_jwt_identity

from app.models import Users
from app.error import AppError

def adminRoute(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        identity = get_jwt_identity()
        user = Users.objects(id = identity).first()
        if(user.role.lower() =="admin"):
            return f(*args, **kwargs)
        else:
            return AppError.badRequest("Admin only route")
    return decorated_function

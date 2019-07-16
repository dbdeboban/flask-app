from flask_restful import Api
from app import flaskAppInstance
from .UserApi import User



restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(User,"/api/User/Signup")
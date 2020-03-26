from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension
from flask_jwt_extended import JWTManager
# from flask_security import Security

db = MongoEngine()
toolbar = DebugToolbarExtension()
jwt = JWTManager()
# security = Security()

from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from flask_jwt_extended import JWTManager
# from flask_security import Security

db = MongoEngine()
login_manager = LoginManager()
toolbar = DebugToolbarExtension()
jwt = JWTManager()
# security = Security()

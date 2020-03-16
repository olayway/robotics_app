from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension


db = MongoEngine()
login_manager = LoginManager()
toolbar = DebugToolbarExtension()

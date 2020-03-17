import os

from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from .extensions import db, login_manager, toolbar
from .commands import add_usecase
from .views import setup
from .auth import auth
from .models import User


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    #the toolbar is only enabled in debug mode

    CORS(app, resources={r'/*': {'origins': '*'}})

    #swagger config#
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        app.config["SWAGGER_URL"], 
        app.config["API_URL"], 
        config={
            'app_name': 'AutoMate App'
        }
    )

    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=app.config["SWAGGER_URL"])
    #swagger config end#

    #extensions#
    db.init_app(app)
    login_manager.init_app(app)
    toolbar.init_app(app)
    #extensions end#

    #blueprint#
    app.register_blueprint(setup)
    app.register_blueprint(auth)
    #end blueprint#

    #clicommands#
    app.cli.add_command(add_usecase)
    #clicommands end#

    #flask-login#
    @login_manager.user_loader
    def load_user(user_id):
        return User.objects.get(id=user_id)
    #flask-login#

    # app.add_url_rule("/add", view_func=test)
    # app.add_url_rule("/get", view_func=get_test)

    return app
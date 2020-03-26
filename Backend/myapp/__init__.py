import os

from datetime import timedelta

from flask import Flask, jsonify, redirect, url_for, request, session
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
# from flask_security import MongoEngineUserDatastore

from .auth import auth
from .commands import add_usecase
from .extensions import db, toolbar, jwt #, security
from .models import User #, Role
from .routes import setup



def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config')
    app.config.from_pyfile('config.py')

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
    toolbar.init_app(app)
    jwt.init_app(app)

    # user_datastore = MongoEngineUserDatastore(db, User, Role)
    # security_ctx = security.init_app(app, user_datastore)
    #extensions end#

    #blueprint#
    app.register_blueprint(setup)
    app.register_blueprint(auth)
    #end blueprint#

    #clicommands#
    app.cli.add_command(add_usecase)
    #clicommands end#

    # app.add_url_rule("/add", view_func=test)
    # app.add_url_rule("/get", view_func=get_test)

    return app
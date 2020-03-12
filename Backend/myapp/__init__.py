import os

from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from .extensions import db
from .commands import add_usecase
from .views import test


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
    #extensions end#

    #clicommands#
    app.cli.add_command(add_usecase)
    #clicommands end#

    return app
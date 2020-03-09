import os
import json

from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from .db import db
from .views import test_page


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    CORS(app, resources={r'/*': {'origins': '*'}})

    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        app.config["SWAGGER_URL"], 
        app.config["API_URL"], 
        config={
            'app_name': 'AutoMate App'
        }
    )

    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=app.config["SWAGGER_URL"])

    app.register_blueprint(test_page)

    db.init_app(app)

    # test route
    # @app.route('/denmark', methods=['GET'])
    # def test():
    #     documents = universal.find({'filter_tags.Company':'BJ-Gear'})
    #     response = []
    #     for doc in documents:
    #         doc['_id'] = str(doc['_id'])
    #         response.append(doc)
    #     return json.dumps(response)

    return app
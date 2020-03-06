import os

from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
import json


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.update(
        MONGO_URI = "mongodb+srv://olayway:KXvhcqmyZIn1NT83@cluster0-6uc3p.mongodb.net/automate_app?retryWrites=true&w=majority",
        SECRET_KEY = 'secret_key'
    )


    mongo = PyMongo(app)
    db = mongo.db
    universal = db['universal']
    yaskawa = db['yaskawa']
    print('Mongo DB:', mongo.db)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def test():
        documents = universal.find({"Country": "Denmark"})
        response = []
        for doc in documents:
            doc['_id'] = str(doc['_id'])
            response.append(doc)
        return json.dumps(response)

    return app
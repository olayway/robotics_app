import os

from datetime import timedelta

from flask import Flask, jsonify, redirect, url_for, request, session
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
# from flask_security import MongoEngineUserDatastore

from .auth import auth
from .routes import main
from .extensions import db, toolbar, jwt  # , security
from .models import User  # , Role
from .commands import add_usecase


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    CORS(app, supports_credentials=True)

    #swagger config#
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        app.config["SWAGGER_URL"],
        app.config["API_URL"],
        config={
            'app_name': 'AutoMate App'
        }
    )

    app.register_blueprint(
        SWAGGERUI_BLUEPRINT,
        url_prefix=app.config["SWAGGER_URL"])
    #swagger config end#

    #extensions#
    db.init_app(app)
    toolbar.init_app(app)
    jwt.init_app(app)

    # user_datastore = MongoEngineUserDatastore(db, User, Role)
    # security_ctx = security.init_app(app, user_datastore)
    #extensions end#

    # check if the tokens identifier is in the blacklist set
    @jwt.token_in_blacklist_loader
    def check_if_token_revoked(decrypted_token):
        from .auth import blacklist
        jti = decrypted_token['jti']
        return jti in blacklist

    #blueprint#
    app.register_blueprint(main)
    app.register_blueprint(auth)
    #end blueprint#

    #clicommands#
    app.cli.add_command(add_usecase)
    #clicommands end#

    # add custom data claims to tokens
    # @jwt.user_claims_loader
    # def add_claims_to_access_token(user):
    #     use_cases = user['use_cases']
    #     use_cases_data = []

    #     for case in use_cases:
    #         use_case = case.basic_info.to_mongo().to_dict()
    #         use_case['id'] = str(case.id)
    #         use_case['title'] = case.content.article_title
    #         use_case['status'] = case.status
    #         use_cases_data.append(use_case)

    #     custom_claims = {
    #         'use_cases': use_cases_data
    #     }
    #     return custom_claims

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user['username']

    @jwt.user_loader_callback_loader
    def user_loader_callback(identity):
        user = User.objects(username=identity).get()
        if not user:
            return None
        return user

    @jwt.user_loader_error_loader
    def custom_user_loader_error(identity):
        response = jsonify({
            "msg": "User {} not found".format(identity['username'])
        })
        return response, 404

    @jwt.expired_token_loader
    def my_expired_token_callback(expired_token):
        token_type = expired_token['type']
        response = jsonify({
            'msg': 'The {} token has expired'.format(token_type)
        })
        return response, 401

    @jwt.needs_fresh_token_loader
    def non_fresh_token_callback():
        response = jsonify({
            'msg': 'This endpoint requires fresh login'
        })
        return response, 401

    @jwt.revoked_token_loader
    def token_revoked_access(revoked_token):
        token_type = revoked_token['type']
        response = jsonify({
            'msg': 'The {} token has been revoked'.format(token_type)
        })
        return response, 401

    @jwt.unauthorized_loader
    def missing_access_token(msg):
        response = jsonify({
            'msg': 'You are not authorized to access this endpoint',
            'reason': msg
        })
        return response, 401

    # app.add_url_rule("/add", view_func=test)
    # app.add_url_rule("/get", view_func=get_test)

    return app

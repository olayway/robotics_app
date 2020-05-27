import json
from time import mktime
from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request, url_for, redirect
from flask_jwt_extended import jwt_required, create_access_token, jwt_refresh_token_required, create_refresh_token, set_access_cookies, set_refresh_cookies, unset_jwt_cookies, current_user, get_raw_jwt

from .models import User

auth = Blueprint('auth', __name__)

#storage engine for revoked tokens#
# (consider redis or postgres for production version)
blacklist = set()
#end storage engine#

# registering new user
@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User.authenticate(**data)

    if user:
        response = jsonify({"msg": "User already exists"})
        return response, 400
    else:
        user = User(**data)
        user.set_password(data['password'])
        user.save()
        response = jsonify({
            'msg': 'User account successfully created'
        })
        return response, 201


# standard login - refresh token and fresh access token returned
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        response = jsonify({
            "authenticated": False,
            "msg": "Invalid credentials"})
        return response, 401

    access_expires = timedelta(minutes=2)
    refresh_expires = timedelta(hours=1)
    access_token = create_access_token(
        identity=user, expires_delta=access_expires, fresh=True)
    refresh_token = create_refresh_token(
        identity=user, expires_delta=refresh_expires)

    response = jsonify({
        'logged_in_as': user.username,
        'company_name': user.company_name,
        'access_token_exp': mktime((datetime.now() + access_expires).timetuple())})

    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response, 200

# fresh login (eg. for changing user settings) - only fresh access token returned (no new refresh token)
@auth.route('/fresh-login', methods=['POST'])
def fresh_login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        response = jsonify({
            "authenticated": False,
            "msg": "Invalid credentials"})
        return response, 401

    access_expires = timedelta(minutes=2)
    access_token = create_access_token(
        identity=user, expires_delta=access_expires, fresh=True)

    response = jsonify({
        'access_token_exp': mktime((datetime.now() + access_expires).timetuple())})

    set_access_cookies(response, access_token)

    return response, 200


# endpoint for refreshing access token
@auth.route('/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh():
    print('CURRENT USER refreshing access', current_user)
    access_expires = timedelta(minutes=2)
    access_token = create_access_token(
        identity=current_user, expires_delta=access_expires, fresh=False)

    response = jsonify({
        'access_token_exp': mktime((datetime.now() + access_expires).timetuple()),
        'fresh': False
    })

    set_access_cookies(response, access_token)
    return response, 200

# endpoint for revoking access token
@auth.route('/logout', methods=['GET'])
@jwt_required
def remove_access_token():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return redirect(url_for('auth.remove_refresh_token'))


# endpoint for revoking refresh token
@auth.route('/refresh-remove', methods=['GET'])
@jwt_refresh_token_required
def remove_refresh_token():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    response = jsonify({'msg': 'Successfully logged out'})
    unset_jwt_cookies(response)
    return response, 200

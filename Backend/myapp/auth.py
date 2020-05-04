from flask import Blueprint, jsonify, render_template, request, url_for, redirect, make_response
from flask_jwt_extended import jwt_required, create_access_token, jwt_refresh_token_required, create_refresh_token, get_jwt_identity, jwt_optional, set_access_cookies, set_refresh_cookies, unset_jwt_cookies, get_jwt_claims, fresh_jwt_required, current_user, get_raw_jwt
from time import mktime
from datetime import datetime, timedelta

from .models import User

auth = Blueprint('auth', __name__)

#storage engine for revoked tokens#
# (consider redis or postgres for production version)
blacklist = set()
#end storage engine#


# registering new user
@auth.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        user = User(**data)
        user.set_password(data['password'])
        user.save()
    else:
        return jsonify({"msg": "User already exists"}), 400

    response = jsonify({
        'msg': 'User account successfully created'
    })

    return response, 201


# standard login - refresh token and fresh access token returned
@auth.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        response = jsonify({
            "authenticated": False,
            "msg": "Invalid credentials"})
        return response, 401

    access_expires = timedelta(minutes=5)
    refresh_expires = timedelta(hours=1)
    access_token = create_access_token(
        identity=user, expires_delta=access_expires, fresh=True)
    refresh_token = create_refresh_token(
        identity=user, expires_delta=refresh_expires)

    response = jsonify({
        'logged_in_as': user.username,
        'access_token_exp': mktime((datetime.now() + access_expires).timetuple()),
        'fresh': True
    })

    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response, 200

# fresh login (eg. for changing user settings) - only fresh access token returned (no new refresh token)
@auth.route('/api/fresh-login', methods=['POST'])
def fresh_login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        response = jsonify({
            "authenticated": False,
            "msg": "Invalid credentials"})
        return response, 401

    access_expires = timedelta(minutes=1)
    access_token = create_access_token(
        identity=user, expires_delta=access_expires, fresh=True)

    response = jsonify({
        'logged_in_as': user.username,
        'access_token_exp': mktime((datetime.now() + access_expires).timetuple()),
        'fresh': True
    })

    set_access_cookies(response, access_token)

    return response, 200

# endpoint for fetching user's use cases
@auth.route('/api/profile/use-cases', methods=['GET', 'POST'])
@jwt_required
def user_use_cases():
    claims = get_jwt_claims()
    use_cases = claims['use_cases']
    print('claims', claims)
    print('use_cases', use_cases)
    response = jsonify({
        'your_use_cases': use_cases
    })
    return response, 200

# endpoint for revoking access token
@auth.route('/api/profile/logout', methods=['GET'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    print(blacklist)
    response = jsonify({'msg': 'Successfully logged out'})
    # unset_jwt_cookies(response)
    return response, 200


@auth.route('/api/profile/settings', methods=['GET', 'POST'])
@fresh_jwt_required
def edit_user_settings():
    username = get_jwt_identity()
    return jsonify(fresh_logged_in_as=username), 200


# endpoint for refreshing access token
@auth.route('/api/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh():
    print('CURRENT USER', current_user)
    # current_user = get_jwt_identity()
    access_expires = timedelta(minutes=1)
    access_token = create_access_token(
        identity=current_user, expires_delta=access_expires, fresh=False)

    response = jsonify({
        'access_token_exp': mktime((datetime.now() + access_expires).timetuple()),
        'fresh': False
    })

    set_access_cookies(response, access_token)
    return response, 200


# endpoint for revoking refresh token
@auth.route('/api/refresh/remove', methods=['GET'])
@jwt_refresh_token_required
def logout2():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    print(blacklist)
    response = jsonify({'msg': 'Successfully logged out'})
    # unset_jwt_cookies(response)
    return response, 200

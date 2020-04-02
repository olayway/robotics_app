from flask import Blueprint, jsonify, render_template, request, url_for, redirect, make_response
from flask_jwt_extended import jwt_required, create_access_token, jwt_refresh_token_required, create_refresh_token, get_jwt_identity, jwt_optional, set_access_cookies, set_refresh_cookies, unset_jwt_cookies, get_jwt_claims, fresh_jwt_required, current_user
from datetime import timedelta

from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/token/register', methods=['POST'])
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


@auth.route('/token/auth', methods=['POST'])
# standard login - refresh token and fresh access token returned
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        response = jsonify({
            "authenticated": False,
            "msg": "Invalid credentials"})
        return response, 401

    access_expires = timedelta(minutes=2)
    refresh_expires = timedelta(minutes=5)
    access_token = create_access_token(
        identity=user, expires_delta=access_expires, fresh=True)
    refresh_token = create_refresh_token(
        identity=user, expires_delta=refresh_expires)

    response = jsonify({
        'logged_in_as': user.username,
        'access_token_exp': access_expires.total_seconds(),
        'refresh_token_exp': refresh_expires.total_seconds()
    })

    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response, 200


@auth.route('/token/fresh-auth', methods=['POST'])
# fresh login (eg. for changing user settings) - only fresh access token returned (no refresh token)
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
        'logged_in_as': user.username,
        'access_token_exp': access_expires.total_seconds(),
    })

    set_access_cookies(response, access_token)

    return response, 200


@auth.route('/token/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh():
    print('CURRENT USER', current_user)
    # current_user = get_jwt_identity()
    expires = timedelta(minutes=5)
    access_token = create_access_token(
        identity=current_user, expires_delta=expires, fresh=False)

    response = jsonify(
        {'token_refreshed': True, 'acces_token_exp': expires.total_seconds()})
    set_access_cookies(response, access_token)
    return response, 200

# endpoint for revoking access token
@auth.route('/token/remove', methods=['GET'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    response = jsonify({'msg': 'Successfully logged out'})
    # unset_jwt_cookies(response)
    return response, 200


# endpoint for revoking refresh token
@auth.route('/token/remove-refresh', methods=['POST'])
@jwt_refresh_token_required
def logout2():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    response = jsonify({'msg': 'Successfully logged out'})
    # unset_jwt_cookies(response)
    return response, 200


@auth.route('/api/profile', methods=['GET'])
@jwt_required
def profile():
    # TODO extract use-case ids from token claims
    # TODO query mongoDB for extracted ids and return them to the user

    response = jsonify({
        'logged_in_as': get_jwt_identity(),
        'use_cases': get_jwt_claims()['use_cases']
    })
    return response, 200


@auth.route('/api/profile/settings', methods=['GET', 'POST'])
@fresh_jwt_required
def edit_user_settings():
    username = get_jwt_identity()
    return jsonify(fresh_logged_in_as=username), 200

# @auth.route('/api/optional_login', methods=['GET'])
# @jwt_optional
# def optional_login():
#     current_user = get_jwt_identity()
#     if current_user:
#         return jsonify(logged_in_as=current_user), 200
#     return jsonify(logged_in_as='anonymous user'), 200

# @auth.route('/logout')
# # @login_required
# def logout():
#     logout_user()
#     print('loggedout')
#     return redirect(url_for('auth.login'))
# @auth.route('/mycases')
# # @login_required
# def mycases():
#     return render_template('mycases.html', name=current_user.username)

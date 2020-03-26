from flask import Blueprint, jsonify, render_template, request, url_for, redirect, make_response
from flask_jwt_extended import jwt_required, jwt_optional, create_access_token, get_jwt_identity
from datetime import timedelta

from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        user = User(**data)
        user.set_password(data['password']) 
        user.save()
        access_token = create_access_token(identity=user.username)
    else:
        return jsonify({"msg": "User already exists"}), 400
    
    return jsonify(access_token=access_token), 201


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return jsonify({"msg": "Invalid credentials", 'authenticated': False}), 401

    access_token = create_access_token(identity=user.username, expires_delta=timedelta(minutes=5))

    return jsonify(access_token=access_token), 200



@auth.route('/loggedin', methods=['GET'])
@jwt_required
def loggedin():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@auth.route('/optional_login', methods=['GET'])
@jwt_optional
def optional_login():
    current_user = get_jwt_identity()
    if current_user:
        return jsonify(logged_in_as=current_user), 200
    return jsonify(logged_in_as='anonymous user'), 200


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
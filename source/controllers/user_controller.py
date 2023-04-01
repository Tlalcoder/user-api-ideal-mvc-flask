from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from source.services.user_service import UserService
from flask_restx import Namespace, Resource, fields

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Check if user already exists with the given email
    existing_user = UserService.get_user_by_email(email)
    if existing_user:
        return jsonify({'message': 'Email already exists'}), 400

    user = UserService.create_user(name, email, password)

    return jsonify({
        'message': 'User created successfully',
        'user': UserService.serialize_user(user)
    }), 201


@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = UserService.get_user_by_email(email)

    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401

    if not UserService.check_password(user, password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id)

    return jsonify({
        'message': 'Login successful',
        'access_token': access_token
    }), 200


@user_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    get_jwt_identity()
    return jsonify({
        'message': 'Access granted',
    }), 200

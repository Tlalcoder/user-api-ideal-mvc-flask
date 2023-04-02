from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from source.services.user_service import UserService
from source.responses.response_helper import error_response, success_response


user_blueprint = Blueprint('user', __name__)
user_service = UserService()


@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Check if user already exists with the given email
    existing_user = user_service.get_user_by_email(email)
    if existing_user:
        return jsonify({'message': 'Email already exists'}), 400

    user = user_service.create_user(name, email, password)

    return jsonify({
        'message': 'User created successfully',
        'user': user_service.serialize_user(user)
    }), 201


@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = user_service.get_user_by_email(email)

    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401

    if not user_service.check_password(user, password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id)

    return jsonify({
        'message': 'Login successful',
        'access_token': access_token
    }), 200


@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify(users), 200


@user_blueprint.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    current_user_id = get_jwt_identity()

    if user_id != current_user_id:
        return error_response('You are not authorized to view this user information', 401)

    user = user_service.get_user_by_id(user_id)
    data = user_service.serialize_user(user)

    if user:
        response = success_response(data)
    else:
        response = error_response('User not found', 404)
    return response


@user_blueprint.route('/delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if user.id != get_jwt_identity():
        return jsonify({'message': 'You are not authorized to delete this user'}), 401

    success = user_service.delete_user(user_id)
    if success:
        return '', 204
    else:
        return jsonify({'message': 'Failed to delete user'}), 500
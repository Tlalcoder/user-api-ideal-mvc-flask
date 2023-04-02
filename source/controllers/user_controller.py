from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from source.services.user_service import UserService


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


@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return 'User not found', 404
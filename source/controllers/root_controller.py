from flask import Blueprint, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

root_blueprint = Blueprint('root', __name__)


@root_blueprint.route('/')
@jwt_required()
def index():
    return jsonify({
        'message': 'PING'
    })
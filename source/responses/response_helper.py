from flask import jsonify


def success_response(data, message='Success'):
    response = {
        'message': message,
        'data': data,
    }
    return jsonify(response), 200


def error_response(message, status_code):
    response = {
        'message': message,
    }
    return jsonify(response), status_code



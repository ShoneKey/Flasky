from flask import jsonify


from app.api_1_0 import api
from app.exceptions import ValidationError


def forbidden(message):
    response = jsonify({'error': 'Forbidden', 'message': message})
    response.status_code = 403
    return response


def bad_request(message):
    response = jsonify({'error': 'Bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'error': 'Unauthorized', 'message': message})
    response.status_code = 401
    return response


def page_not_found(message):
    response = jsonify({'error': 'Not found', 'message': message})
    response.status_code = 404
    return response


def method_not_allowed(message):
    response = jsonify({'error': 'Method not allowed', 'message': message})
    response.status_code = 405
    return response


def internal_server_error(message):
    response = jsonify({'error': 'Internal server error', 'message': message})
    response.status_code = 500
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])

from flask import jsonify, Blueprint

error_handlers_blueprint = Blueprint('errors', __name__)

@error_handlers_blueprint.app_errorhandler(Exception)
def handle_generic_error(e):
    return jsonify({'message': 'An unexpected error occurred', 'error': str(e)}), 500

@error_handlers_blueprint.app_errorhandler(404)
def handle_not_found(e):
    return jsonify({'message': 'Resource not found'}), 404

@error_handlers_blueprint.app_errorhandler(401)
def handle_unauthorized(e):
    return jsonify({'message': 'Unauthorized request'}), 401

@error_handlers_blueprint.app_errorhandler(403)
def handle_forbidden(e):
    return jsonify({'message': 'Forbidden request'}), 403

@error_handlers_blueprint.app_errorhandler(400)
def handle_bad_request(e):
    return jsonify({'message': 'Bad request', 'error': str(e)}), 400


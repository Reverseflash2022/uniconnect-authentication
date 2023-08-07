from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from flask import jsonify

def student_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()
        if not identity or identity.get('role') != 'student':
            return jsonify({'message': 'Permission required: Student'}), 403
        return fn(*args, **kwargs)
    return wrapper

def moderator_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()
        if not identity or identity.get('role') != 'moderator':
            return jsonify({'message': 'Permission required: Moderator'}), 403
        return fn(*args, **kwargs)
    return wrapper


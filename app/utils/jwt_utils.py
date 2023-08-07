from flask_jwt_extended import get_jwt_identity
import jwt
from datetime import datetime, timedelta
from flask import current_app

def encode_auth_token(user_id, user_role):
    """ Generates the Auth Token """
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user_id,
            'role': user_role
        }
        return jwt.encode(
            payload,
            current_app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return str(e)

def decode_auth_token(auth_token):
    """ Decodes the auth token """
    try:
        payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'), algorithms=["HS256"])
        return payload['sub'], payload['role']
    except jwt.ExpiredSignatureError:
        return 'Token expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def get_current_user_role():
    """
    Returns the role of the current user.
    :return: string
    """
    identity = get_jwt_identity()
    return identity['role'] if identity else None


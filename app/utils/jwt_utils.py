from flask_jwt_extended import create_access_token, decode_token, get_jwt_identity

def encode_auth_token(user_id, role):
    """
    Generates the Auth Token.
    :return: string
    """
    payload = {
        'id': user_id,
        'role': role
    }
    return create_access_token(identity=payload)

def decode_auth_token(auth_token):
    """
    Decodes the auth token.
    :return: integer|string
    """
    try:
        payload = decode_token(auth_token)
        return payload['identity']
    except:
        return None

def get_current_user_role():
    """
    Returns the role of the current user.
    :return: string
    """
    identity = get_jwt_identity()
    return identity['role'] if identity else None


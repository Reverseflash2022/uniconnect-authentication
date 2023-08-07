from flask import Blueprint, jsonify, request
from app import jwt, db
from app.models.student import Student
from app.models.moderator import Moderator
from app.utils.jwt_utils import encode_auth_token, decode_auth_token, get_current_user_role
from werkzeug.security import generate_password_hash

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    post_data = request.get_json()
    role = post_data.get('role')

    if role == "student":
        # Create student
        hashed_password = generate_password_hash(post_data.get('password'))
        student = Student(username=post_data.get('username'),
                          _hashed_password=hashed_password,
                          email=post_data.get('email'),
                          courses="")
        db.session.add(student)
        db.session.commit()
        return jsonify({'message': 'Student successfully registered'}), 201

    elif role == "moderator":
        # Create moderator
        moderator = Moderator(moderator_id=post_data.get('moderator_id'),
                              associated_university=post_data.get('associated_university'),
                              permissions="")
        db.session.add(moderator)
        db.session.commit()
        return jsonify({'message': 'Moderator successfully registered'}), 201

    return jsonify({'message': 'Invalid role provided'}), 400

@auth_blueprint.route('/login', methods=['POST'])
def login():
    post_data = request.get_json()
    role = post_data.get('role')

    if role == "student":
        user = Student.query.filter_by(email=post_data.get('email')).first()

    elif role == "moderator":
        user = Moderator.query.filter_by(moderator_id=post_data.get('moderator_id')).first()

    else:
        return jsonify({'message': 'Invalid role provided'}), 401

    if user and (role == "student" and user.check_password(post_data.get('password'))):
        auth_token = encode_auth_token(user.id, role)
        return jsonify({
            'message': 'Successfully logged in',
            'auth_token': auth_token
        }), 200

    return jsonify({'message': 'Invalid credentials provided'}), 401

@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    # Token invalidation can be implemented in multiple ways, 
    # e.g., by adding them to a "blacklist" database table.
    # For simplicity, we'll just inform the user they've logged out.
    return jsonify({'message': 'Successfully logged out'}), 200


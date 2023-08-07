from flask import Blueprint, jsonify, request
from flask_limiter.util import get_remote_address
from app import db
from app.models.student import Student
from app.models.moderator import Moderator
from app.utils.decorators import student_required, moderator_required

user_management_blueprint = Blueprint('user_management', __name__)

# Fetch student profile
@limiter.limit("15 per minute", key_func=get_remote_address)
@user_management_blueprint.route('/student/profile', methods=['GET'])
@student_required
def get_student_profile():
    identity = get_jwt_identity()
    student = Student.query.get(identity['id'])
    return jsonify(student.to_dict()), 200

# Update student profile
@limiter.limit("15 per minute", key_func=get_remote_address)
@user_management_blueprint.route('/student/profile', methods=['PUT'])
@student_required
def update_student_profile():
    identity = get_jwt_identity()
    student = Student.query.get(identity['id'])
    post_data = request.get_json()
    if 'courses' in post_data:
        student.courses = post_data['courses']
    if 'email' in post_data:
        student.email = post_data['email']
    db.session.commit()
    return jsonify({'message': 'Profile updated successfully'}), 200

# Fetch moderator profile
@limiter.limit("5 per minute", key_func=get_remote_address)
@user_management_blueprint.route('/moderator/profile', methods=['GET'])
@moderator_required
def get_moderator_profile():
    identity = get_jwt_identity()
    moderator = Moderator.query.get(identity['id'])
    return jsonify(moderator.to_dict()), 200

# Update moderator profile
@limiter.limit("15 per minute", key_func=get_remote_address)
@user_management_blueprint.route('/moderator/profile', methods=['PUT'])
@moderator_required
def update_moderator_profile():
    identity = get_jwt_identity()
    moderator = Moderator.query.get(identity['id'])
    post_data = request.get_json()
    if 'associated_university' in post_data:
        moderator.associated_university = post_data['associated_university']
    if 'permissions' in post_data:
        moderator.permissions = post_data['permissions']
    db.session.commit()
    return jsonify({'message': 'Profile updated successfully'}), 200


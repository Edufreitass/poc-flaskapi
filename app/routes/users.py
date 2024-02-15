from flask import Blueprint, request, jsonify

from app import db
from app.models.user import User

user_bp = Blueprint('user', __name__)


@user_bp.post('/')
def user_create():
    data = request.get_json()
    user = User(
        name=data['name'],
        age=data['age']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@user_bp.get(rule='/')
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@user_bp.get('/<int:id>')
def get_user_by_id(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())


@user_bp.put('/<int:id>')
def user_update(id):
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user.name = data.get('name', user.name)
    user.age = data.get('age', user.age)

    db.session.commit()
    return jsonify(user.to_dict()), 200

@user_bp.patch('/<int:id>')
def user_patch(id):
    data = request.get_json()
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    allowed_fields = ['age']
    for field in allowed_fields:
        if field in data:
            setattr(user, field, data[field])

    db.session.commit()
    return jsonify(user.to_dict()), 200


@user_bp.delete('/<int:id>')
def user_delete(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

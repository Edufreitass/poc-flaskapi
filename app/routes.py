from flask import Blueprint, request, jsonify

from app import db
from app.models import User

hello_world_bp = Blueprint('hello', __name__)
user_bp = Blueprint('user', __name__)


@hello_world_bp.get('/')
def hello_world():
    return "<p> Hello, World!</p>"


@user_bp.post('/')
def user_create():
    data = request.get_json()
    user = User(
        name=data['name']
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

from flask import Blueprint, jsonify, request

from app import db
from app.models.post import Post

post_bp = Blueprint('post', __name__)


@post_bp.post('/')
def add_post():
    data = request.get_json()
    new_post = Post(
        title=data['title'],
        body=data['body'],
        user_id=data['user_id']
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201


@post_bp.get(rule='/')
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])


@post_bp.get('/<int:post_id>')
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(post.to_dict()), 200


@post_bp.put('/<int:post_id>')
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.body = data.get('body', post.body)
    # Adicione aqui atualizações para outros campos, se necessário
    db.session.commit()
    return jsonify(post.to_dict()), 200

# Deletar um post pelo ID


@post_bp.delete('/<int:post_id>')
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted successfully'}), 200

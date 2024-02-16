import enum
from datetime import datetime

from sqlalchemy import Enum

from app.extensions.extensions import db


class PostStatusEnum(enum.Enum):
    DRAFT = "Rascunho"
    PUBLISHED = "Publicado"
    ARCHIVED = "Arquivado"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(Enum(PostStatusEnum),
                       default=PostStatusEnum.DRAFT,
                       nullable=False)
    # Relacionamento: Um usuário pode ter muitos posts
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at,
            'user_id': self.user_id,
            'status': self.status.value
        }

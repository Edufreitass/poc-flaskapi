from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

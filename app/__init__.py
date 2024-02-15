from flask import Flask
from .extensions import db, migrate
from .routes import hello_world_bp, user_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(hello_world_bp, url_prefix='/hello')
    app.register_blueprint(user_bp, url_prefix='/users')

    return app

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_htmx import HTMX
from flask_cors import CORS

from config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
htmx = HTMX()
cors = CORS()
login = LoginManager()
config = Config()

def create_app():
    app = Flask(__name__)

    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    htmx.init_app(app)
    cors.init_app(app)
    login.init_app(app)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app


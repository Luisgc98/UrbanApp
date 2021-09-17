from flask import Flask
from .config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config=Config):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config)

    Bootstrap().init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    Migrate().init_app(app, db)

    from .auth import auth
    app.register_blueprint(auth)

    from .main import main
    app.register_blueprint(main)

    return app
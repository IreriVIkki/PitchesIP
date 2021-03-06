from flask import Flask
from flask_login import LoginManager
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_simplemde import SimpleMDE

db = SQLAlchemy()
login_manager = LoginManager()
simple = SimpleMDE()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY'] = 'c3be71c065117cd56d5113506fd6fbf3'
    app.config['SIMPLEMDE_JS_IIFE'] = True
    app.config['SIMPLEMDE_USE_CDN'] = True

    # initializing flask extentions by creatiing instances of the extensions
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)

    # importing and regestering my main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app

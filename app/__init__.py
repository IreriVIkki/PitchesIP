from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY'] = 'c3be71c065117cd56d5113506fd6fbf3'

    # initializing flask extentions by creatiing instances of the extensions
    database.init_app(app)

    # importing and regestering my main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

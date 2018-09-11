import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABSQLALCHEMY_DATABASE_URIASE_URL = 'postgresql+psycopg2://vikki:sasawa@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vikki:sasawa@localhost/pitches'
    DEBUG = True
    pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vikki:sasawa@localhost/pitches'
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vikki:sasawa@localhost/pitches'
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}

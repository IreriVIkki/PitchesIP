import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/pitches'
    pass


class DevConfig(Config):

    DEBUG = True
    pass


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass


config_options = {
    'development': DevConfig,
    'Production': ProdConfig,
    'test': TestConfig
}

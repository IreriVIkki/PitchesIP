class DevConfig:
    pass


class ProdConfig:
    pass


class TestConfig:
    pass


config_options = {
    'development': DevConfig,
    'Production': ProdConfig,
    'test': TestConfig
}

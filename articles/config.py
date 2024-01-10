from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URI = ...


class ProductionConfig(Config):
    DATABASE_URI = os.environ.get('PRODUCTION_DB_URI')


class DevelopmentConfig(Config):
    DATABASE_URI = os.environ.get('DEVELOPMENT_DB_URI')
    DEBUG = True


class TestingConfig(Config):
    DATABASE_URI = os.environ.get('TESTING_DB_URI')
    TESTING = True
    WTF_CSRF_ENABLED = False


def get_app_configuration() -> type[Config]:
    config = os.environ.get('APP_CONFIGURATION', '').lower()
    available_configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
    }
    return available_configs.get(config, DevelopmentConfig)

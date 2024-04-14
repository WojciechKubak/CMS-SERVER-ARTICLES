from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret-key')


class DevelopmentConfig(Config):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True

# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
   # project root directory
    BASE_DIR = os.path.join(os.pardir, os.path.dirname(__file__))
    SECRET_KEY = os.environ.get("SECRET_KEY")

    TESTING = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        'case_sensitive': False,
        'echo': True,
        'echo_pool': True
    }


class DevelopmentConfig(Config):
    ASSETS_DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    USE_RELOADER = False

# instance/config.py

# For environment configuration

# config.py

# contains environment settings

import os

class Config(object):
    """Sharing variables configs (cross origin etc)"""
    DEBUG = False
    CSRF_ENABLED = True

class DevelopmentConfig(Config):
    """Development environment variables config."""
    DEBUG = True

class ProductionConfig(Config):
    """Production environment variables config."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
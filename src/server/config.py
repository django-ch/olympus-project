import logging
import os

from environs import Env

env = Env()


class EnvironmentConfig:
    """
    Base class for config that is shared between environments
    """
    LOG_LEVEL = logging.ERROR
    SQLALCHEMY_DATABASE_URI = env('OLYMPUS_PROJECT_DB', '')

class StagingConfig(EnvironmentConfig):
    """
    Staging configuration
    """
    LOG_LEVEL = logging.DEBUG


class DevConfig(EnvironmentConfig):
    """
    Local development configuration
    """
    LOG_DIR = 'logs'
    LOG_LEVEL = logging.DEBUG
    DEBUG = True
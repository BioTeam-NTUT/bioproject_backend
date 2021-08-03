#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: config.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/5/11 11:17 AM
"""

from os import environ
from os.path import abspath

from dotenv import load_dotenv


class Config(object):
    """Base configuration."""

    API_TITLE = "Broad-spectrum polypeptide smart vaccine analyzing platform"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_URL_PREFIX = "/api"
    OPENAPI_SWAGGER_UI_PATH = "/doc"
    OPENAPI_SWAGGER_UI_VERSION = "3.24.2"
    OPENAPI_SWAGGER_UI_URL = """
        https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/
    """

    SECRET_KEY = None
    EMAIL_ADDRESS = None
    SENTRY_DSN = None
    LOG_PATH = None

    def __init__(self):
        is_loaded = load_dotenv("../../.env")
        if not is_loaded:
            raise FileNotFoundError(".env not found")

        self.SECRET_KEY = environ.get("SECRET_KEY")
        self.EMAIL_ADDRESS = environ.get("EMAIL_ADDRESS")
        self.SENTRY_DSN = environ.get("SENTRY_DSN")
        self.LOG_PATH = abspath(environ.get("LOG_PATH"))


class DevConfig(Config):
    """Development configuration."""

    FLASK_ENV = "dev"
    DEBUG = True


class ProdConfig(Config):
    """Development configuration."""

    FLASK_ENV = "prod"
    DEBUG = False

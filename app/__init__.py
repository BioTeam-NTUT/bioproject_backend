#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: __init__.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/5/11 11:19 AM
"""

import sentry_sdk
from flask import Flask
from flask.helpers import get_debug_flag
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from config import ProdConfig, DevConfig


def create_app(config_local=ProdConfig):
    sentry_sdk.init(
        dsn=config_local.SENTRY_DSN,
        integrations=[FlaskIntegration(), CeleryIntegration(), SqlalchemyIntegration()],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,

        # By default the SDK will try to use the SENTRY_RELEASE
        # environment variable, or infer a git commit
        # SHA as release, however you may want to set
        # something more human-readable.
        # release="myapp@1.0.0",
    )
    app_local = Flask(__name__)
    app_local.config.from_object(config_local)

    return app_local


config = DevConfig() if get_debug_flag() else ProdConfig()
app = create_app(config)

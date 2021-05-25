#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: __init__.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/5/11 11:19 AM
"""

from flask import Flask
from routes import blueprint as api

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(api, url_prefix='/api/v1')

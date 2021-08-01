#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: __init__.py.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/7/24 12:16 PM
"""
from flask import Blueprint

from app.routes.protein import protein

api_v1 = Blueprint("api_v1", __name__)
api_v1.register_blueprint(protein, url_prefix="/protein")

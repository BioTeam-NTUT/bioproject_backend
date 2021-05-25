#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: config.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/5/11 11:17 AM
"""

from os import environ

FRONTEND_URL = environ.get('FRONTEND_URL')
SECRET_KEY = environ.get('SECRET_KEY')
EMAIL_ADDRESS = environ.get('EMAIL_ADDRESS')

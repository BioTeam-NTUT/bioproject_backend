#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: __init__.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/5/25 9:31 PM
"""
from flask import Blueprint
from flask_restx import Api, Resource

blueprint = Blueprint('api', __name__)
api = Api(blueprint,
          title='Broad-spectrum polypeptide smart vaccine analyzing platform',
          contact='guyleaf',
          contact_email='ychhua1@gmail.com',
          default='root')


@api.route('/test')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

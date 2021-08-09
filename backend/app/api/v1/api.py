#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: api.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/8/8 5:37 PM
"""

from fastapi import APIRouter

from app.api.v1.endpoints import root

api_v1 = APIRouter()
api_v1.include_router(root.router, tags=["root"])

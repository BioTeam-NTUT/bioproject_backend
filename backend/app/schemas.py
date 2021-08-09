#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: schemas.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/8/8 5:46 PM
"""

from pydantic import BaseModel


class SimpleResponse(BaseModel):
    code: int = 200
    msg: str

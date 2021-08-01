#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: protein.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/7/24 12:23 PM
"""
from flask import Blueprint, request, abort, current_app as app

protein = Blueprint("protein", __name__)


@protein.route("/submit", methods=["POST"])
def submit():
    if len(request.form) == 0:
        app.logger.info("Bad Request")
        abort(400, "Invalid request, it should be formData format")
    form = request.form
    return form

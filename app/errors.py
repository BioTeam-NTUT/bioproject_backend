#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: errors.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/7/24 1:17 PM
"""
from flask import jsonify
from flask import current_app as app

from werkzeug.exceptions import HTTPException


def _get_formatted_error_message(code, name, description):
    return {
        "status": code,
        "name": name,
        "description": description
    }


def handle_known_error(error: HTTPException):
    """Return JSON instead of HTML for HTTP errors."""
    data = _get_formatted_error_message(error.code, error.name, error.description)
    return jsonify(data), error.code


def handler_unknown_error(error: Exception):
    # pass through HTTP errors
    if isinstance(error, HTTPException):
        return error
    data = _get_formatted_error_message(500, "Internal Server Error", "We can't handle this request, please try again "
                                                                      "later")
    app.logger.exception(f"{error.__class__.__name__}: {error}")
    return jsonify(data), 500

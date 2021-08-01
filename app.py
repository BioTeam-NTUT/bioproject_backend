#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: app.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/5/11 11:16 AM
"""
import logging
from logging import getLogger
from logging.handlers import TimedRotatingFileHandler

from flask import request
from flask.logging import default_handler
from werkzeug.exceptions import HTTPException, InternalServerError

from app import app, config
from app.routes import api_v1
from app.errors import handle_known_error, handler_unknown_error

from Bio.Blast import NCBIWWW
from Bio import ExPASy
from Bio import SwissProt

app.register_blueprint(api_v1, url_prefix="/api/v1")
app.register_error_handler(HTTPException, handle_known_error)
app.register_error_handler(Exception, handler_unknown_error)

getLogger('sqlalchemy').addHandler(default_handler)
formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(module)s.%(funcName)s] - %(message)s")
handler = TimedRotatingFileHandler(config.LOG_PATH + "/root.log", when="D", encoding="UTF-8")
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.WARN)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/blast")
def blast():
    query = request.args.get("query")
    if query is None:
        return "fail"
    result = NCBIWWW.qblast("blastp", "swissprot", query)
    return result.read()


@app.route("/uniprot")
def uniprot():
    query = request.args.get("query")
    if query is None:
        return "fail"
    result = ExPASy.get_sprot_raw(query)
    record = SwissProt.read(result)
    return record.entry_name


if __name__ == "__main__":
    app.run()

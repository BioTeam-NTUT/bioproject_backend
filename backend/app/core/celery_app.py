#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: celery_app.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/8/8 5:08 PM
"""

# Both web and worker use this script for setting celery client
from app.core.configs.config import settings
from celery import Celery

celery_app = Celery(
    main="tasks", backend=settings.REDIS_URI, broker=settings.RABBITMQ_URI
)

celery_app.conf.task_routes = {"app.worker.*": {"queue": "main-queue"}}
celery_app.conf.timezone = "Asia/Taipei"

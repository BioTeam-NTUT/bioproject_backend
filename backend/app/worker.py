#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: worker.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/8/8 5:22 PM
"""

from celery.utils.log import get_task_logger

from app.core.celery_app import celery_app

logger = get_task_logger(__name__)


@celery_app.task(name="test_celery", acks_late=True)
def test_celery(word: str) -> str:
    logger.info(f"test task return {word}")
    return f"test task return {word}"

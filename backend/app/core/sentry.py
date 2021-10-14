#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: sentry.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/8/8 4:53 PM
"""
from typing import Any, List, Optional

import sentry_sdk

from app.core.configs.web_config import settings


def set_up_sentry(integrations: Optional[List[Any]] = None):
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        integrations=integrations,
        traces_sample_rate=settings.TRACE_SAMPLE_RATE,
    )

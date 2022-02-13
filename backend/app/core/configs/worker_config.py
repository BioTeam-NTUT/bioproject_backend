#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    File name: worker_config.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/10/13 12:31 AM
"""

from app.core.configs.config import Settings


class WorkerSettings(Settings):
    """Worker configuration."""

    class Config:
        env_file = ".env"


settings = WorkerSettings()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: web_config.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/10/12 11:17 PM
"""

from typing import List, Union

from pydantic import AnyHttpUrl, validator

from app.core.configs.config import Settings


class WebSettings(Settings):
    """Web configuration."""

    PROJECT_NAME: str
    API_V1_PREFIX: str = "/api/v1"

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
        cls, v: Union[str, List[str]]
    ) -> Union[str, List[str]]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        env_file = ".env"


settings = WebSettings()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: config.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/5/11 11:17 AM
"""

import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import (
    AnyHttpUrl,
    BaseSettings,
    EmailStr,
    HttpUrl,
    PostgresDsn,
    RedisDsn,
    validator,
)


class Settings(BaseSettings):
    """Base configuration."""

    PROJECT_NAME: str
    API_V1_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    EMAIL_ADDRESS: EmailStr
    SENTRY_DSN: HttpUrl
    TRACE_SAMPLE_RATE: float = 1.0

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn]

    REDIS_SERVER: str
    REDIS_PASSWORD: str
    REDIS_DB: str
    REDIS_URI: Optional[RedisDsn]

    RABBITMQ_SERVER: str
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_URI: Optional[str]

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB')}",
        )

    @validator("REDIS_URI", pre=True)
    def assemble_redis_uri(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return RedisDsn.build(
            scheme="redis",
            password=values.get("REDIS_PASSWORD"),
            host=values.get("REDIS_SERVER"),
            path=f"/{values.get('REDIS_DB')}",
        )

    @validator("RABBITMQ_URI", pre=True)
    def assemble_rabbitmq_uri(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        return f"amqp://{values.get('RABBITMQ_USER')}:{values.get('RABBITMQ_PASSWORD')}@{values.get('RABBITMQ_SERVER')}:5672//"  # noqa: E501

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[str, List[str]]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()

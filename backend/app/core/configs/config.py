#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: config.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/5/11 11:17 AM
"""

import secrets
from typing import Any, Dict, Optional

from pydantic import BaseSettings, EmailStr, HttpUrl, PostgresDsn, RedisDsn, validator


class Settings(BaseSettings):
    """Base configuration."""

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ENV: str = "production"

    EMAIL_ADDRESS: EmailStr
    SENTRY_DSN: HttpUrl
    TRACE_SAMPLE_RATE: float = 1.0

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn]

    REDIS_SERVER: str
    REDIS_PASSWORD: str
    REDIS_DB: str
    REDIS_PORT: str
    REDIS_URI: Optional[RedisDsn]

    RABBITMQ_SERVER: str
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_PORT: str
    RABBITMQ_URI: Optional[str]

    def is_development_enabled(self):
        return self.ENV.lower() == "development"

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
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
            port=values.get("REDIS_PORT"),
            path=f"/{values.get('REDIS_DB')}",
        )

    @validator("RABBITMQ_URI", pre=True)
    def assemble_rabbitmq_uri(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        return f"amqp://{values.get('RABBITMQ_USER')}:{values.get('RABBITMQ_PASSWORD')}@{values.get('RABBITMQ_SERVER')}:{values.get('RABBITMQ_PORT')}//"  # noqa: E501

    class Config:
        env_file = ".env"


settings = Settings()

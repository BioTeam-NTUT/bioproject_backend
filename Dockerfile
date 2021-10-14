FROM python:3.7-slim-buster
LABEL maintainer="guyleaf <ychhua1@gmail.com>"

COPY backend /backend

WORKDIR /backend

ENV BUILD_DEPS="build-essential" \
    APP_DEPS="curl libpq-dev"

RUN apt-get update \
    && apt-get install -y ${BUILD_DEPS} ${APP_DEPS} --no-install-recommends \
    && pip install poetry \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/doc && rm -rf /usr/share/man \
    && apt-get purge -y --auto-remove ${BUILD_DEPS} \
    && apt-get clean

ENV PYTHONUNBUFFERED="true"

RUN poetry install

ARG FASTAPI_PORT=8000
EXPOSE ${FASTAPI_PORT}

CMD ["uvicorn", "app.main:app"]

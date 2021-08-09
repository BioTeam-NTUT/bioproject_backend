import uvicorn
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.api import api_v1
from app.core.config import settings
from app.core.sentry import set_up_sentry

set_up_sentry()
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_PREFIX}/openapi.json"
)


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_v1, prefix=settings.API_V1_PREFIX)
app = SentryAsgiMiddleware(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

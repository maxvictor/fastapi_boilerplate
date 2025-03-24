from fastapi import FastAPI

from app.core.config import settings
from app.core.logging_config import configure_logging
from app.presentation.routers.api_router import api_router

configure_logging()

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router)

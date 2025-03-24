from fastapi import APIRouter

from app.core.config import settings
from app.presentation.routers.v1 import post_router

api_router = APIRouter()
api_router.include_router(
    post_router.router, prefix=settings.API_V1_STR + "/posts", tags=["Posts"]
)

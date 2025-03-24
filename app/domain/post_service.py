# app/domain/post_service.py
from typing import List

from app.data.schemas.post_schema import PostOut
from app.gateways.external_api import fetch_posts


def get_external_posts() -> List[PostOut]:
    posts_data = fetch_posts()
    return [PostOut(**post) for post in posts_data[:20]]


def create_mocked_post(payload) -> PostOut:
    return PostOut(id=99, **payload.dict())

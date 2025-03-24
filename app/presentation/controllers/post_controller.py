# app/presentation/controllers/post_controller.py
from app.data.schemas.post_schema import PostCreate
from app.domain import post_service


def list_posts():
    return post_service.get_external_posts()


def create_post(payload: PostCreate):
    return post_service.create_mocked_post(payload)

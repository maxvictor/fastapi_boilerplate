from typing import List

from fastapi import APIRouter

from app.data.schemas.post_schema import PostCreate, PostOut
from app.presentation.controllers import post_controller

router = APIRouter()


@router.get("/", response_model=List[PostOut])
def get_posts():
    return post_controller.list_posts()


@router.post("/", response_model=PostOut, status_code=201)
def create_post(payload: PostCreate):
    return post_controller.create_post(payload)

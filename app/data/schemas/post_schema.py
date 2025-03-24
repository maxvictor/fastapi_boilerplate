from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    body: str


class PostOut(PostCreate):
    id: int

    model_config = {"from_attributes": True}

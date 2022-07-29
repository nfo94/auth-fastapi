from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: int = Field(default=None)

    class Config:
        schema_extra = {
            "post_demo": {"title": "example title", "content": "example content"}
        }

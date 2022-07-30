from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: int = Field(default=None)

    class Config:
        schema = {"post_demo": {"title": "example title", "content": "example content"}}


class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema = {
            "user_demo": {
                "name": "example name",
                "email": "example email",
                "password": "example password",
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema = {
            "user_demo": {
                "email": "example email",
                "password": "example password",
            }
        }

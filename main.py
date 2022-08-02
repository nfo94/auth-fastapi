from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import sign_jwt
from app.auth.jwt_bearer import jwt_bearer

posts = [
    {"id": 1, "title": "Elden Ring", "text": "Elden Ring is the best game ever"},
    {"id": 2, "title": "Dark Souls", "text": "Dark Souls is awesome"},
]

users = []

app = FastAPI()


@app.get("/", tags=["test"])
def greet():
    return {"Hello": "World"}


@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}


@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return {"error": "This post does not exist"}
    for post in posts:
        if post["id"] == id:
            return {"data": post}


@app.post("/posts", dependencies=[Depends(jwt_bearer())], tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"info": "Post added"}


@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return sign_jwt(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return sign_jwt(user.email)
    return {"error": "Invalid login details"}

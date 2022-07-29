import uvicorn
from fastapi import FastAPI
from app.model import PostSchema


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
def get_post(id: int):
    def get_one_post(id: int):
        if id > len(posts):
            return {"error": "This post does not exist"}
        for post in posts:
            if post["id"] == id:
                return {"data": post}


@app.post("/posts", tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"info": "Post added"}

# https://www.youtube.com/watch?v=0_seNFCtglk

import jwt
import uvicorn
import pydantic
from decouple import config
from jwt_handler import signJWT
from fastapi import FastAPI, Body
from email_validator import validate_email
from model import PostSchema, UserSchema, UserLoginSchema
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr
from jwt_handler import signJWT, decodeJWT


posts = [
    {
        "id": 1,
        "title": "penguins",
        "text": "Penfuins are a group of aquatic flightless birds." 
    }
]

users = []

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

app = FastAPI()
# Instance of FastAPI classes

# 1 Get - for testing
@app.get("/", tags = ["test"])
def greet():
    return {"Hello":"World!"}

# 2 Get Posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data":posts}

# 3 Get single post {id}
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return {
            "error" : "Post with this ID does not exist!"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data":post
            }

# 4 Post a blog post [A handler for creating a post]
@app.post("/posts", tags=["posts"])
def add_post(post : PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info":"Post Added!"
    }

# 5 USer Signup [ Create a new user ]
@app.post("/user/signup", tags=["user"])
def user_signup(user : UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

@app.post("/user/login", tags=["user"])
def user_login (user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error":"Invalid login details!"
        }   
    
# uvicorn main:app --reload
# 38:57


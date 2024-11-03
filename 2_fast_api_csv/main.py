# https://www.youtube.com/watch?v=0_seNFCtglk

import jwt
import uvicorn
import pydantic
from decouple import config
from jwt_handler import signJWT
from fastapi import FastAPI, Body, Query
from email_validator import validate_email
from model import PostSchema, UserSchema, UserLoginSchema, get_db, Post, PostSchema_Response
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, EmailStr
from jwt_handler import signJWT, decodeJWT
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder 
import csv
from typing import List

# from app.auth.jwt_handler import signJWT
from jwt_handler import signJWT
# from app.auth.jwt_bearer import jwtBearer
from jwt_bearer import jwtBearer

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
@app.post("/posts", dependencies=[Depends(jwtBearer())],  tags=["posts"])
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
    
@app.post("/posts/", response_model=PostSchema_Response)
def create_post(post: PostSchema, db: Session = Depends(get_db)):
    db_item = Post(**post.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return PostSchema_Response(**jsonable_encoder(db_item))

#######################################

CSV_FILE_PATH = 'posts.csv'

def read_csv():
    posts = []
    try:
        with open(CSV_FILE_PATH, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                posts.append({
                    "id": int(row["id"]),
                    "title": row["title"],
                    "content": row["content"]
                })
    except FileNotFoundError:
        # File doesn't exist yet, return empty list
        return []
    return posts

def write_csv(posts: List[dict]):
    with open(CSV_FILE_PATH, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "content"])
        writer.writeheader()
        writer.writerows(posts)

@app.post("/posts_csv/", response_model=PostSchema_Response)
def create_post(post: PostSchema):
    posts = read_csv()
    
    new_id = max([p["id"] for p in posts], default=0) + 1
    new_post = {
        "id": new_id,
        "title": post.title,
        "content": post.content
    }
    
    posts.append(new_post)
    write_csv(posts)
    
    return PostSchema_Response(**new_post)

"""
@app.get("/items/", response_model=List[Item],
                    tags=["items"], 
                    summary="Retrieve a list of items", 
                    description="Get a list of items with optional query parameters.")
"""
@app.get("/posts_csv/",  response_model=List[PostSchema_Response], tags=["gets_csv"], description="Get a list of csv")
def get_all():
    posts = read_csv()
    # [PostSchema_Response(**post) for post in posts]
    return posts


@app.get("/posts_csv/{post_id}", response_model=PostSchema_Response)
def get_post(post_id: int):
    posts = read_csv()
    for post in posts:
        if post["id"] == post_id:
            return post
            #return PostSchema_Response(**post)
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/posts/{post_id}", response_model=PostSchema_Response)
def update_post(post_id: int, updated_post: PostSchema):
    posts = read_csv()
    for post in posts:
        if post["id"] == post_id:
            post["title"] = updated_post.title
            post["content"] = updated_post.content
            write_csv(posts)
            return PostSchema_Response(**post)
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{post_id}", response_model=dict)
def delete_post(post_id: int):
    posts = read_csv()
    posts = [post for post in posts if post["id"] != post_id]
    write_csv(posts)
    return {"detail": "Post deleted"}

######################################
### how the Response_Model work it ###
######################################

@app.get("/Response_Model_work_it/",  response_model=List[PostSchema_Response], tags=["gets_csv"], description="Get a list of csv")
def get_response_model_work_it( ):
#def get_response_model_work_it(item : List[PostSchema_Response]):
    posts = read_csv()
    #[PostSchema_Response(**post) for post in posts]
    #print(posts)
    #return posts
    return [PostSchema_Response(**post) for post in posts]

from fastapi import FastAPI
from pydantic import BaseModel, Field

# import all you need from fastapi-pagination
from fastapi_pagination import Page, add_pagination, paginate
from fastapi_pagination.links import Page

class UserOut(BaseModel):  # define your model
    name: str = Field(..., example="Steve")
    surname: str = Field(..., example="Rogers")

users: List[UserOut] = [
    UserOut(name="John Doe", surname="john-doe@example.com"),
    UserOut(name="Maria Doe", surname="john-doe@example.com"),
    UserOut(name="Pedro Doe", surname="john-doe@example.com"),
    UserOut(name="Liam Doe", surname="john-doe@example.com"),
    UserOut(name="John Doe", surname="john-doe@example.com")
]

@app.get('/users_pagination/')  
#async def get_users() -> Page[UserOut]:  # use Page[UserOut] as return type annotation
def get_users() -> Page[UserOut]:
# def get_users() -> LimitOffsetPage[UserOut]:
    return paginate(users)  # use paginate function to paginate your data

add_pagination(app) 


@app.get("/get_items_csv_limited/")
async def get_items(limit: int = Query(10, le=100)):
    """
    Returns a list of numbers up to the specified limit.

    - **limit**: The maximum number of items to return. Defaults to 10, and is capped at 100.
    """
    data = read_csv()
    # Limit the number of items returned
    limited_data = data[:limit]
    #return {"items": limited_data, "limit": limit}
    return limited_data



#ItemResponse(**jsonable_encoder(db_item))
# uvicorn main:app --reload
# 38:57







'''
#from fastapi import FastAPI, Depends, HTTPException, status
#from fastapi.security import OAuth2PasswordBearer
#from pydantic import BaseModel

#app = FastAPI()

# Initialize JWT handler
jwt_handler = signJWT(secret_key="your-secret-key-here")  # Use a secure secret key in production

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt_handler.verify_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )
        return User(username=username)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

@app.post("/token", response_model=Token)
def login(username: str):
    # In a real app, you would verify credentials here
    access_token = jwt_handler.create_access_token(
        data={"sub": username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
    '''


'''
import time
import jwt
from decouple import config
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def token_response(token: str):
    return {"access_token": token}

def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expires": time.time() + 600  # Token expiration time
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if decoded_token["expires"] >= time.time():
            return decoded_token
        else:
            raise jwt.ExpiredSignatureError("Token has expired")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

class User(BaseModel):
    id: str
    password: str

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = decodeJWT(token)
    return user

@app.post("/login")
async def login(user_data: User):
    if user_data.id == "your_username" and user_data.password == "your_password":
        token = signJWT(user_data.id)
        return token_response(token)
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/protected_route")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello, {current_user['userID']}!"}
    '''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)


# Create tables
Base.metadata.create_all(bind=engine)



class PostSchema(BaseModel):
    title : str = Field(default=None)
    content : str = Field(default=None)
    class Config:
        schema_extra = {
            "post_demo" : {
                "title":"some title about animals",
                "content":"some content about animals",
            }
        }

class PostSchema_Response(BaseModel):
    id : int = Field(default=None)
    title : str = Field(default=None)
    content : str = Field(default=None)
    class Config:
        schema_extra = {
            "post_demo" : {
                "title":"some title about animals",
                "content":"some content about animals",
            }
        }




class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default = None)
    password : str = Field(default = None)
    class Config:
        #the_schema 
        json_schema_extra = {
            "user_demo" : {
                "name" : "Bek",
                "email" : "help@bekbrace.com",
                "password" : "123"
            }
        }


class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default = None)
    password : str = Field(default = None)
    class Config:
        #the_schema 
        json_schema_extra = {
            "user_demo" : {
                "email" : "help@bekbrace.com",
                "password" : "123"
            }
        }
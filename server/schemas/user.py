from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserSchemas(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    firstname: str = Field(...)
    lastname: str = Field(...)
    password: str = Field(...)
    avatar: str = Field(...)


class UserCreateReqModel(BaseModel):
    username: str
    email: EmailStr
    firstname: str
    lastname: str
    password: str
    avatar: str


class UserUpdateReqModel(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    password: Optional[str]
    repassword: Optional[str]
    avatar: Optional[str]

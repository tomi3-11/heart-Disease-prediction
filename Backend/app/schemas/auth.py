from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    role: Literal["admin", "doctor", "nurse"] = "doctor"


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str

    model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str

from pydantic import BaseModel
from typing import Annotated
from pydantic import Field, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: Annotated[str, Field(min_length=3, max_length=50)]
    email: EmailStr
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str



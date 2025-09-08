from pydantic import BaseModel, ConfigDict
from typing import Annotated
from pydantic import Field, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserBase(BaseModel):
    id: int | None = None 
    username: Annotated[str, Field(min_length=3, max_length=50)]
    email: EmailStr
    full_name: str | None = None
    disabled: bool | None = None
class UserCreate(BaseModel):
    username: Annotated[str, Field(min_length=3, max_length=50)]
    email: EmailStr
    password: str  

class User(UserBase):
    id: int  
    model_config = ConfigDict(from_attributes=True)
    
class UserInDB(User):
    id: int | None = None 
    hashed_password: str
    model_config = ConfigDict(from_attributes=True)

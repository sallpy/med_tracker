from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime


class User(BaseModel):
    username: str
    password: str
    email: EmailStr


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, v):
        """
        Validate that password is at least 8 characters long.
        """
        if len(v) < 8:
            raise ValueError("Password must be < than 8 characters")
        return v


class UserIn(User):
    id: int


class AnalysisBase(BaseModel):
    type_of_analysis: str
    type_of_test: str
    due_date: datetime
    result: float

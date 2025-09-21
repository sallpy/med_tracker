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


class AnalysisBase(BaseModel):
    type_of_analysis: str
    type_of_test: str
    due_date: datetime
    result: float

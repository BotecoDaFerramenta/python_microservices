from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from enum import Enum
from datetime import date


class User(BaseModel):
    id: UUID
    username: str
    password: str
    passphrase: str


class UserType(str, Enum):
    admin = "admin"
    teacher = "teacher"
    alumni = "alumni"
    student = "student"


class UserProfile(BaseModel):
    firstname: str
    lastname: str
    middle_initial: str
    age: Optional[int] = 0
    salary: Optional[int] = 0
    birthday: date
    user_type: UserType

from pydantic import validator, UUID4
from typing import Optional
from utils.models_loads import get_users_model
from ninja import Schema
from src.schemas.schemas import CustomBadRequest
from typing import Optional

class UserInput(Schema):
    name: Optional[str]
    email: str 
    password: Optional[str]

    @validator("email", pre=True, always=True)
    def email_must_be_unique(cls, email):
        if get_users_model().objects.filter(email=email).exists():
            raise CustomBadRequest("Email already exists.")
        return email

    @validator("email", pre=True, always=True)
    def email_max_length(cls, email):
        if len(email) > 100:
            raise CustomBadRequest("Email must be shorter than 100 characters")
        return email

    @validator("password", pre=True, always=True)
    def check_password_length(cls, password):
        if len(password) < 8:
            raise CustomBadRequest("Password must be longer than 8 characters")
        if len(password) > 128:
            raise CustomBadRequest("Password must be shorter than 128 characters")
        return password

    @validator("name", pre=True, always=True)
    def name_max_length(cls, name):
        if len(name) > 40:
            raise CustomBadRequest("Name must be shorter than 40 characters")
        return name

class UserLogin(Schema):
    name: Optional[str]
    email: str 
    password: str

    @validator("email", pre=True, always=True)
    def email_must_be_exist(cls, email):
        if get_users_model().objects.filter(email=email).exists():
            return email
        raise CustomBadRequest("The credentials provided are invalid.")

class UserOutput(Schema):
    id: UUID4
    name: str
    email: str
    token: Optional[UUID4]

class UserPhoneInput(Schema):
    token: str
    
class UserPhoneOutput(Schema):
    id: UUID4
    user: UserOutput
    token: str

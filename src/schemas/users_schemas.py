from pydantic import validator, UUID4
from typing import Optional
from utils.models_loads import get_users_model, get_userPhone_model
from ninja.orm import create_schema
from ninja import Schema
from src.schemas.schemas import CustomBadRequest
from typing import Optional

class UserInput(Schema):
    name: Optional[str]
    email: str 
    password: str

    @validator("email", pre=True, always=True)
    def email_must_be_unique(cls, email):
        if get_users_model().objects.filter(email=email).exists():
            raise CustomBadRequest("Email already exists.")
        return email
    
    @validator("password", pre=True, always=True)
    def password_must_has_8_chars(cls, password):
        if len(password) < 8:
            raise CustomBadRequest("Password must be longer than 8 characters")
        return password
    
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
    users_id: UUID4
    token: str
    
class UserPhoneOutput(Schema):
    id: UUID4
    user: UserOutput
    token: str

class PhoneEventOutput(Schema):
    id: UUID4
    user_phone: UserPhoneOutput
    frequency: int
    event_type: str
    message: str

class PhoneEventInput(Schema):
    frequency: int
    event_type: str
    message: str


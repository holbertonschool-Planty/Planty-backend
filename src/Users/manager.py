from src.schemas.schemas import CustomBadRequest
from utils.models_loads import get_phoneEvent_model, get_usersToken_model, get_userPhone_model, get_users_model
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate
from uuid import UUID
from django.db.models import QuerySet
from typing import List
from src.schemas import users_schemas
from django.contrib.auth.models import BaseUserManager
from django.db.models import manager


class UsersManager(BaseUserManager):
    def get_queryset(self):
        return QuerySet(self.model, using=self._db).exclude(is_deleted=True)

    def create_user(self, **data):
        if not data["email"] or not data["password"]:
            raise ValueError('The credentials must be set')
        data["email"] = self.normalize_email(data["email"])
        user = self.model(**data)
        user.set_password(data["password"])
        user.save(using=self._db)
        return user

    def register_user(self, data: dict):
        user_obj = self.create_user(**data)
        return 201, user_obj
   
    def login_user(self, data: users_schemas.UserLogin):
        user = authenticate(email=data.email, password=data.password)
        if user:
            user_token, _ = get_usersToken_model().objects.get_or_create(user=user)
            return 200, self.create_schema(user, user_token.token)
        else:
            raise CustomBadRequest("Invalid credentials")

    def update_user(self, users_id:UUID, data: users_schemas.UserInput):
        user_obj = get_object_or_404(self.model, id=users_id)
        user_obj.name = data.name
        user_obj.save()
        return 200, user_obj

    def delete_user(self, users_id: UUID):
        user_obj = get_object_or_404(self.model, id=users_id)
        user_obj.delete()
        return 200, {"message": "User deleted succesfully"}

    def create_schema(self, user_obj: users_schemas.UserInput, user_token= None):
        return users_schemas.UserOutput(
            id=user_obj.id,
            name=user_obj.name,
            email=user_obj.email,
            token=user_token)

class UsersPhoneManager(manager.Manager):

    def get_tokens_by_user(self, users_id: UUID):
        user_obj = get_object_or_404(get_users_model(), id=users_id)
        list_token = []
        tokens = self.all().filter(users_id=users_id)
        for token in tokens:
            list_token.append(self.create_schema(user_obj, token))
        return 200, list_token

    def save_token(self, users_id: UUID, user_phone_token: str):
        user_obj = get_object_or_404(get_users_model(), id=users_id)
        if get_userPhone_model().objects.filter(user_id=users_id, token=user_phone_token).exists():
            raise CustomBadRequest(f"Token of the user {user_obj.name} already exists.")
        userPhone_obj = self.model(user=user_obj, token=user_phone_token)
        userPhone_obj.save()
        return 201, userPhone_obj
    
    def delete_token(self, users_id: UUID, user_phone_token: str):
        userPhone_obj = get_object_or_404(get_userPhone_model(), user_id=users_id, token=user_phone_token)
        userPhone_obj.delete()
        return 200, {"message": "User deleted succesfully"}




class PhoneEventManager(manager.Manager):

    def create_event(self, userPhone_obj: users_schemas.UserPhoneOutput, data: dict ):
        data["user_phone"] = userPhone_obj
        phoneEvent_obj = self.create(**data)
        return phoneEvent_obj
    
    def delete_event(self, phoneEvent_obj: users_schemas.PhoneEventOutput):
        phoneEvent_obj.delete()
        return {"message": "User deleted succesfully"}

    def delete_events(self, users_id: UUID, user_phone_token: str):
        userPhone_obj = get_object_or_404(get_userPhone_model(), user_id=users_id, token=user_phone_token)
        list_events = get_list_or_404(get_phoneEvent_model(), user_phone=userPhone_obj)
        list_events_removed = []
        for event in list_events:
            list_events_removed.append(self.delete_event(event))
        return 200, list_events_removed

from src.schemas.schemas import CustomBadRequest
from utils.models_loads import get_usersToken_model, get_userPhone_model, get_users_model
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from uuid import UUID
from django.db.models import QuerySet
from src.schemas import users_schemas
from django.contrib.auth.models import BaseUserManager
from src.base.manager import BaseManager


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
        return 201, self.create_schema(user_obj)
   
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
        return 200, self.create_schema(user_obj)

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

class UsersPhoneManager(BaseManager):

    def get_tokens_by_user(self, users_id: UUID):
        user_obj = get_object_or_404(get_users_model(), id=users_id)
        list_token = []
        tokens = self.all().filter(users_id=users_id)
        for token in tokens:
            list_token.append(self.create_schema(user_obj, token))
        return 200, list_token

    def save_token(self, users_id: UUID, user_phone_token: str):
        user_obj = get_object_or_404(get_users_model(), id=users_id)
        if get_userPhone_model().objects.filter(users_id=users_id, token=user_phone_token).exists():
            raise CustomBadRequest(f"Token of the user {user_obj.name} already exists.")
        userPhone_obj = self.model(users_id=user_obj, token=user_phone_token)
        userPhone_obj.save()
        return 201, self.create_schema(user_obj, userPhone_obj)
    
    def delete_token(self, users_id: UUID, user_phone_token: str):
        userPhone_obj = get_object_or_404(get_userPhone_model(), users_id=users_id, token=user_phone_token)
        userPhone_obj.delete()
        return 200, {"message": "User deleted succesfully"}

    def create_schema(self, user_obj: users_schemas.UserInput, userPhone_obj: users_schemas.UserPhoneInput):
        return users_schemas.UserPhoneOutput(
            id=userPhone_obj.id,
            user=get_users_model().objects.create_schema(user_obj),
            token=userPhone_obj.token
        )
from django.db.models.manager import Manager
from src.schemas.schemas import CustomBadRequest
from utils.models_loads import get_users_model
from django.shortcuts import get_object_or_404
from uuid import UUID
from src.schemas import users_schemas

class UsersManager(Manager):

    def create_user(self, data: dict):
        user_obj = self.create(**data)
        return 201, self.create_schema(user_obj)

    def login_user(self, data: users_schemas.UserLogin):
        user_obj = get_object_or_404(self.model, email=data.email)
        if user_obj.password == data.password:
            return 200, self.create_schema(user_obj)
        else:
            return CustomBadRequest("Email doest not exist.")

    def update_user(self, users_id:UUID, data: users_schemas.UserInput):
        user_obj = get_object_or_404(self.model, id=users_id)
        user_obj.name = data.name
        user_obj.save()
        return 200, self.create_schema(user_obj)

    def delete_user(self, users_id: UUID):
        user_obj = get_object_or_404(self.model, id=users_id)
        user_obj.delete()
        return 200, {"message": "User deleted succesfully"}

    def create_schema(self, user_obj: users_schemas.UserInput):
        return users_schemas.UserOutput(
            id=user_obj.id,
            name=user_obj.name,
            email=user_obj.email)
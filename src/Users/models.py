from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from src.Users.manager import UsersManager, UsersPhoneManager
from src.base.models import BaseModel
import uuid

class Users(AbstractBaseUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    objects = UsersManager()
    USERNAME_FIELD = 'email'

    is_deleted = models.BooleanField(default=False)

    def delete(self): 
        self.is_deleted = True 
        self.save()

class UserToken(BaseModel):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)



class UserPhone(BaseModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    token = models.CharField(unique=True)
    objects = UsersPhoneManager()

from django.db import models
from src.Users.manager import UsersManager
import uuid

class Users(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=40)
    objects = UsersManager()

    class Meta:
        verbose_name= 'User'
        verbose_name_plural= 'Users'
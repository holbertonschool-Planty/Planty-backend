from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.timezone import now
from src.Users.manager import UsersManager, UsersPhoneManager, PhoneEventManager
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

class UserToken(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)


class UserPhone(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    token = models.CharField(unique=True)
    objects = UsersPhoneManager()

EVENT_TYPE_CHOICES = [
    ('TYPE_1', 'Tipo de Evento 1'),
    ('TYPE_2', 'Tipo de Evento 2'),
    ('TYPE_3', 'Tipo de Evento 3'),
    ('TYPE_4', 'Tipo de Evento 4'),
    ('TYPE_5', 'Tipo de Evento 5'),
]

class UserPhoneEvent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user_phone = models.ForeignKey(UserPhone, on_delete=models.CASCADE)
    last_event_date = models.DateField(default=now)
    frequency = models.IntegerField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES)
    message = models.CharField(max_length=100)
    objects = PhoneEventManager()
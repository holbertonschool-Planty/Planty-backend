from django.db import models
from src.Users.models import Users
from src.User_devices.manager import UserPlantyManager
from src.Devices.models import Planty
import uuid

class Users_planty(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    plant_name = models.CharField()
    image_url = models.URLField(blank=True)
    location = models.CharField(default="room")
    color_card = models.CharField(max_length=7, default="#38CE61")
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    planty = models.ForeignKey(Planty, on_delete=models.CASCADE)
    objects = UserPlantyManager()

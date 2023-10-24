from django.db import models
from django.contrib.postgres.fields import ArrayField
from src.Plants.models import Plants_info
from src.Devices.manager import DeviceManager
from uuid import uuid4

# Create your models here.

class Planty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    serie = models.CharField(unique=True)
    actual_temperature = ArrayField(base_field=models.PositiveSmallIntegerField())
    actual_light = ArrayField(base_field=models.PositiveSmallIntegerField())
    actual_watering = ArrayField(base_field=models.PositiveSmallIntegerField())
    plants_info = models.ForeignKey(Plants_info, on_delete=models.CASCADE, blank=True, null=True)
    objects = DeviceManager()

from django.db import models
from django.contrib.postgres.fields import ArrayField
from src.base.models import BaseModel
from src.Plants.models import Plants_info
from src.Devices.manager import DeviceManager
from uuid import uuid4

# Create your models here.

class Planty(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    serie = models.CharField(unique=True)
    actual_temperature = ArrayField(base_field=models.PositiveSmallIntegerField())
    actual_light = ArrayField(base_field=models.PositiveSmallIntegerField())
    actual_watering = ArrayField(base_field=models.PositiveSmallIntegerField())
    plants_info_id = models.ForeignKey(Plants_info, on_delete=models.CASCADE)
    objects = DeviceManager()

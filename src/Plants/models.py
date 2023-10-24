from django.db import models
from src.Plants.manager import PlantManager
from uuid import uuid4

# Create your models here.

class Plants_info(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    scientific_name = models.CharField(unique=True, max_length=100)
    station = models.CharField(max_length=40)
    temperature = models.PositiveSmallIntegerField()
    light = models.PositiveSmallIntegerField()
    watering = models.PositiveSmallIntegerField()
    objects = PlantManager()

from typing import List
from src.schemas.plants_info_schemas import PlantsInfoInput
from uuid import UUID
from django.db.models import Manager
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError

class PlantManager(Manager):

    def create_plant(self, data: PlantsInfoInput):
        self.validate_values([data.temperature, data.light, data.watering, data.water_frequency])
        plant_obj = self.create(**dict(data))
        return plant_obj

    def create_plants(self, data: List[PlantsInfoInput]):
        list_plants = [] 
        for plant in data:
            list_plants.append(self.create_plant(plant))
        return 201, list_plants
    


    def update_plant(self, plant_id: UUID, data: PlantsInfoInput):
        self.validate_values([data.temperature, data.light, data.watering, data.water_frequency])
        plant_obj = get_object_or_404(self.model, id=plant_id)
        plant_obj.station = data.station
        plant_obj.temperature = data.temperature
        plant_obj.light = data.light
        plant_obj.watering = data.watering
        plant_obj.save()
        return 200, plant_obj

    def delete_plant(self, plant_id: UUID):
        plant_obj = get_object_or_404(self.model, id=plant_id)
        plant_obj.delete()
        return 200, {"message": "Plant information deleted successfully."}
    
    def validate_values(self, values: List[int]):
        for value in values:
            if value < 0:
                raise HttpError(400, 'The values must be positive')
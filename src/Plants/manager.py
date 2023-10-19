from django.db.models.manager import Manager
from src.schemas.plants_info_schemas import PlantsInfoInput, PlantsInfoOutput
from uuid import UUID
from src.base.manager import BaseManager
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError

class PlantManager(BaseManager):
    
    def create_schema(self, plant_obj: PlantsInfoInput):
        return PlantsInfoOutput(
            id=plant_obj.id,
            scientific_name=plant_obj.scientific_name,
            station=plant_obj.station,
            temperature=plant_obj.temperature,
            light=plant_obj.light,
            watering=plant_obj.watering)
    
    def get_list(self):
        plant_list = []
        plants = self.all()
        for plant in plants:
            plant_list.append(self.create_schema(plant))
        return 200, plant_list

    def create_plant(self, data: dict):
        plant_obj = self.create(**data)
        return 201, self.create_schema(plant_obj)
    
    def update_plant(self, plant_id: UUID, data: PlantsInfoInput):
        values = [data.temperature, data.light, data.watering]
        for value in values:
            if value < 0:
                raise HttpError(400, 'The value must be positive')
        plant_obj = get_object_or_404(self.model, id=plant_id)
        plant_obj.station = data.station
        plant_obj.temperature = data.temperature
        plant_obj.light = data.light
        plant_obj.watering = data.watering
        plant_obj.save()
        return 200, self.create_schema(plant_obj)
    
    def delete_plant(self, plant_id: UUID):
        plant_obj = get_object_or_404(self.model, id=plant_id)
        plant_obj.delete()
        return 200, {"message": "Plant information deleted successfully."}

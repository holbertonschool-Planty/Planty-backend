from src.schemas.plants_info_schemas import PlantsInfoInput
from uuid import UUID
from src.base.manager import BaseManager
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError

class PlantManager(BaseManager):

    def create_plant(self, data: dict):
        plant_obj = self.create(**data)
        return 201, plant_obj

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
        return 200, plant_obj

    def delete_plant(self, plant_id: UUID):
        plant_obj = get_object_or_404(self.model, id=plant_id)
        plant_obj.delete()
        return 200, {"message": "Plant information deleted successfully."}

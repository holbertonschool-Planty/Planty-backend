from src.base.manager import BaseManager
from uuid import UUID
from django.shortcuts import get_object_or_404
from utils.models_loads import get_plant_model
from src.schemas.planty_schemas import PlantyInput, PlantyOutput
from src.schemas.plants_info_schemas import PlantsInfoInput

class DeviceManager(BaseManager):
    
    def create_schema(self, planty_obj: PlantyInput, plant_obj: PlantsInfoInput):
        return PlantyOutput(
            id=planty_obj.id,
            serie=planty_obj.serie,
            actual_temperature=planty_obj.actual_temperature,
            actual_light=planty_obj.actual_light,
            actual_watering=planty_obj.actual_watering,
            plants_info = get_plant_model().objects.create_schema(plant_obj)
        )
        
    def create_planty(self, data: dict):
        plant_obj = get_object_or_404(get_plant_model(), id=data['plants_info_id'])
        data['plants_info_id'] = plant_obj
        data['actual_temperature'] = [data['actual_temperature']]
        data['actual_light'] = [data['actual_light']]
        data['actual_watering'] = [data['actual_watering']]
        planty_obj = self.model(**data)
        planty_obj.save()
        return 201, self.create_schema(planty_obj, plant_obj)

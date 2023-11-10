from django.db.models import Manager
from uuid import UUID, uuid4
from django.shortcuts import get_object_or_404
from utils.models_loads import get_plant_model
from src.schemas.planty_schemas import PlantyInput, PlantyOutput
from src.schemas.plants_info_schemas import PlantsInfoInput
from ninja.errors import HttpError


class DeviceManager(Manager):
    
    def create_planty(self, data: dict):
        if data.get('plants_info_id'):
            plant_obj = get_object_or_404(get_plant_model(), id=data.get('plants_info_id'))
            data['plants_info'] = plant_obj
        data['actual_temperature'] = [data.get('actual_temperature')]
        data['actual_light'] = [data.get('actual_light')]
        data['actual_watering'] = [data.get('actual_watering')]
        planty_obj = self.create(**data)
        return 201, planty_obj

    def delete_planty(self, planty_id: UUID):
        planty_obj = get_object_or_404(self.model, id=planty_id)
        planty_obj.delete()
        return 200, {"message": "Planty deleted successfully."}

    def update_planty(self, planty_id: UUID, data: PlantyInput):
        planty_obj = get_object_or_404(self.model, id=planty_id)
        planty_obj.actual_temperature = self.update_list(planty_obj.actual_temperature, data.actual_temperature)
        planty_obj.actual_light = self.update_list(planty_obj.actual_light, data.actual_light)
        planty_obj.actual_watering = self.update_list(planty_obj.actual_watering, data.actual_watering)
        planty_obj.save()
        return 200, planty_obj


    def update_plant_of_planty(self, planty_id: UUID, plants_info_id: UUID, timezone: int):
        planty_obj = get_object_or_404(self.model, id=planty_id)
        plant_info_obj = get_object_or_404(get_plant_model(), id=plants_info_id)
        setattr(planty_obj, "plants_info", plant_info_obj)
        setattr(planty_obj, "timezone", timezone)
        planty_obj.save()
        return planty_obj

    def create_empty_planty(self, plants_info_id: UUID, timezone: int):
        data = {}
        plant_info_obj = get_object_or_404(get_plant_model(), id=plants_info_id)
        data["plants_info"] = plant_info_obj
        data["timezone"] = timezone
        data["serie"] = uuid4()
        data["actual_temperature"] = self.create_list_twelve(plant_info_obj.temperature)
        data["actual_light"] = self.create_list_twelve(plant_info_obj.light)
        data["actual_watering"] = self.create_list_twelve(plant_info_obj.watering)
        planty_obj_id = self.create(**data)
        print(planty_obj_id)
        return planty_obj_id.id



    def create_list_twelve(self, number):
        sensor_list = []
        for _ in range(0, 12):
            sensor_list.append(number)
        return sensor_list
    
    def update_list(self, list, new_data):
        if new_data < 0:
            raise HttpError(400, 'The value must be positive')
        list.append(new_data)
        if len(list) > 12:
            list.pop(0)
        return list

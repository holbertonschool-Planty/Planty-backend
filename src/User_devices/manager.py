from uuid import UUID
from django.db.models import Manager
from django.shortcuts import get_object_or_404
from ninja import UploadedFile
from config.settings import IMAGE_DEFAULT
from src.schemas.user_devices_schemas import UserPlantyInput, UserPlantyOutput
from src.schemas.schemas import CustomBadRequest
from utils.firebase_helpers import upload_to_firebase, delete_from_firebase
from utils.models_loads import get_users_model, get_planty_model, get_userPlanty_model, get_plant_model

class UserPlantyManager(Manager):
    
    def create_planty_user(self, users_id: UUID, planty_id: UUID, data: dict, file: UploadedFile) -> UserPlantyOutput:
        user_obj = get_object_or_404(get_users_model(), id=users_id)
        planty_obj = get_object_or_404(get_planty_model(), id=planty_id)
        if get_userPlanty_model().objects.filter(user_id=users_id, planty_id=planty_id).exists():
            raise CustomBadRequest(f"The Planty of the user {user_obj.name} already exists.")
        data["user"] = user_obj
        data["planty"] = planty_obj
        if file:
            file_url = upload_to_firebase(file)
            data["image_url"] = file_url
        else:
            data["image_url"] = IMAGE_DEFAULT
        userPlanty_obj = self.create(**data)
        return userPlanty_obj

    def update_planty_user(self, user_planty_id: UUID, data: UserPlantyInput = None, plant_info_id: UUID = None, file: UploadedFile = None):
        userPlanty_obj = get_object_or_404(self.model, id=user_planty_id)
        if data:
            for attr, value in data.dict().items():
                setattr(userPlanty_obj, attr, value)
        if file:
            file_url = upload_to_firebase(file)
            userPlanty_obj.image_url = file_url
            delete_from_firebase(file)
        if plant_info_id:
            plant_info_obj = get_object_or_404(get_plant_model(), id=plant_info_id)
            setattr(userPlanty_obj.planty, "plants_info", plant_info_obj)
        userPlanty_obj.save()
        return 200, userPlanty_obj
    

    def delete_planty_user(self, user_planty_id: UUID):
        userPlanty_obj = get_object_or_404(self.model, id=user_planty_id)
        userPlanty_obj.delete()
        return 200, {"message": "Deleted sucesfully"}
    
    def check_values_of_planty(self, user_planty_id: UUID, alert_id: int):
        userPlanty_obj = get_object_or_404(self.model, id=user_planty_id)
        alerts = []

        if userPlanty_obj.planty.actual_temperature[-1] > userPlanty_obj.planty.plants_info.temperature + 8:
            alerts.append({
                'id': alert_id,
                'name': userPlanty_obj.plant_name,
                'info': 'The temperature is too high',
                'text': 'To keep your plants happy and healthy, we recommend adjusting the environmental temperature to a more suitable level. Ensure shade and, if possible, ventilate the area to reduce heat.',
                'imageSource': userPlanty_obj.image_url,
            })
            alert_id += 1  # Incrementamos el ID

        elif userPlanty_obj.planty.actual_temperature[-1] < userPlanty_obj.planty.plants_info.temperature - 6:
            alerts.append({
                'id': alert_id,
                'name': userPlanty_obj.plant_name,
                'info': 'The temperature is too low',
                'text': 'Your plants might be feeling cold. Make sure to maintain a warmer room temperature to promote healthy growth. Consider using gentle heating or thermal blankets if needed.',
                'imageSource': userPlanty_obj.image_url,
            })
            alert_id += 1  # Incrementamos el ID

        if userPlanty_obj.planty.actual_light[-1] > userPlanty_obj.planty.plants_info.light + 30:
            alerts.append({
                'id': alert_id,
                'name': userPlanty_obj.plant_name,
                'info': 'The plant needs less sunlight.',
                'text': "Too much direct sunlight can be harmful to some plants. Move your plant to a location with partial shade or use curtains to filter the light. This will prevent it from getting sunburned.",
                'imageSource': userPlanty_obj.image_url,
            })
            alert_id += 1  # Incrementamos el ID

        elif userPlanty_obj.planty.actual_light[-1] < userPlanty_obj.planty.plants_info.light - 30:
            alerts.append({
                'id': alert_id,
                'name': userPlanty_obj.plant_name,
                'info': 'The plant needs more light.',
                'text': "Your plants need more light to efficiently carry out photosynthesis. Place them in a spot with bright indirect light or consider using grow lights to supplement natural light.",
                'imageSource': userPlanty_obj.image_url,
            })
            alert_id += 1  # Incrementamos el ID

        if userPlanty_obj.planty.actual_watering[-1] > userPlanty_obj.planty.plants_info.watering + 30:
            alerts.append({
                'id': alert_id,
                'name': userPlanty_obj.plant_name,
                'info': 'The plant needs less watering.',
                'text': "It seems you are providing too much water to your plant. To avoid overwatering and root problems, reduce the amount of water you give and ensure the soil is dry before watering again.",
                'imageSource': userPlanty_obj.image_url,
            })
            alert_id += 1  # Incrementamos el ID

        elif userPlanty_obj.planty.actual_watering[-1] < userPlanty_obj.planty.plants_info.watering - 30:
            alerts.append({
                'id': alert_id,
                'name': userPlanty_obj.plant_name,
                'info': "The plant needs more watering.",
                'text':  "Your plant is dehydrated. Make sure to water it adequately to keep the soil slightly moist. Watch for wilting signs and adjust the watering frequency accordingly.",
                'imageSource': userPlanty_obj.image_url,
            })
            alert_id += 1  # Incrementamos el ID
        return alerts, alert_id

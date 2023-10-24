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

    def update_planty_user(self, users_id: UUID, planty_id: UUID, data: UserPlantyInput, file: UploadedFile, plant_info_id: UUID = None):
        userPlanty_obj = get_object_or_404(self.model, user_id=users_id, planty_id=planty_id)
        for attr, value in data.dict().items():
            setattr(userPlanty_obj, attr, value)
        if file:
            file_url = upload_to_firebase(file)
            data.image_url = file_url
            delete_from_firebase(file)
        if plant_info_id:
            plant_info_obj = get_object_or_404(get_plant_model(), id=plant_info_id)
            setattr(userPlanty_obj.planty, "plants_info", plant_info_obj)
        userPlanty_obj.save()
        return 200, userPlanty_obj

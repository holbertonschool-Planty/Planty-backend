from uuid import UUID
from django.db.models import Manager
from django.shortcuts import get_object_or_404
from ninja import UploadedFile
from config.settings import IMAGE_DEFAULT
from src.schemas.schemas import CustomBadRequest
from utils.firebase_helpers import upload_to_firebase
from utils.models_loads import get_users_model, get_planty_model, get_userPlanty_model

class UserPlantyManager(Manager):
    
    def create_planty_user(self, users_id: UUID, planty_id: UUID, data: dict, file: UploadedFile):
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
        return 201, userPlanty_obj

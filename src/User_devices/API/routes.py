from ninja import Form, Router
from src.schemas.user_devices_schemas import UserPlantyInput, UserPlantyOutput
from utils.firebase_helpers import upload_to_firebase
from utils.models_loads import get_userPlanty_model
from django.shortcuts import get_object_or_404, get_list_or_404
from typing import Dict, List
from src.schemas import schemas
from uuid import UUID
from ninja import File
from ninja.files import UploadedFile


router = Router(tags=["Planty of users"])


@router.get(
    "{users_id}/planty",
    response={
    200: List[UserPlantyOutput],
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def get_planties_by_user(request, users_id: UUID):
    return 200, get_list_or_404(get_userPlanty_model(), user_id=users_id)

@router.post(
        "{users_id}/planty/{planty_id}", response={
    201: UserPlantyOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
    }
)
def add_planty_by_user(request, users_id: UUID, planty_id: UUID, data: UserPlantyInput, file: UploadedFile = None ):
    return get_userPlanty_model().objects.create_planty_user(users_id, planty_id, dict(data), file)

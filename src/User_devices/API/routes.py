from ninja import Form, Router
from src.schemas.user_devices_schemas import CreationPlantyUserOutput, UserPlantyInput, UserPlantyOutput, CreationPlantyUserInput
from utils.firebase_helpers import upload_to_firebase
from utils.models_loads import get_userPlanty_model, get_planty_model, get_userPhone_model, get_phoneEvent_model
from django.shortcuts import get_object_or_404, get_list_or_404
from typing import Dict, List
from src.schemas import schemas
from uuid import UUID
from ninja import File
from ninja.files import UploadedFile


router = Router(tags=["Planty of users"])


@router.get(
    "",
    response={
    200: List[UserPlantyOutput],
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def get_planties_by_user(request, users_id: UUID):
    return 200, get_list_or_404(get_userPlanty_model(), user_id=users_id)


@router.get(
    "{planty_id}",
    response={
    200: UserPlantyOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def get_planty_of_user(request, users_id: UUID, planty_id: UUID):
    return 200, get_object_or_404(get_userPlanty_model(), user_id=users_id, planty_id=planty_id)


@router.post(
    "{planty_id}",
    response={
    201: CreationPlantyUserOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
    }
)
def add_planty_by_user(request, users_id: UUID, planty_id: UUID, data: CreationPlantyUserInput, file: UploadedFile = None):
    userPhone_obj = get_object_or_404(get_userPhone_model(), user_id=users_id, token=data.token_phone)
    response_notifications = []
    get_planty_model().objects.update_plant_of_planty(planty_id, data.plants_info_id)
    response_userplanty = get_userPlanty_model().objects.create_planty_user(users_id, planty_id, dict(data.user_planty), file)
    if data.phone_event:
        response_notifications = get_phoneEvent_model().objects.create_events(data.phone_event, userPhone_obj)
    return 201, CreationPlantyUserOutput(user_planty=response_userplanty, phone_events=response_notifications)


@router.put(
    "{planty_id}",
    response={
    201: CreationPlantyUserOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
    }
)
def update_planty_by_user(request, users_id: UUID, planty_id: UUID, data: CreationPlantyUserInput, file: UploadedFile = None):
    print("AAAAAAAAAAAAAAAAAAAAAAAAaa")
    return get_userPlanty_model().objects.update_planty_user(users_id, planty_id, data.user_planty, file, data.plants_info_id)

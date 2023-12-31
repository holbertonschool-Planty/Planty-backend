from ninja import Form, Router
from src.schemas.user_devices_schemas import UserPlantyOutput
from src.schemas.creation_planty_user_schemas import CreationPlantyUserInput, CreationPlantyUserOutput
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
    "{users_id}",
    response={
    200: List[UserPlantyOutput],
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def get_planties_by_user(request, users_id: UUID):
    return 200, get_list_or_404(get_userPlanty_model(), user_id=users_id)


@router.get(
    "{users_id}/planty/{planty_id}",
    response={
    200: UserPlantyOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def get_planty_of_user(request, users_id: UUID, planty_id: UUID):
    return 200, get_object_or_404(get_userPlanty_model(), user_id=users_id, planty_id=planty_id)

@router.get(
    "{users_id}/check_values/",
    response={
    200: List[Dict],
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def check_values_of_planty(request, users_id: UUID):
    list_planties_by_user = get_list_or_404(get_userPlanty_model(), user_id=users_id)
    filter_list = []
    alert_id = 1
    for user_planty in list_planties_by_user:
        alert_planty, alert_id = get_userPlanty_model().objects.check_values_of_planty(user_planty.id, alert_id)
        filter_list = filter_list + alert_planty
    return 200, filter_list

@router.post(
    "{users_id}/planty/",
    response={
    201: CreationPlantyUserOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
    }
)
def add_planty_by_user(request, users_id: UUID, data: CreationPlantyUserInput, file: UploadedFile = None):
    response_notifications = []
    if not data.planty_id:
        data.planty_id = get_planty_model().objects.create_empty_planty(data.plants_info_id, data.timezone)
    else:
        get_planty_model().objects.update_plant_of_planty(data.planty_id, data.plants_info_id, data.timezone)
    response_userplanty = get_userPlanty_model().objects.create_planty_user(users_id, data.planty_id, dict(data.user_planty), file)
    if data.phone_event:
        response_notifications = get_phoneEvent_model().objects.create_events(data.phone_event, response_userplanty)
    return 201, CreationPlantyUserOutput(user_planty=response_userplanty)

@router.put(
    "{user_planty_id}/",
    response={
    200: UserPlantyOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
    }
)
def update_planty_by_user(request, user_planty_id: UUID, data: CreationPlantyUserInput = None, file: UploadedFile = None):
    kwargs = {'user_planty_id': user_planty_id}
    if data and data.user_planty:
        kwargs['data'] = data.user_planty
    if data and data.plants_info_id:
        kwargs['plant_info_id'] = data.plants_info_id
    if file:
        kwargs['file'] = file
    return get_userPlanty_model().objects.update_planty_user(**kwargs)
    

@router.delete(
    "{user_planty_id}/",
    response={
    200: Dict,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
    }
)
def delete_planty_by_user(request, user_planty_id:UUID):
    return get_userPlanty_model().objects.delete_planty_user(user_planty_id)
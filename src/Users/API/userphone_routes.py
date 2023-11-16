from typing import Dict, List
from ninja import Router
from uuid import UUID
from utils.authentication import TokenAuth
from utils.models_loads import get_users_model, get_userPhone_model, get_phoneEvent_model
from django.shortcuts import get_list_or_404, get_object_or_404
from src.schemas import users_schemas, schemas

router = Router(tags=["Users Phone Token"])


@router.get(
    "",
    response={
        200: List[users_schemas.UserPhoneOutput],
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }
)
def get_list_phone_by_user(request, users_id: UUID):
    return 200, get_list_or_404(get_userPhone_model(), user_id=users_id)

@router.get(
    "{user_phone_token}",
    response={
        200: users_schemas.UserPhoneOutput,
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }
)
def get_phone_by_user(request, users_id: UUID, user_phone_token: str):
    userPhone_obj = get_object_or_404(get_userPhone_model(), user_id=users_id, token=user_phone_token)
    return 200, userPhone_obj


@router.post(
    "",
    response={
        201: users_schemas.UserPhoneOutput,
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }
)
def create_phone_token_by_user(request, users_id: UUID, data: users_schemas.UserPhoneInput):
    return get_userPhone_model().objects.save_token(users_id, data)


@router.delete(
    "{user_phone_token}",
    response={
        200: Dict,
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }
)
def delete_phone_token_by_user(request, users_id: UUID, user_phone_token: str):
    return get_userPhone_model().objects.delete_token(users_id, user_phone_token)

@router.post(
    "{user_phone_token}/notifications",
    response={
        201: users_schemas.PhoneEventOutput,
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }   
)
def create_event(request, users_id: UUID, user_phone_token: str, data: users_schemas.PhoneEventInput):
    userPhone_obj = get_object_or_404(get_userPhone_model(), user_id=users_id, token=user_phone_token)
    return 201, get_phoneEvent_model().objects.create_event(userPhone_obj, dict(data))

@router.get(
        "{user_phone_token}/notifications/",
        response={
            200: List[users_schemas.PhoneEventOutput],
            400: schemas.BadRequestResponse,
            404: schemas.NotFoundResponse,
            500: schemas.InternalServerErrorResponse
        }
)
def get_events_list_by_user(request, users_id: UUID, user_phone_token: str):
    userPhone_obj = get_object_or_404(get_userPhone_model(), user_id=users_id, token=user_phone_token)
    return 200, get_list_or_404(get_phoneEvent_model(), user_phone_id=userPhone_obj.id)
    
@router.delete(
    "{user_phone_token}/notifications",
    response={
        200: List[Dict],
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }   
)
def delete_event(request, users_id: UUID, user_phone_token: str):
    return get_phoneEvent_model().objects.delete_events(users_id, user_phone_token)


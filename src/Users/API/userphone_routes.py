from typing import Dict, List
from ninja import Router
from uuid import UUID
from utils.authentication import TokenAuth
from utils.models_loads import get_users_model, get_userPhone_model
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
    try: 
        return get_userPhone_model().objects.get_tokens_by_user(users_id)
    except Exception:
        return 404, {"detail": "The user does not have any phone token"}


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
    user_obj = get_object_or_404(get_users_model(), id=users_id)
    userPhone_obj = get_object_or_404(get_userPhone_model(), users_id=users_id, token=user_phone_token)
    return get_userPhone_model().objects.create_schema(user_obj, userPhone_obj)


@router.post(
    "{user_phone_token}",
    response={
        201: users_schemas.UserPhoneOutput,
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }
)

def create_phone_token_by_user(request, users_id: UUID, user_phone_token: str):
    return get_userPhone_model().objects.save_token(users_id, user_phone_token)


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
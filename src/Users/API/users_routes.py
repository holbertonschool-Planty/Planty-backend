from typing import Dict
from ninja import Router
from uuid import UUID
from utils.authentication import TokenAuth
from utils.models_loads import get_users_model
from django.shortcuts import get_object_or_404
from src.schemas import users_schemas, schemas

router = Router(tags=["Users"])


@router.get(
    "{users_id}",
    response={
        200: users_schemas.UserOutput,
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }
)
def get_object_users(request, users_id: UUID):
    return get_object_or_404(get_users_model(), id=users_id)


@router.post(
    "",
    response={
        201: users_schemas.UserOutput,
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }
)

def create_object_users(request, data: users_schemas.UserInput):
    return get_users_model().objects.register_user(dict(data))

@router.post(
    "login/",
    response={
        200: users_schemas.UserOutput,
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }
)
def login_object_users(request, data: users_schemas.UserLogin):
    return get_users_model().objects.login_user(data)


@router.put(
    "{users_id}",
        auth=TokenAuth(),
        response={
        200: users_schemas.UserOutput,
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }
)
def update_object_users(request, users_id: UUID, data:users_schemas.UserInput):
    return get_users_model().objects.update_user(users_id, data)

@router.delete(
    "{users_id}",
        response={
        200: Dict,
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
    }
)
def delete_object_users(request, users_id: UUID):
    return get_users_model().objects.delete_user(users_id)


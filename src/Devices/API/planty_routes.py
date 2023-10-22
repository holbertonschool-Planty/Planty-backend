from ninja import Router
from src.schemas.planty_schemas import PlantyInput, PlantyOutput
from src.schemas import schemas
from utils.models_loads import get_planty_model
from django.shortcuts import get_object_or_404
from typing import Dict
from uuid import UUID

router = Router(tags=["Planty"])

@router.post("", response={
    201: PlantyOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def add_planty(request, data: PlantyInput):
    return get_planty_model().objects.create_planty(dict(data))

@router.get("/{planty_id}", response={
    200: PlantyOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def get_planty(request, planty_id: UUID):
    return get_object_or_404(get_planty_model(), id=planty_id)


@router.delete("/{planty_id}", response={
    200: Dict,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def delete_planty(request, planty_id: UUID):
    return get_planty_model().objects.delete_planty(planty_id)

@router.put("/{planty_id}", response={
    200: PlantyOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def update_planty(request, planty_id: UUID, data: PlantyInput):
    return get_planty_model().objects.update_planty(planty_id, data)

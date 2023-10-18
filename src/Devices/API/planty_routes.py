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

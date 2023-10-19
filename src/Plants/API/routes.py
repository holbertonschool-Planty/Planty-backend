from ninja import Router
from src.schemas.plants_info_schemas import PlantsInfoOutput, PlantsInfoInput
from utils.models_loads import get_plant_model
from django.shortcuts import get_object_or_404
from typing import Any, Dict, List
from src.schemas import schemas
from uuid import UUID

router = Router(tags=["Plants info"])

@router.get("", response={
    200: List[PlantsInfoOutput],
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def plants_info(request):
    plants_info = get_plant_model().objects.get_list()
    return plants_info


@router.get("/{plants_info_id}", response={
    200: PlantsInfoOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def get_plant_info_id(request, plants_info_id: UUID):
    return get_object_or_404(get_plant_model(), id=plants_info_id)

@router.post("", response={
    201: PlantsInfoOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def add_plant_info(request, data: PlantsInfoInput):
    return get_plant_model().objects.create_plant(dict(data))

@router.put("/{plants_info_id}", response={
    200: PlantsInfoOutput,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def update_plant_info(request, plants_info_id: UUID, data: PlantsInfoInput):
    return get_plant_model().objects.update_plant(plants_info_id, data)

@router.delete("/{plants_info_id}", response={
    200: Dict,
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def delete_plant_info(request, plants_info_id: UUID):
    return get_plant_model().objects.delete_plant(plants_info_id)

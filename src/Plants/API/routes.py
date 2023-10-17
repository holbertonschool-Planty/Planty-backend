from ninja import Router
from src.Plants.schemas.plants_info_schemas import PlantsInfoOutput, PlantsInfoInput
from utils.model_loads import get_plant_model
from django.shortcuts import get_object_or_404
from typing import Any, Dict
from uuid import UUID

router = Router(tags=["Plants info"])

@router.get("", response={
    200: list[PlantsInfoOutput],
    400: Any,
    404: Any,
    500: Dict
})
def plants_info(request):
    plants_info = get_plant_model().objects.get_list()
    return plants_info


@router.get("/{plants_info_id}", response={
    200: PlantsInfoOutput,
    400: Any,
    404: Any,
    500: Dict
})
def get_plant_info_id(request, plants_info_id: UUID):
    return get_object_or_404(get_plant_model(), id=plants_info_id)

@router.post("", response={
    201: PlantsInfoOutput,
    400: Any,
    400: Any,
    500: Dict
})
def add_plant_info(request, data: PlantsInfoInput):
    return get_plant_model().objects.create_plant(dict(data))

@router.put("/{plants_info_id}", response={
    200: PlantsInfoOutput,
    400: Any,
    404: Any,
    500: Dict
})
def update_plant_info(request, plants_info_id: UUID, data: PlantsInfoInput):
    return get_plant_model().objects.update_plant(plants_info_id, data)

@router.delete("/{plants_info_id}", response={
    200: Dict,
    400: Any,
    404: Any,
    500: Dict
})
def delete_plant_info(request, plants_info_id: UUID):
    return get_plant_model().objects.delete_plant(plants_info_id)

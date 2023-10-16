from ninja import Router
from src.Plants.schemas.plants_info_schemas import PlantsInfoOutput, PlantsInfoInput
from src.Plants.models import Plants_info
from django.shortcuts import get_object_or_404
from typing import Any, Dict

router = Router()

@router.get("", response=list[PlantsInfoOutput])
def plants_info(request):
    plants_info = Plants_info.objects.get_list()
    return plants_info


@router.get("/{plants_info_id}", response={
    200: PlantsInfoOutput,
    404: Any,
    500: Dict
})
def get_plant_info_id(request, plants_info_id: int):
    return get_object_or_404(Plants_info, id=plants_info_id)

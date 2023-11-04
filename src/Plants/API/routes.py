from ninja import Router, UploadedFile
from src.schemas.plants_info_schemas import PlantsInfoOutput, PlantsInfoInput
from utils.firebase_helpers import upload_to_firebase
from utils.models_loads import get_plant_model
from django.shortcuts import get_object_or_404, get_list_or_404
from typing import Dict, List
from src.schemas import schemas
from uuid import UUID

router = Router(tags=["Plants information"])

@router.get("", response={
    200: List[PlantsInfoOutput],
    400: schemas.BadRequestResponse,
    404: schemas.NotFoundResponse,
    500: schemas.InternalServerErrorResponse
})
def plants_info(request):
    return get_list_or_404(get_plant_model())

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
    return 201, get_plant_model().objects.create_plant(data)


@router.post(
    "list/",
    response={
        201: List[PlantsInfoOutput],
        400: schemas.BadRequestResponse,
        404: schemas.NotFoundResponse,
        500: schemas.InternalServerErrorResponse
})
def add_list_plants_info(request, data: List[PlantsInfoInput]):
    return get_plant_model().objects.create_plants(data)



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

#IS ONLY TO TEST, REMOVE THIS IN FUTURE
@router.post(
    "temp_image/",
    response={
        200: Dict
    }
)
def upload_image(request, file: UploadedFile):
    file_url = upload_to_firebase(file)
    return 200, {"message": f"{file_url}"}

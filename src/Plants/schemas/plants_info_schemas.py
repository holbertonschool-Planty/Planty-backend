from ninja import Schema
from ninja.errors import HttpError
from pydantic import UUID4, validator
from src.Plants.models import Plants_info

class PlantsInfoOutput(Schema):
    id: UUID4
    scientific_name: str
    station: str
    temperature: int
    light: int
    watering: int


class PlantsInfoInput(Schema):
    scientific_name: str
    station: str
    temperature: int
    light: int
    watering: int

    @validator("scientific_name", pre=True, always=True)
    def scientific_name_unique(cls, scientific_name):
        if Plants_info.objects.filter(scientific_name=scientific_name).exists():
            raise HttpError(409, f'scientific_name {scientific_name} already exists in database')
        return scientific_name

from ninja import Schema
from ninja.errors import HttpError
from pydantic import UUID4, validator
from utils.models_loads import get_plant_model
from typing import Optional

class PlantsInfoOutput(Schema):
    id: UUID4
    scientific_name: str
    station: str
    temperature: int
    light: int
    watering: int
    water_frequency: int

class PlantsInfoInput(Schema):
    scientific_name: Optional[str]
    station: str
    temperature: int
    light: int
    watering: int
    water_frequency: int

    @validator("scientific_name", pre=True, always=True)
    def scientific_name_unique(cls, scientific_name):
        if get_plant_model().objects.filter(scientific_name=scientific_name).exists():
            raise HttpError(409, f'scientific_name {scientific_name} already exists in database')
        return scientific_name
    
    @validator("scientific_name", pre=True, always=True)
    def scientific_name_max_length(cls, scientific_name):
        if len(scientific_name) > 100:
            raise HttpError(400, "Scientific name must be shorter than 100 characters")
        return scientific_name
    
    @validator("station", pre=True, always=True)
    def station_max_length(cls, station):
        if len(station) > 40:
            raise HttpError(400, "Station must be shorter than 40 characters")
        return station

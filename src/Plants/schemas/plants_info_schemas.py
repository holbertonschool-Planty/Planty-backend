from ninja import Schema
from pydantic import UUID4

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

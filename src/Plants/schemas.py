from ninja import Schema
from pydantic import UUID4

class Plants_info_Out(Schema):
    id: UUID4
    scientific_name: str
    station: str
    temperature: int
    light: int
    watering: int

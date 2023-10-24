from django.shortcuts import get_object_or_404
from ninja import Schema
from ninja.errors import HttpError
from pydantic import UUID4, validator
from utils.models_loads import get_planty_model
from src.schemas.plants_info_schemas import PlantsInfoOutput
from typing import List, Optional

class PlantyOutput(Schema):
	id: UUID4
	serie: str
	actual_temperature: List[int]
	actual_light: List[int]
	actual_watering: List[int]
	plants_info: Optional[PlantsInfoOutput]
  
class PlantyInput(Schema):
	serie: Optional[str]
	actual_temperature: int
	actual_light: int
	actual_watering: int
	plants_info_id: Optional[UUID4] = None
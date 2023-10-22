from ninja import Schema
from ninja.errors import HttpError
from pydantic import UUID4, validator
from utils.models_loads import get_planty_model
from src.schemas.plants_info_schemas import PlantsInfoOutput
from typing import List

class PlantyOutput(Schema):
	id: UUID4
	serie: str
	actual_temperature: List[int]
	actual_light: List[int]
	actual_watering: List[int]
	plants_info: PlantsInfoOutput
  
class PlantyInput(Schema):
	serie: str = None
	actual_temperature: int
	actual_light: int
	actual_watering: int
	plants_info_id: UUID4 = None
  
	@validator("serie", pre=True, always=True)
	def serie_unique(cls, serie):
		if get_planty_model().objects.filter(serie=serie).exists():
			raise HttpError(409, f'User already linked to the specified device.')
		return serie

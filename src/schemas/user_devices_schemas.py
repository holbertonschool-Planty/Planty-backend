from ninja import Schema
from pydantic import UUID4
from typing import Optional
from src.schemas.users_schemas import UserOutput
from src.schemas.planty_schemas import PlantyOutput

class UserPlantyOutput(Schema):
    id: UUID4
    plant_name: str
    image_url: str
    location: str
    color_card: str
    user: UserOutput
    planty: PlantyOutput


class UserPlantyInput(Schema):
    plant_name: str
    image_url: Optional[str]
    location: Optional[str]
    color_card: Optional[str]
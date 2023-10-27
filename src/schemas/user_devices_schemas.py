from ninja import Schema
from pydantic import UUID4
from typing import List, Optional
from src.schemas.users_schemas import PhoneEventOutput, UserOutput, PhoneEventInput
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
    color_card: Optional[str]
    location: Optional[str]
    image_url: Optional[str]

class CreationPlantyUserInput(Schema):
    token_phone: Optional[str]
    user_planty: UserPlantyInput
    plants_info_id: Optional[UUID4]
    timezone: int
    phone_event: Optional[List[PhoneEventInput]]

class CreationPlantyUserOutput(Schema):
    user_planty: UserPlantyOutput
    phone_events: Optional[List[PhoneEventOutput]]

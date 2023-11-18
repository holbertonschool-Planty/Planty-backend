from ninja import Schema
from pydantic import UUID4
from typing import List, Optional
from src.schemas.user_devices_schemas import UserPlantyInput, UserPlantyOutput
from src.schemas.phone_event_schemas import PhoneEventInput, PhoneEventOutput


class CreationPlantyUserInput(Schema):
    user_planty: UserPlantyInput
    plants_info_id: Optional[UUID4]
    planty_id : Optional[UUID4] = None
    timezone: int
    phone_event: Optional[List[PhoneEventInput]]

class CreationPlantyUserOutput(Schema):
    user_planty: UserPlantyOutput

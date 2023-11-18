from ninja import Schema
from pydantic import UUID4
from datetime import date
from src.schemas.user_devices_schemas import UserPlantyOutput
from src.schemas.users_schemas import UserPhoneOutput


class PhoneEventOutput(Schema):
    id: UUID4
    user_device: UserPlantyOutput
    last_event_date: date
    frequency: int
    event_type: str
    message: str

class PhoneEventInput(Schema):
    frequency: int
    event_type: str
    message: str
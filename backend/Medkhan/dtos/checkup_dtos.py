from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from Medkhan import enums
from Medkhan.dtos import BaseOrmModel


class CheckupDTO(BaseOrmModel):
    """Checkup DTO."""

    id: int
    name: str
    description: str
    original_price: int
    discounted_price: int | None
    gender: enums.GenderEnum | None
    checkup_type: enums.CheckupType
    expired_at: str | None
    discount_percentage: int


class CheckupInputDTO(BaseModel):
    """Checkup input DTO."""


class CheckupUpdateDTO(BaseModel):
    """Checkup update DTO."""

from uuid import UUID

from pydantic import BaseModel

from Medkhan.dtos import BaseOrmModel


class CheckupDTO(BaseOrmModel):
    """Checkup DTO."""

    id: UUID


class CheckupInputDTO(BaseModel):
    """Checkup input DTO."""


class CheckupUpdateDTO(BaseModel):
    """Checkup update DTO."""

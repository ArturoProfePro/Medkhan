from uuid import UUID

from pydantic import BaseModel

from Medkhan.dtos import BaseOrmModel


class ServiceDTO(BaseOrmModel):
    """Service DTO."""

    id: UUID
    name: str


class ServiceInputDTO(BaseModel):
    """Service input DTO."""

    name: str


class ServiceUpdateDTO(BaseModel):
    """Service update DTO."""

    name: str | None = None

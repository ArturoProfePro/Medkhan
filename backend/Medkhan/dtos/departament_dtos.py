from uuid import UUID

from pydantic import BaseModel

from Medkhan.dtos import BaseOrmModel


class DepartamentDTO(BaseOrmModel):
    """Departament DTO."""

    id: UUID


class DepartamentInputDTO(BaseModel):
    """Departament input DTO."""


class DepartamentUpdateDTO(BaseModel):
    """Departament update DTO."""

from uuid import UUID

from pydantic import BaseModel

from Medkhan.dtos import BaseOrmModel


class DoctorDTO(BaseOrmModel):
    """Doctor DTO."""

    id: UUID
    full_name: str
    experience_years: int
    consultation_cost: int | None
    category: str
    profile_treatment: str
    work_experience: str
    education: str
    image_url: str | None
    online_booking_link: str | None


class DoctorInputDTO(BaseModel):
    """Doctor input DTO."""

    full_name: str
    experience_years: int
    consultation_cost: int | None
    category: str
    profile_treatment: str
    work_experience: str
    education: str
    image_url: str | None
    online_booking_link: str | None


class DoctorUpdateDTO(BaseModel):
    """Doctor update DTO."""

    full_name: str | None = None
    experience_years: int | None = None
    consultation_cost: int | None = None
    category: str | None = None
    profile_treatment: str | None = None
    work_experience: str | None = None
    education: str | None = None
    image_url: str | None = None
    online_booking_link: str | None = None

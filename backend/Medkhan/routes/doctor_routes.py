from uuid import UUID

from fastapi import APIRouter

from Medkhan.daos import GetDAOs
from Medkhan.dtos import (
    DataResponse,
    EmptyResponse,
    OffsetResults,
    Pagination,
)
from Medkhan.dtos.doctor_dtos import (
    DoctorDTO,
    DoctorInputDTO,
    DoctorUpdateDTO,
)

router = APIRouter(prefix="/doctors")


@router.post("/", status_code=201)
async def create_doctor(
    input_dto: DoctorInputDTO,
    daos: GetDAOs,
) -> DataResponse[DoctorDTO]:
    """Create a new Doctor."""
    created_obj = await daos.doctor.create(input_dto)
    return DataResponse(data=DoctorDTO.model_validate(created_obj))


@router.patch("/{doctor_id}")
async def update_doctor(
    doctor_id: UUID,
    update_dto: DoctorUpdateDTO,
    daos: GetDAOs,
) -> EmptyResponse:
    """Update Doctor."""
    await daos.doctor.update(doctor_id, update_dto)
    return EmptyResponse()


@router.delete("/{doctor_id}")
async def delete_doctor(
    doctor_id: UUID,
    daos: GetDAOs,
) -> EmptyResponse:
    """Delete a Doctor by id."""
    await daos.doctor.delete(id=doctor_id)
    return EmptyResponse()


@router.get("/")
async def get_doctor_paginated(
    daos: GetDAOs,
    pagination: Pagination,
) -> OffsetResults[DoctorDTO]:
    """Get all Doctors paginated."""
    return await daos.doctor.get_offset_results(
        out_dto=DoctorDTO,
        pagination=pagination,
    )


@router.get("/{doctor_id}")
async def get_doctor(
    doctor_id: UUID,
    daos: GetDAOs,
) -> DataResponse[DoctorDTO]:
    """Get a Doctor by id."""
    doctor = await daos.doctor.filter_first(id=doctor_id)
    return DataResponse(data=DoctorDTO.model_validate(doctor))

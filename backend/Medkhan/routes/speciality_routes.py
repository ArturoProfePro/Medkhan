from uuid import UUID

from fastapi import APIRouter

from Medkhan.daos import GetDAOs
from Medkhan.dtos import (
    DataResponse,
    EmptyResponse,
    OffsetResults,
    Pagination,
)
from Medkhan.dtos.speciality_dtos import (
    SpecialityDTO,
    SpecialityInputDTO,
    SpecialityUpdateDTO,
)

router = APIRouter(prefix="/specialities")


@router.post("/", status_code=201)
async def create_speciality(
    input_dto: SpecialityInputDTO,
    daos: GetDAOs,
) -> DataResponse[SpecialityDTO]:
    """Create a new Speciality."""
    created_obj = await daos.speciality.create(input_dto)
    return DataResponse(data=SpecialityDTO.model_validate(created_obj))


@router.patch("/{speciality_id}")
async def update_speciality(
    speciality_id: UUID,
    update_dto: SpecialityUpdateDTO,
    daos: GetDAOs,
) -> EmptyResponse:
    """Update Speciality."""
    await daos.speciality.update(speciality_id, update_dto)
    return EmptyResponse()


@router.delete("/{speciality_id}")
async def delete_speciality(
    speciality_id: UUID,
    daos: GetDAOs,
) -> EmptyResponse:
    """Delete a Speciality by id."""
    await daos.speciality.delete(id=speciality_id)
    return EmptyResponse()


@router.get("/")
async def get_speciality_paginated(
    daos: GetDAOs,
    pagination: Pagination,
) -> OffsetResults[SpecialityDTO]:
    """Get all Specialities paginated."""
    return await daos.speciality.get_offset_results(
        out_dto=SpecialityDTO,
        pagination=pagination,
    )


@router.get("/{speciality_id}")
async def get_speciality(
    speciality_id: UUID,
    daos: GetDAOs,
) -> DataResponse[SpecialityDTO]:
    """Get a Speciality by id."""
    speciality = await daos.speciality.filter_first(id=speciality_id)
    return DataResponse(data=SpecialityDTO.model_validate(speciality))

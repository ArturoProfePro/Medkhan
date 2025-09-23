from uuid import UUID

from fastapi import APIRouter

from Medkhan.daos import GetDAOs
from Medkhan.dtos import (
    DataResponse,
    EmptyResponse,
    OffsetResults,
    Pagination,
)
from Medkhan.dtos.checkup_dtos import (
    CheckupDTO,
    CheckupInputDTO,
    CheckupUpdateDTO,
)

router = APIRouter(prefix="/checkups")


@router.post("/", status_code=201)
async def create_checkup(
    input_dto: CheckupInputDTO,
    daos: GetDAOs,
) -> DataResponse[CheckupDTO]:
    """Create a new Checkup."""
    created_obj = await daos.checkup.create(input_dto)
    return DataResponse(data=CheckupDTO.model_validate(created_obj))


@router.patch("/{checkup_id}")
async def update_checkup(
    checkup_id: UUID,
    update_dto: CheckupUpdateDTO,
    daos: GetDAOs,
) -> EmptyResponse:
    """Update Checkup."""
    await daos.checkup.update(checkup_id, update_dto)
    return EmptyResponse()


@router.delete("/{checkup_id}")
async def delete_checkup(
    checkup_id: UUID,
    daos: GetDAOs,
) -> EmptyResponse:
    """Delete a Checkup by id."""
    await daos.checkup.delete(id=checkup_id)
    return EmptyResponse()


@router.get("/")
async def get_checkup_paginated(
    daos: GetDAOs,
    pagination: Pagination,
) -> OffsetResults[CheckupDTO]:
    """Get all Checkups paginated."""
    return await daos.checkup.get_offset_results(
        out_dto=CheckupDTO,
        pagination=pagination,
    )


@router.get("/{checkup_id}")
async def get_checkup(
    checkup_id: UUID,
    daos: GetDAOs,
) -> DataResponse[CheckupDTO]:
    """Get a Checkup by id."""
    checkup = await daos.checkup.filter_first(id=checkup_id)
    return DataResponse(data=CheckupDTO.model_validate(checkup))

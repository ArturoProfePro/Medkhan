from uuid import UUID

from fastapi import APIRouter

from Medkhan.daos import GetDAOs
from Medkhan.dtos import (
    DataResponse,
    EmptyResponse,
    OffsetResults,
    Pagination,
)
from Medkhan.dtos.departament_dtos import (
    DepartamentDTO,
    DepartamentInputDTO,
    DepartamentUpdateDTO,
)

router = APIRouter(prefix="/departaments")


@router.post("/", status_code=201)
async def create_departament(
    input_dto: DepartamentInputDTO,
    daos: GetDAOs,
) -> DataResponse[DepartamentDTO]:
    """Create a new Departament."""
    created_obj = await daos.departament.create(input_dto)
    return DataResponse(data=DepartamentDTO.model_validate(created_obj))


@router.patch("/{departament_id}")
async def update_departament(
    departament_id: UUID,
    update_dto: DepartamentUpdateDTO,
    daos: GetDAOs,
) -> EmptyResponse:
    """Update Departament."""
    await daos.departament.update(departament_id, update_dto)
    return EmptyResponse()


@router.delete("/{departament_id}")
async def delete_departament(
    departament_id: UUID,
    daos: GetDAOs,
) -> EmptyResponse:
    """Delete a Departament by id."""
    await daos.departament.delete(id=departament_id)
    return EmptyResponse()


@router.get("/")
async def get_departament_paginated(
    daos: GetDAOs,
    pagination: Pagination,
) -> OffsetResults[DepartamentDTO]:
    """Get all Departaments paginated."""
    return await daos.departament.get_offset_results(
        out_dto=DepartamentDTO,
        pagination=pagination,
    )


@router.get("/{departament_id}")
async def get_departament(
    departament_id: UUID,
    daos: GetDAOs,
) -> DataResponse[DepartamentDTO]:
    """Get a Departament by id."""
    departament = await daos.departament.filter_first(id=departament_id)
    return DataResponse(data=DepartamentDTO.model_validate(departament))

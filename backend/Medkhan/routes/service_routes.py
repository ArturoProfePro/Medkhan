from uuid import UUID

from fastapi import APIRouter

from Medkhan.daos import GetDAOs
from Medkhan.dtos import (
    DataResponse,
    EmptyResponse,
    OffsetResults,
    Pagination,
)
from Medkhan.dtos.service_dtos import (
    ServiceDTO,
    ServiceInputDTO,
    ServiceUpdateDTO,
)

router = APIRouter(prefix="/services")


@router.post("/", status_code=201)
async def create_service(
    input_dto: ServiceInputDTO,
    daos: GetDAOs,
) -> DataResponse[ServiceDTO]:
    """Create a new Service."""
    created_obj = await daos.service.create(input_dto)
    return DataResponse(data=ServiceDTO.model_validate(created_obj))


@router.patch("/{service_id}")
async def update_service(
    service_id: UUID,
    update_dto: ServiceUpdateDTO,
    daos: GetDAOs,
) -> EmptyResponse:
    """Update Service."""
    await daos.service.update(service_id, update_dto)
    return EmptyResponse()


@router.delete("/{service_id}")
async def delete_service(
    service_id: UUID,
    daos: GetDAOs,
) -> EmptyResponse:
    """Delete a Service by id."""
    await daos.service.delete(id=service_id)
    return EmptyResponse()


@router.get("/")
async def get_service_paginated(
    daos: GetDAOs,
    pagination: Pagination,
) -> OffsetResults[ServiceDTO]:
    """Get all Services paginated."""
    return await daos.service.get_offset_results(
        out_dto=ServiceDTO,
        pagination=pagination,
    )


@router.get("/{service_id}")
async def get_service(
    service_id: UUID,
    daos: GetDAOs,
) -> DataResponse[ServiceDTO]:
    """Get a Service by id."""
    service = await daos.service.filter_first(id=service_id)
    return DataResponse(data=ServiceDTO.model_validate(service))

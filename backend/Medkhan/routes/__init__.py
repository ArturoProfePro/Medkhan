from fastapi import APIRouter

from Medkhan.routes.checkup_routes import router as checkup_router
from Medkhan.routes.contact_request_routes import (
    router as contact_request_router,
)
from Medkhan.routes.demo_routes import router as demo_router
from Medkhan.routes.departament_routes import router as departament_router
from Medkhan.routes.doctor_routes import router as doctor_router
from Medkhan.routes.health_routes import router as health_router
from Medkhan.routes.service_routes import router as service_router
from Medkhan.routes.speciality_routes import router as speciality_router
from Medkhan.routes.upload_routes import router as upload_router

base_router = APIRouter(prefix="/api/v1")

base_router.include_router(health_router, tags=["health"])
base_router.include_router(demo_router, tags=["demo"])
base_router.include_router(doctor_router, tags=["doctor"])
base_router.include_router(service_router, tags=["service"])
base_router.include_router(checkup_router, tags=["checkup"])
base_router.include_router(contact_request_router, tags=["contact_request"])
base_router.include_router(departament_router, tags=["departament"])
base_router.include_router(speciality_router, tags=["speciality"])
base_router.include_router(upload_router, tags=["upload"])

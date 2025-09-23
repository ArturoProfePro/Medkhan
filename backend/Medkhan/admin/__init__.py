from sqladmin import Admin
from fastapi import FastAPI

from .doctor import DoctorAdmin


async def setup_admin(app: FastAPI):
    """
    Инициализирует и настраивает SQLAdmin.
    """
    admin = Admin(app, app.state.db_engine)
    admin.add_view(DoctorAdmin)

from sqladmin import ModelView

from Medkhan.models.doctor_models import Doctor

from sqladmin import ModelView


class DoctorAdmin(ModelView, model=Doctor):
    column_list = [
        Doctor.full_name,
        Doctor.experience_years,
        Doctor.category,
        Doctor.profile_treatment,
    ]
    name = "Доктор"
    name_plural = "Доктора"
    icon = "fa-solid fa-user-doctor"

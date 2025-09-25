from enum import StrEnum


class GenderEnum(StrEnum):
    male = "Мужской"
    female = "Женский"
    child = "Ребёнок"
    general = "Общий"


class CheckupType(StrEnum):
    first = "FIRST"
    secondary = "SECONDARY"
    third = "THIRD"

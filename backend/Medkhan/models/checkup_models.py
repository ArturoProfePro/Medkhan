import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from Medkhan.db import Base
from Medkhan.enums import CheckupType, GenderEnum


class Checkup(Base):
    """Checkup model."""

    __tablename__ = "checkup"

    id: Mapped[int] = mapped_column(
        sa.Integer, primary_key=True, autoincrement=True, index=True
    )

    name: Mapped[str] = mapped_column(sa.String(256))
    description: Mapped[str] = mapped_column(sa.Text())
    original_price: Mapped[int] = mapped_column(sa.DECIMAL(10, 2))
    discounted_price: Mapped[int] = mapped_column(sa.DECIMAL(10, 2))
    gender: Mapped[GenderEnum | None] = mapped_column(
        sa.Enum(GenderEnum, name="gender_enum", create_type=True),
        nullable=True,
    )
    checkup_type: Mapped[CheckupType] = mapped_column(sa.Enum(CheckupType))

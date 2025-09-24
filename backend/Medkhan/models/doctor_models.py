from uuid import UUID, uuid4

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from Medkhan.db import Base


class Doctor(Base):
    """Doctor model."""

    __tablename__ = "doctor"

    id: Mapped[UUID] = mapped_column(
        sa.UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        index=True,
        default=uuid4,
    )

    created_at = sa.Column(
        sa.DateTime(timezone=True), server_default=func.now()
    )
    updated_at = sa.Column(sa.DateTime(timezone=True), onupdate=func.now())

    full_name: Mapped[str] = mapped_column(sa.String)
    experience_years: Mapped[int] = mapped_column(sa.Integer)
    consultation_cost: Mapped[int | None] = mapped_column(sa.Integer)
    category: Mapped[str] = mapped_column(sa.String)
    profile_treatment: Mapped[str] = mapped_column(sa.String)
    work_experience: Mapped[str] = mapped_column(sa.String)
    education: Mapped[str] = mapped_column(sa.String)

    image_url: Mapped[str | None] = mapped_column(sa.String)

    online_booking_link: Mapped[str | None] = mapped_column(sa.String)

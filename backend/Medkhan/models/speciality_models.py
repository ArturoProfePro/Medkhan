from uuid import UUID, uuid4

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from Medkhan.db import Base


class Speciality(Base):
    """Speciality model."""

    __tablename__ = "speciality"

    id: Mapped[UUID] = mapped_column(
        sa.UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        index=True,
        default=uuid4,
    )

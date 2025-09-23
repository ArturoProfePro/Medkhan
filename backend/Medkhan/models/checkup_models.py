from uuid import UUID, uuid4

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from Medkhan.db import Base


class Checkup(Base):
    """Checkup model."""

    __tablename__ = "checkup"

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

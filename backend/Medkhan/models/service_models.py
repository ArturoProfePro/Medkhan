from uuid import UUID, uuid4

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from Medkhan.db import Base


class Service(Base):
    """Service model."""

    __tablename__ = "service"

    id: Mapped[UUID] = mapped_column(
        sa.UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        index=True,
        default=uuid4,
    )
    name: Mapped[str] = mapped_column(sa.String)

from uuid import UUID, uuid4

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from Medkhan.db import Base


class ContactRequest(Base):
    """ContactRequest model."""

    __tablename__ = "contact_request"

    id: Mapped[UUID] = mapped_column(
        sa.UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        index=True,
        default=uuid4,
    )

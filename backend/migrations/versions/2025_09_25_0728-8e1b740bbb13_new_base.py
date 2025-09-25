"""new_base

Revision ID: 8e1b740bbb13
Revises:
Create Date: 2025-09-25 07:28:44.364698

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8e1b740bbb13"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        sa.text(
            "UPDATE checkup SET checkup_type = 'third' WHERE checkup_type IS NULL"
        )
    )
    pass


def downgrade() -> None:
    pass

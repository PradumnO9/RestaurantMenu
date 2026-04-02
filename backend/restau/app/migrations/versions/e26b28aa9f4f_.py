"""empty message

Revision ID: e26b28aa9f4f
Revises: ed5c8e6f8e27
Create Date: 2026-03-24 22:30:57.720765

"""
from typing import Sequence, Union

from alembic import op
import sqlmodel
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e26b28aa9f4f'
down_revision: Union[str, None] = 'ed5c8e6f8e27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

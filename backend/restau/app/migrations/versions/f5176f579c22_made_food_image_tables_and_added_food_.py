"""made food image tables and added food columns

Revision ID: f5176f579c22
Revises: 67d0fe6fc168
Create Date: 2026-04-04 18:10:02.784507

"""
from typing import Sequence, Union

from alembic import op
import sqlmodel
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5176f579c22'
down_revision: Union[str, None] = '67d0fe6fc168'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

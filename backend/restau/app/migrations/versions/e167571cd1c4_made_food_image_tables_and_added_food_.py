"""made food image tables and added food columns

Revision ID: e167571cd1c4
Revises: f5176f579c22
Create Date: 2026-04-04 18:10:24.131739

"""
from typing import Sequence, Union

from alembic import op
import sqlmodel
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e167571cd1c4'
down_revision: Union[str, None] = 'f5176f579c22'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

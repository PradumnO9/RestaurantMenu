"""made food image tables and added food 

Revision ID: 442650ea897a
Revises: e167571cd1c4
Create Date: 2026-04-05 13:59:10.878578

"""
from typing import Sequence, Union

from alembic import op
import sqlmodel
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '442650ea897a'
down_revision: Union[str, None] = 'e167571cd1c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

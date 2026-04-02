"""FoodPricing Added, Price Table Deprecated For Test

Revision ID: 7d375280ef12
Revises: 36b3682388cb
Create Date: 2026-03-28 18:10:47.040112

"""
from typing import Sequence, Union

from alembic import op
import sqlmodel
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d375280ef12'
down_revision: Union[str, None] = '36b3682388cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

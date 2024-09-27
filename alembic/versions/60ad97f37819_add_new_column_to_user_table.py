"""Add new column to User table

Revision ID: 60ad97f37819
Revises: 63ae78487111
Create Date: 2024-09-23 23:54:27.797121

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60ad97f37819'
down_revision: Union[str, None] = '63ae78487111'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

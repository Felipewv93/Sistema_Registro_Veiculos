"""remove tabela user

Revision ID: 9ddb8f0a4a88
Revises: 85b5e65b1c6e
Create Date: 2025-05-13 22:52:08.955883

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ddb8f0a4a88'
down_revision: Union[str, None] = '85b5e65b1c6e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('user')


def downgrade() -> None:
    pass

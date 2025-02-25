"""create example table

Revision ID: eeba4221d366
Revises: 
Create Date: 2025-01-19 20:42:02.423553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eeba4221d366'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'entity_example',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('example_field', sa.String(45), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('entity_example')

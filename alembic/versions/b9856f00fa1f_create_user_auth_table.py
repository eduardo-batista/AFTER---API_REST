"""create_user_auth_table

Revision ID: b9856f00fa1f
Revises: ea59441264f3
Create Date: 2025-03-07 01:50:56.061283

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9856f00fa1f'
down_revision: Union[str, None] = 'ea59441264f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'user_auth',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('auth_type', sa.Enum('password', 'google', 'apple', name='auth_type_enum'), nullable=False),
        sa.Column('password', sa.String(20), nullable=True),
        sa.Column('auth_token', sa.String(20), nullable=True),
        sa.Column('refresh_token', sa.String(20), nullable=True),
        sa.Column('last_access', sa.TIMESTAMP, nullable=True),
        sa.Column('created_at', sa.TIMESTAMP, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.text('CURRENT_TIMESTAMP'), onupdate=sa.text('CURRENT_TIMESTAMP'))
    )

def downgrade():
    op.drop_table('user_auth')
    op.execute('DROP TYPE auth_type_enum')

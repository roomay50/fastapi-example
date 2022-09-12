"""add phone number

Revision ID: edebf2cce20b
Revises: 2a69779e5573
Create Date: 2022-09-10 01:55:34.541186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edebf2cce20b'
down_revision = '2a69779e5573'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'phone_number')

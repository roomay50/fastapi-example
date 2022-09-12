"""add content column to posts table

Revision ID: f9e4491d8242
Revises: dbc87f60821c
Create Date: 2022-09-10 00:12:26.988652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9e4491d8242'
down_revision = 'dbc87f60821c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

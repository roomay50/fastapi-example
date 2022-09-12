"""add foreign key to posts table

Revision ID: 8b2f0698b950
Revises: fb8139fde177
Create Date: 2022-09-10 00:46:49.405439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b2f0698b950'
down_revision = 'fb8139fde177'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_user_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass

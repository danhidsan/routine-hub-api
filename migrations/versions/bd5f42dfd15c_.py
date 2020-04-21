"""empty message

Revision ID: bd5f42dfd15c
Revises: c55fd1c97a2c
Create Date: 2020-04-21 17:41:19.910886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd5f42dfd15c'
down_revision = 'c55fd1c97a2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exercise', sa.Column('rest_seconds', sa.Integer(), nullable=True))
    op.drop_column('exercise', 'break_seconds')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exercise', sa.Column('break_seconds', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('exercise', 'rest_seconds')
    # ### end Alembic commands ###
"""empty message

Revision ID: 62902d724aab
Revises: 
Create Date: 2020-09-10 17:00:00.218511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62902d724aab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('requests', sa.Column('eth_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('requests', 'eth_id')
    # ### end Alembic commands ###
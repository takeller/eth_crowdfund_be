"""empty message

Revision ID: 751ebb0b80f5
Revises: 661d1ce96a5b
Create Date: 2020-09-09 19:51:56.329039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '751ebb0b80f5'
down_revision = '661d1ce96a5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('campaigns', sa.Column('value', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('campaigns', 'value')
    # ### end Alembic commands ###

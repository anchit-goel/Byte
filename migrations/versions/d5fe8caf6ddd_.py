"""empty message

Revision ID: d5fe8caf6ddd
Revises: 4a5043d7df01
Create Date: 2020-08-25 22:09:45.035473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5fe8caf6ddd'
down_revision = '4a5043d7df01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('date', sa.Column('price', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('date', 'price')
    # ### end Alembic commands ###

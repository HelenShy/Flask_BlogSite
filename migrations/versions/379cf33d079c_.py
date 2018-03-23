"""empty message

Revision ID: 379cf33d079c
Revises: 083872aa6d8c
Create Date: 2018-03-22 18:09:30.380870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '379cf33d079c'
down_revision = '083872aa6d8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('picture_url', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'picture_url')
    # ### end Alembic commands ###

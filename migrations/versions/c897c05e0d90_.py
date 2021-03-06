"""empty message

Revision ID: c897c05e0d90
Revises: 379cf33d079c
Create Date: 2018-03-26 04:33:41.197193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c897c05e0d90'
down_revision = '379cf33d079c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('_title', sa.String(length=128), nullable=True))
    op.add_column('blog_post', sa.Column('url', sa.String(length=128), nullable=True))
    op.drop_column('blog_post', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('title', sa.VARCHAR(length=128), nullable=True))
    op.drop_column('blog_post', 'url')
    op.drop_column('blog_post', '_title')
    # ### end Alembic commands ###

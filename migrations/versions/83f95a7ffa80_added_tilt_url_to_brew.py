"""added tilt url to brew

Revision ID: 83f95a7ffa80
Revises: 
Create Date: 2021-04-05 13:31:21.161041

"""
from alembic import op
import sqlalchemy as sa
from migrations.migration_utils import _table_has_column


# revision identifiers, used by Alembic.
revision = '83f95a7ffa80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    if not _table_has_column('brew', 'tilt_url'):
        # ### commands auto generated by Alembic - please adjust! ###
        op.add_column('brew', sa.Column('tilt_url', sa.String(length=255), nullable=True))
        # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('brew', 'tilt_url')
    # ### end Alembic commands ###

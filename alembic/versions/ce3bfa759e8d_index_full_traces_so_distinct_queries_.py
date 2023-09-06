"""Index full traces so distinct queries are more reasonable

Revision ID: ce3bfa759e8d
Revises: d59c21eaa9e6
Create Date: 2017-09-16 10:15:57.621865

"""

# revision identifiers, used by Alembic.
revision = 'ce3bfa759e8d'
down_revision = 'd59c21eaa9e6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_mastertrace_full'), 'mastertrace', ['full'], unique=False)
    op.create_index(op.f('ix_sitetrace_full'), 'sitetrace', ['full'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sitetrace_full'), table_name='sitetrace')
    op.drop_index(op.f('ix_mastertrace_full'), table_name='mastertrace')
    ### end Alembic commands ###
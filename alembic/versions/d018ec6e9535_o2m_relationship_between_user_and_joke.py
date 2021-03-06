"""o2m relationship between user and joke

Revision ID: d018ec6e9535
Revises: ef109473dfb9
Create Date: 2018-07-29 17:48:47.928030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd018ec6e9535'
down_revision = 'ef109473dfb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jokes', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'jokes', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'jokes', type_='foreignkey')
    op.drop_column('jokes', 'user_id')
    # ### end Alembic commands ###

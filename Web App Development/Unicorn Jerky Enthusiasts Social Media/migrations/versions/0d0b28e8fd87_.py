"""empty message

Revision ID: 0d0b28e8fd87
Revises: 4a87a3635f48
Create Date: 2019-04-23 10:39:31.337996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d0b28e8fd87'
down_revision = '4a87a3635f48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('img_post')
    op.add_column('user', sa.Column('profilepic', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'profilepic')
    op.create_table('img_post',
    sa.Column('ipid', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('imgpath', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ipid', name='img_post_pkey')
    )
    # ### end Alembic commands ###
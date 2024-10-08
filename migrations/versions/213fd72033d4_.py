"""empty message

Revision ID: 213fd72033d4
Revises: 
Create Date: 2024-08-14 02:13:02.971278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '213fd72033d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lastname', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=180), nullable=False),
    sa.Column('salt', sa.String(length=180), nullable=False),
    sa.Column('avatar', sa.String(length=100), nullable=False),
    sa.Column('public_id_avatar', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###

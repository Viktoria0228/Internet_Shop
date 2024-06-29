"""empty message

Revision ID: 4d8310908dd4
Revises: 
Create Date: 2024-06-28 16:04:34.072041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d8310908dd4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('surname', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=70), nullable=False),
    sa.Column('phone_number', sa.String(length=30), nullable=False),
    sa.Column('city_recepient', sa.String(length=30), nullable=False),
    sa.Column('post_office', sa.String(length=50), nullable=False),
    sa.Column('add_wishes', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=False),
    sa.Column('discount', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=70), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('password_confirmation', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('product')
    op.drop_table('order')
    # ### end Alembic commands ###

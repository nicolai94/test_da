"""init_migr

Revision ID: 54b3dfbe989d
Revises: 
Create Date: 2024-01-04 12:01:51.865524

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54b3dfbe989d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('login', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column("created_at", sa.DateTime(), server_default=str(datetime.now()), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=str(datetime.now()), onupdate=str(datetime.now())),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=True)
    op.create_table('item',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column("created_at", sa.DateTime(), server_default=str(datetime.now()), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=str(datetime.now()), onupdate=str(datetime.now())),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_item_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_item'))
    )
    op.create_index(op.f('ix_item_id'), 'item', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_item_id'), table_name='item')
    op.drop_table('item')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###

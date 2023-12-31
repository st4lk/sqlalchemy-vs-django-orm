"""pk

Revision ID: 996b9c783bd6
Revises: 
Create Date: 2023-11-19 00:24:45.215741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '996b9c783bd6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pk_identity',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pk_index',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pk_index_id'), 'pk_index', ['id'], unique=False)
    op.create_table('pk_index_unique',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pk_index_unique_id'), 'pk_index_unique', ['id'], unique=True)
    op.create_table('pk_only',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pk_unique',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pk_unique')
    op.drop_table('pk_only')
    op.drop_index(op.f('ix_pk_index_unique_id'), table_name='pk_index_unique')
    op.drop_table('pk_index_unique')
    op.drop_index(op.f('ix_pk_index_id'), table_name='pk_index')
    op.drop_table('pk_index')
    op.drop_table('pk_identity')
    # ### end Alembic commands ###

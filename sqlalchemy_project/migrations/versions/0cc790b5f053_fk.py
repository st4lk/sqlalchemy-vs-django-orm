"""fk

Revision ID: 0cc790b5f053
Revises: 172c1592b7a8
Create Date: 2023-11-19 16:47:10.291266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cc790b5f053'
down_revision = '172c1592b7a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fk_right',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fk_left',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('right_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['right_id'], ['fk_right.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fk_left_deferred',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('right_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['right_id'], ['fk_right.id'], initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fk_left_deferred_right_id'), 'fk_left_deferred', ['right_id'], unique=False)
    op.create_table('fk_left_index',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('right_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['right_id'], ['fk_right.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fk_left_index_right_id'), 'fk_left_index', ['right_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fk_left_index_right_id'), table_name='fk_left_index')
    op.drop_table('fk_left_index')
    op.drop_index(op.f('ix_fk_left_deferred_right_id'), table_name='fk_left_deferred')
    op.drop_table('fk_left_deferred')
    op.drop_table('fk_left')
    op.drop_table('fk_right')
    # ### end Alembic commands ###

"""relations

Revision ID: 11084a127cda
Revises: ad0c130fee09
Create Date: 2023-11-22 23:37:52.044981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11084a127cda'
down_revision = 'ad0c130fee09'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relations_parent',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('value', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('relations_sub_child',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('value', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('relations_child',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('child_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['child_id'], ['relations_sub_child.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['relations_parent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('relations_one_to_one_child',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('child_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['child_id'], ['relations_child.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('child_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('relations_one_to_one_child')
    op.drop_table('relations_child')
    op.drop_table('relations_sub_child')
    op.drop_table('relations_parent')
    # ### end Alembic commands ###

import sqlalchemy as sa

from application.db.base_class import Base


class RelParent(Base):
    __tablename__ = 'relations_parent'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    value = sa.Column(sa.String(50))

    children = sa.orm.relationship('RelChild', back_populates='parent')


class RelChild(Base):
    __tablename__ = 'relations_child'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    parent_id = sa.Column(sa.Integer, sa.ForeignKey(RelParent.id))
    child_id = sa.Column(sa.Integer, sa.ForeignKey('relations_sub_child.id'))
    value = sa.Column(sa.String(50))

    parent = sa.orm.relationship(RelParent, back_populates='children')
    sub_child = sa.orm.relationship('RelSubChild', back_populates='child')
    o2o_child = sa.orm.relationship('RelOneToOneSubChild', back_populates='child')


class RelSubChild(Base):
    __tablename__ = 'relations_sub_child'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    value = sa.Column(sa.String(50))

    child = sa.orm.relationship(RelChild, back_populates='sub_child')


class RelOneToOneSubChild(Base):
    __tablename__ = 'relations_one_to_one_child'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    child_id = sa.Column(sa.Integer, sa.ForeignKey('relations_child.id'))
    value = sa.Column(sa.String(50))

    child = sa.orm.relationship(RelChild, back_populates='o2o_child', single_parent=True)

    __table_args__ = (
        sa.UniqueConstraint('child_id'),
    )

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from application.db.base_class import Base


class M1(Base):
    __tablename__ = 'session_m1'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    value = sa.Column(sa.String(50))


class UniqueModel(Base):
    __tablename__ = 'session_unique_model'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    value = sa.Column(sa.String(50), nullable=False, unique=True)


class Parent(Base):
    __tablename__ = 'session_parent'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    value = sa.Column(sa.String(50))

    children = relationship('Child', back_populates='parent')


class Child(Base):
    __tablename__ = 'session_child'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    parent_id = sa.Column(sa.Integer, sa.ForeignKey(Parent.id))

    parent = relationship(Parent, back_populates='children')

import sqlalchemy as sa

from application.db.base_class import Base


class LoadedParent(Base):
    __tablename__ = 'relations_loaded_parent'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    value = sa.Column(sa.String(50))

    # uncomment me
    # children = sa.orm.relationship('UnloadedChild', back_populates='parent')

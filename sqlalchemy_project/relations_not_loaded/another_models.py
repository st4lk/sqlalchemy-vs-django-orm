import sqlalchemy as sa

from application.db.base_class import Base


class UnloadedChild(Base):
    __tablename__ = 'relations_not_loaded_child'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    value = sa.Column(sa.String(50))
    parent_id = sa.Column(sa.Integer, sa.ForeignKey('relations_loaded_parent.id'))

    parent = sa.orm.relationship('LoadedParent', back_populates='children')

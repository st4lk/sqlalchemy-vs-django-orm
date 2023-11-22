import sqlalchemy as sa

from application.db.base_class import Base


class AnotherAppModel(Base):
    __tablename__ = 'relations_another_app_model'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    value = sa.Column(sa.String(50))

    children = sa.orm.relationship('RelChild', back_populates='parent')

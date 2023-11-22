import sqlalchemy as sa

from application.db.base_class import Base


class M1(Base):
    __tablename__ = 'connections_m1'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    value = sa.Column(sa.String(50))

import sqlalchemy as sa

from application.db.base_class import Base


class Storage(Base):
    __tablename__ = 'populate_existing_storage'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    key = sa.Column(sa.String(50), nullable=False, unique=True)
    value = sa.Column(sa.String(50), nullable=False)

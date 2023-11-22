import sqlalchemy as sa

from application.db.base_class import Base


class NullableFieldsModel(Base):
    __tablename__ = 'nullable_model'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    # docs: bit.ly/47FUxVq
    value = sa.Column(sa.String(50))

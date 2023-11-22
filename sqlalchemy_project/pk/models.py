import sqlalchemy as sa

from application.db.base_class import Base


class PkOnly(Base):
    __tablename__ = 'pk_only'

    id = sa.Column(sa.Integer, primary_key=True)


class PkIndex(Base):
    __tablename__ = 'pk_index'

    id = sa.Column(sa.Integer, primary_key=True, index=True)


class PkUnique(Base):
    __tablename__ = 'pk_unique'

    id = sa.Column(sa.Integer, primary_key=True, unique=True)


class PkIndexUnique(Base):
    __tablename__ = 'pk_index_unique'

    id = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)


class PkIdentity(Base):
    __tablename__ = 'pk_identity'

    # https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_serial
    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)

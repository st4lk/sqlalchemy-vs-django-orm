import sqlalchemy as sa

from application.db.base_class import Base


class FkRight(Base):
    __tablename__ = 'fk_right'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)


class FkLeft(Base):
    __tablename__ = 'fk_left'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    right_id = sa.Column(sa.Integer, sa.ForeignKey(FkRight.id))


class FkLeftIndex(Base):
    __tablename__ = 'fk_left_index'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    right_id = sa.Column(sa.Integer, sa.ForeignKey(FkRight.id), index=True)


# ------ deferred ----


class FkLeftDeferred(Base):
    __tablename__ = 'fk_left_deferred'

    id = sa.Column(sa.Integer, sa.Identity(), primary_key=True)
    right_id = sa.Column(
        sa.Integer,
        sa.ForeignKey(FkRight.id, deferrable=True, initially='DEFERRED'),
        index=True,
    )

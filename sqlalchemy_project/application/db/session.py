import logging

from pydantic import PostgresDsn
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from application import settings

logger = logging.getLogger(__name__)

sqlalchemy_database_uri = PostgresDsn.build(
    scheme="postgresql+asyncpg",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    port=int(settings.DB_PORT),
    host=settings.DB_HOST,
    path=settings.DB_NAME or '',
)

engine = create_async_engine(
    str(sqlalchemy_database_uri),
    echo=settings.DB_LOG,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    pool_recycle=settings.DB_POOL_RECYCLE,
    pool_timeout=settings.DB_POOL_TIMEOUT,
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session():
    async with SessionLocal() as db_session:
        logger.debug('Yielding new session: %s', db_session)
        yield db_session

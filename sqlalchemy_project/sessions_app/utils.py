import logging

import sqlalchemy as sa
from fastapi import Depends, Request, Path
from sqlalchemy.ext.asyncio import AsyncSession
from application.db.session import get_session
from .models import M1

logger = logging.getLogger(__name__)


async def get_m1_instance(
    request: Request,
    db_session: AsyncSession = Depends(get_session),
    m1_id: int = Path(..., title='M1 id'),
):
    query = sa.Select(M1).where(M1.id == m1_id)
    cursor = await db_session.execute(query)
    m1 = cursor.scalar_one()
    logger.info('*** Returning m1_instance from dependency: %s, session is: %s', m1, db_session)
    return m1

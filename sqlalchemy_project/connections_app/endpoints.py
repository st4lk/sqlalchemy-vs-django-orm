import asyncio
import logging
from typing import Optional

import sqlalchemy as sa
from fastapi import (
    APIRouter,
    Depends,
    Query,
    Request,
)
from sqlalchemy.ext.asyncio import AsyncSession
from application.db.session import SessionLocal, get_session
from .models import M1

router = APIRouter()
logger = logging.getLogger(__name__)


async def sleep_if_requested(sleep_seconds: int):
    logger.info('Sleeping for %s seconds', sleep_seconds)
    await asyncio.sleep(sleep_seconds)


@router.get(
    path='/api/connections/m1/',
    operation_id='api_models',
    status_code=200,
)
async def get_m1(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
        sleep_seconds: Optional[int] = Query(default=0),
):
    query = sa.Select(M1).order_by(M1.value)
    cursor = await db_session.execute(query)
    m1 = cursor.scalars().first()
    logger.debug('m1.value=%s', m1.value if m1 else None)
    if sleep_seconds:
        await sleep_if_requested(sleep_seconds)
    return {'value': m1.value} if m1 else {}


@router.get(
    path='/api/connections/m1/parallel/',
    operation_id='api_models',
    status_code=200,
)
async def get_m1_two_sessions(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
        sleep_seconds: Optional[int] = Query(default=0),
):
    query = sa.Select(M1).order_by(M1.value)
    cursor = await db_session.execute(query)
    m1_first = cursor.scalars().first()

    async with SessionLocal() as another_session:
        another_cursor = await another_session.execute(query)
        m1_last = another_cursor.scalars().last()

    if sleep_seconds:
        await sleep_if_requested(sleep_seconds)
    return {
        'first': {'id': m1_first.id, 'value': m1_first.value} if m1_first else {},
        'last': {'id': m1_last.id, 'value': m1_last.value} if m1_last else {},
    }

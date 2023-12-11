import logging

import sqlalchemy as sa
from fastapi import (
    APIRouter,
    Depends,
    Request,
)
from sqlalchemy.ext.asyncio import AsyncSession
from application.db.session import get_session
from .models import FkRight, FkLeft, FkLeftIndex

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get(
    path='/api/fk/query/',
    operation_id='api_fk_query',
    status_code=200,
)
async def fk_query(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
):
    query = sa.Select(
        FkLeft,
    ).join(
        FkRight,
        FkRight.id == FkLeft.right_id,
    ).where(
        FkRight.id == 95435,
    )
    cursor = await db_session.execute(query)
    instances = cursor.scalars().all()
    return [
        {
            'left.id': left.id,
            'left.right_id': left.right_id,
        } for left in instances
    ]


@router.get(
    path='/api/fk/query/index/',
    operation_id='api_fk_query',
    status_code=200,
)
async def fk_query_index(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
):
    query = sa.Select(
        FkLeftIndex,
    ).join(
        FkRight,
        FkRight.id == FkLeftIndex.right_id,
    ).where(
        FkRight.id == 95435,
    )
    cursor = await db_session.execute(query)
    instances = cursor.scalars().all()
    return [
        {
            'left.id': left.id,
            'left.right_id': left.right_id,
        } for left in instances
    ]

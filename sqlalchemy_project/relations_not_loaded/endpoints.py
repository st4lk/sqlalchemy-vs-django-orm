import logging

import sqlalchemy as sa
from fastapi import (
    APIRouter,
    Depends,
    Request,
)
from sqlalchemy.ext.asyncio import AsyncSession
from application.db.session import get_session
from .models import LoadedParent

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get(
    path='/api/relations/unloaded/',
    operation_id='api_models',
    status_code=200,
)
async def get_parent(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
):
    query = sa.Select(
        LoadedParent,
    )
    cursor = await db_session.execute(query)
    parents = cursor.scalars().all()
    return [
        {
            'id': parent.id,
            'value': parent.value,
        } for parent in parents
    ]

import logging

import sqlalchemy as sa
from fastapi import (
    APIRouter,
    Depends,
    Request,
)
from sqlalchemy.ext.asyncio import AsyncSession
from application.db.session import get_session
from .models import RelParent, RelChild

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get(
    path='/api/relations/parents/',
    operation_id='api_models',
    status_code=200,
)
async def get_parent(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
):
    query = sa.Select(
        RelParent,
    ).options(
        sa.orm.selectinload(RelParent.children).joinedload(RelChild.sub_child),
        sa.orm.selectinload(RelParent.children).joinedload(RelChild.o2o_child),
    )
    cursor = await db_session.execute(query)
    parents = cursor.scalars().all()
    return [
        {
            'id': parent.id,
            'value': parent.value,
            'children': [
                {
                    'id': child.id,
                    'value': child.value,
                    'sub_child': {
                        'id': child.sub_child.id,
                        'value': child.sub_child.value,
                    } if child.sub_child else None,
                    'o2o_child': {
                        'id': child.o2o_child[0].id,
                        'value': child.o2o_child[0].value,
                    },
                }
                for child in parent.children
            ],
        } for parent in parents
    ]

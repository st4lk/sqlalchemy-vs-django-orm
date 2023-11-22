import asyncio
import logging

import sqlalchemy as sa
from fastapi import (
    APIRouter,
    Depends,
    Path,
    Request,
)
from sqlalchemy.ext.asyncio import AsyncSession
from application.db.session import get_session
from .models import M1, Parent, Child, UniqueModel
from .utils import get_m1_instance

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get(
    path='/api/sessions/m1/{m1_id}/',
    operation_id='api_models',
    status_code=200,
)
async def get_m1_by_id(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
        m1_id: int = Path(..., title='M1 id'),
):
    query = sa.Select(M1).where(M1.id == m1_id)
    cursor = await db_session.execute(query)
    m1 = cursor.scalar_one()

    cursor = await db_session.execute(query)
    m1_v2 = cursor.scalar_one()
    logger.info('*** m1 is m1_v2: %s', m1 is m1_v2)
    return {
        'm1': {'id': m1.id, 'value': m1.value},
        'm1_v2': {'id': m1_v2.id, 'value': m1_v2.value},
    }


@router.get(
    path='/api/sessions/m1/{m1_id}/dependency/',
    operation_id='api_models',
    status_code=200,
)
async def get_m1_by_id_dependency(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
        m1_instance=Depends(get_m1_instance),
        m1_instance_b=Depends(get_m1_instance),
        m1_id: int = Path(..., title='M1 id'),
):
    query = sa.Select(M1).where(M1.id == m1_id)
    cursor = await db_session.execute(query)
    another_m1 = cursor.scalar_one()
    logger.info('*** another_m1 from endpoint: %s, session is: %s', another_m1, db_session)
    logger.info('*** m1_instance is another_m1: %s', m1_instance is another_m1)
    logger.info('*** m1_instance_b is another_m1: %s', m1_instance is another_m1)
    return {
        'm1_instance': {'id': m1_instance.id, 'value': m1_instance.value},
        'm1_instance_b': {'id': m1_instance_b.id, 'value': m1_instance_b.value},
        'another_m1': {'id': another_m1.id, 'value': another_m1.value},
    }


@router.get(
    path='/api/sessions/m1/{m1_id}/newsession/',
    operation_id='api_models',
    status_code=200,
)
async def get_from_new_session(
        request: Request,
        m1_instance=Depends(get_m1_instance),
        m1_id: int = Path(..., title='M1 id'),
):
    async for another_session in get_session():
        query = sa.Select(M1).where(M1.id == m1_id)
        another_cursor = await another_session.execute(query)
        another_m1 = another_cursor.scalars().first()
        logging.warning('another_m1 is m1_instance: %s', another_m1 is m1_instance)
    return {
        'm1_instance': {'id': m1_instance.id, 'value': m1_instance.value},
        'another_m1': {'id': another_m1.id, 'value': another_m1.value},
    }


@router.get(
    path='/api/sessions/m1/parallel/same/',
    operation_id='api_models',
    status_code=200,
)
async def get_same_session_parallel(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
):
    query_one = sa.Select(M1).where(M1.id == 1)
    query_two = sa.Select(M1).where(M1.id == 2)
    tasks = [
        asyncio.create_task(db_session.execute(query_one)),
        asyncio.create_task(db_session.execute(query_two)),
    ]
    results = await asyncio.gather(*tasks)
    one = results[0].scalar_one()
    two = results[1].scalar_one()
    return {
        'one': {'id': one.id, 'value': one.value},
        'two': {'id': two.id, 'value': two.value},
    }


@router.get(
    path='/api/sessions/m1/parallel/different/',
    operation_id='api_models',
    status_code=200,
)
async def get_different_session_parallel(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
):
    query_one = sa.Select(M1).where(M1.id == 1)
    query_two = sa.Select(M1).where(M1.id == 2)
    async for another_session in get_session():
        tasks = [
            asyncio.create_task(db_session.execute(query_one)),
            asyncio.create_task(another_session.execute(query_two)),
        ]
        results = await asyncio.gather(*tasks)
        one = results[0].scalar_one()
        two = results[1].scalar_one()
    return {
        'one': {'id': one.id, 'value': one.value},
        'two': {'id': two.id, 'value': two.value},
    }


@router.post(
    path='/api/sessions/m1/updatefield/same/',
    operation_id='api_models',
    status_code=200,
)
async def update_instance_field_same(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
):
    cursor_one = await db_session.execute(sa.Select(M1).where(M1.id == 1))
    another_cursor_one = await db_session.execute(sa.Select(M1).where(M1.id == 1))
    one = cursor_one.scalar_one()
    another_one = another_cursor_one.scalar_one()

    another_one.value = 'another-value-1'
    logger.info('one.value = %s', one.value)
    logger.info('another_one.value = %s', another_one.value)
    await db_session.commit()
    return {
        'one': {'id': one.id, 'value': one.value},
        'another_one': {'id': another_one.id, 'value': another_one.value},
    }


@router.post(
    path='/api/sessions/m1/updatefield/different/',
    operation_id='api_models',
    status_code=200,
)
async def update_instance_field_different(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
):
    cursor_one = await db_session.execute(sa.Select(M1).where(M1.id == 1))
    one = cursor_one.scalar_one()

    async for another_session in get_session():
        another_cursor_one = await another_session.execute(sa.Select(M1).where(M1.id == 1))
        another_one = another_cursor_one.scalar_one()
        another_one.value = 'another-value-3'
        logger.info('one.value = %s', one.value)
        logger.info('another_one.value = %s', another_one.value)
        if True:
            await another_session.flush()
        else:
            another_cursor_two = await another_session.execute(sa.Select(M1).where(M1.id == 2))
            another_two = another_cursor_two.scalar_one()
            logger.info('another_two.value = %s', another_two.value)
    await db_session.commit()
    return {
        'one': {'id': one.id, 'value': one.value},
        'another_one': {'id': another_one.id, 'value': another_one.value},
    }


@router.post(
    path='/api/sessions/updateunique/',
    operation_id='api_models',
    status_code=200,
)
async def update_unique(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
):
    cursor = await db_session.execute(sa.Select(UniqueModel).where(UniqueModel.value == 'two'))
    instance = cursor.scalar_one()

    await db_session.delete(instance)
    await db_session.execute(sa.Insert(UniqueModel).values({'value': 'two'}))
    await db_session.commit()
    return {
        'instance': {'id': instance.id, 'value': instance.value},
    }


@router.post(
    path='/api/sessions/parent/fk/',
    operation_id='api_models',
    status_code=200,
)
async def update_fk(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
):
    parent = Parent(value='unit-of-work-2')
    child = Child(parent=parent)
    db_session.add(parent)
    db_session.add(child)
    await db_session.commit()

    return {
        'parent': {'id': parent.id, 'value': parent.value},
        'child': {'id': child.id, 'child.parent_id': child.parent_id},
    }

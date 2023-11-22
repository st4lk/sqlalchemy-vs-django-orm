import logging

import sqlalchemy as sa
from fastapi import (
    APIRouter,
    Depends,
    Body,
    Request,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert as upsert
from application.db.session import get_session
from .models import Storage

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    path='/api/populate/wrong/',
    operation_id='api_populate',
    status_code=200,
)
async def old_value(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
        data=Body(...),
):
    key = 'one'
    value = data['value']
    cursor = await db_session.execute(sa.Select(Storage).where(Storage.key == key))
    # already fetched instance
    instance = cursor.scalar_one_or_none()
    logger.info('instance = %s', instance)

    upsert_statement = upsert(Storage).values(
        key=key, value=value,
    ).on_conflict_do_update(
        index_elements=[Storage.key],
        set_={'value': value},
    ).returning(Storage)
    cursor = await db_session.execute(upsert_statement)
    upserted_instance = cursor.scalar_one()
    await db_session.commit()

    new_cursor = await db_session.execute(sa.Select(Storage).where(Storage.key == key))
    fresh_instance = new_cursor.scalar_one()

    return {
        'upserted_instance.key': upserted_instance.key,
        'upserted_instance.value': upserted_instance.value,
        'fresh_instance.key': fresh_instance.key,
        'fresh_instance.value': fresh_instance.value,
    }


@router.post(
    path='/api/populate/existing/',
    operation_id='api_populate',
    status_code=200,
)
async def populate_existing(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
        data=Body(...),
):
    key = 'one'
    value = data['value']
    cursor = await db_session.execute(sa.Select(Storage).where(Storage.key == key))
    # already fetched instance
    instance = cursor.scalar_one_or_none()
    logger.info('instance = %s', instance)

    upsert_statement = upsert(Storage).values(
        key=key, value=value,
    ).on_conflict_do_update(
        index_elements=[Storage.key],
        set_={'value': value},
    ).returning(Storage)

    statement = sa.Select(
        Storage,
    ).from_statement(
        upsert_statement,
    ).execution_options(populate_existing=True)
    cursor = await db_session.execute(statement)
    upserted_instance = cursor.scalar_one()
    await db_session.commit()

    new_cursor = await db_session.execute(sa.Select(Storage).where(Storage.key == key))
    fresh_instance = new_cursor.scalar_one()

    return {
        'upserted_instance.key': upserted_instance.key,
        'upserted_instance.value': upserted_instance.value,
        'fresh_instance.key': fresh_instance.key,
        'fresh_instance.value': fresh_instance.value,
    }


@router.post(
    path='/api/populate/refresh/',
    operation_id='api_populate',
    status_code=200,
)
async def refresh(
        request: Request,
        db_session: AsyncSession = Depends(get_session),
        data=Body(...),
):
    key = 'one'
    value = data['value']
    cursor = await db_session.execute(sa.Select(Storage).where(Storage.key == key))
    # already fetched instance
    instance = cursor.scalar_one_or_none()
    logger.info('instance = %s', instance)

    upsert_statement = upsert(Storage).values(
        key=key, value=value,
    ).on_conflict_do_update(
        index_elements=[Storage.key],
        set_={'value': value},
    ).returning(Storage)
    cursor = await db_session.execute(upsert_statement)
    upserted_instance = cursor.scalar_one()
    await db_session.commit()

    await db_session.refresh(upserted_instance)
    new_cursor = await db_session.execute(sa.Select(Storage).where(Storage.key == key))
    fresh_instance = new_cursor.scalar_one()

    return {
        'upserted_instance.key': upserted_instance.key,
        'upserted_instance.value': upserted_instance.value,
        'fresh_instance.key': fresh_instance.key,
        'fresh_instance.value': fresh_instance.value,
    }

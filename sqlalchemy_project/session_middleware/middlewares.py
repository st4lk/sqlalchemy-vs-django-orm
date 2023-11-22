from fastapi import Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from application.db.session import SessionLocal


# @app.middleware("http")  # uncomment me
async def db_session_middleware(request: Request, call_next):
    """
    Open db session in middleware.
    Advantages over isolated opening session (with yield):
    - same session can be used in middleware and in request
    - when other dependencies are using get_session - the session will be the same, not new one
    """
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        await request.state.db.close()
    return response


# use as dependency:


def get_session(request: Request) -> AsyncSession:
    return request.state.db

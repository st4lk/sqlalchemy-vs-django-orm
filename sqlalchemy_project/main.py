import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from application import api, settings
from application.db.session import SessionLocal
from application.loaders import pre_load_all_models

app = FastAPI(
    title=settings.SERVICE_NAME,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     """
#     Open db session in middleware.
#     Advantages over isolated opening session (with yield):
#     - same session can be used in middleware and in request
#     - when other dependencies are using get_session - the session will be the same, not new one
#     """
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         await request.state.db.close()
#     return response

pre_load_all_models()
app.include_router(api.router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        loop='uvloop',
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=True,
    )

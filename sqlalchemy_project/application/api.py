from fastapi import APIRouter

from connections_app.endpoints import router as connections_router
from fk.endpoints import router as fk_router
from populate_existing.endpoints import router as populate_router
from relations.endpoints import router as relations_router
from relations_not_loaded.endpoints import router as relations_not_loaded_router
from sessions_app.endpoints import router as sessions_router

router = APIRouter()

router.include_router(connections_router)
router.include_router(fk_router)
router.include_router(populate_router)
router.include_router(relations_not_loaded_router)
router.include_router(relations_router)
router.include_router(sessions_router)

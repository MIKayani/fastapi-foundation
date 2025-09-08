from fastapi import APIRouter
from app.schemas.config_schema import settings
from app.core.config import get_postgres_connection

router = APIRouter(
    prefix="/server_info",
    tags=["Server Info"],
)

@router.get("/health", response_model=dict)
async def health_check():
    return {"status": "ok"}

@router.get("/readiness", response_model=dict)
async def readiness_check():
    try:
        with get_postgres_connection() as conn:
            with conn.cursor() as curr:
                pass
        return {"ready": True}
    except Exception:
        return {"ready": False}

@router.get("/liveness", response_model=dict)
async def liveness_check():
    return {"alive": True}


@router.get("/version", response_model=dict)
async def version_info():
    return {"title": settings.APP_TITLE, "version": settings.APP_VERSION, "description": settings.APP_DESCRIPTION}
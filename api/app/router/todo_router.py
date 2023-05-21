import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from api.app.config import settings

router = APIRouter(prefix=settings.PREFIX)
logger = logging.getLogger(__name__)


@router.get("/health")
async def health():
    try:
        logger.info("Write something")
        logger.debug("Write this")
        return JSONResponse(content={"Status": "OK"}, media_type="application/json", status_code=200)
    except Exception as e:
        logger.error(f"Something wrong in health check: {e}")
        return JSONResponse(content={"Status": "KO"}, media_type="application/json", status_code=500)

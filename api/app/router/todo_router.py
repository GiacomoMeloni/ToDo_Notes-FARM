from fastapi import APIRouter

from api.app.config import settings

router = APIRouter(prefix=settings.PREFIX, tags=["todo"])


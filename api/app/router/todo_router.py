from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from api.app.config import settings

router = APIRouter(prefix=settings.PREFIX, tags=["todo"])


@router.get('/test_health')
async def test() -> JSONResponse:
    return JSONResponse(content={"message": "ToDo Working!"},
                        status_code=status.HTTP_200_OK)

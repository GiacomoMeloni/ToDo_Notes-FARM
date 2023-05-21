from fastapi import APIRouter

from api.app.config import settings
from api.app.schemas.user_schema import UserAuth

user_router = APIRouter(prefix=settings.PREFIX)

@user_router.post('/create', summary="Create a new user")
async def create_user(data: UserAuth):
    Us
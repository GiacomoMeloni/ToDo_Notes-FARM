from pymongo import errors
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from api.app.config import settings
from api.app.schemas.user_schema import UserAuth, CreateUserResponse
from api.app.services.user_service import UserService

router = APIRouter(prefix=settings.PREFIX)


@router.post('/create', summary="Create a new user", response_model=CreateUserResponse)
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except errors.DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User with this email or username already exist")
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"status": "KO",
                                     "message": "User with this email or username already exist"})

import pymongo.errors
from pymongo import errors
from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException, status, Depends

from api.app.config import settings
from api.app.models.user_model import User
from api.app.deps.user_deps import get_current_user
from api.app.services.user_service import UserService
from api.app.schemas.user_schema import UserAuth, UserOutData, UserUpdate


router = APIRouter(prefix=f"{settings.PREFIX}/user", tags=["users"])


@router.post('/create', summary="Create a new user", response_model=UserOutData)
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


@router.get('/me', summary="Get details of currently logged user", response_model=UserOutData)
async def get_logged_user(user: User = Depends(get_current_user)):
    return user


@router.post('/update', summary="Update User", response_model=UserOutData)
async def update_user(data: UserUpdate, user: User = Depends(get_current_user)):
    try:
        return await UserService.update_user(user.user_id, data=data)
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User does not exist")

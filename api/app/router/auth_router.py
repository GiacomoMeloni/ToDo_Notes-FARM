from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from api.app.config import settings
from api.app.schemas.auth_schema import TokenSchema
from api.app.services.user_service import UserService
from api.app.security import create_access_token, create_refresh_token

router = APIRouter(prefix=settings.PREFIX, tags=["auth"])


@router.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect email or password")

    return {"access_token": create_access_token(user.user_id),
            "refresh_token": create_refresh_token(user.user_id)}

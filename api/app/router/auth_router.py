from jose import jwt
from typing import Any
from pydantic import ValidationError
from fastapi import APIRouter, Depends, HTTPException, status,Body
from fastapi.security import OAuth2PasswordRequestForm

from api.app.config import settings
from api.app.models.user_model import User
from api.app.schemas.auth_schema import TokenSchema
from api.app.schemas.user_schema import UserOutData
from api.app.deps.user_deps import get_current_user
from api.app.schemas.auth_schema import TokenPayload
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


@router.post('/test-token', summary="Test if the access token is valid", response_model=UserOutData)
async def test_token(user: User = Depends(get_current_user)):
    return user


@router.post('/refresh', summary="Refresh token", response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(refresh_token,
                             settings.JWT_REFRESH_SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        token_data = TokenPayload(**payload)

    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

    user = await UserService.get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return {"access_token": create_access_token(user.user_id),
            "refresh_token": create_refresh_token(user.user_id)}

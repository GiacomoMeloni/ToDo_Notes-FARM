from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from api.app.config import settings
from api.app.services.user_service import UserService

router = APIRouter(prefix=settings.PREFIX)


@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(email=form_data.email, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect email or password")

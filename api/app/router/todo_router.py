from fastapi import APIRouter, status, Depends

from api.app.config import settings
from api.app.models.todo_model import ToDo
from api.app.models.user_model import User
from api.app.deps.user_deps import get_current_user
from api.app.services.todo_service import TodoService
from api.app.schemas.todo_schema import ToDoOut, ToDoCreate


router = APIRouter(prefix=settings.PREFIX, tags=["todo"])


@router.get('/', summary="Get all user's todos", response_model=ToDoOut)
async def get_todos(current_user: User = Depends(get_current_user)):
    return await TodoService.list_todos(user=current_user)


@router.post('/create', summary="Create a todo", response_model=ToDo)
async def create_todo(data: ToDoCreate, current_user: User = Depends(get_current_user)):
    return await TodoService.create_todo(data=data, user=current_user)

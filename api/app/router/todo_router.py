from typing import List
from uuid import UUID
from fastapi import APIRouter, status, Depends

from api.app.config import settings
from api.app.models.todo_model import ToDo
from api.app.models.user_model import User
from api.app.deps.user_deps import get_current_user
from api.app.services.todo_service import TodoService
from api.app.schemas.todo_schema import ToDoOut, ToDoCreate, ToDoUpdate


router = APIRouter(prefix=f"{settings.PREFIX}/todo", tags=["todo"])


@router.get('/', summary="Get all user's todos", response_model=List[ToDoOut])
async def get_todos(current_user: User = Depends(get_current_user)):
    return await TodoService.list_todos(user=current_user)


@router.post('/create', summary="Create a todo", response_model=ToDo)
async def create_todo(data: ToDoCreate, current_user: User = Depends(get_current_user)):
    return await TodoService.create_todo(data=data, user=current_user)


@router.get('/{todo_id}', summary="Get a ToDo by ID", response_model=ToDoOut)
async def get_todo(todo_id: UUID, current_user: User = Depends(get_current_user)):
    return await TodoService.get_todo(todo_id=todo_id, user=current_user)


@router.put('/{todo_id}', summary="Update ToDo by ID", response_model=ToDoOut)
async def update_todo(todo_id: UUID, data: ToDoUpdate, current_user: User = Depends(get_current_user)):
    return await TodoService.update_todo(todo_id=todo_id, user=current_user, data=data)


@router.delete('/{todo_id}', summary="Delete ToDo by ID", response_model=ToDoOut)
async def update_todo(todo_id: UUID, current_user: User = Depends(get_current_user)):
    return await TodoService.delete_todo(todo_id=todo_id, user=current_user)

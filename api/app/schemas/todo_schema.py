from datetime import datetime
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class ToDoCreate(BaseModel):
    title: str = Field(..., title='ToDo Title', max_length=55, min_length=1)
    description: str = Field(..., title='ToDo Description', max_length=7555, min_length=1)
    status: Optional[bool] = False


class ToDoUpdate(BaseModel):
    title: Optional[str] = Field(..., title='ToDo Title', max_length=55, min_length=1)
    description: Optional[str] = Field(..., title='ToDo Description', max_length=7555, min_length=1)
    status: Optional[bool] = False


class ToDoOut(BaseModel):
    todo_id: UUID
    status: bool
    title: str
    description: str
    created_at: datetime
    modified_at: datetime

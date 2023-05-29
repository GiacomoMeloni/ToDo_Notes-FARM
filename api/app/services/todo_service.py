from uuid import UUID
from typing import List
from api.app.models.user_model import User
from api.app.models.todo_model import ToDo
from api.app.schemas.todo_schema import ToDoCreate


class TodoService:
    @staticmethod
    async def list_todos(user: User) -> List[ToDo]:
        todos = await ToDo.find(ToDo.owner.id == user.user_id).to_list()
        return todos

    @staticmethod
    async def create_todo(data: ToDoCreate, user: User):
        todo = ToDo(**data.dict(), owner=user)
        return await todo.insert()

    @staticmethod
    async def get_todo(todo_id: UUID, user: User):
        todo = ToDo.find_one(ToDo.todo_id == todo_id, ToDo.owner.id == user.id)
        return todo

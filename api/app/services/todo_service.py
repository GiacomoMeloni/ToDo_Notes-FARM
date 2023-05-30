from uuid import UUID
from typing import List
from api.app.models.user_model import User
from api.app.models.todo_model import ToDo
from api.app.schemas.todo_schema import ToDoCreate, ToDoUpdate


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

    @staticmethod
    async def update_todo(todo_id: UUID, user: User, data: ToDoUpdate):
        todo = await TodoService.get_todo(todo_id=todo_id, user=user)
        await todo.update({"$set": data.dict(exclude_unset=True)})

        await todo.save()
        return todo

    @staticmethod
    async def delete_todo(todo_id: UUID, user: User):
        todo = await TodoService.get_todo(todo_id=todo_id, user=user)
        if todo:
            await todo.delete()

        return None

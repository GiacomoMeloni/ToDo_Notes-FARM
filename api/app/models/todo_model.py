from uuid import UUID, uuid4
from datetime import datetime
from pydantic import Field
from beanie import Document, Indexed, Link, before_event, Replace, Insert

from .user_model import User


class ToDo(Document):
    todo_id: UUID = Field(default_factory=uuid4, unique=True)
    status: bool = False
    title: Indexed(str)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    modified_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]

    def __repr__(self) -> str:
        return f"<Todo {self.title}"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ToDo):
            return self.todo_id == other.todo_id
        return False

    @before_event([Replace, Insert])
    def update_modified_at(self):
        self.modified_at = datetime.utcnow()

    class Settings:
        name = "todos"

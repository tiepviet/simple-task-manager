from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date
from uuid import UUID

class TaskBase(BaseModel):
    title: str
    detail: Optional[str] = None
    due_date: Optional[date] = None
    priority: int = 0

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str] = None
    status: Optional[str] = None

class TaskStatusUpdate(BaseModel):
    status: str

class TaskInDB(TaskBase):
    id: UUID
    status: str
    owner_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class Task(TaskInDB):
    pass

class TaskList(BaseModel):
    id: UUID
    title: str
    status: str
    priority: int
    due_date: Optional[date] = None
    created_at: datetime

    class Config:
        from_attributes = True 
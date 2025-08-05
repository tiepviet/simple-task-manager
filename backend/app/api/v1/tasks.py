from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from datetime import date
from app.core.database import get_db
from app.core.auth import get_current_active_user, get_current_admin_user
from app.crud.task import get_task, get_tasks, get_all_tasks, create_task, update_task, update_task_status, delete_task
from app.schemas.task import Task, TaskCreate, TaskUpdate, TaskStatusUpdate, TaskList
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[TaskList])
def read_tasks(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = Query(None, description="Filter by status (todo/done)"),
    priority: Optional[int] = Query(None, description="Filter by priority (0-3)"),
    due_before: Optional[date] = Query(None, description="Filter by due date (YYYY-MM-DD)"),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    tasks = get_tasks(
        db, 
        user_id=str(current_user.id), 
        skip=skip, 
        limit=limit,
        status=status,
        priority=priority,
        due_before=due_before
    )
    return tasks

@router.post("/", response_model=Task)
def create_new_task(
    task: TaskCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    return create_task(db=db, task=task, user_id=str(current_user.id))

@router.get("/{task_id}", response_model=Task)
def read_task(
    task_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    task = get_task(db, task_id=task_id, user_id=str(current_user.id))
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=Task)
def update_existing_task(
    task_id: str,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    task = update_task(db, task_id=task_id, task_update=task_update, user_id=str(current_user.id))
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.patch("/{task_id}/status", response_model=Task)
def update_task_status_endpoint(
    task_id: str,
    status_update: TaskStatusUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    task = update_task_status(db, task_id=task_id, status=status_update.status, user_id=str(current_user.id))
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete_existing_task(
    task_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    task = delete_task(db, task_id=task_id, user_id=str(current_user.id))
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"} 
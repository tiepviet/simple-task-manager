from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import List, Optional
from datetime import date
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def get_task(db: Session, task_id: str, user_id: str):
    return db.query(Task).filter(
        and_(Task.id == task_id, Task.owner_id == user_id)
    ).first()

def get_tasks(
    db: Session, 
    user_id: str, 
    skip: int = 0, 
    limit: int = 100,
    status: Optional[str] = None,
    priority: Optional[int] = None,
    due_before: Optional[date] = None
):
    query = db.query(Task).filter(Task.owner_id == user_id)
    
    if status:
        query = query.filter(Task.status == status)
    if priority is not None:
        query = query.filter(Task.priority == priority)
    if due_before:
        query = query.filter(Task.due_date <= due_before)
    
    return query.offset(skip).limit(limit).all()

def get_all_tasks(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    user_id: Optional[str] = None,
    status: Optional[str] = None
):
    query = db.query(Task)
    
    if user_id:
        query = query.filter(Task.owner_id == user_id)
    if status:
        query = query.filter(Task.status == status)
    
    return query.offset(skip).limit(limit).all()

def create_task(db: Session, task: TaskCreate, user_id: str):
    db_task = Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: str, task_update: TaskUpdate, user_id: str):
    db_task = get_task(db, task_id, user_id)
    if db_task:
        update_data = task_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def update_task_status(db: Session, task_id: str, status: str, user_id: str):
    db_task = get_task(db, task_id, user_id)
    if db_task:
        db_task.status = status
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: str, user_id: str):
    db_task = get_task(db, task_id, user_id)
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task 
from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.auth import get_current_admin_user
from app.crud.user import get_users
from app.crud.task import get_all_tasks
from app.schemas.user import User
from app.schemas.task import TaskList
from app.models.user import User as UserModel

router = APIRouter()

@router.get("/users", response_model=List[User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.get("/tasks", response_model=List[TaskList])
def read_all_tasks(
    skip: int = 0,
    limit: int = 100,
    user_id: Optional[str] = Query(None, description="Filter by user ID"),
    status: Optional[str] = Query(None, description="Filter by status (todo/done)"),
    current_user: UserModel = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    tasks = get_all_tasks(
        db, 
        skip=skip, 
        limit=limit,
        user_id=user_id,
        status=status
    )
    return tasks 
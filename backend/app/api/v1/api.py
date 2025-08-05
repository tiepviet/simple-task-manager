from fastapi import APIRouter
from app.api.v1 import auth, tasks, admin

api_router = APIRouter()

# Include all routers
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"]) 
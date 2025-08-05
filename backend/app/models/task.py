from sqlalchemy import Column, String, Integer, Date, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(100), nullable=False)
    detail = Column(Text, nullable=True)
    status = Column(String(10), nullable=False, default="todo")  # todo, done
    due_date = Column(Date, nullable=True)
    priority = Column(Integer, default=0)  # 0: low, 1: medium, 2: high, 3: urgent
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationship
    owner = relationship("User", back_populates="tasks") 
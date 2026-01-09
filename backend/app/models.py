from sqlalchemy import Column, Integer, String, Date, DateTime
from datetime import datetime
from db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    due_date = Column(Date, nullable=True)
    priority = Column(String, default="Medium")
    status = Column(String, default="Todo")
    created_at = Column(DateTime, default=datetime.utcnow)

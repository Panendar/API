from fastapi import FastAPI
from pydantic import BaseModel, field_validator, Field
from datetime import datetime, timedelta

app = FastAPI()

class TaskCreate(BaseModel):
    """Request for creating a task"""
    title: str = Field(..., min_length=3, max_length=35)
    description: str | None = None
    due_date: datetime = Field(default_factory=lambda: datetime.now() + timedelta(hours=24))   # Default due date is 24 hours from now
    priority: int = Field(1, ge=1, le=5)
    completed: bool = False

    @field_validator('due_date')
    @classmethod
    def valid_date_time(cls, v):
        if v<=datetime.now():
            raise ValueError("Due date must be in the future")
        return v
    

    
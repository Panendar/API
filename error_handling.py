from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, field_validator, ValidationError

app = FastAPI()

#fake database

tasks = {
    1: {"title": "Buy groceries", "description": "Milk, Bread, Eggs", "completed": False},
    2: {"title": "Read book", "description": "Finish reading '1984'", "completed": True}
}

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Task with id {task_id} not found")
    return tasks[task_id]

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Task with id {task_id} not found")
    del tasks[task_id]
    return {"message": f"Task with id {task_id} has been deleted"}
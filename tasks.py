# from fastapi import FastAPI

# app = FastAPI()

# from datetime import datetime

# @app.get("/tasks")
# def get_all_tasks():
#     return ({"tasks": ["task1", "task2", "task3"]})

# # get task by task-id
# @app.get("/tasks/{task_id}")
# def get_task(task_id: int):
#     return ({"task_id": task_id, "Name": "Sample Task"})


# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from datetime import datetime

# app = FastAPI()

# class TaskCreate(BaseModel):
#     """Request model for creating a task"""
#     title: str
#     description: str| None =None

# class TaskResponse(BaseModel):
#     """Response model for a created task"""
#     Task_id: int
#     title: str
#     description: str| None = None
#     created_at: str

# @app.post("/tasks", response_model=TaskResponse)
# def create_task(task_create: TaskCreate):
#     task_created = {
#         "Task_id": 1,
#         "title": task_create.title,
#         "description": task_create.description,
#         "created_at": datetime.now().isoformat()
#     }
#     return task_created


# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class TaskManager(BaseModel):
#     task_id: int
#     task_name: str
#     description: str = ""
#     completed: bool = False

# class CreateTask(BaseModel):
#     task_name: str
#     description: str = ""
#     completed: bool = False

# @app.post("/tasks")
# def create_task(task: CreateTask):
#     new_task = TaskManager(
#         task_id=1,
#         task_name=task.task_name,
#         description=task.description,
#         completed=task.completed
#     )

#     return {
#         "message": "Task Created Successfully",
#         "task": new_task.dict()
#     }

# from fastapi import FastAPI, status
# app = FastAPI()
# @app.get("/task", status_code=status.HTTP_201_CREATED)
# def read_task():
#     return {"message": "Task Created"}


# from fastapi import FastAPI, HTTPException

# app = FastAPI()
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     if user_id == 1:
#         return {"user_id": user_id, "name": "John Doe"}
#     elif user_id == 2:
#         return {"user_id": user_id, "name": "Jane Smith"}
#     else:
#         raise HTTPException(status_code= 404, detail="User not found")



# TASK MANAGER WITH BASIC CRUD OPERATIONS
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()
class Task(BaseModel):
    id: int
    name: str
    description: str | None = None
    completed: bool = False
    date_created: str | None = datetime.now().isoformat()

class TaskCreate(BaseModel):
    name : str
    description: str | None = None
    completed : bool =False

class GetTask(BaseModel):
    id: int
    name: str
    description: str | None = None
    completed: bool = False

tasks_db: dict[int, dict] = {
    1: {"id": 1, "name": "Task One", "description": "First Task", "completed": False},
    2: {"id": 2, "name": "Task Two", "description": "Second Task", "completed": True},
}

@app.post("/tasks", response_model=Task)
def create_task(create: TaskCreate):
    new_id = max(tasks_db.keys()) + 1 if tasks_db else 1
    description = create.description if create.description else ""
    completed = create.completed if create.completed else False
    created_at = datetime.now().isoformat()
    new_task ={
        "id": new_id,
        "name": create.name,
        "description": create.description,
        "completed": completed,
        "date_created": created_at
    }
    tasks_db[new_id] = new_task
    return new_task

@app.get("/tasks", response_model=list[GetTask])
def get_all_tasks():
    return list(tasks_db.values())

@app.get("/tasks/{task_id}", response_model=GetTask)
def get_task(task_id: int):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
        return ({"message": "Task not found"})
    return task
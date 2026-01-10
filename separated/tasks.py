import sys
from pathlib import Path
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from fastapi import FastAPI, HTTPException, status
from separated.createTask import TaskCreate
from separated.services import TaskService, tasks_db


app = FastAPI(title="Separated Tasks API")
task_service = TaskService()

def _with_id(task_id: int, task: dict) -> dict:
    return task if "ID" in task else {"ID": task_id, **task}


@app.get("/tasks")
def list_tasks():
    return [_with_id(task_id, task) for task_id, task in tasks_db.items()]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return _with_id(task_id, task)


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    return task_service.CreateTask(task)


# if __name__ == "__main__":
#     # Quick smoke test when run as a script (doesn't start a server).
#     created = task_service.CreateTask(
#         TaskCreate(
#             title="Finish project",
#             description="Complete the FastAPI project",
#             priority=1,
#             completed=False,
#         )
#     )
#     print(created)
print("Running quick test...")
print("=" *129)
check = task_service.CreateTask(
        TaskCreate(
            title="Finish project",
            description="Complete the FastAPI project",
            priority=1,
            completed=False,
        ))
print("=" *129)
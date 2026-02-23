# API 

A small FastAPI playground with two example apps:

- `main.py`: greeting endpoints
- `tasks.py`: in-memory task manager (basic CRUD sample)

## Prerequisites

- Python 3.10+ recommended

## Install

```bash
pip install fastapi uvicorn
```

## Run

Run the greeting API:

```bash
uvicorn main:app --reload
```

Run the task manager API:

```bash
uvicorn tasks:app --reload
```

## Endpoints

### Greeting API (`main.py`)

- `GET /`
- `GET /{name}?q=<language>`

### Task Manager (`tasks.py`)

- `GET /tasks`
- `GET /tasks/{task_id}`
- `POST /tasks`

Example create:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"name":"Learn FastAPI","description":"Build sample API","completed":false}'
```
# DATABASE API'S
USING API'S to PERFORM CRUD OPERATIONS
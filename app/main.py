
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

class Task(BaseModel):
    id: str
    title: str
    status: str = "pending"

class TaskCreate(BaseModel):
    title: str

tasks = []

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    new_task = Task(id=str(uuid4()), title=task.title)
    tasks.append(new_task)
    return new_task

@app.get("/tasks", response_model=List[Task])
def get_tasks(status: str = None):
    if status:
        return [t for t in tasks if t.status == status]
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")



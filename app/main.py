from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="To-Do Backend")

# In-memory storage
tasks = []
task_id_counter = 1

class Task(BaseModel):
    title: str
    completed: bool = False

class TaskResponse(Task):
    id: int

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: Task):
    global task_id_counter
    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "completed": task.completed
    }
    tasks.append(new_task)
    task_id_counter += 1
    return new_task

@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["completed"] = updated_task.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

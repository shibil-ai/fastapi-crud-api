
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# SQLAlchemy setup
DATABASE_URL = "sqlite:///./tasks.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Task Model
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models for request and response
class TaskCreate(BaseModel):
    title: str
    description: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str

class TaskList(BaseModel):
    tasks: List[TaskResponse]

# Create a new task
@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    db = SessionLocal()
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()
    return db_task

# Get all tasks
@app.get("/tasks/", response_model=TaskList)
def get_tasks():
    db = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return {"tasks": tasks}

# Get a task by ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    db.close()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update a task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate):
    db = SessionLocal()
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        db.close()
        raise HTTPException(status_code=404, detail="Task not found")
    db_task.title = task.title
    db_task.description = task.description
    db.commit()
    db.refresh(db_task)
    db.close()
    return db_task

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        db.close()
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    db.close()
    return {"message": "Task deleted"}

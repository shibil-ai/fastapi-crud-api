# FastAPI CRUD API

This project demonstrates a simple CRUD API using FastAPI and SQLite. It allows users to create, read, update, and delete tasks.

## Features
- Create, Read, Update, and Delete (CRUD) operations
- Built with **FastAPI** for quick API development
- Uses **SQLAlchemy** as ORM with **SQLite** for storage
- Swagger UI for API documentation

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/shibil-ai/fastapi-crud-api.git
   ```
2. Install the required packages:
   ```bash
   pip install fastapi uvicorn sqlalchemy
   ```
3. Run the API server:
   ```bash
   uvicorn main:app --reload
   ```
4. Access the API at:
   ```
   http://127.0.0.1:8000
   ```
   Visit the Swagger UI:
   ```
   http://127.0.0.1:8000/docs
   ```

## Endpoints
- `POST /tasks/`: Create a new task
- `GET /tasks/`: Retrieve all tasks
- `GET /tasks/{task_id}`: Retrieve a specific task by ID
- `PUT /tasks/{task_id}`: Update a task by ID
- `DELETE /tasks/{task_id}`: Delete a task by ID

## Example Usage
1. Create a task:
   ```bash
   curl -X POST "http://127.0.0.1:8000/tasks/" -d '{"title": "Learn FastAPI", "description": "Build CRUD API"}'
   ```
2. Get all tasks:
   ```bash
   curl http://127.0.0.1:8000/tasks/
   ```

## License
This project is licensed under the MIT License.

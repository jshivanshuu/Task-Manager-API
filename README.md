# Task Manager API

A simple task management REST API built with FastAPI, SQLAlchemy, SQLite, and JWT-based authentication.

## Features

- User signup with password hashing
- User login with JWT access token generation
- Create tasks
- List all tasks
- SQLite database for local development

## Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Passlib with bcrypt
- Python-JOSE for JWT

## Project Structure

```text
Task-Manager-API/
|-- app/
|   |-- auth.py
|   |-- crud.py
|   |-- database.py
|   |-- dependencies.py
|   |-- main.py
|   |-- models.py
|   |-- schema.py
|   `-- routes/
|       |-- task.py
|       `-- user.py
|-- requirements.txt
|-- README.md
`-- test.db
```

## API Endpoints

### Auth

- `POST /signup` - Create a new user
- `POST /login` - Authenticate a user and return an access token

Example signup request:

```json
{
  "email": "user@example.com",
  "password": "secret123"
}
```

Example login response:

```json
{
  "access_token": "<jwt-token>"
}
```

### Tasks

- `POST /tasks` - Create a task
- `GET /tasks` - Get all tasks

Example create task request:

```json
{
  "title": "Finish README",
  "description": "Write clear project documentation"
}
```

## Getting Started

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

`requirements.txt` is currently empty, so install the packages used by the project manually:

```powershell
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose
```

### 3. Run the application

```powershell
uvicorn app.main:app --reload
```

The API will be available at:

- `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Database

- The app uses SQLite by default
- Database URL: `sqlite:///./test.db`
- Tables are created automatically when the app starts

## Current Limitations

- Task creation currently uses a temporary hardcoded `owner_id=1`
- Task routes are not protected by authentication yet
- `requirements.txt` has not been populated
- `crud.py` exists but is not used yet
- The JWT secret is hardcoded and should be moved to environment variables before production use

## Next Improvements

- Protect task routes with JWT authentication
- Link tasks to the authenticated user instead of a hardcoded owner
- Add update and delete task endpoints
- Add response models and better error handling
- Move configuration values into environment variables
- Add tests and populate `requirements.txt`

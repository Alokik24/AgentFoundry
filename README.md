
# AgentFoundry – AutoTasker Agent

[![License](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-in%20progress-yellow.svg)]()

**AgentFoundry** is an open-source developer platform to build, test, and deploy LLM-powered agents with memory, observability, and real-world integration.

🧠 `AutoTasker` is the first module — a task classification + automation agent built using **FastAPI**, **PostgreSQL**, and **LLM logic**.

---

## 🚀 Features

- Async FastAPI backend
- PostgreSQL integration via SQLAlchemy
- Modular structure for agent plug-ins
- OpenAPI auto-docs via Swagger
- Production-ready folder setup

---

## 🗂 Folder Structure

```
agentfoundry/
├── agents/
│   └── autotasker/
│       ├── main.py         # FastAPI entrypoint
│       ├── db.py           # PostgreSQL config
│       ├── models.py       # SQLAlchemy models
│       ├── schemas.py      # Pydantic validation
│       ├── routes.py       # REST API endpoints
│       └── agent.py        # GPT agent logic (coming soon)
├── tests/                  # Unit tests
│   └── test_routes.py
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone + Install
```bash
git clone https://github.com/<yourusername>/agentfoundry.git
cd agentfoundry
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 2. PostgreSQL Setup

```bash
# Ubuntu
sudo apt install postgresql postgresql-contrib
sudo -u postgres psql
```

Inside `psql`:
```sql
CREATE DATABASE agentfoundry;
CREATE USER af_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE agentfoundry TO af_user;
\q
```

Create a `.env` file:

```env
DATABASE_URL=postgresql+asyncpg://af_user:password@localhost:5432/agentfoundry
```

---

## Run the Server

```bash
uvicorn agents.autotasker.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI  
Health check: [http://localhost:8000/autotasker/ping](http://localhost:8000/autotasker/ping)

---

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy (Async)](https://docs.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)

---

## Task API – REST Endpoints

### 🔸 Create a Task
```http
POST /autotasker/tasks
```

### 🔸 Get All Tasks
```http
GET /autotasker/tasks
```

### 🔸 Get a Single Task
```http
GET /autotasker/tasks/{id}
```

### 🔸 Update a Task
```http
PUT /autotasker/tasks/{id}
```

### 🔸 Delete a Task
```http
DELETE /autotasker/tasks/{id}
```

> ℹ️ JSON payloads and responses are fully validated using Pydantic

---

## License

This project is licensed under the BSD 3-Clause License.  
See the [LICENSE](./LICENSE) file for more details.

---

## Contributing

This project is under active development. PRs are welcome once public modules are stabilized.
---

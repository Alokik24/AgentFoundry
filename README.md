# AgentFoundry – AutoTasker Agent

**AgentFoundry** is an open-source developer platform to build, test, and deploy LLM-powered agents with memory, observability, and real-world integration.

`AutoTasker` is the first module — a task classification + automation agent built using **FastAPI**, **PostgreSQL**, and **LLM models**.

---

## Features

- FastAPI backend with async endpoints
- PostgreSQL integration via SQLAlchemy
- Modular agent design
- AutoDocs with Swagger/OpenAPI
- Scalable folder structure for multi-agent systems

---

## Folder Structure

```
agentfoundry/
├── agents/
│   └── autotasker/
│       ├── main.py         # FastAPI entrypoint
│       ├── db.py           # PostgreSQL config
│       ├── models.py       # SQLAlchemy models
│       ├── schemas.py      # Pydantic validation
│       ├── routes.py       # API routes
│       └── agent.py        # GPT logic (coming soon)
├── tests/                  # Unit tests
│   └── test_routes.py
├── .env                    # Environment variables
├── requirements.txt        # Dependencies
└── README.md
```

---

## Setup Instructions

### 1. Clone + Install
```bash
git clone https://github.com/<yourusername>/agentfoundry.git
cd agentfoundry
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Set up PostgreSQL

```bash
# On Ubuntu
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

Add `.env`:
```
DATABASE_URL=postgresql+asyncpg://af_user:password@localhost:5432/agentfoundry
```

---

## Run Server

```bash
uvicorn agents.autotasker.main:app --reload
```

Visit: http://localhost:8000/autotasker/ping


## Tech Stack

- FastAPI
- PostgreSQL + asyncpg
- Pydantic
- SQLAlchemy
- Uvicorn

---

## License

BSD 3-Clause


## Contributing

This project is in active development. PRs welcome once public milestone is reached.

from fastapi import FastAPI
from agents.autotasker.routes import router as task_router

app = FastAPI(title="Agent Foundry - AutoTasker Agent")

app.include_router(task_router, prefix="/autotasker")

@app.get("/")
async def root():
    return {"message": "Welcome to AgentFoundry"}
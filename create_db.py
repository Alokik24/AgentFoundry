
import asyncio
from agents.autotasker.db import engine
from agents.autotasker.models import Base

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_models())

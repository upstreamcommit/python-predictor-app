from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI

from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    init_db()
    yield

app = FastAPI(
    title="Predictor API",
    description="Backend API for a football prediction game.",
    version="0.1.0",
    lifespan=lifespan
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status":"ok"}
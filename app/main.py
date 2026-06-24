from fastapi import FastAPI

from app.db.base import Base
from app.db.database import engine
from app.models import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Predictor API",
    description="Backend API for a football prediction game.",
    version="0.1.0",
)



@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status":"ok"}
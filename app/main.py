from fastapi import FastAPI

app = FastAPI(
    title="Predictor API",
    description="Backend API for a football prediction game.",
    version="0.1.0",
)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status":"ok"}
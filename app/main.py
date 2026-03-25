from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "LocalEdge backend is running"}
from datetime import datetime, timezone

@app.get("/health/heartbeat")
def heartbeat():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

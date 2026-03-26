from fastapi import FastAPI
from datetime import datetime, timezone
from app.firewall import validate_command
from app.orchestrator import Orchestrator

app = FastAPI()

# Create a global orchestrator instance
orchestrator = Orchestrator()

@app.get("/")
def root():
    return {"status": "LocalEdge backend is running"}

@app.get("/health/heartbeat")
def heartbeat():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.post("/command")
def command_router(payload: dict):
    command = payload.get("command")

    validate_command(command)

    result = orchestrator.execute(command, payload)

    return {
        "status": "accepted",
        "command": command,
        "result": result
    }


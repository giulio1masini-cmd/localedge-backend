from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi import HTTPException

SAFE_COMMANDS = {
    "create_website",
    "update_website",
    "generate_voice_agent",
    "run_research",
    "send_outreach",
    "start_trial",
    "sync_business_data"
}

def validate_command(command: str):
    if command not in SAFE_COMMANDS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsafe or unknown command: {command}"
        )
    return True
app = FastAPI()

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

    return {"status": "accepted", "command": command}

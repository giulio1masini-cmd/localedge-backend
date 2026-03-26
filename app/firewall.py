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

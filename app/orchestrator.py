from app.pipelines.website import create_website, update_website
from app.pipelines.voice_agent import generate_voice_agent
from app.pipelines.research import run_research
from app.pipelines.outreach import send_outreach
from app.pipelines.trial import start_trial
from app.pipelines.sync import sync_business_data

class Orchestrator:
    def __init__(self):
        pass

    def execute(self, command: str, payload: dict):
        if command == "create_website":
            return create_website(payload)

        if command == "update_website":
            return update_website(payload)

        if command == "generate_voice_agent":
            return generate_voice_agent(payload)

        if command == "run_research":
            return run_research(payload)

        if command == "send_outreach":
            return send_outreach(payload)

        if command == "start_trial":
            return start_trial(payload)

        if command == "sync_business_data":
            return sync_business_data(payload)

        return {"error": "Unknown command"}

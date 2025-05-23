from pydantic import BaseSettings
from typing import Dict

class Settings(BaseSettings):
    # MCP Configuration
    mcp_api_key: str = ""
    mcp_model_version: str = "latest"
    mcp_endpoint: str = "https://api.mcp.example.com/v1"

    # Application Settings
    debug: bool = True
    port: int = 8000
    host: str = "0.0.0.0"

    # Grading Configuration
    default_grading_criteria: Dict[str, float] = {
        "completeness": 0.4,
        "accuracy": 0.4,
        "clarity": 0.2
    }
    max_feedback_length: int = 500

    class Config:
        env_file = ".env"
        env_prefix = ""

settings = Settings() 
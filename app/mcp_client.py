import requests
from typing import Dict, Any
from .config import settings

class MCPClient:
    def __init__(self):
        self.api_key = settings.mcp_api_key
        self.endpoint = settings.mcp_endpoint
        self.model_version = settings.mcp_model_version
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def grade_submission(self, content: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Send a submission to the MCP model for grading.
        
        Args:
            content: The submission content to grade
            context: Additional context for the grading (optional)
            
        Returns:
            Dict containing the grading results
        """
        try:
            payload = {
                "content": content,
                "context": context or {},
                "model_version": self.model_version,
                "criteria": settings.default_grading_criteria
            }

            response = requests.post(
                f"{self.endpoint}/grade",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error communicating with MCP service: {str(e)}")

mcp_client = MCPClient() 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from .mcp_client import mcp_client
from .config import settings

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Quentum Grade",
    description="A grading tool using Model Context Protocol",
    version="1.0.0"
)

class Submission(BaseModel):
    student_id: str
    content: str
    assignment_id: str
    context: Optional[dict] = None

class GradeResponse(BaseModel):
    score: float
    feedback: str
    breakdown: dict

@app.get("/")
async def root():
    return {"message": "Welcome to Quentum Grade API"}

@app.post("/grade", response_model=GradeResponse)
async def grade_submission(submission: Submission):
    try:
        # Get grading results from MCP
        grading_result = await mcp_client.grade_submission(
            content=submission.content,
            context=submission.context
        )
        
        return GradeResponse(
            score=grading_result.get("score", 0.0),
            feedback=grading_result.get("feedback", ""),
            breakdown=grading_result.get("breakdown", {
                "criteria": {},
                "suggestions": []
            })
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 
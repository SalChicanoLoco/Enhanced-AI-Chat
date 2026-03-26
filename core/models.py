from pydantic import BaseModel, Field
from typing import Optional

class JobRequest(BaseModel):
    session_id: str = Field(min_length=1, max_length=64)
    prompt: str = Field(min_length=1, max_length=10000)

class JobStatus(BaseModel):
    job_id: str
    status: str
    result: Optional[str] = None

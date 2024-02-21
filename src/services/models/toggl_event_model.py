from pydantic import BaseModel

class TogglEvent(BaseModel):
    description: str
    tags: list
    workspace_id: int
    duration: int
    start: str
    created_with: str
    pid: int
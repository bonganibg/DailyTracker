from pydantic import BaseModel

class TogglProject(BaseModel):
    id: int
    name: str
    wid: int
from pydantic import BaseModel

class TogglWorkspace(BaseModel):
        id: str
        name: str
        organization_id: str


        
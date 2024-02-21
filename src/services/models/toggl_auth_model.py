from pydantic import BaseModel

class TogglUserAuth(BaseModel):
    email: str
    password: str
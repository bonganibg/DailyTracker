from pydantic import BaseModel

# create a user class using pydantic    
class User(BaseModel):
    id: str
    hourly_rate: float
    role: str
    division: str

    
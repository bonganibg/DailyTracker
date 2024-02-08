from pydantic import BaseModel

# create a user class using pydantic    
class User(BaseModel):
    hourly_rate: float
    role: str
    division: str

    
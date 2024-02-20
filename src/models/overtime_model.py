from pydantic import BaseModel

class Overtime(BaseModel):
    user_id: str
    deliverable: str
    quantity: float
    rate: float
    unit: str
    date: str
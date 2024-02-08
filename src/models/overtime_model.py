from pydantic import BaseModel

class Overtime(BaseModel):
    user_id: str
    delivarable: str
    quantity: float
    rate: float
    unit: str
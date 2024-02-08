from pydantic import BaseModel

class Overtime(BaseModel):
    delivarable: str
    quantity: float
    rate: float
    unit: str
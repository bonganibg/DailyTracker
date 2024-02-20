from pydantic import BaseModel, Field

class HoursWorked(BaseModel):
    user_id: str
    date: str
    start_time: str
    duration: float 
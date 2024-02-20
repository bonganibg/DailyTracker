from pydantic import BaseModel, Field 

class HoursOff(BaseModel):
    user_id: str
    start_time: str
    duration: float
    date: str
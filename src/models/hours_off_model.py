import datetime
import time
from pydantic import BaseModel, Field 

class HoursOff(BaseModel):
    user_id: str
    start_time: time
    duration: float
    date: datetime
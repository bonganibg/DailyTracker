import datetime
import time
from pydantic import BaseModel, Field 

class HoursOff(BaseModel):
    start_time: time
    duration: float
    date: datetime
import datetime
import time
from pydantic import BaseModel, Field

class HourWorked(BaseModel):
    date: datetime
    start_time: time
    duration: float 
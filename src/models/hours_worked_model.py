import datetime
import time
from pydantic import BaseModel, Field

class HoursWorked(BaseModel):
    user_id: str
    date: datetime
    start_time: time
    duration: float 
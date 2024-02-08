import time
from pydantic import BaseModel, Field

class ExpectedHour(BaseModel):
    day_of_week: int
    start_time: time
    duration: int


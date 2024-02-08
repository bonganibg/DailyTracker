import time
from pydantic import BaseModel, Field

class ExpectedHour(BaseModel):
    user_id: str
    day_of_week: int
    start_time: time
    duration: int


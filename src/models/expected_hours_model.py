from pydantic import BaseModel

class ExpectedHour(BaseModel):
    user_id: str
    day_of_week: int
    start_time: str
    duration: int


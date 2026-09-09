from datetime import date

from pydantic import BaseModel

class DaySummary(BaseModel):
    date: date
    limit: int
    eaten: int
    remaining: int
    status: str
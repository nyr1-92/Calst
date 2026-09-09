from datetime import datetime

from pydantic import BaseModel

# API schema for POST

class ScanCreate(BaseModel):
    food_description: str
    estimated_calories: int
    min_calories: int
    max_calories: int
    confidence: str

# API schema for GET

class Scan(ScanCreate):
    id: int
    created_at: datetime
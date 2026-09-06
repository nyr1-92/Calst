from pydantic import BaseModel

# API schema for GET

class ScanCreate(BaseModel):
    id: int
    food_description: str
    estimated_calories: int
    min_calories: int
    max_calories: int
    confidence: str

# API schema for POST

class Scan(ScanCreate):
    id: int
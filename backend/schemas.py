from pydantic import BaseModel
from datetime import datetime

class ExpenseCreate(BaseModel):
    description: str
    amount: float

class ExpenseResponse(BaseModel):
    id: int
    description: str
    amount: float
    category: str
    created_at: datetime

    class Config:
        from_attributes = True  # for SQLAlchemy

from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class CustomerSchema(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str]
    address: Optional[str]
    date_of_birth: Optional[date]
    account_balance: Optional[float]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
